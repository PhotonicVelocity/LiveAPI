"""Swap the installed Ableton Live version from a local or remote source.

Lists available versions, copies the selected one to /Applications, and
reinstalls the MakeDoc Remote Script.

The version source can be a local directory or an SSH remote (user@host:/path).
It defaults to NAS_HOST:NAS_BASE from .env / environment.

Supported formats per version (checked in order of preference):
    {source}/{major}/Live {version}.tar       — uncompressed tar
    {source}/{major}/Live {version}.tar.gz    — gzipped tar
    {source}/{major}/Live {version}.zip       — zip archive
    {source}/{major}/{version}/{app_name}     — .app inside version dir
    {source}/{major}/{app_name}               — .app directly (single-version layout)

Usage:
    python tools/swap_live.py --list                          # list versions
    python tools/swap_live.py 12.3.5                          # install from default source
    python tools/swap_live.py 12.3.5 --source /Volumes/Live   # install from local path
    python tools/swap_live.py 12.3.5 --source user@nas:/path  # install from remote
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

# Load .env if env vars aren't already set
_env_path = os.path.join(REPO_ROOT, ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _, _v = _line.partition("=")
                os.environ.setdefault(_k.strip(), _v.strip())

# App bundle names by major version
APP_NAMES = {
    "11": "Ableton Live 11 Suite.app",
    "12": "Ableton Live 12 Suite.app",
}

APPLICATIONS = "/Applications"

# Archive extensions in order of preference
ARCHIVE_EXTS = [".tar", ".tar.gz", ".zip"]

# Pattern to extract version from archive filenames like "Live 12.3.5.tar.gz"
_ARCHIVE_RE = re.compile(r"^Live (\d+\.\d+(?:\.\d+)?)(?:" + "|".join(re.escape(e) for e in ARCHIVE_EXTS) + r")$")


def _extract_archive_versions(entries: list[str]) -> set[str]:
    """Extract version strings from archive filenames in a directory listing."""
    versions: set[str] = set()
    for name in entries:
        m = _ARCHIVE_RE.match(name)
        if m:
            versions.add(m.group(1))
    return versions


def _run(args: list[str], **kwargs) -> subprocess.CompletedProcess:
    """Run a subprocess, exiting on failure."""
    result = subprocess.run(args, **kwargs)
    if result.returncode != 0:
        cmd = os.path.basename(args[0])
        print(f"{cmd} failed (exit {result.returncode})", file=sys.stderr)
        sys.exit(1)
    return result


# ---------------------------------------------------------------------------
# Source abstraction — local vs remote
# ---------------------------------------------------------------------------

class LocalSource:
    """Read versions from a local directory."""

    def __init__(self, base: str) -> None:
        self.base = base

    def _listdir(self, path: str) -> list[str]:
        try:
            return os.listdir(path)
        except OSError as e:
            raise RuntimeError(str(e))

    def list_versions(self) -> dict[str, list[str]]:
        versions: dict[str, list[str]] = {}
        for major in self._listdir(self.base):
            major_dir = os.path.join(self.base, major)
            if not os.path.isdir(major_dir) or major not in APP_NAMES:
                continue
            entries = self._listdir(major_dir)
            # Version directories (e.g. "12.3.5/")
            vers = {d for d in entries if d[0].isdigit() and os.path.isdir(os.path.join(major_dir, d))}
            # Archive files (e.g. "Live 12.3.5.tar")
            vers |= _extract_archive_versions(entries)
            versions[major] = sorted(vers, key=lambda v: [int(x) for x in v.split(".")])
        return versions

    def _find_format(self, major: str, version: str, app_name: str) -> str | None:
        """Return the format key for the best available source, or None."""
        major_dir = os.path.join(self.base, major)
        for ext in ARCHIVE_EXTS:
            if os.path.isfile(os.path.join(major_dir, f"Live {version}{ext}")):
                return ext
        if os.path.isdir(os.path.join(major_dir, version, app_name)):
            return "app_in_version"
        if os.path.isdir(os.path.join(major_dir, app_name)):
            return "app_direct"
        return None

    def install(self, major: str, version: str, app_name: str, dest: str) -> None:
        fmt = self._find_format(major, version, app_name)
        major_dir = os.path.join(self.base, major)

        if fmt == ".tar":
            path = os.path.join(major_dir, f"Live {version}.tar")
            print(f"Extracting {path}...")
            _run(["tar", "xf", path, "-C", APPLICATIONS], timeout=300)

        elif fmt == ".tar.gz":
            path = os.path.join(major_dir, f"Live {version}.tar.gz")
            print(f"Extracting {path}...")
            _run(["tar", "xzf", path, "-C", APPLICATIONS], timeout=300)

        elif fmt == ".zip":
            path = os.path.join(major_dir, f"Live {version}.zip")
            print(f"Extracting {path}...")
            _run(["unzip", "-q", "-o", path, "-d", APPLICATIONS], timeout=300)

        elif fmt == "app_in_version":
            path = os.path.join(major_dir, version, app_name)
            print(f"Copying {path}...")
            shutil.copytree(path, dest, symlinks=True)

        elif fmt == "app_direct":
            path = os.path.join(major_dir, app_name)
            print(f"Copying {path}...")
            shutil.copytree(path, dest, symlinks=True)

        else:
            print(f"No .app, .tar, .tar.gz, or .zip found for {version}", file=sys.stderr)
            sys.exit(1)

    def describe(self, major: str, version: str, app_name: str) -> str:
        fmt = self._find_format(major, version, app_name)
        major_dir = os.path.join(self.base, major)
        if fmt in ARCHIVE_EXTS:
            return f"Extract {major_dir}/Live {version}{fmt} → {APPLICATIONS}/{app_name}"
        if fmt == "app_in_version":
            return f"Copy {major_dir}/{version}/{app_name} → {APPLICATIONS}/{app_name}"
        if fmt == "app_direct":
            return f"Copy {major_dir}/{app_name} → {APPLICATIONS}/{app_name}"
        return f"No source found for {version}"


class RemoteSource:
    """Read versions from an SSH remote (user@host:/path)."""

    def __init__(self, host: str, base: str) -> None:
        self.host = host
        self.base = base

    def _ssh(self, cmd: str, timeout: int = 15) -> str:
        result = subprocess.run(
            ["ssh", self.host, cmd],
            capture_output=True, text=True, timeout=timeout,
        )
        if result.returncode != 0:
            raise RuntimeError(f"SSH failed: {result.stderr.strip()}")
        return result.stdout.strip()

    def _remote_exists(self, path: str, flag: str = "-e") -> bool:
        """Check if a remote path exists. flag: -f for file, -d for dir, -e for either."""
        check = subprocess.run(
            ["ssh", self.host, f'test {flag} "{path}" && echo exists'],
            capture_output=True, text=True, timeout=15,
        )
        return "exists" in check.stdout

    def list_versions(self) -> dict[str, list[str]]:
        versions: dict[str, list[str]] = {}
        try:
            majors = self._ssh(f"ls {self.base}").splitlines()
        except Exception as e:
            raise RuntimeError(f"Failed to connect to remote: {e}")
        for major in majors:
            if major not in APP_NAMES:
                continue
            try:
                entries = self._ssh(f"ls {self.base}/{major}").splitlines()
                # Version directories
                vers = {d for d in entries if d[0].isdigit()}
                # Archive files
                vers |= _extract_archive_versions(entries)
                versions[major] = sorted(vers, key=lambda v: [int(x) for x in v.split(".")])
            except Exception:
                continue
        return versions

    def _find_format(self, major: str, version: str, app_name: str) -> str | None:
        """Return the format key for the best available remote source, or None."""
        base = f"{self.base}/{major}"
        for ext in ARCHIVE_EXTS:
            if self._remote_exists(f"{base}/Live {version}{ext}", "-f"):
                return ext
        if self._remote_exists(f"{base}/{version}/{app_name}", "-d"):
            return "app_in_version"
        if self._remote_exists(f"{base}/{app_name}", "-d"):
            return "app_direct"
        return None

    def _download(self, remote_path: str, local_path: str) -> None:
        """SCP a file from the remote."""
        print(f"Downloading {os.path.basename(remote_path)} from remote...")
        _run(["scp", f"{self.host}:{remote_path}", local_path], timeout=600)

    def install(self, major: str, version: str, app_name: str, dest: str) -> None:
        fmt = self._find_format(major, version, app_name)
        base = f"{self.base}/{major}"

        if fmt in (".tar", ".tar.gz", ".zip"):
            remote_path = f"{base}/Live {version}{fmt}"
            local_archive = os.path.join(tempfile.gettempdir(), f"Live {version}{fmt}")
            self._download(remote_path, local_archive)

            print(f"Extracting to {APPLICATIONS}/...")
            if fmt == ".tar":
                _run(["tar", "xf", local_archive, "-C", APPLICATIONS], timeout=300)
            elif fmt == ".tar.gz":
                _run(["tar", "xzf", local_archive, "-C", APPLICATIONS], timeout=300)
            elif fmt == ".zip":
                _run(["unzip", "-q", "-o", local_archive, "-d", APPLICATIONS], timeout=300)
            os.remove(local_archive)

        elif fmt in ("app_in_version", "app_direct"):
            if fmt == "app_in_version":
                remote_path = f"{base}/{version}/{app_name}"
            else:
                remote_path = f"{base}/{app_name}"
            print(f"Copying Live {version} from remote via rsync...")
            _run(
                ["rsync", "-a", "--progress", f"{self.host}:{remote_path}/", f"{dest}/"],
                timeout=600,
            )

        else:
            print(f"No .app, .tar, .tar.gz, or .zip found for {version} on remote", file=sys.stderr)
            sys.exit(1)

    def describe(self, major: str, version: str, app_name: str) -> str:
        fmt = self._find_format(major, version, app_name)
        base = f"{self.host}:{self.base}/{major}"
        if fmt in ARCHIVE_EXTS:
            return f"Download {base}/Live {version}{fmt} → extract to {APPLICATIONS}/{app_name}"
        if fmt == "app_in_version":
            return f"Rsync {base}/{version}/{app_name} → {APPLICATIONS}/{app_name}"
        if fmt == "app_direct":
            return f"Rsync {base}/{app_name} → {APPLICATIONS}/{app_name}"
        return f"No source found for {version} on remote"


def parse_source(source: str) -> LocalSource | RemoteSource:
    """Parse a source string into a LocalSource or RemoteSource."""
    if ":" in source and not source.startswith("/"):
        # user@host:/path or host:/path
        host, _, path = source.partition(":")
        return RemoteSource(host, path)
    return LocalSource(source)


def default_source() -> LocalSource | RemoteSource | None:
    """Build a source from NAS_HOST/NAS_BASE env vars, or return None."""
    host = os.environ.get("NAS_HOST", "")
    base = os.environ.get("NAS_BASE", "")
    if host and base:
        return RemoteSource(host, base)
    if base and os.path.isdir(base):
        return LocalSource(base)
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Swap Ableton Live version")
    parser.add_argument("version", nargs="?", help="Version to install (e.g. 12.3.5)")
    parser.add_argument("--list", action="store_true", help="List available versions")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be installed without doing it")
    parser.add_argument(
        "--source",
        help="Version source: local path or user@host:/path (default: NAS_HOST:NAS_BASE from .env)",
    )
    args = parser.parse_args()

    source = parse_source(args.source) if args.source else default_source()
    if source is None:
        print(
            "No source configured. Use --source /path or --source user@host:/path,\n"
            "or set NAS_HOST and NAS_BASE in .env",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.list or not args.version:
        try:
            versions = source.list_versions()
        except RuntimeError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
        for major in sorted(versions):
            print(f"Live {major}:")
            for v in versions[major]:
                print(f"  {v}")
        return

    try:
        versions = source.list_versions()
    except RuntimeError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    target = args.version
    major = target.split(".")[0]
    if major not in versions:
        print(f"No Live {major}.x versions found at source", file=sys.stderr)
        sys.exit(1)
    if target not in versions[major]:
        print(f"Version {target} not found. Available {major}.x versions:", file=sys.stderr)
        for v in versions[major]:
            print(f"  {v}", file=sys.stderr)
        sys.exit(1)

    app_name = APP_NAMES.get(major)
    if not app_name:
        print(f"Unknown major version: {major}", file=sys.stderr)
        sys.exit(1)

    local_app = os.path.join(APPLICATIONS, app_name)

    if args.dry_run:
        print(source.describe(major, target, app_name))
        return

    # Check Live isn't running
    pgrep = subprocess.run(["pgrep", "-x", "Live"], capture_output=True)
    if pgrep.returncode == 0:
        print("Live is still running. Quit it first.", file=sys.stderr)
        sys.exit(1)

    # Remove existing app bundle
    if os.path.exists(local_app):
        print(f"Removing {local_app}...")
        shutil.rmtree(local_app)

    source.install(major, target, app_name, local_app)
    print(f"Installed {app_name} ({target}) to {APPLICATIONS}/")

    # Reinstall MakeDoc Remote Script
    print("Reinstalling MakeDoc...")
    install = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, "install.py"), "--name", "MakeDoc"],
        cwd=SCRIPT_DIR,
    )
    if install.returncode != 0:
        print("MakeDoc install failed", file=sys.stderr)
        sys.exit(1)

    print(f"\nReady. Launch Live {target} to continue.")


if __name__ == "__main__":
    main()

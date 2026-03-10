"""
Run the full introspection pipeline: capture → probe → device probe → generate stubs.

Requires a running Ableton Live instance with MakeDoc loaded as a Control Surface.
Each phase inside Live is triggered via a tmp file and signals completion via a
corresponding marker file. The device probe is tick-driven and takes ~20 seconds;
the other phases are near-instant.

Usage:
    python tools/run_pipeline.py 11.1                  # run pipeline for Live 11.1
    python tools/run_pipeline.py 12.3.6                # run pipeline for Live 12.3.6
    python tools/run_pipeline.py 11.1 --skip-capture   # skip phase 1 (reuse existing Live.json)
    python tools/run_pipeline.py 11.2 --swap           # quit Live, swap to 11.2, open set, then run
"""

import argparse
import os
import re
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
BUILD_ROOT = os.path.join(REPO_ROOT, "build")

# App bundle names by major version
APP_NAMES = {
    "11": "Ableton Live 11 Suite.app",
    "12": "Ableton Live 12 Suite.app",
}

# Trigger files — MakeDoc watches for these and deletes them on pickup.
TRIGGERS = {
    "capture": "/tmp/makedoc_reload",
    "probe": "/tmp/makedoc_probe",
    "device_probe": "/tmp/makedoc_probe_devices",
}

# Completion markers — written by MakeDoc when each phase finishes.
MARKERS = {
    "capture": "/tmp/makedoc_capture_done",
    "probe": "/tmp/makedoc_probe_done",
    "device_probe": "/tmp/makedoc_device_probe_done",
}

SET_PROJECTS = {
    "11": os.path.join(SCRIPT_DIR, "Set 11 Project", "Set 11.als"),
    "12": os.path.join(SCRIPT_DIR, "Set 12 Project", "Set 12.als"),
}

POLL_INTERVAL = 0.5  # seconds
TIMEOUT = 120  # seconds
LAUNCH_TIMEOUT = 180  # seconds to wait for Live to boot + MakeDoc to respond


def _normalize_version(v: str) -> str:
    """Normalize a version string so '11.1' and '11.1.0' compare equal."""
    parts = v.split(".")
    # Strip trailing zeros: 11.1.0 → 11.1, but keep at least major.minor
    while len(parts) > 2 and parts[-1] == "0":
        parts.pop()
    return ".".join(parts)


def get_installed_version(target_version: str) -> str | None:
    """Read the installed Live version from the app bundle's Info.plist.

    Returns the version string (e.g. '11.1', '12.3.6') or None if the app isn't installed.
    """
    major = target_version.split(".")[0]
    app_name = APP_NAMES.get(major)
    if not app_name:
        return None
    plist = f"/Applications/{app_name}/Contents/Info.plist"
    if not os.path.exists(plist):
        return None
    try:
        result = subprocess.run(
            ["defaults", "read", plist, "CFBundleShortVersionString"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        # Format: "11.1 (2022-01-27_9922074e99)" or "12.3.6 (2024-...)"
        raw = result.stdout.strip()
        match = re.match(r"(\d+\.\d+(?:\.\d+)?)", raw)
        return match.group(1) if match else None
    except Exception:
        return None


def trigger_and_wait(phase: str, timeout: float = TIMEOUT) -> tuple[float, str]:
    """Trigger a phase and block until its completion marker appears.

    Returns (elapsed_seconds, build_dir) where build_dir is the path
    written into the marker by MakeDoc.
    """
    marker = MARKERS[phase]
    trigger = TRIGGERS[phase]

    # Clean up any stale marker from a previous run
    if os.path.exists(marker):
        os.remove(marker)

    # Write trigger file
    with open(trigger, "w") as f:
        f.write("")

    # Poll for completion
    start = time.monotonic()
    while not os.path.exists(marker):
        if time.monotonic() - start > timeout:
            print(f"  ERROR: {phase} timed out after {timeout}s", file=sys.stderr)
            sys.exit(1)
        time.sleep(POLL_INTERVAL)

    elapsed = time.monotonic() - start
    build_dir = open(marker).read().strip()
    os.remove(marker)
    return elapsed, build_dir


def _find_prefs_dir(target: str) -> str | None:
    """Find the Live preferences directory for the target version.

    Live writes to ~/Library/Preferences/Ableton/Live {x.y}/ where x.y
    matches the plist version (which may omit the patch .0).
    """
    prefs_base = os.path.expanduser("~/Library/Preferences/Ableton")
    installed = get_installed_version(target)
    if installed:
        path = os.path.join(prefs_base, f"Live {installed}")
        if os.path.isdir(path):
            return path
    # Fallback: try the target as-is
    path = os.path.join(prefs_base, f"Live {target}")
    if os.path.isdir(path):
        return path
    return None


def _find_log_path(target: str) -> str | None:
    """Find the Live log file path for the target version."""
    prefs = _find_prefs_dir(target)
    if prefs:
        path = os.path.join(prefs, "Log.txt")
        if os.path.exists(path):
            return path
    return None


def _wait_for_makedoc_ready(target: str, timeout: float):
    """Tail the Live log and wait for MakeDoc's ready message."""
    log_path = _find_log_path(target)
    if log_path is None:
        print("  Warning: Could not find Live log file, falling back to timeout", file=sys.stderr)
        time.sleep(10)
        return

    # Record current log size so we only watch new lines
    try:
        start_pos = os.path.getsize(log_path)
    except OSError:
        start_pos = 0

    start = time.monotonic()
    while time.monotonic() - start < timeout:
        try:
            with open(log_path) as f:
                f.seek(start_pos)
                new_content = f.read()
            if "MakeDoc ready" in new_content:
                return
        except OSError:
            pass
        time.sleep(POLL_INTERVAL)

    print(f"  ERROR: MakeDoc did not become ready within {timeout}s", file=sys.stderr)
    sys.exit(1)


def _swap_and_launch(target: str, major: str):
    """Quit Live, swap to the target version, and open the saved set."""
    # Check if the correct version is already installed
    installed = get_installed_version(target)
    needs_swap = installed is None or _normalize_version(installed) != _normalize_version(target)

    # Quit Live if running
    print("Quitting Live...", flush=True)
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, "quit_live.py"), "--wait"],
        timeout=60,
    )
    if result.returncode != 0:
        print("  Failed to quit Live", file=sys.stderr)
        sys.exit(1)

    # Swap version if needed
    if needs_swap:
        print(f"Swapping to Live {target}...", flush=True)
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, "swap_live.py"), target],
            timeout=600,
        )
        if result.returncode != 0:
            print("  Swap failed", file=sys.stderr)
            sys.exit(1)

    # Open the saved set in the correct app
    app_name = APP_NAMES.get(major)
    if not app_name:
        print(f"ERROR: Unknown major version: {major}", file=sys.stderr)
        sys.exit(1)

    set_project = SET_PROJECTS.get(major)
    if not set_project or not os.path.exists(set_project):
        print(f"ERROR: Set project not found for Live {major}", file=sys.stderr)
        sys.exit(1)

    print(f"Opening Set.als in {app_name}...", flush=True)
    subprocess.run(["open", "-a", app_name, set_project])

    print("  Waiting for MakeDoc to initialize...", flush=True)
    _wait_for_makedoc_ready(target, LAUNCH_TIMEOUT)
    print("  Live is ready")


def main():
    parser = argparse.ArgumentParser(description="Run the full MakeDoc introspection pipeline")
    parser.add_argument("version", help="Live version to run against (e.g. 11.1, 12.3.6)")
    parser.add_argument("--skip-capture", action="store_true", help="Skip phase 1 (reuse existing Live.json)")
    parser.add_argument("--swap", action="store_true", help="Quit Live, swap to the target version, and relaunch")
    parser.add_argument("--timeout", type=float, default=TIMEOUT, help=f"Per-phase timeout in seconds (default {TIMEOUT})")
    args = parser.parse_args()

    target = args.version
    major = target.split(".")[0]

    if args.swap:
        _swap_and_launch(target, major)
    else:
        # Verify the correct Live version is installed
        installed = get_installed_version(target)
        if installed is None:
            app_name = APP_NAMES.get(major, f"Ableton Live {major} Suite.app")
            print(f"ERROR: {app_name} not found in /Applications", file=sys.stderr)
            sys.exit(1)
        if _normalize_version(installed) != _normalize_version(target):
            print(
                f"ERROR: Installed Live version is {installed}, expected {target}.\n"
                f"  Use 'python tools/swap_live.py {target}' to install the correct version,\n"
                f"  or pass --swap to do it automatically.",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"Running pipeline for Live {target}")

    # Clear stale markers and triggers from previous runs
    for path in list(MARKERS.values()) + list(TRIGGERS.values()):
        if os.path.exists(path):
            os.remove(path)

    # --- Phase 1: Capture ---
    if not args.skip_capture:
        print("Phase 1/4: Capture (Live.json)...", flush=True)
        elapsed, _ = trigger_and_wait("capture", timeout=args.timeout)
        print(f"  Done ({elapsed:.1f}s)")
    else:
        print("Phase 1/4: Capture — skipped")

    # --- Phase 2: Property probe ---
    print("Phase 2/4: Property probe...", flush=True)
    elapsed, _ = trigger_and_wait("probe", timeout=args.timeout)
    print(f"  Done ({elapsed:.1f}s)")

    # --- Phase 3: Device probe ---
    print("Phase 3/4: Device probe...", flush=True)
    elapsed, _ = trigger_and_wait("device_probe", timeout=args.timeout)
    print(f"  Done ({elapsed:.1f}s)")

    # MakeDoc reports the full version (e.g. 11.1.0) which becomes the build dir name.
    # The target may use a shorter form (11.1), so find the matching build dir.
    build_dir = os.path.join(BUILD_ROOT, target)
    if not os.path.isdir(build_dir):
        # Look for a dir whose normalized version matches (e.g. 11.1 matches 11.1.0/)
        for d in os.listdir(BUILD_ROOT):
            if _normalize_version(d) == _normalize_version(target):
                build_dir = os.path.join(BUILD_ROOT, d)
                break
        else:
            print(f"ERROR: Build directory not found for version {target}", file=sys.stderr)
            sys.exit(1)

    version = os.path.basename(build_dir)

    json_file = os.path.join(build_dir, "Live.json")
    if not os.path.exists(json_file):
        print(f"ERROR: {json_file} not found — did capture run?", file=sys.stderr)
        sys.exit(1)

    print(f"Phase 4/4: Generate stubs ({version})...", flush=True)
    start = time.monotonic()

    sys.path.insert(0, os.path.join(SCRIPT_DIR, "introspection"))
    from generators.StubGenerator import StubGenerator

    generator = StubGenerator(build_dir, version=version)
    generator.generate()

    elapsed = time.monotonic() - start
    stubs_dir = os.path.join(build_dir, "Live")
    print(f"  Done ({elapsed:.1f}s)")

    # --- Summary ---
    probe_path = os.path.join(build_dir, "probe_results.json")
    summary = ""
    if os.path.exists(probe_path):
        import json

        with open(probe_path) as f:
            data = json.load(f)
        total = typed = 0
        for cls in data.values():
            for v in cls.get("properties", {}).values():
                total += 1
                if v.get("runtime_type"):
                    typed += 1
        summary = f"  Properties typed: {typed}/{total} ({100 * typed / total:.1f}%)\n"

    print(f"\nPipeline complete for Live {version}")
    print(f"  Build dir: {build_dir}")
    if summary:
        print(summary, end="")
    print(f"  Stubs: {stubs_dir}/")


if __name__ == "__main__":
    main()

"""Run the full stub generation pipeline (Stages 1 + 2 + 3).

Stage 1 (Capture + Probe) runs inside a live Ableton Live instance with APICapture
loaded as a Control Surface. Phases are triggered via files in /tmp/ and completion
is detected via marker files written by APICapture.

Stages 2 + 3 run outside Live: parse, refine, and generate .pyi stubs.

Requires:
  - A running Ableton Live instance with APICapture loaded (or use --swap to launch one)
  - ANTHROPIC_API_KEY in the environment or in .env for the LLM step

Usage:
    python tools/run_pipeline.py 12.3.6
    python tools/run_pipeline.py 12.3.6 --swap                # quit Live, swap version, relaunch
    python tools/run_pipeline.py 12.3.6 --skip-capture        # skip Stage 1, reuse existing raw data
    python tools/run_pipeline.py 12.3.6 --skip-llm            # stop before LLM step
    python tools/run_pipeline.py 12.3.6 --skip-generate       # stop before stub generation
    python tools/run_pipeline.py 12.3.6 --model claude-opus-4-20250514
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
from os.path import dirname, exists, join

REPO_ROOT = dirname(dirname(__file__))
TOOLS_DIR = dirname(__file__)


def _load_dotenv() -> None:
    """Load .env from the repo root into os.environ (skips existing vars)."""
    env_path = join(REPO_ROOT, ".env")
    if not exists(env_path):
        return
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("'\"")
            if key and key not in os.environ:
                os.environ[key] = value


_load_dotenv()

# --- Stage 1 constants ---

APP_NAMES = {
    "11": "Ableton Live 11 Suite.app",
    "12": "Ableton Live 12 Suite.app",
}

SET_PROJECTS = {
    "11": join(TOOLS_DIR, "sets", "Set 11 Project", "Set 11.als"),
    "12": join(TOOLS_DIR, "sets", "Set 12 Project", "Set 12.als"),
}

# Trigger files — APICapture watches for these and deletes them on pickup.
TRIGGERS = {
    "capture": "/tmp/apicapture_capture",
    "full_probe": "/tmp/apicapture_full_probe",
    "run": "/tmp/apicapture_run",
}

# Completion markers — written by APICapture when each phase finishes.
MARKERS = {
    "capture": "/tmp/apicapture_capture_done",
    "probe": "/tmp/apicapture_probe_done",
}

POLL_INTERVAL = 0.5  # seconds
CAPTURE_TIMEOUT = 120  # seconds
LAUNCH_TIMEOUT = 180  # seconds to wait for Live to boot + APICapture to respond


# --- Stage 1 helpers ---


def _normalize_version(v: str) -> str:
    """Normalize a version string so '11.1' and '11.1.0' compare equal."""
    parts = v.split(".")
    while len(parts) > 2 and parts[-1] == "0":
        parts.pop()
    return ".".join(parts)


def _get_installed_version(target: str) -> str | None:
    """Read the installed Live version from the app bundle's Info.plist."""
    major = target.split(".")[0]
    app_name = APP_NAMES.get(major)
    if not app_name:
        return None
    plist = f"/Applications/{app_name}/Contents/Info.plist"
    if not exists(plist):
        return None
    try:
        result = subprocess.run(
            ["defaults", "read", plist, "CFBundleShortVersionString"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        raw = result.stdout.strip()
        match = re.match(r"(\d+\.\d+(?:\.\d+)?)", raw)
        return match.group(1) if match else None
    except Exception:
        return None


def _find_log_path(target: str) -> str | None:
    """Find the Live log file for the target version."""
    prefs_base = os.path.expanduser("~/Library/Preferences/Ableton")
    for version_str in [target, _get_installed_version(target)]:
        if version_str:
            path = join(prefs_base, f"Live {version_str}", "Log.txt")
            if exists(path):
                return path
    return None


def _wait_for_apicapture_ready(target: str, timeout: float) -> None:
    """Tail the Live log and wait for APICapture's ready message."""
    log_path = _find_log_path(target)
    if log_path is None:
        print("  Warning: Could not find Live log file, falling back to fixed wait", file=sys.stderr)
        time.sleep(10)
        return

    try:
        start_pos = os.path.getsize(log_path)
    except OSError:
        start_pos = 0

    start = time.monotonic()
    while time.monotonic() - start < timeout:
        try:
            with open(log_path) as f:
                f.seek(start_pos)
                if "APICapture ready" in f.read():
                    return
        except OSError:
            pass
        time.sleep(POLL_INTERVAL)

    print(f"  ERROR: APICapture did not become ready within {timeout}s", file=sys.stderr)
    sys.exit(1)


def _swap_and_launch(target: str) -> None:
    """Quit Live, swap to the target version, and open the saved set."""
    major = target.split(".")[0]
    installed = _get_installed_version(target)
    needs_swap = installed is None or _normalize_version(installed) != _normalize_version(target)

    # Quit Live if running
    print("Quitting Live...", flush=True)
    result = subprocess.run(
        [sys.executable, join(TOOLS_DIR, "other", "quit_live.py"), "--wait"],
        timeout=60,
    )
    if result.returncode != 0:
        print("  Failed to quit Live", file=sys.stderr)
        sys.exit(1)

    if needs_swap:
        print(f"Swapping to Live {target}...", flush=True)
        result = subprocess.run(
            [sys.executable, join(TOOLS_DIR, "other", "swap_live.py"), target],
            timeout=600,
        )
        if result.returncode != 0:
            print("  Swap failed", file=sys.stderr)
            sys.exit(1)

    app_name = APP_NAMES.get(major)
    if not app_name:
        print(f"ERROR: Unknown major version: {major}", file=sys.stderr)
        sys.exit(1)

    set_project = SET_PROJECTS.get(major)
    if not set_project or not exists(set_project):
        print(f"ERROR: Set project not found for Live {major}", file=sys.stderr)
        sys.exit(1)

    print(f"Opening Set.als in {app_name}...", flush=True)
    subprocess.run(["open", "-a", app_name, set_project])

    print("  Waiting for APICapture to initialize...", flush=True)
    _wait_for_apicapture_ready(target, LAUNCH_TIMEOUT)
    print("  Live is ready")


def _trigger_and_wait(trigger: str, marker: str, timeout: float) -> float:
    """Write a trigger file and block until the completion marker appears.

    Returns elapsed seconds.
    """
    # Clean up stale marker
    if exists(marker):
        os.remove(marker)

    # Write trigger
    with open(trigger, "w") as f:
        f.write("")

    start = time.monotonic()
    while not exists(marker):
        if time.monotonic() - start > timeout:
            print(f"  ERROR: timed out after {timeout}s waiting for {marker}", file=sys.stderr)
            sys.exit(1)
        time.sleep(POLL_INTERVAL)

    elapsed = time.monotonic() - start
    os.remove(marker)
    return elapsed


def _clear_stale_triggers() -> None:
    """Remove any stale trigger/marker files from previous runs."""
    for path in list(TRIGGERS.values()) + list(MARKERS.values()):
        if exists(path):
            os.remove(path)


# --- Stage 2/3 helper ---


def _run(args: list[str], label: str) -> None:
    """Run a subprocess, printing the label and aborting on failure."""
    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print(f"{'=' * 60}\n")
    result = subprocess.run([sys.executable, *args], cwd=REPO_ROOT)
    if result.returncode != 0:
        print(f"\nFailed at: {label}", file=sys.stderr)
        sys.exit(result.returncode)


# --- Main ---


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the full stub generation pipeline (Stages 1 + 2 + 3)")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--swap", action="store_true", help="Quit Live, swap to target version, and relaunch")
    parser.add_argument("--skip-capture", action="store_true", help="Skip Stage 1 (reuse existing raw data)")
    parser.add_argument("--skip-llm", action="store_true", help="Stop before the LLM resolution step")
    parser.add_argument("--skip-generate", action="store_true", help="Stop before stub generation")
    parser.add_argument("--model", help="Claude model to use for LLM step", default=None)
    parser.add_argument("--timeout", type=float, default=CAPTURE_TIMEOUT,
                        help=f"Stage 1 per-phase timeout in seconds (default {CAPTURE_TIMEOUT})")
    args = parser.parse_args()

    v = args.version
    pipeline = join("stubs", v, "pipeline")

    # --- Stage 1: Capture + Probe (inside Live) ---

    if not args.skip_capture:
        if args.swap:
            _swap_and_launch(v)
        else:
            installed = _get_installed_version(v)
            if installed is None:
                major = v.split(".")[0]
                app_name = APP_NAMES.get(major, f"Ableton Live {major} Suite.app")
                print(f"ERROR: {app_name} not found in /Applications", file=sys.stderr)
                sys.exit(1)
            if _normalize_version(installed) != _normalize_version(v):
                print(
                    f"ERROR: Installed Live is {installed}, expected {v}.\n"
                    f"  Pass --swap to swap automatically, or run tools/other/swap_live.py {v}",
                    file=sys.stderr,
                )
                sys.exit(1)

        _clear_stale_triggers()

        print("\n--- Stage 1: Capture + Probe (inside Live) ---\n")

        # Use apicapture_run trigger which does capture + full probe in one go
        print("Triggering capture + full probe...", flush=True)
        elapsed = _trigger_and_wait(TRIGGERS["run"], MARKERS["capture"], timeout=args.timeout)
        print(f"  Capture done ({elapsed:.1f}s)")

        elapsed = _trigger_and_wait(TRIGGERS["run"], MARKERS["probe"], timeout=args.timeout)
        print(f"  Probe done ({elapsed:.1f}s)")

        # Verify output files exist
        raw_tree = join(pipeline, "LiveTree.raw.json")
        classes = join(pipeline, "LiveClasses.json")
        if not exists(join(REPO_ROOT, raw_tree)):
            print(f"ERROR: {raw_tree} not found after capture", file=sys.stderr)
            sys.exit(1)
        if not exists(join(REPO_ROOT, classes)):
            print(f"ERROR: {classes} not found after probe", file=sys.stderr)
            sys.exit(1)

        print(f"\n  Stage 1 complete: {raw_tree}, {classes}")
    else:
        print("\n--- Stage 1: Capture + Probe — skipped ---")

    # --- Stage 2: Parse & Refine ---

    parse_args = ["tools/parse/run_parse_pipeline.py", v]
    if args.skip_llm:
        parse_args.append("--skip-llm")
    if args.model:
        parse_args.extend(["--model", args.model])
    _run(parse_args, "Stage 2: Parse & refine")

    if args.skip_generate:
        print("\n--skip-generate: stopping before stub generation.")
        return

    # --- Stage 3: Generate ---

    _run(["tools/generate/generate_stubs.py", v],
         "Stage 3: Generate stubs")

    print(f"\nPipeline complete. Stubs at stubs/{v}/Live/")


if __name__ == "__main__":
    main()

"""
Run the full introspection pipeline: capture → probe → device probe → generate stubs.

Requires a running Ableton Live instance with MakeDoc loaded as a Control Surface.
Each phase inside Live is triggered via a tmp file and signals completion via a
corresponding marker file. The device probe is tick-driven and takes ~20 seconds;
the other phases are near-instant.

Usage:
    python tools/run_pipeline.py                 # auto-detect version from latest build dir
    python tools/run_pipeline.py --version 12.3.6
    python tools/run_pipeline.py --skip-capture   # skip phase 1 (reuse existing Live.json)
"""

import argparse
import os
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
BUILD_ROOT = os.path.join(REPO_ROOT, "build")

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

POLL_INTERVAL = 0.5  # seconds
TIMEOUT = 120  # seconds


def trigger_and_wait(phase: str, timeout: float = TIMEOUT):
    """Trigger a phase and block until its completion marker appears."""
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
    os.remove(marker)
    return elapsed


def detect_version() -> str:
    """Return the latest version directory name under build/."""
    if not os.path.isdir(BUILD_ROOT):
        return ""
    versions = sorted(
        (d for d in os.listdir(BUILD_ROOT) if os.path.isdir(os.path.join(BUILD_ROOT, d))),
        reverse=True,
    )
    return versions[0] if versions else ""


def main():
    parser = argparse.ArgumentParser(description="Run the full MakeDoc introspection pipeline")
    parser.add_argument("--version", help="Live version string (e.g. 12.3.6). Auto-detected if omitted.")
    parser.add_argument("--skip-capture", action="store_true", help="Skip phase 1 (reuse existing Live.json)")
    parser.add_argument("--timeout", type=float, default=TIMEOUT, help=f"Per-phase timeout in seconds (default {TIMEOUT})")
    args = parser.parse_args()

    # --- Phase 1: Capture ---
    if not args.skip_capture:
        print("Phase 1/4: Capture (Live.json)...", flush=True)
        elapsed = trigger_and_wait("capture", timeout=args.timeout)
        print(f"  Done ({elapsed:.1f}s)")
    else:
        print("Phase 1/4: Capture — skipped")

    # --- Phase 2: Property probe ---
    print("Phase 2/4: Property probe...", flush=True)
    elapsed = trigger_and_wait("probe", timeout=args.timeout)
    print(f"  Done ({elapsed:.1f}s)")

    # --- Phase 3: Device probe ---
    print("Phase 3/4: Device probe...", flush=True)
    elapsed = trigger_and_wait("device_probe", timeout=args.timeout)
    print(f"  Done ({elapsed:.1f}s)")

    # --- Phase 4: Stub generation (offline) ---
    version = args.version or detect_version()
    if not version:
        print("ERROR: No build directory found and --version not specified", file=sys.stderr)
        sys.exit(1)

    build_dir = os.path.join(BUILD_ROOT, version)
    if not os.path.isdir(build_dir):
        print(f"ERROR: {build_dir} does not exist", file=sys.stderr)
        sys.exit(1)

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

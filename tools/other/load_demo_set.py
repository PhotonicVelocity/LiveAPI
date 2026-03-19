"""Load the Ableton Live Demo Set via the Help menu.

Uses AppleScript to navigate Help > Load Demo Set, dismissing the Save dialog
if it appears. Waits for APICapture to signal ready via /tmp/apicapture_ready.

Usage:
    python tools/other/load_demo_set.py
    python tools/other/load_demo_set.py --no-wait
"""

import argparse
import os
import subprocess
import sys
import time

READY_FILE = "/tmp/apicapture_ready"


def load_demo_set() -> None:
    """Click Help > Load Demo Set via AppleScript, dismissing the Save dialog if it appears."""
    # Remove ready file before triggering so we can detect the new one
    try:
        os.remove(READY_FILE)
    except FileNotFoundError:
        pass

    script = """
    tell application "Ableton Live 12 Suite"
        activate
    end tell
    delay 0.5
    tell application "System Events"
        tell process "Live"
            click menu item "Load Demo Set" of menu "Help" of menu bar 1
            delay 0.5
            -- Live uses a custom dialog (AXGroup), not a native sheet.
            -- The "Don't Save" button uses a curly apostrophe (U+2019).
            try
                set grp to group 1 of window 1
                repeat with b in (every button of grp)
                    if description of b starts with "Don" and description of b ends with "t Save" then
                        click b
                        exit repeat
                    end if
                end repeat
            end try
        end tell
    end tell
    """
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"AppleScript error: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    print("Load Demo Set triggered.")


def wait_for_ready(timeout: int = 30) -> None:
    """Wait for APICapture to signal ready via /tmp/apicapture_ready."""
    start = time.monotonic()
    while time.monotonic() - start < timeout:
        if os.path.exists(READY_FILE):
            elapsed = time.monotonic() - start
            print(f"Demo set loaded ({elapsed:.1f}s)")
            return
        time.sleep(0.5)

    print(f"Timed out after {timeout}s waiting for demo set to load", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Load the Ableton Live Demo Set")
    parser.add_argument("--no-wait", action="store_true", help="Don't wait for the set to finish loading")
    args = parser.parse_args()

    load_demo_set()

    if not args.no_wait:
        wait_for_ready()


if __name__ == "__main__":
    main()

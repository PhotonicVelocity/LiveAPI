"""Quit Ableton Live via AppleScript, dismissing the save dialog if it appears.

Usage:
    python tools/quit_live.py
    python tools/quit_live.py --wait    # block until the process exits
"""

import argparse
import subprocess
import sys
import time

APPLESCRIPT = """
tell application "System Events"
    if not (exists process "Live") then
        return "not_running"
    end if
    tell process "Live"
        -- Use the menu bar to quit (more reliable than keystroke)
        click menu item "Quit Live" of menu "Live" of menu bar 1
        -- If the set is dirty, Live shows a save dialog before quitting.
        -- Live uses a custom dialog (AXGroup), not a native sheet.
        -- The button description uses a curly apostrophe (U+2019).
        repeat 10 times
            delay 0.5
            try
                set grp to group 1 of window 1
                repeat with b in (every button of grp)
                    if description of b starts with "Don" and description of b ends with "t Save" then
                        click b
                        return "quit"
                    end if
                end repeat
            end try
        end repeat
        -- No dialog appeared — set was clean, quit is proceeding.
        return "quit"
    end tell
end tell
"""


def is_live_running() -> bool:
    result = subprocess.run(["pgrep", "-x", "Live"], capture_output=True)
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Quit Ableton Live, dismissing save dialog")
    parser.add_argument("--wait", action="store_true", help="Block until Live has fully exited")
    args = parser.parse_args()

    if not is_live_running():
        print("Live is not running.")
        return

    result = subprocess.run(["osascript", "-e", APPLESCRIPT], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"AppleScript failed: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    output = result.stdout.strip()
    if output == "not_running":
        print("Live is not running.")
        return

    print("Quit signal sent.")

    if args.wait:
        timeout = 30
        start = time.monotonic()
        while is_live_running():
            if time.monotonic() - start > timeout:
                print(f"Live did not exit within {timeout}s", file=sys.stderr)
                sys.exit(1)
            time.sleep(0.5)
        print("Live has exited.")


if __name__ == "__main__":
    main()

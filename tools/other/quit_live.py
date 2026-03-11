"""Force-quit Ableton Live.

WARNING: This kills the Live process immediately. Any unsaved changes will be lost.
Only use this with the APICapture pipeline — never with real sets open.

Usage:
    python tools/quit_live.py
    python tools/quit_live.py --wait    # block until the process exits
"""

import argparse
import subprocess
import sys
import time


def is_live_running() -> bool:
    result = subprocess.run(["pgrep", "-x", "Live"], capture_output=True)
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Force-quit Ableton Live (unsaved changes will be lost)")
    parser.add_argument("--wait", action="store_true", help="Block until Live has fully exited")
    args = parser.parse_args()

    if not is_live_running():
        print("Live is not running.")
        return

    subprocess.run(["pkill", "-x", "Live"])
    print("Kill signal sent.")

    if args.wait:
        timeout = 15
        start = time.monotonic()
        while is_live_running():
            if time.monotonic() - start > timeout:
                print(f"Live did not exit within {timeout}s", file=sys.stderr)
                sys.exit(1)
            time.sleep(0.5)
        print("Live has exited.")


if __name__ == "__main__":
    main()

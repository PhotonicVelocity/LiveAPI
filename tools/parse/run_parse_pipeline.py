"""Run Stage 2: parse raw capture into a structured tree.

Stage 2 is intentionally minimal — capture → parse → generate. The previous
LLM-resolve, callsite-resolve, and apply-refinements steps were stripped per
doc/decisions.md (see "Stub Accuracy and Pipeline Posture"). Helper scripts
remain in this directory but are no longer wired into the active pipeline;
they may be re-introduced in later cleanup steps.

Usage:
    python tools/parse/run_parse_pipeline.py 12.3.6
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from os.path import dirname

REPO_ROOT = dirname(dirname(dirname(__file__)))


def run(args: list[str], label: str) -> None:
    """Run a subprocess, printing the label and aborting on failure."""
    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print(f"{'=' * 60}\n")
    result = subprocess.run([sys.executable, *args], cwd=REPO_ROOT)
    if result.returncode != 0:
        print(f"\nFailed at: {label}", file=sys.stderr)
        sys.exit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Stage 2: parse raw capture")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    args = parser.parse_args()

    run(
        ["tools/parse/parse_apicapture_results.py", args.version],
        "Stage 2: Parse raw capture",
    )

    print(f"\nStage 2 complete. Parsed tree at stubs/{args.version}/pipeline/LiveTree.parsed.json")


if __name__ == "__main__":
    main()

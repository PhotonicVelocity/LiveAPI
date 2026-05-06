"""Run Stage 2: parse raw capture into a structured tree, then apply manual refinements.

Stage 2 is intentionally minimal:
  1. parse_apicapture_results.py — raw capture → LiveTree.parsed.json
  2. apply_manual_refinements.py — reads LiveTree.parsed.json, applies overrides
     from tools/parse/manual_refinements.yaml, writes LiveTree.refined.json.
     The parsed tree is preserved untouched so drift detection on the `from:`
     field of each refinement compares against fresh-parse output, not a prior
     run's apply state. See doc/decisions.md for the refinement contract.

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
    parser = argparse.ArgumentParser(description="Run Stage 2: parse raw capture and apply manual refinements")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--skip-refinements", action="store_true", help="Skip the manual_refinements.yaml step")
    args = parser.parse_args()

    run(
        ["tools/parse/parse_apicapture_results.py", args.version],
        "Stage 2a: Parse raw capture",
    )

    if not args.skip_refinements:
        run(
            ["tools/parse/apply_manual_refinements.py", args.version, "--quiet"],
            "Stage 2b: Apply manual refinements",
        )

    pipeline_dir = f"stubs/{args.version}/pipeline"
    if args.skip_refinements:
        print(f"\nStage 2 complete. Parsed tree at {pipeline_dir}/LiveTree.parsed.json (refinements skipped)")
    else:
        print(
            f"\nStage 2 complete. Parsed tree at {pipeline_dir}/LiveTree.parsed.json; "
            f"refined tree at {pipeline_dir}/LiveTree.refined.json"
        )


if __name__ == "__main__":
    main()

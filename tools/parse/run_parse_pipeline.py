"""Run Stage 2: parse the raw capture and build the per-module LOM YAML seed.

Stage 2 has two steps now that the JSON-layer refinement pipeline has been
retired in favor of `stubs/<v>/lom/*.yaml` as the curated SOT:

  1. parse_apicapture_results_v2.py  — raw capture → LiveTree.parsed.v2.json
  2. build_lom_yaml.py               — parsed tree → stubs/<v>/reports/seed/*.yaml

The seed YAMLs are the algorithmic baseline. The hand-curated SOT lives in
`stubs/<v>/lom/` and is regenerated from the seed only at intentional sync
points (i.e. it does not flow automatically through this pipeline).

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
    parser = argparse.ArgumentParser(description="Run Stage 2: parse raw capture and build LOM YAML seed")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    args = parser.parse_args()

    run(
        ["tools/parse/parse_apicapture_results_v2.py", args.version],
        "Stage 2a: Parse raw capture",
    )

    run(
        ["tools/parse/build_lom_yaml.py", args.version],
        "Stage 2b: Build LOM YAML seed",
    )

    print(
        f"\nStage 2 complete. Parsed tree at stubs/{args.version}/pipeline/LiveTree.parsed.v2.json; "
        f"seed YAMLs at stubs/{args.version}/reports/seed/"
    )


if __name__ == "__main__":
    main()

"""Run Stage 2: parse raw capture data and resolve types/names.

Orchestrates all parse/refine steps in sequence. Requires ANTHROPIC_API_KEY
in the environment (or in .env) for the LLM step.

Usage:
    python tools/parse/run_parse_pipeline.py 12.3.6
    python tools/parse/run_parse_pipeline.py 12.3.6 --skip-llm   # stop before LLM step
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from os.path import dirname, join

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
    parser = argparse.ArgumentParser(description="Run Stage 2: parse and resolve")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--skip-llm", action="store_true", help="Stop before the LLM resolution step")
    parser.add_argument("--model", help="Claude model to use for LLM step", default=None)
    args = parser.parse_args()

    v = args.version
    pipeline = join("stubs", v, "pipeline")

    # 1. Parse raw capture into structured tree
    run(["tools/parse/parse_apicapture_results.py", v],
        "Step 1: Parse raw capture")

    # 2. Extract unresolved items from parsed tree
    run(["tools/parse/extract_unresolved.py", v],
        "Step 2: Extract unresolved items")

    # 3. Deterministic name resolution from decompiled Remote Scripts
    callsite_out = join(pipeline, "refinements.callsite.json")
    run(["tools/parse/callsite_resolve.py", v, "--pretty", "-o", callsite_out],
        "Step 3: Call-site resolution")

    # 4. Apply callsite refinements → intermediate tree
    callsite_tree = join(pipeline, "LiveTree.callsite_resolved.json")
    run(["tools/parse/apply_refinements.py", v,
         "--refinements", callsite_out,
         "--output", callsite_tree],
        "Step 4: Apply callsite refinements")

    # 5. Re-extract remaining unresolved items
    remaining = join(pipeline, "unresolved.remaining.json")
    run(["tools/parse/extract_unresolved.py", v,
         "--input", callsite_tree,
         "--output", remaining],
        "Step 5: Re-extract remaining unresolved items")

    if args.skip_llm:
        print(f"\n--skip-llm: stopping before LLM step. Remaining items in {remaining}")
        return

    # 6. LLM-assisted resolution
    llm_args = ["tools/parse/llm_resolve.py", v, "--input", remaining]
    if args.model:
        llm_args.extend(["--model", args.model])
    run(llm_args, "Step 6: LLM resolution")

    # 7. Apply LLM refinements → final resolved tree
    resolved_tree = join(pipeline, "LiveTree.resolved.json")
    run(["tools/parse/apply_refinements.py", v,
         "--input", callsite_tree,
         "--refinements", join(pipeline, "refinements.llm.json"),
         "--output", resolved_tree],
        "Step 7: Apply LLM refinements")

    print(f"\nStage 2 complete. Resolved tree at {resolved_tree}")


if __name__ == "__main__":
    main()

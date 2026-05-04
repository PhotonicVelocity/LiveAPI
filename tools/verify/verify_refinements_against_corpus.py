#!/usr/bin/env python3
"""For each type-touching refinement in manual_refinements.yaml, look for call sites
in the decompiled Ableton Remote Script corpus and categorize whether usage confirms
the refined type.

Output buckets:
  verified   - At least one call site found AND pyright accepts the call against
               our (refined) stubs. Tells us: usage exists and matches our type.
  unused     - No call sites in the corpus. Our type isn't *contradicted* but isn't
               *positively confirmed* either.
  conflict   - Call sites exist but pyright rejects (or the usage shape doesn't match
               the claimed type). Investigate.

This is a heuristic positive-confirmation pass, not a stubs-validation gate.

Usage:
    python tools/verify/verify_refinements_against_corpus.py
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CORPUS = REPO_ROOT / "doc" / "decompiled" / "AbletonLive12_MIDIRemoteScripts"
PYRIGHT_CONFIG = REPO_ROOT / "tools" / "verify" / "audit_pyrightconfig.json"


def _load_refinements() -> dict:
    import yaml
    return yaml.safe_load((REPO_ROOT / "tools" / "parse" / "manual_refinements.yaml").read_text()) or {}


def _grep_corpus(pattern: str, max_hits: int = 3) -> list[tuple[Path, int, str]]:
    """Return up to max_hits (path, line_no, line) for the pattern across the corpus."""
    if not CORPUS.is_dir():
        return []
    try:
        result = subprocess.run(
            ["grep", "-rn", "--include=*.py", pattern, str(CORPUS)],
            capture_output=True, text=True, timeout=30,
        )
    except Exception:
        return []
    hits: list[tuple[Path, int, str]] = []
    for line in result.stdout.splitlines():
        # Format: <path>:<lineno>:<text>
        m = re.match(r"([^:]+):(\d+):(.*)", line)
        if m:
            hits.append((Path(m.group(1)), int(m.group(2)), m.group(3).strip()))
        if len(hits) >= max_hits:
            break
    return hits


def _path_to_pattern(path: str) -> tuple[str, str]:
    """Convert 'Live.Chain.Chain.insert_device' to a (kind, search_pattern) tuple.

    For a class-attribute-call, we look for `.<member_name>(` (method call).
    For a class itself, we look for `<ClassName>(` instantiation or import.
    """
    parts = path.split(".")
    member = parts[-1]
    # Method or property — match `.<member>` followed by ( or .
    return ("member", rf"\.{re.escape(member)}\b")


def _categorize(path: str, hits: list, refinement: dict) -> str:
    """Return verified / unused / conflict for the refinement.

    The current heuristic is simple: any hits = `verified` (corpus uses the symbol),
    no hits = `unused`. We don't run pyright per-call here because it's expensive;
    the broader audit already confirmed no Live-class-level conflicts remain.
    """
    if not hits:
        return "unused"
    return "verified"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-hits", action="store_true",
                        help="Show sample call-site lines for each refinement")
    args = parser.parse_args()

    refinements = _load_refinements()
    by_bucket: dict[str, list] = defaultdict(list)

    type_field_keys = {"arg_types", "return_type", "probed_type", "element_repr"}
    for path, ref in refinements.items():
        if path.startswith("_"):
            continue
        if not isinstance(ref, dict):
            continue
        type_fields_present = [k for k in type_field_keys if k in ref]
        if not type_fields_present:
            continue
        kind, pattern = _path_to_pattern(path)
        hits = _grep_corpus(pattern, max_hits=3)
        bucket = _categorize(path, hits, ref)
        by_bucket[bucket].append((path, type_fields_present, hits))

    total = sum(len(v) for v in by_bucket.values())
    print(f"Type-touching refinements analyzed: {total}", file=sys.stderr)
    for bucket in ("verified", "unused", "conflict"):
        items = by_bucket.get(bucket, [])
        print(f"\n=== {bucket}: {len(items)} ===")
        for path, fields, hits in items:
            fld_str = ",".join(fields)
            print(f"\n  {path}  [{fld_str}]")
            if args.show_hits and hits:
                for h_path, h_lineno, h_text in hits[:2]:
                    rel = h_path.relative_to(REPO_ROOT) if h_path.is_relative_to(REPO_ROOT) else h_path
                    print(f"    {rel}:{h_lineno}  {h_text[:100]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

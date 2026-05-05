#!/usr/bin/env python3
"""For each type-touching refinement, gather evidence from sibling codebases.

Searches:
  - PythonForLive typed wrappers (~/dev/PythonForLive/src/pythonforlive/typing/)
  - LiveRelay client (~/dev/LiveRelay/clients/python/src/liverelay/)
  - LiveAPI curated baseline (doc/live-api/)
  - LiveAPI decompiled corpus (doc/decompiled/)
  - LiveAPI M4L docs (doc/max-for-live-docs/9.0/)

Output is a Markdown report with per-entry findings, intended for a manual review
pass where confidence flags get updated and follow-up items recorded.

Usage:
    python tools/parse/research_refinements.py > /tmp/refinement_research.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Search roots — only the dirs that exist on this machine are used.
#
# P4L source (typed wrappers) is intentionally NOT a "verification" source — its
# types are derived from the same docs/assumptions we're refining and may share
# our errors. Only P4L's integration tests count as runtime evidence: they actually
# execute against a running Live instance and observe real values.
#
# LR has no integration tests (only unit tests with fake bridges), so LR source
# isn't a verification source either — kept here only to surface that a symbol
# might appear in the bridge's protocol layer.
SEARCH_ROOTS = {
    "P4L-tests": Path.home() / "dev" / "PythonForLive" / "tests" / "integration",
    "P4L-src": Path.home() / "dev" / "PythonForLive" / "src" / "pythonforlive" / "typing",
    "LR-src": Path.home() / "dev" / "LiveRelay" / "clients" / "python" / "src" / "liverelay",
    "baseline": REPO_ROOT / "doc" / "live-api",
    "corpus": REPO_ROOT / "doc" / "decompiled" / "AbletonLive12_MIDIRemoteScripts",
    "m4l": REPO_ROOT / "doc" / "max-for-live-docs" / "9.0",
}


def _grep(pattern: str, root: Path, max_hits: int = 3) -> list[str]:
    """Return up to max_hits short grep lines from `root`."""
    if not root.is_dir():
        return []
    try:
        result = subprocess.run(
            ["grep", "-rn", "--include=*.py", "--include=*.md", pattern, str(root)],
            capture_output=True, text=True, timeout=20,
        )
    except Exception:
        return []
    lines = []
    for line in result.stdout.splitlines():
        m = re.match(r"([^:]+):(\d+):(.*)", line)
        if m:
            try:
                rel = Path(m.group(1)).resolve().relative_to(REPO_ROOT.parent)
            except ValueError:
                rel = m.group(1)
            text = m.group(3).strip()
            if len(text) > 110:
                text = text[:108] + "…"
            lines.append(f"{rel}:{m.group(2)}: {text}")
        if len(lines) >= max_hits:
            break
    return lines


def _short_member(path: str) -> str:
    """Member name from a dotted path."""
    return path.split(".")[-1]


def _classify_refinement(ref: dict) -> list[str]:
    """List the type-touching fields present."""
    fields = []
    for k in ("arg_types", "return_type", "probed_type", "element_repr"):
        if k in ref:
            fields.append(k)
    return fields


def _summarize_to(spec) -> str:
    """One-line summary of a type spec value (handles bare scalar or {from, to})."""
    if isinstance(spec, dict):
        from_v = spec.get("from", "?")
        to_v = spec.get("to", "?")
        return f"{from_v} → {to_v}"
    return f"{spec}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--filter", help="Only emit entries whose path contains this substring")
    args = parser.parse_args()

    refinements = yaml.safe_load(
        (REPO_ROOT / "tools" / "parse" / "manual_refinements.yaml").read_text()
    )

    print("# Refinement research report")
    print()
    print("Per-entry evidence gathered across P4L typed wrappers, LiveRelay client, the")
    print("curated baseline (doc/live-api), the decompiled Remote Script corpus, and M4L")
    print("docs. Use this to update confidence flags in manual_refinements.yaml.")
    print()

    n_emitted = 0
    for path, ref in refinements.items():
        if path.startswith("_") or not isinstance(ref, dict):
            continue
        if args.filter and args.filter not in path:
            continue
        fields = _classify_refinement(ref)
        if not fields:
            continue  # arg-name-only entries — names are decorative, skip per user direction

        member = _short_member(path)
        current_conf = ref.get("confidence", "medium (default)")

        print(f"## `{path}`")
        print()
        print(f"**Current confidence:** {current_conf}")
        print()
        print("**Refinement summary:**")
        for field in fields:
            print(f"- `{field}`: {_summarize_to(ref[field])}")
        print()

        # Searches
        for source, root in SEARCH_ROOTS.items():
            patterns = [rf"\.{re.escape(member)}\b", rf"\b{re.escape(member)}\b"]
            hits = []
            for pat in patterns:
                hits = _grep(pat, root, max_hits=3)
                if hits:
                    break
            if not hits:
                print(f"- **{source}**: no hits")
                continue
            print(f"- **{source}**:")
            for h in hits:
                print(f"  - `{h}`")
        print()
        n_emitted += 1

    print(f"\n# {n_emitted} type-touching entries emitted.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

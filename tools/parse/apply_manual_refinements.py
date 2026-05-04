#!/usr/bin/env python3
"""Apply hand-curated overrides from manual_refinements.yaml to LiveTree.parsed.json.

In strict alignment with doc/decisions.md: refinements are *only* used to correct
known wrongness in stub output, not to make stubs prettier. Each entry in
manual_refinements.yaml must include a `source` field documenting why the override
is justified — see the file header for the contract.

Mutates `LiveTree.parsed.json` in place. Re-running the parse step (which rewrites
the file from raw capture) requires re-running this script afterward; the
`run_parse_pipeline.py` orchestrator chains them.

Requires PyYAML — see requirements-dev.txt.

Usage:
    python tools/parse/apply_manual_refinements.py 12.3.6
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterator
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "error: PyYAML is required. Install with `pip install pyyaml` "
        "or `pip install -r requirements-dev.txt`.",
        file=sys.stderr,
    )
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Refinement entry shape (per dotted path):
#   {
#     "args":         { "argN": "real_name", ... }  # rename positional args
#     "arg_types":    { "name": "Type", ... }       # override an arg's type by name
#     "return_type":  "Type"                        # override the return type
#     "probed_type":  "Type"                        # override the property's probed type
#     "source":       "<rationale citation>"        # required
#   }
ALLOWED_FIELDS = {"args", "arg_types", "return_type", "probed_type", "source", "_note"}


def _walk(node: dict, path: str = "") -> Iterator[tuple[str, dict]]:
    """Yield (dotted_path, node) pairs for every named tree node."""
    name = node.get("name")
    if name:
        cur = f"{path}.{name}" if path else name
        yield cur, node
        for child in node.get("children") or []:
            yield from _walk(child, cur)
    else:
        for child in node.get("children") or []:
            yield from _walk(child, path)


def _apply_one(node: dict, refinement: dict, dotted_path: str) -> list[str]:
    """Apply a single refinement entry to a tree node. Return per-field log lines."""
    log: list[str] = []

    # --- arg name renames -------------------------------------------------
    arg_renames = refinement.get("args") or {}
    if arg_renames:
        args = node.get("args") or []
        if not args:
            log.append(f"  WARN args refinement on node with no args: {dotted_path}")
        for arg in args:
            cur_name = arg.get("name")
            if cur_name in arg_renames:
                arg["name"] = arg_renames[cur_name]
                log.append(f"  {dotted_path}: arg {cur_name!r} -> {arg['name']!r}")

    # --- arg type overrides ----------------------------------------------
    arg_types = refinement.get("arg_types") or {}
    if arg_types:
        args = node.get("args") or []
        for arg in args:
            cur_name = arg.get("name")
            if cur_name in arg_types:
                old = arg.get("type")
                arg["type"] = arg_types[cur_name]
                log.append(f"  {dotted_path}: arg {cur_name!r} type {old!r} -> {arg['type']!r}")

    # --- return type override --------------------------------------------
    if "return_type" in refinement:
        returns = node.setdefault("returns", {})
        old = returns.get("type")
        returns["type"] = refinement["return_type"]
        log.append(f"  {dotted_path}: return type {old!r} -> {returns['type']!r}")

    # --- property probed_type override -----------------------------------
    if "probed_type" in refinement:
        old = node.get("probed_type")
        node["probed_type"] = refinement["probed_type"]
        log.append(f"  {dotted_path}: probed_type {old!r} -> {node['probed_type']!r}")

    return log


def _validate_entry(path: str, entry: dict) -> str | None:
    """Return an error message if the entry is malformed, else None."""
    if not isinstance(entry, dict):
        return f"{path}: refinement must be an object"
    if not entry.get("source"):
        return f"{path}: refinement must include a non-empty `source` field"
    extra = set(entry) - ALLOWED_FIELDS
    if extra:
        return f"{path}: unknown field(s) {sorted(extra)}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--refinements", help="Override path to manual_refinements.json")
    parser.add_argument("--input", help="Override path to LiveTree.parsed.json")
    parser.add_argument("--quiet", action="store_true", help="Don't print per-refinement log lines")
    args = parser.parse_args()

    refinements_path = Path(args.refinements) if args.refinements else (
        REPO_ROOT / "tools" / "parse" / "manual_refinements.yaml"
    )
    parsed_path = Path(args.input) if args.input else (
        REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveTree.parsed.json"
    )

    if not refinements_path.exists():
        print(f"no manual_refinements.yaml at {refinements_path}; nothing to apply", file=sys.stderr)
        return 0
    if not parsed_path.exists():
        print(f"error: parsed tree not found at {parsed_path}", file=sys.stderr)
        return 2

    refinements = yaml.safe_load(refinements_path.read_text()) or {}
    parsed = json.loads(parsed_path.read_text())

    refinements = {k: v for k, v in refinements.items() if not k.startswith("_")}

    errors = [err for path, entry in refinements.items() if (err := _validate_entry(path, entry))]
    if errors:
        print("manual_refinements.json validation errors:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 2

    # Index tree nodes by dotted path
    index = dict(_walk(parsed["tree"]))

    applied = 0
    missed: list[str] = []
    log_lines: list[str] = []
    for path, entry in refinements.items():
        node = index.get(path)
        if not node:
            missed.append(path)
            continue
        log_lines.extend(_apply_one(node, entry, path))
        applied += 1

    parsed_path.write_text(json.dumps(parsed, indent=2) + "\n")

    print(f"Applied {applied} refinements to {parsed_path.relative_to(REPO_ROOT)}", file=sys.stderr)
    if missed:
        print(f"WARN: {len(missed)} refinement target(s) not found in parsed tree:", file=sys.stderr)
        for p in missed[:10]:
            print(f"  {p}", file=sys.stderr)
        if len(missed) > 10:
            print(f"  ... and {len(missed) - 10} more", file=sys.stderr)
    if not args.quiet:
        for line in log_lines:
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Convert refinements.llm.json + refinements.callsite.json to manual_refinements.yaml entries.

Used to bring forward arg-name and (optionally) type refinements from the previous
LLM/callsite pipeline into the new manual_refinements.yaml format. Each emitted entry
includes a `source` field that cites the original provenance ("LLM-derived from M4L
docs", "callsite analysis: 3/3 def votes", etc.) so the strict bar in
doc/decisions.md is preserved.

Output goes to stdout; redirect or copy into manual_refinements.yaml after review.

Default: emits arg-name renames only. Pass --include-types to also emit type
overrides (which carry higher accuracy risk and warrant per-entry review before
merging).

Usage:
    python tools/parse/import_legacy_refinements.py 12.3.6 > /tmp/imports.yaml
    python tools/parse/import_legacy_refinements.py 12.3.6 --include-types
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _walk(node: dict, path: str = ""):
    name = node.get("name")
    if name:
        cur = f"{path}.{name}" if path else name
        yield cur, node
        for child in node.get("children") or []:
            yield from _walk(child, cur)
    else:
        for child in node.get("children") or []:
            yield from _walk(child, path)


def _load_parsed_tree(version: str) -> dict[str, dict]:
    """Return a dotted-path -> node index of the parsed tree."""
    p = REPO_ROOT / "stubs" / version / "pipeline" / "LiveTree.parsed.json"
    data = json.loads(p.read_text())
    return dict(_walk(data["tree"]))


def _classify_llm_source(name_reason: str) -> str:
    """Tag the LLM's name_reason with a short source label."""
    r = name_reason.lower()
    if "maxforlive" in r or "m4l" in r:
        return "M4L docs"
    if "call site" in r or "callsite" in r or "call-site" in r:
        return "callsite"
    if "c++" in r or "signature" in r:
        return "C++ signature"
    if "descript" in r or "docstring" in r:
        return "docstring"
    if "usage" in r:
        return "usage snippet"
    return "structural / other"


def _yaml_string(s: str) -> str:
    """Escape a string for a YAML scalar inside double quotes."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _emit_arg_rename_entry(
    out, dotted: str, args_in_node: list[dict], renames: dict[str, dict], origin: str
) -> int:
    """Emit a YAML entry that renames arg(s). Returns count of renames emitted."""
    actual_arg_names = {a.get("name") for a in args_in_node}

    # Filter renames to only those that match a current arg name and actually change it.
    valid: list[tuple[str, str, str, str]] = []  # (from, to, source_label, source_text)
    for from_name, fix in renames.items():
        if from_name not in actual_arg_names:
            continue  # stale refinement target
        new_name = fix.get("name")
        if not new_name or new_name == from_name:
            continue
        # Determine source label
        if origin == "callsite":
            votes = fix.get("_votes") or {}
            total = fix.get("_total_defs") or sum(votes.values())
            top_vote = votes.get(new_name, 0)
            label = "callsite analysis"
            text = f"definition votes {top_vote}/{total} for {new_name!r}"
        else:
            reason = fix.get("name_reason", "")
            label = _classify_llm_source(reason)
            text = reason.replace("\n", " ").strip()
        valid.append((from_name, new_name, label, text))

    if not valid:
        return 0

    out.write(f"\n{_yaml_string(dotted)}:\n")
    out.write("  args:\n")
    for from_name, new_name, _, _ in valid:
        out.write(f"    {from_name}: {new_name}\n")
    out.write("  source: |\n")
    if origin == "callsite":
        out.write("    Imported from refinements.callsite.json (deterministic AST analysis\n")
        out.write("    of decompiled Ableton Remote Scripts, vote-counted across def signatures):\n")
    else:
        out.write("    Imported from refinements.llm.json (LLM-derived; source labels per arg):\n")
    for from_name, new_name, label, text in valid:
        out.write(f"      - {from_name} -> {new_name}  [{label}]: {text}\n")
    return len(valid)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", default="12.3.6", nargs="?")
    parser.add_argument("--include-types", action="store_true",
                        help="Also emit arg_types / return_type / probed_type fixes (higher risk).")
    parser.add_argument("--source", choices=["both", "llm", "callsite"], default="both",
                        help="Which refinement file(s) to import from.")
    args = parser.parse_args()

    pipeline = REPO_ROOT / "stubs" / args.version / "pipeline"
    tree_index = _load_parsed_tree(args.version)
    out = sys.stdout

    out.write("# Auto-generated YAML fragment from import_legacy_refinements.py — REVIEW BEFORE MERGING.\n")
    out.write(f"# Generated for version {args.version}.\n")
    out.write("# Each entry below corresponds to a single dotted-path member; bring them across\n")
    out.write("# into tools/parse/manual_refinements.yaml after reviewing each `source` line.\n")
    out.write("#\n")
    out.write("# This script defaults to arg-name renames only. Pass --include-types to also\n")
    out.write("# emit higher-risk type overrides (each warrants per-entry review against the\n")
    out.write("# binding before merging).\n")

    total_entries = 0
    total_renames = 0

    # Per-arg merge: callsite wins ties, LLM fills gaps. Per-path emission keeps the
    # source citations distinct so reviewers can see which name came from which source.
    cs_data = json.loads((pipeline / "refinements.callsite.json").read_text()) \
        if args.source in ("both", "callsite") else {"refinements": {}}
    llm_data = json.loads((pipeline / "refinements.llm.json").read_text()) \
        if args.source in ("both", "llm") else {"refinements": {}}

    cs_refs = cs_data.get("refinements", {})
    llm_refs = llm_data.get("refinements", {})
    all_paths = sorted(set(cs_refs) | set(llm_refs))

    out.write("\n# Per-path consolidated entries. Callsite wins ties; LLM fills gaps.\n")
    for path in all_paths:
        node = tree_index.get(path)
        if not node:
            out.write(f"\n# SKIP: {path} not found in parsed tree\n")
            continue
        actual_arg_names = {a.get("name") for a in (node.get("args") or [])}

        cs_args = (cs_refs.get(path) or {}).get("args") or {}
        llm_args = (llm_refs.get(path) or {}).get("args") or {}

        merged_renames: list[tuple[str, str, str, str]] = []  # (from, to, source_label, source_text)
        for from_name in actual_arg_names:
            if from_name in cs_args:
                fix = cs_args[from_name]
                votes = fix.get("_votes") or {}
                total = fix.get("_total_defs") or sum(votes.values())
                top = votes.get(fix.get("name"), 0)
                merged_renames.append(
                    (from_name, fix["name"], "callsite", f"definition votes {top}/{total} for {fix['name']!r}")
                )
            elif from_name in llm_args:
                fix = llm_args[from_name]
                if "name" not in fix or fix["name"] == from_name:
                    continue
                reason = fix.get("name_reason", "")
                merged_renames.append(
                    (from_name, fix["name"], _classify_llm_source(reason), reason.replace("\n", " ").strip())
                )

        merged_renames = [r for r in merged_renames if r[0] != r[1]]
        if not merged_renames:
            continue

        out.write(f"\n{_yaml_string(path)}:\n")
        out.write("  args:\n")
        for from_name, new_name, _, _ in merged_renames:
            out.write(f"    {from_name}: {new_name}\n")
        out.write("  source: |\n")
        sources_used = sorted({label for _, _, label, _ in merged_renames})
        if sources_used == ["callsite"]:
            out.write("    Imported from refinements.callsite.json (AST analysis, vote-counted):\n")
        elif "callsite" in sources_used:
            out.write("    Mixed-source: callsite (deterministic) + LLM (filling gaps):\n")
        else:
            out.write("    Imported from refinements.llm.json (LLM-derived):\n")
        for from_name, new_name, label, text in merged_renames:
            out.write(f"      - {from_name} -> {new_name}  [{label}]: {text}\n")

        total_entries += 1
        total_renames += len(merged_renames)

    if args.include_types:
        out.write("\n# TODO: --include-types is wired but type-override emission not yet implemented.\n")
        out.write("# Bring across types in a separate, per-entry-reviewed pass.\n")

    out.flush()
    print(
        f"\n# Emitted {total_entries} entries containing {total_renames} arg renames.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

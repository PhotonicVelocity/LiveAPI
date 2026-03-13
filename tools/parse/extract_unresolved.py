"""Extract unresolved types and arg names from LiveTree.parsed.json.

Scans the parsed tree for:
- Function args typed "object" (unresolved types)
- Function args named "arg1", "arg2", etc. (unnamed parameters)
- Function returns typed "object"
- Properties with null probed_type

Output is keyed by path and mirrors the refinements.llm.json structure, with shared
context per function and per-arg details. This means the LLM just adds resolved fields
to the same structure it receives as input.

Usage:
    python tools/parse/extract_unresolved.py 12.3.6
"""

from __future__ import annotations

import argparse
import json
import re
from os.path import join

_ARGX_RE = re.compile(r"^arg\d+$")


def extract(tree: dict, version: str) -> dict:
    """Walk the tree and collect all unresolved items, grouped by path."""
    items: dict[str, dict] = {}

    def walk(node: dict, path: str) -> None:
        if node.get("ref"):
            return

        name = node.get("name", "")
        node_type = node.get("type", "")
        current = f"{path}.{name}" if path else name

        if node_type == "function":
            _check_function(node, current, items)
        elif node_type == "property":
            _check_property(node, current, items)

        for child in node.get("children", []):
            walk(child, current)

    for module in tree.get("children", []):
        module_path = f"Live.{module['name']}"
        for child in module.get("children", []):
            walk(child, module_path)

    return {"version": version, "items": items}


def _check_function(node: dict, path: str, items: dict[str, dict]) -> None:
    """Check a function node for unresolved args and return type."""
    args_out: dict[str, dict] = {}
    returns_out: dict | None = None

    for arg in node.get("args", []):
        aname = arg.get("name", "")
        atype = arg.get("type", "")
        if aname == "self":
            continue

        if atype == "object":
            args_out.setdefault(aname, {})["current_type"] = "object"

        if _ARGX_RE.match(aname):
            entry = args_out.setdefault(aname, {})
            entry["current_type"] = atype
            entry["needs_name"] = True

    returns = node.get("returns")
    if returns and returns.get("type") == "object":
        returns_out = {"current_type": "object"}

    if not args_out and not returns_out:
        return

    entry: dict = {}
    if node.get("description"):
        entry["description"] = node["description"]
    if node.get("signature"):
        entry["signature"] = node["signature"]
    if node.get("cpp_signature"):
        entry["cpp_signature"] = node["cpp_signature"]
    if args_out:
        entry["args"] = args_out
    if returns_out:
        entry["returns"] = returns_out

    items[path] = entry


def _check_property(node: dict, path: str, items: dict[str, dict]) -> None:
    """Check a property node for missing probed_type."""
    if not node.get("probed_type"):
        entry: dict = {"probed_type": None}
        if node.get("raw_doc"):
            entry["raw_doc"] = node["raw_doc"]
        items[path] = entry


def main():
    parser = argparse.ArgumentParser(description="Extract unresolved types/names from LiveTree.parsed.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to LiveTree.parsed.json")
    parser.add_argument("--output", help="Path to output unresolved.json")
    args = parser.parse_args()

    input_path = args.input or join("stubs", args.version, "pipeline", "LiveTree.parsed.json")
    output_path = args.output or join("stubs", args.version, "pipeline", "unresolved.json")

    with open(input_path) as f:
        data = json.load(f)

    result = extract(data["tree"], args.version)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    # Summary
    items = result["items"]
    n_args = sum(len(v.get("args", {})) for v in items.values())
    n_returns = sum(1 for v in items.values() if "returns" in v)
    n_props = sum(1 for v in items.values() if "probed_type" in v)
    n_names = sum(
        1 for v in items.values() for a in v.get("args", {}).values() if a.get("needs_name")
    )
    n_types = n_args - n_names + sum(
        1 for v in items.values() for a in v.get("args", {}).values()
        if a.get("current_type") == "object" and not a.get("needs_name")
    )

    print(f"Wrote {len(items)} paths to {output_path}")
    print(f"  arg names to resolve: {n_names}")
    print(f"  arg types to resolve: {sum(1 for v in items.values() for a in v.get('args', {}).values() if a.get('current_type') == 'object')}")
    print(f"  return types to resolve: {n_returns}")
    print(f"  property types to resolve: {n_props}")


if __name__ == "__main__":
    main()

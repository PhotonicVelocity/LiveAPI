"""Extract unresolved types and arg names from LiveTree.parsed.json.

Scans the parsed tree for:
- Function args typed "object" (unresolved types)
- Function args named "arg1", "arg2", etc. (unnamed parameters)
- Function returns typed "object"
- Properties with null probed_type

Writes stubs/{version}/pipeline/unresolved.json with full context for each item.

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
    """Walk the tree and collect all unresolved items."""
    unresolved: list[dict] = []

    def walk(node: dict, path: str) -> None:
        if node.get("ref"):
            return

        name = node.get("name", "")
        node_type = node.get("type", "")
        current = f"{path}.{name}" if path else name

        if node_type == "function":
            _check_function(node, current, unresolved)
        elif node_type == "property":
            _check_property(node, current, unresolved)

        for child in node.get("children", []):
            walk(child, current)

    for module in tree.get("children", []):
        module_path = f"Live.{module['name']}"
        for child in module.get("children", []):
            walk(child, module_path)

    return {"version": version, "unresolved": unresolved}


def _check_function(node: dict, path: str, out: list[dict]) -> None:
    """Check a function node for unresolved args and return type."""
    context = {}
    if node.get("description"):
        context["description"] = node["description"]
    if node.get("signature"):
        context["signature"] = node["signature"]
    if node.get("cpp_signature"):
        context["cpp_signature"] = node["cpp_signature"]

    for arg in node.get("args", []):
        aname = arg.get("name", "")
        atype = arg.get("type", "")
        if aname == "self":
            continue

        if atype == "object":
            entry = {"path": path, "kind": "arg_type", "arg_name": aname, "current_type": "object", **context}
            out.append(entry)

        if _ARGX_RE.match(aname):
            entry = {"path": path, "kind": "arg_name", "arg_name": aname, "current_type": atype, **context}
            out.append(entry)

    returns = node.get("returns")
    if returns and returns.get("type") == "object":
        entry = {"path": path, "kind": "return_type", "current_type": "object", **context}
        out.append(entry)


def _check_property(node: dict, path: str, out: list[dict]) -> None:
    """Check a property node for missing probed_type."""
    if not node.get("probed_type"):
        entry = {"path": path, "kind": "property_type", "current_type": None}
        if node.get("raw_doc"):
            entry["raw_doc"] = node["raw_doc"]
        out.append(entry)


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
    by_kind: dict[str, int] = {}
    for item in result["unresolved"]:
        by_kind[item["kind"]] = by_kind.get(item["kind"], 0) + 1
    total = len(result["unresolved"])
    print(f"Wrote {total} unresolved items to {output_path}")
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")


if __name__ == "__main__":
    main()

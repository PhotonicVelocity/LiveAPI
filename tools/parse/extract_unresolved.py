"""Extract unresolved types and arg names from LiveTree.parsed.json.

Scans the parsed tree for:
- Function args typed "object" (unresolved types)
- Function args named "arg1", "arg2", etc. (unnamed parameters)
- Function args/returns typed "tuple" (need detailed tuple structure)
- Function returns typed "object"
- Properties with null probed_type
- Iterable properties missing element_repr

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
    iterable_classes = _collect_iterable_classes(tree)

    def walk(node: dict, path: str) -> None:
        if node.get("ref"):
            return

        name = node.get("name", "")
        node_type = node.get("type", "")
        current = f"{path}.{name}" if path else name

        if node_type == "function":
            _check_function(node, current, items)
        elif node_type == "property":
            _check_property(node, current, items, iterable_classes)
        elif node_type == "class":
            _check_class(node, current, items)

        for child in node.get("children", []):
            walk(child, current)

    for module in tree.get("children", []):
        module_path = f"Live.{module['name']}"
        for child in module.get("children", []):
            walk(child, module_path)

    return {"version": version, "items": items}


def _collect_iterable_classes(tree: dict) -> dict[str, bool]:
    """Collect iterable classes from the tree. Maps name -> whether element_repr is resolved."""
    iterable: dict[str, bool] = {}

    def walk(node: dict) -> None:
        if node.get("type") == "class" and node.get("iterable"):
            iterable[node["name"]] = bool(node.get("element_repr"))
        for child in node.get("children", []):
            walk(child)

    for module in tree.get("children", []):
        for child in module.get("children", []):
            walk(child)
    return iterable


def _check_function(node: dict, path: str, items: dict[str, dict]) -> None:
    """Check a function node for unresolved args and return type."""
    args_out: dict[str, dict] = {}
    returns_out: dict | None = None

    for arg in node.get("args", []):
        aname = arg.get("name", "")
        atype = arg.get("type", "")
        if aname == "self":
            continue

        needs: list[str] = []

        if atype in ("object", "tuple"):
            needs.append("type")
        if _ARGX_RE.match(aname):
            needs.append("name")

        if needs:
            entry = args_out.setdefault(aname, {})
            entry["current_type"] = atype
            entry["needs"] = needs

    returns = node.get("returns")
    if returns and returns.get("type") in ("object", "tuple"):
        returns_out = {"current_type": returns["type"], "needs": ["type"]}

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


def _check_class(node: dict, path: str, items: dict[str, dict]) -> None:
    """Check a class node for missing element type on iterable classes."""
    if node.get("iterable") and not node.get("element_repr"):
        entry: dict = {"needs": ["element_repr"]}
        if node.get("raw_doc"):
            entry["raw_doc"] = node["raw_doc"]
        items[path] = entry


def _check_property(node: dict, path: str, items: dict[str, dict], iterable_classes: dict[str, bool]) -> None:
    """Check a property node for missing probed_type or missing element type."""
    if not node.get("probed_type"):
        entry: dict = {"probed_type": None, "needs": ["probed_type"]}
        if node.get("raw_doc"):
            entry["raw_doc"] = node["raw_doc"]
        items[path] = entry
    elif not node.get("element_repr"):
        probed = node["probed_type"]
        # Skip if the class itself already has element_repr resolved
        class_resolved = iterable_classes.get(probed, False)
        if (probed in iterable_classes or probed == "tuple") and not class_resolved:
            entry = {
                "probed_type": probed,
                "needs": ["element_repr"],
            }
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

    # Summary — count each "needs" entry across all items
    items = result["items"]
    counts: dict[str, int] = {}
    for entry in items.values():
        for need in entry.get("needs", []):
            counts[need] = counts.get(need, 0) + 1
        if "returns" in entry:
            for need in entry["returns"].get("needs", []):
                counts[f"return_{need}"] = counts.get(f"return_{need}", 0) + 1
        for arg_val in entry.get("args", {}).values():
            for need in arg_val.get("needs", []):
                counts[f"arg_{need}"] = counts.get(f"arg_{need}", 0) + 1

    print(f"Wrote {len(items)} paths to {output_path}")
    for kind, count in sorted(counts.items()):
        print(f"  {kind}: {count}")
    print(f"  total: {sum(counts.values())}")


if __name__ == "__main__":
    main()

"""Apply refinements.llm.json to LiveTree.parsed.json, producing LiveTree.resolved.json.

Walks the parsed tree and applies arg name/type overrides, return type overrides,
and property type overrides in-place. The resolved tree can then be fed directly
to the stub generator without any refinement logic.

Usage:
    python tools/parse/apply_refinements.py 12.3.6
"""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from os.path import exists, join


def apply(tree: dict, refinements: dict) -> tuple[dict, dict[str, int]]:
    """Apply refinements to a deep copy of the tree. Returns the modified tree."""
    tree = deepcopy(tree)
    stats = {"arg_name": 0, "arg_type": 0, "return_type": 0, "property_type": 0, "element_type": 0}

    def walk(node: dict, path: str) -> None:
        if node.get("ref"):
            return

        name = node.get("name", "")
        node_type = node.get("type", "")
        current = f"{path}.{name}" if path else name

        ref = refinements.get(current)
        if ref:
            if node_type == "function":
                _apply_function(node, ref, stats)
            elif node_type == "property":
                _apply_property(node, ref, stats)
            elif node_type == "class":
                _apply_class(node, ref, stats)

        for child in node.get("children", []):
            if child is not None:
                walk(child, current)

    for module in tree.get("children", []):
        module_path = f"Live.{module['name']}"
        for child in module.get("children", []):
            if child is not None:
                walk(child, module_path)

    # Propagate class-level element_repr to properties that return those classes
    _propagate_element_repr(tree, stats)

    return tree, stats


def _apply_function(node: dict, ref: dict, stats: dict) -> None:
    """Apply arg and return type refinements to a function node."""
    arg_refs = ref.get("args", {})
    if arg_refs:
        for arg in node.get("args", []):
            aname = arg.get("name", "")
            if aname in arg_refs:
                overrides = arg_refs[aname]
                if "name" in overrides:
                    arg["name"] = overrides["name"]
                    stats["arg_name"] += 1
                if "type" in overrides:
                    arg["type"] = overrides["type"]
                    stats["arg_type"] += 1

    ret_ref = ref.get("returns")
    if ret_ref and "type" in ret_ref:
        if node.get("returns"):
            node["returns"]["type"] = ret_ref["type"]
        else:
            node["returns"] = {"type": ret_ref["type"]}
        stats["return_type"] += 1


def _apply_property(node: dict, ref: dict, stats: dict) -> None:
    """Apply probed_type or element_repr refinement to a property node."""
    if "probed_type" in ref:
        node["probed_type"] = ref["probed_type"]
        stats["property_type"] += 1
    if "element_repr" in ref:
        node["element_repr"] = ref["element_repr"]
        stats["element_type"] += 1


def _apply_class(node: dict, ref: dict, stats: dict) -> None:
    """Apply element_repr refinement to a class node."""
    if "element_repr" in ref:
        saved_children = node.pop("children", None)
        node["element_repr"] = ref["element_repr"]
        if saved_children is not None:
            node["children"] = saved_children
        stats["element_type"] += 1


def _propagate_element_repr(tree: dict, stats: dict) -> None:
    """Propagate element_repr from class nodes to properties that return those classes."""
    # Build map: class name -> element_repr (skip LomObject — it means the
    # class holds heterogeneous types and isn't useful for individual properties)
    class_element: dict[str, str] = {}
    for module in tree.get("children", []):
        for node in module.get("children", []):
            if node.get("type") == "class" and node.get("element_repr"):
                if "LomObject" not in node["element_repr"]:
                    class_element[node["name"]] = node["element_repr"]

    if not class_element:
        return

    # Stamp onto properties whose probed_type matches
    def walk(node: dict) -> None:
        if node.get("type") == "property" and not node.get("element_repr"):
            elem = class_element.get(node.get("probed_type", ""))
            if elem:
                node["element_repr"] = elem
                stats["element_type"] += 1
        for child in node.get("children", []):
            if child is not None:
                walk(child)

    for module in tree.get("children", []):
        for node in module.get("children", []):
            walk(node)


def main():
    parser = argparse.ArgumentParser(description="Apply refinements to parsed tree")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to LiveTree.parsed.json")
    parser.add_argument("--refinements", help="Path to refinements.llm.json")
    parser.add_argument("--output", help="Path to output LiveTree.resolved.json")
    args = parser.parse_args()

    input_path = args.input or join("stubs", args.version, "pipeline", "LiveTree.parsed.json")
    refinements_path = args.refinements or join("stubs", args.version, "pipeline", "refinements.llm.json")
    output_path = args.output or join("stubs", args.version, "pipeline", "LiveTree.resolved.json")

    with open(input_path) as f:
        data = json.load(f)

    refinements: dict = {}
    if exists(refinements_path):
        with open(refinements_path) as f:
            refinements = json.load(f).get("refinements", {})
        print(f"Loaded refinements for {len(refinements)} paths from {refinements_path}")
    else:
        print(f"No refinements file at {refinements_path}, copying tree as-is")

    resolved_tree, stats = apply(data["tree"], refinements)
    data["tree"] = resolved_tree

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    total = sum(stats.values())
    print(f"Applied {total} individual changes to {output_path}")
    for kind, count in sorted(stats.items()):
        if count:
            print(f"  {kind}: {count}")


if __name__ == "__main__":
    main()

"""Build a types-only skeleton of the parsed API tree.

Reads LiveTree.parsed.json and emits a compact text tree showing all modules, classes,
enums (with values), and properties (with probed types). Functions are omitted since
they're already present on the unresolved items themselves.

Used as LLM context for type resolution. Can also be run standalone to inspect
the skeleton or iterate on its structure.

Format conventions (no explicit type tags):
- Containers (modules/classes) end with `:` and have indented children
- Properties use `name -> Type` or bare `name` (no probed type)
- Enums use `Name = val1, val2, ...`
- String constants use `name = 'value'`
- Exceptions use `!Name`

Usage:
    python tools/parse/build_type_skeleton.py 12.3.6
    python tools/parse/build_type_skeleton.py 12.3.6 --output skeleton.txt
"""

from __future__ import annotations

import argparse
from os.path import join


FUNCTION_TYPES = {"function", "builtin_function_or_method", "method", "method_descriptor"}

INDENT = "\t"


def build_skeleton(tree: dict) -> str:
    """Build a compact text skeleton from the parsed tree.

    Format:
        Live:
        	Application:
        		Application:
        			View:
        				NavDirection = left, right, up, down
        				browse_mode -> bool
        			browser -> Browser
        		ControlDescription:
        			id -> int
    """
    lines: list[str] = []
    _render(tree, 0, lines)
    return "\n".join(lines)


def _render(node: dict, depth: int, lines: list[str]) -> None:
    t = node.get("type")
    name = node.get("name", "")
    prefix = INDENT * depth

    if t in ("module", "class"):
        children = [c for c in node.get("children", []) if isinstance(c, dict)]
        if children:
            lines.append(f"{prefix}{name}:")
            for child in children:
                _render(child, depth + 1, lines)
        else:
            lines.append(f"{prefix}{name}")

    elif t == "enum":
        members = node.get("members", {})
        values = list(members.keys()) if isinstance(members, dict) else []
        if values:
            lines.append(f"{prefix}{name} = {', '.join(values)}")
        else:
            lines.append(f"{prefix}{name}")

    elif t == "property":
        if name == "_live_ptr":
            return
        probed = node.get("probed_type")
        if probed and probed in ("bool", "int", "float", "str", "NoneType"):
            return  # Omit primitive-typed properties to save space
        if probed:
            lines.append(f"{prefix}{name} -> {probed}")
        else:
            lines.append(f"{prefix}{name}")

    elif t == "str":
        val = node.get("value", "")
        lines.append(f"{prefix}{name} = {val!r}")

    elif t == "type":
        lines.append(f"{prefix}!{name}")

    elif t in FUNCTION_TYPES:
        pass  # Omit functions


def main():
    parser = argparse.ArgumentParser(description="Build type skeleton from LiveTree.parsed.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to LiveTree.parsed.json")
    parser.add_argument("--output", help="Path to output skeleton file")
    args = parser.parse_args()

    input_path = args.input or join("stubs", args.version, "pipeline", "LiveTree.parsed.json")
    output_path = args.output or join("stubs", args.version, "pipeline", "type_skeleton.txt")

    import json
    with open(input_path) as f:
        data = json.load(f)

    skeleton = build_skeleton(data["tree"])

    with open(output_path, "w") as f:
        f.write(skeleton)
        f.write("\n")

    # Stats
    lines = skeleton.split("\n")
    size_kb = len(skeleton) / 1024
    containers = sum(1 for l in lines if l.rstrip().endswith(":"))
    props = sum(1 for l in lines if " -> " in l)
    enums = sum(1 for l in lines if " = " in l and "," in l)

    print(f"Wrote {output_path} ({size_kb:.1f} KB, {len(lines)} lines)")
    print(f"  containers: {containers}, properties: {props}, enums: {enums}")


if __name__ == "__main__":
    main()

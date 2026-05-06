#!/usr/bin/env python3
"""Emit per-module YAML in the LOM format from LiveTree.refined.json.

Stage 2 of the new pipeline shape (see doc/dataflow.md, doc/lom-format.md).
Walks the refined tree and writes one YAML per top-level Live module to
stubs/<version>/reports/seed/<Module>.yaml.

Reads the existing refined tree (parsed.json with manual_refinements.yaml
already applied). Once the per-module YAML store takes over, this stage
will fuse parse + refine + emit and LiveTree.refined.json will retire.

Usage:
    python tools/parse/emit_seed_yaml.py 12.3.6
    python tools/parse/emit_seed_yaml.py 12.3.6 --output /tmp/seed
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

_ANCESTOR_RE = re.compile(r"<class '([^']+)'>")
_BORING_BASES = {
    "Boost.Python.instance",
    "instance",
    "object",
}

# Listener triplet pattern. Each property X has add_X_listener,
# remove_X_listener, X_has_listener siblings; the parser emits these as
# full method nodes which we fold into the property's `listenable:` list.
_LISTENER_RE = re.compile(
    r"^(?:add_(?P<add>\w+)_listener|remove_(?P<rem>\w+)_listener|(?P<has>\w+)_has_listener)$"
)

# Suppressed names. _live_ptr is a Boost.Python implementation detail; the
# dunders are noise from the runtime walk that doesn't represent the
# public API.
SKIP_MEMBERS = {
    "_live_ptr",
    "__module__",
    "__qualname__",
    "__init__",
    "__class__",
}


def _norm_doc(text: str | None) -> str | None:
    """Strip trailing whitespace per line + leading/trailing blank lines.

    Boost.Python docstrings often carry trailing spaces and stray leading
    newlines; without normalization PyYAML falls back to double-quoted
    scalar style to preserve them, which makes the seed YAML diff-hostile.
    """
    if not text:
        return text
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def simplify_ancestors(class_node: dict) -> list[str]:
    """Strip Boost.Python boilerplate; reduce ancestors to simple names."""
    out: list[str] = []
    for ancestor_repr in class_node.get("ancestors", []):
        m = _ANCESTOR_RE.match(ancestor_repr)
        if not m:
            continue
        full = m.group(1)
        if full in _BORING_BASES:
            continue
        out.append(full.rsplit(".", 1)[-1])
    return out


def listener_property_name(method_name: str) -> str | None:
    """If method_name is a listener method, return the property it listens to."""
    m = _LISTENER_RE.match(method_name)
    if not m:
        return None
    return m.group("add") or m.group("rem") or m.group("has")


def collect_listener_triplets(class_node: dict) -> dict[str, list[str]]:
    """Group listener methods by property name, ordered add/remove/has."""
    by_prop: dict[str, dict[str, str]] = {}
    for child in class_node.get("children", []):
        if child.get("type") != "function" or child.get("ref"):
            continue
        name = child.get("name", "")
        prop = listener_property_name(name)
        if prop is None:
            continue
        if name.startswith("add_"):
            slot = "add"
        elif name.startswith("remove_"):
            slot = "remove"
        else:
            slot = "has"
        by_prop.setdefault(prop, {})[slot] = name
    return {
        prop: [slots[k] for k in ("add", "remove", "has") if k in slots]
        for prop, slots in by_prop.items()
    }


def convert_args(args: list[dict] | None) -> list[dict]:
    """Drop self; emit the rest in spec shape."""
    if not args:
        return []
    out: list[dict] = []
    for arg in args:
        if arg.get("name") == "self":
            continue
        item: dict[str, Any] = {"name": arg["name"]}
        if arg.get("type"):
            item["type"] = arg["type"]
        if arg.get("optional"):
            item["optional"] = True
            if arg.get("default") is not None:
                item["default"] = arg["default"]
        out.append(item)
    return out


def convert_returns(returns: dict | None) -> dict | None:
    if not returns:
        return None
    out: dict[str, Any] = {}
    if returns.get("type"):
        out["type"] = returns["type"]
    return out or None


def convert_property(node: dict, listener_methods: list[str]) -> dict:
    out: dict[str, Any] = {"kind": "property", "name": node["name"]}
    if node.get("raw_doc"):
        out["raw_doc"] = _norm_doc(node["raw_doc"])
    if node.get("probed_type"):
        out["type"] = node["probed_type"]
    if node.get("probed_repr"):
        out["repr"] = node["probed_repr"]
    if node.get("element_repr"):
        out["element_repr"] = node["element_repr"]
    out["settable"] = bool(node.get("settable"))
    if listener_methods:
        out["listenable"] = listener_methods
    return out


def convert_method_or_function(node: dict, kind: str) -> dict:
    """Convert a function node. Parser's `description` (cleaned) → YAML's
    `raw_doc:`; the verbatim Boost.Python dump is dropped from the schema."""
    out: dict[str, Any] = {"kind": kind, "name": node["name"]}
    if node.get("description"):
        out["raw_doc"] = _norm_doc(node["description"])
    if node.get("signature"):
        out["signature"] = _norm_doc(node["signature"])
    if node.get("cpp_signature"):
        out["cpp_signature"] = _norm_doc(node["cpp_signature"])
    args = convert_args(node.get("args"))
    if args:
        out["args"] = args
    returns = convert_returns(node.get("returns"))
    if returns:
        out["returns"] = returns
    return out


def convert_enum(node: dict) -> dict:
    out: dict[str, Any] = {"kind": "enum", "name": node["name"]}
    if node.get("raw_doc"):
        out["raw_doc"] = _norm_doc(node["raw_doc"])
    if node.get("members"):
        out["members"] = dict(node["members"])  # preserve insertion order
    return out


def convert_constant(node: dict) -> dict:
    """`str`-typed module attribute. Parser stores `value` as a Python repr
    (e.g. `"'Beta'"`); unquote via ast.literal_eval."""
    out: dict[str, Any] = {"kind": "constant", "name": node["name"], "type": "str"}
    val = node.get("value")
    if val is not None:
        try:
            val = ast.literal_eval(val) if isinstance(val, str) else val
        except (ValueError, SyntaxError):
            pass  # leave as-is if it's not a Python literal
        out["value"] = val
    return out


def convert_class_members(class_node: dict) -> list[dict]:
    """Convert a class's children, folding listener triplets into properties.

    Some classes carry listener triplets for names that aren't exposed as
    properties — `Clip.notes`, `Song.data`, `loop_jump`, etc. Those are
    listener-only signals (events / hidden state). They're emitted as
    `kind: property` with only `name:` and `listenable:` set; the absence
    of `type:` is the renderer's cue to treat them as signals.
    """
    triplets = collect_listener_triplets(class_node)
    listener_method_names: set[str] = set()
    for methods in triplets.values():
        listener_method_names.update(methods)

    property_names = {
        c.get("name")
        for c in class_node.get("children", [])
        if c.get("type") == "property" and not c.get("ref") and c.get("name") not in SKIP_MEMBERS
    }
    orphan_props = {
        prop: methods for prop, methods in triplets.items() if prop not in property_names
    }

    out: list[dict] = []
    for child in class_node.get("children", []):
        name = child.get("name")
        if not name or name in SKIP_MEMBERS:
            continue
        # `ref: true` marks inherited members the parser relocated. The
        # canonical copy lives at the defining class; the inherited-site
        # copy is parser-internal and doesn't appear in YAML.
        if child.get("ref"):
            continue
        ctype = child.get("type")
        if ctype == "property":
            out.append(convert_property(child, triplets.get(name, [])))
        elif ctype == "function":
            if name in listener_method_names:
                continue
            out.append(convert_method_or_function(child, "method"))
        elif ctype == "class":
            out.append(convert_class(child))
        elif ctype == "enum":
            out.append(convert_enum(child))
        elif ctype == "str":
            out.append(convert_constant(child))

    for prop_name, methods in orphan_props.items():
        out.append({"kind": "property", "name": prop_name, "listenable": methods})

    return out


def convert_class(node: dict) -> dict:
    out: dict[str, Any] = {"kind": "class", "name": node["name"]}
    if node.get("raw_doc"):
        out["raw_doc"] = _norm_doc(node["raw_doc"])
    out["ancestors"] = simplify_ancestors(node)
    if node.get("init_doc"):
        out["init_doc"] = _norm_doc(node["init_doc"])
    if node.get("constructable"):
        out["constructable"] = True
    if node.get("iterable"):
        out["iterable"] = True
    if node.get("element_repr"):
        out["element_repr"] = node["element_repr"]
    members = convert_class_members(node)
    if members:
        out["members"] = members
    return out


def convert_module_top(module_node: dict) -> dict:
    """Top-level YAML for a module: name, raw_doc, members list.

    Members are emitted in their parser-tree order *except* the
    self-named primary class (`Live.Song.Song`, `Live.Track.Track`, ...)
    which is moved to the front. Per the spec, "first class in members:
    is the primary class — no flag needed."
    """
    out: dict[str, Any] = {"module": module_node["name"]}
    if module_node.get("raw_doc"):
        out["raw_doc"] = module_node["raw_doc"]

    module_name = module_node["name"]
    primary: dict | None = None
    others: list[dict] = []

    for child in module_node.get("children", []):
        name = child.get("name")
        if not name or name in SKIP_MEMBERS:
            continue
        if child.get("ref"):
            continue
        ctype = child.get("type")
        if ctype in ("class", "type"):
            # `type` is a parser leftover (sole occurrence: LimitationError);
            # fold into class. Detection of exception treatment comes from
            # `Exception` in ancestors, not a separate kind.
            converted = convert_class(child)
        elif ctype == "enum":
            converted = convert_enum(child)
        elif ctype == "function":
            converted = convert_method_or_function(child, "function")
        elif ctype == "str":
            converted = convert_constant(child)
        else:
            continue

        if ctype in ("class", "type") and name == module_name:
            primary = converted
        else:
            others.append(converted)

    members = ([primary] if primary else []) + others
    if members:
        out["members"] = members
    return out


# --- YAML emission ------------------------------------------------------- #


def _str_representer(dumper: yaml.SafeDumper, data: str) -> Any:
    """Use literal block style (`|`) for multiline strings; default otherwise."""
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(str, _str_representer)
_Dumper.ignore_aliases = lambda self, data: True  # type: ignore[method-assign]


def emit_yaml(data: dict, path: Path) -> None:
    text = yaml.dump(
        data,
        Dumper=_Dumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=10000,
    )
    path.write_text(text)


def main() -> int:
    p = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    p.add_argument("version", help="Live version (e.g. 12.3.6)")
    p.add_argument("--input", help="path to LiveTree.refined.json")
    p.add_argument("--output", help="output dir")
    args = p.parse_args()

    in_path = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveTree.refined.json"
    )
    out_dir = (
        Path(args.output)
        if args.output
        else REPO_ROOT / "stubs" / args.version / "reports" / "seed"
    )

    if not in_path.exists():
        print(f"error: refined tree not found at {in_path}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(in_path.read_text())
    tree = data["tree"]

    written = 0
    for module_node in tree.get("children", []):
        if module_node.get("type") != "module":
            continue
        name = module_node.get("name")
        if not name:
            continue
        yaml_node = convert_module_top(module_node)
        emit_yaml(yaml_node, out_dir / f"{name}.yaml")
        written += 1

    print(f"Wrote {written} module YAMLs to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build per-module LOM YAML files from LiveTree.parsed.json.

Reads the parsed tree (output of parse_apicapture_results_v2.py) and
emits one YAML file per top-level Live module to
stubs/<v>/reports/seed/<Module>.yaml. Format spec:
doc/lom-format.md (the new named-group shape supersedes the
single-`members:` shape committed in earlier drafts).

Top-down through the file you can read it as five conversion stages.
Each stage maps a layer of the parsed tree onto the YAML shape; later
stages compose with earlier ones via plain function calls — there's no
visitor framework, just a recursive build:

  1. Top-level CLI driver (main): walk modules, dispatch, write files.
  2. Module conversion (build_module_yaml): split children into named
     kind-groups (primary_class / classes / enums / functions / constants).
  3. Per-node conversion (build_member): dispatch by parser `type:` to
     produce a YAML member dict. Recurses into class bodies.
  4. Class-body expansion (_group_class_members): same kind-grouping as
     §2 plus listener-triplet folding and orphan-signal synthesis.
  5. Listener-triplet detection helpers (_LISTENER_RE,
     _collect_listener_triplets): pure inspection of a class's children;
     no mutations.

Helpers (string normalization, kind-discriminator map, skip-list,
YAML emission with literal-block strings) live alongside the stage they
support and are clearly marked.

Iteration plan — extend build_member by one field/transformation at a
time, comparing output diffs at each step:

    Step 1. one file per module, just `module:` and empty `members:`
    Step 2. list class/enum/function/constant names (with kind grouping
            and primary-class promotion)
    Step 3. raw_doc on classes + module
    Step 4. expand class bodies (properties, methods, nested types)
    Step 5 (current). fold listener triplets into `listenable:`
    Step 6+: types, settable, args/returns, ...

Usage:
    python tools/parse/build_lom_yaml.py 12.3.6
    python tools/parse/build_lom_yaml.py 12.3.6 --output /tmp/seed
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


# region------------------------------------------------------------------------- #
# Helpers — string normalization, kind discriminator, skip set
# ------------------------------------------------------------------------------- #


def _norm_doc(text: str | None) -> str | None:
    """Strip trailing whitespace per line + leading/trailing blank lines.

    Boost.Python docstrings carry trailing spaces and stray leading
    newlines; without normalization, PyYAML falls back to double-quoted
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


# Maps the parser's `type` field on each tree node to the YAML `kind:`
# discriminator. `type` (the parser's leftover for exception classes like
# LimitationError) is folded into `class` per the spec — exception classes
# are recognized by `Exception` in `ancestors:`, not a separate kind.
# `str` (module-level constant) becomes `kind: constant`.
_KIND_BY_TYPE = {
    "class": "class",
    "type": "class",
    "enum": "enum",
    "function": "function",
    "property": "property",
    "str": "constant",
}

# Members suppressed from output. `_live_ptr` is a Boost.Python
# implementation detail; the dunders are runtime-walk noise that doesn't
# represent the public API.
SKIP_MEMBERS = {
    "_live_ptr",
    "__module__",
    "__qualname__",
    "__init__",
    "__class__",
}

# endregion


# region------------------------------------------------------------------------- #
# Listener-triplet detection
#
# Each property X that supports change notification has three sibling
# methods on the same class: `add_X_listener(callback)`,
# `remove_X_listener(callback)`, and `X_has_listener(callback) -> bool`.
# In the YAML we fold those three methods into a single `listenable:`
# list on the property they watch and drop the standalone method nodes.
# When the listener triplet's target name isn't an actual property —
# events like `loop_jump`, hidden state like `Clip.notes` — we synthesize
# a listener-only property (no `type:`, only `listenable:`).
# ------------------------------------------------------------------------------- #


_LISTENER_RE = re.compile(
    r"^(?:add_(?P<add>\w+)_listener|remove_(?P<rem>\w+)_listener|(?P<has>\w+)_has_listener)$"
)


def _listener_property_name(method_name: str) -> str | None:
    """If method_name is a listener method, return the property name it watches."""
    m = _LISTENER_RE.match(method_name)
    if not m:
        return None
    return m.group("add") or m.group("rem") or m.group("has")


def _collect_listener_triplets(class_node: dict[str, Any]) -> dict[str, list[str]]:
    """Group listener methods on a class by property name, ordered add → remove → has.

    Output: `{property_name: [method_names_in_canonical_order]}`. A triplet
    can have any 1–3 of the three slots filled depending on what the
    runtime exposes; the list preserves the canonical add/remove/has
    order regardless of which slots are present.
    """
    by_prop: dict[str, dict[str, str]] = {}
    for child in class_node.get("children", []):
        if child.get("type") != "function" or child.get("ref"):
            continue
        name = child.get("name", "")
        prop = _listener_property_name(name)
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

# endregion


# region------------------------------------------------------------------------- #
# Per-node conversion (build_member) and class-body expansion
#
# build_member is the dispatch entry point: given a tree node, return its
# YAML member dict (or None to skip). Only classes recurse; properties,
# functions, enums, and constants emit name-only stubs that later
# iterations will enrich with types, args, descriptions, etc.
#
# _group_class_members is the recursive arm: same kind-grouping as the
# module level (§5) plus the listener-triplet fold and orphan synthesis
# described in the listener-detection section above.
# ------------------------------------------------------------------------------- #


def build_member(node: dict[str, Any]) -> dict[str, Any] | None:
    """Convert a tree-node child into its YAML member dict, or None to skip."""
    node_type = node.get("type")
    if not isinstance(node_type, str):
        return None
    kind = _KIND_BY_TYPE.get(node_type)
    if kind is None:
        return None
    name = node.get("name")
    if not name or name in SKIP_MEMBERS:
        return None

    out: dict[str, Any] = {"kind": kind, "name": name}
    if kind == "class":
        raw_doc = _norm_doc(node.get("raw_doc"))
        if raw_doc:
            out["raw_doc"] = raw_doc
        out.update(_group_class_members(node))
    return out


def _group_class_members(class_node: dict[str, Any]) -> dict[str, Any]:
    """Walk a class's children and group them by kind into named lists.

    Mirrors the module-level structure: properties → methods → nested
    classes → nested enums → nested constants. Empty groups are omitted.
    `ref: true` and SKIP_MEMBERS entries are dropped.

    Listener triplets are folded into the owning property's `listenable:`
    list (the standalone method nodes are removed); orphan triplets
    (no matching property) are emitted as listener-only properties.
    """
    triplets = _collect_listener_triplets(class_node)
    listener_method_names: set[str] = set()
    for methods in triplets.values():
        listener_method_names.update(methods)

    groups: dict[str, list[dict[str, Any]]] = {
        "property": [], "function": [], "class": [], "enum": [], "constant": [],
    }
    seen_property_names: set[str] = set()
    for child in class_node.get("children", []):
        if child.get("ref"):
            continue
        # Drop the listener triplet methods — they're folded onto their
        # owning property below.
        if child.get("type") == "function" and child.get("name") in listener_method_names:
            continue
        member = build_member(child)
        if member is None:
            continue
        kind = member.pop("kind")
        if kind == "property":
            triplet = triplets.get(member["name"])
            if triplet:
                member["listenable"] = triplet
            seen_property_names.add(member["name"])
        groups[kind].append(member)

    # Synthesize orphan listener triplets: their target name doesn't exist
    # as a real property, so emit a bare `name + listenable` property.
    for prop_name, methods in triplets.items():
        if prop_name in seen_property_names:
            continue
        groups["property"].append({"name": prop_name, "listenable": methods})

    return _to_named_groups(
        properties=groups["property"],
        methods=groups["function"],
        classes=groups["class"],
        enums=groups["enum"],
        constants=groups["constant"],
    )


def _to_named_groups(
    *,
    properties: list[dict[str, Any]] | None = None,
    methods: list[dict[str, Any]] | None = None,
    classes: list[dict[str, Any]] | None = None,
    enums: list[dict[str, Any]] | None = None,
    functions: list[dict[str, Any]] | None = None,
    constants: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build the named-group dict, omitting empty groups.

    Used at both the module level (`functions:` for module-level callables)
    and inside classes (`methods:` for class methods, `properties:` for
    properties). Order of insertion is the schema's render order.
    """
    out: dict[str, Any] = {}
    if properties:
        out["properties"] = properties
    if methods:
        out["methods"] = methods
    if classes:
        out["classes"] = classes
    if enums:
        out["enums"] = enums
    if functions:
        out["functions"] = functions
    if constants:
        out["constants"] = constants
    return out

# endregion


# region------------------------------------------------------------------------- #
# Module conversion (build_module_yaml)
#
# Top of the conversion pipeline: walks a module's children, dispatches
# each through build_member, then groups by kind. The self-named class
# (`Live.Song.Song`, `Live.Track.Track`, ...) is promoted to its own
# `primary_class:` key per the spec; everything else lands in `classes:`,
# `enums:`, `functions:`, or `constants:`.
# ------------------------------------------------------------------------------- #


def build_module_yaml(module_node: dict[str, Any]) -> dict[str, Any]:
    """Convert one module node into its YAML-shape dict."""
    module_name = module_node["name"]
    groups: dict[str, list[dict[str, Any]]] = {
        "class": [], "enum": [], "function": [], "constant": [],
    }
    primary: dict[str, Any] | None = None

    for child in module_node.get("children", []):
        if child.get("ref"):
            continue
        member = build_member(child)
        if member is None:
            continue
        # `kind` is implicit in which group the entry lives in — drop the
        # per-entry discriminator.
        kind = member.pop("kind")
        if kind == "class" and member["name"] == module_name:
            primary = member
        else:
            groups[kind].append(member)

    out: dict[str, Any] = {"module": module_name}
    raw_doc = _norm_doc(module_node.get("raw_doc"))
    if raw_doc:
        out["raw_doc"] = raw_doc
    if primary:
        out["primary_class"] = [primary]
    out.update(_to_named_groups(
        classes=groups["class"],
        enums=groups["enum"],
        functions=groups["function"],
        constants=groups["constant"],
    ))
    return out

# endregion


# region------------------------------------------------------------------------- #
# YAML emission — literal-block representer + safe dumper config
# ------------------------------------------------------------------------------- #


def _str_representer(dumper: yaml.SafeDumper, data: str) -> Any:
    """Use literal block style (`|`) for multiline strings; default otherwise."""
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(str, _str_representer)
_Dumper.ignore_aliases = lambda self, data: True  # type: ignore[method-assign]


def emit_yaml(data: dict[str, Any], path: Path) -> None:
    text = yaml.dump(
        data,
        Dumper=_Dumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=10000,
    )
    path.write_text(text)

# endregion


# region------------------------------------------------------------------------- #
# CLI / main
# ------------------------------------------------------------------------------- #


def main() -> int:
    p = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    p.add_argument("version", help="Live version (e.g. 12.3.6)")
    p.add_argument("--input", help="path to LiveTree.parsed.json")
    p.add_argument("--output", help="output dir")
    args = p.parse_args()

    in_path = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveTree.parsed.json"
    )
    out_dir = (
        Path(args.output)
        if args.output
        else REPO_ROOT / "stubs" / args.version / "reports" / "seed"
    )

    if not in_path.exists():
        print(f"error: parsed tree not found at {in_path}", file=sys.stderr)
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
        emit_yaml(build_module_yaml(module_node), out_dir / f"{name}.yaml")
        written += 1

    print(f"Wrote {written} module YAMLs to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# endregion

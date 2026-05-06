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

Iteration plan — each step extended build_member by one field or
transformation, comparing output diffs along the way. The v2 parsed
tree has now been fully extracted; remaining fields require probe data
(LiveClasses.json), folded in by a later stage.

  Done — raw_doc-derived (v2 parsed tree only):
    1.  one file per module, just `module:` and empty `members:`
    2.  list class/enum/function/constant names (with kind grouping
        and primary-class promotion)
    3.  raw_doc on classes + module
    4.  expand class bodies (properties, methods, nested types)
    5.  fold listener triplets into `listenable:`; synthesize
        listener-only properties for orphan signals (loop_jump,
        Clip.notes, Song.data, ...)
    6.  property `settable` + `raw_doc`
    7.  module-level constant `value` + `type`
    8.  enum `members` (the `name: int` map) + `raw_doc`
    9.  function/method `raw_doc` + `signature` + `cpp_signature` +
        `args` (typed positional, `self` kept) + `returns`
    10. class `ancestors` (Boost.Python boilerplate stripped),
        `init_doc`, `constructable`

  Pending — probe-derived (LiveClasses.json):
    11. property `type` (probed_type) + `repr` + `element_repr`
    12. class `iterable` + `element_repr`
    13. getter return-type upgrades / mismatch reports

Usage:
    python tools/parse/build_lom_yaml.py 12.3.6
    python tools/parse/build_lom_yaml.py 12.3.6 --output /tmp/seed
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

# Pattern + filter for the parser's repr-encoded ancestors list. We strip
# the Boost.Python machinery from the chain — `Boost.Python.instance`,
# `instance`, and `object` appear on essentially every class and don't
# carry useful info for the docs surface.
_ANCESTOR_RE = re.compile(r"<class '([^']+)'>")
_BORING_BASES = {
    "Boost.Python.instance",
    "instance",
    "object",
}


def build_class_registry(
    tree: dict[str, Any],
    probe: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the cross-reference index for every class in the tree.

    Returns:
        {
          "by_repr": {class_repr: qualified_tree_path},
          "by_path": {qualified_tree_path: class_repr},   # inverse of by_repr
          "by_name": {simple_name: [qualified_paths]},
          "probe":   {class_repr: probe_entry, ...},      # LiveClasses.json
        }

    The qualified path follows the tree's nesting (e.g.,
    `Live.Song.Song.View` for the View class nested inside Song.Song),
    which is more precise than Boost.Python's repr — `<class 'Song.View'>`
    hides whether View lives at the module level or nested inside
    Song.Song. Only canonical (non-`ref:true`) class/`type` nodes are
    recorded. `by_name` is the inverted index used to qualify simple
    names in raw_doc-derived type strings; collisions (e.g. ~21 distinct
    `View` classes) keep their list intact and the type qualifier
    disambiguates by enclosing-path overlap.
    """
    by_repr: dict[str, str] = {}

    def walk(node: dict[str, Any], path: str) -> None:
        if not isinstance(node, dict):
            return
        node_type = node.get("type")
        if node_type in ("class", "type") and not node.get("ref"):
            r = node.get("repr")
            if isinstance(r, str):
                by_repr[r] = path
        for child in node.get("children", []) or []:
            child_name = child.get("name") if isinstance(child, dict) else None
            walk(child, f"{path}.{child_name}" if child_name else path)

    root_name = tree.get("name") or "Live"
    walk(tree, root_name)

    by_path: dict[str, str] = {path: repr_str for repr_str, path in by_repr.items()}
    by_name: dict[str, list[str]] = {}
    for path in by_repr.values():
        simple = path.rsplit(".", 1)[-1]
        by_name.setdefault(simple, []).append(path)

    return {
        "by_repr": by_repr,
        "by_path": by_path,
        "by_name": by_name,
        "probe": probe or {},
    }


def _qualify_probed_type(info: dict[str, Any], by_repr: dict[str, str]) -> str | None:
    """Resolve a probe property/getter's type info to a qualified path
    or builtin name. Prefer `repr` (full Boost.Python class repr) when
    present — that's the most specific identity. Otherwise fall back to
    the simple `type` name. NoneType is normalized to None (the Python
    annotation form, not the runtime class name).
    """
    repr_str = info.get("repr")
    if isinstance(repr_str, str):
        path = by_repr.get(repr_str)
        if path:
            return path
    type_str = info.get("type")
    if not type_str:
        return None
    if type_str == "NoneType":
        return "None"
    return type_str


def _qualify_element_types(
    info: dict[str, Any],
    by_repr: dict[str, str],
) -> list[str] | None:
    """Resolve a probe entry's `element_reprs` list to a deduped list of
    qualified type names. NoneType placeholders are filtered (empty
    slots aren't informative). Reprs the registry doesn't know fall
    back to the bare class name (covers builtins like `int`, `str` and
    external types).
    """
    reprs = info.get("element_reprs")
    if not reprs:
        return None
    out: list[str] = []
    seen: set[str] = set()
    for r in reprs:
        if not isinstance(r, str):
            continue
        if r == "<class 'NoneType'>":
            continue
        path = by_repr.get(r)
        if path:
            qualified = path
        else:
            m = _ANCESTOR_RE.match(r)
            qualified = m.group(1).rsplit(".", 1)[-1] if m else r
        if qualified not in seen:
            seen.add(qualified)
            out.append(qualified)
    return out or None


# Identifier names that are Python builtins / typing-module fixtures, not
# Live classes. Left alone by the type qualifier.
_BUILTIN_TYPE_NAMES = {
    "None", "True", "False", "Ellipsis",
    "int", "float", "str", "bool", "bytes", "bytearray", "complex",
    "list", "dict", "tuple", "set", "frozenset",
    "object", "type",
    "Any", "Callable", "Iterable", "Iterator", "Generator",
    "Sequence", "Mapping", "MutableMapping",
    "List", "Dict", "Tuple", "Set", "FrozenSet", "Type",
    "Optional", "Union", "Literal",
}

_TYPE_TOKEN_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")


def _prefix_overlap(a: str, b: str) -> int:
    """Length of common dot-separated prefix between two paths."""
    n = 0
    for x, y in zip(a.split("."), b.split(".")):
        if x != y:
            break
        n += 1
    return n


def _qualify_type_string(
    type_str: str,
    by_name: dict[str, list[str]],
    enclosing_path: str | None,
) -> str:
    """Replace each Live-class identifier in a type string with its
    qualified tree path; leave builtins and unknown identifiers alone.

    Composite types (`Iterable[Track]`, `Track | None`, `Tuple[A, B]`)
    are handled by tokenizing on word boundaries — punctuation and
    whitespace pass through unchanged. Names with multiple registry
    matches (e.g. `View`) are disambiguated by picking the candidate
    whose qualified path shares the longest prefix with `enclosing_path`.
    """

    def replace(match: re.Match[str]) -> str:
        token = match.group(0)
        if token in _BUILTIN_TYPE_NAMES:
            return token
        candidates = by_name.get(token)
        if not candidates:
            return token
        if len(candidates) == 1:
            return candidates[0]
        ep = enclosing_path
        if ep:
            return max(candidates, key=lambda p: _prefix_overlap(p, ep))
        # Multi-match without context — leave unqualified rather than
        # picking arbitrarily.
        return token

    return _TYPE_TOKEN_RE.sub(replace, type_str)


def _qualify_ancestors(class_node: dict[str, Any], by_repr: dict[str, str]) -> list[str]:
    """Strip Boost.Python boilerplate; resolve remaining ancestor reprs to
    qualified tree paths via `registry["by_repr"]`.

    `["<class 'LomObject.LomObject'>", "<class 'Boost.Python.instance'>"]`
    becomes `["Live.LomObject.LomObject"]`. Reprs that don't match any
    class in the registry fall back to the parser's `Module.Class` form
    (rare — covers external bases like `Exception`).
    """
    out: list[str] = []
    for ancestor_repr in class_node.get("ancestors", []) or []:
        m = _ANCESTOR_RE.match(ancestor_repr)
        if not m:
            continue
        full = m.group(1)
        if full in _BORING_BASES:
            continue
        out.append(by_repr.get(ancestor_repr, full))
    return out

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


def build_member(
    node: dict[str, Any],
    registry: dict[str, Any],
    enclosing_path: str | None = None,
) -> dict[str, Any] | None:
    """Convert a tree-node child into its YAML member dict, or None to skip.

    `enclosing_path` is the qualified path of the class containing this
    node (or None at module level). Used to disambiguate type names in
    function args/returns when the simple name has multiple registry
    matches (the canonical `View` case).
    """
    node_type = node.get("type")
    if not isinstance(node_type, str):
        return None
    kind = _KIND_BY_TYPE.get(node_type)
    if kind is None:
        return None
    name = node.get("name")
    if not name or name in SKIP_MEMBERS:
        return None

    by_repr: dict[str, str] = registry["by_repr"]
    by_name: dict[str, list[str]] = registry["by_name"]

    probe: dict[str, Any] = registry.get("probe") or {}

    out: dict[str, Any] = {"kind": kind, "name": name}
    if kind == "class":
        # Class identity: emit the qualified tree path so cross-references
        # don't have to do name-based lookup. `path` is unique even when
        # the simple name isn't (e.g., the ~21 distinct nested `View`
        # classes each get a path like Live.Song.Song.View).
        repr_str = node.get("repr")
        class_path: str | None = None
        probe_entry: dict[str, Any] | None = None
        if isinstance(repr_str, str):
            if repr_str in by_repr:
                class_path = by_repr[repr_str]
                out["path"] = class_path
            probe_entry = probe.get(repr_str)
        raw_doc = _norm_doc(node.get("raw_doc"))
        if raw_doc:
            out["raw_doc"] = raw_doc
        out["ancestors"] = _qualify_ancestors(node, by_repr)
        init_doc = _norm_doc(node.get("init_doc"))
        if init_doc:
            out["init_doc"] = init_doc
        out["constructable"] = bool(node.get("constructable"))
        # Probe-derived: iterability + element types for container classes.
        if probe_entry:
            if probe_entry.get("iterable"):
                out["iterable"] = True
            class_element_types = _qualify_element_types(probe_entry, by_repr)
            if class_element_types:
                if len(class_element_types) == 1:
                    out["element_type"] = class_element_types[0]
                else:
                    out["element_types"] = class_element_types
        # Methods inside this class qualify their type strings using the
        # class's own path as the enclosing context.
        out.update(_group_class_members(node, registry, class_path))
    elif kind == "property":
        raw_doc = _norm_doc(node.get("raw_doc"))
        if raw_doc:
            out["raw_doc"] = raw_doc
        # Probe-derived type/element_type. Look up the parent class via
        # enclosing_path → class repr → probe entry → properties[name].
        # When probe data isn't present (or didn't reach this property),
        # the type fields are simply omitted — listener-only signals
        # behave the same way (they have no real property to probe).
        prop_info: dict[str, Any] | None = None
        if enclosing_path:
            parent_repr = registry.get("by_path", {}).get(enclosing_path)
            if parent_repr:
                parent_entry = probe.get(parent_repr) or {}
                prop_info = (parent_entry.get("properties") or {}).get(name)
        if prop_info:
            type_str = _qualify_probed_type(prop_info, by_repr)
            if type_str:
                out["type"] = type_str
            element_types = _qualify_element_types(prop_info, by_repr)
            if element_types:
                if len(element_types) == 1:
                    out["element_type"] = element_types[0]
                else:
                    out["element_types"] = element_types
        # Always emit settable — read-only vs read-write is a critical
        # API attribute, not a "default" that should be implicit.
        out["settable"] = bool(node.get("settable"))
    elif kind == "enum":
        raw_doc = _norm_doc(node.get("raw_doc"))
        if raw_doc:
            out["raw_doc"] = raw_doc
        members = node.get("members")
        if isinstance(members, dict) and members:
            out["members"] = dict(members)  # preserve insertion order
    elif kind == "constant":
        # The parser stores `value` as the Python repr of the string
        # (e.g. "'Beta'"); ast.literal_eval unwraps it back to "Beta".
        # Type is always `str` in the current tree, but we emit it
        # explicitly so the field has standalone meaning.
        out["type"] = "str"
        raw_value = node.get("value")
        if isinstance(raw_value, str):
            try:
                out["value"] = ast.literal_eval(raw_value)
            except (ValueError, SyntaxError):
                out["value"] = raw_value
        elif raw_value is not None:
            out["value"] = raw_value
    elif kind == "function":
        # The parser splits Boost.Python's verbatim raw_doc into three
        # derived fields: `description` (cleaned text — what we want as
        # `raw_doc:` in YAML, per the spec), `signature` (Python form),
        # and `cpp_signature` (C++ form). The verbatim dump doesn't
        # survive into YAML.
        description = _norm_doc(node.get("description"))
        if description:
            out["raw_doc"] = description
        sig = _norm_doc(node.get("signature"))
        if sig:
            out["signature"] = sig
        cpp_sig = _norm_doc(node.get("cpp_signature"))
        if cpp_sig:
            out["cpp_signature"] = cpp_sig
        args = _convert_args(node.get("args"), by_name, enclosing_path)
        if args:
            out["args"] = args
        returns = _convert_returns(node.get("returns"), by_name, enclosing_path)
        if returns:
            out["returns"] = returns
    return out


def _convert_args(
    args: list[dict[str, Any]] | None,
    by_name: dict[str, list[str]],
    enclosing_path: str | None,
) -> list[dict[str, Any]]:
    """Convert parser arg dicts into YAML shape; qualify Live class names
    in each `type:` string against the class registry.

    `self` is kept (the SOT is unopinionated about rendering convention —
    consumers that want to elide it can do so at render time). The
    parser's resolve_signatures step has already renamed `arg1` → `self`
    on instance methods where the type matches the parent class.
    """
    if not args:
        return []
    out: list[dict[str, Any]] = []
    for arg in args:
        item: dict[str, Any] = {"name": arg["name"]}
        type_str = arg.get("type")
        if type_str:
            item["type"] = _qualify_type_string(type_str, by_name, enclosing_path)
        if arg.get("optional"):
            item["optional"] = True
            if arg.get("default") is not None:
                item["default"] = arg["default"]
        out.append(item)
    return out


def _convert_returns(
    returns: dict[str, Any] | None,
    by_name: dict[str, list[str]],
    enclosing_path: str | None,
) -> dict[str, Any] | None:
    """Convert parser returns dict into YAML shape (just `type` for now);
    qualify Live class names in the `type:` string."""
    if not returns:
        return None
    type_str = returns.get("type")
    if type_str:
        return {"type": _qualify_type_string(type_str, by_name, enclosing_path)}
    return None


def _group_class_members(
    class_node: dict[str, Any],
    registry: dict[str, Any],
    enclosing_path: str | None,
) -> dict[str, Any]:
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
        member = build_member(child, registry, enclosing_path)
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


def build_module_yaml(module_node: dict[str, Any], registry: dict[str, str]) -> dict[str, Any]:
    """Convert one module node into its YAML-shape dict."""
    module_name = module_node["name"]
    groups: dict[str, list[dict[str, Any]]] = {
        "class": [], "enum": [], "function": [], "constant": [],
    }
    primary: dict[str, Any] | None = None

    for child in module_node.get("children", []):
        if child.get("ref"):
            continue
        member = build_member(child, registry)
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
    p.add_argument("--probe", help="path to LiveClasses.json (probe data)")
    p.add_argument("--output", help="output dir")
    args = p.parse_args()

    in_path = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveTree.parsed.v2.json"
    )
    probe_path = (
        Path(args.probe)
        if args.probe
        else REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveClasses.json"
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
    probe: dict[str, Any] = {}
    if probe_path.exists():
        probe = json.loads(probe_path.read_text())
    else:
        print(f"warn: probe data not found at {probe_path}; "
              "type/element_type fields will be omitted", file=sys.stderr)
    registry = build_class_registry(tree, probe)

    written = 0
    for module_node in tree.get("children", []):
        if module_node.get("type") != "module":
            continue
        name = module_node.get("name")
        if not name:
            continue
        emit_yaml(build_module_yaml(module_node, registry), out_dir / f"{name}.yaml")
        written += 1

    print(f"Wrote {written} module YAMLs to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# endregion

#!/usr/bin/env python3
"""Parse a per-module markdown file into an in-memory module dict.

Reads `content/<v>/modules/<Module>.md` and returns a dict matching the
"natural new shape" the format spec describes. Downstream code that
needs the legacy lom-YAML shape (for the existing generators)
applies `to_legacy_shape()`; for direct use against the new format,
consume the parser output directly.

Output shape:

    {
      "module": str,
      "description": str,          # module-level prose
      "classes": [<class>, ...],   # all classes (primary + secondary + hoisted nested)
      "enums":   [<enum>, ...],
      "functions": [<function>, ...],
      "constants": [<constant>, ...],
    }

Each class dict carries: name, path, parent (if nested), ancestors,
constructable, init_doc, raw_doc, description (markdown body),
properties, methods.

Each member dict carries the fields from its fenced YAML block,
augmented with: description (markdown body prose between the fenced
block and the next heading).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

# ---------------------------------------------------------------------- regex

# Matches the frontmatter block at the top: `---\n...\n---`.
_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)

# Matches a fenced YAML block: ```yaml\n...\n```
_YAML_FENCE_RE = re.compile(r"```yaml\n(.*?)\n```", re.DOTALL)

# Matches an ATX heading line; capture the level (#'s) and the title text.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


# ---------------------------------------------------------------------- parser


def parse_module_md(path: Path) -> dict[str, Any]:
    """Parse a class-markdown file into a module dict.

    See module docstring for output shape.
    """
    text = path.read_text()
    frontmatter, body = _split_frontmatter(text)
    module_name = frontmatter.get("module")
    if not module_name:
        raise ValueError(f"{path}: missing `module:` in frontmatter")

    # Walk the body and collect H2 sections + the prose preceding the
    # first H2.
    sections = _split_h2_sections(body)

    module: dict[str, Any] = {"module": module_name}
    if "_note" in frontmatter:
        module["_note"] = frontmatter["_note"]
    if sections.preamble.strip():
        module["description"] = sections.preamble.strip() + "\n"

    classes: list[dict[str, Any]] = []
    enums: list[dict[str, Any]] = []
    functions: list[dict[str, Any]] = []
    constants: list[dict[str, Any]] = []

    for h2_title, h2_body in sections.h2_sections:
        if h2_title == "Classes":
            for cls in _parse_classes(h2_body):
                classes.append(cls)
        elif h2_title == "Enums":
            for enum in _parse_h3_entries(h2_body, expected_kind="enum"):
                enums.append(enum)
        elif h2_title == "Functions":
            for fn in _parse_h3_entries(h2_body, expected_kind="function"):
                functions.append(fn)
        elif h2_title == "Constants":
            for c in _parse_h3_entries(h2_body, expected_kind="constant"):
                constants.append(c)
        else:
            # Unrecognized H2 — warn but skip silently for now. Could
            # be authored content the spec doesn't model yet.
            print(
                f"warning: {path.name}: unknown H2 section '{h2_title}'",
                file=sys.stderr,
            )

    module["classes"] = classes
    module["enums"] = enums
    module["functions"] = functions
    module["constants"] = constants
    return module


# ---------------------------------------------------------------------- internal


class _Sections:
    """The result of splitting a markdown body into preamble + H2 sections."""

    def __init__(self, preamble: str, h2_sections: list[tuple[str, str]]) -> None:
        self.preamble = preamble
        self.h2_sections = h2_sections


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Split a markdown text into (frontmatter dict, body string)."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return fm, body


def _split_h2_sections(body: str) -> _Sections:
    """Split a body into (preamble, [(h2_title, h2_body), ...])."""
    h2_starts: list[tuple[int, str]] = []
    for m in re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE):
        h2_starts.append((m.start(), m.group(1)))
    if not h2_starts:
        return _Sections(body, [])
    preamble = body[: h2_starts[0][0]]
    sections: list[tuple[str, str]] = []
    for i, (start, title) in enumerate(h2_starts):
        # Skip the heading line itself for the body.
        line_end = body.find("\n", start)
        body_start = line_end + 1 if line_end != -1 else len(body)
        body_end = h2_starts[i + 1][0] if i + 1 < len(h2_starts) else len(body)
        sections.append((title, body[body_start:body_end]))
    return _Sections(preamble, sections)


def _split_h3_entries(section_body: str) -> list[tuple[str, str]]:
    """Inside a `## ...` section body, split into (h3_title, h3_body) chunks."""
    starts: list[tuple[int, str]] = []
    for m in re.finditer(r"^###\s+(.+?)\s*$", section_body, flags=re.MULTILINE):
        starts.append((m.start(), m.group(1)))
    entries: list[tuple[str, str]] = []
    for i, (start, title) in enumerate(starts):
        line_end = section_body.find("\n", start)
        body_start = line_end + 1 if line_end != -1 else len(section_body)
        body_end = starts[i + 1][0] if i + 1 < len(starts) else len(section_body)
        entries.append((title, section_body[body_start:body_end]))
    return entries


def _split_h4_subgroups(class_body: str) -> dict[str, str]:
    """Inside a class body, split into `Properties`/`Methods` H4 subgroups.

    Returns a `{section_title: section_body}` dict. The class-level
    fenced YAML and description prose sit before the first H4 and are
    returned under the key `_pre_h4` for the caller to consume.
    """
    starts: list[tuple[int, str]] = []
    for m in re.finditer(r"^####\s+(.+?)\s*$", class_body, flags=re.MULTILINE):
        starts.append((m.start(), m.group(1)))
    out: dict[str, str] = {}
    if not starts:
        out["_pre_h4"] = class_body
        return out
    out["_pre_h4"] = class_body[: starts[0][0]]
    for i, (start, title) in enumerate(starts):
        line_end = class_body.find("\n", start)
        body_start = line_end + 1 if line_end != -1 else len(class_body)
        body_end = starts[i + 1][0] if i + 1 < len(starts) else len(class_body)
        out[title] = class_body[body_start:body_end]
    return out


def _split_h5_members(subgroup_body: str) -> list[tuple[str, str]]:
    """Inside a `#### Properties` or `#### Methods` body, split into
    (h5_title, h5_body) chunks — one per member."""
    starts: list[tuple[int, str]] = []
    for m in re.finditer(r"^#####\s+(.+?)\s*$", subgroup_body, flags=re.MULTILINE):
        starts.append((m.start(), m.group(1)))
    members: list[tuple[str, str]] = []
    for i, (start, title) in enumerate(starts):
        line_end = subgroup_body.find("\n", start)
        body_start = line_end + 1 if line_end != -1 else len(subgroup_body)
        body_end = (
            starts[i + 1][0] if i + 1 < len(starts) else len(subgroup_body)
        )
        members.append((title, subgroup_body[body_start:body_end]))
    return members


def _extract_fenced_yaml(body: str) -> tuple[dict[str, Any], str]:
    """Pull the first ```yaml ... ``` block from the body. Returns
    (parsed_yaml, body_with_yaml_removed)."""
    m = _YAML_FENCE_RE.search(body)
    if not m:
        return {}, body
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(
            f"fenced YAML block did not parse to a dict; got {type(data).__name__}"
        )
    remainder = body[: m.start()] + body[m.end():]
    return data, remainder


def _description_prose(body: str) -> str:
    """Strip leading / trailing whitespace from a body chunk to produce
    the description string."""
    return body.strip()


def _unescape_heading(title: str) -> str:
    """Strip surrounding backticks from a heading name. Member names
    with markdown-significant characters (`__init__`, `_live_ptr`)
    are backtick-wrapped in source to survive markdown emphasis
    parsing; the parser unwraps them here.
    """
    title = title.strip()
    if title.startswith("`") and title.endswith("`") and len(title) >= 2:
        return title[1:-1]
    return title


# ---------------------------------------------------------------------- classes


def _parse_classes(classes_section_body: str) -> list[dict[str, Any]]:
    """Parse all class entries from a `## Classes` section body."""
    classes: list[dict[str, Any]] = []
    for h3_title, h3_body in _split_h3_entries(classes_section_body):
        classes.append(_parse_class(h3_title, h3_body))
    return classes


def _parse_class(name: str, body: str) -> dict[str, Any]:
    """Parse one class entry — its fenced YAML block, description, and
    sub-grouped members."""
    h4_groups = _split_h4_subgroups(body)
    pre_h4 = h4_groups.pop("_pre_h4", "")
    yaml_data, prose = _extract_fenced_yaml(pre_h4)
    description = _description_prose(prose)

    cls: dict[str, Any] = {"name": _unescape_heading(name)}
    cls.update(yaml_data)
    if description:
        cls["description"] = description

    if "Properties" in h4_groups:
        cls["properties"] = [
            _parse_member(t, b, expected_kind="property")
            for t, b in _split_h5_members(h4_groups["Properties"])
        ]
    if "Methods" in h4_groups:
        cls["methods"] = [
            _parse_member(t, b, expected_kind="method")
            for t, b in _split_h5_members(h4_groups["Methods"])
        ]
    return cls


def _parse_member(name: str, body: str, *, expected_kind: str) -> dict[str, Any]:
    """Parse one property / method entry from its H5 body."""
    yaml_data, prose = _extract_fenced_yaml(body)
    description = _description_prose(prose)
    member: dict[str, Any] = {"name": _unescape_heading(name)}
    actual_kind = yaml_data.get("kind")
    if actual_kind and actual_kind != expected_kind:
        print(
            f"warning: '{name}' under '{expected_kind}s' but kind: {actual_kind}",
            file=sys.stderr,
        )
    member.update(yaml_data)
    if description:
        member["description"] = description
    return member


def _parse_h3_entries(
    section_body: str, *, expected_kind: str,
) -> list[dict[str, Any]]:
    """Parse H3-level entries (enums / functions / constants) from a section."""
    entries: list[dict[str, Any]] = []
    for h3_title, h3_body in _split_h3_entries(section_body):
        yaml_data, prose = _extract_fenced_yaml(h3_body)
        description = _description_prose(prose)
        entry: dict[str, Any] = {"name": _unescape_heading(h3_title)}
        actual_kind = yaml_data.get("kind")
        if actual_kind and actual_kind != expected_kind:
            print(
                f"warning: '{h3_title}' under '{expected_kind}s' but kind: {actual_kind}",
                file=sys.stderr,
            )
        entry.update(yaml_data)
        if description:
            entry["description"] = description
        entries.append(entry)
    return entries


# ---------------------------------------------------------------------- legacy adapter


def to_legacy_shape(new: dict[str, Any]) -> dict[str, Any]:
    """Translate parser output to the legacy YAML-loader dict shape.

    Roughly the inverse of `tools/parse/md_emit.py`:

    - Hoisted nested classes / enums / constants get re-grafted as children
      of their `parent:` class.
    - The class whose name matches the module name moves out of `classes:`
      into a one-element `primary_class:` list.
    - Per-member: `kind:` discriminator dropped (implicit in old shape);
      `refinement: {<key>: {...}}` blocks convert back to `*_override:`
      siblings (`type_override`, `name_override`, `element_type_override`);
      `listenable: true` expands to the standard
      `add_X_listener / remove_X_listener / X_has_listener` triplet.
    - Method arg lists get an implicit `self` arg prepended, typed to
      the containing class's qualified path.

    Used during the dual-format-loader transition (migration phase 3):
    the existing generators consume the legacy shape; this adapter
    lets them read markdown sources without an internal rewrite.
    """
    module_name = new["module"]
    legacy: dict[str, Any] = {"module": module_name}
    if new.get("description"):
        legacy["description"] = new["description"]
    if new.get("_note"):
        legacy["_note"] = new["_note"]

    # Bucket hoisted children by parent for re-grafting.
    classes_by_parent: dict[str | None, list[dict[str, Any]]] = {}
    enums_by_parent: dict[str | None, list[dict[str, Any]]] = {}
    constants_by_parent: dict[str | None, list[dict[str, Any]]] = {}
    for cls in new.get("classes", []):
        classes_by_parent.setdefault(cls.get("parent"), []).append(cls)
    for enum in new.get("enums", []):
        enums_by_parent.setdefault(enum.get("parent"), []).append(enum)
    for const in new.get("constants", []):
        constants_by_parent.setdefault(const.get("parent"), []).append(const)

    def convert_class(cls: dict[str, Any]) -> dict[str, Any]:
        name = cls["name"]
        path = cls.get("path", "")
        result: dict[str, Any] = {"name": name}
        for key in (
            "path", "ancestors", "init_doc", "constructable", "raw_doc",
            "iterable", "container", "parametric",
        ):
            if key in cls:
                result[key] = cls[key]
        # Class-level element_type_override — reconstruct from
        # `element_type` + `refinement.element_type` if present.
        if "element_type" in cls and "refinement" in cls and "element_type" in cls["refinement"]:
            ref_et = cls["refinement"]["element_type"]
            override: dict[str, Any] = {"value": cls["element_type"]}
            if "confidence" in ref_et:
                override["confidence"] = ref_et["confidence"]
            if "sources" in ref_et:
                override["source"] = ref_et["sources"]
            result["element_type_override"] = override
        elif "element_type" in cls:
            result["element_type"] = cls["element_type"]
        if "description" in cls:
            result["description"] = cls["description"]
        if "properties" in cls:
            result["properties"] = [_convert_property(p) for p in cls["properties"]]
        if "methods" in cls:
            result["methods"] = [
                _convert_method(m, owning_class_path=path) for m in cls["methods"]
            ]
        # Re-graft hoisted children.
        nested_classes = classes_by_parent.get(name, [])
        if nested_classes:
            result["classes"] = [convert_class(c) for c in nested_classes]
        nested_enums = enums_by_parent.get(name, [])
        if nested_enums:
            result["enums"] = [_convert_enum(e) for e in nested_enums]
        nested_constants = constants_by_parent.get(name, [])
        if nested_constants:
            result["constants"] = [_convert_constant(c) for c in nested_constants]
        return result

    # Split classes into primary (name matches module) + others.
    top_level_classes = classes_by_parent.get(None, [])
    primary: list[dict[str, Any]] = []
    others: list[dict[str, Any]] = []
    for cls in top_level_classes:
        converted = convert_class(cls)
        if cls["name"] == module_name:
            primary.append(converted)
        else:
            others.append(converted)
    legacy["primary_class"] = primary
    legacy["classes"] = others
    legacy["enums"] = [_convert_enum(e) for e in enums_by_parent.get(None, [])]
    legacy["functions"] = [
        _convert_function(f) for f in new.get("functions", [])
    ]
    legacy["constants"] = [
        _convert_constant(c) for c in constants_by_parent.get(None, [])
    ]
    return legacy


def _convert_property(prop: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"name": prop["name"]}
    refinement = prop.get("refinement") or {}

    # type / type_override — if `refinement.type` exists, the resolved
    # `type:` is the override value; revert to probed for legacy `type:`.
    if "type" in refinement:
        ref_type = refinement["type"]
        if "probed" in ref_type:
            result["type"] = ref_type["probed"]
        elif "type" in prop:
            result["type"] = prop["type"]
        override: dict[str, Any] = {"value": prop["type"]}
        if "confidence" in ref_type:
            override["confidence"] = ref_type["confidence"]
        if "sources" in ref_type:
            override["source"] = ref_type["sources"]
        result["type_override"] = override
    elif "type" in prop:
        result["type"] = prop["type"]

    # element_type / element_type_override — only the override side
    # survives in legacy; the resolved `element_type:` field is dropped.
    if "element_type" in refinement:
        ref_et = refinement["element_type"]
        override = {"value": prop["element_type"]}
        if "confidence" in ref_et:
            override["confidence"] = ref_et["confidence"]
        if "sources" in ref_et:
            override["source"] = ref_et["sources"]
        result["element_type_override"] = override

    if "settable" in prop:
        result["settable"] = prop["settable"]

    # Expand `listenable: true` to the standard triplet.
    listenable = prop.get("listenable")
    if listenable is True:
        n = prop["name"]
        result["listenable"] = [
            f"add_{n}_listener",
            f"remove_{n}_listener",
            f"{n}_has_listener",
        ]
    elif isinstance(listenable, list):
        result["listenable"] = listenable

    if "raw_doc" in prop:
        result["raw_doc"] = prop["raw_doc"]
    if "description" in prop:
        result["description"] = prop["description"]
    if prop.get("_synthesized"):
        result["_synthesized"] = prop["_synthesized"]
    if "_synthesis_note" in prop:
        result["_synthesis_note"] = prop["_synthesis_note"]
    if "deprecated" in prop:
        result["deprecated"] = prop["deprecated"]
    return result


def _convert_arg(arg: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    refinement = arg.get("refinement") or {}

    # name + name_override
    if "name" in refinement:
        ref_name = refinement["name"]
        if "probed" in ref_name:
            result["name"] = ref_name["probed"]
        else:
            result["name"] = arg["name"]
        override: dict[str, Any] = {"value": arg["name"]}
        if "sources" in ref_name:
            override["source"] = ref_name["sources"]
        result["name_override"] = override
    else:
        result["name"] = arg["name"]

    # type + type_override
    if "type" in refinement:
        ref_type = refinement["type"]
        if "probed" in ref_type:
            result["type"] = ref_type["probed"]
        elif "type" in arg:
            result["type"] = arg["type"]
        override = {"value": arg["type"]}
        if "confidence" in ref_type:
            override["confidence"] = ref_type["confidence"]
        if "sources" in ref_type:
            override["source"] = ref_type["sources"]
        result["type_override"] = override
    elif "type" in arg:
        result["type"] = arg["type"]

    if arg.get("optional"):
        result["optional"] = arg["optional"]
    if "default" in arg:
        result["default"] = arg["default"]
    return result


def _convert_method(
    method: dict[str, Any], *, owning_class_path: str = "",
) -> dict[str, Any]:
    result: dict[str, Any] = {"name": method["name"]}
    if "raw_doc" in method:
        result["raw_doc"] = method["raw_doc"]
    if "signature" in method:
        result["signature"] = method["signature"]
    if "cpp_signature" in method:
        result["cpp_signature"] = method["cpp_signature"]

    # Restore the implicit `self` arg. Defaults to the owning class's
    # path; override via the method's `self_type:` field for methods
    # the probe recorded with an inherited (parent-class) self type.
    self_type = method.get("self_type") or owning_class_path
    args = []
    if self_type:
        args.append({"name": "self", "type": self_type})
    for arg in method.get("args", []):
        args.append(_convert_arg(arg))
    if args:
        result["args"] = args

    returns = method.get("returns") or {}
    if returns:
        r = _convert_returns(returns)
        if r:
            result["returns"] = r

    # Parameterized-observable methods carry a listener triplet.
    # Expand `listenable: true` to the explicit triplet derived from
    # the method's name.
    if method.get("listenable") is True:
        n = method["name"]
        result["listenable"] = [
            f"add_{n}_listener",
            f"remove_{n}_listener",
            f"{n}_has_listener",
        ]
    elif isinstance(method.get("listenable"), list):
        result["listenable"] = method["listenable"]

    if "description" in method:
        result["description"] = method["description"]
    if "deprecated" in method:
        result["deprecated"] = method["deprecated"]
    return result


def _convert_function(fn: dict[str, Any]) -> dict[str, Any]:
    # Module-level function: no `self` arg. Otherwise same shape as method.
    result: dict[str, Any] = {"name": fn["name"]}
    if "raw_doc" in fn:
        result["raw_doc"] = fn["raw_doc"]
    if "signature" in fn:
        result["signature"] = fn["signature"]
    if "cpp_signature" in fn:
        result["cpp_signature"] = fn["cpp_signature"]
    if "args" in fn:
        result["args"] = [_convert_arg(a) for a in fn["args"]]
    returns = fn.get("returns") or {}
    if returns:
        r = _convert_returns(returns)
        if r:
            result["returns"] = r
    if "description" in fn:
        result["description"] = fn["description"]
    return result


def _convert_returns(returns: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    refinement = returns.get("refinement") or {}
    if "type" in refinement:
        ref_type = refinement["type"]
        if "probed" in ref_type:
            result["type"] = ref_type["probed"]
        elif "type" in returns:
            result["type"] = returns["type"]
        override: dict[str, Any] = {"value": returns["type"]}
        if "confidence" in ref_type:
            override["confidence"] = ref_type["confidence"]
        if "sources" in ref_type:
            override["source"] = ref_type["sources"]
        result["type_override"] = override
    elif "type" in returns:
        result["type"] = returns["type"]
    return result


def _convert_enum(enum: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"name": enum["name"]}
    for key in ("path", "members", "raw_doc", "description"):
        if key in enum:
            result[key] = enum[key]
    return result


def _convert_constant(const: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"name": const["name"]}
    for key in ("type", "value", "raw_doc", "description"):
        if key in const:
            result[key] = const[key]
    return result


# ---------------------------------------------------------------------- CLI


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Module markdown file to parse")
    parser.add_argument(
        "--format", choices=("yaml", "json", "repr"), default="yaml",
        help="Output format (default: yaml)",
    )
    parser.add_argument(
        "--legacy", action="store_true",
        help="Emit the legacy YAML-loader shape (for generator compatibility)",
    )
    args = parser.parse_args()
    data = parse_module_md(Path(args.path))
    if args.legacy:
        data = to_legacy_shape(data)
    if args.format == "yaml":
        yaml.dump(data, sys.stdout, sort_keys=False, allow_unicode=True, width=120)
    elif args.format == "json":
        import json
        json.dump(data, sys.stdout, indent=2, default=str)
        print()
    else:
        from pprint import pprint
        pprint(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())

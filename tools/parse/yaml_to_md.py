#!/usr/bin/env python3
"""One-shot converter from a lom YAML module file to the new
markdown midpoint format.

Usage: yaml_to_md.py <Module.yaml>  →  writes alongside as Module.md

Mechanical translation. Output is meant for manual review and tweak;
not intended to be roundtrip-pure with the parser. Used to bootstrap
the canonical example and (eventually) drive migration phase 4.
"""
from __future__ import annotations

import io
import sys
from pathlib import Path
from typing import Any

import yaml


# Force block-scalar style for any multi-line string so embedded
# `init_doc`, `raw_doc`, refinement-source items render readably
# inside the fenced YAML blocks. Without this, PyYAML's heuristics
# pick single-quoted flow style and the embedded `\n`s become hard to
# read.
def _str_presenter(dumper: yaml.Dumper, data: str):
    if "\n" in data:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|",
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, _str_presenter)


# ---------------------------------------------------------------------- helpers


def _block_text(text: str | None) -> str:
    """Return raw text with normalized line endings. Used for raw_doc."""
    if text is None:
        return ""
    return text.rstrip()


def _emit_yaml_block(data: dict[str, Any], indent: int = 0) -> str:
    """Render a fenced YAML block for member-frontmatter use."""
    buf = io.StringIO()
    yaml.dump(
        data, buf,
        default_flow_style=False, sort_keys=False, allow_unicode=True,
        width=120,
    )
    body = buf.getvalue().rstrip()
    if indent:
        prefix = " " * indent
        body = "\n".join(prefix + line if line else line for line in body.split("\n"))
    return f"```yaml\n{body}\n```"


def _normalize_sources(source: Any) -> list[str]:
    """Coerce a YAML `source:` field to a list-of-strings, stripping
    inner whitespace consistently."""
    if source is None:
        return []
    if isinstance(source, str):
        return [_collapse(source)]
    if isinstance(source, list):
        return [_collapse(s) if isinstance(s, str) else str(s) for s in source]
    return [str(source)]


def _collapse(s: str) -> str:
    """Collapse internal newlines + multiple spaces to single spaces."""
    return " ".join(s.split())


def _convert_refinement(override: dict[str, Any]) -> dict[str, Any]:
    """Convert a legacy `<field>_override:` block to the new refinement
    fields. `override` is the contents of a `*_override:` mapping."""
    out: dict[str, Any] = {}
    if "confidence" in override:
        out["confidence"] = override["confidence"]
    if "source" in override:
        out["sources"] = _normalize_sources(override["source"])
    return out


# ---------------------------------------------------------------------- members


def _emit_property(prop: dict[str, Any]) -> list[str]:
    """Render one property as: `##### name\\n\\n<fenced yaml>\\n\\n<prose>`."""
    name = prop["name"]
    data: dict[str, Any] = {"kind": "property"}

    # Resolve type with any override.
    probed_type = prop.get("type")
    type_override = prop.get("type_override")
    if type_override and "value" in type_override:
        data["type"] = type_override["value"]
    elif probed_type is not None:
        data["type"] = probed_type

    if "settable" in prop:
        data["settable"] = prop["settable"]

    listenable = prop.get("listenable")
    if listenable:
        # Currently lose the explicit triplet method list — `true`
        # implies the standard add_X / remove_X / X_has_listener
        # shape. Members with non-standard triplets need manual fixup.
        data["listenable"] = True

    if prop.get("raw_doc"):
        data["raw_doc"] = _block_text(prop["raw_doc"])

    # Refinement on the property's type.
    if type_override and "value" in type_override:
        refinement = _convert_refinement(type_override)
        if probed_type is not None:
            refinement = {"probed": probed_type, **refinement}
        data["refinement"] = refinement

    # element_type_override for Vector-bearing properties stays as-is
    # for now — it's a different concern from the property's own type
    # refinement. Carried verbatim under its current key.
    if "element_type_override" in prop:
        eto = prop["element_type_override"]
        data["element_type_override"] = {
            "value": eto["value"],
            **({"confidence": eto["confidence"]} if "confidence" in eto else {}),
            **({"sources": _normalize_sources(eto.get("source"))}
               if "source" in eto else {}),
        }

    description = prop.get("description") or ""

    lines = [f"##### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


def _convert_arg(arg: dict[str, Any]) -> dict[str, Any]:
    """Convert a method arg with its name_override / type_override."""
    out: dict[str, Any] = {}
    name_override = arg.get("name_override")
    if name_override and "value" in name_override:
        out["name"] = name_override["value"]
    else:
        out["name"] = arg["name"]

    type_override = arg.get("type_override")
    probed_type = arg.get("type")
    if type_override and "value" in type_override:
        out["type"] = type_override["value"]
    elif probed_type is not None:
        out["type"] = probed_type

    if arg.get("optional"):
        out["optional"] = True
    if "default" in arg:
        out["default"] = arg["default"]

    # Refinement: collect both name and type if either is overridden.
    name_ref = None
    type_ref = None
    if name_override and "value" in name_override:
        name_ref = {"probed": arg["name"]}
        if "source" in name_override:
            name_ref["sources"] = _normalize_sources(name_override["source"])
    if type_override and "value" in type_override:
        type_ref = {"probed": probed_type}
        if "confidence" in type_override:
            type_ref["confidence"] = type_override["confidence"]
        if "source" in type_override:
            type_ref["sources"] = _normalize_sources(type_override["source"])

    if name_ref or type_ref:
        ref: dict[str, Any] = {}
        if name_ref:
            ref["name"] = name_ref
        if type_ref:
            ref["type"] = type_ref
        out["refinement"] = ref

    return out


def _emit_method(method: dict[str, Any]) -> list[str]:
    name = method["name"]
    data: dict[str, Any] = {"kind": "method"}

    if "signature" in method:
        data["signature"] = method["signature"]
    if "cpp_signature" in method:
        data["cpp_signature"] = method["cpp_signature"]

    args = method.get("args") or []
    # Drop the implicit `self` arg.
    args = [a for a in args if a.get("name") != "self"]
    if args:
        data["args"] = [_convert_arg(a) for a in args]

    returns = method.get("returns") or {}
    if returns:
        rdata: dict[str, Any] = {}
        rtype_override = returns.get("type_override")
        probed_rtype = returns.get("type")
        if rtype_override and "value" in rtype_override:
            rdata["type"] = rtype_override["value"]
        elif probed_rtype is not None:
            rdata["type"] = probed_rtype
        if rtype_override and "value" in rtype_override:
            refinement: dict[str, Any] = {"probed": probed_rtype}
            if "confidence" in rtype_override:
                refinement["confidence"] = rtype_override["confidence"]
            if "source" in rtype_override:
                refinement["sources"] = _normalize_sources(rtype_override["source"])
            rdata["refinement"] = refinement
        if rdata:
            data["returns"] = rdata

    if method.get("raw_doc"):
        data["raw_doc"] = _block_text(method["raw_doc"])

    description = method.get("description") or ""

    lines = [f"##### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


def _emit_enum(enum: dict[str, Any], parent: str | None = None) -> list[str]:
    name = enum["name"]
    data: dict[str, Any] = {"kind": "enum"}
    if parent:
        data["parent"] = parent
    if "path" in enum:
        data["path"] = enum["path"]
    if enum.get("members"):
        data["members"] = enum["members"]
    if enum.get("raw_doc"):
        data["raw_doc"] = _block_text(enum["raw_doc"])

    description = enum.get("description") or ""

    lines = [f"### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


def _emit_function(fn: dict[str, Any]) -> list[str]:
    name = fn["name"]
    data: dict[str, Any] = {"kind": "function"}
    if "signature" in fn:
        data["signature"] = fn["signature"]
    if "cpp_signature" in fn:
        data["cpp_signature"] = fn["cpp_signature"]
    args = fn.get("args") or []
    if args:
        data["args"] = [_convert_arg(a) for a in args]
    returns = fn.get("returns") or {}
    if returns:
        rdata: dict[str, Any] = {}
        rtype_override = returns.get("type_override")
        probed_rtype = returns.get("type")
        if rtype_override and "value" in rtype_override:
            rdata["type"] = rtype_override["value"]
        elif probed_rtype is not None:
            rdata["type"] = probed_rtype
        if rtype_override and "value" in rtype_override:
            refinement: dict[str, Any] = {"probed": probed_rtype}
            if "confidence" in rtype_override:
                refinement["confidence"] = rtype_override["confidence"]
            if "source" in rtype_override:
                refinement["sources"] = _normalize_sources(rtype_override["source"])
            rdata["refinement"] = refinement
        if rdata:
            data["returns"] = rdata
    if fn.get("raw_doc"):
        data["raw_doc"] = _block_text(fn["raw_doc"])

    description = fn.get("description") or ""
    lines = [f"### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


def _emit_constant(const: dict[str, Any]) -> list[str]:
    name = const["name"]
    data: dict[str, Any] = {"kind": "constant"}
    if "type" in const:
        data["type"] = const["type"]
    if "value" in const:
        data["value"] = const["value"]
    if const.get("raw_doc"):
        data["raw_doc"] = _block_text(const["raw_doc"])

    description = const.get("description") or ""
    lines = [f"### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


# ---------------------------------------------------------------------- classes


def _emit_class(
    cls: dict[str, Any],
    hoisted_classes: list[tuple[str, dict[str, Any]]],
    hoisted_enums: list[tuple[str, dict[str, Any]]],
    parent: str | None = None,
) -> list[str]:
    name = cls["name"]
    data: dict[str, Any] = {"kind": "class"}
    if "path" in cls:
        data["path"] = cls["path"]
    if parent:
        data["parent"] = parent
    if cls.get("ancestors"):
        data["ancestors"] = cls["ancestors"]
    if "init_doc" in cls:
        data["init_doc"] = _block_text(cls["init_doc"])
    if "constructable" in cls:
        data["constructable"] = cls["constructable"]
    if cls.get("raw_doc"):
        data["raw_doc"] = _block_text(cls["raw_doc"])

    description = cls.get("description") or ""

    lines = [f"### {name}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")

    properties = cls.get("properties") or []
    methods = cls.get("methods") or []
    nested_classes = cls.get("classes") or []
    nested_enums = cls.get("enums") or []

    if properties:
        lines.append("#### Properties")
        lines.append("")
        for p in properties:
            lines.extend(_emit_property(p))

    if methods:
        lines.append("#### Methods")
        lines.append("")
        for m in methods:
            lines.extend(_emit_method(m))

    # Defer rendering of nested classes/enums; they will be hoisted to
    # the file's top level by the caller.
    for nc in nested_classes:
        hoisted_classes.append((name, nc))
    for ne in nested_enums:
        hoisted_enums.append((name, ne))

    return lines


# ---------------------------------------------------------------------- module


def convert(module: dict[str, Any]) -> str:
    """Convert a parsed lom-module dict to markdown text."""
    out: list[str] = []
    # Frontmatter.
    out.append("---")
    out.append(f"module: {module['module']}")
    out.append("---")
    out.append("")
    # Module-level prose.
    description = module.get("description")
    if description:
        out.append(description.strip())
        out.append("")

    primary_classes = module.get("primary_class") or []
    other_classes = module.get("classes") or []
    enums = module.get("enums") or []
    functions = module.get("functions") or []
    constants = module.get("constants") or []

    # Collect nested classes/enums as we walk; they hoist to top-level
    # under ## Classes / ## Enums with their `parent:` field set.
    hoisted_classes: list[tuple[str, dict[str, Any]]] = []
    hoisted_enums: list[tuple[str, dict[str, Any]]] = []

    all_classes = list(primary_classes) + list(other_classes)
    if all_classes:
        out.append("## Classes")
        out.append("")
        for cls in all_classes:
            out.extend(_emit_class(cls, hoisted_classes, hoisted_enums))
        for parent_name, nested_cls in hoisted_classes:
            # Recursively hoist deeper nestings as well.
            out.extend(_emit_class(
                nested_cls, hoisted_classes, hoisted_enums,
                parent=parent_name,
            ))

    if enums or hoisted_enums:
        out.append("## Enums")
        out.append("")
        for e in enums:
            out.extend(_emit_enum(e))
        for parent_name, nested_enum in hoisted_enums:
            out.extend(_emit_enum(nested_enum, parent=parent_name))

    if functions:
        out.append("## Functions")
        out.append("")
        for fn in functions:
            out.extend(_emit_function(fn))

    if constants:
        out.append("## Constants")
        out.append("")
        for c in constants:
            out.extend(_emit_constant(c))

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: yaml_to_md.py <Module.yaml>", file=sys.stderr)
        return 2
    in_path = Path(sys.argv[1])
    module = yaml.safe_load(in_path.read_text())
    out_path = (
        in_path.parent.parent / "modules" / (in_path.stem + ".md")
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(convert(module))
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

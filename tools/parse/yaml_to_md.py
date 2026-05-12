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


# Member names with markdown-significant characters need backticking in
# headings so prettier / CommonMark don't mangle them — `__init__`
# rendered bare becomes `**init**` (bold) on round-trip. Wrapping in
# backticks tells the renderer this is inline code, preserved verbatim.
def _escape_heading_name(name: str) -> str:
    if name.startswith("_") or name.endswith("_") or "__" in name or "*" in name:
        return f"`{name}`"
    return name


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

    # element_type — present when the property returns a Vector-like
    # whose element type is refined. The probe doesn't typically
    # report the element type; it's filled in by hand via the legacy
    # `element_type_override:` block which we restructure here under
    # `refinement.element_type`.
    element_override = prop.get("element_type_override")
    if element_override and "value" in element_override:
        data["element_type"] = element_override["value"]

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

    # Refinement — always-nested form. Sub-keys: type, element_type.
    refinement: dict[str, Any] = {}
    if type_override and "value" in type_override:
        sub: dict[str, Any] = {"probed": probed_type}
        if "confidence" in type_override:
            sub["confidence"] = type_override["confidence"]
        if "source" in type_override:
            sub["sources"] = _normalize_sources(type_override["source"])
        refinement["type"] = sub
    if element_override and "value" in element_override:
        sub2: dict[str, Any] = {}
        if "confidence" in element_override:
            sub2["confidence"] = element_override["confidence"]
        if "source" in element_override:
            sub2["sources"] = _normalize_sources(element_override["source"])
        refinement["element_type"] = sub2
    if refinement:
        data["refinement"] = refinement

    if prop.get("_synthesized"):
        data["_synthesized"] = prop["_synthesized"]
    if prop.get("_synthesis_note"):
        data["_synthesis_note"] = _block_text(prop["_synthesis_note"])
    if "deprecated" in prop:
        data["deprecated"] = prop["deprecated"]

    description = prop.get("description") or ""

    lines = [f"##### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
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


def _emit_method(method: dict[str, Any], owning_class_path: str = "") -> list[str]:
    name = method["name"]
    data: dict[str, Any] = {"kind": "method"}

    if "signature" in method:
        data["signature"] = method["signature"]
    if "cpp_signature" in method:
        data["cpp_signature"] = method["cpp_signature"]

    args = method.get("args") or []
    # Drop the implicit `self` arg from the markdown's args list — it's
    # always present in the legacy YAML, never authored, restored on
    # the adapter side. BUT: if the probed `self` type differs from
    # the owning class (Boost.Python sometimes records `self` typed to
    # the class that *declared* the method, even when inherited), we
    # preserve that as a top-level `self_type:` field on the method
    # so the round-trip is clean.
    self_arg = next((a for a in args if a.get("name") == "self"), None)
    if (
        self_arg
        and owning_class_path
        and self_arg.get("type")
        and self_arg["type"] != owning_class_path
    ):
        data["self_type"] = self_arg["type"]
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
        # Always-nested refinement: sub-key `type` for type overrides.
        if rtype_override and "value" in rtype_override:
            sub: dict[str, Any] = {"probed": probed_rtype}
            if "confidence" in rtype_override:
                sub["confidence"] = rtype_override["confidence"]
            if "source" in rtype_override:
                sub["sources"] = _normalize_sources(rtype_override["source"])
            rdata["refinement"] = {"type": sub}
        if rdata:
            data["returns"] = rdata

    # Parameterized-observable methods (e.g. `Application.View.is_view_visible`)
    # carry a `listenable:` triplet on the method itself — the listener
    # callbacks take the same first arg as the method. Preserved as
    # `listenable: true` shorthand; the parser/adapter expands the
    # triplet from the method name.
    if method.get("listenable"):
        data["listenable"] = True

    if method.get("raw_doc"):
        data["raw_doc"] = _block_text(method["raw_doc"])

    if "deprecated" in method:
        data["deprecated"] = method["deprecated"]

    description = method.get("description") or ""

    lines = [f"##### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
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

    lines = [f"### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
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
            sub: dict[str, Any] = {"probed": probed_rtype}
            if "confidence" in rtype_override:
                sub["confidence"] = rtype_override["confidence"]
            if "source" in rtype_override:
                sub["sources"] = _normalize_sources(rtype_override["source"])
            rdata["refinement"] = {"type": sub}
        if rdata:
            data["returns"] = rdata
    if fn.get("raw_doc"):
        data["raw_doc"] = _block_text(fn["raw_doc"])
    if "deprecated" in fn:
        data["deprecated"] = fn["deprecated"]

    description = fn.get("description") or ""
    lines = [f"### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")
    return lines


def _emit_constant(const: dict[str, Any], parent: str | None = None) -> list[str]:
    name = const["name"]
    data: dict[str, Any] = {"kind": "constant"}
    if parent:
        data["parent"] = parent
    if "type" in const:
        data["type"] = const["type"]
    if "value" in const:
        data["value"] = const["value"]
    if const.get("raw_doc"):
        data["raw_doc"] = _block_text(const["raw_doc"])

    description = const.get("description") or ""
    lines = [f"### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
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
    hoisted_constants: list[tuple[str, dict[str, Any]]],
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
    # Container-class flags (`iterable`, `container`, `parametric`) preserved
    # verbatim for Vector / XVector classes.
    for flag in ("iterable", "container", "parametric"):
        if flag in cls:
            data[flag] = cls[flag]
    # Class-level element_type — for Vector classes where the element
    # type is refined via `element_type_override`. Same shape as on a
    # property: top-level `element_type:` for the resolved value,
    # `refinement.element_type` for the metadata.
    element_override = cls.get("element_type_override")
    element_type = cls.get("element_type")
    if element_override and "value" in element_override:
        data["element_type"] = element_override["value"]
    elif element_type is not None:
        data["element_type"] = element_type
    if cls.get("raw_doc"):
        data["raw_doc"] = _block_text(cls["raw_doc"])
    if element_override and "value" in element_override:
        sub: dict[str, Any] = {}
        if "confidence" in element_override:
            sub["confidence"] = element_override["confidence"]
        if "source" in element_override:
            sub["sources"] = _normalize_sources(element_override["source"])
        data["refinement"] = {"element_type": sub}

    description = cls.get("description") or ""

    lines = [f"### {_escape_heading_name(name)}", "", _emit_yaml_block(data)]
    if description.strip():
        lines.append("")
        lines.append(description.strip())
    lines.append("")

    properties = cls.get("properties") or []
    methods = cls.get("methods") or []
    nested_classes = cls.get("classes") or []
    nested_enums = cls.get("enums") or []
    nested_constants = cls.get("constants") or []

    if properties:
        lines.append("#### Properties")
        lines.append("")
        for p in properties:
            lines.extend(_emit_property(p))

    if methods:
        lines.append("#### Methods")
        lines.append("")
        owning_path = cls.get("path", "")
        for m in methods:
            lines.extend(_emit_method(m, owning_path))

    # Defer rendering of nested classes / enums / constants; they will
    # be hoisted to the file's top level by the caller with a `parent:`
    # field marking the structural nesting.
    for nc in nested_classes:
        hoisted_classes.append((name, nc))
    for ne in nested_enums:
        hoisted_enums.append((name, ne))
    for nc in nested_constants:
        hoisted_constants.append((name, nc))

    return lines


# ---------------------------------------------------------------------- module


def convert(module: dict[str, Any]) -> str:
    """Convert a parsed lom-module dict to markdown text."""
    out: list[str] = []
    # Frontmatter.
    frontmatter: dict[str, Any] = {"module": module["module"]}
    if "_note" in module:
        frontmatter["_note"] = _block_text(module["_note"])
    out.append("---")
    fm_buf = io.StringIO()
    yaml.dump(
        frontmatter, fm_buf,
        default_flow_style=False, sort_keys=False, allow_unicode=True,
        width=120,
    )
    out.append(fm_buf.getvalue().rstrip())
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

    # Collect nested classes / enums / constants as we walk; they
    # hoist to top-level under ## Classes / ## Enums / ## Constants
    # with their `parent:` field set.
    hoisted_classes: list[tuple[str, dict[str, Any]]] = []
    hoisted_enums: list[tuple[str, dict[str, Any]]] = []
    hoisted_constants: list[tuple[str, dict[str, Any]]] = []

    all_classes = list(primary_classes) + list(other_classes)
    if all_classes:
        out.append("## Classes")
        out.append("")
        for cls in all_classes:
            out.extend(_emit_class(
                cls, hoisted_classes, hoisted_enums, hoisted_constants,
            ))
        for parent_name, nested_cls in hoisted_classes:
            # Recursively hoist deeper nestings as well.
            out.extend(_emit_class(
                nested_cls,
                hoisted_classes, hoisted_enums, hoisted_constants,
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

    if constants or hoisted_constants:
        out.append("## Constants")
        out.append("")
        for c in constants:
            out.extend(_emit_constant(c))
        for parent_name, nested_const in hoisted_constants:
            out.extend(_emit_constant(nested_const, parent=parent_name))

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

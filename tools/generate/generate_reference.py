#!/usr/bin/env python3
"""Generate Starlight (Astro) MDX reference pages from stubs/<v>/lom/*.yaml.

Phase 1 of the documentation roadmap (`doc/reference-roadmap.md`): mechanical
translation of what the parser already knows. Built incrementally per the
step-ladder — each step adds one layer of detail to the rendered output.

Paused state: through Step 4 (property types). Module skeletons, syntax-
highlighted class/enum/function signatures, main-class promotion, class
descriptions, property listing with linkified types. No methods rendered
yet, no enum members, no override metadata surfaced — those land in
later steps.

Output layout — flat, one MDX page per module:

    web/src/content/docs/modules/
      <Module>.mdx

Usage:
    python tools/generate/generate_reference.py [VERSION] [--input DIR] [--output DIR]

Defaults:
    VERSION   12.3.6
    --input   stubs/<VERSION>/lom
    --output  web/src/content/docs
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Ancestors that aren't worth showing in the displayed class signature.
# Boost.Python's implementation classes are noise (every Live class derives
# from them); LomObject is intentionally NOT in this list — when it's the
# first informative ancestor (e.g. Clip → LomObject directly), we want to
# show it. Classes with a more-specific direct base (e.g. Track →
# DeviceContainer) display that instead because `base_class_for` returns
# the first non-boring ancestor.
_BORING_ANCESTORS = {
    "Boost.Python.instance",
    "instance",
    "object",
}

# Internal members suppressed from rendered docs. `_live_ptr` is the
# Boost.Python pointer-to-C++ implementation detail; `__init__` is rendered
# specially when the time comes (Phase 1 step still pending).
SKIP_MEMBERS = {
    "_live_ptr",
    "__init__",
}

# Site-base prefix for in-MDX cross-references. Mirrors `base: "/LiveAPI"` in
# astro.config.mjs — Astro doesn't auto-prefix arbitrary content links.
DOCS_URL_BASE = "/LiveAPI/modules"

# Identifier-token regex used by the type linker. Single Python-style token —
# composite types like `Vector[Clip] | None` keep their punctuation literal;
# only the bare identifiers get linked.
_TYPE_TOKEN_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")

# Strip `Live.<Module>.` prefix from qualified type strings for display.
# `Live.Base.Vector[Live.Clip.Clip] | None` → `Vector[Clip] | None`.
_LIVE_PREFIX_RE = re.compile(r"\bLive\.\w+\.")


# --- Override-aware field access --------------------------------------- #


def _resolve(node: dict, key: str) -> Any:
    """Read `key` from `node`, preferring `<key>_override.value` when present.

    Mirrors the override-resolution helper in `generate_stubs.py`. Same
    rule: parser-derived field and human override sit side-by-side; the
    consumer picks the override.
    """
    override = node.get(f"{key}_override")
    if isinstance(override, dict) and "value" in override:
        return override["value"]
    return node.get(key)


# --- Class registry + type linking ------------------------------------- #


def base_class_for(class_node: dict) -> str | None:
    """Return the simple name of the closest informative base class, or None.

    Filters the universal `LomObject` base + Boost.Python boilerplate —
    they don't carry useful info in the rendered signature.
    """
    for ancestor in class_node.get("ancestors") or []:
        if ancestor in _BORING_ANCESTORS:
            continue
        return ancestor.rsplit(".", 1)[-1]
    return None


def build_class_registry(modules: dict[str, dict]) -> dict[str, str]:
    """Return `{ClassName: module_name}` for top-level documented types.

    Top-level classes and enums in each module are linkable; nested types
    (e.g. `Track.View`, `Clip.WarpMode`) aren't anchored on their own pages
    yet — they're left as plain text by the linker until Step 10.
    """
    registry: dict[str, str] = {}
    for module_name, doc in modules.items():
        for cls in doc.get("primary_class") or []:
            if cls.get("name"):
                registry.setdefault(cls["name"], module_name)
        for cls in doc.get("classes") or []:
            if cls.get("name"):
                registry.setdefault(cls["name"], module_name)
        for enum in doc.get("enums") or []:
            if enum.get("name"):
                registry.setdefault(enum["name"], module_name)
    return registry


def display_type(type_str: str) -> str:
    """Strip `Live.<Module>.` prefix from qualified tokens for display."""
    return _LIVE_PREFIX_RE.sub("", type_str)


def linkify_type(type_str: str, registry: dict[str, str]) -> str:
    """Wrap each registry-known identifier in the type string with an `<a>`.

    Composite types like `Vector[Clip] | None` are tokenized on word
    boundaries — punctuation passes through verbatim, and unknown
    identifiers (`bool`, `None`, `int`, ...) stay literal.
    """

    def replace(match: re.Match[str]) -> str:
        token = match.group(0)
        module = registry.get(token)
        if module is None:
            return token
        return f'<a href="{DOCS_URL_BASE}/{module.lower()}/#{token.lower()}">{token}</a>'

    return _TYPE_TOKEN_RE.sub(replace, type_str)


# --- Text normalization ------------------------------------------------ #


def first_sentence(text: str | None) -> str:
    """Extract the first sentence from a runtime docstring, normalized."""
    if not text:
        return ""
    flat = " ".join(line.strip() for line in text.strip().splitlines() if line.strip())
    if ". " in flat:
        return flat.split(". ", 1)[0] + "."
    return flat


def normalize_paragraph(text: str | None) -> str:
    """Collapse a multi-line runtime docstring to a single normalized paragraph."""
    if not text:
        return ""
    return " ".join(line.strip() for line in text.strip().splitlines() if line.strip())


def escape_yaml_scalar(text: str) -> str:
    """Escape a string for a YAML frontmatter scalar (quoted form)."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


# --- Signature HTML ---------------------------------------------------- #


def _signature_html(
    *,
    kw: str,
    name: str,
    module_name: str,
    base_html: str | None = None,
    suffix: str = "",
) -> str:
    """Render a syntax-highlighted signature span.

    Nested span structure so pseudo-elements can color the keyword and
    path distinctly, while the base lives in the DOM as a real element
    (so it can host a link to the base class's reference page):

        <span class="sig" data-kw=...>
          <span class="sig-name" data-path=...>NAME</span>
          <span class="sig-base">(BASE_HTML)</span>      # optional
        </span>

    The keyword and path are CSS pseudo-elements (not in DOM text), so
    Starlight's right-side TOC picks up the name without extra fluff. The
    base IS in DOM text — `base_html` may already contain an `<a>`
    wrapping the base name for cross-page navigation.

    `suffix` is for visual additions kept in DOM text (e.g. empty `()` on
    function signatures — small enough that a parenthesized TOC reads fine).
    """
    outer_attrs = f' data-kw="{kw}"'
    inner_attrs = f' data-path="Live.{module_name}."'
    base_part = f'<span class="sig-base">({base_html})</span>' if base_html else ""
    return (
        f'<span class="sig"{outer_attrs}>'
        f'<span class="sig-name"{inner_attrs}>{name}</span>'
        f'{base_part}'
        f"</span>{suffix}"
    )


def class_signature_html(cls: dict, module_name: str, registry: dict[str, str]) -> str:
    """Render `class Name(Base):` — Base linked to its anchor when known."""
    base = base_class_for(cls)
    base_html: str | None = None
    if base:
        target_module = registry.get(base)
        if target_module:
            base_html = (
                f'<a href="{DOCS_URL_BASE}/{target_module.lower()}/#{base.lower()}">{base}</a>'
            )
        else:
            base_html = base
    return _signature_html(
        kw="class",
        name=cls["name"],
        module_name=module_name,
        base_html=base_html,
    )


def enum_signature_html(enum: dict, module_name: str) -> str:
    """All Live enums inherit `int`; the base is implicit and not shown."""
    return _signature_html(
        kw="enum",
        name=enum["name"],
        module_name=module_name,
    )


def function_signature_html(fn: dict, module_name: str) -> str:
    """Empty parens for now — full args land in a later step."""
    return _signature_html(
        kw="def",
        name=fn["name"],
        module_name=module_name,
        suffix="()",
    )


def property_heading_html(prop: dict, registry: dict[str, str]) -> str:
    """Render a property name + Python-annotation-style type.

    H5 isn't in the right-side TOC (capped at H3) so the type can sit in
    the DOM text without polluting nav. Live types in the annotation
    become `<a>` links; non-Live tokens (`bool`, `None`, ...) stay literal.
    """
    name = _resolve(prop, "name")
    type_str = _resolve(prop, "type")
    if not type_str:
        return name
    rendered = linkify_type(display_type(type_str), registry)
    return f'{name}<span class="prop-type">: {rendered}</span>'


# --- Module page rendering --------------------------------------------- #


def relpath_for(module_name: str) -> str:
    """Docs-relative path for a module's MDX file (no leading slash).

    All module pages live under `modules/` so Starlight's `autogenerate`
    works cleanly — generating from the docs root collides with index.mdx
    and leaves the sidebar empty.
    """
    return f"modules/{module_name}.mdx"


def render_module_page(module_name: str, doc: dict, registry: dict[str, str]) -> str:
    """Render one module's MDX page (paused at Step 4: property types).

    Layout:
      - YAML frontmatter (title + description from the module's first sentence)
      - Module description paragraph
      - Primary class section: signature, doc, properties listing
      - "Other classes" section: each class as a sub-section
      - Module Enums section
      - Module Functions section
    """
    raw_doc = doc.get("raw_doc")
    description = first_sentence(raw_doc) or f"The Live.{module_name} module."

    primary_classes = doc.get("primary_class") or []
    other_classes = doc.get("classes") or []
    enums = doc.get("enums") or []
    functions = doc.get("functions") or []

    # The lom format already promotes the conventional Live.X.X main class
    # into `primary_class:`. A few modules (e.g. Conversions, Licensing —
    # function-only modules) have no primary class.
    main_class = primary_classes[0] if primary_classes else None

    lines: list[str] = []
    lines.append("---")
    lines.append(f"title: {module_name}")
    lines.append(f'description: "{escape_yaml_scalar(description)}"')
    lines.append("---")
    lines.append("")
    lines.append(description)
    lines.append("")

    def emit_class(cls: dict) -> None:
        """Append a class block — H3 signature, description, property list."""
        lines.append(f"### {class_signature_html(cls, module_name, registry)}")
        lines.append("")
        doc_text = normalize_paragraph(cls.get("raw_doc"))
        if doc_text:
            lines.append(doc_text)
            lines.append("")
        properties = [
            p for p in (cls.get("properties") or [])
            if _resolve(p, "name") and _resolve(p, "name") not in SKIP_MEMBERS
        ]
        if properties:
            lines.append("#### Properties")
            lines.append("")
            for prop in properties:
                lines.append(f"##### {property_heading_html(prop, registry)}")
                lines.append("")

    def emit_member(heading_html: str, doc_text: str | None) -> None:
        """Append an H3 heading + an optional description paragraph below.

        Used for non-class members (enums, module functions) where there's
        no nested member structure to render at this step.
        """
        lines.append(f"### {heading_html}")
        lines.append("")
        if doc_text:
            lines.append(doc_text)
            lines.append("")

    if main_class is not None:
        emit_class(main_class)

    if other_classes:
        header = "Other classes" if main_class is not None else "Classes"
        lines.append(f"## {header}")
        lines.append("")
        for cls in other_classes:
            emit_class(cls)

    if enums:
        lines.append("## Module Enums")
        lines.append("")
        for enum in enums:
            emit_member(
                enum_signature_html(enum, module_name),
                normalize_paragraph(enum.get("raw_doc")),
            )

    if functions:
        lines.append("## Module Functions")
        lines.append("")
        for fn in functions:
            emit_member(
                function_signature_html(fn, module_name),
                normalize_paragraph(fn.get("raw_doc")),
            )

    return "\n".join(lines)


# --- CLI --------------------------------------------------------------- #


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    parser.add_argument("version", nargs="?", default="12.3.6",
                        help="Live version (default: 12.3.6)")
    parser.add_argument("--input", help="lom YAML dir (default: stubs/<v>/lom)")
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "web" / "src" / "content" / "docs"),
        help="output dir for MDX (default: web/src/content/docs)",
    )
    args = parser.parse_args()

    in_dir = Path(args.input) if args.input else REPO_ROOT / "stubs" / args.version / "lom"
    out_dir = Path(args.output)

    if not in_dir.exists():
        print(f"error: lom YAML dir not found at {in_dir}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)

    # Load every module YAML up front — registry build needs cross-module
    # visibility for type linking.
    modules: dict[str, dict] = {}
    for path in sorted(in_dir.glob("*.yaml")):
        d = yaml.safe_load(path.read_text())
        if isinstance(d, dict) and d.get("module"):
            modules[d["module"]] = d

    registry = build_class_registry(modules)

    written = 0
    for module_name, doc in modules.items():
        out_file = out_dir / relpath_for(module_name)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(render_module_page(module_name, doc, registry))
        written += 1

    print(f"Wrote {written} module pages to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

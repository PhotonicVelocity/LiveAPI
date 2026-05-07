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

# Internal members suppressed from rendered docs. `__init__` is a constructor,
# not a property, and is rendered specially when the time comes (Phase 1 step
# still pending). `_live_ptr` IS surfaced — it's the pointer-to-C++ handle
# that LomObject exposes universally, and showing it (declared on LomObject,
# inherited everywhere else) is the clearest demonstration of the LOM's
# universal-base structure.
SKIP_MEMBERS = {
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


# --- Inheritance ------------------------------------------------------- #


# Strip raw HTML tags + entities so slug() sees only the visible text.
_HTML_TAG_RE = re.compile(r"<[^>]+>")


def starlight_slug(heading_text: str) -> str:
    """Mirror Starlight's heading-to-id slug behavior.

    Observed pattern from the rendered site: lowercase, strip HTML tags,
    keep alphanumerics + underscores, replace runs of any other characters
    (`:`, ` `, `[`, `]`, `,`, ...) with a single `-`. Trim leading/trailing
    `-`. Examples:
      `name: str`                          → `name-str`
      `parameters: ATimeableValueVector`   → `parameters-atimeablevaluevector`
      `can_compare_ab: bool`               → `can_compare_ab-bool`
    """
    text = _HTML_TAG_RE.sub("", heading_text).lower()
    out = re.sub(r"[^a-z0-9_]+", "-", text)
    return out.strip("-")


def build_class_index(modules: dict[str, dict]) -> dict[str, tuple[str, dict]]:
    """Return `{qualified_path: (module_name, class_dict)}` for every class.

    Used to look up an ancestor by its qualified `Live.X.Y` path so we can
    render properties inherited from it with links to its declaration page.
    """
    index: dict[str, tuple[str, dict]] = {}

    def walk(cls: dict, module_name: str, parent_qpath: str) -> None:
        if not isinstance(cls, dict) or not cls.get("name"):
            return
        path = cls.get("path") or f"{parent_qpath}.{cls['name']}"
        index[path] = (module_name, cls)
        for nested in cls.get("classes") or []:
            walk(nested, module_name, path)

    for module_name, doc in modules.items():
        base = f"Live.{module_name}"
        for top in doc.get("primary_class") or []:
            walk(top, module_name, base)
        for top in doc.get("classes") or []:
            walk(top, module_name, base)
    return index


def inherited_properties(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
) -> list[tuple[str, str, dict]]:
    """Walk the class's ancestor chain transitively and collect inherited
    properties as (ancestor_qpath, ancestor_module_name, prop_dict).

    Each property is yielded once; if multiple ancestors declare the same
    name (e.g. an MRO with shadowing), the first ancestor encountered wins.
    Properties in `SKIP_MEMBERS` are filtered.
    """
    out: list[tuple[str, str, dict]] = []
    seen_names: set[str] = set()
    seen_ancestors: set[str] = set()
    stack = list(cls.get("ancestors") or [])
    while stack:
        anc_path = stack.pop(0)
        if anc_path in seen_ancestors:
            continue
        seen_ancestors.add(anc_path)
        entry = class_index.get(anc_path)
        if entry is None:
            continue
        anc_module, anc_cls = entry
        for prop in anc_cls.get("properties") or []:
            name = _resolve(prop, "name")
            if not name or name in SKIP_MEMBERS or name in seen_names:
                continue
            seen_names.add(name)
            out.append((anc_path, anc_module, prop))
        stack.extend(anc_cls.get("ancestors") or [])
    return out


def inherited_properties_block(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
    registry: dict[str, str],
) -> list[str]:
    """Render the `Inherited` H4 subsection for a class. Returns the lines
    to append (empty list if nothing to inherit). Format:

        #### Inherited

        From `LomObject`: [_live_ptr](/LiveAPI/modules/lomobject/#_live_ptr-int)

    One line per ancestor, comma-joined property links inline. Compact;
    surfaces what's available without re-declaring full type/listenable.
    """
    inherited = inherited_properties(cls, class_index)
    if not inherited:
        return []

    # Group by ancestor, preserving first-encountered order.
    by_ancestor: list[tuple[str, str, list[dict]]] = []
    seen: dict[str, int] = {}
    for anc_path, anc_module, prop in inherited:
        if anc_path not in seen:
            seen[anc_path] = len(by_ancestor)
            by_ancestor.append((anc_path, anc_module, []))
        by_ancestor[seen[anc_path]][2].append(prop)

    out = ["#### Inherited", ""]
    for anc_path, anc_module, props in by_ancestor:
        anc_name = anc_path.rsplit(".", 1)[-1]
        # Each prop link points to the ancestor's H5 anchor on the ancestor's
        # module page. Anchor matches Starlight's auto-slug of the H5 text.
        links = []
        for p in props:
            pname = _resolve(p, "name")
            heading = property_heading_html(p, registry)
            slug = starlight_slug(heading)
            links.append(
                f'[{pname}]({DOCS_URL_BASE}/{anc_module.lower()}/#{slug})'
            )
        out.append(f"From `{anc_name}`: {', '.join(links)}")
        out.append("")
    return out


# --- Module page rendering --------------------------------------------- #


def relpath_for(module_name: str) -> str:
    """Docs-relative path for a module's MDX file (no leading slash).

    All module pages live under `modules/` so Starlight's `autogenerate`
    works cleanly — generating from the docs root collides with index.mdx
    and leaves the sidebar empty.
    """
    return f"modules/{module_name}.mdx"


def render_module_page(
    module_name: str,
    doc: dict,
    registry: dict[str, str],
    class_index: dict[str, tuple[str, dict]] | None = None,
) -> str:
    """Render one module's MDX page (Step 5: properties + inherited).

    Layout:
      - YAML frontmatter (title + description)
      - Module description paragraph
      - Primary class section: signature, doc, own properties, inherited
      - "Other classes" section: each class as a sub-section
      - Module Enums section
      - Module Functions section
    """
    if class_index is None:
        class_index = {}
    # Hand-authored module description (per doc/lom-format.md). Falls back
    # to a visible placeholder so empty modules are obvious to writers.
    description = doc.get("description") or "_No module description._"
    # SEO frontmatter — strip markdown emphasis from the placeholder so the
    # `<meta>` snippet reads naturally.
    seo_description = first_sentence(doc.get("description")) or f"Reference for Live.{module_name}."

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
    lines.append(f'description: "{escape_yaml_scalar(seo_description)}"')
    lines.append("---")
    lines.append("")
    lines.append(description)
    lines.append("")

    def emit_class(cls: dict) -> None:
        """Append a class block — H3 signature, description, properties,
        and inherited-from-ancestor properties.
        """
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
        for line in inherited_properties_block(cls, class_index, registry):
            lines.append(line)

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
    class_index = build_class_index(modules)

    written = 0
    for module_name, doc in modules.items():
        out_file = out_dir / relpath_for(module_name)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(render_module_page(module_name, doc, registry, class_index))
        written += 1

    print(f"Wrote {written} module pages to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

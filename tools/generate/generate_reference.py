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
import html
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Ancestors that aren't worth showing in the displayed class signature.
# Boost.Python's implementation classes are noise (every Live class derives
# from them). LomObject is suppressed because the LOM badge surfaces that
# fact more usefully — every LOM class gets a clickable [LomObject] chip
# next to its signature linking to the LOM-model explainer page, so a
# `(LomObject)` on the inheritance line would be redundant. Classes with
# a more-specific direct base (e.g. Track → DeviceContainer) display that
# instead because `base_class_for` returns the first non-boring ancestor.
_BORING_ANCESTORS = {
    "Boost.Python.instance",
    "instance",
    "object",
    "Live.LomObject.LomObject",
}

# Qualified path of the universal LOM root. Used to detect "is this class
# transitively a LomObject?" for the signature badge.
_LOM_OBJECT_PATH = "Live.LomObject.LomObject"

# Property names that conceptually belong to every LomObject — the LOM
# identity/navigation surface. Rendered with a small linked chip next to
# the property heading so they read as "from the LomObject foundation"
# wherever they appear (own or inherited), regardless of which section
# they happen to land in. `_live_ptr` is structurally inherited from
# LomObject; `canonical_parent` is synthesized onto LomObject in the
# YAML (see LomObject.yaml) to mirror the runtime convention of
# covariant per-class redeclaration.
LOM_UNIVERSAL_MEMBERS = frozenset({"_live_ptr", "canonical_parent"})

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
    name: str,
    module_name: str,
    base_html: str | None = None,
    suffix: str = "",
) -> str:
    """Render a path-prefixed signature span.

    Nested span structure so the path can be a CSS pseudo-element (kept
    out of DOM text, so the right-side TOC sees the bare name), while
    the base lives in the DOM as a real element (so it can host a link
    to the base class's reference page):

        <span class="sig">
          <span class="sig-name" data-path=...>NAME</span>
          <span class="sig-base">(BASE_HTML)</span>      # optional
        </span>

    No leading keyword (`class` / `enum` / `def`). The page's section
    header (`## Other classes` / `## Enums` / `## Functions`) already
    labels the kind, and the structural shape of the signature
    (inheritance parens vs args + return vs neither) communicates the
    member type. Repeating the keyword on every entry was redundant —
    and `enum` was anyway a Sphinx-doc convention rather than literal
    Python (Live's enums are int-subclass `class`es bound by
    Boost.Python).

    `suffix` is for visual additions kept in DOM text — primarily the
    `(args) -> R` portion on function / method signatures, hung off
    the suffix slot via `_callable_args_returns_html`.
    """
    inner_attrs = f' data-path="Live.{module_name}."'
    base_part = f'<span class="sig-base">({base_html})</span>' if base_html else ""
    return (
        f'<span class="sig">'
        f'<span class="sig-name"{inner_attrs}>{name}</span>'
        f'{base_part}'
        f"</span>{suffix}"
    )


def is_lom_object(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
) -> bool:
    """Return True if `cls` is `LomObject` itself or transitively derives
    from it. Walks the ancestor chain via `class_index` (which has every
    documented class keyed by qualified path).
    """
    if cls.get("path") == _LOM_OBJECT_PATH:
        return True
    seen: set[str] = set()
    stack: list[str] = list(cls.get("ancestors") or [])
    while stack:
        anc = stack.pop()
        if anc in seen:
            continue
        seen.add(anc)
        if anc == _LOM_OBJECT_PATH:
            return True
        entry = class_index.get(anc)
        if entry is None:
            continue
        stack.extend(entry[1].get("ancestors") or [])
    return False


def lom_badge_html() -> str:
    """The `[LomObject]` chip rendered next to a LOM class's signature.

    Compact monospace pill, muted color, links to the LomObject page where
    the universal lifetime / identity / construction model is documented.
    """
    return (
        f'<a class="lom-badge" href="{DOCS_URL_BASE}/lomobject/" '
        f'title="This is a LomObject — see the LomObject page for the universal '
        f'identity / lifetime model">LomObject</a>'
    )


def class_signature_html(
    cls: dict,
    module_name: str,
    registry: dict[str, str],
    display_name: str | None = None,
    class_index: dict[str, tuple[str, dict]] | None = None,
) -> str:
    """Render `class Name(Base):` — Base linked to its anchor when known.

    `display_name` overrides the bare `cls["name"]` for the rendered text;
    used to display dotted nested-class names (e.g. `Track.View` instead of
    just `View`) when a nested class is rendered at the top level.

    `class_index` enables the LomObject badge — any class whose ancestor
    chain reaches `Live.LomObject.LomObject` gets a chip after the
    signature (suppressed on `LomObject` itself, which would point at its
    own page). Pass `None` to disable the badge.
    """
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
    sig = _signature_html(
        name=display_name or cls["name"],
        module_name=module_name,
        base_html=base_html,
    )
    # Skip the badge on LomObject itself — pointing at its own page would
    # be a no-op link, and the page IS the explainer the badge advertises.
    if (
        class_index is not None
        and cls.get("path") != _LOM_OBJECT_PATH
        and is_lom_object(cls, class_index)
    ):
        sig = f"{sig} {lom_badge_html()}"
    return sig


def enum_signature_html(
    enum: dict,
    module_name: str,
    display_name: str | None = None,
) -> str:
    """All Live enums inherit `int`; the base is implicit and not shown.

    `display_name` overrides the bare `enum["name"]` for the rendered text;
    used to display dotted nested-enum names (e.g. `Track.monitoring_states`)
    when a nested enum is rendered at the top level alongside module enums.
    """
    return _signature_html(
        name=display_name or enum["name"],
        module_name=module_name,
    )


def _callable_args_returns_html(
    callable_node: dict,
    registry: dict[str, str],
    *,
    owning_class_name: str | None = None,
) -> str:
    """Render the `(args) -> return` portion of a callable signature.

    Shared between class methods and module-level functions. Returns
    the inner HTML for a `.meth-sig` span:

        <span class="meth-sig">(<span class="meth-arg">x</span>: T,
          <span class="meth-arg">k</span>: T2 = <span class="meth-default">D</span>)
          <span class="meth-arrow">-&gt;</span> R</span>

    Drops `self` (methods only). Honors `name_override` on args
    (Boost.Python's `arg1` / `arg2` placeholders supplanted by corpus +
    M4L docs). When `owning_class_name` is supplied, defaults of the
    form `<owning_class_name>.X.Y` drop the redundant class-name prefix
    on the class's own page.
    """
    prefix = f"{owning_class_name}." if owning_class_name else None
    arg_parts: list[str] = []
    for arg in callable_node.get("args") or []:
        arg_name = _resolve(arg, "name")
        if arg_name == "self":
            continue
        arg_type = _resolve(arg, "type")
        type_part = ""
        if arg_type:
            type_part = f": {linkify_type(display_type(arg_type), registry)}"
        default = arg.get("default")
        if (
            prefix is not None
            and isinstance(default, str)
            and default.startswith(prefix)
        ):
            default = default[len(prefix):]
        default_part = (
            f' = <span class="meth-default">{default}</span>'
            if default is not None
            else ""
        )
        arg_parts.append(
            f'<span class="meth-arg">{arg_name}</span>'
            f'{type_part}{default_part}'
        )
    args_html = ", ".join(arg_parts)
    returns = callable_node.get("returns") or {}
    return_part = ""
    if isinstance(returns, dict):
        return_type = _resolve(returns, "type")
        if return_type:
            return_part = (
                f' <span class="meth-arrow">-&gt;</span> '
                f'{linkify_type(display_type(return_type), registry)}'
            )
    return f'<span class="meth-sig">({args_html}){return_part}</span>'


def function_signature_html(
    fn: dict,
    module_name: str,
    registry: dict[str, str],
) -> str:
    """Module-level function signature: `def name(args) -> return`.

    Same kw/path/name framing as classes (rendered as H3 with the
    keyword as a CSS pseudo-element); the args + return portion is the
    same `.meth-sig` span machinery as methods, hung off the suffix
    slot of `_signature_html`.
    """
    return _signature_html(
        name=fn["name"],
        module_name=module_name,
        suffix=_callable_args_returns_html(fn, registry),
    )


def method_signature_html(
    method: dict,
    registry: dict[str, str],
    *,
    owning_class_name: str | None = None,
) -> str:
    """Render a Python-style method signature: `name(arg: T, k: T2 = D) -> R`.

    Method name in monospace bold (inherits from H5); args + return in
    the `.meth-sig` muted scaffolding span — same machinery as
    module-level functions, just without the surrounding kw/path
    signature wrapper since methods sit inside their class's page.
    """
    name = _resolve(method, "name")
    return f'{name}{_callable_args_returns_html(method, registry, owning_class_name=owning_class_name)}'


def member_description_text(member: dict) -> str | None:
    """Resolve the displayable description for a property or method.

    Hand-authored `description:` takes precedence over parser-derived
    `raw_doc:` — same convention as the class-level pair (terse runtime
    docstring vs. authored prose). Both honor sibling `<field>_override:`
    blocks via `_resolve`.

    Description is preserved as-is (may be multi-paragraph markdown);
    raw_doc fallback is collapsed to a single paragraph (runtime
    docstrings are line-wrapped at the binding source and the wrap
    points carry no semantic meaning).
    """
    desc = _resolve(member, "description")
    if isinstance(desc, str) and desc.strip():
        return desc.strip()
    raw = _resolve(member, "raw_doc")
    if isinstance(raw, str) and raw.strip():
        return normalize_paragraph(raw)
    return None


def member_flags_html(member: dict) -> str:
    """Render small chip(s) for member modifiers — read-only,
    listenable. The default case (settable, not listenable for
    properties; not listenable for methods) returns empty string so
    most members render with no flags line at all, keeping the page
    quiet for the common case and reserving visual weight for the
    deviations:

      - `[read-only]` — `settable: false` (properties only)
      - `[listen]`    — `listenable:` present (folded listener triplet)

    Methods don't use `settable:`; they only ever pick up the
    `listen` chip — currently `Application.View.is_view_visible` is
    the only such method (a parameterized observable whose triplet
    takes a view-name identifier alongside the callback).

    Output is a div line that lives between the member heading and
    the description, so the chips read as metadata attached to the
    member without competing with the name + type on the heading.
    """
    chips: list[str] = []
    if _resolve(member, "settable") is False:
        chips.append('<span class="prop-flag prop-flag-ro">read-only</span>')
    if _resolve(member, "listenable"):
        chips.append(
            f'<a class="prop-flag prop-flag-listen" '
            f'href="{DOCS_URL_BASE}/listener/" '
            f'title="This member is observable — see Listener for the '
            f'subscription model.">listen</a>'
        )
    if not chips:
        return ""
    return f'<div class="prop-flags">{" ".join(chips)}</div>'


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
    """Mirror Starlight's heading-to-id slug behavior (GitHub-style slugger).

    Algorithm: strip HTML tags, decode HTML entities (so `&gt;` collapses
    to `>` and gets dropped as punctuation, matching what Starlight's
    slugger sees from the rendered heading), lowercase, drop punctuation
    WITHOUT inserting a separator, replace runs of whitespace with a
    single `-`, trim leading/trailing `-`. Examples:
      `name: str`                          → `name-str`
      `parameters: ATimeableValueVector`   → `parameters-atimeablevaluevector`
      `Track(DeviceContainer)`             → `trackdevicecontainer`
      `view: Device.View`                  → `view-deviceview`
      `foo() -&gt; None`                   → `foo---none`
    """
    text = _HTML_TAG_RE.sub("", heading_text)
    text = html.unescape(text).lower()
    # Drop punctuation; keep word chars, whitespace, and dashes
    text = re.sub(r"[^\w\s-]", "", text)
    # Whitespace runs → single `-`
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


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


def resolve_lom_universal(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
) -> list[dict]:
    """Resolve `_live_ptr` and `canonical_parent` for `cls`, picking the
    closest declaration in the MRO (own → ancestor BFS). Returns the
    resolved prop dicts in canonical order. Used to pin the LOM
    identity/navigation pair at the top of the Properties section on
    every LomObject class — uniform position regardless of whether the
    class declares them itself (covariant override) or inherits them.
    """
    out: list[dict] = []
    own_by_name = {
        _resolve(p, "name"): p
        for p in (cls.get("properties") or [])
        if _resolve(p, "name")
    }
    for name in ("_live_ptr", "canonical_parent"):
        if name in own_by_name:
            out.append(own_by_name[name])
            continue
        # BFS the ancestor chain — first match wins.
        seen: set[str] = set()
        stack = list(cls.get("ancestors") or [])
        found = None
        while stack and found is None:
            anc_path = stack.pop(0)
            if anc_path in seen:
                continue
            seen.add(anc_path)
            entry = class_index.get(anc_path)
            if entry is None:
                continue
            _anc_module, anc_cls = entry
            for p in anc_cls.get("properties") or []:
                if _resolve(p, "name") == name:
                    found = p
                    break
            if found is None:
                stack.extend(anc_cls.get("ancestors") or [])
        if found is not None:
            out.append(found)
    return out


def inherited_methods(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
) -> list[tuple[str, str, dict]]:
    """Walk the class's ancestor chain transitively and collect inherited
    methods as (ancestor_qpath, ancestor_module_name, method_dict).

    Same dedup machinery as `inherited_properties`: BFS by ancestor,
    first occurrence per name wins (so closer ancestors with covariant
    overrides shadow farther ancestors), and the class's own methods
    shadow inherited copies. `SKIP_MEMBERS` filtered (`__init__`).
    """
    out: list[tuple[str, str, dict]] = []
    own_names = {
        _resolve(m, "name")
        for m in (cls.get("methods") or [])
        if _resolve(m, "name")
    }
    seen_names: set[str] = set(own_names)
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
        _anc_module, anc_cls = entry
        for method in anc_cls.get("methods") or []:
            name = _resolve(method, "name")
            if not name or name in SKIP_MEMBERS or name in seen_names:
                continue
            seen_names.add(name)
            out.append((anc_path, _anc_module, method))
        stack.extend(anc_cls.get("ancestors") or [])
    return out


def inherited_properties(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
) -> list[tuple[str, str, dict]]:
    """Walk the class's ancestor chain transitively and collect inherited
    properties as (ancestor_qpath, ancestor_module_name, prop_dict).

    Each property is yielded once; if multiple ancestors declare the same
    name (e.g. an MRO with shadowing), the first ancestor encountered wins.
    Properties already declared on `cls` itself shadow the inherited copy
    (covariant overrides like `Track.canonical_parent: Song` vs the
    synthesized `LomObject.canonical_parent: LomObject | None`) — those
    are filtered out so they don't double-render. Properties in
    `SKIP_MEMBERS` are also filtered.
    """
    out: list[tuple[str, str, dict]] = []
    own_names = {
        _resolve(p, "name")
        for p in (cls.get("properties") or [])
        if _resolve(p, "name")
    }
    seen_names: set[str] = set(own_names)
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


def inherited_block(
    cls: dict,
    class_index: dict[str, tuple[str, dict]],
    registry: dict[str, str],
) -> list[str]:
    """Render the `Inherited` H4 subsection for a class. Returns the lines
    to append (empty list if nothing to inherit). Format:

        #### Inherited

        From `Device`: [can_compare_ab](...), [class_name](...), [foo()](...)

    One line per ancestor, comma-joined member links inline. Properties
    render as bare names (`name`); methods render with parens (`foo()`)
    so the eye picks up the kind without dropping into the type / arg
    detail. Compact — surfaces what's available without re-declaring
    full signatures.

    Universal LOM members (`_live_ptr`, `canonical_parent`) are pinned
    at the top of the Properties section by `emit_class`, so they're
    filtered out here to avoid double-rendering.
    """
    inherited_props = [
        (a, m, p) for (a, m, p) in inherited_properties(cls, class_index)
        if _resolve(p, "name") not in LOM_UNIVERSAL_MEMBERS
    ]
    inherited_meths = inherited_methods(cls, class_index)
    if not inherited_props and not inherited_meths:
        return []

    # Group by ancestor, preserving first-encountered order. Each entry:
    # [path, module, props, methods].
    by_ancestor: list[list] = []
    seen: dict[str, int] = {}

    def _slot(anc_path: str, anc_module: str) -> list:
        if anc_path not in seen:
            seen[anc_path] = len(by_ancestor)
            by_ancestor.append([anc_path, anc_module, [], []])
        return by_ancestor[seen[anc_path]]

    for anc_path, anc_module, prop in inherited_props:
        _slot(anc_path, anc_module)[2].append(prop)
    for anc_path, anc_module, method in inherited_meths:
        _slot(anc_path, anc_module)[3].append(method)

    out = ["#### Inherited", ""]
    for anc_path, anc_module, props, methods in by_ancestor:
        anc_name = anc_path.rsplit(".", 1)[-1]
        links: list[str] = []
        for p in props:
            pname = _resolve(p, "name")
            slug = starlight_slug(property_heading_html(p, registry))
            links.append(
                f'[{pname}]({DOCS_URL_BASE}/{anc_module.lower()}/#{slug})'
            )
        for method in methods:
            mname = _resolve(method, "name")
            slug = starlight_slug(
                method_signature_html(
                    method, registry, owning_class_name=anc_name,
                )
            )
            links.append(
                f'[{mname}()]({DOCS_URL_BASE}/{anc_module.lower()}/#{slug})'
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
    # Title defaults to the module name. Modules can override via a
    # top-level `title:` field in their lom YAML when a more descriptive
    # page heading is warranted (e.g. LomObject's foundation-page role).
    page_title = doc.get("title") or module_name
    lines.append("---")
    lines.append(f"title: {page_title}")
    lines.append(f'description: "{escape_yaml_scalar(seo_description)}"')
    lines.append("---")
    lines.append("")
    lines.append(description)
    lines.append("")

    def emit_class(cls: dict, display_name: str | None = None) -> None:
        """Append a class block — H3 signature, description, then the
        class's H4 section scaffold (Properties, Methods, Nested classes,
        Nested enums, Constants).

        Nested classes render as a link list pointing OUT to where they're
        rendered at the top level (in the page's own `## Nested classes`
        H2 section). This keeps every class on a uniform render — same
        depth, same heading levels, same future member layout — instead
        of inlining nested classes one level deeper and running out of
        heading levels.

        `display_name` overrides the rendered class name (used to show
        `Track.View` for a nested class hoisted to the top level).
        """
        sig = class_signature_html(
            cls, module_name, registry,
            display_name=display_name, class_index=class_index,
        )
        lines.append(f"### {sig}")
        lines.append("")
        doc_text = normalize_paragraph(cls.get("raw_doc"))
        if doc_text:
            lines.append(doc_text)
            lines.append("")
        # Hand-authored, multi-paragraph class description (markdown).
        # Lives on the class node as `description:` (see lom-format.md
        # — analogous to the module-top-level `description:`, but
        # scoped to one class). Renders below the runtime docstring so
        # both are visible: parser-derived terse line first, authored
        # context after.
        class_description = cls.get("description")
        if class_description:
            lines.append(class_description.strip())
            lines.append("")
        rendered_name = display_name or cls["name"]
        # Partition the YAML's `properties:` list into real properties
        # (anything with a type) and signal-only triplets (`listenable:`
        # but no `type:` — see Listener page §"Signal-only triplets").
        # Signal-only entries aren't readable attributes; they exist
        # only as listener triplets, so they render under their own
        # `#### Signals` section rather than mixed into Properties
        # where the absence of a type would be silently misleading.
        properties: list[dict] = []
        signals: list[dict] = []
        for p in (cls.get("properties") or []):
            pname = _resolve(p, "name")
            if not pname or pname in SKIP_MEMBERS:
                continue
            if not _resolve(p, "type") and _resolve(p, "listenable"):
                signals.append(p)
            else:
                properties.append(p)
        # Pin LOM-universal members (`_live_ptr`, `canonical_parent`) at
        # the top of the Properties section on every LomObject class
        # other than LomObject itself. Resolves each from the closest
        # MRO declaration — own (covariant override like
        # `Track.canonical_parent: Song`) takes precedence, otherwise
        # walks ancestors. The Inherited section filters the same names
        # so nothing renders twice.
        pinned: list[dict] = []
        if (
            class_index is not None
            and is_lom_object(cls, class_index)
            and cls.get("path") != _LOM_OBJECT_PATH
        ):
            pinned = resolve_lom_universal(cls, class_index)
            pinned_names = {_resolve(p, "name") for p in pinned}
            properties = [
                p for p in properties
                if _resolve(p, "name") not in pinned_names
            ]
        if pinned or properties:
            lines.append("#### Properties")
            lines.append("")
            if pinned:
                # Single LomObject chip acts as the sub-header for the
                # pinned LOM-universal pair (`_live_ptr`, `canonical_parent`).
                # Per-property chips suppressed — the header carries the
                # link, and the separator below creates the visual break
                # before the per-class properties begin.
                lines.append(
                    f'<a class="lom-pinned-header" '
                    f'href="{DOCS_URL_BASE}/lomobject/#properties" '
                    f'title="LOM identity / navigation pair — universal '
                    f'across every LomObject. Click for the canonical '
                    f'declarations on LomObject.">LomObject</a>'
                )
                lines.append("")
                # Descriptions on the pinned pair are suppressed: each
                # subclass's `canonical_parent` raw_doc is just "Get the
                # canonical parent of the X" — restates the name without
                # adding signal. The canonical explanation lives on
                # LomObject and the chip header links there. Flag chips
                # (RO / listen) still render — they're per-class facts,
                # not redundant with the foundation page.
                for prop in pinned:
                    heading = property_heading_html(prop, registry)
                    lines.append(f"##### {heading}")
                    lines.append("")
                    flags = member_flags_html(prop)
                    if flags:
                        lines.append(flags)
                        lines.append("")
                lines.append('<hr class="lom-pinned-separator" />')
                lines.append("")
            for prop in properties:
                heading = property_heading_html(prop, registry)
                lines.append(f"##### {heading}")
                lines.append("")
                flags = member_flags_html(prop)
                if flags:
                    lines.append(flags)
                    lines.append("")
                desc = member_description_text(prop)
                if desc:
                    lines.append(f"<div class=\"member-desc\">\n\n{desc}\n\n</div>")
                    lines.append("")
        # Inherited members from transitive ancestors — rendered as a
        # single H4 block under the class so what's available via the
        # MRO is visible without re-declaring every type / listener.
        for line in inherited_block(cls, class_index, registry):
            lines.append(line)
        # Signal-only listener triplets — `notes`, `loop_jump`, etc.
        # Surfaced in their own section so the reader doesn't read
        # them as untyped properties; the section header is the
        # signal that "these are subscription points, not attributes."
        # The `[listen]` chip stays on each entry as the link to the
        # Listener foundation page.
        if signals:
            lines.append("#### Signals")
            lines.append("")
            for prop in signals:
                heading = property_heading_html(prop, registry)
                lines.append(f"##### {heading}")
                lines.append("")
                flags = member_flags_html(prop)
                if flags:
                    lines.append(flags)
                    lines.append("")
                desc = member_description_text(prop)
                if desc:
                    lines.append(f"<div class=\"member-desc\">\n\n{desc}\n\n</div>")
                    lines.append("")
        # Filter listener-triplet methods folded into a parent method's
        # `listenable:` field — the parameterized-observable case (the
        # only current example: `Application.View.is_view_visible` and
        # its three matching `*_listener` methods). The triplet members
        # are surfaced via the parent method's `[listen]` chip; their
        # signatures are documented through the parent's `description:`.
        triplet_method_names: set[str] = set()
        for m in cls.get("methods") or []:
            for triplet_name in (_resolve(m, "listenable") or []):
                if isinstance(triplet_name, str):
                    triplet_method_names.add(triplet_name)
        methods = [
            m for m in (cls.get("methods") or [])
            if (
                _resolve(m, "name")
                and _resolve(m, "name") not in SKIP_MEMBERS
                and _resolve(m, "name") not in triplet_method_names
            )
        ]
        if methods:
            lines.append("#### Methods")
            lines.append("")
            for method in methods:
                heading = method_signature_html(
                    method, registry,
                    owning_class_name=cls.get("name"),
                )
                lines.append(f"##### {heading}")
                lines.append("")
                flags = member_flags_html(method)
                if flags:
                    lines.append(flags)
                    lines.append("")
                desc = member_description_text(method)
                if desc:
                    lines.append(f"<div class=\"member-desc\">\n\n{desc}\n\n</div>")
                    lines.append("")
        # Nested types — classes and enums declared inside this class.
        # Surfaced as a unified link list pointing into the page's flat
        # top-level `## Other classes` / `## Enums` sections, where they're
        # rendered once. Keeps the parent-class member layout flat (one
        # section per kind: properties, methods, nested types) instead of
        # splitting on declaration kind.
        nested_classes = cls.get("classes") or []
        nested_enums = cls.get("enums") or []
        if nested_classes or nested_enums:
            lines.append("#### Nested types")
            lines.append("")
            for nc in nested_classes:
                nc_display = f"{rendered_name}.{nc['name']}"
                base = base_class_for(nc)
                # Anchor matches Starlight's auto-slug for the H3 heading
                # we'll emit at the top level. The H3 visible text is the
                # full signature span — `Name(Base)` after HTML stripping.
                anchor_text = f"{nc_display}({base})" if base else nc_display
                anchor = starlight_slug(anchor_text)
                first_line = first_sentence(nc.get("raw_doc")) or ""
                line = f"- [`{nc_display}`](#{anchor})"
                if first_line:
                    line += f" — {first_line}"
                lines.append(line)
            for ne in nested_enums:
                ne_display = f"{rendered_name}.{ne['name']}"
                # H3 text for an enum is just the dotted name (kw/path are
                # CSS pseudo-elements), so the slug is simpler than for a
                # class with a base.
                anchor = starlight_slug(ne_display)
                first_line = first_sentence(ne.get("raw_doc")) or ""
                line = f"- [`{ne_display}`](#{anchor})"
                if first_line:
                    line += f" — {first_line}"
                lines.append(line)
            lines.append("")
        if cls.get("constants"):
            lines.append("#### Constants")
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

    # Collect all non-primary classes onto a single flat list:
    # other top-level classes + nested classes from every top-level class
    # (including from primary). Nested classes render via the same
    # `emit_class` machinery, but with a dotted display name (`Track.View`)
    # so the qualified identity is clear. Parents' `Nested classes` link
    # lists point into this section.
    classes_flat: list[tuple[dict | None, dict]] = []
    for cls in other_classes:
        classes_flat.append((None, cls))
    for top_cls in [*primary_classes, *other_classes]:
        for nc in top_cls.get("classes") or []:
            classes_flat.append((top_cls, nc))

    if classes_flat:
        # "Other classes" only makes sense when there's a primary; without
        # one (function-only modules and the like) just call them Classes.
        header = "Other classes" if main_class is not None else "Classes"
        lines.append(f"## {header}")
        lines.append("")
        for parent, cls in classes_flat:
            display = f"{parent['name']}.{cls['name']}" if parent else None
            emit_class(cls, display_name=display)

    # Same flattening for enums — top-level module enums + nested ones.
    enums_flat: list[tuple[dict | None, dict]] = []
    for enum in enums:
        enums_flat.append((None, enum))
    for top_cls in [*primary_classes, *other_classes]:
        for ne in top_cls.get("enums") or []:
            enums_flat.append((top_cls, ne))

    if enums_flat:
        lines.append("## Enums")
        lines.append("")
        for parent, enum in enums_flat:
            display = f"{parent['name']}.{enum['name']}" if parent else None
            sig = enum_signature_html(enum, module_name, display_name=display)
            lines.append(f"### {sig}")
            lines.append("")
            desc = member_description_text(enum)
            if desc:
                # Enum description — top-level H3 entity, sits at page
                # margin like a class description. NOT wrapped in
                # `.member-desc` (that's for property / method
                # descriptions nested under a class's H4 sections).
                lines.append(desc)
                lines.append("")
            members = enum.get("members") or {}
            if members:
                # `#### Members` heading parallels `#### Properties` /
                # `#### Methods` on classes — same structural role on
                # an enum. Member listing rendered as a raw HTML table
                # (no markdown header row needed); names in monospace,
                # values right-aligned and muted.
                lines.append("#### Members")
                lines.append("")
                lines.append('<table class="enum-members">')
                for member_name, member_value in members.items():
                    lines.append(
                        f'<tr><td><code>{member_name}</code></td>'
                        f'<td>{member_value}</td></tr>'
                    )
                lines.append('</table>')
                lines.append("")

    if functions:
        lines.append("## Functions")
        lines.append("")
        for fn in functions:
            emit_member(
                function_signature_html(fn, module_name, registry),
                member_description_text(fn),
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

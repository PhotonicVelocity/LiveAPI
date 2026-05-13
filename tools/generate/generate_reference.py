#!/usr/bin/env python3
# vibe-coded: substantial AI-assisted authoring. Review before relying on.
"""Generate Starlight (Astro) MDX reference pages from content/<v>/modules/*.md.

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
    --input   content/<VERSION>/modules
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
# Foundation pages (LomObject, Listener, Calling conventions, Remote
# scripts) render at the site root, not under `/modules/`, so the
# cross-cutting chips and badges that link to them build URLs against
# this base.
FOUNDATION_URL_BASE = "/LiveAPI"

# Identifier-token regex used by the type linker. Matches either a
# dotted PascalCase chain (greedy, longest-first — `Application.View.NavDirection`)
# or a single identifier (`Clip`, `int`, `bool`). The dotted alternative
# comes first so the regex engine prefers it; that lets the linker
# look up nested types under their full qualified name in the registry
# and link the whole chain to the correct anchor rather than partial-
# matching the leading top-level class.
# First segment must start uppercase (so plain `foo.bar` lowercase
# chains aren't matched as type tokens); inner segments accept either
# case so nested snake_case enums like `MixerDevice.panning_modes`
# match. Registry lookup gates which tokens actually become links.
_TYPE_TOKEN_RE = re.compile(
    r"\b[A-Z][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\b"
    r"|\b[A-Za-z_][A-Za-z0-9_]*\b"
)

# Strip `Live.<Module>.` prefix from qualified type strings for display.
# `Live.Base.Vector[Live.Clip.Clip] | None` → `Vector[Clip] | None`.
_LIVE_PREFIX_RE = re.compile(r"\bLive\.\w+\.")

# Match every fully-qualified Live class identifier in a type string.
# Used by the references-index builder to pull out cross-reference
# targets from property `type:` and method `returns.type:` fields.
# `Live.Base.Vector[Live.Clip.Clip] | None` matches both
# `Live.Base.Vector` and `Live.Clip.Clip`.
_LIVE_CLASS_RE = re.compile(r"\bLive(?:\.[A-Z][A-Za-z0-9_]*)+\b")


# --- Override-aware field access --------------------------------------- #


def _resolve(node: dict, key: str) -> Any:
    """Read `key` from `node`. The markdown SOT stores resolved values
    directly (with the parser-derived diagnostics living under
    `refinement.<key>.probed`), so this is just `node.get(key)`. Kept as
    a named helper because the access pattern is grep-friendly and the
    historical override-merge behavior makes the call sites read clearly.
    """
    return node.get(key)


def _listener_triplet(member: dict) -> list[str]:
    """Three listener-triplet method names for a member.

    `listenable:` can be `true` (shorthand — expand to `add_X_listener` /
    `remove_X_listener` / `X_has_listener` derived from the member's name)
    or an explicit list. Empty list when the member isn't listenable.
    """
    listenable = member.get("listenable")
    if listenable is True:
        n = member.get("name", "")
        return [f"add_{n}_listener", f"remove_{n}_listener", f"{n}_has_listener"]
    if isinstance(listenable, list):
        return listenable
    return []


def override_marker_html(node: dict, key: str) -> str:
    """Small superscript marker rendered after a value that came from a
    `refinement` block. The marker carries a structured tooltip child
    (hidden by default, revealed on hover/focus) with the probed-as
    value, a confidence chip, and the refinement's `sources:` evidence
    as a tagged bullet list. The visible asterisk is a CSS `::before`
    pseudo-element on `.override-marker` so MDX doesn't see a bare `*`
    as markdown emphasis."""
    refinement = node.get("refinement") or {}
    block = refinement.get(key)
    if not isinstance(block, dict):
        return ""

    # `original` is the probed-as value (what the parser/runtime saw
    # before manual refinement). May be absent for refinements that
    # exist only to assert confidence / sources for an unchanged value.
    original = block.get("probed")
    confidence = block.get("confidence", "")
    raw_source = block.get("sources", "")

    def _flat(s: object) -> str:
        return re.sub(r"\s+", " ", str(s)).strip() if s else ""

    def _esc(s: str) -> str:
        return html.escape(s, quote=True)

    def _mdx_text(s: str) -> str:
        """Escape MDX-significant characters in inline element-child
        text while leaving backtick-delimited code spans untouched.

        MDX honors backslash-escapes for `<` `>` `{` `}` outside code
        spans — they decode to literal characters at render time. But
        inside backtick code spans MDX treats the content as opaque
        and DOESN'T decode the backslashes, so we'd emit visible
        backslash-angle-bracket literals if we ran the escape blindly.
        """
        out: list[str] = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch == "`":
                j = s.find("`", i + 1)
                if j == -1:
                    # Unmatched backtick — drop the special meaning,
                    # keep as literal.
                    out.append("\\`")
                    i += 1
                else:
                    # Pass code span verbatim, including delimiters.
                    out.append(s[i : j + 1])
                    i = j + 1
            elif ch == "\\":
                out.append("\\\\")
                i += 1
            elif ch in "<>{}":
                out.append("\\" + ch)
                i += 1
            else:
                out.append(ch)
                i += 1
        return "".join(out)

    def _fmt_type(v: object) -> str:
        return display_type(v) if isinstance(v, str) else str(v)

    parts: list[str] = []

    # Top row: probed-as on the left, confidence chip floated right.
    # The refined value is visible in the page text the marker is
    # attached to, so we don't repeat it; we only show what was
    # probed (the parser-derived original) so the reader can see what
    # changed. Confidence chip sits in the same row so the trust
    # signal reads alongside the value being scrutinized, not above
    # it.
    if original is not None or confidence:
        row_parts: list[str] = []
        if original is not None:
            row_parts.append(
                f'<span class="ot-row-left">'
                f'<span class="ot-label">Probed as</span>'
                f'<code class="ot-value">{_mdx_text(_fmt_type(original))}</code>'
                f'</span>'
            )
        else:
            # Confidence-only refinement (no probed value to surface) — keep
            # the row structure so the chip still floats to the right edge.
            row_parts.append('<span class="ot-row-left"></span>')
        if confidence:
            conf_slug = re.sub(r"[^a-z0-9]+", "-", confidence.lower()).strip("-")
            row_parts.append(
                f'<span class="ot-confidence ot-confidence-{_esc(conf_slug)}">'
                f'{_esc(confidence)} confidence</span>'
            )
        parts.append(f'<span class="ot-row">{"".join(row_parts)}</span>')

    # `source:` accepts a single string or a YAML list of independent
    # evidence points. Each list item may carry a leading `[tag]`
    # prefix marking the evidence type — extracted and rendered as a
    # styled chip on the bullet so readers can scan provenance at a
    # glance.
    if isinstance(raw_source, list):
        items = [_flat(item) for item in raw_source if item]
    elif raw_source:
        items = [_flat(raw_source)]
    else:
        items = []

    if items:
        bullet_html: list[str] = []
        tag_re = re.compile(r"^\[([^\]]+)\]\s*(.*)$")
        for item in items:
            m = tag_re.match(item)
            if m:
                tag = m.group(1)
                body = m.group(2)
                tag_slug = re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")
                bullet_html.append(
                    f'<li>'
                    f'<span class="ot-tag ot-tag-{_esc(tag_slug)}">'
                    f'{_esc(tag)}</span>'
                    f' {_mdx_text(body)}'
                    f'</li>'
                )
            else:
                bullet_html.append(f'<li>{_mdx_text(item)}</li>')
        parts.append(
            f'<ul class="ot-sources">{"".join(bullet_html)}</ul>'
        )

    if not parts:
        parts.append('<span class="ot-row">Manually refined.</span>')

    inner = "".join(parts)
    return (
        f'<sup class="override-marker" tabindex="0" '
        f'aria-label="manually refined">'
        f'<span class="override-marker-tooltip" role="tooltip">'
        f'{inner}</span></sup>'
    )


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
    """Return `{display_name: module_name}` for every documented type.

    Display name is the dotted simple form: `Track` for a top-level
    class, `Application.View` for a depth-1 nested class,
    `Application.View.NavDirection` for a depth-2 nested enum, etc.
    Walks every module's class tree recursively so the linkifier can
    resolve nested types of any depth.
    """
    registry: dict[str, str] = {}

    def walk(cls: dict, prefix: str, module_name: str) -> None:
        if not isinstance(cls, dict):
            return
        name = cls.get("name")
        if not name:
            return
        full = f"{prefix}.{name}" if prefix else name
        registry.setdefault(full, module_name)
        for nested in cls.get("classes") or []:
            walk(nested, full, module_name)
        for enum in cls.get("enums") or []:
            e_name = enum.get("name")
            if e_name:
                registry.setdefault(f"{full}.{e_name}", module_name)

    for module_name, doc in modules.items():
        for cls in doc.get("classes") or []:
            walk(cls, "", module_name)
        for enum in doc.get("enums") or []:
            if enum.get("name"):
                registry.setdefault(enum["name"], module_name)
    return registry


def display_type(type_str: str) -> str:
    """Strip `Live.<Module>.` prefix from qualified tokens for display."""
    return _LIVE_PREFIX_RE.sub("", type_str)


def linkify_type(
    type_str: str,
    registry: dict[str, str],
    current_module: str | None = None,
) -> str:
    """Wrap each registry-known identifier in the type string with an `<a>`.

    Composite types like `Vector[Clip] | None` are tokenized on word
    boundaries — punctuation passes through verbatim, and unknown
    identifiers (`bool`, `None`, `int`, ...) stay literal.

    Dotted patterns (`Application.View.NavDirection`) try longest-prefix
    matching against the registry: full path first, then progressively
    shorter prefixes, so deeply-nested types link to the correct anchor
    when registered, falling back to the top-level class link otherwise.
    Anchors strip the dots — Starlight's auto-slug for an H3 heading
    `Application.View.NavDirection` is `applicationviewnavdirection`.

    `current_module` (the module being rendered) shortens the displayed
    link text when the matched type lives on the same page: for a
    same-module candidate, the longest same-module prefix is stripped
    from the visible text. So `Application.View.NavDirection` on the
    Application page renders as `NavDirection` (link still targets
    `#applicationviewnavdirection`); cross-module references stay
    fully qualified for disambiguation. The `title` attribute carries
    the full qualified name for hover.
    """

    def replace(match: re.Match[str]) -> str:
        token = match.group(0)
        parts = token.split(".")
        for i in range(len(parts), 0, -1):
            candidate = ".".join(parts[:i])
            module = registry.get(candidate)
            if module is None:
                continue
            anchor = candidate.lower().replace(".", "")
            display = candidate
            if (
                current_module is not None
                and module.lower() == current_module.lower()
                and i > 1
            ):
                for j in range(i - 1, 0, -1):
                    prefix = ".".join(parts[:j])
                    prefix_module = registry.get(prefix)
                    if (
                        prefix_module is not None
                        and prefix_module.lower() == current_module.lower()
                    ):
                        display = ".".join(parts[j:i])
                        break
            link = (
                f'<a href="{DOCS_URL_BASE}/{module.lower()}/#{anchor}" '
                f'title="{candidate}">{display}</a>'
            )
            trailing = "".join(f".{p}" for p in parts[i:])
            return f"{link}{trailing}"
        return token

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
    base_name: str | None = None,
    base_href: str | None = None,
    suffix: str = "",
) -> str:
    """Render a path-prefixed signature span.

    Nested span structure so the path AND the inheritance base both
    sit out of DOM text — the right-side TOC reads only the bare
    class/enum/function name. The path is a CSS pseudo-element on
    `.sig-name::before` (via `data-path`); the base name and its
    surrounding parens are CSS pseudo-elements on the empty
    `.sig-base-link` / `.sig-base-text` element (via `data-base`):

        <span class="sig">
          <span class="sig-name" data-path=...>NAME</span>
          <span class="sig-base">                   # optional
            <a class="sig-base-link" href=... data-base=...></a>
          </span>
        </span>

    The `<a>` for a linked base has no DOM children but renders the
    base name via `::before { content: attr(data-base) }`; clicks on
    the rendered text hit the `<a>` so navigation still works.
    `aria-label` carries the base name for screen readers.

    No leading keyword (`class` / `enum` / `def`). The page's section
    header (`## Other classes` / `## Enums` / `## Functions`) already
    labels the kind, and the structural shape of the signature
    (inheritance parens vs args + return vs neither) communicates the
    member type.

    `suffix` is for visual additions kept in DOM text — primarily the
    LomObject chip on classes (also rendered with empty DOM text so
    its label doesn't pollute the TOC).
    """
    inner_attrs = f' data-path="Live.{module_name}."'
    if base_name:
        if base_href:
            base_inner = (
                f'<a class="sig-base-link" href="{base_href}" '
                f'data-base="{base_name}" aria-label="{base_name}"></a>'
            )
        else:
            base_inner = (
                f'<span class="sig-base-text" data-base="{base_name}" '
                f'aria-label="{base_name}"></span>'
            )
        base_part = f'<span class="sig-base">{base_inner}</span>'
    else:
        base_part = ""
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
    """The `[LomObject]` chip rendered inside a LOM class's H3 signature.

    The `<a>` deliberately has no text content — its visible
    "LomObject" label comes from a CSS `::before` pseudo-element so
    that Starlight's right-side TOC (which reads heading
    `textContent`) doesn't pick up the chip's text. The `<a>` box
    stays clickable because the pseudo-element renders inside it.
    Float-right via CSS pulls the chip to the right edge of the H3's
    row.
    """
    return (
        f'<a class="lom-badge" href="{FOUNDATION_URL_BASE}/live-object-model/" '
        f'title="This is a LomObject — see the LomObject page for the universal '
        f'identity / lifetime model" aria-label="LomObject"></a>'
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

    `class_index` enables the LomObject chip — appended INSIDE the H3
    sig HTML so CSS float-right reliably positions it on the H3's row.
    The chip element has no DOM text content (its visible label comes
    from `::before`), so Starlight's TOC stays clean.
    """
    base = base_class_for(cls)
    base_href: str | None = None
    if base:
        target_module = registry.get(base)
        if target_module:
            base_href = (
                f"{DOCS_URL_BASE}/{target_module.lower()}/#{base.lower()}"
            )
    sig = _signature_html(
        name=display_name or cls["name"],
        module_name=module_name,
        base_name=base,
        base_href=base_href,
    )
    # Append the LomObject chip INSIDE the sig HTML (so it goes inside
    # the H3 element when emitted as `### {sig}`). The chip's `<a>`
    # has no DOM text content (visible label is a CSS pseudo-element),
    # so the H3's textContent is unaffected and Starlight's TOC stays
    # clean. Skip on LomObject itself (self-link) and on non-LOM
    # classes (Live.Base.Vector, Live.Base.Timer).
    if (
        class_index is not None
        and cls.get("path") != _LOM_OBJECT_PATH
        and is_lom_object(cls, class_index)
    ):
        sig = f"{sig}{lom_badge_html()}"
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


def function_signature_html(
    fn: dict,
    module_name: str,
) -> str:
    """Module-level function H3: `Live.Module.name()`.

    Path prefix + name (matching the class/enum convention) + empty
    `()` to mark the entry as callable. The full `(args) -> R` body
    is rendered separately on the next line by the caller — keeping
    Starlight's right-side TOC to a short `name()` instead of the
    full signature blob.
    """
    return _signature_html(
        name=fn["name"],
        module_name=module_name,
        suffix="()",
    )


def callable_signature_block_html(
    callable_node: dict,
    module_name: str,
    registry: dict[str, str],
    *,
    owning_class_name: str | None = None,
) -> str:
    """Render the Parameters / Returns block below a function H3 or
    method H5. Sphinx-style labeled sections, rendered as a sibling
    of the heading so the text stays out of `textContent`. One arg
    per line; empty sections are skipped (no-arg callables show only
    `Returns`; `None`-returning ones show only `Parameters`).

    `owning_class_name` (methods only): drops the `<class_name>.`
    prefix from default values matching the class — same trim that
    inline method signatures used to apply (e.g.
    `Song.CaptureMode.all` → `CaptureMode.all` on the Song page).
    """
    prefix = f"{owning_class_name}." if owning_class_name else None
    arg_items: list[str] = []
    for arg in callable_node.get("args") or []:
        arg_name = _resolve(arg, "name")
        if arg_name == "self":
            continue
        arg_type = _resolve(arg, "type")
        type_part = ""
        if arg_type:
            linked = linkify_type(
                display_type(arg_type), registry, current_module=module_name,
            )
            marker = override_marker_html(arg, "type")
            type_part = f': <span class="fn-arg-type">{linked}{marker}</span>'
        default = arg.get("default")
        if (
            prefix is not None
            and isinstance(default, str)
            and default.startswith(prefix)
        ):
            default = default[len(prefix):]
        default_part = ""
        if default is not None:
            default_part = (
                f' = <span class="fn-arg-default">{default}</span>'
            )
        arg_items.append(
            f'<li>'
            f'<span class="fn-arg-name">{arg_name}</span>'
            f'{type_part}{default_part}'
            f'</li>'
        )

    return_html = ""
    returns = callable_node.get("returns") or {}
    if isinstance(returns, dict):
        return_type = _resolve(returns, "type")
        # Skip `None` returns — they're the void-method default and
        # showing `Returns: None` for every mutator (delete_*, set_*,
        # ...) is noise. The convention becomes "no Returns section =
        # nothing meaningful to return," matching standard Python doc
        # convention. Genuinely-missing return types render the same
        # way (also no Returns section).
        if return_type and return_type != "None":
            return_html = linkify_type(
                display_type(return_type), registry,
                current_module=module_name,
            )
            return_html += override_marker_html(returns, "type")

    parts: list[str] = []
    if arg_items:
        # `Parameters` label deep-links to the Calling conventions
        # foundation page — every method / function takes positional
        # args only (no kwargs). The chip-style link explains the
        # binding's positional-only constraint and the `/` PEP 570
        # marker that surfaces in the generated `.pyi` stubs.
        params_href = f"{FOUNDATION_URL_BASE}/calling-conventions/"
        params_tooltip = (
            "All LOM methods / functions take positional arguments "
            "only. See Calling conventions for details."
        )
        parts.append(
            f'<div class="fn-sig-section">'
            f'<div class="fn-sig-label">'
            f'<a href="{params_href}" title="{params_tooltip}">'
            f'Parameters</a></div>'
            f'<ul class="fn-sig-args">{"".join(arg_items)}</ul>'
            f'</div>'
        )
    if return_html:
        parts.append(
            f'<div class="fn-sig-section">'
            f'<div class="fn-sig-label">Returns</div>'
            f'<div class="fn-sig-return">{return_html}</div>'
            f'</div>'
        )
    if not parts:
        return ""
    return f'<div class="fn-sig-block">{"".join(parts)}</div>'


def method_signature_html(method: dict) -> str:
    """Method H5 heading: `name()`.

    Bare method name + empty parens. The full `(args) -> R` body
    renders in a structured Parameters / Returns block below the
    H5, via `callable_signature_block_html` — same treatment as
    module functions. Keeps the H5 short and consistent with the
    function H3 convention.
    """
    name = _resolve(method, "name")
    return f"{name}()"


def emit_description_block(lines: list[str], member: dict, *, wrapped: bool) -> None:
    """Emit description prose for `member`.

    The body always renders as plain prose, regardless of source: authored
    `description:` when present, else the `raw_doc:` text as fallback. The
    source signal (runtime docstring vs authored, with the original
    raw_doc text on hover) is appended as a footnote marker at the end of
    the body so the affordance sits next to the prose it annotates rather
    than on the heading — see `source_footnote_html()`.

    `wrapped=True` puts the body inside `<div class="member-desc">`
    — used for properties / methods / signal-only nested under a class
    (indented gutter, muted color). `wrapped=False` emits at page margin
    — for class / enum / function H3 entities whose prose sits flush
    with the signature.

    Both fields honor sibling `<field>_override:` blocks via `_resolve`.
    """
    desc = _resolve(member, "description")
    raw = _resolve(member, "raw_doc")
    has_desc = isinstance(desc, str) and bool(desc.strip())
    has_raw = isinstance(raw, str) and bool(raw.strip())
    if has_desc:
        body = desc.strip()
    elif has_raw:
        body = normalize_paragraph(raw)
    else:
        return
    marker = source_footnote_html(member)
    if marker:
        # Put the marker on its own source line — joined inline with a
        # preceding text paragraph by markdown's adjacent-line rule, but
        # safely separated when the body ends in a block construct
        # (closing code fence, list, etc.) where appending content on
        # the same line would prevent the construct from closing and
        # break MDX parsing of everything that follows.
        body = f"{body}\n{marker}"
    if wrapped:
        lines.append(f'<div class="member-desc">\n\n{body}\n\n</div>')
    else:
        lines.append(body)
    lines.append("")


def source_footnote_html(member: dict) -> str:
    """Footnote marker on a member heading signalling the source of the
    rendered body text. Hover/focus reveals a structured tooltip.

    Two states (matching `emit_description_block`'s body-source logic):

    - `description:` present → body is authored prose. Tooltip shows
      the original `raw_doc` text under a "Runtime docstring" label so
      readers can compare authored vs source.
    - `description:` absent and `raw_doc:` present → body is the
      raw_doc text rendered verbatim. Tooltip says "Runtime docstring —
      not yet investigated."
    - Neither: returns empty string.

    The visible glyph is a CSS `::before` pseudo-element on
    `.source-marker` so MDX doesn't parse a literal character as
    markdown formatting.
    """
    desc = _resolve(member, "description")
    raw = _resolve(member, "raw_doc")
    has_desc = isinstance(desc, str) and bool(desc.strip())
    has_raw = isinstance(raw, str) and bool(raw.strip())
    if not has_raw:
        return ""

    if has_desc:
        raw_html = "<br/>".join(
            html.escape(line, quote=True)
            for line in raw.strip().splitlines()
        )
        inner = (
            f'<span class="sm-label">Runtime docstring</span>'
            f'<span class="sm-raw">{raw_html}</span>'
        )
        label = "view runtime docstring"
    else:
        inner = (
            f'<span class="sm-note">'
            f'From Live\'s runtime docstring.'
            f'</span>'
        )
        label = "from Live's runtime docstring"

    return (
        f'<sup class="source-marker" tabindex="0" '
        f'aria-label="{label}">'
        f'<span class="source-marker-tooltip" role="tooltip">'
        f'{inner}</span></sup>'
    )


def member_flags_html(member: dict) -> str:
    """Render small chip(s) for member modifiers — read-only,
    listenable. The default case (settable, not listenable for
    properties; not listenable for methods) returns empty string so
    most members render with no chips at all, keeping the page quiet
    for the common case and reserving visual weight for the deviations:

      - `[read-only]` — `settable: false` (properties only)
      - `[listen]`    — `listenable:` present (folded listener triplet)

    Output is inline HTML — `<span>` / `<a>` chips with no DOM text
    content. The visible labels come from CSS `::before`
    pseudo-elements on each `prop-flag-*` class; same `::before`
    trick used for the LomObject chip. This keeps the chip text out
    of the H5's `textContent`, so the auto-slug (and inherited-block
    link computation) sees only the property name + type.

    Returned HTML is appended INSIDE the H5 heading line; CSS
    floats it right onto the H5 row.
    """
    chips: list[str] = []
    if _resolve(member, "settable") is False:
        chips.append(
            '<span class="prop-flag prop-flag-ro" aria-label="read-only"></span>'
        )
    if _resolve(member, "listenable"):
        # Listener-only triplets (`listenable` present but no `type:` —
        # `Clip.notes`, `Track.data`, ...) deep-link the chip to the
        # Listener-only-triplets section of the foundation page;
        # value-bearing observable properties land at the page top.
        is_listener_only = not _resolve(member, "type")
        if is_listener_only:
            href = f"{FOUNDATION_URL_BASE}/listeners/#listener-only-triplets"
            tooltip = (
                "Listener-only triplet — see Listeners for what makes "
                "these distinct from value-bearing observables."
            )
        else:
            href = f"{FOUNDATION_URL_BASE}/listeners/"
            tooltip = (
                "This member is observable — see Listener for the "
                "subscription model."
            )
        chips.append(
            f'<a class="prop-flag prop-flag-listen" '
            f'href="{href}" '
            f'title="{tooltip}" aria-label="listen"></a>'
        )
    # Deprecated members carry a `deprecated:` field on their YAML
    # node — usually `deprecated: { replaced_by: <method_name> }`,
    # which produces a clickable chip jumping to the replacement
    # method's anchor on the same page. Bare `deprecated: true` (or
    # an empty dict) emits a non-link chip when no clean single
    # replacement exists; the method's `description:` carries any
    # migration prose in that case.
    deprecated = _resolve(member, "deprecated")
    if deprecated:
        replaced_by = (
            deprecated.get("replaced_by")
            if isinstance(deprecated, dict)
            else None
        )
        if replaced_by:
            chips.append(
                f'<a class="prop-flag prop-flag-deprecated" '
                f'href="#{replaced_by}" '
                f'title="Deprecated — use {replaced_by} instead." '
                f'aria-label="deprecated"></a>'
            )
        else:
            chips.append(
                '<span class="prop-flag prop-flag-deprecated" '
                'aria-label="deprecated"></span>'
            )
    if not chips:
        return ""
    return f'<span class="prop-flags">{"".join(chips)}</span>'


def property_heading_html(
    prop: dict,
    registry: dict[str, str],
    current_module: str | None = None,
) -> str:
    """Render a property name + Python-annotation-style type.

    H5 isn't in the right-side TOC (capped at H3) so the type can sit in
    the DOM text without polluting nav. Live types in the annotation
    become `<a>` links; non-Live tokens (`bool`, `None`, ...) stay literal.
    `current_module` shortens same-module type display via `linkify_type`.
    """
    name = _resolve(prop, "name")
    type_str = _resolve(prop, "type")
    if not type_str:
        return name
    rendered = linkify_type(
        display_type(type_str), registry, current_module=current_module,
    )
    marker = override_marker_html(prop, "type")
    return f'{name}<span class="prop-type">: {rendered}{marker}</span>'


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
        for top in doc.get("classes") or []:
            walk(top, module_name, base)
    return index


def build_references_index(
    modules: dict[str, dict],
    registry: dict[str, str],
) -> dict[str, list[dict]]:
    """Return `{qualified_target_path: [reference, ...]}` capturing every
    property `type:` and method `returns.type:` reference to a Live class.

    Drives the per-class "Referenced by" section. Each reference record:

        {
          "owner_module":   str,
          "owner_display":  str,   # `Track`, `Application.View`, ...
          "owner_anchor":   str,   # owner class's H3 anchor on its page
          "member_name":    str,
          "member_anchor":  str,   # member's H5 anchor on owner's page
          "kind":           "property" | "return",
          "type_str":       str,   # the original qualified type annotation
        }

    Filtering rules:
      - Self-references (a class's member that references the class
        itself, e.g. `Track.group_track: Track | None`) are skipped —
        the reader is already on the class's page.
      - LOM-universal members (`_live_ptr`, `canonical_parent`) are
        skipped — they declare on every LomObject class and would
        dominate every target's reference list with the same noise.
      - `Live.Base.Vector` is skipped as a target — the parametric
        base is referenced by every list-returning member in the LOM
        and is structural, not a navigable destination. Concrete
        XVector classes still register references.
      - Deprecated members are skipped — surfacing a class as
        "referenced by `set_notes` (deprecated)" misleads readers
        toward an API they shouldn't call.
    """
    index: dict[str, list[dict]] = {}
    universal = {"_live_ptr", "canonical_parent"}
    skip_targets = {"Live.Base.Vector"}

    def emit(target: str, record: dict) -> None:
        if target in skip_targets:
            return
        index.setdefault(target, []).append(record)

    def extract_targets(type_str: object) -> list[str]:
        if not isinstance(type_str, str):
            return []
        return _LIVE_CLASS_RE.findall(type_str)

    def walk_class(cls: dict, owner_module: str, prefix: str = "") -> None:
        if not isinstance(cls, dict):
            return
        name = cls.get("name")
        if not name:
            return
        owner_display = f"{prefix}.{name}" if prefix else name
        owner_path = cls.get("path") or ""
        owner_anchor = owner_display.lower().replace(".", "")

        for prop in cls.get("properties") or []:
            if _resolve(prop, "deprecated"):
                continue
            mname = _resolve(prop, "name")
            if not mname or mname in universal:
                continue
            type_str = _resolve(prop, "type")
            targets = extract_targets(type_str)
            if not targets:
                continue
            heading = property_heading_html(prop, registry, current_module=owner_module)
            member_anchor = starlight_slug(heading)
            for target in targets:
                if target == owner_path:
                    continue
                emit(target, {
                    "owner_module": owner_module,
                    "owner_display": owner_display,
                    "owner_anchor": owner_anchor,
                    "member_name": mname,
                    "member_anchor": member_anchor,
                    "kind": "property",
                    "type_str": type_str,
                })

        for method in cls.get("methods") or []:
            if _resolve(method, "deprecated"):
                continue
            mname = _resolve(method, "name")
            if not mname:
                continue
            returns = method.get("returns") or {}
            ret_type = (
                _resolve(returns, "type") if isinstance(returns, dict) else None
            )
            if not ret_type or ret_type == "None":
                continue
            targets = extract_targets(ret_type)
            if not targets:
                continue
            heading = method_signature_html(method)
            member_anchor = starlight_slug(heading)
            for target in targets:
                if target == owner_path:
                    continue
                emit(target, {
                    "owner_module": owner_module,
                    "owner_display": owner_display,
                    "owner_anchor": owner_anchor,
                    "member_name": mname,
                    "member_anchor": member_anchor,
                    "kind": "return",
                    "type_str": ret_type,
                })

        for nested in cls.get("classes") or []:
            walk_class(nested, owner_module, owner_display)

    for module_name, doc in modules.items():
        for top in doc.get("classes") or []:
            walk_class(top, module_name)

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


def group_inherited_by_ancestor(
    items: list[tuple[str, str, dict]],
) -> list[tuple[str, str, list[dict]]]:
    """Group `[(anc_path, anc_module, item), ...]` by ancestor,
    preserving first-encountered order. Returns
    `[(anc_path, anc_module, [items]), ...]`.
    """
    by_ancestor: list[list] = []
    seen: dict[str, int] = {}
    for anc_path, anc_module, item in items:
        if anc_path not in seen:
            seen[anc_path] = len(by_ancestor)
            by_ancestor.append([anc_path, anc_module, []])
        by_ancestor[seen[anc_path]][2].append(item)
    return [(p, m, items) for p, m, items in by_ancestor]


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
            slug = starlight_slug(method_signature_html(method))
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
    references_index: dict[str, list[dict]] | None = None,
    body_only: bool = False,
) -> str:
    """Render one module's MDX page (Step 5: properties + inherited).

    Layout:
      - YAML frontmatter (title + description) — skipped when `body_only`
      - Module description paragraph — skipped when `body_only`
      - Primary class section: signature, doc, own properties, inherited
      - "Other classes" section: each class as a sub-section
      - Module Enums section
      - Module Functions section

    `body_only=True` skips the frontmatter and the top-level description
    paragraph so the result can be embedded inside a foundation-page MDX
    after the foundation's own prose. The class / enum / function
    sections render identically in both modes.
    """
    if class_index is None:
        class_index = {}
    if references_index is None:
        references_index = {}
    # Hand-authored module description (per doc/lom-format.md). Falls back
    # to a visible placeholder so empty modules are obvious to writers.
    description = doc.get("description") or "_No module description._"
    # SEO frontmatter — strip markdown emphasis from the placeholder so the
    # `<meta>` snippet reads naturally.
    seo_description = first_sentence(doc.get("description")) or f"Reference for Live.{module_name}."

    # Split classes into "primary" (the conventional Live.X.X self-named
    # class) and "other" by matching the module name. A few modules
    # (Conversions, Licensing — function-only) have no primary class.
    all_classes = doc.get("classes") or []
    primary_classes = [c for c in all_classes if c.get("name") == module_name]
    other_classes = [c for c in all_classes if c.get("name") != module_name]
    enums = doc.get("enums") or []
    functions = doc.get("functions") or []

    main_class = primary_classes[0] if primary_classes else None

    lines: list[str] = []
    if not body_only:
        # Title defaults to the module name. Modules can override via a
        # top-level `title:` field in their lom YAML when a more
        # descriptive page heading is warranted.
        page_title = doc.get("title") or module_name
        lines.append("---")
        lines.append(f"title: {page_title}")
        lines.append(f'description: "{escape_yaml_scalar(seo_description)}"')
        # Pages flagged `sidebar_hidden: true` in their lom YAML are
        # excluded from Starlight's autogenerated sidebar group.
        if doc.get("sidebar_hidden"):
            lines.append("sidebar:")
            lines.append("  hidden: true")
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
        # LomObject chip is appended INSIDE the H3 sig HTML by
        # `class_signature_html` (its `<a>` has no DOM text content;
        # the visible label comes from CSS `::before` so the H3's
        # textContent stays clean for Starlight's TOC).
        sig = class_signature_html(
            cls, module_name, registry,
            display_name=display_name, class_index=class_index,
        )
        lines.append(f"### {sig}")
        lines.append("")
        # Hand-authored, multi-paragraph class description (markdown)
        # lives on the class node as `description:` (see lom-format.md —
        # analogous to the module-top-level `description:`, but scoped
        # to one class) and overrides parser-derived `raw_doc`. The
        # original raw_doc remains accessible via the source-footnote
        # marker on the H3 heading (see `source_footnote_html`).
        emit_description_block(lines, cls, wrapped=False)
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
        # Partition properties into active vs deprecated. Deprecated
        # properties join the deprecated methods in the collapsed
        # `<details>` block at the bottom of the class.
        deprecated_properties = [p for p in properties if _resolve(p, "deprecated")]
        properties = [p for p in properties if not _resolve(p, "deprecated")]

        # Group inherited members by ancestor — properties go at the
        # top of the Properties section, methods at the top of the
        # Methods section. One collapsed `<details class="...-inherited-section">`
        # per ancestor that contributes; LomObject gets its own
        # purple-tinted CSS class to read as a foundation cue, other
        # ancestors use a neutral gray box.
        inherited_props_by_anc = (
            group_inherited_by_ancestor(inherited_properties(cls, class_index))
            if class_index is not None else []
        )
        inherited_methods_by_anc = (
            group_inherited_by_ancestor(inherited_methods(cls, class_index))
            if class_index is not None else []
        )

        # LOM-universal pair (`_live_ptr`, `canonical_parent`) belongs
        # in the LomObject box conceptually, even when the closest
        # MRO declaration is on an intermediate ancestor (e.g.
        # DriftDevice inherits `canonical_parent` from Device with the
        # narrower `Track` type — but the reader expects to see it
        # alongside `_live_ptr` under "From LomObject"). Resolve the
        # pair from the closest declaration; filter the same names
        # out of the regular Properties + the other ancestor boxes;
        # rebuild the LomObject ancestor entry with the resolved pair.
        pinned: list[dict] = []
        if (
            class_index is not None
            and is_lom_object(cls, class_index)
            and cls.get("path") != _LOM_OBJECT_PATH
        ):
            pinned = resolve_lom_universal(cls, class_index)
        pinned_names = {_resolve(p, "name") for p in pinned}
        if pinned_names:
            properties = [
                p for p in properties
                if _resolve(p, "name") not in pinned_names
            ]
            inherited_props_by_anc = [
                (a, m, [p for p in props if _resolve(p, "name") not in pinned_names])
                for a, m, props in inherited_props_by_anc
                if a != _LOM_OBJECT_PATH
            ]
            inherited_props_by_anc = [
                (a, m, props) for a, m, props in inherited_props_by_anc if props
            ]
            inherited_props_by_anc.append(
                (_LOM_OBJECT_PATH, "LomObject", pinned)
            )

        # Reverse both lists so the foundational ancestor (LomObject)
        # leads, working down toward the most-specific. BFS gave us
        # closest-first; foundational-first reads more naturally
        # ("here are the LOM basics, then what Device adds, then ...")
        # — and gives the LomObject box stable top-of-section
        # placement matching how class signatures advertise the
        # LomObject badge first too.
        inherited_props_by_anc = list(reversed(inherited_props_by_anc))
        inherited_methods_by_anc = list(reversed(inherited_methods_by_anc))

        def _emit_inherited_box(
            anc_path: str,
            anc_module: str,
            members: list[dict],
            kind: str,
            open_by_default: bool = False,
        ) -> None:
            """Emit one collapsed `<details>` per ancestor, with full
            renders of the inherited members inside. `kind` is
            'property' or 'method'. `open_by_default` expands the box
            on page load — used when the section has no own members,
            so the reader isn't left staring at an empty section."""
            anc_name = anc_path.rsplit(".", 1)[-1]
            is_lom = anc_path == _LOM_OBJECT_PATH
            anc_anchor_section = (
                "properties" if kind == "property" else "methods"
            )
            href = (
                f"{DOCS_URL_BASE}/{anc_module.lower()}/#{anc_anchor_section}"
                if is_lom else
                f"{DOCS_URL_BASE}/{anc_module.lower()}/#{anc_name.lower()}"
            )
            open_attr = " open" if open_by_default else ""
            lines.append(f'<details class="inherited-section"{open_attr}>')
            lines.append(
                f'<summary>Inherited from '
                f'<a href="{href}"><code>{anc_name}</code></a>'
                f'</summary>'
            )
            lines.append("")
            for m in members:
                if kind == "property":
                    heading = property_heading_html(m, registry, current_module=anc_module)
                    flags = member_flags_html(m)
                    lines.append(f"##### {heading}{flags}")
                    lines.append("")
                    emit_description_block(lines, m, wrapped=True)
                else:  # method
                    heading = method_signature_html(m)
                    flags = member_flags_html(m)
                    lines.append(f"##### {heading}{flags}")
                    lines.append("")
                    sig_block = callable_signature_block_html(
                        m, anc_module, registry,
                        owning_class_name=anc_name,
                    )
                    if sig_block:
                        lines.append(sig_block)
                        lines.append("")
                    emit_description_block(lines, m, wrapped=True)
            lines.append('</details>')
            lines.append("")

        if inherited_props_by_anc or properties:
            lines.append("#### Properties")
            lines.append("")
            inherited_props_open = not properties
            for anc_path, anc_module, props in inherited_props_by_anc:
                _emit_inherited_box(
                    anc_path, anc_module, props, "property",
                    open_by_default=inherited_props_open,
                )
            for prop in properties:
                heading = property_heading_html(prop, registry, current_module=module_name)
                flags = member_flags_html(prop)
                lines.append(f"##### {heading}{flags}")
                lines.append("")
                emit_description_block(lines, prop, wrapped=True)
        # Signal-only listener triplets — `notes`, `loop_jump`, etc.
        # Surfaced in their own section so the reader doesn't read
        # them as untyped properties; the section header is the
        # signal that "these are subscription points, not attributes."
        # The `[listen]` chip stays on each entry as the link to the
        # Listener foundation page.
        if signals:
            lines.append("#### Listener Only")
            lines.append("")
            for prop in signals:
                # H5 is the bare event name (`notes`, `loop_jump`,
                # ...) — clean for slug + TOC. The actual three
                # triplet methods (`add_X_listener`,
                # `remove_X_listener`, `X_has_listener`) render in a
                # sub-line below the heading, dot-separated, in
                # muted scaffolding color. Reader gets the full
                # triplet without the H5 needing to disambiguate
                # alternation.
                heading = property_heading_html(prop, registry, current_module=module_name)
                flags = member_flags_html(prop)
                lines.append(f"##### {heading}{flags}")
                lines.append("")
                triplet = _listener_triplet(prop)
                if triplet:
                    methods_html = "  ·  ".join(
                        f'<span class="listener-only-method">{m}</span>'
                        for m in triplet
                    )
                    lines.append(
                        f'<div class="listener-only-triplet">{methods_html}</div>'
                    )
                    lines.append("")
                emit_description_block(lines, prop, wrapped=True)
        # Filter listener-triplet methods folded into a parent method's
        # `listenable:` field — the parameterized-observable case (the
        # only current example: `Application.View.is_view_visible` and
        # its three matching `*_listener` methods). The triplet members
        # are surfaced via the parent method's `[listen]` chip; their
        # signatures are documented through the parent's `description:`.
        triplet_method_names: set[str] = set()
        for m in cls.get("methods") or []:
            for triplet_name in _listener_triplet(m):
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
        # Container classes (`Live.Base.Vector` and every concrete
        # `XVector`) bind `append` and `extend` at the runtime level,
        # but the lom YAML build filters them — they're synthesized at
        # stub-render time from the container flag + element type
        # (see doc/lom-format.md §"Iterable container classes"). Mirror
        # the synthesis here so the rendered reference shows the same
        # mutator API. Element type: parametric `Vector` itself uses
        # the type variable `T`; concrete containers use their
        # resolved `element_type:`.
        synth_methods: list[dict] = []
        if cls.get("container") or cls.get("parametric"):
            cls_path = cls.get("path") or ""
            if cls.get("parametric"):
                elem_type = "T"
            else:
                elem_type = _resolve(cls, "element_type")
            if elem_type:
                synth_methods = [
                    {
                        "name": "append",
                        "args": [
                            {"name": "self", "type": cls_path},
                            {"name": "value", "type": elem_type},
                        ],
                        "returns": {"type": "None"},
                    },
                    {
                        "name": "extend",
                        "args": [
                            {"name": "self", "type": cls_path},
                            {"name": "values", "type": f"Iterable[{elem_type}]"},
                        ],
                        "returns": {"type": "None"},
                    },
                ]
        methods = synth_methods + methods
        # Partition active vs deprecated. Deprecated methods get
        # surfaced in a collapsed `<details>` block at the bottom
        # of the class so they don't crowd the main Methods list
        # but stay reachable for readers maintaining older code.
        active_methods = [m for m in methods if not _resolve(m, "deprecated")]
        deprecated_methods = [m for m in methods if _resolve(m, "deprecated")]

        def _render_method(method: dict) -> None:
            heading = method_signature_html(method)
            flags = member_flags_html(method)
            lines.append(f"##### {heading}{flags}")
            lines.append("")
            sig_block = callable_signature_block_html(
                method, module_name, registry,
                owning_class_name=cls.get("name"),
            )
            if sig_block:
                lines.append(sig_block)
                lines.append("")
            emit_description_block(lines, method, wrapped=True)

        if inherited_methods_by_anc or active_methods:
            lines.append("#### Methods")
            lines.append("")
            inherited_methods_open = not active_methods
            for anc_path, anc_module, methods_from_anc in inherited_methods_by_anc:
                _emit_inherited_box(
                    anc_path, anc_module, methods_from_anc, "method",
                    open_by_default=inherited_methods_open,
                )
            for method in active_methods:
                _render_method(method)

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

        # Deprecated section — last in the class block. Holds members
        # the YAML's `deprecated:` field flagged. Collapsed by default
        # so the supported API reads cleanly; deprecated members stay
        # reachable for readers maintaining older code.
        if deprecated_properties or deprecated_methods:
            lines.append('<details class="deprecated-section">')
            lines.append('<summary>Deprecated</summary>')
            lines.append("")
            for prop in deprecated_properties:
                heading = property_heading_html(prop, registry, current_module=module_name)
                flags = member_flags_html(prop)
                lines.append(f"##### {heading}{flags}")
                lines.append("")
                emit_description_block(lines, prop, wrapped=True)
            for method in deprecated_methods:
                _render_method(method)
            lines.append('</details>')
            lines.append("")

        # References — every member elsewhere in the LOM whose type or
        # return is this class. Collapsed by default; gated on
        # non-empty (most non-data-bearing classes have nothing here).
        # Sits at the very bottom of the class block so the class's
        # own structural surface (Properties, Methods, Nested types,
        # Deprecated) reads first.
        class_path = cls.get("path")
        refs = references_index.get(class_path, []) if class_path else []
        if refs:
            refs_sorted = sorted(
                refs,
                key=lambda r: (
                    r["owner_module"], r["owner_display"], r["member_name"],
                ),
            )
            count = len(refs_sorted)
            label = (
                f"Returned by {count} member"
                f"{'s' if count != 1 else ''} elsewhere in the LOM"
            )
            lines.append('<details class="references-section">')
            lines.append(f'<summary>{label}</summary>')
            lines.append("")
            current_owner: str | None = None
            current_anchor = ""
            current_module = ""
            for ref in refs_sorted:
                owner_display = ref["owner_display"]
                if owner_display != current_owner:
                    if current_owner is not None:
                        lines.append('</ul>')
                        lines.append('</div>')
                    current_owner = owner_display
                    current_anchor = ref["owner_anchor"]
                    current_module = ref["owner_module"]
                    href = (
                        f'{DOCS_URL_BASE}/{current_module.lower()}/'
                        f'#{current_anchor}'
                    )
                    lines.append('<div class="ref-group">')
                    lines.append(
                        f'<a class="ref-owner" href="{href}">'
                        f'<code>{owner_display}</code></a>'
                    )
                    lines.append('<ul class="ref-members">')
                type_html = linkify_type(
                    display_type(ref["type_str"]), registry,
                    current_module=module_name,
                )
                member_href = (
                    f'{DOCS_URL_BASE}/{ref["owner_module"].lower()}/'
                    f'#{ref["member_anchor"]}'
                )
                if ref["kind"] == "return":
                    inner = (
                        f'<a class="ref-member-link" href="{member_href}">'
                        f'<span class="ref-member-name">'
                        f'{ref["member_name"]}()</span></a>'
                        f'<span class="ref-arrow"> → </span>'
                        f'<span class="ref-type">{type_html}</span>'
                    )
                else:
                    inner = (
                        f'<a class="ref-member-link" href="{member_href}">'
                        f'<span class="ref-member-name">'
                        f'{ref["member_name"]}</span></a>'
                        f'<span class="ref-sep">: </span>'
                        f'<span class="ref-type">{type_html}</span>'
                    )
                lines.append(f'<li>{inner}</li>')
            if current_owner is not None:
                lines.append('</ul>')
                lines.append('</div>')
            lines.append('</details>')
            lines.append("")

    if main_class is not None:
        emit_class(main_class)

    # Collect every non-primary class and every nested class/enum at
    # any depth. Each hoisted entry carries the full dotted display
    # path (e.g. `Application.View`, `Application.View.NavDirection`)
    # so the qualified identity is clear and the slug matches the
    # link list emitted by the parent's `#### Nested types` block.
    # Parents' Nested types lists only show *direct* children — the
    # reader walks into a nested class's hoisted entry to find its
    # own Nested types list, recursively.
    classes_flat: list[tuple[str | None, dict]] = []  # (display_path, cls)
    enums_flat: list[tuple[str | None, dict]] = []    # (display_path, enum)
    for cls in other_classes:
        classes_flat.append((None, cls))
    for enum in enums:
        enums_flat.append((None, enum))

    def _walk_nested(cls: dict, prefix: str) -> None:
        for nc in cls.get("classes") or []:
            display = f"{prefix}.{nc['name']}"
            classes_flat.append((display, nc))
            _walk_nested(nc, display)
        for ne in cls.get("enums") or []:
            display = f"{prefix}.{ne['name']}"
            enums_flat.append((display, ne))

    for top_cls in [*primary_classes, *other_classes]:
        _walk_nested(top_cls, top_cls["name"])

    if classes_flat:
        # "Other classes" only makes sense when there's a primary; without
        # one (function-only modules and the like) just call them Classes.
        header = "Other classes" if main_class is not None else "Classes"
        lines.append(f"## {header}")
        lines.append("")
        for display, cls in classes_flat:
            emit_class(cls, display_name=display)

    if enums_flat:
        lines.append("## Enums")
        lines.append("")
        for display, enum in enums_flat:
            sig = enum_signature_html(enum, module_name, display_name=display)
            lines.append(f"### {sig}")
            lines.append("")
            # Enum description — top-level H3 entity, sits at page
            # margin like a class description. NOT wrapped in
            # `.member-desc` (that's for property / method descriptions
            # nested under a class's H4 sections).
            emit_description_block(lines, enum, wrapped=False)
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
            lines.append(f"### {function_signature_html(fn, module_name)}")
            lines.append("")
            sig_block = callable_signature_block_html(fn, module_name, registry)
            if sig_block:
                lines.append(sig_block)
                lines.append("")
            emit_description_block(lines, fn, wrapped=False)

    return "\n".join(lines)


# --- CLI --------------------------------------------------------------- #


_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n?", re.DOTALL)


def parse_foundation_markdown(path: Path) -> tuple[dict, str]:
    """Parse a foundation markdown file into `(frontmatter, body)`.

    Foundation pages carry their content as standard MDX-style files —
    YAML frontmatter between `---` fences, markdown body after. Authors
    edit these directly under `content/<v>/` rather than going
    through the lom YAML.
    """
    text = path.read_text()
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    frontmatter = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return frontmatter, body


def render_foundation_page(
    frontmatter: dict,
    body: str,
    module_doc: dict | None,
    registry: dict[str, str],
    class_index: dict[str, tuple[str, dict]],
    references_index: dict[str, list[dict]],
) -> str:
    """Compose a foundation page MDX: frontmatter + authored prose +
    (optionally) the absorbed module's structural rendering.

    `frontmatter` keys honored:
      - `title:` — page title (required)
      - `slug:` — Starlight slug override; defaults to filename
      - `sidebar_badge:` — badge text on the manual sidebar entry
        (the badge itself lives in `astro.config.mjs`; this field is
        informational documentation of the link).
      - `include_module: X` — if present, `module_doc` should be the
        lom YAML for module `X`; its class / enum / function content
        is appended to the page after the markdown body.
    """
    title = frontmatter.get("title") or "Untitled"
    description = first_sentence(body) or title
    lines: list[str] = []
    lines.append("---")
    lines.append(f"title: {title}")
    lines.append(f'description: "{escape_yaml_scalar(description)}"')
    # Foundation pages are hoisted manually in `astro.config.mjs`;
    # hide them from Starlight's autogenerated Modules group so they
    # don't appear twice in the sidebar.
    lines.append("sidebar:")
    lines.append("  hidden: true")
    lines.append("---")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")
    if module_doc is not None:
        module_name = module_doc["module"]
        lines.append(render_module_page(
            module_name, module_doc, registry, class_index, references_index,
            body_only=True,
        ).rstrip())
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    parser.add_argument("version", nargs="?", default="12.3.6",
                        help="Live version (default: 12.3.6)")
    parser.add_argument("--input", help="modules markdown dir (default: content/<v>/modules)")
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "web" / "src" / "content" / "docs"),
        help="output dir for MDX (default: web/src/content/docs)",
    )
    args = parser.parse_args()

    md_dir = Path(args.input) if args.input else REPO_ROOT / "content" / args.version / "modules"
    # Foundation pages are siblings to `modules/` — flat in content/<v>/.
    foundation_dir = md_dir.parent
    out_dir = Path(args.output)

    if not md_dir.exists():
        print(f"error: modules markdown dir not found at {md_dir}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)

    parse_dir = str(REPO_ROOT / "tools" / "parse")
    if parse_dir not in sys.path:
        sys.path.insert(0, parse_dir)
    from parse_module_md import parse_module_md, regraft_hoisted

    # Load every module up front — registry build needs cross-module
    # visibility for type linking.
    modules: dict[str, dict] = {}
    for path in sorted(md_dir.glob("*.md")):
        d = regraft_hoisted(parse_module_md(path))
        if isinstance(d, dict) and d.get("module"):
            modules[d["module"]] = d

    registry = build_class_registry(modules)
    class_index = build_class_index(modules)
    references_index = build_references_index(modules, registry)

    # Foundation pages — authored markdown files under
    # `content/<v>/`. Each may absorb a lom module's
    # structural content via `include_module:` frontmatter; absorbed
    # modules are skipped from the regular per-module page output.
    absorbed_modules: set[str] = set()
    foundation_pages: list[tuple[Path, dict, str]] = []
    if foundation_dir.exists():
        for path in sorted(foundation_dir.glob("*.md")):
            fm, body = parse_foundation_markdown(path)
            foundation_pages.append((path, fm, body))
            mod = fm.get("include_module")
            if mod:
                absorbed_modules.add(mod)

    written = 0
    for path, fm, body in foundation_pages:
        slug = fm.get("slug") or path.stem
        include_module = fm.get("include_module")
        module_doc = modules.get(include_module) if include_module else None
        text = render_foundation_page(
            fm, body, module_doc, registry, class_index, references_index,
        )
        # Foundation pages render at the site root (`<slug>.mdx`) so
        # their URLs are `/<slug>/`, not `/modules/<slug>/` — they're
        # cross-cutting concepts, not per-module reference pages.
        out_file = out_dir / f"{slug}.mdx"
        out_file.write_text(text)
        written += 1

    for module_name, doc in modules.items():
        if module_name in absorbed_modules:
            continue
        out_file = out_dir / relpath_for(module_name)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(render_module_page(
            module_name, doc, registry, class_index, references_index,
        ))
        written += 1

    print(f"Wrote {written} pages to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

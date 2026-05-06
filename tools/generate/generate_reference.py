#!/usr/bin/env python3
"""Generate Starlight (Astro) MDX reference pages from LiveTree.refined.json.

Phase 1 of the documentation roadmap (`doc/reference-roadmap.md`): mechanical
translation of what the parser already knows. Built incrementally per the
step-ladder — each step adds one layer of detail to the rendered output.

Step 1 (current):
    Module page skeletons. One MDX page per top-level Live module, with the
    module's title, a one-line description, and a bullet list of the class
    names it contains. No per-class detail yet.

Output layout — flat, one MDX page per module:

    web/src/content/docs/
      <Module>.mdx

Usage:
    python tools/generate/generate_reference.py [--input PATH] [--output DIR]

Defaults:
    --input   stubs/12.3.6/pipeline/LiveTree.refined.json
    --output  web/src/content/docs
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

_ANCESTOR_RE = re.compile(r"<class '([^']+)'>")
_BORING_BASES = {
    "Boost.Python.instance",
    "instance",
    "object",
}


def base_class_for(class_node: dict) -> str | None:
    """Return the simple name of the closest informative base class, or None.

    Filters out `Boost.Python.instance` and friends — they're essentially
    `object` and don't carry useful info in the displayed signature.
    """
    for ancestor_repr in class_node.get("ancestors", []):
        m = _ANCESTOR_RE.match(ancestor_repr)
        if not m:
            continue
        full = m.group(1)
        if full in _BORING_BASES:
            continue
        # Take the last dotted component as the displayed name.
        return full.rsplit(".", 1)[-1]
    return None


def relpath_for(module_name: str) -> str:
    """Return the docs-relative path for a module's MDX file (no leading slash).

    All module pages live under `modules/` so Starlight's `autogenerate` works
    cleanly — autogenerating from the docs root collides with index.mdx and
    leaves the sidebar empty.
    """
    return f"modules/{module_name}.mdx"


def first_sentence(text: str | None) -> str:
    """Extract the first sentence from a runtime docstring, normalized."""
    if not text:
        return ""
    flat = " ".join(line.strip() for line in text.strip().splitlines() if line.strip())
    # Clip at first period+space, retaining the period.
    if ". " in flat:
        return flat.split(". ", 1)[0] + "."
    return flat


def escape_yaml_scalar(text: str) -> str:
    """Escape a string for a YAML frontmatter scalar (quoted form)."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def _signature_html(
    *,
    kw: str,
    name: str,
    module_name: str,
    base: str | None = None,
    suffix: str = "",
) -> str:
    """Render a syntax-highlighted signature span.

    Nested span structure so pseudo-elements can color the keyword, path,
    and base distinctly:

        <span class="sig" data-kw=... data-base=...>
          <span class="sig-name" data-path=...>NAME</span>
        </span>

    Only the innermost text node ("NAME") is in the DOM text content, so
    Starlight's right-side TOC shows just the bare name — the keyword,
    path, and base render via CSS pseudo-elements and don't pollute the
    TOC label.

    `suffix` is for visual additions kept in DOM text (e.g. empty `()` on
    function signatures — small enough that a parenthesized TOC reads fine).
    """
    outer_attrs = f' data-kw="{kw}"'
    if base:
        outer_attrs += f' data-base="({base})"'
    inner_attrs = f' data-path="Live.{module_name}."'
    return (
        f'<span class="sig"{outer_attrs}>'
        f'<span class="sig-name"{inner_attrs}>{name}</span>'
        f"</span>{suffix}"
    )


def class_signature_html(class_node: dict, module_name: str) -> str:
    """Render a class signature."""
    return _signature_html(
        kw="class",
        name=class_node["name"],
        module_name=module_name,
        base=base_class_for(class_node),
    )


def enum_signature_html(enum_node: dict, module_name: str) -> str:
    """Render an enum signature. All Live enums inherit `int`; base is implicit."""
    return _signature_html(
        kw="enum",
        name=enum_node["name"],
        module_name=module_name,
    )


def function_signature_html(fn_node: dict, module_name: str) -> str:
    """Render a function signature. Empty parens for now — args land in Step 9."""
    return _signature_html(
        kw="def",
        name=fn_node["name"],
        module_name=module_name,
        suffix="()",
    )


def render_module_page(module_node: dict) -> str:
    """Render one module's MDX page (Step 1: skeleton only)."""
    module_name = module_node["name"]
    raw_doc = module_node.get("raw_doc")
    description = first_sentence(raw_doc) or f"The Live.{module_name} module."

    classes = [
        c for c in module_node.get("children", [])
        if c.get("type") == "class" and c.get("name")
    ]
    enums = [
        c for c in module_node.get("children", [])
        if c.get("type") == "enum" and c.get("name")
    ]
    functions = [
        c for c in module_node.get("children", [])
        if c.get("type") == "function" and c.get("name")
    ]

    # The "main" class is the one with the same name as its module — that's
    # the conventional Live.X module / Live.X.X class pairing (Live.Song.Song,
    # Live.Track.Track, etc.). Some modules have no self-named class; in that
    # case all classes go under "Classes" and there's no main signature line.
    main_class = next((c for c in classes if c["name"] == module_name), None)
    other_classes = [c for c in classes if c is not main_class]

    lines: list[str] = []
    lines.append("---")
    lines.append(f"title: {module_name}")
    lines.append(f'description: "{escape_yaml_scalar(description)}"')
    lines.append("---")
    lines.append("")

    # Module-level intro. Most modules have no docstring, so this is usually
    # just the placeholder — we'll fold authored prose in via the Phase-2
    # records system.
    lines.append(description)
    lines.append("")

    # Main class — rendered as a regular H3 under its own "Primary class"
    # H2 section. Members (properties, methods, inner classes) of the main
    # class will land here in later steps as the H3's body content.
    if main_class is not None:
        lines.append("## Primary class")
        lines.append("")
        lines.append(f"### {class_signature_html(main_class, module_name)}")
        lines.append("")

    # Other classes — auxiliary types that live alongside the main class in
    # the same module (e.g. Live.Song has BeatTime, CuePoint, SmptTime in
    # addition to Song itself). Header label changes based on whether there
    # was a main class.
    if other_classes:
        header = "Other classes" if main_class is not None else "Classes"
        lines.append(f"## {header}")
        lines.append("")
        for cls in other_classes:
            lines.append(f"### {class_signature_html(cls, module_name)}")
            lines.append("")

    # Enums use the same signature span structure — keyword `enum` (semantically
    # clearer than the literal `class Foo(int):` Python construct). All Live
    # enums inherit from `int`; the base is implicit and not rendered.
    if enums:
        lines.append("## Module Enums")
        lines.append("")
        for enum in enums:
            lines.append(f"### {enum_signature_html(enum, module_name)}")
            lines.append("")

    # Functions render with `def` and empty parens — args land in a later
    # step, but the parens flag the heading as a callable up front.
    if functions:
        lines.append("## Module Functions")
        lines.append("")
        for fn in functions:
            lines.append(f"### {function_signature_html(fn, module_name)}")
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    parser.add_argument(
        "--input",
        default=str(REPO_ROOT / "stubs" / "12.3.6" / "pipeline" / "LiveTree.refined.json"),
    )
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "web" / "src" / "content" / "docs"),
    )
    args = parser.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.output)

    if not in_path.exists():
        print(f"error: refined tree not found at {in_path}", file=sys.stderr)
        return 2

    data = json.loads(in_path.read_text())
    tree = data["tree"]

    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for module_node in tree.get("children", []):
        if module_node.get("type") != "module":
            continue
        module_name = module_node.get("name")
        if not module_name:
            continue
        out_file = out_dir / relpath_for(module_name)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(render_module_page(module_node))
        written += 1

    print(f"Wrote {written} module pages to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

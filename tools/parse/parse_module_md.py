#!/usr/bin/env python3
"""Parse a per-module markdown file into an in-memory module dict.

Reads `stubs/<v>/modules/<Module>.md` and returns a dict matching the
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
    if sections.preamble.strip():
        module["description"] = sections.preamble.rstrip() + "\n"

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

    cls: dict[str, Any] = {"name": name}
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
    member: dict[str, Any] = {"name": name}
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
        entry: dict[str, Any] = {"name": h3_title}
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


# ---------------------------------------------------------------------- CLI


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Module markdown file to parse")
    parser.add_argument(
        "--format", choices=("yaml", "json", "repr"), default="yaml",
        help="Output format (default: yaml)",
    )
    args = parser.parse_args()
    data = parse_module_md(Path(args.path))
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

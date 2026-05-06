#!/usr/bin/env python3
"""Find tree members still needing manual refinement entries.

Walks LiveTree.refined.json (post-refinement output) and reports anything the
parser couldn't pin down: function args/returns still typed `object`/`tuple`/
`list`, args still named `argN`, properties with null or `NoneType`
probed_type, and iterable classes/properties missing `element_repr`.

Each line is a candidate for a manual_refinements.yaml entry — runs are useful
after a fresh capture, a corpus pin bump, or just to get a sense of what's
left unresolved.

Usage:
    python tools/parse/find_unrefined.py 12.3.6
    python tools/parse/find_unrefined.py 12.3.6 --kind arg_type
    python tools/parse/find_unrefined.py 12.3.6 --top-classes 10
    python tools/parse/find_unrefined.py 12.3.6 --output /tmp/unrefined.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

ARGN_RE = re.compile(r"^arg\d+$")

# Types the parser emits when it couldn't narrow further. `LomObject` is
# omitted — it's a legitimate type (used in refinements for device-container
# args that genuinely accept any LomObject) and flagging it produces noise.
UNRESOLVED_TYPES = {"object", "tuple", "list"}

# probed_type values that signal "probe didn't catch a real value."
UNRESOLVED_PROBED = {None, "NoneType", "None"}

# Property names where None is the actual value (don't flag).
KNOWN_NONE_PROPS = {"canonical_parent"}

# Categorized findings — flat list of (kind, path, detail).
Finding = tuple[str, str, str]


def _walk(node: dict, path: str, iterable_classes: dict[str, bool], findings: list[Finding]) -> None:
    if node.get("ref"):
        return

    name = node.get("name", "")
    cur = f"{path}.{name}" if path and name else (path or name)
    node_type = node.get("type", "")

    if node_type in ("function", "method_descriptor", "builtin_function_or_method"):
        _check_function(node, cur, findings)
    elif node_type == "property":
        _check_property(node, cur, iterable_classes, findings)
    elif node_type == "class":
        _check_class(node, cur, findings)

    for child in node.get("children") or []:
        _walk(child, cur, iterable_classes, findings)


def _collect_iterable_classes(tree: dict) -> dict[str, bool]:
    """Map iterable-class name → whether it has element_repr resolved."""
    out: dict[str, bool] = {}

    def walk(node: dict) -> None:
        if node.get("type") == "class" and node.get("iterable"):
            out[node.get("name", "")] = bool(node.get("element_repr"))
        for child in node.get("children") or []:
            walk(child)

    walk(tree)
    return out


def _check_function(node: dict, path: str, findings: list[Finding]) -> None:
    args = node.get("args") or []
    for arg in args:
        aname = arg.get("name") or ""
        atype = arg.get("type") or ""
        if aname == "self":
            continue
        if atype in UNRESOLVED_TYPES:
            findings.append(("arg_type", path, f"{aname}: {atype}"))
        if ARGN_RE.match(aname):
            findings.append(("arg_name", path, f"{aname}"))

    returns = node.get("returns") or {}
    rtype = returns.get("type")
    if rtype in UNRESOLVED_TYPES:
        findings.append(("return_type", path, str(rtype)))


def _check_property(node: dict, path: str, iterable_classes: dict[str, bool], findings: list[Finding]) -> None:
    name = node.get("name", "")
    probed = node.get("probed_type")
    if name in KNOWN_NONE_PROPS:
        return
    if probed in UNRESOLVED_PROBED:
        findings.append(("probed_type", path, f"probed_type={probed!r}"))
        return
    # Iterable property whose element type isn't known.
    if not node.get("element_repr"):
        if probed in iterable_classes and not iterable_classes[probed]:
            findings.append(("element_repr_property", path, f"probed_type={probed}"))
        elif probed in ("tuple", "list"):
            findings.append(("element_repr_property", path, f"probed_type={probed}"))


def _check_class(node: dict, path: str, findings: list[Finding]) -> None:
    if node.get("iterable") and not node.get("element_repr"):
        findings.append(("element_repr_class", path, "iterable=True"))


def _format_report(findings: list[Finding], top_classes: int) -> str:
    by_kind: dict[str, list[tuple[str, str]]] = {}
    for kind, path, detail in findings:
        by_kind.setdefault(kind, []).append((path, detail))

    lines: list[str] = []
    lines.append("# Unrefined items in `LiveTree.refined.json`")
    lines.append("")
    lines.append("Each entry is a candidate for a `tools/parse/manual_refinements.yaml` "
                 "entry. Categories listed in priority order — type accuracy issues come "
                 "before name decoration.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    counts = Counter(kind for kind, _, _ in findings)
    for kind in (
        "arg_type", "return_type", "probed_type",
        "element_repr_property", "element_repr_class",
        "arg_name",
    ):
        if counts[kind]:
            lines.append(f"- **{kind}** — {counts[kind]} item(s)")
    lines.append(f"- **total** — {len(findings)}")
    lines.append("")

    if top_classes > 0:
        # Group findings by their containing class (everything before the last `.`).
        class_counts: Counter[str] = Counter()
        for _, path, _ in findings:
            container = path.rsplit(".", 1)[0]
            class_counts[container] += 1
        if class_counts:
            lines.append(f"## Top {top_classes} most-affected paths")
            lines.append("")
            for container, n in class_counts.most_common(top_classes):
                lines.append(f"- `{container}` — {n} item(s)")
            lines.append("")

    section_titles = {
        "arg_type": "Function args still typed `object` / `tuple` / `list`",
        "return_type": "Function returns still typed `object` / `tuple` / `list`",
        "probed_type": "Properties with null or `NoneType` probed_type",
        "element_repr_property": "Iterable properties missing `element_repr`",
        "element_repr_class": "Iterable classes missing `element_repr`",
        "arg_name": "Function args still named `argN`",
    }

    for kind in (
        "arg_type", "return_type", "probed_type",
        "element_repr_property", "element_repr_class",
        "arg_name",
    ):
        items = by_kind.get(kind) or []
        if not items:
            continue
        lines.append(f"## {section_titles[kind]}")
        lines.append("")
        for path, detail in items:
            lines.append(f"- `{path}` — {detail}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Find unrefined items in LiveTree.refined.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to LiveTree.refined.json (default: stubs/<version>/pipeline/...)")
    parser.add_argument("--output", help="Write report to this path instead of stdout")
    parser.add_argument("--kind", choices=[
        "arg_type", "return_type", "probed_type",
        "element_repr_property", "element_repr_class",
        "arg_name",
    ], help="Limit report to one category")
    parser.add_argument("--top-classes", type=int, default=10,
                        help="Show top-N most-affected paths (default: 10; pass 0 to suppress)")
    args = parser.parse_args()

    input_path = Path(args.input) if args.input else (
        REPO_ROOT / "stubs" / args.version / "pipeline" / "LiveTree.refined.json"
    )
    if not input_path.exists():
        print(f"error: refined tree not found at {input_path}", file=sys.stderr)
        return 2

    data = json.loads(input_path.read_text())
    iterable_classes = _collect_iterable_classes(data["tree"])
    findings: list[Finding] = []
    _walk(data["tree"], "", iterable_classes, findings)

    if args.kind:
        findings = [f for f in findings if f[0] == args.kind]

    report = _format_report(findings, args.top_classes)

    if args.output:
        Path(args.output).write_text(report)
        print(f"Wrote {len(findings)} findings to {args.output}", file=sys.stderr)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())

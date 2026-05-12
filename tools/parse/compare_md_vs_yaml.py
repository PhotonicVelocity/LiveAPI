#!/usr/bin/env python3
"""Compare parser+adapter output (markdown path) against the YAML
loader output for the same module. Used to validate that the dual-
format loader produces equivalent dicts going into the existing
generators.

Usage:
    compare_md_vs_yaml.py <ModuleName>

Loads:
    stubs/12.3.6/modules/<ModuleName>.md  via parse_module_md + to_legacy_shape
    stubs/12.3.6/lom/<ModuleName>.yaml    via yaml.safe_load

Prints a brief OK / per-path diff to stdout. Exit 0 if equivalent;
non-zero if any divergence.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

# Re-use the parser + adapter from the sibling module.
sys.path.insert(0, str(Path(__file__).parent))
from parse_module_md import parse_module_md, to_legacy_shape  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
VERSION = "12.3.6"


def _norm_str(s: str) -> str:
    """Whitespace-normalize a string for comparison. Collapses any run
    of whitespace (including newlines) to a single space. Strips
    leading/trailing whitespace."""
    return " ".join(s.split())


def _norm_source_field(v: Any) -> list[str]:
    """Normalize a `source:` field to a list of whitespace-normalized
    strings. The YAML loader may emit a single string for a one-item
    source while the adapter always emits a list — compare as lists."""
    if isinstance(v, str):
        return [_norm_str(v)]
    if isinstance(v, list):
        return [_norm_str(x) if isinstance(x, str) else x for x in v]
    return v


def _diff(a: Any, b: Any, path: str = "") -> list[str]:
    """Recursively diff two values. Returns a list of human-readable
    divergence strings. Normalizes cosmetic differences:
    whitespace-in-strings, source-str-vs-single-element-list, and
    missing-key-vs-empty-list."""
    # Normalize `source:` fields — either side may be a str (one item)
    # or a list (multiple items). Compare as normalized lists.
    if path.endswith(".source") and (isinstance(a, (str, list)) or isinstance(b, (str, list))):
        na = _norm_source_field(a)
        nb = _norm_source_field(b)
        if na == nb:
            return []
        if len(na) != len(nb):
            return [f"{path}: list length differs — md→legacy has {len(na)}, yaml has {len(nb)}"]
        out: list[str] = []
        for i, (av, bv) in enumerate(zip(na, nb)):
            if av != bv:
                out.append(f"{path}[{i}]: {av!r} != {bv!r}")
        return out
    # Whitespace-normalize plain strings.
    if isinstance(a, str) and isinstance(b, str):
        if _norm_str(a) == _norm_str(b):
            return []
        return [f"{path}: {a!r} != {b!r}"]
    if type(a) is not type(b):
        if a == b:
            return []
        return [f"{path}: type mismatch — {type(a).__name__} {a!r} != {type(b).__name__} {b!r}"]
    if isinstance(a, dict):
        out: list[str] = []
        a_keys = set(a.keys())
        b_keys = set(b.keys())
        only_a = a_keys - b_keys
        only_b = b_keys - a_keys
        # Empty list / empty dict / None on one side equals missing key
        # on the other — these are equivalent shapes downstream.
        only_a_real = {k for k in only_a if a.get(k) not in ([], {}, None, False)}
        only_b_real = {k for k in only_b if b.get(k) not in ([], {}, None, False)}
        if only_a_real:
            out.append(f"{path}: keys only in md→legacy: {sorted(only_a_real)}")
        if only_b_real:
            out.append(f"{path}: keys only in yaml: {sorted(only_b_real)}")
        for k in a_keys & b_keys:
            out.extend(_diff(a[k], b[k], f"{path}.{k}"))
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [f"{path}: list length differs — md→legacy has {len(a)}, yaml has {len(b)}"]
        out = []
        for i, (av, bv) in enumerate(zip(a, b)):
            out.extend(_diff(av, bv, f"{path}[{i}]"))
        return out
    if a == b:
        return []
    return [f"{path}: {a!r} != {b!r}"]


def compare(module: str) -> int:
    md_path = REPO_ROOT / "stubs" / VERSION / "modules" / f"{module}.md"
    yaml_path = REPO_ROOT / "stubs" / VERSION / "lom" / f"{module}.yaml"
    if not md_path.exists():
        print(f"missing: {md_path}", file=sys.stderr)
        return 2
    if not yaml_path.exists():
        print(f"missing: {yaml_path}", file=sys.stderr)
        return 2

    parsed = parse_module_md(md_path)
    md_legacy = to_legacy_shape(parsed)
    yaml_doc = yaml.safe_load(yaml_path.read_text())

    diffs = _diff(md_legacy, yaml_doc, f"<{module}>")
    if not diffs:
        print(f"OK: {module} md→legacy == yaml")
        return 0
    print(f"DIVERGES: {module} — {len(diffs)} differences")
    for d in diffs[:40]:
        print(f"  {d}")
    if len(diffs) > 40:
        print(f"  ... ({len(diffs) - 40} more)")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: compare_md_vs_yaml.py <ModuleName>", file=sys.stderr)
        return 2
    return compare(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())

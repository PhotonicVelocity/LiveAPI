#!/usr/bin/env python3
"""Port tools/parse/manual_refinements.yaml entries onto stubs/<v>/lom/<Module>.yaml.

The legacy refinements file is dotted-path-keyed, applied at the parsed-JSON
layer. The new lom YAML SOT carries each override as a sibling
`<field>_override:` block (per doc/lom-format.md), so the parser-derived
value and the human override sit side-by-side.

Field mapping:
    args: {old: new}      -> arg.name_override = {value: new, source}        (no confidence)
    arg_types: {x: T}     -> arg.type_override = {value: T, confidence, source}
    return_type: T        -> method.returns.type_override = {value: T, ...}
    probed_type: T        -> property.type_override = {value: T, ...}
    element_repr: T       -> class.element_type_override / property.element_type_override

Where a refinement value is `{from: X, to: Y}`, `from:` is validated
against the current lom value (warns on mismatch — that's our drift signal).
The override block records `value: Y`. Metadata fields (source, confidence,
_note) are carried onto the override; the legacy file remains in git
history as the rationale archive.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools" / "parse"))
from build_lom_yaml import emit_yaml  # noqa: E402


def _spec_value(spec: Any) -> Any:
    if isinstance(spec, dict) and "to" in spec:
        return spec["to"]
    return spec


def _spec_from(spec: Any) -> Any:
    if isinstance(spec, dict) and "from" in spec:
        return spec["from"]
    return None


def _insert_after(d: dict, after_key: str, new_key: str, new_value: Any) -> None:
    """Insert (new_key, new_value) into d immediately after after_key, preserving
    dict order. If new_key already exists, just overwrite (keeps existing slot).
    If after_key is absent, append at end.
    """
    if new_key in d:
        d[new_key] = new_value
        return
    if after_key not in d:
        d[new_key] = new_value
        return
    items = list(d.items())
    d.clear()
    for k, v in items:
        d[k] = v
        if k == after_key:
            d[new_key] = new_value


def _build_override(value: Any, confidence: str | None, source: str, *, with_confidence: bool = True) -> dict:
    out: dict[str, Any] = {"value": value}
    if with_confidence and confidence:
        out["confidence"] = confidence
    out["source"] = source
    return out


def _find_in_module(module_yaml: dict, segments: list[str]) -> tuple[dict, str] | None:
    """Walk segments to locate the target node. Returns (node, kind) or None."""
    current = module_yaml
    for i, seg in enumerate(segments):
        is_last = i == len(segments) - 1
        found, kind = None, None
        for cls in current.get("primary_class") or []:
            if cls.get("name") == seg:
                found, kind = cls, "class"
                break
        if not found:
            for cls in current.get("classes") or []:
                if cls.get("name") == seg:
                    found, kind = cls, "class"
                    break
        if not found:
            for prop in current.get("properties") or []:
                if prop.get("name") == seg:
                    found, kind = prop, "property"
                    break
        if not found:
            for m in current.get("methods") or []:
                if m.get("name") == seg:
                    found, kind = m, "method"
                    break
        if not found:
            for f in current.get("functions") or []:
                if f.get("name") == seg:
                    found, kind = f, "function"
                    break
        if not found:
            for e in current.get("enums") or []:
                if e.get("name") == seg:
                    found, kind = e, "enum"
                    break
        if not found:
            for c in current.get("constants") or []:
                if c.get("name") == seg:
                    found, kind = c, "constant"
                    break
        if not found:
            return None
        if is_last:
            return found, kind
        if kind != "class":
            return None
        current = found
    return None


def _find_arg(args: list[dict], name: str) -> dict | None:
    """Find arg by current name OR by name_override.value (post-rename)."""
    for a in args:
        if a.get("name") == name:
            return a
    for a in args:
        ov = a.get("name_override")
        if isinstance(ov, dict) and ov.get("value") == name:
            return a
    return None


def _apply_args_rename(target: dict, args_map: dict, source: str, warns: list[str]) -> None:
    args = target.get("args") or []
    for old_name, new_name in args_map.items():
        arg = _find_arg(args, old_name)
        if not arg:
            warns.append(f"args rename: arg '{old_name}' not found")
            continue
        # No confidence for name renames (per spec / user direction).
        _insert_after(arg, "name", "name_override", _build_override(new_name, None, source, with_confidence=False))


def _apply_arg_types(target: dict, types_map: dict, confidence: str | None, source: str, warns: list[str]) -> None:
    args = target.get("args") or []
    for arg_name, spec in types_map.items():
        arg = _find_arg(args, arg_name)
        if not arg:
            warns.append(f"arg_types: arg '{arg_name}' not found")
            continue
        from_val = _spec_from(spec)
        new_val = _spec_value(spec)
        if from_val is not None and arg.get("type") != from_val:
            warns.append(f"arg_types: '{arg_name}' from-mismatch: expected {from_val!r}, got {arg.get('type')!r}")
        _insert_after(arg, "type", "type_override", _build_override(new_val, confidence, source))


def _apply_return_type(target: dict, spec: Any, confidence: str | None, source: str, warns: list[str]) -> None:
    if "returns" not in target:
        target["returns"] = {}
    returns = target["returns"]
    from_val = _spec_from(spec)
    new_val = _spec_value(spec)
    if from_val is not None and returns.get("type") != from_val:
        warns.append(f"return_type: from-mismatch: expected {from_val!r}, got {returns.get('type')!r}")
    _insert_after(returns, "type", "type_override", _build_override(new_val, confidence, source))


def _apply_probed_type(target: dict, spec: Any, confidence: str | None, source: str, warns: list[str]) -> None:
    from_val = _spec_from(spec)
    new_val = _spec_value(spec)
    if from_val is not None and target.get("type") != from_val:
        warns.append(f"probed_type: from-mismatch: expected {from_val!r}, got {target.get('type')!r}")
    _insert_after(target, "type", "type_override", _build_override(new_val, confidence, source))


def _apply_element_repr(target: dict, kind: str, spec: Any, confidence: str | None, source: str, warns: list[str]) -> None:
    from_val = _spec_from(spec)
    new_val = _spec_value(spec)
    if from_val is not None and target.get("element_type") != from_val:
        # Quiet: parser may not have populated element_type for typed Vector subclasses.
        if target.get("element_type") is not None:
            warns.append(f"element_repr: from-mismatch: expected {from_val!r}, got {target.get('element_type')!r}")
    if kind == "class":
        anchor = "element_type" if "element_type" in target else "iterable"
        _insert_after(target, anchor, "element_type_override", _build_override(new_val, confidence, source))
    elif kind in ("property", "method", "function"):
        # No native element_type field on property — stash override block; consumer
        # will use it to upgrade the property's iterable element type.
        _insert_after(target, "type", "element_type_override", _build_override(new_val, confidence, source))
    else:
        warns.append(f"element_repr on unsupported kind {kind}")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("version", help="Live version (e.g. 12.3.6)")
    p.add_argument("--refinements", default="tools/parse/manual_refinements.yaml")
    p.add_argument("--lom-dir", help="lom output dir (default: stubs/<v>/lom)")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    refs_path = REPO_ROOT / args.refinements
    lom_dir = Path(args.lom_dir) if args.lom_dir else REPO_ROOT / "stubs" / args.version / "lom"

    refs = yaml.safe_load(refs_path.read_text())
    cache: dict[str, dict] = {}
    changed: set[str] = set()
    warnings: list[str] = []
    applied = 0
    not_found = 0

    for path, entry in refs.items():
        if path.startswith("_") or not isinstance(entry, dict):
            continue
        if not path.startswith("Live."):
            warnings.append(f"{path}: not Live.* prefixed, skipped")
            continue
        segs = path[len("Live."):].split(".")
        module_name, target_segs = segs[0], segs[1:]
        if not target_segs:
            warnings.append(f"{path}: no target segments")
            continue

        if module_name not in cache:
            module_path = lom_dir / f"{module_name}.yaml"
            if not module_path.exists():
                warnings.append(f"{path}: module {module_name}.yaml not found")
                not_found += 1
                continue
            cache[module_name] = yaml.safe_load(module_path.read_text())

        result = _find_in_module(cache[module_name], target_segs)
        if result is None:
            warnings.append(f"{path}: target not found")
            not_found += 1
            continue
        target, kind = result

        confidence = entry.get("confidence")
        source = entry.get("source", "<no source>")
        per_entry: list[str] = []

        if isinstance(entry.get("args"), dict):
            _apply_args_rename(target, entry["args"], source, per_entry)
        if isinstance(entry.get("arg_types"), dict):
            _apply_arg_types(target, entry["arg_types"], confidence, source, per_entry)
        if "return_type" in entry:
            _apply_return_type(target, entry["return_type"], confidence, source, per_entry)
        if "probed_type" in entry:
            _apply_probed_type(target, entry["probed_type"], confidence, source, per_entry)
        if "element_repr" in entry:
            _apply_element_repr(target, kind, entry["element_repr"], confidence, source, per_entry)

        for w in per_entry:
            warnings.append(f"{path}: {w}")
        applied += 1
        changed.add(module_name)

    for w in warnings:
        print(f"WARN  {w}")
    print(f"\n{'Would apply' if args.dry_run else 'Applied'} {applied} entries across {len(changed)} modules; "
          f"{not_found} paths not found; {len(warnings)} warnings")

    if not args.dry_run:
        for mod in changed:
            emit_yaml(cache[mod], lom_dir / f"{mod}.yaml")

    return 0


if __name__ == "__main__":
    sys.exit(main())

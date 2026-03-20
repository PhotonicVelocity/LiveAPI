"""Stamp behavioral probe data onto LiveTree.resolved.json.

Reads ProbeResults.json and stamps behavioral_async, behavioral_undo,
behavioral_notes, behavioral_effect, and behavioral_side_effects onto
matching property and method nodes in the resolved tree.

Runs independently of the parse pipeline — operates on the final
LiveTree.resolved.json after all refinement steps are complete.

Usage:
    python tools/parse/stamp_behavioral.py 12.3.6
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


STUBS_DIR = Path(__file__).resolve().parent.parent.parent / "stubs"


def resolve_pipeline_dir(version: str) -> Path:
    """Resolve a version string to a pipeline directory."""
    ver_dir = STUBS_DIR / version
    if ver_dir.is_dir():
        return ver_dir / "pipeline"
    fallback = STUBS_DIR / f"{version}.0"
    if fallback.is_dir():
        return fallback / "pipeline"
    available = sorted(p.name for p in STUBS_DIR.iterdir() if p.is_dir()) if STUBS_DIR.is_dir() else []
    msg = f"No stubs directory found for version '{version}'"
    if available:
        msg += f"\nAvailable: {', '.join(available)}"
    raise SystemExit(msg)


def _find_class_node(tree_root: dict, probe_name: str) -> dict | None:
    """Find a class node matching a probe class name like 'Song' or 'Song.View'."""
    parts = probe_name.split(".")
    root = tree_root.get("tree", tree_root) if isinstance(tree_root, dict) else tree_root
    for module in root.get("children", []):
        if not isinstance(module, dict) or module.get("type") != "module":
            continue
        for child in module.get("children", []):
            if isinstance(child, dict) and child.get("type") == "class" and child.get("name") == parts[0]:
                node = child
                for inner in parts[1:]:
                    found = None
                    for c in node.get("children", []):
                        if isinstance(c, dict) and c.get("type") == "class" and c.get("name") == inner:
                            found = c
                            break
                    if found is None:
                        return None
                    node = found
                return node
    return None


def _simplify_side_effects(raw_effects: list[dict]) -> list[dict[str, str]]:
    """Reduce side effects to unique (class, prop) pairs."""
    seen: set[tuple[str, str]] = set()
    result = []
    for effect in raw_effects:
        key = (effect.get("label", ""), effect.get("prop", ""))
        if key not in seen:
            seen.add(key)
            result.append({"class": key[0], "prop": key[1]})
    return result


def stamp(tree_data: dict, behavioral_data: dict) -> tuple[int, int]:
    """Stamp behavioral data onto tree nodes. Returns (properties_stamped, methods_stamped)."""
    classes = behavioral_data.get("classes", {})
    stamped_props = 0
    stamped_methods = 0

    for probe_cls_name, cls_entry in classes.items():
        class_node = _find_class_node(tree_data, probe_cls_name)
        if class_node is None:
            continue

        children = class_node.get("children", [])

        # Stamp properties
        for prop_name, prop_data in cls_entry.get("properties", {}).items():
            for child in children:
                if child.get("name") == prop_name and child.get("type") in ("property", "getset_descriptor"):
                    child["behavioral_async"] = prop_data.get("async_visibility")
                    child["behavioral_undo"] = prop_data.get("undo_tracked")
                    notes = prop_data.get("notes")
                    if notes:
                        child["behavioral_notes"] = notes
                    side_effects = prop_data.get("side_effects")
                    if side_effects:
                        child["behavioral_side_effects"] = _simplify_side_effects(side_effects)
                    stamped_props += 1
                    break

        # Stamp methods
        for method_name, method_data in cls_entry.get("methods", {}).items():
            for child in children:
                if child.get("name") == method_name and child.get("type") in (
                    "function", "builtin_function_or_method", "method_descriptor",
                ):
                    effect = method_data.get("effect")
                    if effect:
                        child["behavioral_effect"] = {
                            "label": effect.get("label"),
                            "prop": effect.get("prop"),
                        }
                        child["behavioral_async"] = effect.get("async_visibility")
                        child["behavioral_undo"] = effect.get("undo_tracked")
                    else:
                        child["behavioral_async"] = method_data.get("async_visibility")
                        child["behavioral_undo"] = method_data.get("undo_tracked")
                    notes = method_data.get("notes")
                    if notes:
                        child["behavioral_notes"] = notes
                    side_effects = method_data.get("side_effects")
                    if side_effects:
                        child["behavioral_side_effects"] = _simplify_side_effects(side_effects)
                    stamped_methods += 1
                    break

    return stamped_props, stamped_methods


def main() -> None:
    parser = argparse.ArgumentParser(description="Stamp behavioral probe data onto LiveTree.resolved.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    args = parser.parse_args()

    pipeline_dir = resolve_pipeline_dir(args.version)
    tree_path = pipeline_dir / "LiveTree.resolved.json"
    behavioral_path = pipeline_dir / "ProbeResults.json"

    if not tree_path.exists():
        raise SystemExit(f"Resolved tree not found: {tree_path}")
    if not behavioral_path.exists():
        raise SystemExit(f"Probe results not found: {behavioral_path}")

    with open(tree_path, "r", encoding="utf-8") as f:
        tree_data = json.load(f)
    with open(behavioral_path, "r", encoding="utf-8") as f:
        behavioral_data = json.load(f)

    props, methods = stamp(tree_data, behavioral_data)

    with open(tree_path, "w", encoding="utf-8") as f:
        json.dump(tree_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Stamped {props} properties, {methods} methods onto {tree_path}")


if __name__ == "__main__":
    main()

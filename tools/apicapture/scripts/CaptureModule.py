"""
CaptureModule — raw snapshot of a Python module's structure via dir().

Recursively walks every attribute reachable from the root module, recording
name, type, repr, docstring, and value for each node. Classes get their
children walked (properties, methods, subclasses); enum-like types (int
subclasses with names/values) are captured without recursion. Classes that
can be constructed with no arguments are marked as constructable.

Output is LiveTree.raw.json — a nested tree with no filtering or interpretation.
PropertyProbe consumes this to build its repr index.
"""

from __future__ import annotations

import inspect
import json
import os
import sys


def capture(module, outdir: str) -> str:
    """Walk module tree and write raw capture JSON. Returns output path."""
    tree = _walk(module, seen=set())

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    path = os.path.join(outdir, f"{module.__name__}Tree.raw.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            {"python_version": sys.version.split(" ")[0], "tree": tree},
            f,
            indent=2,
            ensure_ascii=False,
        )
    return path


def _walk(obj, seen: set[int]) -> dict:
    """Recursively walk obj and everything in dir(obj). Returns a tree node."""
    obj_id = id(obj)
    if obj_id in seen:
        node = {"name": getattr(obj, "__name__", "(unknown)"), "type": type(obj).__name__, "id": obj_id, "ref": True}
        try:
            node["repr"] = repr(obj)
        except Exception:
            pass
        return node
    seen.add(obj_id)

    node: dict = {
        "name": getattr(obj, "__name__", "(unknown)"),
        "type": type(obj).__name__,
        "id": obj_id,
    }

    try:
        node["repr"] = repr(obj)
    except Exception:
        pass

    try:
        node["raw_doc"] = getattr(obj, "__doc__", None)
    except Exception:
        pass

    if isinstance(obj, (int, float, str, bool)):
        node["value"] = obj

    # Recurse into dir() members
    try:
        members = dir(obj)
    except Exception:
        return node

    children: list[dict] = []

    for attr_name in sorted(members):
        if attr_name.startswith("__"):
            continue
        try:
            member = getattr(obj, attr_name)
        except Exception:
            continue

        if inspect.isclass(member) and type(member).__name__ == "type":
            # Enum class (int subclass) — don't recurse, just grab names/values
            child: dict = {
                "name": attr_name,
                "type": "type",
                "id": id(member),
            }
            try:
                child["repr"] = repr(member)
            except Exception:
                pass
            try:
                child["raw_doc"] = getattr(member, "__doc__", None)
            except Exception:
                pass
            try:
                child["names"] = repr(getattr(member, "names", None))
                child["values"] = repr(getattr(member, "values", None))
            except Exception:
                pass
            children.append(child)
        elif inspect.ismodule(member) or inspect.isclass(member) or inspect.isbuiltin(member) or inspect.isfunction(member):
            child = _walk(member, seen)
            if inspect.isclass(member):
                # Pop children so class metadata appears before children in JSON output
                saved_children = child.pop("children", None)
                try:
                    init_doc = getattr(member.__init__, "__doc__", None)
                    if init_doc:
                        child["init_doc"] = init_doc
                except Exception:
                    pass
                try:
                    bases = member.__bases__
                    if bases and bases != (object,):
                        child["bases"] = [repr(b) for b in bases]
                except Exception:
                    pass
                try:
                    member()
                    child["constructable"] = True
                except Exception:
                    pass
                if saved_children is not None:
                    child["children"] = saved_children
            children.append(child)
        elif isinstance(member, property):
            child: dict = {
                "name": attr_name,
                "type": "property",
                "id": id(member),
                "settable": getattr(member, "fset", None) is not None,
            }
            try:
                child["raw_doc"] = getattr(member, "__doc__", None)
            except Exception:
                pass
            children.append(child)
        else:
            child: dict = {
                "name": attr_name,
                "type": type(member).__name__,
                "id": id(member),
            }
            try:
                child["value"] = repr(member)
            except Exception:
                pass
            children.append(child)

    if children:
        node["children"] = children

    return node

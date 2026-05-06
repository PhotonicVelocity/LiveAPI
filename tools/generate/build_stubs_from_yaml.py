#!/usr/bin/env python3
"""Build .pyi stub files from per-module LOM YAML.

Reads stubs/<v>/reports/seed/*.yaml (output of build_lom_yaml.py) and
emits .pyi stubs structurally equivalent to what the old generator
produces from LiveTree.parsed.json. Used to validate the YAML carries
all the data the old pipeline consumed.

Usage:
    python tools/generate/build_stubs_from_yaml.py 12.3.6
    python tools/generate/build_stubs_from_yaml.py 12.3.6 --output stubs/<v>/variants/v2-yaml/Live
"""

from __future__ import annotations

import argparse
import re
import sys
from io import StringIO
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# --- Type rendering ---------------------------------------------------- #

# Matches `Live.<Module>.<Class>[.<Nested>...]` in qualified type strings.
_LIVE_PATH_RE = re.compile(r"\bLive\.[A-Za-z_][\w.]*")


def render_type(qualified: str, current_module: str, imports: set[tuple[str, str]]) -> str:
    """Convert a qualified Live path → bare/dotted form for stub emission.

    `Live.Track.Track` from Song module → "Track" + import from Live.Track.
    `Live.Song.Song.View` from Song module → "View" (same module, bare leaf).
    `Live.Device.Device.View` from RackDevice module → "Device.View" + import.
    Non-Live paths (builtins, composites) pass through unchanged.
    """
    parts = qualified.split(".")
    if len(parts) < 3 or parts[0] != "Live":
        return qualified
    target_module = parts[1]
    top_class = parts[2]
    rest = parts[3:]
    if target_module == current_module:
        # Same module: bare leaf works at every nesting level under
        # `from __future__ import annotations` (lazy resolution).
        return parts[-1]
    imports.add((f"Live.{target_module}", top_class))
    return ".".join([top_class, *rest]) if rest else top_class


def render_type_string(type_str: str | None, current_module: str, imports: set[tuple[str, str]]) -> str:
    """Replace each Live.X.Y[.Z...] token in a composite type string with
    its rendered form, accumulating imports."""
    if not type_str:
        return "Any"
    return _LIVE_PATH_RE.sub(lambda m: render_type(m.group(0), current_module, imports), type_str)


# --- Stub formatting --------------------------------------------------- #

INDENT = "    "


def _indent(lines: list[str], level: int) -> list[str]:
    return [INDENT * level + line if line else line for line in lines]


def _wrap_docstring(text: str) -> list[str]:
    """Format a docstring in the convention used by the old generator —
    triple-quoted, on its own line(s) when multi-line, inline otherwise."""
    text = text.strip()
    if not text:
        return []
    if "\n" not in text:
        return [f'"""{text}"""']
    return ['"""', *text.split("\n"), '"""']


def _ret_type_for_type(type_str: str | None, element_type: str | None,
                      current_module: str, imports: set[tuple[str, str]],
                      registry: dict[str, Any]) -> str:
    """Resolve a property/return type string for stub emission.

    For generic-Vector references that carry a per-use `element_type`,
    render as `Vector[E]`. For everything else, just render the type
    string straight through.
    """
    if type_str is None:
        return "Any"
    base = render_type_string(type_str, current_module, imports)
    if element_type and type_str in registry.get("generic_containers", set()):
        elem = render_type_string(element_type, current_module, imports)
        return f"{base}[{elem}]"
    return base


def _format_arg(arg: dict[str, Any], current_module: str, imports: set[tuple[str, str]]) -> str:
    name = arg["name"]
    type_str = render_type_string(arg.get("type") or "Any", current_module, imports)
    if arg.get("optional"):
        default = arg.get("default") or "None"
        # Optional widening: when the default is the bare `None` literal
        # and the type doesn't already admit None, widen to `T | None` so
        # the annotation reflects what the binding actually accepts.
        # Matches v1 generator behavior.
        if default == "None" and type_str != "None" and "None" not in type_str.split():
            type_str = f"{type_str} | None"
        return f"{name}: {type_str} = {default}"
    return f"{name}: {type_str}"


def _format_method_args(args: list[dict[str, Any]], current_module: str,
                        imports: set[tuple[str, str]], is_method: bool) -> str:
    """Produce the parenthesized arg list including PEP 570 `, /`.

    Live's binding accepts only positional args, so every callable ends
    with `, /` after its last positional. For methods, `self` is the
    first arg and is rendered as `self` (no type annotation, matching
    Python convention)."""
    formatted: list[str] = []
    rest = list(args)
    if is_method and rest and rest[0].get("name") == "self":
        formatted.append("self")
        rest = rest[1:]
    for arg in rest:
        formatted.append(_format_arg(arg, current_module, imports))
    if formatted and (len(formatted) > 1 or not is_method or formatted[0] != "self"):
        formatted.append("/")
    return ", ".join(formatted)


_LISTENER_ADD_DOC = (
    'Add a listener function or method, which will be called as soon as the\n'
    'property "{prop}" has changed.'
)
_LISTENER_REMOVE_DOC = (
    'Remove a previously set listener function or method from\n'
    'property "{prop}".'
)
_LISTENER_HAS_DOC = (
    'Returns true, if the given listener function or method is connected\n'
    'to the property "{prop}".'
)


def _build_listener_method(method_name: str, prop_name: str) -> list[str]:
    """Re-expand one folded listener method into a full def block."""
    if method_name.startswith("add_"):
        doc = _LISTENER_ADD_DOC.format(prop=prop_name)
        ret = "None"
    elif method_name.startswith("remove_"):
        doc = _LISTENER_REMOVE_DOC.format(prop=prop_name)
        ret = "None"
    else:
        doc = _LISTENER_HAS_DOC.format(prop=prop_name)
        ret = "bool"
    out = [f"def {method_name}(self, callback: Callable[[], None], /) -> {ret}:"]
    for line in _indent(_wrap_docstring(doc), 1):
        out.append(line)
    out.append(INDENT + "...")
    return out


def _build_property_block(prop: dict[str, Any], current_module: str,
                           imports: set[tuple[str, str]],
                           registry: dict[str, Any]) -> list[str]:
    """Just the @property + setter (NO listeners — those are emitted as
    separate sortable members so they alphabetize with regular methods).
    A blank line separates the @property body from the @setter so each
    `def` reads as its own block (matching v1's spacing)."""
    name = prop["name"]
    type_str = prop.get("type")
    if type_str is None:
        # Listener-only signal — no @property body, only listeners.
        return []
    rendered = _ret_type_for_type(type_str, prop.get("element_type"),
                                  current_module, imports, registry)
    out = ["@property", f"def {name}(self) -> {rendered}:"]
    raw_doc = prop.get("raw_doc")
    if raw_doc:
        for line in _indent(_wrap_docstring(raw_doc), 1):
            out.append(line)
    out.append(INDENT + "...")
    if prop.get("settable"):
        out.append("")
        out.append(f"@{name}.setter")
        out.append(f"def {name}(self, value: {rendered}) -> None: ...")
    return out


def _build_init_block(cls: dict[str, Any]) -> list[str] | None:
    """For constructable classes, synthesize a `def __init__` line. The
    parser doesn't emit __init__ as a regular method node; we infer it
    from the `constructable: true` flag and (where present) the
    `init_doc:` field. Most cases collapse to `def __init__(self) -> None: ...`."""
    if not cls.get("constructable"):
        return None
    return [f"def __init__(self) -> None: ..."]


def _build_method_block(method: dict[str, Any], current_module: str,
                         imports: set[tuple[str, str]], registry: dict[str, Any],
                         is_method: bool) -> list[str]:
    """Class method or module-level function block."""
    name = method["name"]
    args = method.get("args") or []
    returns = method.get("returns") or {}
    ret_type = _ret_type_for_type(returns.get("type"), returns.get("element_type"),
                                  current_module, imports, registry)
    arg_str = _format_method_args(args, current_module, imports, is_method)
    out = [f"def {name}({arg_str}) -> {ret_type}:"]
    raw_doc = method.get("raw_doc")
    if raw_doc:
        for line in _indent(_wrap_docstring(raw_doc), 1):
            out.append(line)
    out.append(INDENT + "...")
    return out


def _build_enum_block(enum: dict[str, Any]) -> list[str]:
    out = [f"class {enum['name']}(int):"]
    raw_doc = enum.get("raw_doc")
    if raw_doc:
        for line in _indent(_wrap_docstring(raw_doc), 1):
            out.append(line)
    members = enum.get("members") or {}
    if not members:
        if not raw_doc:
            out.append(INDENT + "...")
    else:
        # Emit by ascending value (matches v1 generator). The parser's
        # dict order can be source-declaration order which doesn't always
        # align with value order.
        for n, v in sorted(members.items(), key=lambda kv: kv[1]):
            out.append(f"{INDENT}{n}: int = {v}")
    return out


def _build_constant_block(const: dict[str, Any]) -> list[str]:
    return [f"{const['name']}: {const.get('type', 'str')} = {const['value']!r}"]


def _collect_class_members(cls: dict[str, Any], current_module: str,
                            imports: set[tuple[str, str]],
                            registry: dict[str, Any]) -> list[tuple[str, list[str]]]:
    """Collect all member blocks at this class as (sort_key, lines) tuples.

    Listener triplets are emitted as separate methods so they alphabetize
    inline with regular methods (matching v1's ordering). For
    constructable classes, a `def __init__` is synthesized at the
    standard `__init__` sort key (the YAML doesn't carry __init__ as a
    real method node — we infer it from the `constructable` flag).
    """
    entries: list[tuple[str, list[str]]] = []
    init_block = _build_init_block(cls)
    if init_block is not None:
        entries.append(("__init__", init_block))
    for nested in cls.get("classes") or []:
        entries.append((nested["name"], _build_class_block(nested, current_module, imports, registry)))
    for nested in cls.get("enums") or []:
        entries.append((nested["name"], _build_enum_block(nested)))
    for prop in cls.get("properties") or []:
        block = _build_property_block(prop, current_module, imports, registry)
        if block:
            entries.append((prop["name"], block))
        for listener in prop.get("listenable") or []:
            entries.append((listener, _build_listener_method(listener, prop["name"])))
    for m in cls.get("methods") or []:
        entries.append((m["name"], _build_method_block(m, current_module, imports, registry, True)))
    for c in cls.get("constants") or []:
        entries.append((c["name"], _build_constant_block(c)))
    return entries


def _build_class_block(cls: dict[str, Any], current_module: str,
                       imports: set[tuple[str, str]],
                       registry: dict[str, Any]) -> list[str]:
    """Class definition with members alphabetized at each level."""
    name = cls["name"]
    ancestors = cls.get("ancestors") or []
    base_str = ""
    if ancestors:
        bases = [render_type(a, current_module, imports) for a in ancestors[:1]]
        base_str = f"({', '.join(bases)})"
    out = [f"class {name}{base_str}:"]
    raw_doc = cls.get("raw_doc")
    if raw_doc:
        for line in _indent(_wrap_docstring(raw_doc), 1):
            out.append(line)
        out.append("")

    members = _collect_class_members(cls, current_module, imports, registry)
    if not members:
        out.append(INDENT + "...")
        return out

    # Sort alphabetically by name. Each block emits as a unit, separated
    # by blank lines.
    members.sort(key=lambda kv: kv[0])
    for i, (_, block) in enumerate(members):
        for line in _indent(block, 1):
            out.append(line)
        if i < len(members) - 1:
            out.append("")
    return out


# --- Module emission --------------------------------------------------- #


def emit_module(module: dict[str, Any], registry: dict[str, Any]) -> str:
    """Generate a full .pyi for one module.

    Order matches v1: primary class first (regardless of name), then all
    other classes + enums sorted alphabetically together, then functions
    sorted alphabetically, then constants.
    """
    module_name = module["module"]
    imports: set[tuple[str, str]] = set()

    # Class-like entries (classes + enums) intermix alphabetically except
    # the primary class which leads regardless.
    class_entries: list[tuple[str, list[str]]] = []
    for cls in module.get("classes") or []:
        class_entries.append((cls["name"], _build_class_block(cls, module_name, imports, registry)))
    for enum in module.get("enums") or []:
        class_entries.append((enum["name"], _build_enum_block(enum)))
    class_entries.sort(key=lambda kv: kv[0])

    fn_entries: list[tuple[str, list[str]]] = []
    for fn in module.get("functions") or []:
        fn_entries.append((fn["name"], _build_method_block(fn, module_name, imports, registry, False)))
    fn_entries.sort(key=lambda kv: kv[0])

    const_entries: list[tuple[str, list[str]]] = []
    for c in module.get("constants") or []:
        const_entries.append((c["name"], _build_constant_block(c)))
    const_entries.sort(key=lambda kv: kv[0])

    body: list[str] = []

    # Primary class first
    for cls in module.get("primary_class") or []:
        body.extend(_build_class_block(cls, module_name, imports, registry))
        body.append("")
    # Then class-like, function, constant groups
    for _, block in class_entries:
        body.extend(block)
        body.append("")
    for _, block in fn_entries:
        body.extend(block)
        body.append("")
    for _, block in const_entries:
        body.extend(block)
        body.append("")

    # __all__ follows the same ordering as the emitted bodies: primary
    # class first, then class-likes alphabetically, then functions
    # alphabetically, then constants alphabetically.
    names: list[str] = []
    for cls in module.get("primary_class") or []:
        names.append(cls["name"])
    names.extend(name for name, _ in class_entries)
    names.extend(name for name, _ in fn_entries)
    names.extend(name for name, _ in const_entries)

    # Header
    buf = StringIO()
    buf.write("from __future__ import annotations\n")
    buf.write("from typing import TYPE_CHECKING, Any, Callable, Iterable\n\n")
    if imports:
        buf.write("if TYPE_CHECKING:\n")
        # Group imports by module, sort
        by_module: dict[str, set[str]] = {}
        for mod, cls_name in imports:
            by_module.setdefault(mod, set()).add(cls_name)
        for mod in sorted(by_module):
            classes = sorted(by_module[mod])
            buf.write(f"    from {mod} import {', '.join(classes)}\n")
        # Three blank lines between the TYPE_CHECKING block and the
        # first class — matches v1 (PEP 8-style "two blank lines around
        # top-level defs," with one extra to follow the conditional).
        buf.write("\n\n\n")
    else:
        buf.write("\n\n")

    buf.write("\n".join(body))
    if not body or body[-1] != "":
        buf.write("\n")

    if names:
        buf.write(f"__all__ = {names!r}\n")

    return buf.getvalue()


# --- Pre-computation: which qualified types are generic containers? ----- #


def build_generic_containers_set(seed_dir: Path) -> set[str]:
    """Identify qualified class paths that are iterable but lack a class-
    level singular `element_type` — i.e., the "generic" containers (Vector,
    ObjectVector). For these, per-use sites carry the element_type and the
    stub generator should render uses as `<Class>[<element>]`."""
    out: set[str] = set()
    for path in sorted(seed_dir.glob("*.yaml")):
        d = yaml.safe_load(path.read_text())

        def walk(cls: dict[str, Any]) -> None:
            if cls.get("iterable") and not cls.get("element_type"):
                p = cls.get("path")
                if p:
                    out.add(p)
            for n in cls.get("classes") or []:
                walk(n)

        for cls in (d.get("primary_class") or []) + (d.get("classes") or []):
            walk(cls)
    return out


# --- CLI --------------------------------------------------------------- #


def main() -> int:
    p = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    p.add_argument("version", help="Live version (e.g. 12.3.6)")
    p.add_argument("--input", help="seed yaml dir")
    p.add_argument("--output", help="output dir for .pyi files")
    args = p.parse_args()

    seed_dir = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "stubs" / args.version / "reports" / "seed"
    )
    out_dir = (
        Path(args.output)
        if args.output
        else REPO_ROOT / "stubs" / args.version / "variants" / "v2-no-refinements" / "Live"
    )

    if not seed_dir.exists():
        print(f"error: seed yaml dir not found at {seed_dir}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)

    registry = {"generic_containers": build_generic_containers_set(seed_dir)}

    written = 0
    all_module_names: list[str] = []
    for path in sorted(seed_dir.glob("*.yaml")):
        module = yaml.safe_load(path.read_text())
        text = emit_module(module, registry)
        out_path = out_dir / f"{module['module']}.pyi"
        out_path.write_text(text)
        all_module_names.append(module["module"])
        written += 1

    # __init__.pyi — re-export every module. Format matches v1: plain
    # `from . import X` (no `as X` alias, no future-import).
    init_buf = StringIO()
    for name in sorted(all_module_names):
        init_buf.write(f"from . import {name}\n")
    init_buf.write(f"\n__all__ = {sorted(all_module_names)!r}\n")
    (out_dir / "__init__.pyi").write_text(init_buf.getvalue())

    print(f"Wrote {written} .pyi files to {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

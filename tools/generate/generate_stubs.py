#!/usr/bin/env python3
"""Build .pyi stub files from per-module LOM YAML.

Reads stubs/<v>/lom/*.yaml (the curated SOT) and emits .pyi stubs.
Wherever the YAML carries a sibling `<field>_override:` block, the
override's `value:` is preferred over the parser-derived field — that's
the seam through which manual refinements reach the rendered stubs.

Usage:
    python tools/generate/generate_stubs.py 12.3.6
    python tools/generate/generate_stubs.py 12.3.6 --input <dir> --output <dir>
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

# --- Override-aware field access --------------------------------------- #


def _resolve(node: dict[str, Any], key: str) -> Any:
    """Read `key` from `node`, preferring `<key>_override.value` when present.

    Mirrors the override pattern in doc/lom-format.md: parser-derived
    field and human override sit side-by-side; consumer picks override.
    """
    override = node.get(f"{key}_override")
    if isinstance(override, dict) and "value" in override:
        return override["value"]
    return node.get(key)


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


def _ret_type_for_type(type_str: str | None,
                       current_module: str,
                       imports: set[tuple[str, str]]) -> str:
    """Resolve a property/return type for stub emission.

    The YAML now carries fully-resolved canonical type strings
    (`list[float]`, `Live.Base.Vector[Live.Track.Track]`, `int | None`,
    etc.) — the stub generator just unqualifies the Live class names
    and accumulates imports.
    """
    if type_str is None:
        return "Any"
    return render_type_string(type_str, current_module, imports)


def _format_arg(arg: dict[str, Any], current_module: str, imports: set[tuple[str, str]],
                enclosing_class: str | None = None) -> str:
    name = _resolve(arg, "name")
    # The YAML's `type:` already carries optional widening (`T | None`
    # when default is None) — we just unqualify Live class names here.
    type_str = render_type_string(_resolve(arg, "type") or "Any", current_module, imports)
    if arg.get("optional"):
        default = arg.get("default") or "None"
        # Boost.Python's signature qualifies module-level enums under the
        # enclosing class (e.g. `Application.MessageButtons.OK_BUTTON`).
        # In our stubs MessageButtons is at module scope, so strip the
        # enclosing-class prefix to get `MessageButtons.OK_BUTTON` — the
        # form that actually resolves under pyright.
        if enclosing_class and default.startswith(f"{enclosing_class}."):
            default = default[len(enclosing_class) + 1:]
        return f"{name}: {type_str} = {default}"
    return f"{name}: {type_str}"


def _format_method_args(args: list[dict[str, Any]], current_module: str,
                        imports: set[tuple[str, str]], is_method: bool,
                        method_name: str = "", enclosing_class: str | None = None) -> str:
    """Produce the parenthesized arg list including PEP 570 `, /`.

    Live's binding accepts only positional args, so every callable ends
    with `, /` after its last positional. For methods, `self` is the
    first arg and is rendered as `self` (no type annotation, matching
    Python convention). `__init__` skips the `, /` marker — v1 emits
    `def __init__(self, ...) -> None: ...` without the positional-only
    fence."""
    formatted: list[str] = []
    rest = list(args)
    if is_method and rest and rest[0].get("name") == "self":
        formatted.append("self")
        rest = rest[1:]
    for arg in rest:
        formatted.append(_format_arg(arg, current_module, imports, enclosing_class))
    if (
        method_name != "__init__"
        and formatted
        and (len(formatted) > 1 or not is_method or formatted[0] != "self")
    ):
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

    Three cases for type rendering:
    - Real property with `type:` → emit `def name(self) -> T: ...`
    - Real property without `type:` (probe didn't observe it) → emit
      `def name(self): ...` matching v1's no-annotation style
    - Listener-only signal (no `type:`, no `settable:`) → emit nothing
      here; only the listener methods land in the class body
    """
    name = _resolve(prop, "name")
    type_str = _resolve(prop, "type")
    # Property-level element_type_override upgrades a non-parametric type
    # to its parametric form for the two cases where the property type
    # itself is generic: `Live.Base.Vector` + element=DeviceParameter →
    # `Live.Base.Vector[DeviceParameter]`, and `tuple` + element=int →
    # `tuple[int, ...]`. For typed Vector subclasses (UnavailableFeatureVector,
    # BrowserItemIterator, etc.) the element lives on the class itself, so the
    # override is redundant at the property site and skipped here.
    elem_ov = prop.get("element_type_override")
    if isinstance(elem_ov, dict) and elem_ov.get("value") and type_str:
        elem_val = elem_ov["value"]
        if type_str == "tuple":
            type_str = f"tuple[{elem_val}, ...]"
        elif type_str == "Live.Base.Vector":
            type_str = f"Live.Base.Vector[{elem_val}]"
    has_settable = "settable" in prop
    if type_str is None and not has_settable:
        return []  # listener-only signal — handled by the listener methods
    if type_str is None:
        # Real property with no observed type — emit without return
        # annotation (matches v1).
        out = ["@property", f"def {name}(self):"]
        raw_doc = prop.get("raw_doc")
        if raw_doc:
            for line in _indent(_wrap_docstring(raw_doc), 1):
                out.append(line)
        out.append(INDENT + "...")
        return out
    rendered = _ret_type_for_type(type_str, current_module, imports)
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


# Dunder sort prefixes so dunders precede all alphabetical members and
# come out in the iteration-protocol's canonical order (iter, getitem,
# len, contains, bool). __init__ leads when present.
_DUNDER_SORT_PREFIX = {
    "__init__":     "00_init",
    "__iter__":     "01_iter",
    "__getitem__":  "02_getitem",
    "__len__":      "03_len",
    "__contains__": "04_contains",
    "__bool__":     "05_bool",
}


def _sort_key(name: str) -> str:
    return _DUNDER_SORT_PREFIX.get(name, name)


def _build_iterable_dunders(cls: dict[str, Any], current_module: str,
                             imports: set[tuple[str, str]]) -> list[tuple[str, list[str]]]:
    """Synthesize iterator-protocol methods for an iterable container
    class. Element type uses the class's `element_type:` when known,
    otherwise `Any`. The `__getitem__` triplet is overload + overload +
    impl (matching v1's emission). Live-class element types are
    rendered through the type qualifier so they unqualify + add imports
    cleanly.

    Only fires for *containers* — classes that have both `append` and
    `extend`. Plain iterators (e.g. `Browser.BrowserItemIterator`) are
    flagged iterable for the base class but don't get dunders, since
    iterators don't support append/extend or __len__-style operations.
    """
    if not cls.get("iterable"):
        return []
    # Only the parametric base (`Live.Base.Vector`) gets dunders synthesized
    # at this layer. Non-parametric containers inherit the protocol from
    # `Vector[E]` (their declared base), and plain iterators get only the
    # `Iterable[E]` base with no body.
    if not cls.get("parametric"):
        return []
    cls_name = cls["name"]
    # Parametric containers use TypeVar `T` for the element type and
    # `Self` for the slice return — that way subclasses inheriting via
    # `class XVector(Vector[E])` see slice operations narrow to `XVector`,
    # not the broader `Vector[E]`.
    if cls.get("parametric"):
        elem = "T"
        cls_name = "Self"
    else:
        elem_raw = _resolve(cls, "element_type") or "Any"
        elem = render_type_string(elem_raw, current_module, imports)
    out: list[tuple[str, list[str]]] = []

    out.append(("__iter__", [f"def __iter__(self) -> Iterator[{elem}]: ..."]))

    # __getitem__ is emitted as 3 separate `def` blocks (overload + overload
    # + impl) but they share the sort key — listed alphabetically, all
    # three blocks appear together at the __getitem__ position.
    getitem_block = [
        "@overload",
        f"def __getitem__(self, index: int) -> {elem}: ...",
        "",
        "@overload",
        f"def __getitem__(self, index: slice) -> {cls_name}: ...",
        "",
        f"def __getitem__(self, index: int | slice) -> {elem} | {cls_name}: ...",
    ]
    out.append(("__getitem__", getitem_block))

    out.append(("__len__", ["def __len__(self) -> int: ..."]))
    out.append(("__contains__", ["def __contains__(self, value: object) -> bool: ..."]))
    out.append(("__bool__", ["def __bool__(self) -> bool: ..."]))
    return out


def _build_container_mutators(cls: dict[str, Any], current_module: str,
                               imports: set[tuple[str, str]]) -> list[tuple[str, list[str]]]:
    """Synthesize `append` / `extend` for concrete container subclasses
    (`container: true` flag). Both methods use the class's element type
    directly so the abstract `Vector(Generic[T_co])` base stays read-only
    at the type level — `T_co` covariance lets `Vector[Subclass]`
    substitute for `Vector[Parent]`, which the input position of an
    inherited `append(value: T)` would forbid.
    """
    if not cls.get("container"):
        return []
    elem_raw = _resolve(cls, "element_type")
    if not elem_raw:
        return []
    elem = render_type_string(elem_raw, current_module, imports)
    return [
        ("append", [f"def append(self, value: {elem}, /) -> None: ..."]),
        ("extend", [f"def extend(self, values: Iterable[{elem}], /) -> None: ..."]),
    ]


def _build_method_block(method: dict[str, Any], current_module: str,
                         imports: set[tuple[str, str]], registry: dict[str, Any],
                         is_method: bool, enclosing_class: str | None = None) -> list[str]:
    """Class method or module-level function block."""
    name = _resolve(method, "name")
    args = method.get("args") or []
    returns = method.get("returns") or {}
    ret_type = _ret_type_for_type(_resolve(returns, "type"), current_module, imports)
    arg_str = _format_method_args(args, current_module, imports, is_method, name, enclosing_class)
    raw_doc = method.get("raw_doc")
    # __init__ uses inline form (`def __init__(...) -> None: ...`)
    # regardless of arg count — matches v1's emission. Other methods
    # use the multi-line body even when there's no docstring.
    if name == "__init__":
        return [f"def {name}({arg_str}) -> {ret_type}: ..."]
    out = [f"def {name}({arg_str}) -> {ret_type}:"]
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
    val = const["value"]
    # Prefer double-quoted string literals (matching v1's emission style)
    # — `repr()` defaults to single quotes for plain strings.
    if isinstance(val, str) and "\n" not in val and '"' not in val:
        val_str = f'"{val}"'
    else:
        val_str = repr(val)
    return [f"{const['name']}: {const.get('type', 'str')} = {val_str}"]


def _collect_class_members(cls: dict[str, Any], current_module: str,
                            imports: set[tuple[str, str]],
                            registry: dict[str, Any]) -> list[tuple[str, list[str], str]]:
    """Collect all member blocks at this class as (sort_key, lines, kind) tuples.

    The third tuple element is a presentational kind tag used by the
    emitter to decide spacing — consecutive `constant` entries pack
    tight (no blank line between them), other adjacent kinds get a
    blank-line separator.
    """
    entries: list[tuple[str, list[str], str]] = []
    # Iterator-protocol synthesis for iterable container classes —
    # __iter__/__getitem__/__len__/__contains__/__bool__. Stub-specific
    # presentation; not in the YAML.
    for key, lines in _build_iterable_dunders(cls, current_module, imports):
        entries.append((key, lines, "method"))
    for key, lines in _build_container_mutators(cls, current_module, imports):
        entries.append((key, lines, "method"))
    for nested in cls.get("classes") or []:
        entries.append((nested["name"], _build_class_block(nested, current_module, imports, registry), "class"))
    for nested in cls.get("enums") or []:
        entries.append((nested["name"], _build_enum_block(nested), "enum"))
    for prop in cls.get("properties") or []:
        block = _build_property_block(prop, current_module, imports, registry)
        if block:
            entries.append((prop["name"], block, "property"))
        for listener in prop.get("listenable") or []:
            entries.append((listener, _build_listener_method(listener, prop["name"]), "method"))
    for m in cls.get("methods") or []:
        entries.append((m["name"], _build_method_block(m, current_module, imports, registry, True, cls["name"]), "method"))
    for c in cls.get("constants") or []:
        entries.append((c["name"], _build_constant_block(c), "constant"))
    return entries


def _build_class_block(cls: dict[str, Any], current_module: str,
                       imports: set[tuple[str, str]],
                       registry: dict[str, Any]) -> list[str]:
    """Class definition with members alphabetized at each level.

    Iterable container classes:
      - Parametric base (`Live.Base.Vector`) → `class Vector(Generic[T])`
        with full iterator-protocol + append/extend declared once,
        all typed against the TypeVar `T`.
      - Concrete iterable subclasses (`MidiNoteVector`, `FloatVector`, ...)
        → `class XVector(Vector[E])` with empty body. Every dunder and
        every typed method comes from the parameterized base.
      - Non-container iterables that lack append/extend (e.g. iterators)
        keep `Iterable[E]` as the base since they don't fit the Vector shape.
    """
    name = cls["name"]
    base_str = ""
    if cls.get("iterable"):
        is_container = bool(cls.get("container"))
        if cls.get("parametric"):
            base_str = "(Generic[T])"
            typing_extras: set[str] = registry["_module_typing_extras"]
            typing_extras.update(("Generic", "Iterator", "Self", "TypeVar", "overload"))
            registry["_module_emits_typevar"] = True
        elif is_container:
            elem = _resolve(cls, "element_type")
            if elem:
                elem_rendered = render_type_string(elem, current_module, imports)
                imports.add(("Live.Base", "Vector"))
                base_str = f"(Vector[{elem_rendered}])"
            else:
                base_str = "(Iterable)"
                typing_extras = registry["_module_typing_extras"]
                typing_extras.add("Iterable")
        else:
            # Plain iterator (no append/extend) — Iterable[E] base, no
            # synthesized dunders, no TypeVar (concrete element type).
            elem = _resolve(cls, "element_type")
            if elem:
                elem_rendered = render_type_string(elem, current_module, imports)
                base_str = f"(Iterable[{elem_rendered}])"
            else:
                base_str = "(Iterable)"
            typing_extras = registry["_module_typing_extras"]
            typing_extras.add("Iterable")
    else:
        # `Boost.Python.instance` is a binding artifact — every Live
        # class has it somewhere in the ancestor chain, but it isn't
        # a useful base in stub form (it has no methods worth
        # surfacing and pyright treats it as opaque). Filter so the
        # stub picks the closest semantically meaningful ancestor.
        ancestors = [
            a for a in (cls.get("ancestors") or [])
            if a != "Boost.Python.instance"
        ]
        if ancestors:
            bases = [render_type(a, current_module, imports) for a in ancestors[:1]]
            base_str = f"({', '.join(bases)})"
    raw_doc = cls.get("raw_doc")
    members = _collect_class_members(cls, current_module, imports, registry)
    if not members and not raw_doc:
        # Empty class body — inline form: `class X(B): ...`
        return [f"class {name}{base_str}: ..."]

    out = [f"class {name}{base_str}:"]
    if raw_doc:
        for line in _indent(_wrap_docstring(raw_doc), 1):
            out.append(line)
    if members:
        # Blank line separates the class header (declaration + optional
        # docstring) from its first member. Matches v1.
        out.append("")
    if not members:
        # Class with only a docstring needs no `...` filler — the
        # docstring itself counts as the body (matches v1).
        if not raw_doc:
            out.append(INDENT + "...")
        return out

    # Dunders sort first (canonical iter-protocol order). Regular
    # members sort alphabetically after. Consecutive constants pack
    # tight (no blank between them) — matches v1's class-attribute
    # emission style for enum-like constant containers (Variants).
    members.sort(key=lambda kv: _sort_key(kv[0]))
    prev_kind: str | None = None
    for i, (_, block, kind) in enumerate(members):
        # Drop the inter-member blank line when both this and the
        # previous entry are constants. Also when the previous entry
        # was the class docstring's separator and this is a constant
        # (constants attach directly under the docstring, no blank).
        if i == 0 and raw_doc and kind == "constant":
            # Remove the blank line we added after the docstring.
            if out and out[-1] == "":
                out.pop()
        elif i > 0:
            if not (prev_kind == "constant" and kind == "constant"):
                out.append("")
        for line in _indent(block, 1):
            out.append(line)
        prev_kind = kind
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
    # Per-module accumulator for extra typing names beyond the standard
    # set. Iterable container classes add `Iterator` and `overload`;
    # the generic Vector adds `Generic` and `TypeVar`.
    registry["_module_typing_extras"] = set()
    registry["_module_emits_typevar"] = False

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

    # Typing imports — TYPE_CHECKING first, rest case-sensitive
    # alphabetical (matches v1's order: TYPE_CHECKING, Any, Callable,
    # Iterable, Iterator, overload, ...).
    base_names = {"TYPE_CHECKING", "Any", "Callable", "Iterable"}
    extras = registry.get("_module_typing_extras") or set()
    rest = sorted((base_names | extras) - {"TYPE_CHECKING"})
    typing_names = ["TYPE_CHECKING", *rest]
    buf.write(f"from typing import {', '.join(typing_names)}\n\n")
    # TypeVar declaration for the generic Vector base. Covariant — `T`
    # appears only in output positions (iter, getitem) on the abstract
    # base. Concrete container subclasses (FloatVector, MidiNoteVector,
    # ...) get their own append/extend methods synthesized with their
    # concrete element type, so `T` never appears in input position.
    if registry.get("_module_emits_typevar"):
        buf.write("T = TypeVar('T', covariant=True)\n\n")
    if imports:
        buf.write("if TYPE_CHECKING:\n")
        # Group imports by module, sort
        by_module: dict[str, set[str]] = {}
        for mod, cls_name in imports:
            by_module.setdefault(mod, set()).add(cls_name)
        for mod in sorted(by_module):
            classes = sorted(by_module[mod])
            buf.write(f"    from {mod} import {', '.join(classes)}\n")
        # Three blank lines before first class (matches v1).
        buf.write("\n\n\n")
    else:
        # No TYPE_CHECKING block; two blank lines before first class
        # (the typing import already wrote one).
        buf.write("\n")

    buf.write("\n".join(body))
    if not body or body[-1] != "":
        buf.write("\n")

    if names:
        # Blank line between the last class/function and __all__
        # (matches v1's spacing).
        buf.write(f"\n__all__ = {names!r}\n")

    return buf.getvalue()


# --- CLI --------------------------------------------------------------- #


def main() -> int:
    p = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
    p.add_argument("version", help="Live version (e.g. 12.3.6)")
    p.add_argument("--input", help="lom yaml dir (default: stubs/<v>/lom)")
    p.add_argument("--output", help="output dir for .pyi files")
    args = p.parse_args()

    seed_dir = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "stubs" / args.version / "lom"
    )
    # Dual-format loader (migration phase 3): if a sibling `modules/`
    # dir contains `<Module>.md`, that markdown is the source of truth
    # and we parse it instead of the YAML. The legacy YAML branch
    # stays in place for modules not yet converted.
    md_dir = seed_dir.parent / "modules"
    out_dir = (
        Path(args.output).resolve()
        if args.output
        else REPO_ROOT / "stubs" / args.version / "Live"
    )

    if not seed_dir.exists():
        print(f"error: seed yaml dir not found at {seed_dir}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)

    # Per-module renderer state lives in this dict; each emit_module call
    # resets the per-module accumulators.
    registry: dict[str, Any] = {}

    # Build a set of module names that have markdown form available so
    # the per-module loop can prefer markdown over yaml.
    md_modules: set[str] = set()
    if md_dir.exists():
        md_modules = {p.stem for p in md_dir.glob("*.md")}

    def _load_module(yaml_path: Path) -> dict:
        """Prefer the markdown source when present; fall back to YAML."""
        module_name = yaml_path.stem
        if module_name in md_modules:
            # Sibling-script import: tools/ isn't a package, so add the
            # parse dir to sys.path and import by module name.
            parse_dir = str(REPO_ROOT / "tools" / "parse")
            if parse_dir not in sys.path:
                sys.path.insert(0, parse_dir)
            from parse_module_md import parse_module_md, to_legacy_shape
            md_path = md_dir / f"{module_name}.md"
            return to_legacy_shape(parse_module_md(md_path))
        return yaml.safe_load(yaml_path.read_text())

    written = 0
    all_module_names: list[str] = []
    for path in sorted(seed_dir.glob("*.yaml")):
        module = _load_module(path)
        # Foundation pages (e.g. `CallingConventions.yaml`,
        # `RemoteScripts.yaml`) are docs-only lom YAMLs — pure prose,
        # no `primary_class:` / `classes:` / `enums:` / `functions:` /
        # `constants:` content. Skip so the stub package doesn't ship
        # empty `Live.<Foundation>` modules that would pollute
        # downstream pyright namespaces. `LomObject` and `Listener`
        # are sidebar-hidden but DO have real class content, so they
        # still ship.
        has_content = any(
            module.get(k) for k in
            ("primary_class", "classes", "enums", "functions", "constants")
        )
        if not has_content:
            continue
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

    # PEP 561 marker — signals "this package ships type information".
    (out_dir / "py.typed").write_text("")

    try:
        rel = out_dir.relative_to(REPO_ROOT)
        print(f"Wrote {written} .pyi files to {rel}/")
    except ValueError:
        print(f"Wrote {written} .pyi files to {out_dir}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

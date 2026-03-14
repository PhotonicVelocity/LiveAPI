#!/usr/bin/env python3
"""Generate markdown reference docs from .pyi stub files.

Usage:
    python tools/generate/generate_reference.py [--stubs STUBS_DIR] [--output OUTPUT_DIR]

Defaults:
    --stubs   stubs/12.3.6/Live
    --output  reference
"""

from __future__ import annotations

import argparse
import ast
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

# Listener method patterns to exclude from the public API
LISTENER_PATTERNS = re.compile(
    r"^(add_\w+_listener|remove_\w+_listener|\w+_has_listener)$"
)

# Internal/private members to skip
SKIP_MEMBERS = {"_live_ptr", "__init__", "__module__", "__qualname__"}

# ---------------------------------------------------------------------------
# Directory layout — mirrors the old reference/ structure
# ---------------------------------------------------------------------------

# Namespace -> subdirectory mapping. Namespaces not listed here go to root.
CATEGORY_MAP: dict[str, str] = {
    # tracks/
    "Track": "tracks",
    "Clip": "tracks",
    "ClipSlot": "tracks",
    "Envelope": "tracks",
    "MixerDevice": "tracks",
    "TakeLane": "tracks",
    # devices/
    "Device": "devices",
    "DeviceParameter": "devices",
    "DeviceIO": "devices",
    "Chain": "devices",
    "ChainMixerDevice": "devices",
    "DrumChain": "devices",
    "DrumPad": "devices",
    "RackDevice": "devices",
    "CcControlDevice": "devices",
    "CompressorDevice": "devices",
    "DriftDevice": "devices",
    "DrumCellDevice": "devices",
    "Eq8Device": "devices",
    "HybridReverbDevice": "devices",
    "LooperDevice": "devices",
    "MaxDevice": "devices",
    "MeldDevice": "devices",
    "PluginDevice": "devices",
    "RoarDevice": "devices",
    "Sample": "devices",
    "ShifterDevice": "devices",
    "SimplerDevice": "devices",
    "SpectralResonatorDevice": "devices",
    "WavetableDevice": "devices",
    # other/
    "Conversions": "other",
    "Groove": "other",
    "GroovePool": "other",
    "TuningSystem": "other",
    "Base": "other",
    "Licensing": "other",
    "Listener": "other",
    "LomObject": "other",
    "MidiMap": "other",
}

# Ordered nav structure for mkdocs — groups and their members.
# Namespaces within each group are written in display order.
NAV_STRUCTURE: list[tuple[str | None, list[str]]] = [
    (None, ["Application", "Song", "Scene"]),
    ("Tracks", ["Track", "Clip", "ClipSlot", "Envelope", "MixerDevice", "TakeLane"]),
    (
        "Devices",
        ["Device", "DeviceParameter", "Chain", "ChainMixerDevice", "DrumChain", "DrumPad", "RackDevice"],
    ),
    (
        "Device Subclasses",
        [
            "CcControlDevice",
            "CompressorDevice",
            "DeviceIO",
            "DriftDevice",
            "DrumCellDevice",
            "Eq8Device",
            "HybridReverbDevice",
            "LooperDevice",
            "MaxDevice",
            "MeldDevice",
            "PluginDevice",
            "RoarDevice",
            "Sample",
            "ShifterDevice",
            "SimplerDevice",
            "SpectralResonatorDevice",
            "WavetableDevice",
        ],
    ),
    (
        "Other",
        [
            "Browser",
            "Base",
            "Conversions",
            "Groove",
            "GroovePool",
            "Licensing",
            "Listener",
            "LomObject",
            "MidiMap",
            "TuningSystem",
        ],
    ),
]


def ns_relpath(ns_name: str) -> str:
    """Return the relative path (from reference/) for a namespace's .md file."""
    subdir = CATEGORY_MAP.get(ns_name)
    if subdir:
        return f"{subdir}/{ns_name}.md"
    return f"{ns_name}.md"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class PropertyInfo:
    name: str
    type: str
    settable: bool
    listenable: bool
    docstring: str


@dataclass
class MethodInfo:
    name: str
    args: list[tuple[str, str, str | None]]  # (name, type, default)
    return_type: str
    docstring: str


@dataclass
class EnumValue:
    name: str
    value: str


@dataclass
class EnumInfo:
    name: str
    docstring: str
    values: list[EnumValue]


@dataclass
class ClassInfo:
    name: str
    namespace: str  # e.g. "Live.Song"
    docstring: str
    constructable: bool
    init_args: list[tuple[str, str, str | None]]
    properties: list[PropertyInfo] = field(default_factory=list)
    methods: list[MethodInfo] = field(default_factory=list)
    enums: list[EnumInfo] = field(default_factory=list)
    inner_classes: list[ClassInfo] = field(default_factory=list)


@dataclass
class ModuleFunctions:
    """Module-level functions (not inside a class)."""

    functions: list[MethodInfo] = field(default_factory=list)


# ---------------------------------------------------------------------------
# AST Parsing
# ---------------------------------------------------------------------------


def get_docstring(node: ast.AST) -> str:
    """Extract docstring from a class or function node."""
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, (ast.Constant, ast.Str))
        ):
            val = node.body[0].value
            raw = val.value if isinstance(val, ast.Constant) else val.s
            if not isinstance(raw, str):
                return ""
            # Normalize whitespace: collapse multi-line docstrings
            lines = raw.strip().splitlines()
            cleaned = []
            for line in lines:
                cleaned.append(line.strip())
            return " ".join(cleaned)
    return ""


def annotation_to_str(node: ast.AST | None) -> str:
    """Convert an annotation AST node to a string representation."""
    if node is None:
        return "Any"
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "None"
        return repr(node.value)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{annotation_to_str(node.value)}.{node.attr}"
    if isinstance(node, ast.Subscript):
        return f"{annotation_to_str(node.value)}[{annotation_to_str(node.slice)}]"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return f"{annotation_to_str(node.left)} | {annotation_to_str(node.right)}"
    if isinstance(node, ast.Tuple):
        return ", ".join(annotation_to_str(e) for e in node.elts)
    if isinstance(node, ast.List):
        return ", ".join(annotation_to_str(e) for e in node.elts)
    # Fallback: use ast.unparse if available (Python 3.9+)
    try:
        return ast.unparse(node)
    except Exception:
        return "Any"


def is_enum_class(node: ast.ClassDef) -> bool:
    """Check if a class definition looks like an enum (class attrs with int values, no methods)."""
    has_class_attrs = False
    has_methods = False
    for item in node.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            has_class_attrs = True
        elif isinstance(item, ast.FunctionDef):
            if item.name not in ("__init__", "__str__", "__repr__"):
                has_methods = True
        elif isinstance(item, ast.Expr) and isinstance(item.value, (ast.Constant, ast.Str)):
            continue  # docstring
        elif isinstance(item, ast.Pass):
            continue
    return has_class_attrs and not has_methods


def parse_enum(node: ast.ClassDef) -> EnumInfo:
    """Parse a class that looks like an enum."""
    values = []
    for item in node.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            val = ""
            if isinstance(item.value, ast.Constant):
                val = str(item.value.value)
            values.append(EnumValue(name=item.target.id, value=val))
    return EnumInfo(name=node.name, docstring=get_docstring(node), values=values)


def extract_listenable_properties(node: ast.ClassDef) -> set[str]:
    """Find all property names that have add_X_listener methods."""
    listenable = set()
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            m = re.match(r"^add_(\w+)_listener$", item.name)
            if m:
                listenable.add(m.group(1))
    return listenable


def extract_settable_properties(node: ast.ClassDef) -> set[str]:
    """Find all property names that have setters."""
    settable = set()
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            for dec in item.decorator_list:
                if isinstance(dec, ast.Attribute) and dec.attr == "setter":
                    if isinstance(dec.value, ast.Name):
                        settable.add(dec.value.id)
    return settable


def parse_function_args(
    node: ast.FunctionDef,
) -> list[tuple[str, str, str | None]]:
    """Parse function arguments, skipping 'self'. Returns list of (name, type, default|None)."""
    args_info = []
    arguments = node.args

    # Build defaults mapping: defaults align to the end of args
    num_args = len(arguments.args)
    num_defaults = len(arguments.defaults)
    default_offset = num_args - num_defaults

    for i, arg in enumerate(arguments.args):
        if arg.arg == "self":
            continue
        type_str = annotation_to_str(arg.annotation)
        default = None
        default_idx = i - default_offset
        if default_idx >= 0 and default_idx < len(arguments.defaults):
            default = annotation_to_str(arguments.defaults[default_idx])
        args_info.append((arg.arg, type_str, default))

    return args_info


def parse_class(node: ast.ClassDef, namespace: str) -> ClassInfo:
    """Parse a class definition into ClassInfo."""
    docstring = get_docstring(node)
    listenable = extract_listenable_properties(node)
    settable = extract_settable_properties(node)

    constructable = False
    init_args: list[tuple[str, str, str | None]] = []

    properties: list[PropertyInfo] = []
    methods: list[MethodInfo] = []
    enums: list[EnumInfo] = []
    inner_classes: list[ClassInfo] = []

    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            if item.name in SKIP_MEMBERS:
                if item.name == "__init__":
                    constructable = True
                    init_args = parse_function_args(item)
                continue

            # Skip listener boilerplate
            if LISTENER_PATTERNS.match(item.name):
                continue

            # Skip property setters (handled via settable set)
            is_setter = False
            is_property = False
            for dec in item.decorator_list:
                if isinstance(dec, ast.Attribute) and dec.attr == "setter":
                    is_setter = True
                if isinstance(dec, ast.Name) and dec.id == "property":
                    is_property = True
            if is_setter:
                continue

            if is_property:
                prop_type = annotation_to_str(item.returns)
                prop_doc = get_docstring(item)
                properties.append(
                    PropertyInfo(
                        name=item.name,
                        type=prop_type,
                        settable=item.name in settable,
                        listenable=item.name in listenable,
                        docstring=prop_doc,
                    )
                )
            else:
                # Regular method
                args = parse_function_args(item)
                ret = annotation_to_str(item.returns)
                doc = get_docstring(item)
                methods.append(MethodInfo(name=item.name, args=args, return_type=ret, docstring=doc))

        elif isinstance(item, ast.ClassDef):
            if is_enum_class(item):
                enums.append(parse_enum(item))
            else:
                inner = parse_class(item, f"{namespace}.{node.name}")
                inner_classes.append(inner)

    return ClassInfo(
        name=node.name,
        namespace=namespace,
        docstring=docstring,
        constructable=constructable,
        init_args=init_args,
        properties=properties,
        methods=methods,
        enums=enums,
        inner_classes=inner_classes,
    )


def parse_stub_file(path: Path, namespace: str) -> tuple[list[ClassInfo], list[EnumInfo], list[MethodInfo]]:
    """Parse a .pyi file and return classes, module-level enums, and module-level functions."""
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    classes: list[ClassInfo] = []
    enums: list[EnumInfo] = []
    functions: list[MethodInfo] = []

    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            if is_enum_class(node):
                enums.append(parse_enum(node))
            else:
                classes.append(parse_class(node, namespace))
        elif isinstance(node, ast.FunctionDef):
            if node.name.startswith("_"):
                continue
            args = parse_function_args(node)
            ret = annotation_to_str(node.returns)
            doc = get_docstring(node)
            functions.append(MethodInfo(name=node.name, args=args, return_type=ret, docstring=doc))

    return classes, enums, functions


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------


def escape_table_cell(text: str) -> str:
    """Escape characters that break markdown table cells."""
    return text.replace("|", "\\|")


def format_args_signature(args: list[tuple[str, str, str | None]]) -> str:
    """Format function arguments for a summary signature."""
    parts = []
    for name, type_str, default in args:
        # Simplify type for signature display
        display_type = type_str.replace(" | None", "").replace("None | ", "")
        if default is not None:
            # Clean up default display
            default_display = default.replace("'", "").replace('"', "")
            parts.append(f"{name}: {display_type} = {default_display}")
        else:
            parts.append(f"{name}: {display_type}")
    return ", ".join(parts)


def format_args_detail(args: list[tuple[str, str, str | None]]) -> list[str]:
    """Format function arguments for detailed display."""
    lines = []
    for name, type_str, default in args:
        display_type = type_str.replace(" | None", "").replace("None | ", "")
        if default is not None:
            default_display = default.replace("'", "").replace('"', "")
            lines.append(f"  - `{name}: {display_type} = {default_display}`")
        else:
            lines.append(f"  - `{name}: {display_type}`")
    return lines


def truncate_summary(docstring: str, max_len: int = 80) -> str:
    """Get a short summary from a docstring."""
    if not docstring:
        return ""
    # Take first sentence
    first = docstring.split(". ")[0].split(".\n")[0]
    if not first.endswith("."):
        first += "."
    if len(first) > max_len:
        return first[: max_len - 3] + "..."
    return first


def generate_class_markdown(
    cls: ClassInfo,
    module_enums: list[EnumInfo],
    module_functions: list[MethodInfo],
    module_classes: list[ClassInfo],
    is_inner: bool = False,
) -> str:
    """Generate markdown for a single class."""
    lines: list[str] = []
    heading = "##" if is_inner else "#"
    sub = "###" if is_inner else "##"
    detail = "####" if is_inner else "###"

    if is_inner:
        lines.append(f"{heading} {cls.name}")
        lines.append("")
        lines.append(f"> `{cls.namespace}.{cls.name}`")
    else:
        lines.append(f"# {cls.name}")
        lines.append("")
        lines.append(f"> `{cls.namespace}.{cls.name}`")

    lines.append("")

    if cls.docstring:
        lines.append(cls.docstring)
        lines.append("")

    if cls.constructable:
        if cls.init_args:
            sig = format_args_signature(cls.init_args)
            lines.append(f"**Constructor:** `{cls.name}({sig})`")
        else:
            lines.append(f"**Constructor:** `{cls.name}()`")
        lines.append("")

    # --- Inner classes (View, etc.) ---
    for inner in cls.inner_classes:
        inner_md = generate_class_markdown(inner, [], [], [], is_inner=True)
        lines.append(inner_md)

    # --- Properties ---
    if cls.properties:
        lines.append(f"{sub} Properties")
        lines.append("")

        # Summary table
        lines.append(f"| Property | Type | Settable | Listenable | Description |")
        lines.append(f"| --- | --- | --- | --- | --- |")
        for prop in cls.properties:
            settable = "yes" if prop.settable else "no"
            listenable = "yes" if prop.listenable else "no"
            summary = escape_table_cell(truncate_summary(prop.docstring))
            esc_type = escape_table_cell(prop.type)
            lines.append(f"| `{prop.name}` | `{esc_type}` | `{settable}` | `{listenable}` | {summary} |")
        lines.append("")

        # Per-property details
        for prop in cls.properties:
            lines.append(f"{detail} `{prop.name}`")
            lines.append("")
            lines.append(f"- **Type:** `{prop.type}`")
            lines.append(f"- **Settable:** `{'yes' if prop.settable else 'no'}`")
            lines.append(f"- **Listenable:** `{'yes' if prop.listenable else 'no'}`")
            lines.append("")
            if prop.docstring:
                lines.append(prop.docstring)
                lines.append("")

    # --- Methods ---
    if cls.methods:
        lines.append(f"{sub} Methods")
        lines.append("")

        # Summary table
        lines.append(f"| Method | Returns | Description |")
        lines.append(f"| --- | --- | --- |")
        for method in cls.methods:
            sig = escape_table_cell(format_args_signature(method.args))
            summary = escape_table_cell(truncate_summary(method.docstring))
            esc_ret = escape_table_cell(method.return_type)
            lines.append(f"| `{method.name}({sig})` | `{esc_ret}` | {summary} |")
        lines.append("")

        # Per-method details
        for method in cls.methods:
            sig = format_args_signature(method.args)
            lines.append(f"{detail} `{method.name}({sig})`")
            lines.append("")
            lines.append(f"- **Returns:** `{method.return_type}`")
            if method.args:
                lines.append(f"- **Args:**")
                for arg_line in format_args_detail(method.args):
                    lines.append(arg_line)
            lines.append("")
            if method.docstring:
                lines.append(method.docstring)
                lines.append("")

    # --- Enums (from the class itself) ---
    all_enums = cls.enums + [e for e in module_enums]
    if all_enums:
        lines.append(f"{sub} Enums")
        lines.append("")
        for enum in all_enums:
            lines.append(f"{detail} `{enum.name}`")
            lines.append("")
            if enum.docstring:
                lines.append(enum.docstring)
                lines.append("")
            lines.append("| Value | Name |")
            lines.append("| --- | --- |")
            for val in enum.values:
                lines.append(f"| `{val.value}` | `{val.name}` |")
            lines.append("")

    # --- Module-level helper classes (non-enum, non-primary) ---
    for helper_cls in module_classes:
        helper_md = generate_class_markdown(helper_cls, [], [], [], is_inner=True)
        lines.append(helper_md)

    # --- Module-level functions ---
    if module_functions:
        lines.append(f"{sub} Module Functions")
        lines.append("")
        lines.append(f"| Function | Returns | Description |")
        lines.append(f"| --- | --- | --- |")
        for func in module_functions:
            sig = escape_table_cell(format_args_signature(func.args))
            summary = escape_table_cell(truncate_summary(func.docstring))
            esc_ret = escape_table_cell(func.return_type)
            lines.append(f"| `{func.name}({sig})` | `{esc_ret}` | {summary} |")
        lines.append("")

        for func in module_functions:
            sig = format_args_signature(func.args)
            lines.append(f"{detail} `{func.name}({sig})`")
            lines.append("")
            lines.append(f"- **Returns:** `{func.return_type}`")
            if func.args:
                lines.append(f"- **Args:**")
                for arg_line in format_args_detail(func.args):
                    lines.append(arg_line)
            lines.append("")
            if func.docstring:
                lines.append(func.docstring)
                lines.append("")

    return "\n".join(lines)


def generate_namespace_markdown(
    primary_class: ClassInfo | None,
    module_enums: list[EnumInfo],
    module_functions: list[MethodInfo],
    module_classes: list[ClassInfo],
) -> str:
    """Generate markdown for a namespace that may or may not have a primary class."""
    if primary_class:
        return generate_class_markdown(primary_class, module_enums, module_functions, module_classes)

    # No primary class — module is just enums, functions, and helper classes
    # Use the namespace name as the page title
    lines: list[str] = []

    if module_classes:
        for cls in module_classes:
            cls_md = generate_class_markdown(cls, [], [], [])
            lines.append(cls_md)

    if module_enums:
        lines.append("## Enums")
        lines.append("")
        for enum in module_enums:
            lines.append(f"### `{enum.name}`")
            lines.append("")
            if enum.docstring:
                lines.append(enum.docstring)
                lines.append("")
            lines.append("| Value | Name |")
            lines.append("| --- | --- |")
            for val in enum.values:
                lines.append(f"| `{val.value}` | `{val.name}` |")
            lines.append("")

    if module_functions:
        lines.append("## Module Functions")
        lines.append("")
        lines.append("| Function | Returns | Description |")
        lines.append("| --- | --- | --- |")
        for func in module_functions:
            sig = escape_table_cell(format_args_signature(func.args))
            summary = escape_table_cell(truncate_summary(func.docstring))
            esc_ret = escape_table_cell(func.return_type)
            lines.append(f"| `{func.name}({sig})` | `{esc_ret}` | {summary} |")
        lines.append("")
        for func in module_functions:
            sig = format_args_signature(func.args)
            lines.append(f"### `{func.name}({sig})`")
            lines.append("")
            lines.append(f"- **Returns:** `{func.return_type}`")
            if func.args:
                lines.append(f"- **Args:**")
                for arg_line in format_args_detail(func.args):
                    lines.append(arg_line)
            lines.append("")
            if func.docstring:
                lines.append(func.docstring)
                lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Namespace processing
# ---------------------------------------------------------------------------


def process_namespace(ns_dir: Path) -> tuple[str, str]:
    """Process a single namespace directory and return (filename, markdown content).

    Returns the namespace name and generated markdown.
    """
    ns_name = ns_dir.name  # e.g. "Song"
    namespace = f"Live.{ns_name}"

    # Parse the __init__.pyi for enums, helper classes, and module functions
    init_file = ns_dir / "__init__.pyi"
    init_classes: list[ClassInfo] = []
    init_enums: list[EnumInfo] = []
    init_functions: list[MethodInfo] = []
    if init_file.exists():
        init_classes, init_enums, init_functions = parse_stub_file(init_file, namespace)

    # Parse the main class file (e.g., Song/Song.pyi)
    main_file = ns_dir / f"{ns_name}.pyi"
    primary_class: ClassInfo | None = None
    main_classes: list[ClassInfo] = []

    if main_file.exists():
        main_classes, main_enums, main_functions = parse_stub_file(main_file, namespace)
        # The primary class is the one matching the namespace name
        for cls in main_classes:
            if cls.name == ns_name:
                primary_class = cls
                break
        # Any extra classes in the main file that aren't the primary
        extra_main = [c for c in main_classes if c.name != ns_name]
        init_classes.extend(extra_main)
        init_enums.extend(main_enums)
        init_functions.extend(main_functions)

    # Filter out the primary class from init_classes (it's re-exported)
    init_classes = [c for c in init_classes if c.name != ns_name]

    md = generate_namespace_markdown(primary_class, init_enums, init_functions, init_classes)
    return ns_name, md


def generate_index(namespaces: list[str]) -> str:
    """Generate the index.md landing page."""
    lines = [
        "# Live Object Model Reference",
        "",
        "Comprehensive reference for the Ableton Live Object Model (LOM) — the object hierarchy exposed by Live's",
        "Python runtime to Control Surface scripts, Max for Live devices, and external clients.",
        "",
        "## About",
        "",
        "Ableton does not publicly document the Live Python API. This reference is auto-generated from",
        "API stubs produced by running introspection inside Live.",
        "",
        "## How to Read",
        "",
        "Each page documents one LOM class with:",
        "",
        "- **Summary tables** — quick overview of all properties and methods",
        "- **Detail sections** — per-member descriptions with type info",
        "- **Enums** — value tables for enum types defined in each namespace",
        "",
        "Use the sidebar navigation to browse by LOM hierarchy, or search for a specific class or member.",
        "",
    ]

    # Build grouped listing
    for group_name, members in NAV_STRUCTURE:
        present = [m for m in members if m in namespaces]
        if not present:
            continue
        if group_name:
            lines.append(f"## {group_name}")
        else:
            lines.append("## Core")
        lines.append("")
        lines.append("| Class | Namespace |")
        lines.append("| --- | --- |")
        for ns in present:
            rel = ns_relpath(ns)
            lines.append(f"| [{ns}]({rel}) | `Live.{ns}` |")
        lines.append("")

    # Any namespaces not in the nav structure
    all_in_nav = {m for _, members in NAV_STRUCTURE for m in members}
    extras = sorted(set(namespaces) - all_in_nav)
    if extras:
        lines.append("## Other Namespaces")
        lines.append("")
        lines.append("| Class | Namespace |")
        lines.append("| --- | --- |")
        for ns in extras:
            rel = ns_relpath(ns)
            lines.append(f"| [{ns}]({rel}) | `Live.{ns}` |")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def generate_mkdocs_nav(namespaces: list[str]) -> list[str]:
    """Generate the nav section lines for mkdocs.yml."""
    lines = [
        "nav:",
        "  - index.md",
    ]

    for group_name, members in NAV_STRUCTURE:
        present = [m for m in members if m in namespaces]
        if not present:
            continue
        if group_name is None:
            # Root-level entries
            for ns in present:
                lines.append(f"  - {ns_relpath(ns)}")
        else:
            lines.append(f"  - {group_name}:")
            for ns in present:
                lines.append(f"      - {ns_relpath(ns)}")

    # Any namespaces not covered by the nav structure
    all_in_nav = {m for _, members in NAV_STRUCTURE for m in members}
    extras = sorted(set(namespaces) - all_in_nav)
    if extras:
        lines.append("  - Other:")
        for ns in extras:
            lines.append(f"      - {ns_relpath(ns)}")

    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate reference docs from .pyi stubs")
    parser.add_argument("--stubs", default="stubs/12.3.6/Live", help="Path to Live stubs directory")
    parser.add_argument("--output", default="reference", help="Output directory for generated markdown")
    args = parser.parse_args()

    stubs_dir = Path(args.stubs)
    output_dir = Path(args.output)

    if not stubs_dir.exists():
        print(f"Error: stubs directory not found: {stubs_dir}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    for subdir in ("tracks", "devices", "other"):
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)

    # Find all namespace directories (those containing .pyi files)
    namespaces: list[str] = []
    for item in sorted(stubs_dir.iterdir()):
        if item.is_dir() and (item / "__init__.pyi").exists():
            namespaces.append(item.name)

    print(f"Found {len(namespaces)} namespaces in {stubs_dir}")

    generated_files: list[Path] = []
    for ns_name in namespaces:
        ns_dir = stubs_dir / ns_name
        name, md = process_namespace(ns_dir)
        out_file = output_dir / ns_relpath(name)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(md, encoding="utf-8")
        generated_files.append(out_file)
        print(f"  Generated {out_file}")

    # Generate index
    index_md = generate_index(namespaces)
    index_file = output_dir / "index.md"
    index_file.write_text(index_md, encoding="utf-8")
    generated_files.append(index_file)
    print(f"  Generated {index_file}")

    # Run prettier on generated files
    print("\nRunning prettier on generated files...")
    for f in generated_files:
        try:
            subprocess.run(
                ["prettier", "--prose-wrap", "preserve", "--write", str(f)],
                capture_output=True,
                text=True,
                check=True,
            )
        except FileNotFoundError:
            print("  Warning: prettier not found, skipping formatting")
            break
        except subprocess.CalledProcessError as e:
            print(f"  Warning: prettier failed on {f}: {e.stderr}")

    # Print nav section for mkdocs.yml
    nav_lines = generate_mkdocs_nav(namespaces)
    print(f"\nDone! Generated {len(generated_files)} files in {output_dir}/")
    print("\n--- Suggested mkdocs.yml nav section ---")
    print("\n".join(nav_lines))


if __name__ == "__main__":
    main()

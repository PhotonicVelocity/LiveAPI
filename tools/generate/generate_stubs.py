"""Generate .pyi stub files from LiveTree.resolved.json.

Walks the resolved tree and emits typed Python stubs for the Ableton Live Object Model.
The tree structure drives the output layout: each namespace module becomes a package
directory, and classes/enums/functions are rendered according to their node type.

Usage:
    python tools/parse/generate_stubs.py 12.3.6
    python tools/parse/generate_stubs.py 12.3.6 --input path/to/resolved.json --output path/to/Live
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from io import StringIO
from os import makedirs
from os.path import abspath, exists, join

_HEADER = "from __future__ import annotations\nfrom typing import TYPE_CHECKING, Any, Callable, Iterable\n"

# Extra header for files that define Vector types (need Generic, TypeVar, Iterator)
_VECTOR_HEADER = (
    "from __future__ import annotations\n"
    "from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload\n"
    "\nT = TypeVar('T')\n"
)

# Matches capitalized identifiers that could be class/enum references in type annotations.
_TYPE_REF_RE = re.compile(r"\b([A-Z][A-Za-z0-9]+)\b")

# Matches Boost.Python init_doc arg patterns: (type)name or (type)name=default
_INIT_ARG_RE = re.compile(r"\((\w+)\)(\w+)(?:=([^\s\],\)]+))?")

# Names that should never appear in TYPE_CHECKING imports.
_SKIP_NAMES = {"None", "Callable", "Any", "TYPE_CHECKING", "IO", "Exception"}


class StubGenerator:
    def __init__(self, tree: dict, output_dir: str):
        self.tree = tree
        self.output_dir = output_dir

        # Indexes built in Phase 1
        self._class_to_module: dict[str, str] = {}
        self._module_classes: dict[str, set[str]] = {}
        self._nested_class_parent: dict[str, str] = {}  # "View" -> "Device" (nested class -> parent)
        self._enum_lookup: dict[str, int] = {}
        self._vector_types: set[str] = set()  # class names that are vector types
        self._vector_element_fallback: dict[str, str] = {}  # vector class -> default element type

    # ------------------------------------------------------------------
    # Phase 1: Indexing
    # ------------------------------------------------------------------

    def _build_indexes(self) -> None:
        """Walk the entire tree once to build lookup tables."""
        for module_node in self.tree.get("children", []):
            module_name = module_node["name"]
            self._module_classes.setdefault(module_name, set())
            for child in module_node.get("children", []):
                self._index_node(child, module_name, parent_class=None)

    def _index_node(self, node: dict, module_name: str, parent_class: str | None) -> None:
        if node.get("ref"):
            return

        name = node.get("name", "")
        node_type = node.get("type", "")

        if node_type in ("class", "enum", "type"):
            if parent_class:
                # Nested class — track parent so we can qualify references
                self._nested_class_parent[name] = parent_class
            else:
                self._class_to_module[name] = module_name
                self._module_classes[module_name].add(name)

            # Index enum members for default resolution
            if node_type == "enum" and node.get("members"):
                for mname, mval in node["members"].items():
                    self._enum_lookup[f"{module_name}.{name}.{mname}"] = mval

            # Detect vector types from iterable flag on class nodes
            if node_type == "class":
                if node.get("iterable"):
                    self._vector_types.add(name)
                element_repr = node.get("element_repr")
                if element_repr:
                    m = re.match(r"<class '(?:[\w.]+\.)?(\w+)'>", element_repr)
                    if m:
                        self._vector_element_fallback[name] = m.group(1)

            # Recurse into children
            for child in node.get("children", []):
                self._index_node(child, module_name, parent_class=parent_class or name)

    # ------------------------------------------------------------------
    # Phase 2: Generation
    # ------------------------------------------------------------------

    def generate(self) -> None:
        """Main entry point: index, then generate all stub files."""
        self._build_indexes()

        if exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        makedirs(self.output_dir)

        module_names: list[str] = []
        for module_node in self.tree.get("children", []):
            module_name = module_node["name"]
            module_names.append(module_name)
            self._write_module(module_node)

        self._write_top_init(module_names)

        # PEP 561 marker
        with open(join(self.output_dir, "py.typed"), "w") as f:
            pass

    def _write_module(self, module_node: dict) -> None:
        """Write one namespace module as a package directory."""
        module_name = module_node["name"]
        module_dir = join(self.output_dir, module_name)
        makedirs(module_dir)

        main_class, init_nodes = self._split_main_class(module_node)

        if main_class is not None:
            self._write_class_file(module_name, main_class, module_dir)
            self._write_init_file(module_name, init_nodes, module_dir, import_main=True)
        else:
            self._write_init_file(module_name, init_nodes, module_dir, import_main=False)

    def _split_main_class(self, module_node: dict) -> tuple[dict | None, list[dict]]:
        """Split children into main-class node and remaining init-level nodes.

        The main class is a direct child class whose name matches the module name.
        """
        module_name = module_node["name"]
        main_class = None
        init_nodes: list[dict] = []

        for child in module_node.get("children", []):
            if child.get("ref"):
                continue
            if (
                child.get("type") == "class"
                and child.get("name") == module_name
                and main_class is None
            ):
                main_class = child
            else:
                init_nodes.append(child)

        return main_class, init_nodes

    # ------------------------------------------------------------------
    # File writers
    # ------------------------------------------------------------------

    def _write_class_file(self, module_name: str, main_class_node: dict, module_dir: str) -> None:
        """Write {Module}/{Module}.pyi containing the main class."""
        buf = StringIO()
        path = f"Live.{module_name}"
        self._render_class(main_class_node, buf, indent=0, path=path)

        body = buf.getvalue()

        # Collect names defined in this file (the main class + its nested classes)
        defined_names = self._collect_defined_names(main_class_node)

        type_checking_block = self._build_type_checking_block(
            body, module_name, defined_names, is_class_file=True
        )

        out_file = join(module_dir, f"{module_name}.pyi")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(_HEADER)
            if type_checking_block:
                f.write(f"\n{type_checking_block}\n")
            f.write(body)
            f.write(f"\n\n__all__ = [{module_name!r}]\n")

    def _write_init_file(
        self,
        module_name: str,
        nodes: list[dict],
        module_dir: str,
        *,
        import_main: bool,
    ) -> None:
        """Write {Module}/__init__.pyi with helper classes, enums, and functions."""
        buf = StringIO()
        exports: list[str] = []

        if import_main:
            exports.append(module_name)

        mod_path = f"Live.{module_name}"
        for node in nodes:
            node_type = node.get("type", "")
            if node_type == "class":
                self._render_class(node, buf, indent=0, path=mod_path)
                exports.append(node["name"])
            elif node_type == "enum":
                self._render_enum(node, buf, indent=0)
                exports.append(node["name"])
            elif node_type == "type":
                self._render_type_node(node, buf, indent=0)
                exports.append(node["name"])
            elif node_type == "function":
                func_path = f"{mod_path}.{node['name']}"
                self._render_function(node, buf, indent=0, is_method=False, path=func_path)
                exports.append(node["name"])

        body = buf.getvalue()

        defined_names = set(exports)
        type_checking_block = self._build_type_checking_block(
            body, module_name, defined_names, is_class_file=False
        )

        # Use vector header if this module defines any vector types
        has_vectors = any(n.get("name", "") in self._vector_types for n in nodes if n.get("type") == "class")
        header = _VECTOR_HEADER if has_vectors else _HEADER

        out_file = join(module_dir, "__init__.pyi")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(header)
            if import_main:
                f.write(f"from .{module_name} import {module_name}\n")
            if type_checking_block:
                f.write(f"\n{type_checking_block}\n")
            f.write(body)
            f.write(f"\n\n__all__ = {exports!r}\n")

    def _write_top_init(self, module_names: list[str]) -> None:
        """Write Live/__init__.pyi that imports all submodules."""
        out_file = join(self.output_dir, "__init__.pyi")
        with open(out_file, "w", encoding="utf-8") as f:
            for name in module_names:
                f.write(f"from . import {name}\n")
            f.write(f"\n__all__ = {module_names!r}\n")

    # ------------------------------------------------------------------
    # Node renderers
    # ------------------------------------------------------------------

    def _render_class(self, node: dict, buf: StringIO, indent: int, path: str = "") -> None:
        """Render a class node and its non-ref children."""
        name = node["name"]
        class_path = f"{path}.{name}" if path else name
        pad = "    " * indent

        # Determine base class for vector types
        base = self._vector_base(name, node)
        if base:
            buf.write(f"\n\n{pad}class {name}({base}):")
        else:
            buf.write(f"\n\n{pad}class {name}:")
        doc = node.get("description") or node.get("raw_doc")
        has_body = False

        if doc:
            self._write_docstring(doc, buf, indent + 1)
            has_body = True

        # Render __init__ for constructable classes
        if node.get("constructable") and node.get("init_doc"):
            self._render_init(node, buf, indent + 1, containing_class=name)
            has_body = True

        # Render dunder methods for the base Vector class
        if name == "Vector" and base == "Generic[T]":
            self._render_vector_dunders(buf, indent + 1)
            has_body = True

        # Render children
        children = [c for c in node.get("children", []) if not c.get("ref")]
        if children:
            self._render_children(children, buf, indent + 1, path=class_path, containing_class=name)
            has_body = True

        if not has_body:
            buf.write(f"\n{pad}    ...")

    def _render_init(self, node: dict, buf: StringIO, indent: int, containing_class: str = "") -> None:
        """Parse init_doc and render an __init__ method for constructable classes."""
        init_doc = node.get("init_doc", "")
        if not init_doc:
            return

        # Extract the signature line (first line starting with __init__)
        sig_line = ""
        for line in init_doc.strip().split("\n"):
            line = line.strip()
            if line.startswith("__init__"):
                sig_line = line
                break

        if not sig_line:
            return

        # Parse args from the signature
        args = list(_INIT_ARG_RE.finditer(sig_line))
        if not args:
            return

        pad = "    " * indent

        # Build arg list, skipping the first (object)arg1 which is self
        formatted_args = ["self"]
        for i, m in enumerate(args):
            if i == 0 and m.group(1) == "object" and m.group(2) == "arg1":
                continue  # Skip implicit self
            arg_type = self._resolve_probed_type(m.group(1), containing_class=containing_class)
            arg_name = m.group(2)
            default = m.group(3)
            if default is not None:
                formatted_args.append(f"{arg_name}: {arg_type} = {default}")
            else:
                formatted_args.append(f"{arg_name}: {arg_type}")

        args_str = ", ".join(formatted_args)
        buf.write(f"\n\n{pad}def __init__({args_str}) -> None: ...")

    def _render_enum(self, node: dict, buf: StringIO, indent: int) -> None:
        """Render an enum node as a class with int attributes."""
        name = node["name"]
        pad = "    " * indent

        buf.write(f"\n\n{pad}class {name}:")
        doc = node.get("raw_doc")
        if doc:
            self._write_docstring(doc, buf, indent + 1)

        members = node.get("members", {})
        if members:
            for mname, mval in sorted(members.items(), key=lambda x: x[1]):
                buf.write(f"\n{pad}    {mname}: int = {mval}")
        else:
            buf.write(f"\n{pad}    ...")

    def _render_function(
        self, node: dict, buf: StringIO, indent: int, *, is_method: bool, path: str = ""
    ) -> None:
        """Render a function/method node."""
        name = node["name"]
        pad = "    " * indent

        # Build args
        args = node.get("args", [])
        formatted_args: list[str] = []
        for arg in args:
            formatted_args.append(self._format_arg(arg))

        args_str = ", ".join(formatted_args)

        # Return type
        returns = node.get("returns")
        ret_type = returns["type"] if returns and returns.get("type") else "None"

        buf.write(f"\n\n{pad}def {name}({args_str}) -> {ret_type}:")

        doc = node.get("description")
        if doc:
            self._write_docstring(doc, buf, indent + 1)

        buf.write(f"\n{pad}    ...")

    def _render_property(
        self, node: dict, buf: StringIO, indent: int, path: str = "", containing_class: str = "",
    ) -> None:
        """Render a property node with optional setter."""
        name = node["name"]
        pad = "    " * indent

        probed_type = node.get("probed_type")
        probed_repr = node.get("probed_repr", "")
        type_str = (
            self._resolve_probed_type(
                probed_type, containing_class=containing_class, probed_repr=probed_repr,
            )
            if probed_type else None
        )

        # For generic vector bases (Vector, ObjectVector), parameterize with the
        # property's element type. For specialized vectors (MidiNoteVector), keep the
        # concrete class name — the class def already extends Vector[T].
        _GENERIC_VECTORS = {"Vector", "ObjectVector"}
        if type_str and type_str in _GENERIC_VECTORS:
            element_repr = node.get("element_repr")
            if element_repr:
                m = re.match(r"<class '(?:[\w.]+\.)?(\w+)'>", element_repr)
                if m:
                    elem = self._resolve_probed_type(
                        m.group(1), containing_class=containing_class, probed_repr=element_repr,
                    )
                    if elem:
                        type_str = f"Vector[{elem}]"

        if type_str == "tuple":
            element_repr = node.get("element_repr")
            if element_repr:
                m = re.match(r"<class '(?:[\w.]+\.)?(\w+)'>", element_repr)
                if m:
                    elem = self._resolve_probed_type(
                        m.group(1), containing_class=containing_class, probed_repr=element_repr,
                    )
                    if elem:
                        type_str = f"tuple[{elem}, ...]"

        # Getter
        ret_annotation = f" -> {type_str}" if type_str else ""
        buf.write(f"\n\n{pad}@property")
        buf.write(f"\n{pad}def {name}(self){ret_annotation}:")

        doc = node.get("raw_doc")
        if doc:
            self._write_docstring(doc, buf, indent + 1)

        buf.write(f"\n{pad}    ...")

        # Setter
        if node.get("settable") and type_str:
            buf.write(f"\n\n{pad}@{name}.setter")
            buf.write(f"\n{pad}def {name}(self, value: {type_str}) -> None: ...")

    def _render_str_const(self, node: dict, buf: StringIO, indent: int) -> None:
        """Render a string constant (e.g. Variants members)."""
        name = node["name"]
        pad = "    " * indent

        # Value comes as "'Beta'" — strip outer quotes and re-emit
        raw_value = node.get("value", "")
        if raw_value.startswith("'") and raw_value.endswith("'"):
            value = raw_value[1:-1]
        elif raw_value.startswith('"') and raw_value.endswith('"'):
            value = raw_value[1:-1]
        else:
            value = raw_value

        buf.write(f'\n{pad}{name}: str = "{value}"')

    def _render_type_node(self, node: dict, buf: StringIO, indent: int) -> None:
        """Render a type node (e.g. LimitationError as an Exception subclass)."""
        name = node["name"]
        pad = "    " * indent

        buf.write(f"\n\n{pad}class {name}(Exception): ...")

    def _render_children(
        self, children: list[dict], buf: StringIO, indent: int, path: str = "",
        containing_class: str = "",
    ) -> None:
        """Render a list of child nodes, dispatching by type."""
        for child in children:
            if child.get("ref"):
                continue

            child_name = child.get("name", "")
            child_path = f"{path}.{child_name}" if path else child_name
            node_type = child.get("type", "")
            if node_type == "class":
                self._render_class(child, buf, indent, path=path)
            elif node_type == "enum":
                self._render_enum(child, buf, indent)
            elif node_type == "function":
                self._render_function(child, buf, indent, is_method=True, path=child_path)
            elif node_type == "property":
                self._render_property(child, buf, indent, path=child_path, containing_class=containing_class)
            elif node_type == "str":
                self._render_str_const(child, buf, indent)
            elif node_type == "type":
                self._render_type_node(child, buf, indent)

    # ------------------------------------------------------------------
    # Type resolution
    # ------------------------------------------------------------------

    def _resolve_probed_type(
        self, probed_type: str | None, *, containing_class: str = "", probed_repr: str = "",
    ) -> str:
        """Map a probed type name to a Python type annotation.

        If the type is a nested class (e.g. View), qualify it with the parent class
        (e.g. Device.View) — unless the containing class defines that nested class itself.
        Uses probed_repr (e.g. "<class 'Device.View'>") for precise parent resolution.
        """
        if not probed_type:
            return "None"
        resolved = "None" if probed_type == "NoneType" else probed_type
        if resolved in self._nested_class_parent:
            # Extract parent from probed_repr if available (e.g. "<class 'Device.View'>" -> "Device")
            parent = None
            if probed_repr:
                inner = probed_repr.strip("<>").removeprefix("class ").strip("'\"")
                if "." in inner:
                    parent = inner.rsplit(".", 1)[0]
            # Fall back to the indexed parent
            if not parent:
                parent = self._nested_class_parent[resolved]
            if parent != containing_class:
                resolved = f"{parent}.{resolved}"
        return resolved

    def _format_arg(self, arg: dict) -> str:
        """Format a function argument for the stub signature."""
        name = arg["name"]
        if name == "self":
            return "self"

        arg_type = arg.get("type", "object")
        default = arg.get("default")

        # When default references an enum, widen type to accept both enum and int
        if default and arg_type == "int" and "." in str(default):
            parts = str(default).split(".")
            if len(parts) == 3:
                enum_class = parts[1]
                # Check if the enum class is known
                if enum_class in self._class_to_module:
                    arg_type = f"{enum_class} | int"

        # When default is None, widen type to accept None
        if str(default) == "None" and "None" not in arg_type:
            arg_type = f"{arg_type} | None"

        s = f"{name}: {arg_type}"
        if default is not None:
            s += f" = {self._resolve_default(str(default))}"
        return s

    def _resolve_default(self, default: str) -> str:
        """Resolve a default value, replacing enum references with their int value."""
        if "." not in default:
            return default
        # Check if it's a float (not an enum reference)
        try:
            float(default)
            return default
        except ValueError:
            pass

        val = self._enum_lookup.get(default)
        if val is not None:
            return str(val)
        return default

    # ------------------------------------------------------------------
    # TYPE_CHECKING imports
    # ------------------------------------------------------------------

    def _build_type_checking_block(
        self,
        body: str,
        module_name: str,
        defined_names: set[str],
        *,
        is_class_file: bool,
    ) -> str:
        """Scan body for type references and build an `if TYPE_CHECKING:` import block."""
        # Find all capitalized identifiers that could be class references
        referenced = set(_TYPE_REF_RE.findall(body))

        # Filter to known Live API classes/enums
        referenced &= self._class_to_module.keys()

        # Remove stdlib/builtin names
        referenced -= _SKIP_NAMES

        # Remove names defined in this file
        referenced -= defined_names

        if not referenced:
            return ""

        sibling_imports: list[str] = []
        cross_imports: dict[str, list[str]] = {}

        for cls in sorted(referenced):
            source_module = self._class_to_module[cls]
            if source_module == module_name:
                if is_class_file:
                    sibling_imports.append(cls)
                # For __init__.pyi, skip — name is defined locally
            else:
                cross_imports.setdefault(source_module, []).append(cls)

        if not sibling_imports and not cross_imports:
            return ""

        lines = ["if TYPE_CHECKING:"]
        if sibling_imports:
            lines.append(f"    from . import {', '.join(sorted(sibling_imports))}")
        for mod in sorted(cross_imports):
            names = ", ".join(sorted(cross_imports[mod]))
            lines.append(f"    from Live.{mod} import {names}")

        return "\n".join(lines) + "\n"

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _collect_defined_names(self, node: dict) -> set[str]:
        """Collect all class/enum names defined within a node (including nested)."""
        names = set()
        if node.get("type") in ("class", "enum", "type"):
            names.add(node["name"])
        for child in node.get("children", []):
            if not child.get("ref"):
                names.update(self._collect_defined_names(child))
        return names

    def _render_vector_dunders(self, buf: StringIO, indent: int) -> None:
        """Render dunder methods for the base Vector(Generic[T]) class."""
        pad = "    " * indent
        buf.write(f"\n\n{pad}def __iter__(self) -> Iterator[T]: ...")
        buf.write(f"\n\n{pad}@overload")
        buf.write(f"\n{pad}def __getitem__(self, index: int) -> T: ...")
        buf.write(f"\n\n{pad}@overload")
        buf.write(f"\n{pad}def __getitem__(self, index: slice) -> Vector[T]: ...")
        buf.write(f"\n\n{pad}def __getitem__(self, index: int | slice) -> T | Vector[T]: ...")
        buf.write(f"\n\n{pad}def __len__(self) -> int: ...")
        buf.write(f"\n\n{pad}def __contains__(self, value: object) -> bool: ...")
        buf.write(f"\n\n{pad}def __bool__(self) -> bool: ...")

    def _vector_base(self, name: str, node: dict) -> str:
        """Return the base class string for vector types, or empty string for non-vectors."""
        if name not in self._vector_types:
            return ""
        if name == "Vector":
            return "Generic[T]"
        # Specialized vector: derive element type from fallback map (built during indexing)
        elem = self._vector_element_fallback.get(name)
        if elem:
            return f"Vector[{elem}]"
        return "Vector"

    def _write_docstring(self, doc: str, buf: StringIO, indent: int) -> None:
        """Write a docstring at the given indent level."""
        pad = "    " * indent
        lines = doc.strip().split("\n")
        if len(lines) == 1:
            buf.write(f'\n{pad}"""{lines[0].strip()}"""')
        else:
            buf.write(f'\n{pad}"""')
            for line in lines:
                stripped = line.strip()
                if stripped:
                    buf.write(f"\n{pad}{stripped}")
                else:
                    buf.write("")
            buf.write(f'\n{pad}"""')


def main():
    parser = argparse.ArgumentParser(description="Generate .pyi stub files from LiveTree.resolved.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument(
        "--input", help="Path to LiveTree.resolved.json (default: stubs/{version}/pipeline/LiveTree.resolved.json)"
    )
    parser.add_argument("--output", help="Output directory (default: stubs/{version}/Live)")
    args = parser.parse_args()

    input_path = args.input or join("stubs", args.version, "pipeline", "LiveTree.resolved.json")
    output_dir = args.output or join("stubs", args.version, "Live")

    with open(input_path) as f:
        data = json.load(f)

    generator = StubGenerator(data["tree"], output_dir)
    generator.generate()
    print(f"Stubs written to {abspath(output_dir)}")


if __name__ == "__main__":
    main()

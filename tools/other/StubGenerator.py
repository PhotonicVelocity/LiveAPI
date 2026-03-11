import io
import json
import codecs
import re
import shutil
from typing import IO, List, Optional
from os import makedirs
from os.path import abspath, join, exists

# Map probe runtime_type values to Python type annotation strings.
# Live API class names pass through as-is (they reference sibling classes in the stub package).
# Vector types map to tuple[element, ...] since Live vectors are immutable sequences.
_TYPE_MAP: dict[str, str] = {
    # Primitives
    "bool": "bool",
    "int": "int",
    "float": "float",
    "str": "str",
    "NoneType": "None",
    # Vector types -> tuple[element, ...]
    "Vector": "tuple",
    "StringVector": "tuple[str, ...]",
    "IntVector": "tuple[int, ...]",
    "BrowserItemVector": "tuple[BrowserItem, ...]",
    "RoutingChannelVector": "tuple[RoutingChannel, ...]",
    "RoutingTypeVector": "tuple[RoutingType, ...]",
    "ObjectVector": "tuple[object, ...]",
    "UnavailableFeatureVector": "tuple[UnavailableFeature, ...]",
    "ATimeableValueVector": "tuple[DeviceParameter, ...]",
    "WarpMarkerVector": "tuple[WarpMarker, ...]",
    "BrowserItemIterator": "BrowserItemIterator",
    "RoutingChannelLayout": "RoutingChannelLayout",
}

_HEADER = "from __future__ import annotations\nfrom typing import TYPE_CHECKING, Callable\n"

# Regex to find bare class-name references in type annotations.
# Matches word-boundary class names that appear in type contexts (after ->, in tuple[...], as arg types).
_TYPE_REF_RE = re.compile(r"\b([A-Z][A-Za-z0-9]+)\b")


class StubGenerator:
    script_dir: str
    version: str
    probe_data: dict

    def __init__(self, script_dir: str, version: str):
        self.script_dir = script_dir
        self.version = version
        self.probe_data = self._load_probe_data()
        self._current_class_key: Optional[str] = None
        self._pending_listeners: List[str] = []
        self._pending_listener_indent: str = ""
        self._seen_methods: set[str] = set()
        self._enum_lookup: dict[str, int] = {}
        self._enum_lookup_classes: set[str] = set()
        self._module_classes: dict[str, set[str]] = {}  # module -> set of class names defined in it
        self._class_to_module: dict[str, str] = {}  # class name -> module name

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _load_probe_data(self) -> dict:
        """Load probe_results.json if available."""
        probe_file = join(self.script_dir, "probe_results.json")
        if exists(probe_file):
            try:
                with open(probe_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: could not load probe data: {e}")
        return {}

    def _load_capture(self, path: str) -> Optional[dict]:
        """Load Live.json capture file."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading capture file '{path}': {e}")
            return None

    # ------------------------------------------------------------------
    # Probe helpers
    # ------------------------------------------------------------------

    def _get_probe_info(self, class_name: str, prop_name: str) -> Optional[dict]:
        """Look up probe data for a property. class_name is like 'Live.Song.Song'."""
        key = class_name.replace("Live.", "", 1) if class_name.startswith("Live.") else class_name
        class_data = self.probe_data.get(key, {})
        return class_data.get("properties", {}).get(prop_name)

    def _get_probe_class(self, class_name: str) -> Optional[dict]:
        """Look up probe data for a class."""
        key = class_name.replace("Live.", "", 1) if class_name.startswith("Live.") else class_name
        return self.probe_data.get(key)

    def _format_return_type(self, probe_info: dict) -> str:
        """Convert probe runtime_type to a type annotation string."""
        rt = probe_info.get("runtime_type", "")
        if not rt:
            return "None"
        if rt in _TYPE_MAP:
            return _TYPE_MAP[rt]
        if rt == "Vector":
            elem = probe_info.get("runtime_element_type", "")
            if elem and elem != "(empty)":
                return f"tuple[{elem}, ...]"
            return "tuple"
        return rt

    # ------------------------------------------------------------------
    # Top-level entry point
    # ------------------------------------------------------------------

    def generate(self):
        in_file = abspath(join(self.script_dir, "Live.json"))
        out_dir = abspath(join(self.script_dir, "Live"))

        if exists(out_dir):
            shutil.rmtree(out_dir)
        makedirs(out_dir)

        data = self._load_capture(in_file)
        if data is None:
            return

        elements = data["elements"]
        self._build_enum_lookup(elements)
        modules = self._group_by_module(elements)
        self._build_class_maps(elements)

        # Write each submodule
        module_names = []
        for module_name, module_elements in modules.items():
            module_names.append(module_name)
            self._write_module(module_name, module_elements, out_dir)

        # Top-level Live/__init__.py
        with codecs.open(join(out_dir, "__init__.py"), "w", "utf-8") as f:
            for name in module_names:
                f.write(f"from . import {name}\n")
            f.write(f"\n__all__ = {module_names!r}\n")

        # PEP 561 marker
        with open(join(out_dir, "py.typed"), "w") as f:
            f.write("")

    def _build_enum_lookup(self, elements: list[dict]):
        """Build lookup table: 'Song.CaptureMode.all' -> 0, for resolving default values."""
        for el in elements:
            if el.get("enum") and el.get("enum_values"):
                name = el["name"]  # e.g. 'Live.Application.MessageButtons'
                parts = name.split(".")
                if len(parts) >= 3:
                    key_prefix = ".".join(parts[1:])  # 'Application.MessageButtons'
                    self._enum_lookup_classes.add(key_prefix)
                    for vname, vval in el["enum_values"].items():
                        self._enum_lookup[f"{key_prefix}.{vname}"] = vval

    def _build_class_maps(self, elements: list[dict]):
        """Build module_classes and class_to_module maps for TYPE_CHECKING import resolution."""
        for el in elements:
            name = el.get("name", "")
            kind = el.get("kind", "")
            if kind in ("Class", "Sub-Class") and name.count(".") == 2:
                parts = name.split(".")
                module = parts[1]
                cls = parts[2]
                self._module_classes.setdefault(module, set()).add(cls)
                self._class_to_module[cls] = module

    # ------------------------------------------------------------------
    # Module grouping
    # ------------------------------------------------------------------

    def _group_by_module(self, elements: list[dict]) -> dict[str, list[dict]]:
        """Group elements by top-level module (e.g., 'Live.Song' -> 'Song')."""
        modules: dict[str, list[dict]] = {}
        current_module: Optional[str] = None

        for el in elements:
            name = el.get("name")
            if name is None or name == "Live":
                continue

            if el["kind"] == "Module":
                parts = name.split(".")
                if len(parts) == 2:
                    current_module = parts[1]
                    modules[current_module] = []

            if current_module is not None:
                modules[current_module].append(el)

        return modules

    # ------------------------------------------------------------------
    # Per-module output
    # ------------------------------------------------------------------

    def _write_module(self, module_name: str, elements: list[dict], out_dir: str):
        """Write Live/{module_name}/__init__.py and optionally {module_name}.py."""
        module_dir = join(out_dir, module_name)
        makedirs(module_dir)

        # Determine if there's a main class (same name as module)
        has_main_class = any(
            el["kind"] in ("Class", "Sub-Class")
            and el.get("name", "").split(".")[-1] == module_name
            and el.get("name", "").count(".") == 2  # Live.Song.Song depth
            for el in elements
        )

        if has_main_class:
            # Split: main class + its members -> {Module}.py, rest -> __init__.py
            main_elements, init_elements = self._split_main_class(module_name, elements)
            self._write_class_file(module_name, main_elements, module_dir)
            self._write_init_file(module_name, init_elements, module_dir, import_main=True)
        else:
            # Everything in __init__.py
            self._write_init_file(module_name, elements, module_dir, import_main=False)

    def _split_main_class(
        self, module_name: str, elements: list[dict]
    ) -> tuple[list[dict], list[dict]]:
        """Split elements into main-class elements and init elements.

        The main class (e.g. Live.Song.Song) and all its members/nested classes
        go into the class file. Everything else (module-level functions, helper
        classes, enums) goes into __init__.py.
        """
        main_prefix = f"Live.{module_name}.{module_name}"
        main_elements: list[dict] = []
        init_elements: list[dict] = []

        for el in elements:
            name = el.get("name", "")
            # The main class itself, or anything nested under it
            if name == main_prefix or name.startswith(main_prefix + "."):
                main_elements.append(el)
            else:
                init_elements.append(el)

        return main_elements, init_elements

    def _write_class_file(self, module_name: str, elements: list[dict], module_dir: str):
        """Write {Module}/{Module}.py containing the main class."""
        out_file = join(module_dir, f"{module_name}.py")

        # Write body to buffer first so we can scan for type references
        buf = io.StringIO()
        exports: list[str] = []

        for el in elements:
            name = el.get("name", "")
            kind = el.get("kind", "")
            if kind in ("Class", "Sub-Class") and name == f"Live.{module_name}.{module_name}":
                exports.append(module_name)
            self._write_element(el, buf, module_name)
        self._flush_listeners(buf)

        body = buf.getvalue()
        type_checking_block = self._build_type_checking_block(body, module_name, is_class_file=True)

        with codecs.open(out_file, "w", "utf-8") as f:
            f.write(_HEADER)
            if type_checking_block:
                f.write(f"\n{type_checking_block}\n")
            f.write(body)
            f.write(f"\n\n__all__ = {exports!r}\n")

    def _write_init_file(
        self, module_name: str, elements: list[dict], module_dir: str, *, import_main: bool
    ):
        """Write {Module}/__init__.py with helper classes and re-exports."""
        out_file = join(module_dir, "__init__.py")

        # Write body to buffer first so we can scan for type references
        buf = io.StringIO()
        exports: list[str] = []
        if import_main:
            exports.append(module_name)

        for el in elements:
            name = el.get("name", "")
            kind = el.get("kind", "")
            if kind in ("Class", "Sub-Class") and name.count(".") == 2:
                short = name.split(".")[-1]
                exports.append(short)
            elif kind == "Built-In" and name.count(".") == 2:
                short = name.split(".")[-1]
                if "(" in short:
                    short = short.split("(")[0]
                exports.append(short)

            if kind == "Module":
                continue
            self._write_element(el, buf, module_name)
        self._flush_listeners(buf)

        body = buf.getvalue()
        # Names defined in this __init__.py: all exports except the main class (imported from .py file)
        defined_names = set(exports)
        type_checking_block = self._build_type_checking_block(
            body, module_name, is_class_file=False, defined_names=defined_names
        )

        with codecs.open(out_file, "w", "utf-8") as f:
            f.write(_HEADER)
            if import_main:
                f.write(f"from .{module_name} import {module_name}\n")
            if type_checking_block:
                f.write(f"\n{type_checking_block}\n")
            f.write(body)
            f.write(f"\n\n__all__ = {exports!r}\n")

    # ------------------------------------------------------------------
    # Element writing
    # ------------------------------------------------------------------

    def _write_element(self, el: dict, f: IO[str], module_name: str):
        """Write a single element to a stub file.

        Indent is relative to the module — a class like Live.Song.Song is at
        indent 0, its members at indent 1, nested View at indent 1, View
        members at indent 2, etc.
        """
        kind = el.get("kind")
        name = el.get("name")
        if kind is None or name is None or name == "Live":
            return

        parts = name.split(".")
        # depth relative to module: Live.Song.X = 0, Live.Song.Song.x = 1, etc.
        depth = len(parts) - 2  # subtract "Live" and module name

        # Module-level functions and top-level classes are at depth 1 -> indent 0
        if kind == "Built-In" and depth == 1:
            depth = 0
        elif kind in ("Class", "Sub-Class") and depth == 1:
            depth = 0
        elif depth >= 2:
            depth -= 1

        indent = "    " * depth
        short_name = parts[-1]
        if "(" in short_name:
            short_name = short_name.split("(")[0]
        if not short_name:
            return

        print(f"Generating {kind} '{name}'")

        if kind == "Module":
            return

        elif kind in ("Class", "Sub-Class"):
            self._flush_listeners(f)
            self._seen_methods = set()

            if len(parts) >= 2:
                self._current_class_key = ".".join(parts[1:])

            if el.get("enum"):
                self._write_enum_class(f, indent, short_name, el.get("enum_values", {}), el.get("doc"))
                return

            probe_class = self._get_probe_class(name)
            if probe_class and probe_class.get("likely_enum"):
                self._write_enum_class(
                    f, indent, short_name, probe_class.get("enum_values", {}), el.get("doc")
                )
                return

            if probe_class:
                self._pending_listeners = probe_class.get("listeners", [])
                self._pending_listener_indent = indent + "    "
            else:
                self._pending_listeners = []

            doc = el.get("doc")
            f.write(f"\n\n{indent}class {short_name}:\n")
            if doc:
                f.write(f'{indent}    """\n{indent}    {doc}\n    {indent}"""\n')
            else:
                # Ensure valid syntax for classes with no doc and potentially no members
                f.write(f"{indent}    ...\n")

        elif kind == "Built-In":
            args = el.get("args")
            ret = el.get("returns")
            doc = el.get("doc")

            f.write(f"\n\n{indent}def {short_name}(")
            if args:
                args_str = ", ".join(self._format_arg(a) for a in args)
                f.write(args_str)
            f.write(f") -> {ret or 'None'}:\n")

            if doc:
                f.write(f'{indent}    """\n{indent}    {doc}\n    {indent}"""\n')
            f.write(f"{indent}    ...\n")

        elif kind == "Method":
            self._seen_methods.add(short_name)
            args = el.get("args")
            ret = el.get("returns")
            doc = el.get("doc")

            is_listener = (
                (short_name.startswith("add_") or short_name.startswith("remove_"))
                and short_name.endswith("_listener")
            ) or short_name.endswith("_has_listener")
            if args is not None:
                if is_listener:
                    args_str = ", ".join(
                        self._format_listener_arg(a, is_last=(i == len(args) - 1))
                        for i, a in enumerate(args)
                    )
                else:
                    args_str = ", ".join(self._format_arg(a) for a in args)
                f.write(f"\n{indent}def {short_name}(self, {args_str}) -> {ret or 'None'}:\n")
            elif ret is not None:
                f.write(f"\n{indent}def {short_name}(self) -> {ret}:\n")
            else:
                f.write(f"\n{indent}def {short_name}(self, *a, **k) -> None:\n")

            if doc:
                f.write(f'{indent}    """\n{indent}    {doc}\n    {indent}"""\n')
            f.write(f"{indent}    ...\n")

        elif kind in ("Property", "Value"):
            doc = el.get("doc")
            return_type = ""
            probe_info = None
            if self._current_class_key:
                probe_info = self._get_probe_info(self._current_class_key, short_name)
                if probe_info and probe_info.get("runtime_type"):
                    return_type = f" -> {self._format_return_type(probe_info)}"

            f.write(f"\n{indent}@property\n")
            f.write(f"{indent}def {short_name}(self){return_type}:\n")

            if doc:
                f.write(f'{indent}    """\n{indent}    {doc}\n    {indent}"""\n')
            f.write(f"{indent}    ...\n")

            if probe_info and probe_info.get("settable"):
                f.write(f"\n{indent}@{short_name}.setter\n")
                f.write(f"{indent}def {short_name}(self, value) -> None:\n")
                f.write(f"{indent}    ...\n")

    # ------------------------------------------------------------------
    # TYPE_CHECKING imports
    # ------------------------------------------------------------------

    def _build_type_checking_block(
        self,
        body: str,
        module_name: str,
        *,
        is_class_file: bool,
        defined_names: set[str] | None = None,
    ) -> str:
        """Scan body text for type references and build an `if TYPE_CHECKING:` import block.

        For class files (e.g. Song/Song.py):
          - sibling imports come from the module's __init__.py: `from . import X`
          - cross-module imports: `from Live.{Module} import X`

        For __init__.py files:
          - no sibling imports (names are defined locally)
          - cross-module imports: `from Live.{Module} import X`
        """
        # Find all capitalized identifiers that could be class references
        referenced = set(_TYPE_REF_RE.findall(body))

        # Filter to only known Live API classes
        referenced &= self._class_to_module.keys()

        # Remove builtins and standard types that aren't actual imports
        builtins = {"None", "Callable", "IO"}
        referenced -= builtins

        # Names defined in this file don't need importing
        if defined_names:
            referenced -= defined_names

        # For class files, the main class itself is defined here
        if is_class_file:
            referenced.discard(module_name)

        if not referenced:
            return ""

        sibling_imports: list[str] = []
        cross_imports: dict[str, list[str]] = {}  # module -> [class names]

        module_classes = self._module_classes.get(module_name, set())

        for cls in sorted(referenced):
            source_module = self._class_to_module[cls]
            if source_module == module_name:
                # Same module — sibling import
                if is_class_file:
                    sibling_imports.append(cls)
                # For __init__.py, skip — the name is defined locally or imported from .py
            else:
                # Cross-module import
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

    def _flush_listeners(self, f: IO[str]):
        """Write listener method stubs (add/remove/has) for the current class, then clear."""
        if not self._pending_listeners:
            return
        indent = self._pending_listener_indent
        for prop_name in self._pending_listeners:
            if f"add_{prop_name}_listener" in self._seen_methods:
                continue
            f.write(f"\n{indent}def add_{prop_name}_listener(self, listener: Callable) -> None:\n")
            f.write(f"{indent}    ...\n")
            f.write(f"\n{indent}def remove_{prop_name}_listener(self, listener: Callable) -> None:\n")
            f.write(f"{indent}    ...\n")
            f.write(f"\n{indent}def {prop_name}_has_listener(self, listener: Callable) -> bool:\n")
            f.write(f"{indent}    ...\n")
        self._pending_listeners = []

    def _write_enum_class(self, f: IO[str], indent: str, short_name: str,
                          enum_values: dict, doc: Optional[str]):
        """Write an enum-like class with named int values."""
        f.write(f"\n\n{indent}class {short_name}:\n")
        if doc:
            f.write(f'{indent}    """\n{indent}    {doc}\n    {indent}"""\n')
        if enum_values:
            for vname, vval in sorted(enum_values.items(), key=lambda x: x[1]):
                f.write(f"{indent}    {vname}: int = {vval}\n")
        else:
            f.write(f"{indent}    ...\n")

    def _format_arg(self, arg: dict) -> str:
        arg_type = arg["type"]
        default = arg.get("default")
        # When default references an enum (e.g. "Song.CaptureMode.all"),
        # accept both the enum class and raw int since Live supports either
        if default and arg_type == "int" and "." in str(default):
            parts = str(default).split(".")
            if len(parts) == 3 and f"{parts[0]}.{parts[1]}" in self._enum_lookup_classes:
                arg_type = f"{parts[1]} | int"
        s = f"{arg['name']}: {arg_type}"
        if default is not None:
            s += f"={self._resolve_default(default)}"
        return s

    def _format_listener_arg(self, arg: dict, *, is_last: bool = False) -> str:
        # Only rename to "listener" for the last object arg (the actual callback)
        name = "listener" if arg["type"] == "object" and is_last else arg["name"]
        type_str = "Callable" if arg["type"] == "object" and is_last else arg["type"]
        s = f"{name}: {type_str}"
        if "default" in arg:
            s += f"={self._resolve_default(arg['default'])}"
        return s

    def _resolve_default(self, default) -> str:
        """Resolve a default value, replacing qualified enum references with their int value."""
        s = str(default)
        if "." not in s or s.replace(".", "").replace("-", "").replace("e+", "").replace("e-", "").isdigit():
            return s
        # Look up in enum data: "Song.CaptureMode.all" -> 0
        val = self._enum_lookup.get(s)
        if val is not None:
            return str(val)
        return s

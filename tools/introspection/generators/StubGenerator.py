import json
import codecs
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
    "ATimeableValueVector": "tuple[ATimeableValue, ...]",
    "WarpMarkerVector": "tuple[WarpMarker, ...]",
    "BrowserItemIterator": "BrowserItemIterator",
    "RoutingChannelLayout": "RoutingChannelLayout",
}


class StubGenerator:
    script_dir: str
    version: str
    probe_data: dict

    def __init__(self, script_dir: str, version: str):
        self.script_dir = script_dir
        self.version = version
        self.probe_data = self._load_probe_data()
        self._current_class_key: Optional[str] = None
        # Pending listener stubs to flush when the current class ends
        self._pending_listeners: List[str] = []
        self._pending_listener_indent: str = ""
        # Method names already emitted for the current class (to avoid duplicate listeners)
        self._seen_methods: set[str] = set()

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

    def _get_probe_info(self, class_name: str, prop_name: str) -> Optional[dict]:
        """Look up probe data for a property. class_name is like 'Live.Song.Song'."""
        # Probe keys strip the 'Live.' prefix: 'Song.Song'
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
        # Check the map first (covers named vector types like StringVector)
        if rt in _TYPE_MAP:
            return _TYPE_MAP[rt]
        # Generic Vector with probed element type
        if rt == "Vector":
            elem = probe_info.get("runtime_element_type", "")
            if elem and elem != "(empty)":
                return f"tuple[{elem}, ...]"
            return "tuple"
        # Unmapped types pass through as class references (e.g., BrowserItem, Song, Quantization)
        return rt

    def generate(self):
        in_file = abspath(join(self.script_dir, "Live.json"))
        out_dir = abspath(join(self.script_dir, "Live"))
        if not exists(out_dir):
            makedirs(out_dir)

        data = self._load_capture(in_file)
        if data is None:
            return

        elements = data["elements"]

        # Monolithic __init__.py
        with codecs.open(join(out_dir, "__init__.py"), "w", "utf-8") as f:
            f.write("from types import ModuleType\nfrom typing import Callable\n")
            for el in elements:
                self._write_element(el, f)
            self._flush_listeners(f)

        # Per-module class files
        self._generate_per_module(elements, out_dir)

        # PEP 561 marker — tells type checkers this package has inline types
        with open(join(out_dir, "py.typed"), "w") as f:
            f.write("")

    def _load_capture(self, path: str) -> Optional[dict]:
        """Load Live.json capture file."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading capture file '{path}': {e}")
            return None

    def _generate_per_module(self, elements: list[dict], out_dir: str):
        """Write per-module stub files into classes/ subdirectory."""
        classes_dir = join(out_dir, "classes")
        if not exists(classes_dir):
            makedirs(classes_dir)

        # Group elements by top-level module (e.g., "Live.Song" -> "Song")
        modules: dict[str, list[dict]] = {}
        current_module: Optional[str] = None

        for el in elements:
            name = el.get("name")
            if name is None or name == "Live":
                continue

            # Detect top-level module boundaries (e.g., "Live.Song")
            if el["kind"] == "Module" and name is not None:
                parts = name.split(".")
                if len(parts) == 2:  # "Live.Song" — top-level module
                    current_module = parts[1]
                    modules[current_module] = []

            if current_module is not None:
                modules[current_module].append(el)

        # Write each module to its own file
        for module_name, module_elements in modules.items():
            out_file = join(classes_dir, f"{module_name}.py")
            with codecs.open(out_file, "w", "utf-8") as f:
                f.write("from types import ModuleType\nfrom typing import Callable\n")
                for el in module_elements:
                    self._write_element(el, f)
                self._flush_listeners(f)

    def _write_element(self, el: dict, f: IO[str]):
        """Write a single element to a stub file."""
        kind = el.get("kind")
        name = el.get("name")
        if kind is None or name is None or name == "Live":
            return

        level = name.count(".") - 1
        indent = "    " * level
        short_name = name.split(".")[-1]
        if "(" in short_name:
            short_name = short_name.split("(")[0]
        if not short_name:
            return

        print("Generating %s '%s'" % (kind, name))

        if kind == "Module":
            self._flush_listeners(f)
            f.write(f"\n\n{indent}class {short_name}(ModuleType):\n")

        elif kind in ("Class", "Sub-Class"):
            self._flush_listeners(f)
            self._seen_methods = set()

            # Track current class for property probe lookups
            parts = name.split(".")
            if len(parts) >= 2:
                self._current_class_key = ".".join(parts[1:])

            # Check if this is an enum class (from capture data or probe data)
            if el.get("enum"):
                self._write_enum_class(f, indent, short_name, el.get("enum_values", {}), el.get("doc"))
                return

            # Fall back to probe data for enum detection
            probe_class = self._get_probe_class(name)
            if probe_class and probe_class.get("likely_enum"):
                self._write_enum_class(f, indent, short_name, probe_class.get("enum_values", {}), el.get("doc"))
                return

            # Queue listener stubs for this class (flushed when the next class starts or file ends)
            if probe_class:
                self._pending_listeners = probe_class.get("listeners", [])
                self._pending_listener_indent = indent + "    "
            else:
                self._pending_listeners = []

            f.write(f"\n{indent}class {short_name}(object):\n")
            f.write(f"{indent}    def __init__(self, *a, **k):\n")
            indent += "    "
            doc = el.get("doc")
            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    ...\n" % indent)

        elif kind == "Method":
            self._seen_methods.add(short_name)
            args = el.get("args")
            ret = el.get("returns")
            doc = el.get("doc")

            # Listener callbacks: retype the callback arg from object -> Callable
            is_listener = (
                (short_name.startswith("add_") or short_name.startswith("remove_"))
                and short_name.endswith("_listener")
            ) or short_name.endswith("_has_listener")
            if args is not None:
                fmt = self._format_listener_arg if is_listener else self._format_arg
                args_str = ", ".join(fmt(a) for a in args)
                f.write(f"\n{indent}def {short_name}(self, {args_str}) -> {ret or 'None'}:\n")
            elif ret is not None:
                # Signature was parsed but method takes no args beyond self
                f.write(f"\n{indent}def {short_name}(self) -> {ret}:\n")
            else:
                f.write(f"\n{indent}def {short_name}(self, *a, **k) -> None:\n")

            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    ...\n" % indent)

        elif kind == "Built-In":
            args = el.get("args")
            ret = el.get("returns")
            doc = el.get("doc")

            f.write(f"\n{indent}@staticmethod\n")
            if args:
                args_str = ", ".join(self._format_arg(a) for a in args)
                f.write(f"{indent}def {short_name}({args_str}) -> {ret or 'None'}:\n")
            else:
                f.write(f"{indent}def {short_name}() -> {ret or 'None'}:\n")

            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    ...\n" % indent)

        elif kind in ("Property", "Value"):
            doc = el.get("doc")
            # Look up probe data for return type
            return_type = ""
            probe_info = None
            if self._current_class_key:
                probe_info = self._get_probe_info(self._current_class_key, short_name)
                if probe_info and probe_info.get("runtime_type"):
                    return_type = f" -> {self._format_return_type(probe_info)}"

            f.write(f"\n{indent}@property\n")
            f.write(f"{indent}def {short_name}(self){return_type}:\n")

            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    ...\n" % indent)

            # Add setter if property is settable
            if probe_info and probe_info.get("settable"):
                f.write(f"\n{indent}@{short_name}.setter\n")
                f.write(f"{indent}def {short_name}(self, value) -> None:\n")
                f.write("%s    ...\n" % indent)

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
            # Live API convention: X_has_listener (not has_X_listener)
            f.write(f"\n{indent}def {prop_name}_has_listener(self, listener: Callable) -> bool:\n")
            f.write(f"{indent}    ...\n")
        self._pending_listeners = []

    def _write_enum_class(self, f: IO[str], indent: str, short_name: str,
                          enum_values: dict, doc: Optional[str]):
        """Write an enum-like class with named int values."""
        f.write(f"\n{indent}class {short_name}:\n")
        if doc:
            f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
        if enum_values:
            for vname, vval in sorted(enum_values.items(), key=lambda x: x[1]):
                f.write(f"{indent}    {vname}: int = {vval}\n")
        else:
            f.write(f"{indent}    ...\n")

    @staticmethod
    def _format_arg(arg: dict) -> str:
        """Format a structured arg dict into a Python parameter string."""
        s = f"{arg['name']}: {arg['type']}"
        if "default" in arg:
            s += f"={arg['default']}"
        return s

    @staticmethod
    def _format_listener_arg(arg: dict) -> str:
        """Format an arg for a listener method, retyping object -> Callable."""
        type_str = "Callable" if arg["type"] == "object" else arg["type"]
        s = f"{arg['name']}: {type_str}"
        if "default" in arg:
            s += f"={arg['default']}"
        return s

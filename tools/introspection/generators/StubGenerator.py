from io import BytesIO
import json
import re
import codecs
from typing import Callable, IO, List, Optional, Tuple, Union
import xml.etree.ElementTree as ElementTree
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
        in_file = abspath(join(self.script_dir, "Live.xml"))
        out_dir = abspath(join(self.script_dir, "Live"))
        if not exists(out_dir):
            makedirs(out_dir)

        xml = self.parse_xml(in_file)
        if xml is None:
            return

        elements = self._collect_elements(xml)

        # Monolithic __init__.py
        with codecs.open(join(out_dir, "__init__.py"), "w", "utf-8") as f:
            f.write("from types import ModuleType\nfrom typing import Callable\n")
            for tag, name, doc in elements:
                self.generate_code(tag, name, doc, f)
            self._flush_listeners(f)

        # Per-module class files
        self._generate_per_module(elements, out_dir)

        # PEP 561 marker — tells type checkers this package has inline types
        with open(join(out_dir, "py.typed"), "w") as f:
            f.write("")

    def _collect_elements(self, xml) -> List[Tuple[Optional[str], Optional[str], Optional[str]]]:
        """Parse XML into a list of (tag, name, doc) tuples."""
        elements: List[Tuple[Optional[str], Optional[str], Optional[str]]] = []
        last_tag = None
        last_name = None
        last_doc = None
        for element in xml.findall("./*"):
            if element.tag == "Doc":
                last_doc = element.text.strip() if element.text else ""
            else:
                if last_tag is not None:
                    elements.append((last_tag, last_name, last_doc))
                last_doc = None
                last_tag = element.tag
                last_name = element.text.strip() if element.text else ""
        if last_tag is not None:
            elements.append((last_tag, last_name, last_doc))
        return elements

    def _generate_per_module(self, elements, out_dir: str):
        """Write per-module stub files into classes/ subdirectory."""
        classes_dir = join(out_dir, "classes")
        if not exists(classes_dir):
            makedirs(classes_dir)

        # Group elements by top-level module (e.g., "Live.Song" -> "Song")
        modules: dict[str, List[Tuple[Optional[str], Optional[str], Optional[str]]]] = {}
        current_module: Optional[str] = None

        for tag, name, doc in elements:
            if name is None or name == "Live":
                continue

            # Detect top-level module boundaries (e.g., "Live.Song")
            if tag == "Module" and name is not None:
                parts = name.split(".")
                if len(parts) == 2:  # "Live.Song" — top-level module
                    current_module = parts[1]
                    modules[current_module] = []

            if current_module is not None:
                modules[current_module].append((tag, name, doc))

        # Write each module to its own file
        for module_name, module_elements in modules.items():
            out_file = join(classes_dir, f"{module_name}.py")
            with codecs.open(out_file, "w", "utf-8") as f:
                f.write("from types import ModuleType\nfrom typing import Callable\n")
                for tag, name, doc in module_elements:
                    self.generate_code(tag, name, doc, f)
                self._flush_listeners(f)

    def generate_code(self, tag, name, doc, f: IO[str]):
        if doc is not None:
            doc = (
                doc.replace("&gt;", ">")
                .replace("&lt;", "<")
                .replace("&amp;gt;", ">")
                .replace("&amp;lt;", "<")
                .replace("&amp;", "&")
            )
        if tag is not None and name is not None and name != "Live":
            level = name.count(".") - 1
            indent = "    " * level
            short_name = name.split(".")[-1]
            if "(" in short_name:
                short_name = short_name.split("(")[0]
            if not short_name:
                return

            print("Generating %s '%s'" % (tag, name))

            if tag == "Header":
                f.write(f'"""Stub generated for Ableton Live {self.version}"""\n')
                return

            if tag == "Module":
                self._flush_listeners(f)
                f.write(f"\n\n{indent}class {short_name}(ModuleType):\n")

            if tag == "Class" or tag == "Sub-Class":
                # Flush listener stubs for the previous class before starting a new one
                self._flush_listeners(f)
                self._seen_methods = set()

                # Track current class for property probe lookups
                # Build qualified name: for "Live.Song.Song" -> "Song.Song"
                parts = name.split(".")
                if len(parts) >= 2:
                    self._current_class_key = ".".join(parts[1:])

                # Check if this is an enum class (has enum_values in probe, no properties)
                probe_class = self._get_probe_class(name)
                if probe_class and probe_class.get("likely_enum"):
                    self._write_enum_class(f, indent, short_name, probe_class, doc)
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

            if tag == "Method":
                self._seen_methods.add(short_name)
                args, ret, doc = self.parse_args_from_doc(doc)
                if args and len(args) > 0:
                    args.remove(args[0])  # remove first arg because that is "self"
                    f.write(
                        "\n%sdef %s(self, %s) -> %s:\n"
                        % (
                            indent,
                            short_name,
                            ", ".join([self.format_arg(arg) for arg in args]),
                            ret,
                        )
                    )
                    doc = "%s%s" % (doc, self.make_arg_doc(args, ret, indent + "    "))
                else:
                    f.write(
                        "\n%sdef %s(self, *a, **k) -> %s:\n" % (indent, short_name, ret)
                    )

            if tag == "Built-In":
                args, ret, doc = self.parse_args_from_doc(doc)
                f.write(f"\n{indent}@staticmethod\n")
                if args:
                    f.write(
                        f"{indent}def {short_name}({', '.join([self.format_arg(arg) for arg in args])}) -> {ret}:\n"
                    )
                    doc = f"{doc}{self.make_arg_doc(args, ret, indent + '    ')}"
                else:
                    f.write("%sdef %s():\n" % (indent, short_name))

            if tag == "Property" or tag == "Value":
                # Look up probe data for return type
                return_type = ""
                probe_info = None
                if self._current_class_key:
                    probe_info = self._get_probe_info(self._current_class_key, short_name)
                    if probe_info and "runtime_type" in probe_info:
                        return_type = f" -> {self._format_return_type(probe_info)}"

                f.write(f"\n{indent}@property\n")
                f.write(f"{indent}def {short_name}(self){return_type}:\n")

                # Write the doc + body for the getter
                if doc:
                    f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
                f.write("%s    ...\n" % indent)

                # Add setter if property is settable
                if probe_info and probe_info.get("settable"):
                    f.write(f"\n{indent}@{short_name}.setter\n")
                    f.write(f"{indent}def {short_name}(self, value) -> None:\n")
                    f.write("%s    ...\n" % indent)

                return  # Already wrote body above

            if doc:
                f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
            f.write("%s    ...\n" % indent)

    def _flush_listeners(self, f: IO[str]):
        """Write listener method stubs (add/remove/has) for the current class, then clear."""
        if not self._pending_listeners:
            return
        indent = self._pending_listener_indent
        for prop_name in self._pending_listeners:
            # Skip if the XML already defined these listener methods
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

    def _write_enum_class(self, f: IO[str], indent: str, short_name: str, probe_class: dict, doc: Optional[str]):
        """Write an enum-like class with named int values."""
        f.write(f"\n{indent}class {short_name}:\n")
        if doc:
            f.write('{0}    """\n{0}    {1}\n    {0}"""\n'.format(indent, doc))
        enum_values = probe_class.get("enum_values", {})
        if enum_values:
            for vname, vval in sorted(enum_values.items(), key=lambda x: x[1]):
                f.write(f"{indent}    {vname}: int = {vval}\n")
        else:
            f.write(f"{indent}    ...\n")

    def parse_args_from_doc(
        self, doc: Optional[str]
    ) -> Tuple[List[Tuple[str, str, Union[str, None]]], Optional[str], Optional[str]]:
        args: List[Tuple[str, str, Union[str, None]]] = []
        ret: Optional[str] = None
        original_doc = doc

        try:
            if doc and ":" in doc:
                parts = doc.split(":", 1)
                raw_args = re.sub(r"^.*\( (.*)\) -> *([^ ]+) *$", r"\1, \2", parts[0])
                raw_args = raw_args.replace("[", "").replace("]", "").split(", ")
                ret = raw_args[-1]
                for arg in raw_args[:-1]:
                    arg_parts = re.split("[()]", arg)
                    # Use regex to split by "=" and assign to arg_name and arg_default
                    name_default = re.split(r"=", arg_parts[2].strip(), maxsplit=1)
                    arg_name = name_default[0].strip()
                    arg_type = arg_parts[1].strip()

                    args.append((arg_name, arg_type, None))

                doc = parts[1].strip()
        except Exception as e:
            # Be permissive for older Live versions with different doc formats
            print(f"Warning: could not parse args from doc: {e}")
            return [], None, original_doc

        # Sanitize ret — must be a valid Python type expression
        if ret and not re.match(r"^[\w\[\], .]+$", ret):
            ret = None

        return args or [], ret or None, doc or None

    def format_arg(self, arg: Tuple[str, str, Union[str, None]]):
        return f"{arg[0]}: {arg[1]}{'=' + arg[2] if arg[2] is not None else ''}"

    def make_arg_doc(self, args, ret, indent):
        arg_doc = ""
        for arg in args:
            if "=" in arg[0]:
                arg_parts = arg[0].split("=")
                arg_doc = "{0}\n{1}:param {2}: {2} defaults to {4} \n{1}:type {2}: {3}".format(
                    arg_doc, indent, arg_parts[0], arg_parts[1], arg_parts[1]
                )
            else:
                arg_doc = "{0}\n{1}:param {2}: {2}\n{1}:type {2}: {3}".format(
                    arg_doc, indent, arg[0], arg[1]
                )
        if ret:
            arg_doc = "{0}\n{1}:rtype: {2}".format(arg_doc, indent, ret)
        return arg_doc

    def read_file(self, name) -> str:
        with codecs.open(name, "r", "utf-8") as f:
            return f.read()

    def parse_xml(self, file):
        """
        Create and return a namespace-agnostic ElementTree root element.

        :param file: Path to the XML file.
        :return: Root ElementTree.Element or None if parsing fails.
        """
        try:
            text = self.read_file(file)

            tree = ElementTree.iterparse(BytesIO(text.encode("UTF-8")))
            for _, el in tree:
                if "}" in el.tag:
                    el.tag = el.tag.split("}", 1)[1]  # strip all namespaces
            return tree.root.find("Live")  # type: ignore

        except Exception as e:
            print(f"Unexpected error while parsing XML file '{file}': {e}")

        return None

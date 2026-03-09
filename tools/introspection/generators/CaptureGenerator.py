from __future__ import annotations

import inspect
import json
import os
import re
import sys

from ..helpers.app import get_version_number
from .Generator import Generator


class CaptureGenerator(Generator):
    lines = []

    def __init__(self, module, outdir, script_dir):
        super().__init__(
            module,
            outdir,
            script_dir,
            os.path.join(outdir, str(module.__name__) + ".json"),
            header="",
            footer="",
        )
        self._elements: list[dict] = []
        self._version = get_version_number(module)
        self._python_version = sys.version.split(" ")[0]

    def generate(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        self._describe_module(self.module)

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "version": self._version,
                    "python_version": self._python_version,
                    "elements": self._elements,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

    def _clean_doc(self, doc):
        """Normalize whitespace in docstrings."""
        doc = doc.replace("\n", "")
        doc = doc.replace("   ", "")
        return doc

    def _get_doc(self, obj):
        """Get object's doc string with whitespace normalized."""
        if getattr(obj, "__doc__") is not None:
            return self._clean_doc(getattr(obj, "__doc__"))

    def _parse_signature(self, raw_doc):
        """Parse a Boost.Python docstring into structured fields.

        Input format:
            method( (Type)arg1, (Type)arg2 [, (Type)arg3=default]) -> RetType : Description C++ signature :  ...

        Returns a dict with optional keys: args, returns, doc, cpp_signature.
        Returns None if the docstring doesn't match the expected format.
        """
        if not raw_doc:
            return None

        result = {}
        remaining = raw_doc

        # Extract C++ signature if present (take the last occurrence).
        # Boost.Python sometimes concatenates a duplicate signature after the C++ sig;
        # strip all C++ signature blocks to isolate the primary signature.
        cpp_marker = "C++ signature :"
        while cpp_marker in remaining:
            before, cpp_sig = remaining.rsplit(cpp_marker, 1)
            remaining = before.rstrip()
            cpp_sig = cpp_sig.strip()
            if cpp_sig and "cpp_signature" not in result:
                result["cpp_signature"] = cpp_sig

        # Strip trailing " :" left over from the " : C++ signature :" separator
        if remaining.endswith(":"):
            remaining = remaining[:-1].rstrip()

        # Split at first " : " to separate signature from description
        if " : " in remaining:
            sig_part, desc_part = remaining.split(" : ", 1)
            desc_part = desc_part.strip()
            # Clean up any C++ signature remnants leaked into the description
            if cpp_marker in desc_part:
                desc_part = desc_part[:desc_part.index(cpp_marker)].rstrip().rstrip(":")
            if desc_part:
                result["doc"] = desc_part
        else:
            sig_part = remaining

        # Parse: method_name( (Type)arg [, (Type)arg=default]) -> RetType
        # Also handles: method_name() -> RetType (no args)
        sig_match = re.match(r"^[\w]+\(\s*(.*?)\)\s*->\s*(\S+)\s*$", sig_part)
        corrupted_ret = False
        if not sig_match:
            # Boost.Python sometimes concatenates class docstrings onto the return type
            # (e.g., "-> StartupDialogServes as an entry point..."). Try a lenient match.
            sig_match = re.match(r"^[\w]+\(\s*(.*?)\)\s*->\s*(\S+)", sig_part)
            if not sig_match:
                return None
            corrupted_ret = True

        args_str = sig_match.group(1)
        ret = sig_match.group(2)

        # Recover corrupted return type by splitting at the last CamelCase boundary
        # (e.g., "StartupDialogServes" -> "StartupDialog")
        if corrupted_ret:
            for i in range(len(ret) - 1, 0, -1):
                if ret[i - 1].islower() and ret[i].isupper():
                    ret = ret[:i]
                    break

        # Validate return type is a valid identifier
        if ret and re.match(r"^[\w\[\], .]+$", ret):
            result["returns"] = ret

        # Parse individual args: (Type)name or (Type)name=default
        if args_str.strip():
            # Remove optional brackets
            args_str = args_str.replace("[", "").replace("]", "")
            args = []
            for arg_match in re.finditer(r"\((\w+)\)(\w+)(?:=(\S+))?", args_str):
                arg: dict = {"name": arg_match.group(2), "type": arg_match.group(1)}
                if arg_match.group(3):
                    arg["default"] = arg_match.group(3)
                args.append(arg)
            if args:
                result["args"] = args

        return result if result else None

    def _detect_enum(self, obj):
        """Detect if a class is a Boost.Python enum (int subclass with named int values).

        Returns a dict of {name: value} or None if not an enum.
        """
        try:
            if not inspect.isclass(obj):
                return None
            if not issubclass(obj, int):
                return None
            # Collect int-valued class attributes (enum members)
            values = {}
            for attr_name in dir(obj):
                if attr_name.startswith("_"):
                    continue
                try:
                    val = getattr(obj, attr_name)
                except Exception:
                    continue
                if isinstance(val, int) and not callable(val):
                    values[attr_name] = int(val)
            return values if values else None
        except Exception:
            return None

    def _print_obj_info(self, description, obj, name=None):
        """Collect element info into the elements list."""

        obj_name = getattr(obj, "__name__", None)
        recovered_doc = None

        # Boost.Python sometimes concatenates the docstring onto __name__;
        # strip the overlap by checking if __doc__ text appears as a suffix
        if obj_name:
            obj_doc = getattr(obj, "__doc__", None) or ""
            if obj_doc and len(obj_name) > len(obj_doc):
                overlap = obj_name[len(obj_name) - len(obj_doc):]
                if obj_doc.startswith(overlap):
                    obj_name = obj_name[:len(obj_name) - len(obj_doc)]
            # If name had a space and __doc__ is None, Boost.Python concatenated the
            # doc directly into __name__. Split at the last CamelCase boundary
            # (lowercase followed by uppercase) to recover the real class name.
            if " " in obj_name:
                first_word = obj_name.split(" ", 1)[0]
                rest = obj_name[len(first_word):].strip()
                if not obj_doc:
                    for i in range(len(first_word) - 1, 0, -1):
                        if first_word[i - 1].islower() and first_word[i].isupper():
                            rest = first_word[i:] + " " + rest if rest else first_word[i:]
                            first_word = first_word[:i]
                            break
                    if rest:
                        recovered_doc = rest.rstrip(".")
                obj_name = first_word

        # Filter out unnamed Boost.Python functions and special methods
        if obj_name:
            if "<" in obj_name or obj_name.startswith("__"):
                return

        # Determine the name to use
        name_str = obj_name if obj_name is not None else name

        if name_str is None:
            return

        # Handle self.lines stack
        if len(self.lines) != 0:
            assert name_str is not None
            self.lines.append("." + name_str)
            if inspect.ismethod(obj) or inspect.isbuiltin(obj):
                self.lines[-1] += "()"
        else:
            self.lines.append(name_str)

        # Build the dotted name string
        line_str = "".join(self.lines)

        # Build the element dict
        element: dict = {"kind": description, "name": line_str}

        # Get the raw docstring
        raw_doc = self._get_doc(obj) if hasattr(obj, "__doc__") and getattr(obj, "__doc__") else None
        if not raw_doc and recovered_doc:
            raw_doc = self._clean_doc(recovered_doc)

        # For methods and built-ins, parse the signature into structured fields
        if description in ("Method", "Built-In") and raw_doc:
            parsed = self._parse_signature(raw_doc)
            if parsed:
                # Methods: strip the implicit self arg (first arg is always the class itself)
                if description == "Method" and "args" in parsed:
                    parsed["args"] = parsed["args"][1:]
                    if not parsed["args"]:
                        del parsed["args"]
                element.update(parsed)
            else:
                # Parsing failed — store raw doc
                element["doc"] = raw_doc

        # For classes, detect enums
        elif description in ("Class", "Sub-Class"):
            enum_values = self._detect_enum(obj)
            if enum_values is not None:
                element["enum"] = True
                element["enum_values"] = enum_values
            if raw_doc:
                element["doc"] = raw_doc

        # For everything else, store the raw doc
        else:
            if raw_doc:
                element["doc"] = raw_doc

        self._elements.append(element)

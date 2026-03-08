import inspect
import json
import os
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

        # Add docstring if available
        doc = self._get_doc(obj) if hasattr(obj, "__doc__") and getattr(obj, "__doc__") else None
        if doc:
            element["doc"] = doc
        elif recovered_doc:
            element["doc"] = self._clean_doc(recovered_doc)

        self._elements.append(element)

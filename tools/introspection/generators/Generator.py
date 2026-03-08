from codecs import StreamReaderWriter
import codecs
import inspect
import os
from typing import Any, Union
from abc import abstractmethod


class Generator:
    module: Any
    outdir: str
    script_dir: str
    filepath: str
    file: Union[StreamReaderWriter, None] = None
    header: str
    footer: str

    lines = []

    def __init__(self, module, outdir, script_dir, filepath, header="", footer=""):
        self.module = module
        self.outdir = outdir
        self.script_dir = script_dir
        self.filepath = filepath
        self.header = header
        self.footer = footer

    def generate(self):
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        if self.filepath is not None:
            self.file = codecs.open(self.filepath, "w", "utf-8")

        self.write(self.header)
        self._describe_module(self.module)
        self.write(self.footer)

        self.close()

    def write(self, text: str) -> None:
        if text is not None and self.file is not None:
            self.file.write(text)

    def close(self):
        """
        Closes the documentation file.
        """
        if self.file is not None:
            self.file.close()
            self.file = None

    def _describe_obj(self, descr: str, obj):
        """Describe object passed as argument, and identify as Class, Method, Property, Value, or Built-In"""

        # Attempt to get object name via __name__ or __qualname__
        obj_name = getattr(obj, "__name__", getattr(obj, "__qualname__", None))

        if obj_name:
            # Boost.Python sometimes concatenates the docstring onto __name__;
            # strip the overlap by checking if __doc__ text appears as a suffix
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
                if not obj_doc:
                    for i in range(len(first_word) - 1, 0, -1):
                        if first_word[i - 1].islower() and first_word[i].isupper():
                            first_word = first_word[:i]
                            break
                obj_name = first_word
            # Filter out unnamed Boost.Python functions and special methods
            if "<" in obj_name or obj_name.startswith("__"):
                return
            # Filter out non-subclass 'type' and 'class' types
            if obj_name in ("type", "class"):
                return

            # Output initial object information
            self._print_obj_info(descr, obj)

        # If the object is a method or built-in, stop further processing
        if inspect.ismethod(obj) or inspect.isbuiltin(obj):
            if self.lines:
                self.lines.pop()
            return

        try:
            # Retrieve all members of the object, skipping attributes that raise
            members = []
            for name in dir(obj):
                try:
                    members.append((name, getattr(obj, name)))
                except Exception as e:
                    # Older Live versions may throw on attribute access; skip safely
                    print(f"Skipping member {name} on {obj}: {e}")
                    continue

            # Process properties
            for name, member in members:
                if isinstance(member, property):
                    self._print_obj_info("Property", member, name)
                    if self.lines:
                        self.lines.pop()

            # Process methods and functions
            for name, member in members:
                if inspect.isbuiltin(member) or inspect.isfunction(member):
                    self._describe_obj("Method", member)

            # Process subclasses of the current object
            for name, member in members:
                if inspect.isclass(member):
                    # Check if 'member' is a subclass of 'obj'
                    try:
                        if issubclass(member, obj):
                            self._describe_obj("Sub-Class", member)
                        else:
                            self._describe_obj("Class", member)
                    except Exception:
                        # 'obj' may not be a class, or issubclass may fail on older Live versions
                        self._describe_obj("Class", member)

            if self.lines:
                self.lines.pop()

        except Exception as e:
            # Log the exception with more detail without corrupting XML output
            print(f"Error processing object {obj}: {e}")
            return

    def _describe_module(self, module):
        """
        Describe the module object passed as argument
        including its root classes and functions
        """

        self._print_obj_info("Module", module)

        for name in dir(module):  # do the built-ins first
            try:
                obj = getattr(module, name)
            except Exception as e:
                print(f"Skipping module member {name} on {module}: {e}")
                continue
            if inspect.isbuiltin(obj):
                self._describe_obj("Built-In", obj)

        for name in dir(module):  # then the rest
            try:
                obj = getattr(module, name)
            except Exception as e:
                print(f"Skipping module member {name} on {module}: {e}")
                continue
            if inspect.isclass(obj):
                self._describe_obj("Class", obj)
            elif inspect.ismethod(obj) or inspect.isfunction(obj):
                self._describe_obj("Method", obj)
            elif inspect.ismodule(obj):
                self._describe_module(obj)

        if self.lines:
            self.lines.pop()

    @abstractmethod
    def _print_obj_info(self, description: str, obj: Any, name=None):
        """Print object's descriptor and name on one line, and docstring (if any) on the next"""
        pass

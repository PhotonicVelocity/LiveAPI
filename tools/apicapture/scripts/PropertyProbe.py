"""
PropertyProbe — iterative runtime type discovery for the Live API.

Starting from a raw capture tree (LiveTree.raw.json), this module:

1. Builds a repr index — a dict keyed by class repr (e.g. "<class 'Song.Song'>")
   containing each class's properties, getters, path, and completeness status.

2. Seeds initial instances — gets Application from Live (Song is discovered
   naturally via get_document) and constructs any types marked as constructable.

3. Runs a probe loop — picks the next unprobed instance of an incomplete class,
   reads all its properties and no-arg getters to discover runtime types, and
   registers any new objects found. Repeats until every reachable class is complete.

4. Dumps results to LiveClasses.json — the repr index with instance data stripped.
   Pass verbose=True to dump() to include instance data for debugging.

The probe loop is also called by DeviceProbe after each device load, so newly
loaded devices get their types discovered in the same pass.
"""

from __future__ import annotations

import json
import os
from typing import Any

import Live  # type: ignore

# Primitive types that don't need further discovery
_PRIMITIVES = ("int", "float", "str", "bool", "NoneType")


class PropertyProbe:
    def __init__(self, c_instance: Any, outdir: str, log_fn: Any = None):
        self.c_instance = c_instance
        self.outdir = outdir
        self.log = log_fn or (lambda msg: None)
        self._hardcoded_done: set[int] = set()
        self._initialized = False
        self.repr_index: dict[str, dict] = {}

    # --- Public API ---

    def init(self) -> bool:
        """Build repr index from raw capture and seed initial instances. Idempotent."""
        if self._initialized:
            return True

        data = self._load_raw_capture()
        if data is None:
            self.log("PropertyProbe: no raw capture found")
            return False

        self.repr_index = {}
        self._build_repr_index(data["tree"], self.repr_index, "")
        self.log(f"PropertyProbe: {len(self.repr_index)} classes indexed by repr")

        app = Live.Application.get_application()
        self._add_instance(app)

        self._construct_types()

        self._initialized = True
        return True

    def run(self, verbose: bool = False) -> str:
        """Init, probe, and dump. Returns output path."""
        if not self.init():
            return ""
        self._probe_loop()
        return self.dump(verbose=verbose)

    def dump(self, verbose: bool = False) -> str:
        """Write LiveClasses.json. Returns output path.

        Pass verbose=True to include instance data (live pointers, probe status)
        for debugging. By default, instances are stripped from the output.
        """
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        output = {}
        for k, v in self.repr_index.items():
            entry = dict(v)
            if verbose and "instances" in entry:
                entry["instances"] = [
                    {kk: vv for kk, vv in inst.items() if kk != "_obj"} for inst in entry["instances"]
                ]
            else:
                entry.pop("instances", None)
            output[k] = entry

        path = os.path.join(self.outdir, "LiveClasses.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        return path

    # --- Index construction ---

    def _load_raw_capture(self) -> dict | None:
        """Load the raw capture tree from LiveTree.raw.json."""
        path = os.path.join(self.outdir, "LiveTree.raw.json")
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _build_repr_index(self, node: dict, index: dict[str, dict], path: str):
        """Recursively walk the capture tree, creating an index entry for each class.

        Each entry records the class's module path, its properties (from child nodes
        of type "property"), and its no-arg getters (children named get_*).
        """
        current = path + "/" + node.get("name", "?")
        if node.get("type") == "class" and not node.get("ref"):
            r = node.get("repr")
            if r and r not in index:
                props = {
                    c["name"]: {"probed": False}
                    for c in node.get("children", [])
                    if c.get("type") == "property"
                }
                getters = {
                    c["name"]: {"probed": False}
                    for c in node.get("children", [])
                    if c.get("type") == "function" and c.get("name", "").startswith("get_")
                }
                entry = {
                    "path": current,
                    "complete": False,
                    "constructable": False,
                    "properties": props,
                    "getters": getters,
                }
                if node.get("constructable"):
                    entry["constructable"] = True
                index[r] = entry
        for child in node.get("children", []):
            self._build_repr_index(child, index, current)

    # --- Instance seeding ---

    def _construct_types(self):
        """Construct instances of types marked as constructable in the raw capture."""
        for r, entry in self.repr_index.items():
            if not entry.get("constructable"):
                continue
            # Resolve class from path: /Live/MidiMap/CCFeedbackRule -> Live.MidiMap.CCFeedbackRule
            parts = entry["path"].strip("/").split("/")
            try:
                cls = Live
                for part in parts[1:]:  # skip "Live"
                    cls = getattr(cls, part)
                obj = cls()  # type: ignore
                self._add_instance(obj)
                self.log(f"  Constructed {r}")
            except Exception as e:
                self.log(f"  Failed to construct {r}: {e}")

        for constructor in self._hardcoded_constructors():
            try:
                obj = constructor()
                self._add_instance(obj)
                class_repr = repr(type(obj))
                self.log(f"  Constructed {class_repr}")
                entry = self.repr_index.get(class_repr)
                if entry is not None:
                    entry["constructable"] = True
            except Exception as e:
                self.log(f"  Failed hardcoded construction: {e}")

    def _hardcoded_constructors(self) -> list:
        """Registry of constructor calls that need specific arguments."""
        return [
            lambda: Live.Base.Timer(callback=lambda: None, interval=1, start=False),
            lambda: Live.Clip.MidiNoteSpecification(pitch=60, start_time=0.0, duration=0.25),
            lambda: Live.Clip.WarpMarker(sample_time=0.0, beat_time=0.0),
            lambda: Live.Envelope.EnvelopeEventControlCoefficients(x1=0.0, y1=0.0, x2=0.0, y2=0.0),
            lambda: Live.Envelope.EnvelopeEvent(
                time=0.0, value=0.0,
                control_coefficients=Live.Envelope.EnvelopeEventControlCoefficients(x1=0.0, y1=0.0, x2=0.0, y2=0.0),
            ),
            lambda: Live.TuningSystem.PitchClassAndOctave(index_in_octave=0, octave=0),
            lambda: Live.TuningSystem.ReferencePitch(index_in_octave=0, octave=0, frequency=440.0),
        ]

    # --- Probe loop ---

    def _probe_loop(self):
        """Pick unprobed instances and discover their types until no work remains.

        Each iteration: update completeness flags, find the next unprobed instance,
        probe its properties and getters, then mark it done. Falls back to hardcoded
        method calls for types that need arguments we can't infer.
        """
        while True:
            self._update_completeness()
            next_item = self._next_unprobed()
            if next_item is not None:
                cls_repr, entry, inst = next_item
                self.log(f"Probing {cls_repr} at {entry['path']} with _live_ptr={inst['_live_ptr']}")
                self._probe_properties(entry, inst)
                self._probe_getters(entry, inst)
                inst["probed"] = True
            elif self._probe_hardcoded():
                continue
            else:
                break

    def _probe_properties(self, entry: dict, inst: dict):
        """Read each property on a live instance to discover its runtime type.

        For unprobed properties (or those previously resolved as NoneType), records
        the type name and repr, then discovers the value to register new instances.
        For already-probed properties whose type is incomplete or iterable, rediscovers
        them to pick up child instances that may not have been reachable before.
        Also records element_repr for iterable properties (vectors/lists).
        """
        obj = inst["_obj"]
        for prop_name, prop_info in entry["properties"].items():
            try:
                prop = getattr(obj, prop_name)
                if not prop_info["probed"] or prop_info.get("type") == "NoneType":
                    type_name = type(prop).__name__
                    # Skip if already probed and still NoneType (no new info)
                    if prop_info["probed"] and type_name == "NoneType":
                        continue
                    prop_info["probed"] = True
                    prop_info["type"] = type_name
                    self.log(f"  Found property {prop_name} with type {type_name}")
                    if type_name not in _PRIMITIVES:
                        prop_info["repr"] = repr(type(prop))
                    self._discover(prop)
                    if hasattr(prop, "__iter__") and not isinstance(prop, str):
                        self._record_element_type(prop, prop_info)
                elif prop_info.get("repr") and not self._is_complete(prop_info["repr"]):
                    # Re-discover incomplete child types
                    self._discover(prop)
                elif hasattr(prop, "__iter__"):
                    # Re-discover iterables to pick up new elements
                    self._discover(prop)
            except Exception as e:
                self.log(f"  Failed to access property {prop_name}: {e}")

    def _probe_getters(self, entry: dict, inst: dict):
        """Call each no-arg getter on a live instance to discover its return type.

        Records the type name and repr, then discovers the value to register new instances.
        Also records element_repr for iterable return values (vectors/lists).
        """
        obj = inst["_obj"]
        for getter_name, getter_info in entry["getters"].items():
            if getter_info["probed"]:
                continue
            try:
                result = getattr(obj, getter_name)()
                getter_info["probed"] = True
                type_name = type(result).__name__
                getter_info["type"] = type_name
                self.log(f"  Getter {getter_name} returned {type_name}")
                if type_name not in _PRIMITIVES:
                    getter_info["repr"] = repr(type(result))
                self._discover(result)
                if hasattr(result, "__iter__") and not isinstance(result, str):
                    self._record_element_type(result, getter_info)
            except Exception as e:
                self.log(f"  Failed to call {getter_name}: {e}")

    def _probe_hardcoded(self) -> bool:
        """Call methods that require arguments. Returns True if new instances were discovered."""
        found = False
        for i, call in enumerate(self._hardcoded_calls()):
            if i in self._hardcoded_done:
                continue
            repr_key, method_name, args = call
            # Ensure the method appears in the getter list so results are recorded
            if repr_key in self.repr_index:
                self.repr_index[repr_key].setdefault("getters", {}).setdefault(method_name, {"probed": False})
            if repr_key not in self.repr_index or not self.repr_index[repr_key].get("instances"):
                continue
            obj = self.repr_index[repr_key]["instances"][0]["_obj"]
            try:
                result = getattr(obj, method_name)(*args)
                if hasattr(result, "__iter__"):
                    for item in result:
                        self._discover(item)
                else:
                    self._discover(result)
                found = True
                self.log(f"  Hardcoded {method_name} succeeded")
                # Record return type on the getter entry (if it exists)
                entry = self.repr_index[repr_key]
                getter_info = entry.get("getters", {}).get(method_name)
                if getter_info and not getter_info.get("probed"):
                    type_name = type(result).__name__
                    getter_info["probed"] = True
                    getter_info["type"] = type_name
                    if type_name not in _PRIMITIVES:
                        getter_info["repr"] = repr(type(result))
                if hasattr(result, "__iter__") and not isinstance(result, str):
                    self._record_element_type(result, getter_info)
            except Exception as e:
                self.log(f"  Failed to call {method_name}: {e}")
            self._hardcoded_done.add(i)
        return found

    def _hardcoded_calls(self) -> list[tuple[str, str, tuple]]:
        """Registry of method calls that need arguments. Each entry: (class_repr, method, args)."""
        return [
            ("<class 'Envelope.Envelope'>", "events_in_range", (0, 999999)),
        ]

    # --- Element type recording ---

    def _record_element_type(self, iterable: Any, prop_info: dict | None = None) -> None:
        """Record element_reprs for an iterable's element types.

        element_reprs is a set of all unique type reprs found across probing.
        Stamps are accumulated on both the vector class entry in repr_index
        and on prop_info so each property knows its own element types.
        """
        vec_repr = repr(type(iterable))
        vec_entry = self.repr_index.get(vec_repr)
        for item in iterable:
            item_repr = repr(type(item))
            if vec_entry is not None:
                reprs = vec_entry.setdefault("element_reprs", [])
                if item_repr not in reprs:
                    reprs.append(item_repr)
                    self.log(f"  Recorded element_repr on {vec_repr}: {item_repr}")
            if prop_info is not None:
                reprs = prop_info.setdefault("element_reprs", [])
                if item_repr not in reprs:
                    reprs.append(item_repr)
                    self.log(f"  Recorded element_repr on property: {item_repr}")

    # --- Completeness tracking ---

    def _update_completeness(self):
        """Recompute complete flags for all classes. Runs until stable.

        A class is complete when:
        1. All its properties are probed.
        2. Every child type (property repr in the index) is also complete.
        3. Vector classes have element_repr recorded.

        Getters do NOT block completeness — they may need args we can't provide.
        canonical_parent is excluded to avoid circular dependencies.
        """
        changed = True
        while changed:
            changed = False
            for class_repr, entry in self.repr_index.items():
                if entry.get("complete"):
                    continue

                if any(not p["probed"] for p in entry.get("properties", {}).values()):
                    continue

                # Vector classes need element_reprs to be complete
                name = entry.get("path", "").rsplit("/", 1)[-1]
                if name.endswith("Vector") and name != "Vector" and not entry.get("element_reprs"):
                    continue

                all_children_complete = True
                for prop_name, p in entry.get("properties", {}).items():
                    if prop_name == "canonical_parent":
                        continue
                    child_repr = p.get("repr")
                    if child_repr and child_repr != class_repr:
                        child_entry = self.repr_index.get(child_repr)
                        if child_entry and not child_entry.get("complete"):
                            all_children_complete = False
                    if not all_children_complete:
                        break
                if not all_children_complete:
                    continue

                entry["complete"] = True
                changed = True

    def _is_complete(self, class_repr: str) -> bool:
        """Check the stored complete flag for a class."""
        entry = self.repr_index.get(class_repr)
        if entry is None:
            return True
        return entry.get("complete", False)

    # --- Instance discovery ---

    def _discover(self, obj: Any):
        """Register obj as an instance if its class is in the index, and iterate if possible."""
        type_name = type(obj).__name__
        if type_name in _PRIMITIVES:
            return
        class_repr = repr(type(obj))
        if class_repr in self.repr_index:
            self._add_instance(obj)
        if hasattr(obj, "__iter__"):
            for item in obj:
                self._add_instance(item)

    def _add_instance(self, obj: Any):
        """Register a live object in its class's entry, keyed by _live_ptr or id."""
        class_repr = repr(type(obj))
        entry = self.repr_index.get(class_repr)
        if entry is None:
            self.log(f"PropertyProbe: no match for {class_repr}")
            return

        ptr = getattr(obj, "_live_ptr", None)
        key = ptr if ptr is not None else id(obj)
        instances = entry.setdefault("instances", [])
        if any(i["_key"] == key for i in instances):
            return
        instances.append({"_live_ptr": ptr, "_key": key, "probed": False, "_obj": obj})

    def _next_unprobed(self) -> tuple[str, dict, dict] | None:
        """Find the next unprobed instance to work on.

        Prioritizes incomplete classes, but also revisits complete classes that have
        NoneType properties — a different instance may resolve them to a real type.
        """
        for r, entry in self.repr_index.items():
            if self._is_complete(r):
                has_none = any(p.get("type") == "NoneType" for p in entry.get("properties", {}).values())
                if not has_none:
                    continue
            for inst in entry.get("instances", []):
                if not inst["probed"]:
                    return (r, entry, inst)
        return None

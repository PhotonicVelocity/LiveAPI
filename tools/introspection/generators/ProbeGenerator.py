"""
Probe generator — runs inside Live to discover runtime property types,
settability, listener support, and enum values.

Outputs probe_results.json alongside Live.json from Phase 1.
Requires a Live session with a document open (fresh empty set is sufficient).
"""

import inspect
import json
import os
import warnings
from typing import Any, Optional


class ProbeGenerator:
    def __init__(self, module: Any, outdir: str, c_instance: Any = None):
        self.module = module
        self.outdir = outdir
        self.c_instance = c_instance
        self._live_objects: dict[str, Any] = {}

    def generate(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            self._generate()

    def _generate(self):
        if self.c_instance is not None:
            self._collect_live_objects()

        results = {}
        self._probe_module(self.module, results)

        out_file = os.path.join(self.outdir, "probe_results.json")
        with open(out_file, "w") as f:
            json.dump(results, f, indent=2, default=str)

    # ------------------------------------------------------------------
    # Object tree navigation — walk from root objects reachable in a
    # fresh empty Live set.
    # ------------------------------------------------------------------

    def _collect_live_objects(self):
        """Walk the live object tree to collect instances for runtime type probing."""
        try:
            song = self.c_instance.song()
            app = song.application
        except Exception:
            try:
                import Live  # type: ignore
                app = Live.Application.get_application()
                song = app.get_document()
            except Exception:
                return

        self._register(app, "Application.Application")
        self._register(song, "Song.Song")
        self._try(lambda: self._register(app.view, "Application.Application.View"))
        self._try(lambda: self._register(song.view, "Song.Song.View"))
        self._try(lambda: self._register(app.browser, "Browser.Browser"))
        self._try(lambda: self._register(app.browser.instruments, "Browser.BrowserItem"))

        # Scenes
        self._try(lambda: self._register(song.scenes[0], "Scene.Scene"))

        # Groove pool
        self._try(lambda: self._register(song.groove_pool, "GroovePool.GroovePool"))

        # Cue points
        self._try(lambda: self._register(song.cue_points[0], "Song.CuePoint"))

        # Tuning system
        self._try(lambda: self._register(song.tuning_system, "TuningSystem.TuningSystem"))

        # Walk all tracks (regular + return + master)
        all_tracks = []
        self._try(lambda: all_tracks.extend(song.tracks))
        self._try(lambda: all_tracks.extend(song.return_tracks))
        self._try(lambda: all_tracks.append(song.master_track))

        for track in all_tracks:
            self._collect_from_track(track)

    def _collect_from_track(self, track: Any):
        """Collect instances reachable from a track."""
        self._try(lambda: self._register(track, "Track.Track"))
        self._try(lambda: self._register(track.view, "Track.Track.View"))
        self._try(lambda: self._register(track.mixer_device, "MixerDevice.MixerDevice"))

        # Routing types and channels
        self._try(lambda: self._register(track.available_input_routing_types[0], "Track.RoutingType"))
        self._try(lambda: self._register(track.available_output_routing_types[0], "Track.RoutingType"))
        self._try(lambda: self._register(track.available_input_routing_channels[0], "Track.RoutingChannel"))
        self._try(lambda: self._register(track.available_output_routing_channels[0], "Track.RoutingChannel"))

        # Mixer device parameters
        self._try(lambda: self._register(track.mixer_device.volume, "DeviceParameter.DeviceParameter"))

        # Clip slots
        try:
            slots = track.clip_slots
            if len(slots) > 0:
                self._register(slots[0], "ClipSlot.ClipSlot")
                for slot in slots:
                    try:
                        if slot.has_clip:
                            clip = slot.clip
                            self._register(clip, "Clip.Clip")
                            self._try(lambda: self._register(clip.view, "Clip.Clip.View"))
                            break
                    except Exception:
                        continue
        except Exception:
            pass

        # Devices
        try:
            for device in track.devices:
                self._collect_from_device(device)
        except Exception:
            pass

    def _collect_from_device(self, device: Any):
        """Collect instances reachable from a device."""
        self._try(lambda: self._register(device, "Device.Device"))
        self._try(lambda: self._register(device.view, "Device.Device.View"))
        self._try(lambda: self._register(device.parameters[0], "DeviceParameter.DeviceParameter"))

        # Register specialized device type by class name
        cls_name = type(device).__name__
        if cls_name != "Device":
            self._try(lambda: self._register(device, f"{cls_name}.{cls_name}"))

        # Chains (Rack devices)
        try:
            chains = device.chains
            if len(chains) > 0:
                chain = chains[0]
                self._register(chain, "Chain.Chain")
                self._try(lambda: self._register(chain.mixer_device, "ChainMixerDevice.ChainMixerDevice"))
        except Exception:
            pass

        # Drum pads (Drum Rack)
        try:
            drum_pads = device.drum_pads
            if len(drum_pads) > 0:
                self._register(drum_pads[0], "DrumPad.DrumPad")
        except Exception:
            pass

    def _try(self, fn):
        try:
            fn()
        except Exception:
            pass

    def _register(self, obj: Any, class_key: str):
        """Register a live object instance. First registration wins — earlier instances
        tend to have more properties accessible (e.g., regular track vs master track)."""
        if obj is not None and class_key not in self._live_objects:
            self._live_objects[class_key] = obj

    # ------------------------------------------------------------------
    # Probe logic — iterate modules/classes and inspect properties
    # ------------------------------------------------------------------

    def _probe_module(self, module: Any, results: dict):
        for name in sorted(dir(module)):
            if name.startswith("__"):
                continue
            try:
                obj = getattr(module, name)
            except Exception:
                continue
            if inspect.ismodule(obj):
                self._probe_module(obj, results)
            elif inspect.isclass(obj):
                qualified = f"{module.__name__}.{name}"
                result = self._probe_class(obj, qualified)
                # Only store classes that produced data
                if result:
                    # Use key format StubGenerator expects: "Song.Song" not "Live.Song.Song"
                    key = qualified.replace("Live.", "", 1) if qualified.startswith("Live.") else qualified
                    results[key] = result

    def _probe_class(self, cls: Any, qualified_name: str) -> Optional[dict]:
        result: dict = {}

        try:
            members = sorted(dir(cls))
        except Exception:
            return None

        # Detect listeners from method names
        listener_props = set()
        for name in members:
            if name.startswith("add_") and name.endswith("_listener"):
                listener_props.add(name[4:-9])
        if listener_props:
            result["listeners"] = sorted(listener_props)

        # Detect enum classes (int subclass with named int values)
        try:
            if inspect.isclass(cls) and issubclass(cls, int):
                enum_values = {}
                for name in members:
                    if name.startswith("_"):
                        continue
                    try:
                        val = getattr(cls, name)
                    except Exception:
                        continue
                    if isinstance(val, int) and not callable(val):
                        enum_values[name] = int(val)
                if enum_values:
                    result["likely_enum"] = True
                    result["enum_values"] = enum_values
                    return result
        except Exception:
            pass

        # Find a live instance for runtime type probing
        live_key = qualified_name.replace("Live.", "", 1) if qualified_name.startswith("Live.") else qualified_name
        live_instance = self._live_objects.get(live_key)

        # Probe properties
        properties = {}
        for name in members:
            if name.startswith("__"):
                continue
            try:
                member = getattr(cls, name)
            except Exception:
                continue
            if isinstance(member, property):
                prop_info = self._probe_property(member, name, live_instance)
                if prop_info:
                    properties[name] = prop_info

        if properties:
            result["properties"] = properties

        return result if result else None

    def _probe_property(self, prop: Any, name: str, live_instance: Any) -> dict:
        info: dict = {}

        # Settable? Check descriptor-level fset (no mutation)
        if getattr(prop, "fset", None) is not None:
            info["settable"] = True

        # Runtime value type
        if live_instance is not None:
            try:
                value = getattr(live_instance, name)
                value_type = type(value).__name__
                info["runtime_type"] = value_type

                # For sequences, probe element type
                if value_type in ("list", "tuple", "Vector"):
                    try:
                        if hasattr(value, "__len__") and len(value) > 0:
                            info["runtime_element_type"] = type(value[0]).__name__
                        else:
                            info["runtime_element_type"] = "(empty)"
                    except Exception:
                        pass
            except Exception as e:
                info["runtime_error"] = str(e)

        return info

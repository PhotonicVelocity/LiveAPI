from __future__ import annotations

"""
Property probe — runs inside Live to discover runtime property types,
settability, listener support, and enum values.

Outputs probe_results.json alongside Live.json from Phase 1.
Requires a Live session with a document open (fresh empty set is sufficient).

## Object collection

The probe needs live instances of each class to read property values from.
Collection happens in two phases within `_collect_live_objects()`:

1. **Natural walk** — traverses the object tree from Application/Song downward,
   registering every reachable instance. First registration wins so that richer
   instances (e.g. regular track vs master track) take priority.

2. **Scaffolding** — creates temporary Live objects (clips, MIDI notes, etc.)
   to reach classes that don't exist in a fresh empty set. Each `_ensure_*`
   method follows the same pattern:
   - Check if the class key is already registered (skip if so).
   - Create the object via the Live API.
   - Register the instance.
   - Append a cleanup callable to `self._cleanup`.

   To add a new temp object type, add one `_ensure_*` method and one call
   at the end of `_collect_live_objects()`. Methods are called in dependency
   order (e.g. clip before MIDI notes, since notes need a clip to live in).

## Cleanup

`self._cleanup` is a LIFO stack of `(description, callable)` tuples.
`_run_cleanup()` pops and executes each in reverse order so dependents are
removed before their parents (notes before clip, clip before track).
Cleanup runs in a `finally` block in `_generate()` — after probing is
complete but guaranteed even on failure.
"""

import inspect
import json
import os
import warnings
from typing import Any, Optional


class PropertyProbe:
    def __init__(self, module: Any, outdir: str, c_instance: Any = None):
        self.module = module
        self.outdir = outdir
        self.c_instance = c_instance
        self._live_objects: dict[str, Any] = {}
        self._alt_instances: dict[str, list[Any]] = {}  # fallback instances per class key
        self._cleanup: list[tuple[str, Any]] = []  # (description, callable)

    def generate(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            self._generate()

    def _generate(self):
        if self.c_instance is not None:
            self._collect_live_objects()

        try:
            results = {}
            self._probe_module(self.module, results)
        finally:
            self._run_cleanup()

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

        # Groove pool + individual grooves
        self._try(lambda: self._register(song.groove_pool, "GroovePool.GroovePool"))
        self._try(lambda: self._register(song.groove_pool.grooves[0], "Groove.Groove"))

        # Cue points
        self._try(lambda: self._register(song.cue_points[0], "Song.CuePoint"))

        # Tuning system + sub-objects — returns None in a fresh set with no custom
        # tuning loaded. TODO: probe with a saved set that has a tuning system.
        self._try(lambda: self._register(song.tuning_system, "TuningSystem.TuningSystem"))
        self._try(lambda: self._register(song.tuning_system.reference_pitch, "TuningSystem.ReferencePitch"))
        self._try(lambda: self._register(song.tuning_system.highest_note, "TuningSystem.PitchClassAndOctave"))

        # Value objects from song methods
        self._try(lambda: self._register(song.get_current_beats_song_time(), "Song.BeatTime"))
        self._try(lambda: self._register(song.get_current_smpte_song_time(0), "Song.SmptTime"))

        # Walk all tracks — non-group audio tracks first so Track.Track gets an
        # instance with arm, monitoring, and input/output meters. Group tracks lack
        # arm/implicit_arm/current_monitoring_state; MIDI tracks lack meters.
        all_tracks = []
        self._try(lambda: all_tracks.extend(song.tracks))
        self._try(lambda: all_tracks.extend(song.return_tracks))
        all_tracks.sort(key=lambda t: (
            0 if self._try_bool(lambda: t.has_audio_input) and not self._try_bool(lambda: t.is_foldable) else
            1 if not self._try_bool(lambda: t.is_foldable) else
            2
        ))
        self._try(lambda: all_tracks.append(song.master_track))

        for track in all_tracks:
            self._collect_from_track(track)

        # Master track mixer has crossfader, cue_volume, song_tempo that regular
        # track mixers lack. Register as alt so both are probed — the primary
        # (regular track) covers crossfade_assign, the alt covers the rest.
        self._try(lambda: self._register_alt(
            song.master_track.mixer_device, "MixerDevice.MixerDevice"
        ))

        # Construction — standalone value types that don't need the live set
        self._ensure_constructable_types()

        # Scaffolding — create temp objects to reach missing classes
        self._ensure_cue_point(song)
        self._ensure_take_lane(song)
        # Device loading via browser.load_item() is async and unreliable for
        # probing — devices aren't initialized until the next tick, and cleanup
        # of loaded devices is fragile. Specialized device classes (DriftDevice,
        # SimplerDevice, etc.) require a set that already contains those devices.

    def _collect_from_track(self, track: Any):
        """Collect instances reachable from a track."""
        # Group tracks lack arm/monitoring; register as alt so fold_state is still probed
        is_group = self._try_bool(lambda: track.is_foldable)
        if is_group:
            self._register_alt(track, "Track.Track")
        else:
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
        is_audio = self._try_bool(lambda: track.has_audio_input)
        try:
            slots = track.clip_slots
            if len(slots) > 0:
                self._register(slots[0], "ClipSlot.ClipSlot")
                for slot in slots:
                    try:
                        if slot.has_clip:
                            clip = slot.clip
                            # Audio clips expose more Clip properties — force-overwrite
                            self._register(clip, "Clip.Clip", force=is_audio)
                            self._try(lambda: self._register(clip.view, "Clip.Clip.View", force=is_audio))
                            self._collect_from_clip(clip, is_audio)
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

    def _collect_from_clip(self, clip: Any, is_audio: bool):
        """Extract sub-objects from an existing clip (MIDI notes, warp markers, envelopes)."""
        if is_audio:
            # Warp markers from warped audio clips
            try:
                markers = clip.warp_markers
                if len(markers) > 0:
                    self._register(markers[0], "Clip.WarpMarker")
            except Exception:
                pass
        else:
            # MIDI notes
            try:
                notes = clip.get_notes_extended(0, 128, 0.0, clip.length)
                if len(notes) > 0:
                    self._register(notes[0], "Clip.MidiNote")
            except Exception:
                pass

        # Automation envelopes — try 12.2+ collection first, then legacy per-parameter API.
        # Register under both old and new keys so the probe finds the instance regardless of version.
        try:
            if hasattr(clip, "automation_envelopes"):
                envs = clip.automation_envelopes
                if envs and len(envs) > 0:
                    env = envs[0]
                    self._register(env, "Envelope.Envelope")
                    self._register(env, "Clip.AutomationEnvelope")
                    self._try_envelope_events(env, clip)
                    return
        except Exception:
            pass
        try:
            if clip.has_envelopes:
                track = clip.canonical_parent.canonical_parent  # clip → clip_slot → track
                param = track.mixer_device.volume
                env = clip.automation_envelope(param)
                if env is not None:
                    self._register(env, "Clip.AutomationEnvelope")
                    self._register(env, "Envelope.Envelope")
                    self._try_envelope_events(env, clip)
        except Exception:
            pass

    def _try_envelope_events(self, env: Any, clip: Any):
        """Try to extract EnvelopeEvent sub-objects (12.2+ only)."""
        try:
            events = env.events_in_range(0.0, clip.length)
            if len(events) > 0:
                self._register(events[0], "Envelope.EnvelopeEvent")
                self._try(lambda: self._register(
                    events[0].control_coefficients, "Envelope.EnvelopeEventControlCoefficients"
                ))
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

    def _try_bool(self, fn) -> bool:
        try:
            return bool(fn())
        except Exception:
            return False

    def _register(self, obj: Any, class_key: str, force: bool = False):
        """Register a live object instance. First registration wins unless force=True.
        Use force=True when a later instance is known to expose strictly more properties
        (e.g., audio clip over MIDI clip, master mixer over regular mixer)."""
        if obj is not None and (force or class_key not in self._live_objects):
            self._live_objects[class_key] = obj

    def _register_alt(self, obj: Any, class_key: str):
        """Register an alternative instance for a class. Used when different instances
        expose different subsets of properties (e.g., master vs regular track mixer).
        The primary instance is tried first; alts are tried for properties that fail."""
        if obj is not None:
            self._alt_instances.setdefault(class_key, []).append(obj)

    # ------------------------------------------------------------------
    # Scaffolding — create temporary objects to reach missing classes
    # ------------------------------------------------------------------

    def _ensure_cue_point(self, song: Any):
        """Create a temp cue point if Song.CuePoint is not yet registered."""
        if "Song.CuePoint" in self._live_objects:
            return

        try:
            song.set_or_delete_cue()
            cue_points = song.cue_points
            if len(cue_points) > 0:
                self._register(cue_points[0], "Song.CuePoint")
                self._cleanup.append(("delete temp cue point", lambda: song.set_or_delete_cue()))
        except Exception:
            pass

    def _ensure_take_lane(self, song: Any):
        """Create a temp take lane to probe TakeLane.TakeLane."""
        if "TakeLane.TakeLane" in self._live_objects:
            return

        # Find a MIDI track to create the take lane on
        midi_track = None
        try:
            for track in song.tracks:
                if track.has_midi_input:
                    midi_track = track
                    break
        except Exception:
            return
        if midi_track is None:
            return

        try:
            take_lane = midi_track.create_take_lane()
            if take_lane is not None:
                self._register(take_lane, "TakeLane.TakeLane")
                # No delete_take_lane API exists; the lane stays but is harmless in a fresh set
        except Exception:
            pass

    def _ensure_constructable_types(self):
        """Register instances of classes that can be constructed directly (no Live session needed)."""
        try:
            import Live  # type: ignore

            # MidiMap feedback rules — plain value objects used by Control Surfaces
            if "MidiMap.CCFeedbackRule" not in self._live_objects:
                self._try(lambda: self._register(Live.MidiMap.CCFeedbackRule(), "MidiMap.CCFeedbackRule"))
            if "MidiMap.NoteFeedbackRule" not in self._live_objects:
                self._try(lambda: self._register(Live.MidiMap.NoteFeedbackRule(), "MidiMap.NoteFeedbackRule"))
            if "MidiMap.PitchBendFeedbackRule" not in self._live_objects:
                self._try(lambda: self._register(
                    Live.MidiMap.PitchBendFeedbackRule(), "MidiMap.PitchBendFeedbackRule"
                ))

            # Base.Timer — used by Push 2, v3 framework, third-party scripts
            if "Base.Timer" not in self._live_objects:
                self._try(lambda: self._register(
                    Live.Base.Timer(callback=lambda: None, interval=1, start=False), "Base.Timer"
                ))

            # Base.Text — returned by Live.Base.get_text()
            if "Base.Text" not in self._live_objects:
                self._try(lambda: self._register(Live.Base.get_text("", ""), "Base.Text"))

            # Clip.MidiNoteSpecification — constructable value object for creating MIDI notes
            self._try(lambda: self._register(
                Live.Clip.MidiNoteSpecification(pitch=60, start_time=0.0, duration=0.25),
                "Clip.MidiNoteSpecification",
            ))
        except Exception:
            pass

    def _run_cleanup(self):
        """Run all cleanup actions in LIFO order."""
        while self._cleanup:
            desc, fn = self._cleanup.pop()
            try:
                fn()
            except Exception:
                pass

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

        # Find live instances for runtime type probing
        live_key = qualified_name.replace("Live.", "", 1) if qualified_name.startswith("Live.") else qualified_name
        live_instance = self._live_objects.get(live_key)
        alt_instances = self._alt_instances.get(live_key, [])

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
                prop_info = self._probe_property(member, name, live_instance, alt_instances)
                if prop_info:
                    properties[name] = prop_info

        if properties:
            result["properties"] = properties

        return result if result else None

    def _probe_property(
        self, prop: Any, name: str, live_instance: Any, alt_instances: list[Any] | None = None,
    ) -> dict:
        info: dict = {
            "settable": getattr(prop, "fset", None) is not None,
            "runtime_type": None,
        }

        # Try the primary instance, then alts if it fails
        instances = ([live_instance] if live_instance is not None else []) + (alt_instances or [])
        for instance in instances:
            try:
                value = getattr(instance, name)
                value_type = type(value).__name__
                info["runtime_type"] = value_type
                info.pop("runtime_error", None)

                # For sequences, probe element type
                if value_type in ("list", "tuple", "Vector"):
                    try:
                        if hasattr(value, "__len__") and len(value) > 0:
                            info["runtime_element_type"] = type(value[0]).__name__
                        else:
                            info["runtime_element_type"] = "(empty)"
                    except Exception:
                        pass
                break  # success — no need to try more instances
            except Exception as e:
                info["runtime_error"] = str(e)

        return info

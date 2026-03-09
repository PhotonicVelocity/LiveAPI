from __future__ import annotations

"""
Device property probe — tick-driven probe that loads devices from the browser
one at a time, waits for initialization, probes their properties, and cleans up.

This is Phase 2 Step 4 of the introspection pipeline. It runs after the
synchronous PropertyProbe (steps 1-3) and merges results into the same
probe_results.json.

## Execution model

Unlike PropertyProbe which runs synchronously, DevicePropertyProbe is a state
machine driven by MakeDoc's schedule_message tick loop. Each tick advances one
step:

    INIT → LOAD → WAIT → PROBE → LOAD → ... → DONE

This is necessary because browser.load_item() is async — devices aren't
initialized until the next tick after loading.

## Trigger

    touch /tmp/makedoc_probe_devices
"""

import inspect
import json
import os
import warnings
from typing import Any


# State constants
_INIT = "INIT"
_LOAD = "LOAD"
_WAIT = "WAIT"
_PROBE = "PROBE"
_CLEANUP = "CLEANUP"
_DONE = "DONE"


class DevicePropertyProbe:
    def __init__(self, module: Any, outdir: str, c_instance: Any, log_fn: Any = None):
        self.module = module
        self.outdir = outdir
        self.c_instance = c_instance
        self._log = log_fn or (lambda msg: None)

        self._state = _INIT
        self._items: list[Any] = []  # browser items to load
        self._index = 0
        self._results: dict = {}
        self._track: Any = None
        self._song: Any = None
        self._browser: Any = None
        self._seen_class_names: set[str] = set()  # device class names already probed
        self._reprobed_class_names: set[str] = set()  # classes that got a second chance
        self._wait_retries = 0  # retry counter for device load

    def tick(self) -> bool:
        """Advance the state machine until an async boundary or completion.

        Loops internally so that non-blocking transitions (PROBE → LOAD,
        skip → LOAD, CLEANUP, etc.) happen instantly.  Only yields back
        to the caller when entering WAIT — the one-tick pause needed for
        browser.load_item() to finish.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            while True:
                try:
                    result = self._step()
                except Exception as e:
                    self._log(f"DevicePropertyProbe error in {self._state}: {e}")
                    if self._state in (_LOAD, _WAIT, _PROBE):
                        self._index += 1
                        self._state = _LOAD
                        continue
                    self._state = _CLEANUP
                    continue
                if not result:
                    return False
                # Yield only when entering WAIT (async load needs one tick)
                if self._state == _WAIT:
                    return True

    def _step(self) -> bool:
        """Execute a single state transition."""
        if self._state == _INIT:
            return self._do_init()
        elif self._state == _LOAD:
            return self._do_load()
        elif self._state == _WAIT:
            self._state = _PROBE
            return True
        elif self._state == _PROBE:
            return self._do_probe()
        elif self._state == _CLEANUP:
            return self._do_cleanup()
        else:
            return False

    # ------------------------------------------------------------------
    # State handlers
    # ------------------------------------------------------------------

    def _do_init(self) -> bool:
        """Set up: load existing results, create scratch track, collect browser items."""
        try:
            self._song = self.c_instance.song()
            self._browser = self._song.application.browser
        except Exception:
            try:
                import Live  # type: ignore
                app = Live.Application.get_application()
                self._song = app.get_document()
                self._browser = app.browser
            except Exception as e:
                self._log(f"Cannot access song/browser: {e}")
                return False

        # Load existing probe results to merge into
        results_path = os.path.join(self.outdir, "probe_results.json")
        try:
            with open(results_path, "r") as f:
                self._results = json.load(f)
        except Exception:
            self._results = {}

        # Create a scratch MIDI track at the end
        try:
            track_count = len(list(self._song.tracks))
            self._song.create_midi_track(track_count)
            self._track = list(self._song.tracks)[-1]
            self._log(f"Created scratch track at index {track_count}")
        except Exception as e:
            self._log(f"Failed to create scratch track: {e}")
            return False

        # Collect device items from browser
        self._items = self._collect_browser_items()
        self._log(f"Found {len(self._items)} devices to probe")
        self._index = 0

        if not self._items:
            self._state = _CLEANUP
        else:
            self._state = _LOAD
        return True

    def _do_load(self) -> bool:
        """Load the next device from the browser."""
        if self._index >= len(self._items):
            self._state = _CLEANUP
            return True

        item = self._items[self._index]
        try:
            name = item.name
        except Exception:
            name = f"item[{self._index}]"

        self._log(f"Loading device {self._index + 1}/{len(self._items)}: {name}")

        try:
            # Select the scratch track so load_item targets it
            self._song.view.selected_track = self._track
            self._browser.load_item(item)
        except Exception as e:
            self._log(f"  Failed to load {name}: {e}")
            self._index += 1
            return True  # stay in LOAD, try next

        self._wait_retries = 0
        self._state = _WAIT
        return True

    def _do_probe(self) -> bool:
        """Probe the loaded device and its nested objects."""
        try:
            devices = self._track.devices
            if len(devices) == 0:
                self._wait_retries += 1
                if self._wait_retries < 10:
                    self._state = _WAIT  # not ready yet — yield and retry
                    return True
                self._log("  No device found after load — skipping")
                self._index += 1
                self._state = _LOAD
                return True

            device = devices[-1]
            cls_name = type(device).__name__

            if cls_name in self._seen_class_names:
                # Re-probe if there are still untyped properties (different
                # instances may expose different subsets, e.g. Instrument Rack
                # vs Drum Rack both map to RackDevice, or sample-loaded Simpler
                # enables slice mode on View)
                if cls_name not in self._reprobed_class_names and self._has_untyped_props(cls_name):
                    self._reprobed_class_names.add(cls_name)
                    self._log(f"  Re-probing {cls_name} (has untyped properties)")
                    self._probe_device(device, cls_name)
                else:
                    self._log(f"  Already probed {cls_name} — skipping")
            else:
                self._seen_class_names.add(cls_name)
                self._log(f"  Probing {cls_name}")
                self._probe_device(device, cls_name)

            # Always try nested objects — _probe_instance skips if already typed.
            # This is separate from _probe_device because nested classes (Chain,
            # DrumChain, DeviceIO, etc.) may only be populated on certain devices
            # that share the same Python class (e.g. Drum Rack vs Instrument Rack
            # are both RackDevice, but only Instrument Rack has top-level chains).
            self._probe_nested(device)

            # Delete the device
            try:
                self._track.delete_device(len(devices) - 1)
            except Exception as e:
                self._log(f"  Failed to delete device: {e}")
        except Exception as e:
            self._log(f"  Probe error: {e}")

        self._index += 1
        self._state = _LOAD
        return True

    def _do_cleanup(self) -> bool:
        """Delete scratch track and write results."""
        # Delete any remaining devices on the scratch track
        try:
            while len(self._track.devices) > 0:
                self._track.delete_device(0)
        except Exception:
            pass

        # Delete the scratch track
        try:
            tracks = list(self._song.tracks)
            track_idx = tracks.index(self._track)
            self._song.delete_track(track_idx)
            self._log("Deleted scratch track")
        except Exception as e:
            self._log(f"Failed to delete scratch track: {e}")

        # Write merged results
        out_path = os.path.join(self.outdir, "probe_results.json")
        try:
            with open(out_path, "w") as f:
                json.dump(self._results, f, indent=2, default=str)
            self._log(f"Device probe complete — {len(self._seen_class_names)} device classes probed")
        except Exception as e:
            self._log(f"Failed to write results: {e}")

        self._state = _DONE
        return False

    def _has_untyped_props(self, cls_name: str) -> bool:
        """Check if any result keys for this class have untyped properties.

        Checks the device key and its View key. A property is "untyped" if
        it has no runtime_type — even if it has a runtime_error, a different
        instance might succeed (e.g. sample-loaded Simpler vs empty Simpler).
        """
        for suffix in (f"{cls_name}.{cls_name}", f"{cls_name}.{cls_name}.View"):
            props = self._results.get(suffix, {}).get("properties", {})
            for p in props.values():
                if not p.get("runtime_type"):
                    return True
        return False

    # ------------------------------------------------------------------
    # Browser walking
    # ------------------------------------------------------------------

    def _collect_browser_items(self) -> list[Any]:
        """Collect loadable device items from browser categories.

        Collects device templates (lightweight) for most devices, plus one preset
        per Rack folder — rack presets load with devices already inside, giving us
        Chain/ChainMixerDevice/DrumChain instances that empty racks lack.
        """
        items = []
        seen_names: set[str] = set()

        for category_attr in ("instruments", "audio_effects", "midi_effects"):
            try:
                root = getattr(self._browser, category_attr)
            except Exception:
                continue
            self._walk_browser(root, items, seen_names)
            # Also grab one preset per Rack folder (Instrument Rack, Drum Rack, etc.)
            self._collect_rack_presets(root, items)

        # Add a Drum Rack preset from browser.drums — the Drum Rack device template
        # has no children, but browser.drums contains populated Drum Rack presets
        # that give us DrumChain/DrumPad instances to probe.
        try:
            drums_root = self._browser.drums
            drum_preset = self._find_first_adg(drums_root)
            if drum_preset:
                items.append(drum_preset)
                self._log(f"Added drum preset '{drum_preset.name}' for DrumChain probing")
        except Exception:
            pass

        # Add a sample from browser.samples — loading it creates a SimplerDevice
        # with the sample already loaded, enabling slice mode probing
        try:
            samples_root = self._browser.samples
            sample_item = self._find_first_loadable(samples_root)
            if sample_item:
                items.append(sample_item)
                self._log(f"Added sample '{sample_item.name}' for SimplerDevice slice probing")
        except Exception:
            pass

        # Add the first available plug-in from browser.plugins — gives us a
        # PluginDevice instance to probe (AU/VST varies by machine).
        try:
            plugins_root = self._browser.plugins
            plugin_item = self._find_first_plugin(plugins_root)
            if plugin_item:
                items.append(plugin_item)
                self._log(f"Added plugin '{plugin_item.name}' for PluginDevice probing")
            else:
                self._log("No plugin found in browser.plugins")
        except Exception as e:
            self._log(f"Failed to search browser.plugins: {e}")

        return items

    def _walk_browser(self, item: Any, items: list, seen_names: set):
        """Recursively collect device template items from a browser tree."""
        try:
            children = item.children
        except Exception:
            return
        for child in children:
            try:
                if child.is_device and child.is_loadable:
                    name = child.name
                    if name not in seen_names:
                        seen_names.add(name)
                        items.append(child)
                elif not child.is_loadable:
                    # Folder — recurse
                    self._walk_browser(child, items, seen_names)
            except Exception:
                continue

    def _collect_rack_presets(self, category_root: Any, items: list):
        """Add one preset per Rack folder to the item list.

        Rack folders (Instrument Rack, Audio Effect Rack, Drum Rack, MIDI Effect Rack)
        contain .adg presets that load with devices already inside — giving us populated
        Chain/ChainMixerDevice/DrumChain instances that empty rack templates lack.
        """
        try:
            children = category_root.children
        except Exception:
            return
        for child in children:
            try:
                name = child.name
            except Exception:
                continue
            if "Rack" in name:
                preset = self._find_first_loadable(child)
                if preset:
                    items.append(preset)
                    self._log(f"Added rack preset '{preset.name}' from '{name}'")

    def _find_first_adg(self, item: Any) -> Any:
        """Find the first loadable .adg (device group) in a browser tree."""
        try:
            children = item.children
        except Exception:
            return None
        for child in children:
            try:
                if child.is_loadable and child.name.endswith(".adg"):
                    return child
            except Exception:
                continue
            if not getattr(child, "is_loadable", False):
                result = self._find_first_adg(child)
                if result:
                    return result
        return None

    def _find_first_plugin(self, item: Any, depth: int = 0) -> Any:
        """Find the first loadable plugin in the browser.plugins tree.

        Plugins may report is_device=True or is_loadable=True depending on the
        Live version. We accept either, but skip folders.
        """
        try:
            children = item.children
        except Exception:
            return None
        for child in children:
            try:
                is_folder = getattr(child, "is_folder", False)
                is_loadable = getattr(child, "is_loadable", False)
                is_device = getattr(child, "is_device", False)
                if not is_folder and (is_loadable or is_device):
                    return child
            except Exception:
                continue
            # Recurse into folders (max 5 levels: category → manufacturer → plugin)
            if depth < 5:
                result = self._find_first_plugin(child, depth + 1)
                if result:
                    return result
        return None

    def _find_first_loadable(self, item: Any) -> Any:
        """Find the first loadable item in a browser tree."""
        try:
            children = item.children
        except Exception:
            return None
        for child in children:
            try:
                if child.is_loadable:
                    return child
            except Exception:
                continue
            result = self._find_first_loadable(child)
            if result:
                return result
        return None

    # ------------------------------------------------------------------
    # Device probing
    # ------------------------------------------------------------------

    def _probe_device(self, device: Any, cls_name: str):
        """Probe the device class, its view, and device-specific scaffolding (A/B compare, slice mode)."""
        # Probe the device class itself
        device_key = f"{cls_name}.{cls_name}"
        self._probe_instance(device, device_key)

        # Probe the device view
        try:
            view = device.view
            self._probe_instance(view, f"{cls_name}.{cls_name}.View")
        except Exception:
            pass

        # A/B compare — save preset to slot so is_using_compare_preset_b is readable
        try:
            if device.can_compare_ab:
                device.save_preset_to_compare_ab_slot()
                self._probe_instance(device, device_key)
                self._log("    Probed after enabling A/B compare")
        except Exception:
            pass

        # Sample (SimplerDevice) — set slice mode so selected_slice is readable on View
        if cls_name == "SimplerDevice":
            try:
                sample = device.sample
                if sample is not None:
                    self._probe_instance(sample, "Sample.Sample")
                    try:
                        device.playback_mode = 2  # Slice mode
                        self._probe_instance(device.view, f"{cls_name}.{cls_name}.View")
                        self._log("    Probed SimplerDevice.View in slice mode")
                    except Exception as e:
                        self._log(f"    Failed to set slice mode: {e}")
            except Exception:
                pass

    def _probe_nested(self, device: Any):
        """Probe nested objects reachable from a device.

        Called for every loaded device regardless of whether the device class
        was already seen.  _probe_instance short-circuits when all properties
        are already typed, so the cost for duplicates is negligible.
        """
        # Chains (Rack devices)
        try:
            chains = device.chains
            if len(chains) > 0:
                chain = chains[0]
                self._probe_instance(chain, "Chain.Chain")
                try:
                    self._probe_instance(chain.mixer_device, "ChainMixerDevice.ChainMixerDevice")
                except Exception:
                    pass
        except Exception:
            pass

        # Drum pads (Drum Rack) — iterate to find a populated pad since pad 0
        # (note C-2) is typically empty; drum kits populate higher pads (C1+).
        try:
            drum_pads = device.drum_pads
            if len(drum_pads) > 0:
                self._probe_instance(drum_pads[0], "DrumPad.DrumPad")
                for pad in drum_pads:
                    try:
                        pad_chains = pad.chains
                        if len(pad_chains) > 0:
                            pad_chain = pad_chains[0]
                            if type(pad_chain).__name__ == "DrumChain":
                                self._probe_instance(pad_chain, "DrumChain.DrumChain")
                            break
                    except Exception:
                        continue
        except Exception:
            pass

        # Sample (SimplerDevice)
        try:
            sample = device.sample
            if sample is not None:
                self._probe_instance(sample, "Sample.Sample")
        except Exception:
            pass

        # DeviceIO — from MaxDevice audio_inputs/audio_outputs
        for attr in ("audio_inputs", "audio_outputs"):
            try:
                ios = getattr(device, attr)
                if ios is not None and len(ios) > 0:
                    io = ios[0]
                    if type(io).__name__ == "DeviceIO":
                        self._probe_instance(io, "DeviceIO.DeviceIO")
                        break
            except Exception:
                continue

        # Quantized DeviceParameter — find a parameter with value_items to cover
        # properties that fail on continuous parameters (e.g. value_items, short_value_items).
        dp_key = "DeviceParameter.DeviceParameter"
        if self._has_untyped_props("DeviceParameter"):
            try:
                for param in device.parameters:
                    try:
                        items = param.value_items
                        if items and len(items) > 0:
                            self._probe_instance(param, dp_key)
                            self._log(f"    Probed quantized param '{param.name}'")
                            break
                    except Exception:
                        continue
            except Exception:
                pass

    def _probe_instance(self, instance: Any, class_key: str):
        """Probe all properties of a live object instance and store results."""
        # Skip if already probed with runtime types
        existing = self._results.get(class_key, {})
        existing_props = existing.get("properties", {})
        if existing_props and all(p.get("runtime_type") for p in existing_props.values()):
            return

        cls = type(instance)

        try:
            members = sorted(dir(cls))
        except Exception:
            return

        result = existing.copy() if existing else {}

        # Detect listeners from method names
        listener_props = set()
        for name in members:
            if name.startswith("add_") and name.endswith("_listener"):
                listener_props.add(name[4:-9])
        if listener_props:
            result["listeners"] = sorted(listener_props)

        # Probe properties
        properties = dict(existing_props)  # preserve existing data
        for name in members:
            if name.startswith("__"):
                continue
            try:
                member = getattr(cls, name)
            except Exception:
                continue
            if not isinstance(member, property):
                continue

            # Skip if already typed from a previous probe
            if name in properties and properties[name].get("runtime_type"):
                continue

            info: dict = {
                "settable": getattr(member, "fset", None) is not None,
                "runtime_type": None,
            }
            try:
                value = getattr(instance, name)
                value_type = type(value).__name__
                info["runtime_type"] = value_type

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

            properties[name] = info

        if properties:
            result["properties"] = properties

        if result:
            self._results[class_key] = result

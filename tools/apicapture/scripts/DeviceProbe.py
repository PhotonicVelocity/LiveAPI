"""
DeviceProbe — tick-driven device loader for PropertyProbe.

Discovers device-specific types that aren't reachable from Application/Song alone.
Walks the Live browser to collect all loadable devices, then loads them one at a
time onto track 0 using a tick-driven state machine:

    LOAD → WAIT → PROBE → LOAD → ...

browser.load_item() is async — the device isn't available until the next tick.
The state machine loops internally within each tick, only yielding control back
to APICapture on the LOAD→WAIT transition (the async boundary). All other transitions
(WAIT→PROBE, PROBE→LOAD) happen instantly.

After each device loads, the probe discovers its type and runs PropertyProbe's
probe loop to explore all new properties. On completion, cleanup() deletes any
remaining devices and dumps the final LiveClasses.json. Pass verbose=True to
cleanup() to include instance data in the output for debugging.
"""

from __future__ import annotations

from typing import Any

import Live  # type: ignore

from .PropertyProbe import PropertyProbe


class DeviceProbe:
    def __init__(self, probe: PropertyProbe, log_fn: Any = None):
        self.probe = probe
        self.log = log_fn or (lambda msg: None)
        self._items: list[tuple[str, Any]] = []  # (display_name, BrowserItem)
        self._index = 0
        self._state = "LOAD"
        self._browser: Any = None
        self._song: Any = None
        self._track: Any = None
        self._wait_retries = 0

    # --- Public API ---

    def init(self) -> bool:
        """Collect browser items and set up target track. Returns False if setup fails."""
        if not self.probe.init():
            self.log("DeviceProbe: PropertyProbe init failed")
            return False

        app = Live.Application.get_application()
        self._browser = app.browser
        self._song = app.get_document()
        self._track = self._song.tracks[0]

        self._collect_devices()
        self.log(f"DeviceProbe: {len(self._items)} devices to probe")

        self._index = 0
        self._state = "LOAD"
        return len(self._items) > 0

    def tick(self) -> bool:
        """Advance the state machine one step. Returns False when all devices are done.

        Loops internally so that non-blocking transitions (WAIT→PROBE, PROBE→LOAD)
        happen instantly. Only yields on the LOAD→WAIT boundary where
        browser.load_item() needs one tick to complete.
        """
        while True:
            try:
                if self._state == "LOAD":
                    if not self._do_load():
                        return False
                    if self._state == "WAIT":
                        return True
                elif self._state == "WAIT":
                    self._state = "PROBE"
                elif self._state == "PROBE":
                    if not self._do_probe():
                        return False
                else:
                    return False
            except Exception as e:
                self.log(f"DeviceProbe error in {self._state}: {e}")
                self._index += 1
                self._state = "LOAD"
                if self._index >= len(self._items):
                    return False

    def cleanup(self, verbose: bool = False):
        """Delete remaining devices on the scratch track and dump final results."""
        try:
            while len(self._track.devices) > 0:
                self._track.delete_device(0)
        except Exception:
            pass

        out = self.probe.dump(verbose=verbose)
        self.log(f"DeviceProbe: wrote {out}")

    # --- State machine handlers ---

    def _do_load(self) -> bool:
        """Load the next device from the browser onto the scratch track."""
        if self._index >= len(self._items):
            return False

        name, item = self._items[self._index]
        self.log(f"DeviceProbe: loading {self._index + 1}/{len(self._items)}: {name}")

        self._song.view.selected_track = self._track
        self._browser.load_item(item)
        self._wait_retries = 0
        self._state = "WAIT"
        return True

    def _do_probe(self) -> bool:
        """Probe the loaded device's types, then delete it.

        If no device appeared after loading, retries up to 10 ticks before skipping.
        Otherwise, discovers the device, runs PropertyProbe's loop, and deletes it.
        """
        devices = self._track.devices
        if len(devices) == 0:
            self._wait_retries += 1
            if self._wait_retries < 10:
                self._state = "WAIT"
                return True
            self.log("  No device found after load — skipping")
            self._index += 1
            self._state = "LOAD"
            return self._index < len(self._items)

        device = devices[-1]
        self.probe._discover(device)
        self.log(f"  Discovered {repr(type(device))}")

        self.probe._probe_loop()

        try:
            self._track.delete_device(len(devices) - 1)
        except Exception as e:
            self.log(f"  Failed to delete device: {e}")

        self._index += 1
        self._state = "LOAD"
        return self._index < len(self._items)

    # --- Browser collection ---

    def _collect_devices(self):
        """Walk the browser and collect all loadable device items.

        Collects bare devices from each category, plus special items needed to
        discover types that only appear on specific device kinds:
        - Rack presets (.adg) for Chain/ChainMixerDevice
        - Drum Rack preset for DrumChain/DrumPad
        - Audio sample for SimplerDevice slice mode
        - Plugin for PluginDevice
        """
        browser = self._browser

        # Bare devices from the three main categories
        for category in ("instruments", "audio_effects", "midi_effects"):
            root = getattr(browser, category)
            for device in root.children:
                self._items.append((device.name, device))

        # Rack presets — load with devices inside for Chain/ChainMixerDevice probing
        for category in ("instruments", "audio_effects", "midi_effects"):
            root = getattr(browser, category)
            for device in root.children:
                if "Rack" in device.name:
                    preset = self._find_first_loadable(device, ".adg")
                    if preset:
                        self._items.append((f"{device.name} (preset)", preset))
                        self.log(f"DeviceProbe: added rack preset '{preset.name}' from '{device.name}'")

        # Drum Rack preset from browser.drums
        drum_preset = self._find_first_loadable(browser.drums, ".adg")
        if drum_preset:
            self._items.append(("Drum Rack (preset)", drum_preset))
            self.log(f"DeviceProbe: added drum preset '{drum_preset.name}'")

        # Sample from browser.samples
        sample = self._find_first_loadable(browser.samples, ".wav")
        if sample:
            self._items.append(("Simpler (sample)", sample))
            self.log(f"DeviceProbe: added sample '{sample.name}'")

        # Plugin from browser.plugins
        plugin = self._find_first_plugin(browser.plugins)
        if plugin:
            self._items.append(("Plugin", plugin))
            self.log(f"DeviceProbe: added plugin '{plugin.name}'")

    def _find_first_loadable(self, root: Any, ext: str) -> Any | None:
        """Recursively find the first loadable item under root matching ext."""
        for child in root.children:
            if child.is_loadable and child.name.endswith(ext):
                return child
            if child.is_folder:
                result = self._find_first_loadable(child, ext)
                if result is not None:
                    return result
        return None

    def _find_first_plugin(self, root: Any, depth: int = 0) -> Any | None:
        """Recursively find the first loadable plugin in browser.plugins."""
        for child in root.children:
            is_folder = getattr(child, "is_folder", False)
            is_loadable = getattr(child, "is_loadable", False)
            is_device = getattr(child, "is_device", False)
            if not is_folder and (is_loadable or is_device):
                return child
            if depth < 5:
                result = self._find_first_plugin(child, depth + 1)
                if result is not None:
                    return result
        return None

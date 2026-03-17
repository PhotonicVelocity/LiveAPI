from __future__ import annotations

"""
APICapture — MIDI Remote Script that captures Live API metadata.

Runs inside Ableton Live as a Control Surface. On load, starts a tick loop
that polls for trigger files. All phases are triggered externally — nothing
runs automatically on startup. Stub generation is a separate offline step.

Trigger files control which phase runs:

    touch /tmp/apicapture_run            # full pipeline (capture + full probe)
    touch /tmp/apicapture_capture        # raw capture (dir() tree dump → LiveTree.raw.json)
    touch /tmp/apicapture_probe          # basic probe (PropertyProbe only, no devices)
    touch /tmp/apicapture_full_probe     # full probe (PropertyProbe + DeviceProbe)

Each phase writes a completion marker (/tmp/apicapture_*_done) when finished.
Probe output (LiveClasses.json) strips instance data by default; write
"verbose" into the trigger file to include it for debugging:

    echo verbose > /tmp/apicapture_probe

Changes to this file require restarting Live. The scripts in scripts/
(CaptureModule, PropertyProbe, DeviceProbe) are reloaded via importlib on
every trigger, so edits there take effect immediately after reinstalling.

Based on work by Hanz Petrov, Nathan Ramella, Patrick Mueller, and Anand.
Licensed under GPL v3+.
"""

import importlib
import os
import sys
import Live  # type: ignore
from _Framework.ControlSurface import ControlSurface  # type: ignore
from .helpers.app import get_version_number
from .scripts import CaptureModule as _capture_mod
from .scripts import PropertyProbe as _probe_mod
from .scripts import DeviceProbe as _device_probe_mod

CAPTURE_TRIGGER = "/tmp/apicapture_capture"
PROBE_TRIGGER = "/tmp/apicapture_probe"
FULL_PROBE_TRIGGER = "/tmp/apicapture_full_probe"
RUN_TRIGGER = "/tmp/apicapture_run"
TARGETED_PROBE_TRIGGER = "/tmp/apicapture_targeted_probe"

# Completion markers — written by each phase so external scripts can poll for progress.
CAPTURE_DONE = "/tmp/apicapture_capture_done"
PROBE_DONE = "/tmp/apicapture_probe_done"
TARGETED_PROBE_DONE = "/tmp/apicapture_targeted_probe_done"

ALL_TRIGGERS = (CAPTURE_TRIGGER, PROBE_TRIGGER, FULL_PROBE_TRIGGER, RUN_TRIGGER, TARGETED_PROBE_TRIGGER)
ALL_MARKERS = (CAPTURE_DONE, PROBE_DONE, TARGETED_PROBE_DONE)


class APICapture(ControlSurface):
    script_dir: str
    outdir: str

    def __init__(self, c_instance, outdir: str):
        ControlSurface.__init__(self, c_instance)
        self._c_instance = c_instance
        self.log_message(f"Running Python Version: {sys.version}")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.version = get_version_number(Live)
        self.outdir = os.path.join(outdir, self.version, "pipeline")
        self._device_probe: _device_probe_mod.DeviceProbe | None = None
        self._verbose = False

        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        # Clear stale triggers from previous sessions so nothing runs unexpectedly on load
        for trigger in ALL_TRIGGERS + ALL_MARKERS:
            if os.path.exists(trigger):
                os.remove(trigger)
                self.log_message(f"Removed stale trigger: {trigger}")

        self.log_message("APICapture ready — waiting for trigger files")
        self.schedule_message(1, self._tick)

    def _tick(self):
        """Poll for trigger files and drive active device probe."""
        try:
            opts = self._consume_trigger(CAPTURE_TRIGGER)
            if opts is not None:
                self._run_capture()
            opts = self._consume_trigger(PROBE_TRIGGER)
            if opts is not None:
                self._run_probe(verbose=opts.get("verbose", False))
            opts = self._consume_trigger(FULL_PROBE_TRIGGER)
            if opts is not None:
                self._run_full_probe(verbose=opts.get("verbose", False))
            opts = self._consume_trigger(RUN_TRIGGER)
            if opts is not None:
                self._run_capture()
                self._run_full_probe(verbose=opts.get("verbose", False))
            script_path = self._consume_script_trigger(TARGETED_PROBE_TRIGGER)
            if script_path is not None:
                self._run_targeted_probe(script_path)
            # Drive active device probe one step per tick
            if self._device_probe is not None:
                if not self._device_probe.tick():
                    self._device_probe.cleanup(verbose=self._verbose)
                    self._touch(PROBE_DONE)
                    self.log_message("Device probe finished")
                    self._device_probe = None
        except Exception as e:
            self.log_message(f"APICapture tick error: {e}")
        self.schedule_message(1, self._tick)

    def _consume_trigger(self, path: str) -> dict | None:
        """Read and remove a trigger file. Returns parsed options, or None if absent.

        Trigger file contents are parsed as space-separated flags.
        Currently supported: "verbose" — includes instance data in probe output.
        """
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r") as f:
                content = f.read().strip()
        except Exception:
            content = ""
        os.remove(path)
        flags = content.split() if content else []
        return {"verbose": "verbose" in flags}

    def _touch(self, path: str):
        """Write a completion marker containing the build directory path."""
        with open(path, "w") as f:
            f.write(self.outdir)

    def _run_capture(self):
        """Raw capture — dir() tree dump → LiveTree.raw.json."""
        self.log_message("Running raw capture")
        try:
            importlib.reload(_capture_mod)
            out = _capture_mod.capture(Live, outdir=self.outdir)
            self._touch(CAPTURE_DONE)
            self.log_message(f"Capture complete — {out}")
        except Exception as e:
            self.log_message(f"Capture error: {e}")

    def _run_probe(self, verbose: bool = False):
        """Basic probe — PropertyProbe only (no device loading)."""
        self.log_message("Running basic probe")
        try:
            importlib.reload(_probe_mod)
            probe = _probe_mod.PropertyProbe(
                c_instance=self._c_instance,
                outdir=self.outdir,
                log_fn=self.log_message,
            )
            out = probe.run(verbose=verbose)
            self._touch(PROBE_DONE)
            self.log_message(f"Basic probe complete — {out}")
        except Exception as e:
            self.log_message(f"Basic probe error: {e}")

    def _run_full_probe(self, verbose: bool = False):
        """Full probe — PropertyProbe + DeviceProbe (loads all devices from browser)."""
        self.log_message("Running full probe")
        try:
            importlib.reload(_probe_mod)
            importlib.reload(_device_probe_mod)
            probe = _probe_mod.PropertyProbe(
                c_instance=self._c_instance,
                outdir=self.outdir,
                log_fn=self.log_message,
            )

            device_probe = _device_probe_mod.DeviceProbe(
                probe=probe,
                log_fn=self.log_message,
            )
            if device_probe.init():
                self._device_probe = device_probe
                self._verbose = verbose
                self.log_message("Full probe started")
            else:
                probe.run(verbose=verbose)
                self._touch(PROBE_DONE)
                self.log_message("Probe complete (no devices to probe)")
        except Exception as e:
            self.log_message(f"Full probe error: {e}")

    def _consume_script_trigger(self, path: str) -> str | None:
        """Read and remove a trigger file whose content is a script path. Returns the path, or None if absent."""
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r") as f:
                content = f.read().strip()
        except Exception:
            content = ""
        os.remove(path)
        return content if content else None

    def _run_targeted_probe(self, script_path: str):
        """Load and run a targeted probe script.

        The script must define a ``run(song, log)`` function.
        ``song`` is the Live.Song.Song object, ``log`` is the ControlSurface logger.
        """
        script_path = os.path.join(self.script_dir, script_path)
        self.log_message(f"Running targeted probe: {script_path}")
        try:
            import importlib.util

            spec = importlib.util.spec_from_file_location("_targeted_probe", script_path)
            if spec is None or spec.loader is None:
                self.log_message(f"Targeted probe error: cannot load {script_path}")
                return
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if not hasattr(mod, "run"):
                self.log_message(f"Targeted probe error: {script_path} has no run() function")
                return
            song = self._c_instance.song()
            mod.run(song, self.log_message)
            self._touch(TARGETED_PROBE_DONE)
            self.log_message("Targeted probe complete")
        except Exception as e:
            self.log_message(f"Targeted probe error: {e}")

    def disconnect(self):
        ControlSurface.disconnect(self)

"""
MakeDoc — MIDI Remote Script that captures Live API metadata.

Runs inside Ableton Live as a Control Surface. On load, starts a tick loop
that polls for trigger files. All phases are triggered externally — nothing
runs automatically on startup. Stub generation is a separate offline step.

Trigger files control which phase runs:

    touch /tmp/makedoc_reload          # re-run capture (reloads generator code)
    touch /tmp/makedoc_probe           # run probe (reads live objects for types)
    touch /tmp/makedoc_probe_devices   # run device probe (tick-driven)

Each phase writes a completion marker (/tmp/makedoc_*_done) when finished.

Based on work by Hanz Petrov, Nathan Ramella, Patrick Mueller, and Anand.
Licensed under GPL v3+.
"""

import importlib
import os
import sys
import Live  # type: ignore
from _Framework.ControlSurface import ControlSurface  # type: ignore
from .helpers.app import get_version_number
from .generators import Generator as _gen_mod
from .generators import CaptureGenerator as _capgen_mod
from .generators import PropertyProbe as _probe_mod
from .generators import DevicePropertyProbe as _devprobe_mod

RELOAD_TRIGGER = "/tmp/makedoc_reload"
PROBE_TRIGGER = "/tmp/makedoc_probe"
DEVICE_PROBE_TRIGGER = "/tmp/makedoc_probe_devices"

# Completion markers — written by each phase so external scripts can poll for progress.
CAPTURE_DONE = "/tmp/makedoc_capture_done"
PROBE_DONE = "/tmp/makedoc_probe_done"
DEVICE_PROBE_DONE = "/tmp/makedoc_device_probe_done"


class APIMakeDoc(ControlSurface):
    script_dir: str
    outdir: str

    def __init__(self, c_instance, outdir: str):
        ControlSurface.__init__(self, c_instance)
        self._c_instance = c_instance
        self.log_message(f"Running Python Version: {sys.version}")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.version = get_version_number(Live)
        self.outdir = os.path.join(outdir, self.version)
        self._device_probe: _devprobe_mod.DevicePropertyProbe | None = None

        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        self.log_message("MakeDoc ready — waiting for trigger files")
        self.schedule_message(1, self._tick)

    def _tick(self):
        """Poll for trigger files and drive active device probe."""
        try:
            if os.path.exists(RELOAD_TRIGGER):
                os.remove(RELOAD_TRIGGER)
                self._reload_and_capture()
            if os.path.exists(PROBE_TRIGGER):
                os.remove(PROBE_TRIGGER)
                self._reload_and_probe()
            if os.path.exists(DEVICE_PROBE_TRIGGER):
                os.remove(DEVICE_PROBE_TRIGGER)
                self._start_device_probe()
            # Drive active device probe one step per tick
            if self._device_probe is not None:
                if not self._device_probe.tick():
                    self._touch(DEVICE_PROBE_DONE)
                    self.log_message("Device probe finished")
                    self._device_probe = None
        except Exception as e:
            self.log_message(f"MakeDoc tick error: {e}")
        self.schedule_message(1, self._tick)

    @staticmethod
    def _touch(path: str):
        """Write a completion marker file."""
        with open(path, "w") as f:
            f.write("")

    def _reload_and_capture(self):
        """Reload generator modules and re-run capture."""
        self.log_message("Reloading generator modules...")
        try:
            importlib.reload(_gen_mod)
            importlib.reload(_capgen_mod)
            self.log_message("Generator modules reloaded")
        except Exception as e:
            self.log_message(f"Reload error: {e}")
            return
        self._run_capture()

    def _reload_and_probe(self):
        """Reload probe module and run probe."""
        self.log_message("Reloading probe module...")
        try:
            importlib.reload(_probe_mod)
            self.log_message("Probe module reloaded")
        except Exception as e:
            self.log_message(f"Reload error: {e}")
            return
        self._run_probe()

    def _start_device_probe(self):
        """Reload device probe module and start tick-driven device probing."""
        self.log_message("Reloading device probe module...")
        try:
            importlib.reload(_devprobe_mod)
            self.log_message("Device probe module reloaded")
        except Exception as e:
            self.log_message(f"Reload error: {e}")
            return
        self.log_message("Starting device property probe")
        self._device_probe = _devprobe_mod.DevicePropertyProbe(
            Live,
            outdir=self.outdir,
            c_instance=self._c_instance,
            log_fn=self.log_message,
        )

    def _run_capture(self):
        self.log_message("Capturing Live API metadata")
        generator = _capgen_mod.CaptureGenerator(
            Live,
            outdir=self.outdir,
            script_dir=self.script_dir,
        )
        generator.generate()
        self._touch(CAPTURE_DONE)
        self.log_message("Capture complete")

    def _run_probe(self):
        self.log_message("Probing Live API runtime types")
        probe = _probe_mod.PropertyProbe(
            Live,
            outdir=self.outdir,
            c_instance=self._c_instance,
        )
        probe.generate()
        self._touch(PROBE_DONE)
        self.log_message("Probe complete — results in probe_results.json")

    def disconnect(self):
        ControlSurface.disconnect(self)

"""
MakeDoc — MIDI Remote Script that captures Live API metadata.

Runs inside Ableton Live as a Control Surface. On load, introspects the Live
module and writes raw data files (Live.json) to the output directory.
Stub generation is a separate offline step.

Trigger files control which phase runs:

    touch /tmp/makedoc_reload    # re-run capture (reloads generator code)
    touch /tmp/makedoc_probe     # run probe (reads live objects for types)

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
from .generators import ProbeGenerator as _probegen_mod

RELOAD_TRIGGER = "/tmp/makedoc_reload"
PROBE_TRIGGER = "/tmp/makedoc_probe"


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

        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        self._run_capture()
        self.schedule_message(10, self._tick)

    def _tick(self):
        """Poll for trigger files."""
        try:
            if os.path.exists(RELOAD_TRIGGER):
                os.remove(RELOAD_TRIGGER)
                self._reload_and_capture()
            if os.path.exists(PROBE_TRIGGER):
                os.remove(PROBE_TRIGGER)
                self._reload_and_probe()
        except Exception as e:
            self.log_message(f"MakeDoc tick error: {e}")
        self.schedule_message(10, self._tick)

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
            importlib.reload(_probegen_mod)
            self.log_message("Probe module reloaded")
        except Exception as e:
            self.log_message(f"Reload error: {e}")
            return
        self._run_probe()

    def _run_capture(self):
        self.log_message("Capturing Live API metadata")
        generator = _capgen_mod.CaptureGenerator(
            Live,
            outdir=self.outdir,
            script_dir=self.script_dir,
        )
        generator.generate()
        self.log_message("Capture complete")

    def _run_probe(self):
        self.log_message("Probing Live API runtime types")
        probe = _probegen_mod.ProbeGenerator(
            Live,
            outdir=self.outdir,
            c_instance=self._c_instance,
        )
        probe.generate()
        self.log_message("Probe complete — results in probe_results.json")

    def disconnect(self):
        ControlSurface.disconnect(self)

"""
MakeDoc — MIDI Remote Script that captures Live API metadata.

Runs inside Ableton Live as a Control Surface. On load, introspects the Live
module and writes raw data files (Live.xml) to the output directory.
Stub generation is a separate offline step.

Reload support: after the initial run, MakeDoc polls for a trigger file.
When found, generator modules are reloaded and capture re-runs with updated code.

    touch /tmp/makedoc_reload

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
from .generators import DocumentationGenerator as _docgen_mod

RELOAD_TRIGGER = "/tmp/makedoc_reload"


class APIMakeDoc(ControlSurface):
    script_dir: str
    outdir: str

    def __init__(self, c_instance, outdir: str):
        ControlSurface.__init__(self, c_instance)
        self.log_message(f"Running Python Version: {sys.version}")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.version = get_version_number(Live)
        self.outdir = os.path.join(outdir, self.version)

        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)

        self._run()
        self.schedule_message(10, self._tick)

    def _tick(self):
        """Poll for reload trigger file."""
        try:
            if os.path.exists(RELOAD_TRIGGER):
                os.remove(RELOAD_TRIGGER)
                self._reload_and_run()
        except Exception as e:
            self.log_message(f"MakeDoc tick error: {e}")
        self.schedule_message(10, self._tick)

    def _reload_and_run(self):
        """Reload generator modules and re-run capture."""
        self.log_message("Reloading generator modules...")
        try:
            importlib.reload(_gen_mod)
            importlib.reload(_docgen_mod)
            self.log_message("Generator modules reloaded")
        except Exception as e:
            self.log_message(f"Reload error: {e}")
            return
        self._run()

    def _run(self):
        self.log_message("Capturing Live API metadata")
        self._build_documentation()
        self.log_message("Capture complete")

    def _build_documentation(self):
        doc_generator = _docgen_mod.DocumentationGenerator(
            Live,
            outdir=self.outdir,
            script_dir=self.script_dir,
        )
        doc_generator.generate()

    def disconnect(self):
        ControlSurface.disconnect(self)

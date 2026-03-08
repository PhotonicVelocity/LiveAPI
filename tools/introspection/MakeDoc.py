"""
MakeDoc — MIDI Remote Script that captures Live API metadata.

Runs inside Ableton Live as a Control Surface. On load, introspects the Live
module and writes raw data files (Live.xml + probe_results.json) to the output
directory. Stub generation is a separate offline step.

Based on work by Hanz Petrov, Nathan Ramella, Patrick Mueller, and Anand.
Licensed under GPL v3+.
"""

import os
import sys
import Live  # type: ignore
from _Framework.ControlSurface import ControlSurface  # type: ignore
from .helpers.app import get_version_number
from .generators.DocumentationGenerator import DocumentationGenerator


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

    def _run(self):
        self.log_message("Capturing Live API metadata")
        self._build_documentation()
        self.log_message("Capture complete")

    def _build_documentation(self):
        doc_generator = DocumentationGenerator(
            Live,
            outdir=self.outdir,
            script_dir=self.script_dir,
        )
        doc_generator.generate()

    def disconnect(self):
        ControlSurface.disconnect(self)

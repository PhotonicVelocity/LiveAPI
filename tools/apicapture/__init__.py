from .APICapture import APICapture

import os as _os

OUTPUTFOLDER = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))), "stubs")


def create_instance(c_instance):
    return APICapture(c_instance, outdir=OUTPUTFOLDER)

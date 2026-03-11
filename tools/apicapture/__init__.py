from .APICapture import APICapture

OUTPUTFOLDER = (
    "%%%OUTPUTFOLDER%%%"  # this is a placeholder value that is replaced at installation
)


def create_instance(c_instance):
    return APICapture(c_instance, outdir=OUTPUTFOLDER)

from .MakeDoc import APIMakeDoc

OUTPUTFOLDER = (
    "%%%OUTPUTFOLDER%%%"  # this is a placeholder value that is replaced at installation
)


def create_instance(c_instance):
    return APIMakeDoc(c_instance, outdir=OUTPUTFOLDER)

from types import ModuleType
from typing import Callable


class LomObject(ModuleType):

    class LomObject(object):
        def __init__(self, *a, **k):
            """
            this is the base class for an object that is accessible via the LOM
            """
            ...

        @property
        def _live_ptr(self):
            ...

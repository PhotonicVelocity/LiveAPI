from types import ModuleType
from typing import Callable


class GroovePool(ModuleType):

    class GroovePool(object):
        def __init__(self, *a, **k):
            """
            This class represents the groove pool in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def grooves(self) -> tuple:
            """
            Access to the list of grooves
            """
            ...

        def add_grooves_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "grooves" has changed.
            """
            ...

        def grooves_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "grooves".
            """
            ...

        def remove_grooves_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "grooves".
            """
            ...

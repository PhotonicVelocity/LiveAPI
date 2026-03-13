from types import ModuleType
from typing import Callable


class Listener(ModuleType):

    class ListenerHandle(object):
        def __init__(self, *a, **k):
            """
            This class represents a Python listener when connected to a Live property.
            """
            ...

        @property
        def listener_func(self):
            """
            Returns the original function
            """
            ...

        @property
        def listener_self(self):
            """
            Returns the weak reference to original self, if it was a bound method
            """
            ...

        @property
        def name(self):
            """
            Prints the name of the property that this listener is connected to
            """
            ...

        def disconnect(self) -> None:
            """
            Disconnects the listener from its property
            """
            ...

    class ListenerVector(object):
        def __init__(self, *a, **k):
            """
            A read only container for accessing a list of listeners.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

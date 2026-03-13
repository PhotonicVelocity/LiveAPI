from types import ModuleType
from typing import Callable


class ChainMixerDevice(ModuleType):

    class ChainMixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Chain's Mixer Device in Live, which gives youaccess to the Volume, Panning, and Send properties of a Chain.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Chain:
            """
            Get the canonical parent of the mixer device.
            """
            ...

        @property
        def chain_activator(self) -> DeviceParameter:
            """
            Const access to the Chain's Activator Device Parameter.
            """
            ...

        @property
        def panning(self) -> DeviceParameter:
            """
            Const access to the Chain's Panning Device Parameter.
            """
            ...

        @property
        def sends(self) -> tuple:
            """
            Const access to the Chain's list of Send Amount Device Parameters.
            """
            ...

        @property
        def volume(self) -> DeviceParameter:
            """
            Const access to the Chain's Volume Device Parameter.
            """
            ...

        def add_sends_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sends" has changed.
            """
            ...

        def remove_sends_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sends".
            """
            ...

        def sends_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sends".
            """
            ...

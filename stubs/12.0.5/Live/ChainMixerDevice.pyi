from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Chain import Chain
    from Live.Device import Device
    from Live.DeviceParameter import DeviceParameter
    from Live.LomObject import LomObject



class ChainMixerDevice(LomObject):
    """
    This class represents a Chain's Mixer Device in Live, which gives you
    access to the Volume, Panning, and Send properties of a Chain.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    def add_sends_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "sends" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> Chain:
        """Get the canonical parent of the mixer device."""
        ...

    @property
    def chain_activator(self) -> DeviceParameter:
        """Const access to the Chain's Activator Device Parameter."""
        ...

    @property
    def panning(self) -> DeviceParameter:
        """Const access to the Chain's Panning Device Parameter."""
        ...

    def remove_sends_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "sends".
        """
        ...

    @property
    def sends(self) -> Vector:
        """Const access to the Chain's list of Send Amount Device Parameters."""
        ...

    def sends_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "sends".
        """
        ...

    @property
    def volume(self) -> DeviceParameter:
        """Const access to the Chain's Volume Device Parameter."""
        ...

__all__ = ['ChainMixerDevice']

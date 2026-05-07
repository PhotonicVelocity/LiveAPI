from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.ChainMixerDevice import ChainMixerDevice
    from Live.LomObject import LomObject
    from Live.RackDevice import RackDevice
    from Live.Track import DeviceContainer



class Chain(DeviceContainer):
    """This class represents a group device chain in Live."""

    def add_devices_listener(self, callback: Callable[[], None], /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "devices" has changed.
        """
        ...

    def add_is_auto_colored_listener(self, callback: Callable[[], None], /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_auto_colored" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> RackDevice:
        """Get the canonical parent of the chain."""
        ...

    @property
    def devices(self) -> Vector[LomObject]:
        """Return const access to all available Devices that are present in the chains"""
        ...

    def devices_has_listener(self, callback: Callable[[], None], /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "devices".
        """
        ...

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all Audio Chains.
        """
        ...

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Chain sends out an Audio signal. This is
        true for all Audio Chains, and MIDI chains with an Instrument.
        """
        ...

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all MIDI Chains.
        """
        ...

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Chain sends out MIDI events. This is
        true for all MIDI Chains with no Instruments.
        """
        ...

    @property
    def is_auto_colored(self) -> bool:
        """
        Get/set access to the auto color flag of the Chain.
        If True, the Chain will always have the same color as the containing
        Track or Chain.
        """
        ...

    @is_auto_colored.setter
    def is_auto_colored(self, value: bool) -> None: ...

    def is_auto_colored_has_listener(self, callback: Callable[[], None], /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_auto_colored".
        """
        ...

    @property
    def mixer_device(self) -> ChainMixerDevice:
        """
        Return access to the mixer device that holds the chain's mixer parameters:
        the Volume, Pan, and Sendamounts.
        """
        ...

    def remove_devices_listener(self, callback: Callable[[], None], /) -> None:
        """
        Remove a previously set listener function or method from
        property "devices".
        """
        ...

    def remove_is_auto_colored_listener(self, callback: Callable[[], None], /) -> None:
        """
        Remove a previously set listener function or method from
        property "is_auto_colored".
        """
        ...

__all__ = ['Chain']

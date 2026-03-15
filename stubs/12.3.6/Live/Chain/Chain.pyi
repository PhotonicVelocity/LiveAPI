from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.ChainMixerDevice import ChainMixerDevice
    from Live.LomObject import LomObject
    from Live.RackDevice import RackDevice
    from Live.Track import Track
    from Live.WavetableDevice import WavetableDevice



class Chain:
    """This class represents a group device chain in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_color_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "color_index" has changed.
        """
        ...

    def add_color_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "color" has changed.
        """
        ...

    def add_devices_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "devices" has changed.
        """
        ...

    def add_is_auto_colored_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_auto_colored" has changed.
        """
        ...

    def add_mute_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mute" has changed.
        """
        ...

    def add_muted_via_solo_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "muted_via_solo" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_solo_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "solo" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> RackDevice:
        """Get the canonical parent of the chain."""
        ...

    @property
    def color(self) -> int:
        """Access the color index of the Chain."""
        ...

    @color.setter
    def color(self, value: int) -> None: ...

    def color_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "color".
        """
        ...

    @property
    def color_index(self) -> int:
        """Access the color index of the Chain."""
        ...

    @color_index.setter
    def color_index(self, value: int) -> None: ...

    def color_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "color_index".
        """
        ...

    def delete_device(self, device: int | None) -> None:
        """Remove a device identified by its index from the chain. Throws runtime error if bad index."""
        ...

    @property
    def devices(self) -> Vector[WavetableDevice]:
        """Return const access to all available Devices that are present in the chains"""
        ...

    def devices_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "devices".
        """
        ...

    def duplicate_device(self, arg2: int | None) -> None:
        """Duplicate the device at the given index in the chain."""
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

    def insert_device(self, DeviceName: str | None, DeviceIndex: int = -1) -> LomObject:
        """Add a device at a given index in the chain. At end if -1."""
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

    def is_auto_colored_has_listener(self, callback: Callable | None) -> bool:
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

    @property
    def mute(self) -> bool:
        """Mute/unmute the chain."""
        ...

    @mute.setter
    def mute(self, value: bool) -> None: ...

    def mute_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mute".
        """
        ...

    @property
    def muted_via_solo(self) -> bool:
        """
        Return const access to whether this chain is muted due to some other chain
        being soloed.
        """
        ...

    def muted_via_solo_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "muted_via_solo".
        """
        ...

    @property
    def name(self) -> str:
        """Read/write access to the name of the Chain, as visible in the track header."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def name_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    def remove_color_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "color_index".
        """
        ...

    def remove_color_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "color".
        """
        ...

    def remove_devices_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "devices".
        """
        ...

    def remove_is_auto_colored_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "is_auto_colored".
        """
        ...

    def remove_mute_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mute".
        """
        ...

    def remove_muted_via_solo_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "muted_via_solo".
        """
        ...

    def remove_name_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_solo_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "solo".
        """
        ...

    @property
    def solo(self) -> bool:
        """
        Get/Set the solo status of the chain. Note that this will not disable the
        solo state of any other Chain in the same rack. If you want exclusive solo,
        you have to disable the solo state of the other Chains manually.
        """
        ...

    @solo.setter
    def solo(self, value: bool) -> None: ...

    def solo_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "solo".
        """
        ...

__all__ = ['Chain']

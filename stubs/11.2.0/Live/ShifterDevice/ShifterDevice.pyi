from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class ShifterDevice(Device):
    """This class represents a Shifter device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_pitch_bend_range_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_bend_range" has changed.
        """
        ...

    def add_pitch_mode_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_mode_index" has changed.
        """
        ...

    @property
    def can_have_chains(self) -> bool:
        """Returns true if the device is a rack."""
        ...

    @property
    def can_have_drum_pads(self) -> bool:
        """Returns true if the device is a drum rack."""
        ...

    @property
    def canonical_parent(self) -> Track:
        """Get the canonical parent of the Device."""
        ...

    @property
    def class_display_name(self) -> str:
        """Return const access to the name of the device's class name as displayed in Live's browser and device chain"""
        ...

    @property
    def class_name(self) -> str:
        """Return const access to the name of the device's class."""
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    @property
    def pitch_bend_range(self) -> int:
        """Return the pitch bend range for MIDI pitch mode"""
        ...

    @pitch_bend_range.setter
    def pitch_bend_range(self, value: int) -> None: ...

    def pitch_bend_range_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_bend_range".
        """
        ...

    @property
    def pitch_mode_index(self) -> int:
        """Return the current pitch mode index"""
        ...

    @pitch_mode_index.setter
    def pitch_mode_index(self, value: int) -> None: ...

    def pitch_mode_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_mode_index".
        """
        ...

    @property
    def pitch_mode_list(self) -> StringVector:
        """Return the current pitch mode list"""
        ...

    def remove_pitch_bend_range_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_bend_range".
        """
        ...

    def remove_pitch_mode_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_mode_index".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> Track.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['ShifterDevice']

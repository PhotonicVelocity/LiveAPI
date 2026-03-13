from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track, View



class DrumCellDevice:
    """This class represents a DrumCell device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_gain_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "gain" has changed.
        """
        ...

    @property
    def can_compare_ab(self) -> bool:
        """Returns true if the Device has the capability to AB compare."""
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
    def gain(self) -> float:
        """Return the Gain value"""
        ...

    @gain.setter
    def gain(self, value: float) -> None: ...

    def gain_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "gain".
        """
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def is_using_compare_preset_b(self) -> bool:
        """Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."""
        ...

    @is_using_compare_preset_b.setter
    def is_using_compare_preset_b(self, value: bool) -> None: ...

    @property
    def latency_in_ms(self) -> float:
        """Returns the latency of the device in ms."""
        ...

    @property
    def latency_in_samples(self) -> int:
        """Returns the latency of the device in samples."""
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def parameters(self) -> tuple[DeviceParameter, ...]:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def remove_gain_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "gain".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['DrumCellDevice']

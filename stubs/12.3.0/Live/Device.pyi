from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.DeviceParameter import DeviceParameter
    from Live.LomObject import LomObject
    from Live.Track import Track



class Device(LomObject):
    """This class represents a MIDI or Audio DSP-Device in Live."""

    class View(LomObject):
        """Representing the view aspects of a device."""

        @property
        def _live_ptr(self) -> int:
            ...

        def add_is_collapsed_listener(self, callback: Callable | None, /) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "is_collapsed" has changed.
            """
            ...

        @property
        def canonical_parent(self) -> Device:
            """Get the canonical parent of the View."""
            ...

        @property
        def is_collapsed(self) -> bool:
            """Get/Set/Listen if the device is shown collapsed in the device chain."""
            ...

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None: ...

        def is_collapsed_has_listener(self, callback: Callable | None, /) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "is_collapsed".
            """
            ...

        def remove_is_collapsed_listener(self, callback: Callable | None, /) -> None:
            """
            Remove a previously set listener function or method from
            property "is_collapsed".
            """
            ...

    @property
    def _live_ptr(self) -> int:
        ...

    def add_is_active_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_active" has changed.
        """
        ...

    def add_is_using_compare_preset_b_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_using_compare_preset_b" has changed.
        """
        ...

    def add_latency_in_ms_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "latency_in_ms" has changed.
        """
        ...

    def add_latency_in_samples_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "latency_in_samples" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_parameters_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "parameters" has changed.
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
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    def is_active_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_active".
        """
        ...

    @property
    def is_using_compare_preset_b(self) -> bool:
        """Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."""
        ...

    @is_using_compare_preset_b.setter
    def is_using_compare_preset_b(self, value: bool) -> None: ...

    def is_using_compare_preset_b_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_using_compare_preset_b".
        """
        ...

    @property
    def latency_in_ms(self) -> float:
        """Returns the latency of the device in ms."""
        ...

    def latency_in_ms_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "latency_in_ms".
        """
        ...

    @property
    def latency_in_samples(self) -> int:
        """Returns the latency of the device in samples."""
        ...

    def latency_in_samples_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "latency_in_samples".
        """
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def name_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def parameters_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "parameters".
        """
        ...

    def remove_is_active_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "is_active".
        """
        ...

    def remove_is_using_compare_preset_b_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "is_using_compare_preset_b".
        """
        ...

    def remove_latency_in_ms_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "latency_in_ms".
        """
        ...

    def remove_latency_in_samples_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "latency_in_samples".
        """
        ...

    def remove_name_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_parameters_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "parameters".
        """
        ...

    def save_preset_to_compare_ab_slot(self) -> None:
        """Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws."""
        ...

    def store_chosen_bank(self, script_index: int | None, bank_index: int | None, /) -> None:
        """Set the selected bank in the device for persistency."""
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> View:
        """Representing the view aspects of a device."""
        ...

class ATimeableValueVector(Vector[DeviceParameter]):

    def append(self, value: DeviceParameter | None, /) -> None:
        ...

    def extend(self, values: Iterable[DeviceParameter] | None, /) -> None:
        ...

class DeviceType(int):
    """The type of the device."""
    undefined: int = 0
    instrument: int = 1
    audio_effect: int = 2
    midi_effect: int = 4

__all__ = ['Device', 'ATimeableValueVector', 'DeviceType']

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.DeviceIO import DeviceIO
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class MaxDevice(Device):
    """This class represents a Max for Live device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_audio_inputs_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "audio_inputs" has changed.
        """
        ...

    def add_audio_outputs_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "audio_outputs" has changed.
        """
        ...

    def add_bank_parameters_changed_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "bank_parameters_changed" has changed.
        """
        ...

    def add_midi_inputs_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_inputs" has changed.
        """
        ...

    def add_midi_outputs_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_outputs" has changed.
        """
        ...

    @property
    def audio_inputs(self) -> Vector[DeviceIO]:
        """Const access to a list of all audio inputs of the device."""
        ...

    def audio_inputs_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "audio_inputs".
        """
        ...

    @property
    def audio_outputs(self) -> Vector[DeviceIO]:
        """Const access to a list of all audio outputs of the device."""
        ...

    def audio_outputs_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "audio_outputs".
        """
        ...

    def bank_parameters_changed_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "bank_parameters_changed".
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

    def get_bank_count(self) -> int:
        """Get the number of parameter banks. This is related to hardware control surfaces."""
        ...

    def get_bank_name(self, bank_index: int | None, /) -> str:
        """Get the name of a parameter bank given by index. This is related to hardware control surfaces."""
        ...

    def get_bank_parameters(self, bank_index: int | None, /) -> list[int]:
        """Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces."""
        ...

    def get_value_item_icons(self, parameter: DeviceParameter | None, /) -> list[str]:
        """Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces."""
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
    def midi_inputs(self) -> Vector:
        """Const access to a list of all midi outputs of the device."""
        ...

    def midi_inputs_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_inputs".
        """
        ...

    @property
    def midi_outputs(self) -> Vector:
        """Const access to a list of all midi outputs of the device."""
        ...

    def midi_outputs_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_outputs".
        """
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

    def remove_audio_inputs_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "audio_inputs".
        """
        ...

    def remove_audio_outputs_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "audio_outputs".
        """
        ...

    def remove_bank_parameters_changed_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "bank_parameters_changed".
        """
        ...

    def remove_midi_inputs_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_inputs".
        """
        ...

    def remove_midi_outputs_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_outputs".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> Device.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['MaxDevice']

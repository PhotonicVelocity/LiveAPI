from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class SpectralResonatorDevice(Device):
    """This class represents a Spectral Resonator device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_frequency_dial_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "frequency_dial_mode_list" has changed.
        """
        ...

    def add_frequency_dial_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "frequency_dial_mode" has changed.
        """
        ...

    def add_midi_gate_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_gate_list" has changed.
        """
        ...

    def add_midi_gate_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_gate" has changed.
        """
        ...

    def add_mod_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_mode_list" has changed.
        """
        ...

    def add_mod_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_mode" has changed.
        """
        ...

    def add_mono_poly_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mono_poly_list" has changed.
        """
        ...

    def add_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mono_poly" has changed.
        """
        ...

    def add_pitch_bend_range_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_bend_range" has changed.
        """
        ...

    def add_pitch_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_mode_list" has changed.
        """
        ...

    def add_pitch_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_mode" has changed.
        """
        ...

    def add_polyphony_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "polyphony" has changed.
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
    def frequency_dial_mode(self) -> int:
        """Return the current frequency dial mode index"""
        ...

    @frequency_dial_mode.setter
    def frequency_dial_mode(self, value: int) -> None: ...

    def frequency_dial_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "frequency_dial_mode".
        """
        ...

    @property
    def frequency_dial_mode_list(self) -> StringVector:
        """Return the current frequency dial mode list"""
        ...

    def frequency_dial_mode_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "frequency_dial_mode_list".
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
    def midi_gate(self) -> int:
        """Return the current midi gate index"""
        ...

    @midi_gate.setter
    def midi_gate(self, value: int) -> None: ...

    def midi_gate_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_gate".
        """
        ...

    @property
    def midi_gate_list(self) -> StringVector:
        """Return the current midi gate list"""
        ...

    def midi_gate_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_gate_list".
        """
        ...

    @property
    def mod_mode(self) -> int:
        """Return the current mod mode index"""
        ...

    @mod_mode.setter
    def mod_mode(self, value: int) -> None: ...

    def mod_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_mode".
        """
        ...

    @property
    def mod_mode_list(self) -> StringVector:
        """Return the current mod mode list"""
        ...

    def mod_mode_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_mode_list".
        """
        ...

    @property
    def mono_poly(self) -> int:
        """Return the current mono poly mode index"""
        ...

    @mono_poly.setter
    def mono_poly(self, value: int) -> None: ...

    def mono_poly_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mono_poly".
        """
        ...

    @property
    def mono_poly_list(self) -> StringVector:
        """Return the current mono poly mode list"""
        ...

    def mono_poly_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mono_poly_list".
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

    @property
    def pitch_bend_range(self) -> int:
        """Return the current pitch bend range"""
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
    def pitch_mode(self) -> int:
        """Return the current pitch mode index"""
        ...

    @pitch_mode.setter
    def pitch_mode(self, value: int) -> None: ...

    def pitch_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_mode".
        """
        ...

    @property
    def pitch_mode_list(self) -> StringVector:
        """Return the current pitch mode list"""
        ...

    def pitch_mode_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_mode_list".
        """
        ...

    @property
    def polyphony(self) -> int:
        """Return the current polyphony"""
        ...

    @polyphony.setter
    def polyphony(self, value: int) -> None: ...

    def polyphony_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "polyphony".
        """
        ...

    def remove_frequency_dial_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "frequency_dial_mode_list".
        """
        ...

    def remove_frequency_dial_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "frequency_dial_mode".
        """
        ...

    def remove_midi_gate_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_gate_list".
        """
        ...

    def remove_midi_gate_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_gate".
        """
        ...

    def remove_mod_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_mode_list".
        """
        ...

    def remove_mod_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_mode".
        """
        ...

    def remove_mono_poly_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mono_poly_list".
        """
        ...

    def remove_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mono_poly".
        """
        ...

    def remove_pitch_bend_range_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_bend_range".
        """
        ...

    def remove_pitch_mode_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_mode_list".
        """
        ...

    def remove_pitch_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_mode".
        """
        ...

    def remove_polyphony_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "polyphony".
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

__all__ = ['SpectralResonatorDevice']

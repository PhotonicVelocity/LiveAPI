from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class DriftDevice:
    """This class represents a Drift device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_mod_matrix_filter_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_filter_source_1_index" has changed.
        """
        ...

    def add_mod_matrix_filter_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_filter_source_2_index" has changed.
        """
        ...

    def add_mod_matrix_lfo_source_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_lfo_source_index" has changed.
        """
        ...

    def add_mod_matrix_pitch_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_pitch_source_1_index" has changed.
        """
        ...

    def add_mod_matrix_pitch_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_pitch_source_2_index" has changed.
        """
        ...

    def add_mod_matrix_shape_source_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_shape_source_index" has changed.
        """
        ...

    def add_mod_matrix_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_source_1_index" has changed.
        """
        ...

    def add_mod_matrix_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_source_2_index" has changed.
        """
        ...

    def add_mod_matrix_source_3_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_source_3_index" has changed.
        """
        ...

    def add_mod_matrix_target_1_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_target_1_index" has changed.
        """
        ...

    def add_mod_matrix_target_2_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_target_2_index" has changed.
        """
        ...

    def add_mod_matrix_target_3_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mod_matrix_target_3_index" has changed.
        """
        ...

    def add_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_bend_range" has changed.
        """
        ...

    def add_voice_count_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "voice_count_index" has changed.
        """
        ...

    def add_voice_mode_index_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "voice_mode_index" has changed.
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
    def mod_matrix_filter_source_1_index(self) -> int:
        """Return the filter mod source 1 index"""
        ...

    @mod_matrix_filter_source_1_index.setter
    def mod_matrix_filter_source_1_index(self, value: int) -> None: ...

    def mod_matrix_filter_source_1_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_filter_source_1_index".
        """
        ...

    @property
    def mod_matrix_filter_source_1_list(self) -> StringVector:
        """Return the filter mod source 1 list"""
        ...

    @property
    def mod_matrix_filter_source_2_index(self) -> int:
        """Return the filter mod source 2 index"""
        ...

    @mod_matrix_filter_source_2_index.setter
    def mod_matrix_filter_source_2_index(self, value: int) -> None: ...

    def mod_matrix_filter_source_2_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_filter_source_2_index".
        """
        ...

    @property
    def mod_matrix_filter_source_2_list(self) -> StringVector:
        """Return the filter mod source 2 list"""
        ...

    @property
    def mod_matrix_lfo_source_index(self) -> int:
        """Return the lfo mod source index"""
        ...

    @mod_matrix_lfo_source_index.setter
    def mod_matrix_lfo_source_index(self, value: int) -> None: ...

    def mod_matrix_lfo_source_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_lfo_source_index".
        """
        ...

    @property
    def mod_matrix_lfo_source_list(self) -> StringVector:
        """Return the lfo mod source list"""
        ...

    @property
    def mod_matrix_pitch_source_1_index(self) -> int:
        """Return the pitch mod source 1 index"""
        ...

    @mod_matrix_pitch_source_1_index.setter
    def mod_matrix_pitch_source_1_index(self, value: int) -> None: ...

    def mod_matrix_pitch_source_1_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_pitch_source_1_index".
        """
        ...

    @property
    def mod_matrix_pitch_source_1_list(self) -> StringVector:
        """Return the pitch mod source 1 list"""
        ...

    @property
    def mod_matrix_pitch_source_2_index(self) -> int:
        """Return the pitch mod source 2 index"""
        ...

    @mod_matrix_pitch_source_2_index.setter
    def mod_matrix_pitch_source_2_index(self, value: int) -> None: ...

    def mod_matrix_pitch_source_2_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_pitch_source_2_index".
        """
        ...

    @property
    def mod_matrix_pitch_source_2_list(self) -> StringVector:
        """Return the pitch mod source 2 list"""
        ...

    @property
    def mod_matrix_shape_source_index(self) -> int:
        """Return the shape mod source index"""
        ...

    @mod_matrix_shape_source_index.setter
    def mod_matrix_shape_source_index(self, value: int) -> None: ...

    def mod_matrix_shape_source_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_shape_source_index".
        """
        ...

    @property
    def mod_matrix_shape_source_list(self) -> StringVector:
        """Return the shape mod source list"""
        ...

    @property
    def mod_matrix_source_1_index(self) -> int:
        """Return the custom mod source 1 index"""
        ...

    @mod_matrix_source_1_index.setter
    def mod_matrix_source_1_index(self, value: int) -> None: ...

    def mod_matrix_source_1_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_source_1_index".
        """
        ...

    @property
    def mod_matrix_source_1_list(self) -> StringVector:
        """Return the custom mod source 1 list"""
        ...

    @property
    def mod_matrix_source_2_index(self) -> int:
        """Return the custom mod source 2 index"""
        ...

    @mod_matrix_source_2_index.setter
    def mod_matrix_source_2_index(self, value: int) -> None: ...

    def mod_matrix_source_2_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_source_2_index".
        """
        ...

    @property
    def mod_matrix_source_2_list(self) -> StringVector:
        """Return the custom mod source 2 list"""
        ...

    @property
    def mod_matrix_source_3_index(self) -> int:
        """Return the custom mod source 3 index"""
        ...

    @mod_matrix_source_3_index.setter
    def mod_matrix_source_3_index(self, value: int) -> None: ...

    def mod_matrix_source_3_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_source_3_index".
        """
        ...

    @property
    def mod_matrix_source_3_list(self) -> StringVector:
        """Return the custom mod source 3 list"""
        ...

    @property
    def mod_matrix_target_1_index(self) -> int:
        """Return the custom mod target 1 index"""
        ...

    @mod_matrix_target_1_index.setter
    def mod_matrix_target_1_index(self, value: int) -> None: ...

    def mod_matrix_target_1_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_target_1_index".
        """
        ...

    @property
    def mod_matrix_target_1_list(self) -> StringVector:
        """Return the custom mod target 1 list"""
        ...

    @property
    def mod_matrix_target_2_index(self) -> int:
        """Return the custom mod target 2 index"""
        ...

    @mod_matrix_target_2_index.setter
    def mod_matrix_target_2_index(self, value: int) -> None: ...

    def mod_matrix_target_2_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_target_2_index".
        """
        ...

    @property
    def mod_matrix_target_2_list(self) -> StringVector:
        """Return the custom mod target 2 list"""
        ...

    @property
    def mod_matrix_target_3_index(self) -> int:
        """Return the custom mod target 3 index"""
        ...

    @mod_matrix_target_3_index.setter
    def mod_matrix_target_3_index(self, value: int) -> None: ...

    def mod_matrix_target_3_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mod_matrix_target_3_index".
        """
        ...

    @property
    def mod_matrix_target_3_list(self) -> StringVector:
        """Return the custom mod target 3 list"""
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
        """Return the Pitch Bend Range"""
        ...

    @pitch_bend_range.setter
    def pitch_bend_range(self, value: int) -> None: ...

    def pitch_bend_range_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_bend_range".
        """
        ...

    def remove_mod_matrix_filter_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_filter_source_1_index".
        """
        ...

    def remove_mod_matrix_filter_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_filter_source_2_index".
        """
        ...

    def remove_mod_matrix_lfo_source_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_lfo_source_index".
        """
        ...

    def remove_mod_matrix_pitch_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_pitch_source_1_index".
        """
        ...

    def remove_mod_matrix_pitch_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_pitch_source_2_index".
        """
        ...

    def remove_mod_matrix_shape_source_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_shape_source_index".
        """
        ...

    def remove_mod_matrix_source_1_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_source_1_index".
        """
        ...

    def remove_mod_matrix_source_2_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_source_2_index".
        """
        ...

    def remove_mod_matrix_source_3_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_source_3_index".
        """
        ...

    def remove_mod_matrix_target_1_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_target_1_index".
        """
        ...

    def remove_mod_matrix_target_2_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_target_2_index".
        """
        ...

    def remove_mod_matrix_target_3_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mod_matrix_target_3_index".
        """
        ...

    def remove_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_bend_range".
        """
        ...

    def remove_voice_count_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "voice_count_index".
        """
        ...

    def remove_voice_mode_index_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "voice_mode_index".
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

    @property
    def voice_count_index(self) -> int:
        """Return the voice count index"""
        ...

    @voice_count_index.setter
    def voice_count_index(self, value: int) -> None: ...

    def voice_count_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "voice_count_index".
        """
        ...

    @property
    def voice_count_list(self) -> StringVector:
        """Return the voice count list"""
        ...

    @property
    def voice_mode_index(self) -> int:
        """Return the voice mode index"""
        ...

    @voice_mode_index.setter
    def voice_mode_index(self, value: int) -> None: ...

    def voice_mode_index_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "voice_mode_index".
        """
        ...

    @property
    def voice_mode_list(self) -> StringVector:
        """Return the voice mode list"""
        ...

__all__ = ['DriftDevice']

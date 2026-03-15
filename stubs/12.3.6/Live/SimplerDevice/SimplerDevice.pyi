from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Sample import Sample
    from Live.Track import Track



class SimplerDevice:
    """This class represents a Simpler device."""

    class View:
        """Representing the view aspects of a simpler device."""

        @property
        def _live_ptr(self) -> int:
            ...

        def add_sample_end_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_end" has changed.
            """
            ...

        def add_sample_env_fade_in_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_env_fade_in" has changed.
            """
            ...

        def add_sample_env_fade_out_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_env_fade_out" has changed.
            """
            ...

        def add_sample_loop_end_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_loop_end" has changed.
            """
            ...

        def add_sample_loop_fade_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_loop_fade" has changed.
            """
            ...

        def add_sample_loop_start_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_loop_start" has changed.
            """
            ...

        def add_sample_start_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "sample_start" has changed.
            """
            ...

        def add_selected_slice_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_slice" has changed.
            """
            ...

        @property
        def canonical_parent(self) -> SimplerDevice:
            """Get the canonical parent of the View."""
            ...

        @property
        def is_collapsed(self) -> bool:
            """Get/Set/Listen if the device is shown collapsed in the device chain."""
            ...

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None: ...

        def remove_sample_end_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_end".
            """
            ...

        def remove_sample_env_fade_in_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_env_fade_in".
            """
            ...

        def remove_sample_env_fade_out_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_env_fade_out".
            """
            ...

        def remove_sample_loop_end_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_loop_end".
            """
            ...

        def remove_sample_loop_fade_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_loop_fade".
            """
            ...

        def remove_sample_loop_start_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_loop_start".
            """
            ...

        def remove_sample_start_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "sample_start".
            """
            ...

        def remove_selected_slice_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_slice".
            """
            ...

        @property
        def sample_end(self) -> int:
            """Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded."""
            ...

        def sample_end_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_end".
            """
            ...

        @property
        def sample_env_fade_in(self) -> int:
            """Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded."""
            ...

        def sample_env_fade_in_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_env_fade_in".
            """
            ...

        @property
        def sample_env_fade_out(self) -> int:
            """Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded."""
            ...

        def sample_env_fade_out_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_env_fade_out".
            """
            ...

        @property
        def sample_loop_end(self) -> int:
            """Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded."""
            ...

        def sample_loop_end_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_loop_end".
            """
            ...

        @property
        def sample_loop_fade(self) -> int:
            """Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded."""
            ...

        def sample_loop_fade_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_loop_fade".
            """
            ...

        @property
        def sample_loop_start(self) -> int:
            """Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded."""
            ...

        def sample_loop_start_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_loop_start".
            """
            ...

        @property
        def sample_start(self) -> int:
            """Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded."""
            ...

        def sample_start_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "sample_start".
            """
            ...

        @property
        def selected_slice(self) -> int:
            """Access to the selected slice."""
            ...

        @selected_slice.setter
        def selected_slice(self, value: int) -> None: ...

        def selected_slice_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_slice".
            """
            ...

    @property
    def _live_ptr(self) -> int:
        ...

    def add_can_warp_as_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_warp_as" has changed.
        """
        ...

    def add_can_warp_double_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_warp_double" has changed.
        """
        ...

    def add_can_warp_half_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_warp_half" has changed.
        """
        ...

    def add_multi_sample_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "multi_sample_mode" has changed.
        """
        ...

    def add_note_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "note_pitch_bend_range" has changed.
        """
        ...

    def add_pad_slicing_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pad_slicing" has changed.
        """
        ...

    def add_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "pitch_bend_range" has changed.
        """
        ...

    def add_playback_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "playback_mode" has changed.
        """
        ...

    def add_playing_position_enabled_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "playing_position_enabled" has changed.
        """
        ...

    def add_playing_position_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "playing_position" has changed.
        """
        ...

    def add_retrigger_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "retrigger" has changed.
        """
        ...

    def add_sample_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "sample" has changed.
        """
        ...

    def add_slicing_playback_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "slicing_playback_mode" has changed.
        """
        ...

    def add_voices_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "voices" has changed.
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
    def can_warp_as(self) -> bool:
        """Returns true if warp_as is available."""
        ...

    def can_warp_as_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_warp_as".
        """
        ...

    @property
    def can_warp_double(self) -> bool:
        """Returns true if warp_double is available."""
        ...

    def can_warp_double_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_warp_double".
        """
        ...

    @property
    def can_warp_half(self) -> bool:
        """Returns true if warp_half is available."""
        ...

    def can_warp_half_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_warp_half".
        """
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

    def crop(self) -> None:
        """
        Crop the loaded sample to the active area between start- and end marker.
        Calling this method on an empty simpler raises an error.
        """
        ...

    def guess_playback_length(self) -> float:
        """
        Return an estimated beat time for the playback length between start- and end-marker.
        Calling this method on an empty simpler raises an error.
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
    def multi_sample_mode(self) -> bool:
        """Returns whether Simpler is in mulit-sample mode."""
        ...

    def multi_sample_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "multi_sample_mode".
        """
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def note_pitch_bend_range(self) -> int:
        """Access to the Note Pitch Bend Range in Simpler."""
        ...

    @note_pitch_bend_range.setter
    def note_pitch_bend_range(self, value: int) -> None: ...

    def note_pitch_bend_range_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "note_pitch_bend_range".
        """
        ...

    @property
    def pad_slicing(self) -> bool:
        """
        When set to true, slices can be added in slicing mode by playing notes
        .that are not assigned to slices, yet.
        """
        ...

    @pad_slicing.setter
    def pad_slicing(self, value: bool) -> None: ...

    def pad_slicing_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pad_slicing".
        """
        ...

    @property
    def parameters(self) -> Vector[DeviceParameter]:
        """Const access to the list of available automatable parameters for this device."""
        ...

    @property
    def pitch_bend_range(self) -> int:
        """Access to the Pitch Bend Range in Simpler."""
        ...

    @pitch_bend_range.setter
    def pitch_bend_range(self, value: int) -> None: ...

    def pitch_bend_range_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "pitch_bend_range".
        """
        ...

    @property
    def playback_mode(self) -> int:
        """Access to Simpler's playback mode."""
        ...

    @playback_mode.setter
    def playback_mode(self, value: int) -> None: ...

    def playback_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "playback_mode".
        """
        ...

    @property
    def playing_position(self) -> float:
        """
        Constant access to the current playing position in the sample.
        The returned value is the normalized position between sample start and end.
        """
        ...

    @property
    def playing_position_enabled(self) -> bool:
        """
        Returns whether Simpler is showing the playing position.
        The returned value is True while the sample is played back
        """
        ...

    def playing_position_enabled_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "playing_position_enabled".
        """
        ...

    def playing_position_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "playing_position".
        """
        ...

    def remove_can_warp_as_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_warp_as".
        """
        ...

    def remove_can_warp_double_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_warp_double".
        """
        ...

    def remove_can_warp_half_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_warp_half".
        """
        ...

    def remove_multi_sample_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "multi_sample_mode".
        """
        ...

    def remove_note_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "note_pitch_bend_range".
        """
        ...

    def remove_pad_slicing_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "pad_slicing".
        """
        ...

    def remove_pitch_bend_range_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "pitch_bend_range".
        """
        ...

    def remove_playback_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "playback_mode".
        """
        ...

    def remove_playing_position_enabled_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "playing_position_enabled".
        """
        ...

    def remove_playing_position_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "playing_position".
        """
        ...

    def remove_retrigger_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "retrigger".
        """
        ...

    def remove_sample_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "sample".
        """
        ...

    def remove_slicing_playback_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "slicing_playback_mode".
        """
        ...

    def remove_voices_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "voices".
        """
        ...

    @property
    def retrigger(self) -> bool:
        """Access to Simpler's retrigger mode."""
        ...

    @retrigger.setter
    def retrigger(self, value: bool) -> None: ...

    def retrigger_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "retrigger".
        """
        ...

    def reverse(self) -> None:
        """
        Reverse the loaded sample.
        Calling this method on an empty simpler raises an error.
        """
        ...

    @property
    def sample(self) -> Sample:
        """Get the loaded Sample."""
        ...

    def sample_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "sample".
        """
        ...

    @property
    def slicing_playback_mode(self) -> int:
        """Access to Simpler's slicing playback mode."""
        ...

    @slicing_playback_mode.setter
    def slicing_playback_mode(self, value: int) -> None: ...

    def slicing_playback_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "slicing_playback_mode".
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

    @property
    def voices(self) -> int:
        """Access to the number of voices in Simpler."""
        ...

    @voices.setter
    def voices(self, value: int) -> None: ...

    def voices_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "voices".
        """
        ...

    def warp_as(self, beat_time: float | None) -> None:
        """
        Warp the playback region between start- and end-marker as the given length.
        Calling this method on an empty simpler raises an error.
        """
        ...

    def warp_double(self) -> None:
        """Doubles the tempo for region between start- and end-marker."""
        ...

    def warp_half(self) -> None:
        """Halves the tempo for region between start- and end-marker."""
        ...

__all__ = ['SimplerDevice']

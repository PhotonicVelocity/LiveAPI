from types import ModuleType
from typing import Callable


class SimplerDevice(ModuleType):

    @staticmethod
    def get_available_voice_numbers() -> IntVector:
        """
        Get a vector of valid Simpler voice numbers.
        """
        ...

    class PlaybackMode:
        classic: int = 0
        one_shot: int = 1
        slicing: int = 2

    class SimplerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Simpler device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def can_warp_as(self) -> bool:
            """
            Returns true if warp_as is available.
            """
            ...

        @property
        def can_warp_double(self) -> bool:
            """
            Returns true if warp_double is available.
            """
            ...

        @property
        def can_warp_half(self) -> bool:
            """
            Returns true if warp_half is available.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def multi_sample_mode(self) -> bool:
            """
            Returns whether Simpler is in mulit-sample mode.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def pad_slicing(self) -> bool:
            """
            When set to true, slices can be added in slicing mode by playing notes .that are not assigned to slices, yet.
            """
            ...

        @pad_slicing.setter
        def pad_slicing(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def playback_mode(self) -> int:
            """
            Access to Simpler's playback mode.
            """
            ...

        @playback_mode.setter
        def playback_mode(self, value) -> None:
            ...

        @property
        def playing_position(self) -> float:
            """
            Constant access to the current playing position in the sample.The returned value is the normalized position between sample start and end.
            """
            ...

        @property
        def playing_position_enabled(self) -> bool:
            """
            Returns whether Simpler is showing the playing position.The returned value is True while the sample is played back
            """
            ...

        @property
        def retrigger(self) -> bool:
            """
            Access to Simpler's retrigger mode.
            """
            ...

        @retrigger.setter
        def retrigger(self, value) -> None:
            ...

        @property
        def sample(self) -> None:
            """
            Get the loaded Sample.
            """
            ...

        @property
        def slicing_playback_mode(self) -> int:
            """
            Access to Simpler's slicing playback mode.
            """
            ...

        @slicing_playback_mode.setter
        def slicing_playback_mode(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def voices(self) -> int:
            """
            Access to the number of voices in Simpler.
            """
            ...

        @voices.setter
        def voices(self, value) -> None:
            ...

        def add_can_warp_as_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_as" has changed.
            """
            ...

        def add_can_warp_double_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_double" has changed.
            """
            ...

        def add_can_warp_half_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_half" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_multi_sample_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "multi_sample_mode" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_pad_slicing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pad_slicing" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playback_mode" has changed.
            """
            ...

        def add_playing_position_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_position_enabled" has changed.
            """
            ...

        def add_playing_position_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_position" has changed.
            """
            ...

        def add_retrigger_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "retrigger" has changed.
            """
            ...

        def add_sample_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sample" has changed.
            """
            ...

        def add_slicing_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_playback_mode" has changed.
            """
            ...

        def add_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "voices" has changed.
            """
            ...

        def can_warp_as_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_as".
            """
            ...

        def can_warp_double_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_double".
            """
            ...

        def can_warp_half_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_half".
            """
            ...

        def crop(self) -> None:
            """
            Crop the loaded sample to the active area between start- and end marker. Calling this method on an empty simpler raises an error.
            """
            ...

        def guess_playback_length(self) -> float:
            """
            Return an estimated beat time for the playback length between start- and end-marker. Calling this method on an empty simpler raises an error.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def multi_sample_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "multi_sample_mode".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def pad_slicing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pad_slicing".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def playback_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playback_mode".
            """
            ...

        def playing_position_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_position_enabled".
            """
            ...

        def playing_position_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_position".
            """
            ...

        def remove_can_warp_as_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_as".
            """
            ...

        def remove_can_warp_double_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_double".
            """
            ...

        def remove_can_warp_half_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_half".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_multi_sample_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "multi_sample_mode".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_pad_slicing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pad_slicing".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playback_mode".
            """
            ...

        def remove_playing_position_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_position_enabled".
            """
            ...

        def remove_playing_position_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_position".
            """
            ...

        def remove_retrigger_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "retrigger".
            """
            ...

        def remove_sample_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sample".
            """
            ...

        def remove_slicing_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_playback_mode".
            """
            ...

        def remove_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "voices".
            """
            ...

        def retrigger_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "retrigger".
            """
            ...

        def reverse(self) -> None:
            """
            Reverse the loaded sample. Calling this method on an empty simpler raises an error.
            """
            ...

        def sample_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample".
            """
            ...

        def slicing_playback_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_playback_mode".
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "voices".
            """
            ...

        def warp_as(self, beat_time: float) -> None:
            """
            Warp the playback region between start- and end-marker as the given length. Calling this method on an empty simpler raises an error.
            """
            ...

        def warp_double(self) -> None:
            """
            Doubles the tempo for region between start- and end-marker.
            """
            ...

        def warp_half(self) -> None:
            """
            Halves the tempo for region between start- and end-marker.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a simpler device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> SimplerDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            @property
            def sample_end(self) -> int:
                """
                Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_env_fade_in(self) -> int:
                """
                Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_env_fade_out(self) -> int:
                """
                Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_end(self) -> int:
                """
                Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_fade(self) -> int:
                """
                Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_start(self) -> int:
                """
                Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_start(self) -> int:
                """
                Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def selected_slice(self) -> int:
                """
                Access to the selected slice.
                """
                ...

            @selected_slice.setter
            def selected_slice(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_sample_end_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_end" has changed.
                """
                ...

            def add_sample_env_fade_in_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_env_fade_in" has changed.
                """
                ...

            def add_sample_env_fade_out_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_env_fade_out" has changed.
                """
                ...

            def add_sample_loop_end_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_end" has changed.
                """
                ...

            def add_sample_loop_fade_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_fade" has changed.
                """
                ...

            def add_sample_loop_start_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_start" has changed.
                """
                ...

            def add_sample_start_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_start" has changed.
                """
                ...

            def add_selected_slice_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_slice" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_sample_end_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_end".
                """
                ...

            def remove_sample_env_fade_in_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_env_fade_in".
                """
                ...

            def remove_sample_env_fade_out_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_env_fade_out".
                """
                ...

            def remove_sample_loop_end_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_end".
                """
                ...

            def remove_sample_loop_fade_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_fade".
                """
                ...

            def remove_sample_loop_start_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_start".
                """
                ...

            def remove_sample_start_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_start".
                """
                ...

            def remove_selected_slice_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_slice".
                """
                ...

            def sample_end_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_end".
                """
                ...

            def sample_env_fade_in_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_env_fade_in".
                """
                ...

            def sample_env_fade_out_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_env_fade_out".
                """
                ...

            def sample_loop_end_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_end".
                """
                ...

            def sample_loop_fade_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_fade".
                """
                ...

            def sample_loop_start_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_start".
                """
                ...

            def sample_start_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_start".
                """
                ...

            def selected_slice_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_slice".
                """
                ...

    class SlicingPlaybackMode:
        mono: int = 0
        poly: int = 1
        thru: int = 2

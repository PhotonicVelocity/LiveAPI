from types import ModuleType
from typing import Callable


class Sample(ModuleType):

    class Sample(object):
        def __init__(self, *a, **k):
            """
            This class represents a sample file loaded into a Simpler instance.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def beats_granulation_resolution(self) -> int:
            """
            Access to the Granulation Resolution parameter in Beats Warp Mode.
            """
            ...

        @beats_granulation_resolution.setter
        def beats_granulation_resolution(self, value) -> None:
            ...

        @property
        def beats_transient_envelope(self) -> float:
            """
            Access to the Transient Envelope parameter in Beats Warp Mode.
            """
            ...

        @beats_transient_envelope.setter
        def beats_transient_envelope(self, value) -> None:
            ...

        @property
        def beats_transient_loop_mode(self) -> int:
            """
            Access to the Transient Loop Mode parameter in Beats Warp Mode.
            """
            ...

        @beats_transient_loop_mode.setter
        def beats_transient_loop_mode(self, value) -> None:
            ...

        @property
        def canonical_parent(self) -> SimplerDevice:
            """
            Access to the sample's canonical parent.
            """
            ...

        @property
        def complex_pro_envelope(self) -> float:
            """
            Access to the Envelope parameter in Complex Pro Mode.
            """
            ...

        @complex_pro_envelope.setter
        def complex_pro_envelope(self, value) -> None:
            ...

        @property
        def complex_pro_formants(self) -> float:
            """
            Access to the Formants parameter in Complex Pro Warp Mode.
            """
            ...

        @complex_pro_formants.setter
        def complex_pro_formants(self, value) -> None:
            ...

        @property
        def end_marker(self) -> int:
            """
            Access to the position of the sample's end marker.
            """
            ...

        @end_marker.setter
        def end_marker(self, value) -> None:
            ...

        @property
        def file_path(self) -> str:
            """
            Get the path of the sample file.
            """
            ...

        @property
        def gain(self) -> float:
            """
            Access to the sample gain.
            """
            ...

        @gain.setter
        def gain(self, value) -> None:
            ...

        @property
        def length(self) -> int:
            """
            Get the length of the sample file in sample frames.
            """
            ...

        @property
        def sample_rate(self) -> float:
            """
            Access to the audio sample rate of the sample.
            """
            ...

        @property
        def slices(self) -> tuple:
            """
            Access to the list of slice points in sample time in the sample.
            """
            ...

        @property
        def slicing_beat_division(self) -> int:
            """
            Access to sample's slicing step size.
            """
            ...

        @slicing_beat_division.setter
        def slicing_beat_division(self, value) -> None:
            ...

        @property
        def slicing_region_count(self) -> int:
            """
            Access to sample's slicing split count.
            """
            ...

        @slicing_region_count.setter
        def slicing_region_count(self, value) -> None:
            ...

        @property
        def slicing_sensitivity(self) -> float:
            """
            Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.The higher the sensitivity, the more slices will be available.
            """
            ...

        @slicing_sensitivity.setter
        def slicing_sensitivity(self, value) -> None:
            ...

        @property
        def slicing_style(self) -> int:
            """
            Access to sample's slicing style.
            """
            ...

        @slicing_style.setter
        def slicing_style(self, value) -> None:
            ...

        @property
        def start_marker(self) -> int:
            """
            Access to the position of the sample's start marker.
            """
            ...

        @start_marker.setter
        def start_marker(self, value) -> None:
            ...

        @property
        def texture_flux(self) -> float:
            """
            Access to the Flux parameter in Texture Warp Mode.
            """
            ...

        @texture_flux.setter
        def texture_flux(self, value) -> None:
            ...

        @property
        def texture_grain_size(self) -> float:
            """
            Access to the Grain Size parameter in Texture Warp Mode.
            """
            ...

        @texture_grain_size.setter
        def texture_grain_size(self, value) -> None:
            ...

        @property
        def tones_grain_size(self) -> float:
            """
            Access to the Grain Size parameter in Tones Warp Mode.
            """
            ...

        @tones_grain_size.setter
        def tones_grain_size(self, value) -> None:
            ...

        @property
        def warp_markers(self) -> tuple[WarpMarker, ...]:
            """
            Get the warp markers for this sample.
            """
            ...

        @property
        def warp_mode(self) -> int:
            """
            Access to the sample's warp mode.
            """
            ...

        @warp_mode.setter
        def warp_mode(self, value) -> None:
            ...

        @property
        def warping(self) -> bool:
            """
            Access to the sample's warping property.
            """
            ...

        @warping.setter
        def warping(self, value) -> None:
            ...

        def add_beats_granulation_resolution_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_granulation_resolution" has changed.
            """
            ...

        def add_beats_transient_envelope_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_transient_envelope" has changed.
            """
            ...

        def add_beats_transient_loop_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_transient_loop_mode" has changed.
            """
            ...

        def add_complex_pro_envelope_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "complex_pro_envelope" has changed.
            """
            ...

        def add_complex_pro_formants_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "complex_pro_formants" has changed.
            """
            ...

        def add_end_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "end_marker" has changed.
            """
            ...

        def add_file_path_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "file_path" has changed.
            """
            ...

        def add_gain_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "gain" has changed.
            """
            ...

        def add_slices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slices" has changed.
            """
            ...

        def add_slicing_beat_division_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_beat_division" has changed.
            """
            ...

        def add_slicing_region_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_region_count" has changed.
            """
            ...

        def add_slicing_sensitivity_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_sensitivity" has changed.
            """
            ...

        def add_slicing_style_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_style" has changed.
            """
            ...

        def add_start_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "start_marker" has changed.
            """
            ...

        def add_texture_flux_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "texture_flux" has changed.
            """
            ...

        def add_texture_grain_size_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "texture_grain_size" has changed.
            """
            ...

        def add_tones_grain_size_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tones_grain_size" has changed.
            """
            ...

        def add_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_markers" has changed.
            """
            ...

        def add_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_mode" has changed.
            """
            ...

        def add_warping_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warping" has changed.
            """
            ...

        def beat_to_sample_time(self, beat_time: float) -> float:
            """
            Converts the given beat time to sample time. Raises an error if the sample is not warped.
            """
            ...

        def beats_granulation_resolution_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_granulation_resolution".
            """
            ...

        def beats_transient_envelope_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_transient_envelope".
            """
            ...

        def beats_transient_loop_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_transient_loop_mode".
            """
            ...

        def clear_slices(self) -> None:
            """
            Clears all slices created in Simpler's manual mode.
            """
            ...

        def complex_pro_envelope_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "complex_pro_envelope".
            """
            ...

        def complex_pro_formants_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "complex_pro_formants".
            """
            ...

        def end_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "end_marker".
            """
            ...

        def file_path_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "file_path".
            """
            ...

        def gain_display_string(self) -> str:
            """
            Get the gain's display value as a string.
            """
            ...

        def gain_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "gain".
            """
            ...

        def insert_slice(self, slice_time: int) -> None:
            """
            Add a slice point at the provided time if there is none.
            """
            ...

        def move_slice(self, old_time: int, new_time: int) -> int:
            """
            Move the slice point at the provided time.
            """
            ...

        def remove_beats_granulation_resolution_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_granulation_resolution".
            """
            ...

        def remove_beats_transient_envelope_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_transient_envelope".
            """
            ...

        def remove_beats_transient_loop_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_transient_loop_mode".
            """
            ...

        def remove_complex_pro_envelope_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "complex_pro_envelope".
            """
            ...

        def remove_complex_pro_formants_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "complex_pro_formants".
            """
            ...

        def remove_end_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "end_marker".
            """
            ...

        def remove_file_path_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "file_path".
            """
            ...

        def remove_gain_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "gain".
            """
            ...

        def remove_slice(self, slice_time: int) -> None:
            """
            Remove the slice point at the provided time if there is one.
            """
            ...

        def remove_slices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slices".
            """
            ...

        def remove_slicing_beat_division_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_beat_division".
            """
            ...

        def remove_slicing_region_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_region_count".
            """
            ...

        def remove_slicing_sensitivity_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_sensitivity".
            """
            ...

        def remove_slicing_style_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_style".
            """
            ...

        def remove_start_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "start_marker".
            """
            ...

        def remove_texture_flux_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "texture_flux".
            """
            ...

        def remove_texture_grain_size_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "texture_grain_size".
            """
            ...

        def remove_tones_grain_size_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tones_grain_size".
            """
            ...

        def remove_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_markers".
            """
            ...

        def remove_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_mode".
            """
            ...

        def remove_warping_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warping".
            """
            ...

        def reset_slices(self) -> None:
            """
            Resets all edited slices to their original positions.
            """
            ...

        def sample_to_beat_time(self, sample_time: float) -> float:
            """
            Converts the given sample time to beat time. Raises an error if the sample is not warped.
            """
            ...

        def slices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slices".
            """
            ...

        def slicing_beat_division_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_beat_division".
            """
            ...

        def slicing_region_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_region_count".
            """
            ...

        def slicing_sensitivity_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_sensitivity".
            """
            ...

        def slicing_style_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_style".
            """
            ...

        def start_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "start_marker".
            """
            ...

        def texture_flux_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "texture_flux".
            """
            ...

        def texture_grain_size_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "texture_grain_size".
            """
            ...

        def tones_grain_size_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tones_grain_size".
            """
            ...

        def warp_markers_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_markers".
            """
            ...

        def warp_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_mode".
            """
            ...

        def warping_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warping".
            """
            ...

    class SlicingBeatDivision:
        sixteenth: int = 0
        sixteenth_triplett: int = 1
        eighth: int = 2
        eighth_triplett: int = 3
        quarter: int = 4
        quarter_triplett: int = 5
        half: int = 6
        half_triplett: int = 7
        one_bar: int = 8
        two_bars: int = 9
        four_bars: int = 10

    class SlicingStyle:
        transient: int = 0
        beat: int = 1
        region: int = 2
        manual: int = 3

    class TransientLoopMode:
        off: int = 0
        forward: int = 1
        alternate: int = 2

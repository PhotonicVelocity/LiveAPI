from types import ModuleType
from typing import Callable


class WavetableDevice(ModuleType):

    class EffectMode:
        none: int = 0
        frequency_modulation: int = 1
        sync_and_pulse_width: int = 2
        warp_and_fold: int = 3

    class FilterRouting:
        serial: int = 0
        parallel: int = 1
        split: int = 2

    class ModulationSource:
        amp_envelope: int = 0
        envelope_2: int = 1
        envelope_3: int = 2
        lfo_1: int = 3
        lfo_2: int = 4
        midi_velocity: int = 5
        midi_note: int = 6
        midi_pitch_bend: int = 7
        midi_channel_pressure: int = 8
        midi_mod_wheel: int = 9
        midi_random: int = 10

    class UnisonMode:
        none: int = 0
        classic: int = 1
        slow_shimmer: int = 2
        fast_shimmer: int = 3
        phase_sync: int = 4
        position_spread: int = 5
        random_note: int = 6

    class VoiceCount:
        two: int = 0
        three: int = 1
        four: int = 2
        five: int = 3
        six: int = 4
        seven: int = 5
        eight: int = 6

    class Voicing:
        mono: int = 0
        poly: int = 1

    class WavetableDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Wavetable device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
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
        def filter_routing(self) -> int:
            """
            Return the current filter routing.
            """
            ...

        @filter_routing.setter
        def filter_routing(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def mono_poly(self) -> int:
            """
            Return the current voicing mode.
            """
            ...

        @mono_poly.setter
        def mono_poly(self, value) -> None:
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
        def oscillator_1_effect_mode(self) -> int:
            """
            Return the current effect mode of the oscillator 1.
            """
            ...

        @oscillator_1_effect_mode.setter
        def oscillator_1_effect_mode(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetable_category(self) -> int:
            """
            Return the current wavetable category of the oscillator 1.
            """
            ...

        @oscillator_1_wavetable_category.setter
        def oscillator_1_wavetable_category(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetable_index(self) -> int:
            """
            Return the current wavetable index of the oscillator 1.
            """
            ...

        @oscillator_1_wavetable_index.setter
        def oscillator_1_wavetable_index(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetables(self) -> tuple[str, ...]:
            """
            Get a vector of oscillator 1's wavetable names.
            """
            ...

        @property
        def oscillator_2_effect_mode(self) -> int:
            """
            Return the current effect mode of the oscillator 2.
            """
            ...

        @oscillator_2_effect_mode.setter
        def oscillator_2_effect_mode(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetable_category(self) -> int:
            """
            Return the current wavetable category of the oscillator 2.
            """
            ...

        @oscillator_2_wavetable_category.setter
        def oscillator_2_wavetable_category(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetable_index(self) -> int:
            """
            Return the current wavetable index of the oscillator 2.
            """
            ...

        @oscillator_2_wavetable_index.setter
        def oscillator_2_wavetable_index(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetables(self) -> tuple[str, ...]:
            """
            Get a vector of oscillator 2's wavetable names.
            """
            ...

        @property
        def oscillator_wavetable_categories(self) -> tuple[str, ...]:
            """
            Get a vector of the available wavetable categories.
            """
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def poly_voices(self) -> int:
            """
            Return the current number of polyphonic voices. Uses the VoiceCount enumeration.
            """
            ...

        @poly_voices.setter
        def poly_voices(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def unison_mode(self) -> int:
            """
            Return the current unison mode.
            """
            ...

        @unison_mode.setter
        def unison_mode(self, value) -> None:
            ...

        @property
        def unison_voice_count(self) -> int:
            """
            Return the current number of unison voices.
            """
            ...

        @unison_voice_count.setter
        def unison_voice_count(self, value) -> None:
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def visible_modulation_target_names(self) -> tuple[str, ...]:
            """
            Get the names of all the visible modulation targets.
            """
            ...

        def add_filter_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "filter_routing" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_modulation_matrix_changed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "modulation_matrix_changed" has changed.
            """
            ...

        def add_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_oscillator_1_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_effect_mode" has changed.
            """
            ...

        def add_oscillator_1_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_category" has changed.
            """
            ...

        def add_oscillator_1_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_index" has changed.
            """
            ...

        def add_oscillator_1_wavetables_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetables" has changed.
            """
            ...

        def add_oscillator_2_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_effect_mode" has changed.
            """
            ...

        def add_oscillator_2_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_category" has changed.
            """
            ...

        def add_oscillator_2_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_index" has changed.
            """
            ...

        def add_oscillator_2_wavetables_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetables" has changed.
            """
            ...

        def add_parameter_to_modulation_matrix(self, parameter: DeviceParameter) -> int:
            """
            Add a non-pitch parameter to the modulation matrix.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "poly_voices" has changed.
            """
            ...

        def add_unison_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unison_mode" has changed.
            """
            ...

        def add_unison_voice_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unison_voice_count" has changed.
            """
            ...

        def add_visible_modulation_target_names_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_modulation_target_names" has changed.
            """
            ...

        def filter_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "filter_routing".
            """
            ...

        def get_modulation_target_parameter_name(self, target_index: int) -> str:
            """
            Get the parameter name of the modulation target at the given index.
            """
            ...

        def get_modulation_value(self, target_index: int, source: int) -> float:
            """
            Get the value of a modulation amount for the given target-source connection.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_parameter_modulatable(self, parameter: DeviceParameter) -> bool:
            """
            Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def modulation_matrix_changed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "modulation_matrix_changed".
            """
            ...

        def mono_poly_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def oscillator_1_effect_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_effect_mode".
            """
            ...

        def oscillator_1_wavetable_category_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_category".
            """
            ...

        def oscillator_1_wavetable_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_index".
            """
            ...

        def oscillator_1_wavetables_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetables".
            """
            ...

        def oscillator_2_effect_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_effect_mode".
            """
            ...

        def oscillator_2_wavetable_category_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_category".
            """
            ...

        def oscillator_2_wavetable_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_index".
            """
            ...

        def oscillator_2_wavetables_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetables".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def poly_voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "poly_voices".
            """
            ...

        def remove_filter_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "filter_routing".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_modulation_matrix_changed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "modulation_matrix_changed".
            """
            ...

        def remove_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_oscillator_1_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_effect_mode".
            """
            ...

        def remove_oscillator_1_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetable_category".
            """
            ...

        def remove_oscillator_1_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetable_index".
            """
            ...

        def remove_oscillator_1_wavetables_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetables".
            """
            ...

        def remove_oscillator_2_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_effect_mode".
            """
            ...

        def remove_oscillator_2_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetable_category".
            """
            ...

        def remove_oscillator_2_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetable_index".
            """
            ...

        def remove_oscillator_2_wavetables_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetables".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "poly_voices".
            """
            ...

        def remove_unison_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unison_mode".
            """
            ...

        def remove_unison_voice_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unison_voice_count".
            """
            ...

        def remove_visible_modulation_target_names_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_modulation_target_names".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def set_modulation_value(self, target_index: int, source: int, value: float) -> None:
            """
            Set the value of a modulation amount for the given target-source connection.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def unison_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unison_mode".
            """
            ...

        def unison_voice_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unison_voice_count".
            """
            ...

        def visible_modulation_target_names_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_modulation_target_names".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> WavetableDevice:
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

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
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

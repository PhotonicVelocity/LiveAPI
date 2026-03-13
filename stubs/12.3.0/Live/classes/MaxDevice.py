from types import ModuleType
from typing import Callable


class MaxDevice(ModuleType):

    class MaxDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Max for Live device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def audio_inputs(self) -> tuple:
            """
            Const access to a list of all audio inputs of the device.
            """
            ...

        @property
        def audio_outputs(self) -> tuple:
            """
            Const access to a list of all audio outputs of the device.
            """
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
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self):
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
        def midi_inputs(self) -> tuple:
            """
            Const access to a list of all midi outputs of the device.
            """
            ...

        @property
        def midi_outputs(self) -> tuple:
            """
            Const access to a list of all midi outputs of the device.
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
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
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

        def add_audio_inputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "audio_inputs" has changed.
            """
            ...

        def add_audio_outputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "audio_outputs" has changed.
            """
            ...

        def add_bank_parameters_changed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "bank_parameters_changed" has changed.
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

        def add_midi_inputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_inputs" has changed.
            """
            ...

        def add_midi_outputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_outputs" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def audio_inputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "audio_inputs".
            """
            ...

        def audio_outputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "audio_outputs".
            """
            ...

        def bank_parameters_changed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "bank_parameters_changed".
            """
            ...

        def get_bank_count(self) -> int:
            """
            Get the number of parameter banks. This is related to hardware control surfaces.
            """
            ...

        def get_bank_name(self, arg2: int) -> str:
            """
            Get the name of a parameter bank given by index. This is related to hardware control surfaces.
            """
            ...

        def get_bank_parameters(self, arg2: int) -> list:
            """
            Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.
            """
            ...

        def get_value_item_icons(self, arg2: DeviceParameter) -> list:
            """
            Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
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

        def midi_inputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_inputs".
            """
            ...

        def midi_outputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_outputs".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_audio_inputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "audio_inputs".
            """
            ...

        def remove_audio_outputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "audio_outputs".
            """
            ...

        def remove_bank_parameters_changed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "bank_parameters_changed".
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

        def remove_midi_inputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_inputs".
            """
            ...

        def remove_midi_outputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_outputs".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
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
            def canonical_parent(self) -> MaxDevice:
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

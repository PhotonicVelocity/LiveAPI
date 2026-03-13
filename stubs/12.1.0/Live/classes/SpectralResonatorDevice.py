from types import ModuleType
from typing import Callable


class SpectralResonatorDevice(ModuleType):

    class SpectralResonatorDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Spectral Resonator device.
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
        def frequency_dial_mode(self) -> int:
            """
            Return the current frequency dial mode index
            """
            ...

        @frequency_dial_mode.setter
        def frequency_dial_mode(self, value) -> None:
            ...

        @property
        def frequency_dial_mode_list(self) -> tuple[str, ...]:
            """
            Return the current frequency dial mode list
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
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
        def midi_gate(self) -> int:
            """
            Return the current midi gate index
            """
            ...

        @midi_gate.setter
        def midi_gate(self, value) -> None:
            ...

        @property
        def midi_gate_list(self) -> tuple[str, ...]:
            """
            Return the current midi gate list
            """
            ...

        @property
        def mod_mode(self) -> int:
            """
            Return the current mod mode index
            """
            ...

        @mod_mode.setter
        def mod_mode(self, value) -> None:
            ...

        @property
        def mod_mode_list(self) -> tuple[str, ...]:
            """
            Return the current mod mode list
            """
            ...

        @property
        def mono_poly(self) -> int:
            """
            Return the current mono poly mode index
            """
            ...

        @mono_poly.setter
        def mono_poly(self, value) -> None:
            ...

        @property
        def mono_poly_list(self) -> tuple[str, ...]:
            """
            Return the current mono poly mode list
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
        def pitch_bend_range(self) -> int:
            """
            Return the current pitch bend range
            """
            ...

        @pitch_bend_range.setter
        def pitch_bend_range(self, value) -> None:
            ...

        @property
        def pitch_mode(self) -> int:
            """
            Return the current pitch mode index
            """
            ...

        @pitch_mode.setter
        def pitch_mode(self, value) -> None:
            ...

        @property
        def pitch_mode_list(self) -> tuple[str, ...]:
            """
            Return the current pitch mode list
            """
            ...

        @property
        def polyphony(self) -> int:
            """
            Return the current polyphony
            """
            ...

        @polyphony.setter
        def polyphony(self, value) -> None:
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

        def add_frequency_dial_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "frequency_dial_mode_list" has changed.
            """
            ...

        def add_frequency_dial_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "frequency_dial_mode" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
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

        def add_midi_gate_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_gate_list" has changed.
            """
            ...

        def add_midi_gate_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_gate" has changed.
            """
            ...

        def add_mod_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_mode_list" has changed.
            """
            ...

        def add_mod_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_mode" has changed.
            """
            ...

        def add_mono_poly_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly_list" has changed.
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

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
            """
            ...

        def add_pitch_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_mode_list" has changed.
            """
            ...

        def add_pitch_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_mode" has changed.
            """
            ...

        def add_polyphony_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "polyphony" has changed.
            """
            ...

        def frequency_dial_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "frequency_dial_mode".
            """
            ...

        def frequency_dial_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "frequency_dial_mode_list".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
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

        def midi_gate_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_gate".
            """
            ...

        def midi_gate_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_gate_list".
            """
            ...

        def mod_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_mode".
            """
            ...

        def mod_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_mode_list".
            """
            ...

        def mono_poly_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly".
            """
            ...

        def mono_poly_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly_list".
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

        def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
            """
            ...

        def pitch_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_mode".
            """
            ...

        def pitch_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_mode_list".
            """
            ...

        def polyphony_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "polyphony".
            """
            ...

        def remove_frequency_dial_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "frequency_dial_mode_list".
            """
            ...

        def remove_frequency_dial_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "frequency_dial_mode".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
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

        def remove_midi_gate_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_gate_list".
            """
            ...

        def remove_midi_gate_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_gate".
            """
            ...

        def remove_mod_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_mode_list".
            """
            ...

        def remove_mod_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_mode".
            """
            ...

        def remove_mono_poly_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly_list".
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

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_bend_range".
            """
            ...

        def remove_pitch_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_mode_list".
            """
            ...

        def remove_pitch_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_mode".
            """
            ...

        def remove_polyphony_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "polyphony".
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
            def canonical_parent(self) -> SpectralResonatorDevice:
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

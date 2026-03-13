from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class MeldDevice:
    """
    This class represents a Meld device.
    """

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
        Returns the mode of Polyphony
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
    def parameters(self) -> tuple[DeviceParameter, ...]:
        """
        Const access to the list of available automatable parameters for this device.
        """
        ...

    @property
    def poly_voices(self) -> int:
        """
        Return the Poly Voice count
        """
        ...

    @poly_voices.setter
    def poly_voices(self, value) -> None:
        ...

    @property
    def selected_engine(self) -> bool:
        """
        Return what Voice Engine is selected
        """
        ...

    @selected_engine.setter
    def selected_engine(self, value) -> None:
        ...

    @property
    def type(self) -> DeviceType:
        """
        Return the type of the device.
        """
        ...

    @property
    def unison_voices(self) -> int:
        """
        Return the Unison Voice count
        """
        ...

    @unison_voices.setter
    def unison_voices(self, value) -> None:
        ...

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a device.
        """
        ...

    def add_is_active_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_active" has changed.
        """
        ...

    def add_is_using_compare_preset_b_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
        """
        ...

    def add_latency_in_ms_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
        """
        ...

    def add_latency_in_samples_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
        """
        ...

    def add_mono_poly_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
        """
        ...

    def add_name_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        ...

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "parameters" has changed.
        """
        ...

    def add_poly_voices_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "poly_voices" has changed.
        """
        ...

    def add_selected_engine_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "selected_engine" has changed.
        """
        ...

    def add_unison_voices_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "unison_voices" has changed.
        """
        ...

    def is_active_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_active".
        """
        ...

    def is_using_compare_preset_b_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
        """
        ...

    def latency_in_ms_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "latency_in_ms".
        """
        ...

    def latency_in_samples_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "latency_in_samples".
        """
        ...

    def mono_poly_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mono_poly".
        """
        ...

    def name_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        ...

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "parameters".
        """
        ...

    def poly_voices_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "poly_voices".
        """
        ...

    def remove_is_active_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_active".
        """
        ...

    def remove_is_using_compare_preset_b_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_using_compare_preset_b".
        """
        ...

    def remove_latency_in_ms_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "latency_in_ms".
        """
        ...

    def remove_latency_in_samples_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "latency_in_samples".
        """
        ...

    def remove_mono_poly_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "mono_poly".
        """
        ...

    def remove_name_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        ...

    def remove_parameters_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "parameters".
        """
        ...

    def remove_poly_voices_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "poly_voices".
        """
        ...

    def remove_selected_engine_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "selected_engine".
        """
        ...

    def remove_unison_voices_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "unison_voices".
        """
        ...

    def save_preset_to_compare_ab_slot(self) -> None:
        """
        Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
        """
        ...

    def selected_engine_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "selected_engine".
        """
        ...

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        Set the selected bank in the device for persistency.
        """
        ...

    def unison_voices_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "unison_voices".
        """
        ...


    class View:
        """
        Representing the view aspects of a device.
        """

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> MeldDevice:
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

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
            """
            ...

        def is_collapsed_has_listener(self, listener: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_collapsed".
            """
            ...

        def remove_is_collapsed_listener(self, listener: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_collapsed".
            """
            ...


__all__ = ['MeldDevice']

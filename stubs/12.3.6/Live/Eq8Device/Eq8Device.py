from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class Eq8Device:
    """
    This class represents an Eq8 device.
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
    def edit_mode(self) -> bool:
        """
        Access to Eq8's edit mode.
        """
        ...

    @edit_mode.setter
    def edit_mode(self, value) -> None:
        ...

    @property
    def global_mode(self) -> int:
        """
        Access to Eq8's global mode.
        """
        ...

    @global_mode.setter
    def global_mode(self, value) -> None:
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
    def name(self) -> str:
        """
        Return access to the name of the device.
        """
        ...

    @name.setter
    def name(self, value) -> None:
        ...

    @property
    def oversample(self) -> bool:
        """
        Access to Eq8's oversample value.
        """
        ...

    @oversample.setter
    def oversample(self, value) -> None:
        ...

    @property
    def parameters(self) -> tuple[DeviceParameter, ...]:
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

    def add_edit_mode_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "edit_mode" has changed.
        """
        ...

    def add_global_mode_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "global_mode" has changed.
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

    def add_name_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        ...

    def add_oversample_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "oversample" has changed.
        """
        ...

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "parameters" has changed.
        """
        ...

    def edit_mode_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "edit_mode".
        """
        ...

    def global_mode_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "global_mode".
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

    def name_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        ...

    def oversample_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oversample".
        """
        ...

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "parameters".
        """
        ...

    def remove_edit_mode_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "edit_mode".
        """
        ...

    def remove_global_mode_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "global_mode".
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

    def remove_name_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        ...

    def remove_oversample_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "oversample".
        """
        ...

    def remove_parameters_listener(self, listener: Callable) -> None:
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


    class View:
        """
        Representing the view aspects of an Eq8 device.
        """

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Eq8Device:
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
        def selected_band(self) -> int:
            """
            Access to the selected filter band.
            """
            ...

        @selected_band.setter
        def selected_band(self, value) -> None:
            ...

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
            """
            ...

        def add_selected_band_listener(self, listener: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "selected_band" has changed.
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

        def remove_selected_band_listener(self, listener: Callable) -> None:
            """
            Remove a previously set listener function or method from property "selected_band".
            """
            ...

        def selected_band_has_listener(self, listener: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_band".
            """
            ...


__all__ = ['Eq8Device']

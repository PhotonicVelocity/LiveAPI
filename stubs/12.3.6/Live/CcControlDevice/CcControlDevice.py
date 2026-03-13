from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class CcControlDevice:
    """
    This class represents a CcControl device.
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
    def custom_bool_target(self) -> int:
        """
        Return the custom bool target
        """
        ...

    @custom_bool_target.setter
    def custom_bool_target(self, value) -> None:
        ...

    @property
    def custom_bool_target_list(self) -> tuple[str, ...]:
        """
        Return the custom bool target list
        """
        ...

    @property
    def custom_float_target_0(self) -> int:
        """
        Return the custom float target 0
        """
        ...

    @custom_float_target_0.setter
    def custom_float_target_0(self, value) -> None:
        ...

    @property
    def custom_float_target_0_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 0 list
        """
        ...

    @property
    def custom_float_target_1(self) -> int:
        """
        Return the custom float target 1
        """
        ...

    @custom_float_target_1.setter
    def custom_float_target_1(self, value) -> None:
        ...

    @property
    def custom_float_target_10(self) -> int:
        """
        Return the custom float target 10
        """
        ...

    @custom_float_target_10.setter
    def custom_float_target_10(self, value) -> None:
        ...

    @property
    def custom_float_target_10_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 10 list
        """
        ...

    @property
    def custom_float_target_11(self) -> int:
        """
        Return the custom float target 11
        """
        ...

    @custom_float_target_11.setter
    def custom_float_target_11(self, value) -> None:
        ...

    @property
    def custom_float_target_11_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 11 list
        """
        ...

    @property
    def custom_float_target_1_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 1 list
        """
        ...

    @property
    def custom_float_target_2(self) -> int:
        """
        Return the custom float target 2
        """
        ...

    @custom_float_target_2.setter
    def custom_float_target_2(self, value) -> None:
        ...

    @property
    def custom_float_target_2_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 2 list
        """
        ...

    @property
    def custom_float_target_3(self) -> int:
        """
        Return the custom float target 3
        """
        ...

    @custom_float_target_3.setter
    def custom_float_target_3(self, value) -> None:
        ...

    @property
    def custom_float_target_3_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 3 list
        """
        ...

    @property
    def custom_float_target_4(self) -> int:
        """
        Return the custom float target 4
        """
        ...

    @custom_float_target_4.setter
    def custom_float_target_4(self, value) -> None:
        ...

    @property
    def custom_float_target_4_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 4 list
        """
        ...

    @property
    def custom_float_target_5(self) -> int:
        """
        Return the custom float target 5
        """
        ...

    @custom_float_target_5.setter
    def custom_float_target_5(self, value) -> None:
        ...

    @property
    def custom_float_target_5_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 5 list
        """
        ...

    @property
    def custom_float_target_6(self) -> int:
        """
        Return the custom float target 6
        """
        ...

    @custom_float_target_6.setter
    def custom_float_target_6(self, value) -> None:
        ...

    @property
    def custom_float_target_6_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 6 list
        """
        ...

    @property
    def custom_float_target_7(self) -> int:
        """
        Return the custom float target 7
        """
        ...

    @custom_float_target_7.setter
    def custom_float_target_7(self, value) -> None:
        ...

    @property
    def custom_float_target_7_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 7 list
        """
        ...

    @property
    def custom_float_target_8(self) -> int:
        """
        Return the custom float target 8
        """
        ...

    @custom_float_target_8.setter
    def custom_float_target_8(self, value) -> None:
        ...

    @property
    def custom_float_target_8_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 8 list
        """
        ...

    @property
    def custom_float_target_9(self) -> int:
        """
        Return the custom float target 9
        """
        ...

    @custom_float_target_9.setter
    def custom_float_target_9(self, value) -> None:
        ...

    @property
    def custom_float_target_9_list(self) -> tuple[str, ...]:
        """
        Return the custom float target 9 list
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

    def add_custom_bool_target_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_bool_target" has changed.
        """
        ...

    def add_custom_float_target_0_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_0" has changed.
        """
        ...

    def add_custom_float_target_10_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_10" has changed.
        """
        ...

    def add_custom_float_target_11_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_11" has changed.
        """
        ...

    def add_custom_float_target_1_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_1" has changed.
        """
        ...

    def add_custom_float_target_2_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_2" has changed.
        """
        ...

    def add_custom_float_target_3_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_3" has changed.
        """
        ...

    def add_custom_float_target_4_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_4" has changed.
        """
        ...

    def add_custom_float_target_5_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_5" has changed.
        """
        ...

    def add_custom_float_target_6_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_6" has changed.
        """
        ...

    def add_custom_float_target_7_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_7" has changed.
        """
        ...

    def add_custom_float_target_8_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_8" has changed.
        """
        ...

    def add_custom_float_target_9_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "custom_float_target_9" has changed.
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

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "parameters" has changed.
        """
        ...

    def custom_bool_target_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_bool_target".
        """
        ...

    def custom_float_target_0_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_0".
        """
        ...

    def custom_float_target_10_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_10".
        """
        ...

    def custom_float_target_11_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_11".
        """
        ...

    def custom_float_target_1_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_1".
        """
        ...

    def custom_float_target_2_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_2".
        """
        ...

    def custom_float_target_3_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_3".
        """
        ...

    def custom_float_target_4_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_4".
        """
        ...

    def custom_float_target_5_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_5".
        """
        ...

    def custom_float_target_6_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_6".
        """
        ...

    def custom_float_target_7_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_7".
        """
        ...

    def custom_float_target_8_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_8".
        """
        ...

    def custom_float_target_9_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "custom_float_target_9".
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

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "parameters".
        """
        ...

    def remove_custom_bool_target_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_bool_target".
        """
        ...

    def remove_custom_float_target_0_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_0".
        """
        ...

    def remove_custom_float_target_10_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_10".
        """
        ...

    def remove_custom_float_target_11_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_11".
        """
        ...

    def remove_custom_float_target_1_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_1".
        """
        ...

    def remove_custom_float_target_2_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_2".
        """
        ...

    def remove_custom_float_target_3_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_3".
        """
        ...

    def remove_custom_float_target_4_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_4".
        """
        ...

    def remove_custom_float_target_5_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_5".
        """
        ...

    def remove_custom_float_target_6_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_6".
        """
        ...

    def remove_custom_float_target_7_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_7".
        """
        ...

    def remove_custom_float_target_8_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_8".
        """
        ...

    def remove_custom_float_target_9_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "custom_float_target_9".
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

    def remove_parameters_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "parameters".
        """
        ...

    def resend(self) -> None:
        """
        Resend all CC values.
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
        Representing the view aspects of a device.
        """

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> CcControlDevice:
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


__all__ = ['CcControlDevice']

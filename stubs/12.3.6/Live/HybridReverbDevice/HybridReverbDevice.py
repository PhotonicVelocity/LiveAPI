from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Device import Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class HybridReverbDevice:
    """
    This class represents a Hybrid Reverb device.
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
    def ir_attack_time(self) -> float:
        """
        Return the current IrAttackTime
        """
        ...

    @ir_attack_time.setter
    def ir_attack_time(self, value) -> None:
        ...

    @property
    def ir_category_index(self) -> int:
        """
        Return the current IR category index
        """
        ...

    @ir_category_index.setter
    def ir_category_index(self, value) -> None:
        ...

    @property
    def ir_category_list(self) -> tuple[str, ...]:
        """
        Return the current IR categories list
        """
        ...

    @property
    def ir_decay_time(self) -> float:
        """
        Return the current IrDecayTime
        """
        ...

    @ir_decay_time.setter
    def ir_decay_time(self, value) -> None:
        ...

    @property
    def ir_file_index(self) -> int:
        """
        Return the current IR file index
        """
        ...

    @ir_file_index.setter
    def ir_file_index(self, value) -> None:
        ...

    @property
    def ir_file_list(self) -> tuple[str, ...]:
        """
        Return the current IR file list
        """
        ...

    @property
    def ir_size_factor(self) -> float:
        """
        Return the current IrSizeFactor
        """
        ...

    @ir_size_factor.setter
    def ir_size_factor(self, value) -> None:
        ...

    @property
    def ir_time_shaping_on(self) -> bool:
        """
        Return the current IrTimeShapingOn
        """
        ...

    @ir_time_shaping_on.setter
    def ir_time_shaping_on(self, value) -> None:
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

    def add_ir_attack_time_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_attack_time" has changed.
        """
        ...

    def add_ir_category_index_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_category_index" has changed.
        """
        ...

    def add_ir_decay_time_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_decay_time" has changed.
        """
        ...

    def add_ir_file_index_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_file_index" has changed.
        """
        ...

    def add_ir_file_list_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_file_list" has changed.
        """
        ...

    def add_ir_size_factor_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_size_factor" has changed.
        """
        ...

    def add_ir_time_shaping_on_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ir_time_shaping_on" has changed.
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

    def ir_attack_time_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_attack_time".
        """
        ...

    def ir_category_index_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_category_index".
        """
        ...

    def ir_decay_time_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_decay_time".
        """
        ...

    def ir_file_index_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_file_index".
        """
        ...

    def ir_file_list_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_file_list".
        """
        ...

    def ir_size_factor_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_size_factor".
        """
        ...

    def ir_time_shaping_on_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ir_time_shaping_on".
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

    def remove_ir_attack_time_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_attack_time".
        """
        ...

    def remove_ir_category_index_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_category_index".
        """
        ...

    def remove_ir_decay_time_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_decay_time".
        """
        ...

    def remove_ir_file_index_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_file_index".
        """
        ...

    def remove_ir_file_list_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_file_list".
        """
        ...

    def remove_ir_size_factor_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_size_factor".
        """
        ...

    def remove_ir_time_shaping_on_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ir_time_shaping_on".
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
        def canonical_parent(self) -> HybridReverbDevice:
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


__all__ = ['HybridReverbDevice']

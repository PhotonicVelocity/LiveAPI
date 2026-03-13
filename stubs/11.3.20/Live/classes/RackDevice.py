from types import ModuleType
from typing import Callable


class RackDevice(ModuleType):

    class RackDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Rack device.
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
        def can_show_chains(self) -> bool:
            """
            return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def chain_selector(self) -> DeviceParameter:
            """
            Const access to the chain selector parameter.
            """
            ...

        @property
        def chains(self) -> tuple:
            """
            Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.
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
        def drum_pads(self) -> tuple:
            """
            Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def has_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def has_macro_mappings(self) -> bool:
            """
            Returns true if any of the rack's macros are mapped to a parameter.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_showing_chains(self) -> bool:
            """
            Returns True, if it is showing chains.
            """
            ...

        @is_showing_chains.setter
        def is_showing_chains(self, value) -> None:
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
        def macros_mapped(self) -> tuple:
            """
            A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something
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
        def return_chains(self) -> tuple:
            """
            Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.
            """
            ...

        @property
        def selected_variation_index(self) -> int:
            """
            Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.
            """
            ...

        @selected_variation_index.setter
        def selected_variation_index(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def variation_count(self) -> int:
            """
            Access to the number of macro variations currently stored.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def visible_drum_pads(self) -> tuple:
            """
            Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def visible_macro_count(self) -> int:
            """
            Access to the number of macros that are currently visible.
            """
            ...

        def add_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "chains" has changed.
            """
            ...

        def add_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "drum_pads" has changed.
            """
            ...

        def add_has_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_drum_pads" has changed.
            """
            ...

        def add_has_macro_mappings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_macro_mappings" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
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

        def add_macro(self) -> None:
            """
            Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls is reached.
            """
            ...

        def add_macros_mapped_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "macros_mapped" has changed.
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

        def add_return_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "return_chains" has changed.
            """
            ...

        def add_variation_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "variation_count" has changed.
            """
            ...

        def add_visible_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_drum_pads" has changed.
            """
            ...

        def add_visible_macro_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_macro_count" has changed.
            """
            ...

        def chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "chains".
            """
            ...

        def copy_pad(self, arg2: int, arg3: int) -> None:
            """
            Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.
            """
            ...

        def delete_selected_variation(self) -> None:
            """
            Deletes the currently selected macro variation.Does nothing if there is no selected variation.
            """
            ...

        def drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "drum_pads".
            """
            ...

        def has_drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_drum_pads".
            """
            ...

        def has_macro_mappings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_macro_mappings".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_showing_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_showing_chains".
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

        def macros_mapped_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "macros_mapped".
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

        def randomize_macros(self) -> None:
            """
            Randomizes the values for all macro controls not excluded from randomization.
            """
            ...

        def recall_last_used_variation(self) -> None:
            """
            Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.
            """
            ...

        def recall_selected_variation(self) -> None:
            """
            Recalls the currently selected macro variation.Does nothing if there are no variations.
            """
            ...

        def remove_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "chains".
            """
            ...

        def remove_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "drum_pads".
            """
            ...

        def remove_has_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_drum_pads".
            """
            ...

        def remove_has_macro_mappings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_macro_mappings".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_showing_chains".
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

        def remove_macro(self) -> None:
            """
            Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls is reached.
            """
            ...

        def remove_macros_mapped_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "macros_mapped".
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

        def remove_return_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "return_chains".
            """
            ...

        def remove_variation_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "variation_count".
            """
            ...

        def remove_visible_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_drum_pads".
            """
            ...

        def remove_visible_macro_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_macro_count".
            """
            ...

        def return_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "return_chains".
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def store_variation(self) -> None:
            """
            Stores a new variation of the values of all currently mapped macros
            """
            ...

        def variation_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "variation_count".
            """
            ...

        def visible_drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_drum_pads".
            """
            ...

        def visible_macro_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_macro_count".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a rack device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> RackDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def drum_pads_scroll_position(self) -> int:
                """
                Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.
                """
                ...

            @drum_pads_scroll_position.setter
            def drum_pads_scroll_position(self, value) -> None:
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
            def is_showing_chain_devices(self) -> bool:
                """
                Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is false.
                """
                ...

            @is_showing_chain_devices.setter
            def is_showing_chain_devices(self, value) -> None:
                ...

            @property
            def selected_chain(self) -> None:
                """
                Return access to the currently selected chain.
                """
                ...

            @selected_chain.setter
            def selected_chain(self, value) -> None:
                ...

            @property
            def selected_drum_pad(self) -> DrumPad:
                """
                Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
                """
                ...

            @selected_drum_pad.setter
            def selected_drum_pad(self, value) -> None:
                ...

            def add_drum_pads_scroll_position_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "drum_pads_scroll_position" has changed.
                """
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_is_showing_chain_devices_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_showing_chain_devices" has changed.
                """
                ...

            def add_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_chain" has changed.
                """
                ...

            def add_selected_drum_pad_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_drum_pad" has changed.
                """
                ...

            def drum_pads_scroll_position_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "drum_pads_scroll_position".
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def is_showing_chain_devices_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_showing_chain_devices".
                """
                ...

            def remove_drum_pads_scroll_position_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "drum_pads_scroll_position".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_is_showing_chain_devices_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_showing_chain_devices".
                """
                ...

            def remove_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_chain".
                """
                ...

            def remove_selected_drum_pad_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_drum_pad".
                """
                ...

            def selected_chain_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_chain".
                """
                ...

            def selected_drum_pad_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_drum_pad".
                """
                ...

from types import ModuleType
from typing import Callable


class CompressorDevice(ModuleType):

    class CompressorDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Compressor device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def available_input_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of source channels for input routing in the sidechain.
            """
            ...

        @property
        def available_input_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of source types for input routing in the sidechain.
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
        def input_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current source channel for input routing in the sidechain.Raises ValueError if the channel isn't one of the current values inavailable_input_routing_channels.
            """
            ...

        @input_routing_channel.setter
        def input_routing_channel(self, value) -> None:
            ...

        @property
        def input_routing_type(self) -> RoutingType:
            """
            Get and set the current source type for input routing in the sidechain.Raises ValueError if the type isn't one of the current values inavailable_input_routing_types.
            """
            ...

        @input_routing_type.setter
        def input_routing_type(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
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

        def add_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
            """
            ...

        def add_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
            """
            ...

        def add_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
            """
            ...

        def add_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
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

        def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
            """
            ...

        def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
            """
            ...

        def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_channel".
            """
            ...

        def input_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_type".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
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

        def remove_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_channels".
            """
            ...

        def remove_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_types".
            """
            ...

        def remove_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_channel".
            """
            ...

        def remove_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_type".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
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

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Compressor device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> CompressorDevice:
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

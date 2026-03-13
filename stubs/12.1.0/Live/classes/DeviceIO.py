from types import ModuleType
from typing import Callable


class DeviceIO(ModuleType):

    class DeviceIO(object):
        def __init__(self, *a, **k):
            """
            This class represents a specific input or output bus of a device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def available_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of channels for this IO endpoint.
            """
            ...

        @property
        def available_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of available routing types for this IO endpoint.
            """
            ...

        @property
        def canonical_parent(self) -> MaxDevice:
            """
            Get the canonical parent of the device IO.
            """
            ...

        @property
        def default_external_routing_channel_is_none(self) -> bool:
            """
            Get and set whether the default routing channel for External routing types is none.
            """
            ...

        @default_external_routing_channel_is_none.setter
        def default_external_routing_channel_is_none(self, value) -> None:
            ...

        @property
        def routing_channel(self) -> RoutingChannel:
            """
            Get and set the current routing channel.Raises ValueError if the channel isn't one of the current values inavailable_routing_channels.
            """
            ...

        @routing_channel.setter
        def routing_channel(self, value) -> None:
            ...

        @property
        def routing_type(self) -> RoutingType:
            """
            Get and set the current routing type.Raises ValueError if the type isn't one of the current values inavailable_routing_types.
            """
            ...

        @routing_type.setter
        def routing_type(self, value) -> None:
            ...

        def add_available_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_routing_channels" has changed.
            """
            ...

        def add_available_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_routing_types" has changed.
            """
            ...

        def add_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "routing_channel" has changed.
            """
            ...

        def add_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "routing_type" has changed.
            """
            ...

        def available_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_routing_channels".
            """
            ...

        def available_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_routing_types".
            """
            ...

        def remove_available_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_routing_channels".
            """
            ...

        def remove_available_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_routing_types".
            """
            ...

        def remove_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "routing_channel".
            """
            ...

        def remove_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "routing_type".
            """
            ...

        def routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "routing_channel".
            """
            ...

        def routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "routing_type".
            """
            ...

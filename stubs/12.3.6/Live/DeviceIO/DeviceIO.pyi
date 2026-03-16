from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.LomObject import LomObject
    from Live.MaxDevice import MaxDevice
    from Live.Track import RoutingChannel, RoutingChannelVector, RoutingType, RoutingTypeVector



class DeviceIO(LomObject):
    """This class represents a specific input or output bus of a device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_available_routing_channels_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "available_routing_channels" has changed.
        """
        ...

    def add_available_routing_types_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "available_routing_types" has changed.
        """
        ...

    def add_routing_channel_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "routing_channel" has changed.
        """
        ...

    def add_routing_type_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "routing_type" has changed.
        """
        ...

    @property
    def available_routing_channels(self) -> RoutingChannelVector:
        """Return a list of channels for this IO endpoint."""
        ...

    def available_routing_channels_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "available_routing_channels".
        """
        ...

    @property
    def available_routing_types(self) -> RoutingTypeVector:
        """Return a list of available routing types for this IO endpoint."""
        ...

    def available_routing_types_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "available_routing_types".
        """
        ...

    @property
    def canonical_parent(self) -> MaxDevice:
        """Get the canonical parent of the device IO."""
        ...

    @property
    def default_external_routing_channel_is_none(self) -> bool:
        """Get and set whether the default routing channel for External routing types is none."""
        ...

    @default_external_routing_channel_is_none.setter
    def default_external_routing_channel_is_none(self, value: bool) -> None: ...

    def remove_available_routing_channels_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "available_routing_channels".
        """
        ...

    def remove_available_routing_types_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "available_routing_types".
        """
        ...

    def remove_routing_channel_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "routing_channel".
        """
        ...

    def remove_routing_type_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "routing_type".
        """
        ...

    @property
    def routing_channel(self) -> RoutingChannel:
        """
        Get and set the current routing channel.
        Raises ValueError if the channel isn't one of the current values in
        available_routing_channels.
        """
        ...

    @routing_channel.setter
    def routing_channel(self, value: RoutingChannel) -> None: ...

    def routing_channel_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "routing_channel".
        """
        ...

    @property
    def routing_type(self) -> RoutingType:
        """
        Get and set the current routing type.
        Raises ValueError if the type isn't one of the current values in
        available_routing_types.
        """
        ...

    @routing_type.setter
    def routing_type(self, value: RoutingType) -> None: ...

    def routing_type_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "routing_type".
        """
        ...

__all__ = ['DeviceIO']

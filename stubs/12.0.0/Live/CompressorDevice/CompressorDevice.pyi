from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import RoutingChannel, RoutingChannelVector, RoutingType, RoutingTypeVector, Track



class CompressorDevice(Device):
    """This class represents a Compressor device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_available_input_routing_channels_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "available_input_routing_channels" has changed.
        """
        ...

    def add_available_input_routing_types_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "available_input_routing_types" has changed.
        """
        ...

    def add_input_routing_channel_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "input_routing_channel" has changed.
        """
        ...

    def add_input_routing_type_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "input_routing_type" has changed.
        """
        ...

    @property
    def available_input_routing_channels(self) -> RoutingChannelVector:
        """Return a list of source channels for input routing in the sidechain."""
        ...

    def available_input_routing_channels_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "available_input_routing_channels".
        """
        ...

    @property
    def available_input_routing_types(self) -> RoutingTypeVector:
        """Return a list of source types for input routing in the sidechain."""
        ...

    def available_input_routing_types_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "available_input_routing_types".
        """
        ...

    @property
    def can_have_chains(self) -> bool:
        """Returns true if the device is a rack."""
        ...

    @property
    def can_have_drum_pads(self) -> bool:
        """Returns true if the device is a drum rack."""
        ...

    @property
    def canonical_parent(self) -> Track:
        """Get the canonical parent of the Device."""
        ...

    @property
    def class_display_name(self) -> str:
        """Return const access to the name of the device's class name as displayed in Live's browser and device chain"""
        ...

    @property
    def class_name(self) -> str:
        """Return const access to the name of the device's class."""
        ...

    @property
    def input_routing_channel(self) -> RoutingChannel:
        """
        Get and set the current source channel for input routing in the sidechain.
        Raises ValueError if the channel isn't one of the current values in
        available_input_routing_channels.
        """
        ...

    @input_routing_channel.setter
    def input_routing_channel(self, value: RoutingChannel) -> None: ...

    def input_routing_channel_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "input_routing_channel".
        """
        ...

    @property
    def input_routing_type(self) -> RoutingType:
        """
        Get and set the current source type for input routing in the sidechain.
        Raises ValueError if the type isn't one of the current values in
        available_input_routing_types.
        """
        ...

    @input_routing_type.setter
    def input_routing_type(self, value: RoutingType) -> None: ...

    def input_routing_type_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "input_routing_type".
        """
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def latency_in_ms(self) -> float:
        """Returns the latency of the device in ms."""
        ...

    @property
    def latency_in_samples(self) -> int:
        """Returns the latency of the device in samples."""
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def remove_available_input_routing_channels_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "available_input_routing_channels".
        """
        ...

    def remove_available_input_routing_types_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "available_input_routing_types".
        """
        ...

    def remove_input_routing_channel_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "input_routing_channel".
        """
        ...

    def remove_input_routing_type_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "input_routing_type".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> Device.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['CompressorDevice']

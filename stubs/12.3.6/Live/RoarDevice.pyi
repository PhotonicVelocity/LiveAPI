from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device



class RoarDevice(Device):
    """This class represents a Roar device."""

    def add_env_listen_listener(self, callback: Callable[[], None], /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "env_listen" has changed.
        """
        ...

    def add_routing_mode_index_listener(self, callback: Callable[[], None], /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "routing_mode_index" has changed.
        """
        ...

    @property
    def env_listen(self) -> bool:
        """Return the Envelope Input Listen toggle state"""
        ...

    @env_listen.setter
    def env_listen(self, value: bool) -> None: ...

    def env_listen_has_listener(self, callback: Callable[[], None], /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "env_listen".
        """
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def is_using_compare_preset_b(self) -> bool:
        """Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."""
        ...

    @is_using_compare_preset_b.setter
    def is_using_compare_preset_b(self, value: bool) -> None: ...

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

    def remove_env_listen_listener(self, callback: Callable[[], None], /) -> None:
        """
        Remove a previously set listener function or method from
        property "env_listen".
        """
        ...

    def remove_routing_mode_index_listener(self, callback: Callable[[], None], /) -> None:
        """
        Remove a previously set listener function or method from
        property "routing_mode_index".
        """
        ...

    @property
    def routing_mode_index(self) -> int:
        """Return the routing mode index"""
        ...

    @routing_mode_index.setter
    def routing_mode_index(self, value: int) -> None: ...

    def routing_mode_index_has_listener(self, callback: Callable[[], None], /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "routing_mode_index".
        """
        ...

    @property
    def routing_mode_list(self) -> StringVector:
        """Return the routing mode list"""
        ...

__all__ = ['RoarDevice']

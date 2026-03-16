from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')
from .Track import Track

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Chain import Chain
    from Live.LomObject import LomObject



class DeviceContainer(LomObject):
    """This class is a common super class of Track and Chain"""

    @property
    def _live_ptr(self) -> int:
        ...

class DeviceInsertMode(int):
    default: int = 0
    selected_left: int = 1
    selected_right: int = 2
    count: int = 3

class RoutingChannel:
    """This class represents a routing channel."""

    @property
    def display_name(self) -> str:
        """Display name of routing channel."""
        ...

    @property
    def layout(self) -> RoutingChannelLayout:
        """The routing channel's Layout, e.g., mono or stereo."""
        ...

class RoutingChannelLayout(int):
    midi: int = 0
    mono: int = 1
    stereo: int = 2

class RoutingChannelVector(Vector[RoutingChannel]):
    """A container for returning routing channels from Live."""

    def append(self, value: RoutingChannel | None, /) -> None:
        ...

    def extend(self, values: Iterable[RoutingChannel] | None, /) -> None:
        ...

class RoutingType:
    """This class represents a routing type."""

    @property
    def attached_object(self) -> Track:
        """Live object associated with the routing type."""
        ...

    @property
    def category(self) -> int:
        """Category of the routing type."""
        ...

    @property
    def display_name(self) -> str:
        """Display name of routing type."""
        ...

class RoutingTypeCategory(int):
    external: int = 0
    rewire: int = 1
    resampling: int = 2
    master: int = 3
    track: int = 4
    parent_group_track: int = 5
    none: int = 6
    invalid: int = 7

class RoutingTypeVector(Vector[RoutingType]):
    """A container for returning routing types from Live."""

    def append(self, value: RoutingType | None, /) -> None:
        ...

    def extend(self, values: Iterable[RoutingType] | None, /) -> None:
        ...

__all__ = ['Track', 'DeviceContainer', 'DeviceInsertMode', 'RoutingChannel', 'RoutingChannelLayout', 'RoutingChannelVector', 'RoutingType', 'RoutingTypeCategory', 'RoutingTypeVector']

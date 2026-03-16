from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')

if TYPE_CHECKING:
    from Live.Base import Vector



class ListenerHandle:
    """This class represents a Python listener when connected to a Live property."""

    def disconnect(self) -> None:
        """Disconnects the listener from its property"""
        ...

    @property
    def listener_func(self) -> Callable:
        """Returns the original function"""
        ...

    @property
    def listener_self(self) -> Any:
        """Returns the weak reference to original self, if it was a bound method"""
        ...

    @property
    def name(self) -> str:
        """Prints the name of the property that this listener is connected to"""
        ...

class ListenerVector(Vector[ListenerHandle]):
    """A read only container for accessing a list of listeners."""

    def append(self, value: ListenerHandle | None) -> None:
        ...

    def extend(self, values: Iterable[ListenerHandle] | None) -> None:
        ...

__all__ = ['ListenerHandle', 'ListenerVector']

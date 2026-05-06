from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable, Iterator, overload



class ListenerHandle:
    """This class represents a Python listener when connected to a Live property."""

    def disconnect(self) -> None:
        """Disconnects the listener from its property"""
        ...

    @property
    def listener_func(self):
        """Returns the original function"""
        ...

    @property
    def listener_self(self):
        """Returns the weak reference to original self, if it was a bound method"""
        ...

    @property
    def name(self):
        """Prints the name of the property that this listener is connected to"""
        ...

class ListenerVector(Iterable):
    """A read only container for accessing a list of listeners."""

    def __iter__(self) -> Iterator[Any]: ...

    @overload
    def __getitem__(self, index: int) -> Any: ...

    @overload
    def __getitem__(self, index: slice) -> ListenerVector: ...

    def __getitem__(self, index: int | slice) -> Any | ListenerVector: ...

    def __len__(self) -> int: ...

    def __contains__(self, value: object) -> bool: ...

    def __bool__(self) -> bool: ...

    def append(self, value: ListenerHandle, /) -> None:
        ...

    def extend(self, values: Iterable[ListenerHandle], /) -> None:
        ...
__all__ = ['ListenerHandle', 'ListenerVector']

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable



class ListenerHandle:
    """This class represents a Python listener when connected to a Live property."""

    def disconnect(self) -> None:
        """Disconnects the listener from its property"""
        ...

class ListenerVector:
    """A read only container for accessing a list of listeners."""

    def append(self, value: ListenerHandle, /) -> None:
        ...

    def extend(self, values: Iterable[ListenerHandle], /) -> None:
        ...
__all__ = ['ListenerHandle', 'ListenerVector']

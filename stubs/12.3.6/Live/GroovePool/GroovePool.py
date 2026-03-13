from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Song import Song



class GroovePool:
    """
    This class represents the groove pool in Live.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> Song:
        """
        Get the canonical parent of the groove pool.
        """
        ...

    @property
    def grooves(self) -> tuple:
        """
        Access to the list of grooves
        """
        ...

    def add_grooves_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "grooves" has changed.
        """
        ...

    def grooves_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "grooves".
        """
        ...

    def remove_grooves_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "grooves".
        """
        ...


__all__ = ['GroovePool']

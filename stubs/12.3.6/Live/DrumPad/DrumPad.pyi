from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.RackDevice import RackDevice



class DrumPad:
    """This class represents a drum group device pad in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_chains_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "chains" has changed.
        """
        ...

    def add_mute_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mute" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_solo_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "solo" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> RackDevice:
        """Get the canonical parent of the drum pad."""
        ...

    @property
    def chains(self) -> Vector:
        """Return const access to the list of chains in this drum pad."""
        ...

    def chains_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "chains".
        """
        ...

    def delete_all_chains(self) -> None:
        """Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live."""
        ...

    @property
    def mute(self) -> bool:
        """Mute/unmute the pad."""
        ...

    @mute.setter
    def mute(self, value: bool) -> None: ...

    def mute_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mute".
        """
        ...

    @property
    def name(self) -> str:
        """Return const access to the drum pad's name. It depends on the contained chains."""
        ...

    def name_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    @property
    def note(self) -> int:
        """Get the MIDI note of the drum pad."""
        ...

    def remove_chains_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "chains".
        """
        ...

    def remove_mute_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "mute".
        """
        ...

    def remove_name_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_solo_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "solo".
        """
        ...

    @property
    def solo(self) -> bool:
        """Solo/unsolo the pad."""
        ...

    @solo.setter
    def solo(self, value: bool) -> None: ...

    def solo_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "solo".
        """
        ...

__all__ = ['DrumPad']

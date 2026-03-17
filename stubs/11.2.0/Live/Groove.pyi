from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.GroovePool import GroovePool
    from Live.LomObject import LomObject



class Groove(LomObject):
    """This class represents a groove in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_name_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_quantization_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "quantization_amount" has changed.
        """
        ...

    def add_random_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "random_amount" has changed.
        """
        ...

    def add_timing_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "timing_amount" has changed.
        """
        ...

    def add_velocity_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "velocity_amount" has changed.
        """
        ...

    @property
    def base(self) -> Base:
        """Get/set the groove's base grid."""
        ...

    @base.setter
    def base(self, value: Base) -> None: ...

    @property
    def canonical_parent(self) -> GroovePool:
        """Get the canonical parent of the groove."""
        ...

    @property
    def name(self) -> str:
        """Read/write/listen access to the groove's name"""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def name_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    @property
    def quantization_amount(self) -> float:
        """Read/write/listen access to the groove's quantization amount."""
        ...

    @quantization_amount.setter
    def quantization_amount(self, value: float) -> None: ...

    def quantization_amount_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "quantization_amount".
        """
        ...

    @property
    def random_amount(self) -> float:
        """Read/write/listen access to the groove's random amount."""
        ...

    @random_amount.setter
    def random_amount(self, value: float) -> None: ...

    def random_amount_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "random_amount".
        """
        ...

    def remove_name_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_quantization_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "quantization_amount".
        """
        ...

    def remove_random_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "random_amount".
        """
        ...

    def remove_timing_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "timing_amount".
        """
        ...

    def remove_velocity_amount_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "velocity_amount".
        """
        ...

    @property
    def timing_amount(self) -> float:
        """Read/write/listen access to the groove's timing amount."""
        ...

    @timing_amount.setter
    def timing_amount(self, value: float) -> None: ...

    def timing_amount_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "timing_amount".
        """
        ...

    @property
    def velocity_amount(self) -> float:
        """Read/write/listen access to the groove's velocity amount."""
        ...

    @velocity_amount.setter
    def velocity_amount(self, value: float) -> None: ...

    def velocity_amount_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "velocity_amount".
        """
        ...

class Base(int):
    gb_four: int = 0
    gb_eight: int = 1
    gb_eight_triplet: int = 2
    gb_sixteen: int = 3
    gb_sixteen_triplet: int = 4
    gb_thirtytwo: int = 5
    count: int = 6

__all__ = ['Groove', 'Base']

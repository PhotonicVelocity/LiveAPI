from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Clip import Clip
    from Live.LomObject import LomObject



class Envelope(LomObject):
    """This class represents an automation or modulation envelope in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> Clip:
        """Get the canonical parent of the envelope."""
        ...

    def delete_events_in_range(self, start_time: float | None, end_time: float | None, /) -> None:
        """Deletes the events in the specified time range."""
        ...

    def events_in_range(self, start_time: float | None, end_time: float | None, /) -> EnvelopeEventVector:
        """Returns the events in the specified time range."""
        ...

    def insert_step(self, start_time: float | None, length: float | None, value: float | None, /) -> None:
        """Given a start time, a step length and a value, creates a step in the envelope."""
        ...

    def value_at_time(self, time: float | None, /) -> float:
        """Returns the parameter value at the specified time."""
        ...

class EnvelopeEvent:
    """This is a class that represents an envelope event."""

    def __init__(self, time: float, value: float, control_coefficients: EnvelopeEventControlCoefficients) -> None: ...

    @property
    def control_coefficients(self) -> EnvelopeEventControlCoefficients:
        ...

    @control_coefficients.setter
    def control_coefficients(self, value: EnvelopeEventControlCoefficients) -> None: ...

    @property
    def time(self) -> float:
        ...

    @time.setter
    def time(self, value: float) -> None: ...

    @property
    def value(self) -> float:
        ...

    @value.setter
    def value(self, value: float) -> None: ...

class EnvelopeEventControlCoefficients:
    """This class represents the control coefficients of an envelope event."""

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None: ...

    @property
    def x1(self) -> float:
        ...

    @x1.setter
    def x1(self, value: float) -> None: ...

    @property
    def x2(self) -> float:
        ...

    @x2.setter
    def x2(self, value: float) -> None: ...

    @property
    def y1(self) -> float:
        ...

    @y1.setter
    def y1(self, value: float) -> None: ...

    @property
    def y2(self) -> float:
        ...

    @y2.setter
    def y2(self, value: float) -> None: ...

class EnvelopeEventVector(Vector[EnvelopeEvent]):
    """A container for holding envelope events."""

    def append(self, value: EnvelopeEvent | None, /) -> None:
        ...

    def extend(self, values: Iterable[EnvelopeEvent] | None, /) -> None:
        ...

__all__ = ['Envelope', 'EnvelopeEvent', 'EnvelopeEventControlCoefficients', 'EnvelopeEventVector']

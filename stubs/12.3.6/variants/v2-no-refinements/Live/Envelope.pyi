from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
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

    def delete_events_in_range(self, arg2: float, arg3: float, /) -> None:
        """Deletes the events in the specified time range."""
        ...

    def events_in_range(self, arg2: float, arg3: float, /) -> EnvelopeEventVector:
        """Returns the events in the specified time range."""
        ...

    def insert_step(self, arg2: float, arg3: float, arg4: float, /) -> None:
        """Given a start time, a step length and a value, creates a step in the envelope."""
        ...

    def value_at_time(self, arg2: float, /) -> float:
        """Returns the parameter value at the specified time."""
        ...

class EnvelopeEvent:
    """This is a class that represents an envelope event."""

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

class EnvelopeEventVector:
    """A container for holding envelope events."""

    def append(self, value: EnvelopeEvent, /) -> None:
        ...

    def extend(self, values: Iterable[EnvelopeEvent], /) -> None:
        ...
__all__ = ['Envelope', 'EnvelopeEvent', 'EnvelopeEventControlCoefficients', 'EnvelopeEventVector']

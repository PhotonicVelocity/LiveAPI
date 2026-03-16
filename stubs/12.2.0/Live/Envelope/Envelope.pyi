from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from . import EnvelopeEventVector
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

__all__ = ['Envelope']

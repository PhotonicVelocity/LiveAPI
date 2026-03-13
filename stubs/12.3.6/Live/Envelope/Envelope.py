from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from . import EnvelopeEventVector
    from Live.Clip import Clip



class Envelope:
    """
    This class represents an automation or modulation envelope in Live.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> Clip:
        """
        Get the canonical parent of the envelope.
        """
        ...

    def delete_events_in_range(self, arg2: float, arg3: float) -> None:
        """
        Deletes the events in the specified time range.
        """
        ...

    def events_in_range(self, arg2: float, arg3: float) -> EnvelopeEventVector:
        """
        Returns the events in the specified time range.
        """
        ...

    def insert_step(self, arg2: float, arg3: float, arg4: float) -> None:
        """
        Given a start time, a step length and a value, creates a step in the envelope.
        """
        ...

    def value_at_time(self, arg2: float) -> float:
        """
        Returns the parameter value at the specified time.
        """
        ...


__all__ = ['Envelope']

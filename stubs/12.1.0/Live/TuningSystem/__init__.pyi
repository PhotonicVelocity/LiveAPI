from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .TuningSystem import TuningSystem


class PitchClassAndOctave:
    """This class represents a PitchClassAndOctave type."""

    def __init__(self, index_in_octave: int, octave: int) -> None: ...

    @property
    def index_in_octave(self) -> int:
        """A PitchClassAndOctave's index within the pseudo octave."""
        ...

    @property
    def octave(self) -> int:
        """A PitchClassAndOctave's octave."""
        ...

class ReferencePitch:
    """This class represents a ReferencePitch type."""

    def __init__(self, index_in_octave: int, octave: int, frequency: float) -> None: ...

    @property
    def frequency(self) -> float:
        """A ReferencePitch's frequency in Hz."""
        ...

    @property
    def index_in_octave(self) -> int:
        """A ReferencePitch's index within the pseudo octave."""
        ...

    @property
    def octave(self) -> int:
        """A ReferencePitch's octave."""
        ...

__all__ = ['TuningSystem', 'PitchClassAndOctave', 'ReferencePitch']

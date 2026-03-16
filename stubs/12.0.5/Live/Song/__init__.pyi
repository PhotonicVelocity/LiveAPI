from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .Song import Song

if TYPE_CHECKING:
    from Live.LomObject import LomObject



class BeatTime:
    """Represents a Time, splitted into Bars, Beats, SubDivision and Ticks."""

    def __init__(self) -> None: ...

    @property
    def bars(self) -> int:
        ...

    @bars.setter
    def bars(self, value: int) -> None: ...

    @property
    def beats(self) -> int:
        ...

    @beats.setter
    def beats(self, value: int) -> None: ...

    @property
    def sub_division(self) -> int:
        ...

    @sub_division.setter
    def sub_division(self, value: int) -> None: ...

    @property
    def ticks(self) -> int:
        ...

    @ticks.setter
    def ticks(self, value: int) -> None: ...

class CaptureDestination(int):
    """The destination for MIDI capture."""
    auto: int = 0
    session: int = 1
    arrangement: int = 2

class CaptureMode(int):
    """The capture mode that is used for capture and insert scene."""
    all: int = 0
    all_except_selected: int = 1

class CuePoint(LomObject):
    """Represents a 'Marker' in the arrangement."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_name_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_time_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "time" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> Song:
        """Get the canonical parent of the cue point."""
        ...

    def jump(self) -> None:
        """
        When the Song is playing, set the playing-position quantized to
        this Cuepoint's time. When not playing, simply move the start
        playing position.
        """
        ...

    @property
    def name(self) -> str:
        """Get/Listen to the name of this CuePoint, as visible in the arranger."""
        ...

    def name_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    def remove_name_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_time_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "time".
        """
        ...

    @property
    def time(self) -> float:
        """Get/Listen to the CuePoint's time in beats."""
        ...

    def time_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "time".
        """
        ...

class Quantization(int):
    q_no_q: int = 0
    q_8_bars: int = 1
    q_4_bars: int = 2
    q_2_bars: int = 3
    q_bar: int = 4
    q_half: int = 5
    q_half_triplet: int = 6
    q_quarter: int = 7
    q_quarter_triplet: int = 8
    q_eight: int = 9
    q_eight_triplet: int = 10
    q_sixtenth: int = 11
    q_sixtenth_triplet: int = 12
    q_thirtytwoth: int = 13

class RecordingQuantization(int):
    rec_q_no_q: int = 0
    rec_q_quarter: int = 1
    rec_q_eight: int = 2
    rec_q_eight_triplet: int = 3
    rec_q_eight_eight_triplet: int = 4
    rec_q_sixtenth: int = 5
    rec_q_sixtenth_triplet: int = 6
    rec_q_sixtenth_sixtenth_triplet: int = 7
    rec_q_thirtysecond: int = 8

class SessionRecordStatus(int):
    off: int = 0
    on: int = 1
    transition: int = 2

class SmptTime:
    """
    Represents a Time, split into Hours, Minutes, Seconds and Frames.
    The frame type must be specified when calling a function that returns
    a SmptTime.
    """

    def __init__(self) -> None: ...

    @property
    def frames(self) -> int:
        ...

    @frames.setter
    def frames(self, value: int) -> None: ...

    @property
    def hours(self) -> int:
        ...

    @hours.setter
    def hours(self, value: int) -> None: ...

    @property
    def minutes(self) -> int:
        ...

    @minutes.setter
    def minutes(self, value: int) -> None: ...

    @property
    def seconds(self) -> int:
        ...

    @seconds.setter
    def seconds(self, value: int) -> None: ...

class TimeFormat(int):
    ms_time: int = 0
    smpte_24: int = 1
    smpte_25: int = 2
    smpte_30: int = 3
    smpte_30_drop: int = 4
    smpte_29: int = 5

class TuningSystem(LomObject):
    """Represents a Tuning System and its properties."""

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def maximum_note(self) -> tuple[int, ...]:
        """
        Returns a tuple where the first entry is the index within the pseudo octave and
        the second entry is the octave or the maximum note in the tuning system.
        """
        ...

    @property
    def minimum_note(self) -> tuple[int, ...]:
        """
        Returns a tuple where the first entry is the index within the pseudo octave and
        the second entry is the octave or the minimum note in the tuning system.
        """
        ...

    @property
    def number_of_notes_in_pseudo_octave(self) -> int:
        """Get the number of notes in the pseudo octave."""
        ...

def get_all_scales_ordered() -> tuple[tuple[str, tuple[int, ...]], ...]:
    """Get an ordered tuple of tuples of all available scale names to intervals."""
    ...

__all__ = ['Song', 'BeatTime', 'CaptureDestination', 'CaptureMode', 'CuePoint', 'Quantization', 'RecordingQuantization', 'SessionRecordStatus', 'SmptTime', 'TimeFormat', 'TuningSystem', 'get_all_scales_ordered']

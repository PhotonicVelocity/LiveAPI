from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable
from .Clip import Clip


class AutomationEnvelope:
    """Describes parameter automation per clip."""

    def insert_step(self, time: float | None, value: float | None, curve: float | None) -> None:
        ...

    def value_at_time(self, time: float | None) -> float:
        ...

class ClipLaunchQuantization:
    q_global: int = 0
    q_none: int = 1
    q_8_bars: int = 2
    q_4_bars: int = 3
    q_2_bars: int = 4
    q_bar: int = 5
    q_half: int = 6
    q_half_triplet: int = 7
    q_quarter: int = 8
    q_quarter_triplet: int = 9
    q_eighth: int = 10
    q_eighth_triplet: int = 11
    q_sixteenth: int = 12
    q_sixteenth_triplet: int = 13
    q_thirtysecond: int = 14

class GridQuantization:
    no_grid: int = 0
    g_8_bars: int = 1
    g_4_bars: int = 2
    g_2_bars: int = 3
    g_bar: int = 4
    g_half: int = 5
    g_quarter: int = 6
    g_eighth: int = 7
    g_sixteenth: int = 8
    g_thirtysecond: int = 9
    count: int = 10

class LaunchMode:
    trigger: int = 0
    gate: int = 1
    toggle: int = 2
    repeat: int = 3

class MidiNote:
    """An object representing a MIDI Note"""

    @property
    def duration(self) -> float:
        ...

    @duration.setter
    def duration(self, value: float) -> None: ...

    @property
    def mute(self) -> bool:
        ...

    @mute.setter
    def mute(self, value: bool) -> None: ...

    @property
    def note_id(self) -> int:
        """
        A numerical ID that's unique within the originating clip of the note. Not to be
        used directly, but important for other API calls, namely apply_note_modifications.
        """
        ...

    @property
    def pitch(self) -> int:
        ...

    @pitch.setter
    def pitch(self, value: int) -> None: ...

    @property
    def probability(self) -> float:
        ...

    @probability.setter
    def probability(self, value: float) -> None: ...

    @property
    def release_velocity(self) -> float:
        ...

    @release_velocity.setter
    def release_velocity(self, value: float) -> None: ...

    @property
    def start_time(self) -> float:
        ...

    @start_time.setter
    def start_time(self, value: float) -> None: ...

    @property
    def velocity(self) -> float:
        ...

    @velocity.setter
    def velocity(self, value: float) -> None: ...

    @property
    def velocity_deviation(self) -> float:
        ...

    @velocity_deviation.setter
    def velocity_deviation(self, value: float) -> None: ...

class MidiNoteSpecification:
    """
    An object specifying the data for creating a MIDI note. To be used with the
    add_new_notes function.
    """

    def __init__(self, pitch: int, start_time: float, duration: float, velocity: float = 100.0, mute: bool = False, probability: float = 1.0, velocity_deviation: float = 0.0, release_velocity: float = 64.0) -> None: ...

class MidiNoteVector:
    """A container for holding MIDI notes from Live."""

    def append(self, value: MidiNote | None) -> None:
        ...

    def extend(self, values: MidiNote | None) -> None:
        ...

class WarpMarker:
    """This class represents a WarpMarker type."""

    def __init__(self, sample_time: float, beat_time: float) -> None: ...

    @property
    def beat_time(self) -> float:
        """A WarpMarker's beat time."""
        ...

    @property
    def sample_time(self) -> float:
        """A WarpMarker's sample time."""
        ...

class WarpMarkerVector:
    """A container for returning warp markers from Live."""

    def append(self, value: WarpMarker | None) -> None:
        ...

    def extend(self, values: WarpMarker | None) -> None:
        ...

class WarpMode:
    beats: int = 0
    tones: int = 1
    texture: int = 2
    repitch: int = 3
    complex: int = 4
    rex: int = 5
    complex_pro: int = 6
    count: int = 7

__all__ = ['Clip', 'AutomationEnvelope', 'ClipLaunchQuantization', 'GridQuantization', 'LaunchMode', 'MidiNote', 'MidiNoteSpecification', 'MidiNoteVector', 'WarpMarker', 'WarpMarkerVector', 'WarpMode']

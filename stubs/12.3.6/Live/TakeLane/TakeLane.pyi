from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Clip import Clip
    from Live.LomObject import LomObject
    from Live.Track import Track



class TakeLane(LomObject):
    """This class represents a take lane in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_arrangement_clips_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "arrangement_clips" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    @property
    def arrangement_clips(self) -> Vector[Clip]:
        """Read-only access to the arrangement clips in the take lane."""
        ...

    def arrangement_clips_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "arrangement_clips".
        """
        ...

    @property
    def canonical_parent(self) -> Track:
        """Get the canonical parent of the take lane."""
        ...

    def create_audio_clip(self, file_path: str | None, start_time: float | None) -> Clip:
        """
        Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.
        Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
        """
        ...

    def create_midi_clip(self, start_time: float | None, length: float | None) -> Clip:
        """
        Creates an empty MIDI clip and inserts it into the arrangement at the specified time.
        Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
        """
        ...

    @property
    def name(self) -> str:
        """Read/write access to the name of the TakeLane, as visible in the take lane header."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def name_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    def remove_arrangement_clips_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "arrangement_clips".
        """
        ...

    def remove_name_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

__all__ = ['TakeLane']

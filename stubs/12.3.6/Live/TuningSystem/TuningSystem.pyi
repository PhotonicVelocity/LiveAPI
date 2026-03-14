from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from . import PitchClassAndOctave, ReferencePitch
    from Live.Song import Song



class TuningSystem:
    """Represents a Tuning System and its properties."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_highest_note_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "highest_note" has changed.
        """
        ...

    def add_lowest_note_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "lowest_note" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_note_tunings_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "note_tunings" has changed.
        """
        ...

    def add_reference_pitch_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "reference_pitch" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> Song:
        """Get the canonical parent of the TuningSystem."""
        ...

    @property
    def highest_note(self) -> PitchClassAndOctave:
        """
        Get/Set the highest note of the current tuning system, where the first entry is
        the index within the pseudo octave and the second entry is the octave.
        """
        ...

    @highest_note.setter
    def highest_note(self, value: PitchClassAndOctave) -> None: ...

    def highest_note_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "highest_note".
        """
        ...

    @property
    def lowest_note(self) -> PitchClassAndOctave:
        """
        Get/Set the lowest note of the current tuning system, where the first entry is
        the index within the pseudo octave and the second entry is the octave.
        """
        ...

    @lowest_note.setter
    def lowest_note(self, value: PitchClassAndOctave) -> None: ...

    def lowest_note_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "lowest_note".
        """
        ...

    @property
    def name(self) -> str:
        """Get/Set the name of the currently active tuning system."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def name_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    @property
    def note_tunings(self) -> list:
        """Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament."""
        ...

    @note_tunings.setter
    def note_tunings(self, value: list) -> None: ...

    def note_tunings_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "note_tunings".
        """
        ...

    @property
    def number_of_notes_in_pseudo_octave(self) -> int:
        """Get the number of notes in the pseudo octave."""
        ...

    @property
    def pseudo_octave_in_cents(self) -> float:
        """Get the pseudo octave in cents for the currently active tuning system."""
        ...

    @property
    def reference_pitch(self) -> ReferencePitch:
        """Get/Set the reference pitch the currently active tuning system."""
        ...

    @reference_pitch.setter
    def reference_pitch(self, value: ReferencePitch) -> None: ...

    def reference_pitch_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "reference_pitch".
        """
        ...

    def remove_highest_note_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "highest_note".
        """
        ...

    def remove_lowest_note_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "lowest_note".
        """
        ...

    def remove_name_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_note_tunings_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "note_tunings".
        """
        ...

    def remove_reference_pitch_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "reference_pitch".
        """
        ...

__all__ = ['TuningSystem']

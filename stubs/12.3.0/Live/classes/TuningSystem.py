from types import ModuleType
from typing import Callable


class TuningSystem(ModuleType):

    class PitchClassAndOctave(object):
        def __init__(self, *a, **k):
            """
            This class represents a PitchClassAndOctave type.
            """
            ...

        @property
        def index_in_octave(self) -> int:
            """
            A PitchClassAndOctave's index within the pseudo octave.
            """
            ...

        @property
        def octave(self) -> int:
            """
            A PitchClassAndOctave's octave.
            """
            ...

    class ReferencePitch(object):
        def __init__(self, *a, **k):
            """
            This class represents a ReferencePitch type.
            """
            ...

        @property
        def frequency(self) -> float:
            """
            A ReferencePitch's frequency in Hz.
            """
            ...

        @property
        def index_in_octave(self) -> int:
            """
            A ReferencePitch's index within the pseudo octave.
            """
            ...

        @property
        def octave(self) -> int:
            """
            A ReferencePitch's octave.
            """
            ...

    class TuningSystem(object):
        def __init__(self, *a, **k):
            """
            Represents a Tuning System and its properties.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the TuningSystem.
            """
            ...

        @property
        def highest_note(self) -> PitchClassAndOctave:
            """
            Get/Set the highest note of the current tuning system, where the first entry isthe index within the pseudo octave and the second entry is the octave.
            """
            ...

        @highest_note.setter
        def highest_note(self, value) -> None:
            ...

        @property
        def lowest_note(self) -> PitchClassAndOctave:
            """
            Get/Set the lowest note of the current tuning system, where the first entry isthe index within the pseudo octave and the second entry is the octave.
            """
            ...

        @lowest_note.setter
        def lowest_note(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Get/Set the name of the currently active tuning system.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def note_tunings(self) -> list:
            """
            Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament.
            """
            ...

        @note_tunings.setter
        def note_tunings(self, value) -> None:
            ...

        @property
        def number_of_notes_in_pseudo_octave(self) -> int:
            """
            Get the number of notes in the pseudo octave.
            """
            ...

        @property
        def pseudo_octave_in_cents(self) -> float:
            """
            Get the pseudo octave in cents for the currently active tuning system.
            """
            ...

        @property
        def reference_pitch(self) -> ReferencePitch:
            """
            Get/Set the reference pitch the currently active tuning system.
            """
            ...

        @reference_pitch.setter
        def reference_pitch(self, value) -> None:
            ...

        def add_highest_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "highest_note" has changed.
            """
            ...

        def add_lowest_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "lowest_note" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_note_tunings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "note_tunings" has changed.
            """
            ...

        def add_reference_pitch_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "reference_pitch" has changed.
            """
            ...

        def highest_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "highest_note".
            """
            ...

        def lowest_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "lowest_note".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def note_tunings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "note_tunings".
            """
            ...

        def reference_pitch_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "reference_pitch".
            """
            ...

        def remove_highest_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "highest_note".
            """
            ...

        def remove_lowest_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "lowest_note".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_note_tunings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "note_tunings".
            """
            ...

        def remove_reference_pitch_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "reference_pitch".
            """
            ...

from types import ModuleType
from typing import Callable


class Conversions(ModuleType):

    @staticmethod
    def audio_to_midi_clip(song: Song, audio_clip: Clip, audio_to_midi_type: int) -> None:
        """
        Creates a MIDI clip in a new MIDI track with the notes extracted from the given audio_clip. The `audio_to_midi_type` decides which algorithm is used in the process. Raises error when called with an inconvertible clip or invalid `audio_to_midi_type`.
        """
        ...

    @staticmethod
    def create_drum_rack_from_audio_clip(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new track with a drum rack with a simpler on the first pad with the specified audio clip.
        """
        ...

    @staticmethod
    def create_midi_track_from_drum_pad(song: Song, drum_pad: DrumPad) -> None:
        """
        Creates a new Midi track containing the specified Drum Pad's device chain.
        """
        ...

    @staticmethod
    def create_midi_track_with_simpler(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new Midi track with a simpler including the specified audio clip.
        """
        ...

    @staticmethod
    def is_convertible_to_midi(song: Song, audio_clip: Clip) -> bool:
        """
        Returns whether `audio_clip` can be converted to MIDI. Raises error when called with a MIDI clip
        """
        ...

    @staticmethod
    def move_devices_on_track_to_new_drum_rack_pad(song: Song, track_index: int) -> LomObject:
        """
        Moves the entire device chain of the track according to the track index onto the C1 (note 36) drum pad of a new drum rack in a new track.If the track associated with the track index does not contain any devices nothing changes (i.e. a new track and new drum rack are not created).
        """
        ...

    @staticmethod
    def sliced_simpler_to_drum_rack(song: Song, simpler: SimplerDevice) -> None:
        """
        Converts the Simpler into a Drum Rack, assigning each slice to a drum pad. Calling it on a non-sliced simpler raises an error.
        """
        ...

    class AudioToMidiType:
        harmony_to_midi: int = 0
        melody_to_midi: int = 1
        drums_to_midi: int = 2

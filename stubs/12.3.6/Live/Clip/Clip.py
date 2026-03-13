from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from . import MidiNote, MidiNoteSpecification, MidiNoteVector, WarpMarker
    from Live.Base import IntU64Vector
    from Live.ClipSlot import ClipSlot
    from Live.DeviceParameter import DeviceParameter
    from Live.Envelope import Envelope
    from Live.Track import Track



class Clip:
    """
    This class represents a Clip in Live. It can be either an AudioClip or a MIDI Clip, in an Arrangement or the Session, dependingon the Track (Slot) it lives in.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def automation_envelopes(self) -> tuple:
        """
        Const access to a list of all automation envelopes for this clip.
        """
        ...

    @property
    def available_warp_modes(self) -> tuple[int, ...]:
        """
        Available for AudioClips only.Get/Set the available warp modes, that can be used.
        """
        ...

    @property
    def canonical_parent(self) -> ClipSlot:
        """
        Get the canonical parent of the Clip.
        """
        ...

    @property
    def color(self) -> int:
        """
        Get/set access to the color of the Clip (RGB).
        """
        ...

    @color.setter
    def color(self, value) -> None:
        ...

    @property
    def color_index(self) -> int:
        """
        Get/set access to the color index of the Clip.
        """
        ...

    @color_index.setter
    def color_index(self, value) -> None:
        ...

    @property
    def end_marker(self) -> float:
        """
        Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).
        """
        ...

    @end_marker.setter
    def end_marker(self, value) -> None:
        ...

    @property
    def end_time(self) -> float:
        """
        Get the clip's end time.
        """
        ...

    @property
    def file_path(self) -> str:
        """
        Get the path of the file represented by the Audio Clip.
        """
        ...

    @property
    def gain(self) -> float:
        """
        Available for AudioClips only.Read/write access to the gain setting of theAudio Clip
        """
        ...

    @gain.setter
    def gain(self, value) -> None:
        ...

    @property
    def gain_display_string(self) -> str:
        """
        Return a string with the gain as dB value
        """
        ...

    @property
    def groove(self) -> None:
        """
        Get the groove associated with this clip.
        """
        ...

    @groove.setter
    def groove(self, value) -> None:
        ...

    @property
    def has_envelopes(self) -> bool:
        """
        Will notify if the clip gets his first envelope or the last envelope is removed.
        """
        ...

    @property
    def has_groove(self) -> bool:
        """
        Returns true if a groove is associated with this clip.
        """
        ...

    @property
    def is_arrangement_clip(self) -> bool:
        """
        return true if this Clip is an Arrangement Clip.A Clip can be either a Session or Arrangement Clip.
        """
        ...

    @property
    def is_audio_clip(self) -> bool:
        """
        Return true if this Clip is an Audio Clip.A Clip can be either an Audioclip or a MIDI Clip.
        """
        ...

    @property
    def is_midi_clip(self) -> bool:
        """
        return true if this Clip is a MIDI Clip.A Clip can be either an Audioclip or a MIDI Clip.
        """
        ...

    @property
    def is_overdubbing(self) -> bool:
        """
        returns true if the Clip is recording overdubs
        """
        ...

    @property
    def is_playing(self) -> bool:
        """
        Get/Set if this Clip is currently playing. If the Clips trigger modeis set to a quantization value, the Clip will not start playing immediately.If you need to know wether the Clip was triggered, use the is_triggered property.
        """
        ...

    @is_playing.setter
    def is_playing(self, value) -> None:
        ...

    @property
    def is_recording(self) -> bool:
        """
        returns true if the Clip was triggered to record or is recording.
        """
        ...

    @property
    def is_session_clip(self) -> bool:
        """
        return true if this Clip is a Session Clip.A Clip can be either a Session or Arrangement Clip.
        """
        ...

    @property
    def is_take_lane_clip(self) -> bool:
        """
        return true if this Clip is a Take Lane Clip.A Take Lane Clip is also always an Arrangement Clip.
        """
        ...

    @property
    def is_triggered(self) -> bool:
        """
        returns true if the Clip was triggered or is playing.
        """
        ...

    @property
    def launch_mode(self) -> int:
        """
        Get/Set access to the launch mode setting of the Clip.
        """
        ...

    @launch_mode.setter
    def launch_mode(self, value) -> None:
        ...

    @property
    def launch_quantization(self) -> int:
        """
        Get/Set access to the launch quantization setting of the Clip.
        """
        ...

    @launch_quantization.setter
    def launch_quantization(self, value) -> None:
        ...

    @property
    def legato(self) -> bool:
        """
        Get/Set access to the legato setting of the Clip
        """
        ...

    @legato.setter
    def legato(self, value) -> None:
        ...

    @property
    def length(self) -> float:
        """
        Get to the Clips length in beats/seconds (unit depends on warping).
        """
        ...

    @property
    def loop_end(self) -> float:
        """
        Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).
        """
        ...

    @loop_end.setter
    def loop_end(self, value) -> None:
        ...

    @property
    def loop_start(self) -> float:
        """
        Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).
        """
        ...

    @loop_start.setter
    def loop_start(self, value) -> None:
        ...

    @property
    def looping(self) -> bool:
        """
        Get/Set the Clips 'loop is enabled' flag.Only Warped Audio Clips or MIDI Clip can be looped.
        """
        ...

    @looping.setter
    def looping(self, value) -> None:
        ...

    @property
    def muted(self) -> bool:
        """
        Read/write access to the mute state of the Clip.
        """
        ...

    @muted.setter
    def muted(self, value) -> None:
        ...

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Clip.
        """
        ...

    @name.setter
    def name(self, value) -> None:
        ...

    @property
    def pitch_coarse(self) -> int:
        """
        Available for AudioClips only.Read/write access to the pitch (in halftones) setting of theAudio Clip, ranging from -48 to 48
        """
        ...

    @pitch_coarse.setter
    def pitch_coarse(self, value) -> None:
        ...

    @property
    def pitch_fine(self) -> float:
        """
        Available for AudioClips only.Read/write access to the pitch fine setting of theAudio Clip, ranging from -500 to 500
        """
        ...

    @pitch_fine.setter
    def pitch_fine(self, value) -> None:
        ...

    @property
    def playing_position(self) -> float:
        """
        Constant access to the current playing position of the clip.The returned value is the position in beats for midi and warped audio clips,or in seconds for unwarped audio clips. Stopped clips will return 0.
        """
        ...

    @property
    def position(self) -> float:
        """
        Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
        """
        ...

    @position.setter
    def position(self, value) -> None:
        ...

    @property
    def ram_mode(self) -> bool:
        """
        Available for AudioClips only.Read/write access to the Ram mode setting of the Audio Clip
        """
        ...

    @ram_mode.setter
    def ram_mode(self, value) -> None:
        ...

    @property
    def sample_length(self) -> int:
        """
        Available for AudioClips only.Get the sample length in sample time or -1 if there is no sample available.
        """
        ...

    @property
    def sample_rate(self) -> float:
        """
        Available for AudioClips only.Read-only access to the Clip's sampling rate.
        """
        ...

    @property
    def signature_denominator(self) -> int:
        """
        Get/Set access to the global signature denominator of the Clip.
        """
        ...

    @signature_denominator.setter
    def signature_denominator(self, value) -> None:
        ...

    @property
    def signature_numerator(self) -> int:
        """
        Get/Set access to the global signature numerator of the Clip.
        """
        ...

    @signature_numerator.setter
    def signature_numerator(self, value) -> None:
        ...

    @property
    def start_marker(self) -> float:
        """
        Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).
        """
        ...

    @start_marker.setter
    def start_marker(self, value) -> None:
        ...

    @property
    def start_time(self) -> float:
        """
        Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement View clips, this is the offset within the arrangement.
        """
        ...

    @property
    def velocity_amount(self) -> float:
        """
        Get/Set access to the velocity to volume amount of the Clip.
        """
        ...

    @velocity_amount.setter
    def velocity_amount(self, value) -> None:
        ...

    @property
    def view(self) -> View:
        """
        Get the view of the Clip.
        """
        ...

    @property
    def warp_markers(self) -> tuple[WarpMarker, ...]:
        """
        Available for AudioClips only.Get the warp markers for this audio clip.
        """
        ...

    @property
    def warp_mode(self) -> int:
        """
        Available for AudioClips only.Get/Set the warp mode for this audio clip.
        """
        ...

    @warp_mode.setter
    def warp_mode(self, value) -> None:
        ...

    @property
    def warping(self) -> bool:
        """
        Available for AudioClips only.Get/Set if this Clip is timestreched.
        """
        ...

    @warping.setter
    def warping(self, value) -> None:
        ...

    @property
    def will_record_on_start(self) -> bool:
        """
        returns true if the Clip will record on being started.
        """
        ...

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        ...

    def add_color_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        ...

    def add_end_marker_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "end_marker" has changed.
        """
        ...

    def add_end_time_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "end_time" has changed.
        """
        ...

    def add_file_path_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "file_path" has changed.
        """
        ...

    def add_gain_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "gain" has changed.
        """
        ...

    def add_groove_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "groove" has changed.
        """
        ...

    def add_has_envelopes_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "has_envelopes" has changed.
        """
        ...

    def add_is_overdubbing_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_overdubbing" has changed.
        """
        ...

    def add_is_recording_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_recording" has changed.
        """
        ...

    def add_launch_mode_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "launch_mode" has changed.
        """
        ...

    def add_launch_quantization_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "launch_quantization" has changed.
        """
        ...

    def add_legato_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "legato" has changed.
        """
        ...

    def add_loop_end_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "loop_end" has changed.
        """
        ...

    def add_loop_jump_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "loop_jump" has changed.
        """
        ...

    def add_loop_start_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "loop_start" has changed.
        """
        ...

    def add_looping_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "looping" has changed.
        """
        ...

    def add_muted_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "muted" has changed.
        """
        ...

    def add_name_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        ...

    def add_new_notes(self, arg2: object) -> IntU64Vector:
        """
        Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification objects. The objects will be used to construct new notes in the clip.
        """
        ...

    def add_notes_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "notes" has changed.
        """
        ...

    def add_pitch_coarse_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "pitch_coarse" has changed.
        """
        ...

    def add_pitch_fine_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "pitch_fine" has changed.
        """
        ...

    def add_playing_position_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "playing_position" has changed.
        """
        ...

    def add_playing_status_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "playing_status" has changed.
        """
        ...

    def add_position_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "position" has changed.
        """
        ...

    def add_ram_mode_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "ram_mode" has changed.
        """
        ...

    def add_signature_denominator_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "signature_denominator" has changed.
        """
        ...

    def add_signature_numerator_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "signature_numerator" has changed.
        """
        ...

    def add_start_marker_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "start_marker" has changed.
        """
        ...

    def add_start_time_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "start_time" has changed.
        """
        ...

    def add_velocity_amount_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "velocity_amount" has changed.
        """
        ...

    def add_warp_marker(self, warp_marker: object) -> None:
        """
        Available for AudioClips only. Adds the specified warp marker, if possible.
        """
        ...

    def add_warp_markers_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "warp_markers" has changed.
        """
        ...

    def add_warp_mode_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "warp_mode" has changed.
        """
        ...

    def add_warping_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "warping" has changed.
        """
        ...

    def apply_note_modifications(self, arg2: MidiNoteVector) -> None:
        """
        Expects a list of notes as returned from get_notes_extended. The content of the list will be used to modify existing notes in the clip, based on matching note IDs. This function should be used when modifying existing notes, e.g. changing the velocity or start time. The function ensures that per-note events attached to the modified notes are preserved. This is NOT the case when replacing notes via a combination of remove_notes_extended and add_new_notes. The given list can be a subset of the notes in the clip, but it must not contain any notes that are not present in the clip.
        """
        ...

    def automation_envelope(self, arg2: DeviceParameter) -> Envelope:
        """
        Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.
        """
        ...

    def beat_to_sample_time(self, beat_time: float) -> float:
        """
        Available for AudioClips only. Converts the given beat time to sample time. Raises an error if the sample is not warped.
        """
        ...

    def clear_all_envelopes(self) -> None:
        """
        Clears all envelopes for this clip.
        """
        ...

    def clear_envelope(self, arg2: DeviceParameter) -> None:
        """
        Clears the envelope of this clips given parameter.
        """
        ...

    def color_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color".
        """
        ...

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color_index".
        """
        ...

    def create_automation_envelope(self, arg2: DeviceParameter) -> Envelope:
        """
        Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.
        """
        ...

    def crop(self) -> None:
        """
        Crops the clip. The region that is cropped depends on whether the clip is looped or not. If looped, the region outside of the loop is removed. If not looped, the region outside the start and end markers is removed.
        """
        ...

    def deselect_all_notes(self) -> None:
        """
        De-selects all notes present in the clip.
        """
        ...

    def duplicate_loop(self) -> None:
        """
        Make the loop two times longer and duplicates notes and envelopes. Duplicates the clip start/end range if the clip is not looped.
        """
        ...

    def duplicate_notes_by_id(self, note_ids: object, destination_time: object=None, transposition_amount: int=0) -> IntU64Vector:
        """
        Duplicate all notes matching the given note IDs. If the optional destination_time is not provided, new notes will be inserted after the last selected note. This behavior can be observed when duplicating notes in the Live GUI. If the transposition_amount is specified, the notes in the region will be transposed by the number of semitones. Raises an error on audio clips.
        """
        ...

    def duplicate_region(self, region_start: float, region_length: float, destination_time: float, pitch: int=-1, transposition_amount: int=0) -> None:
        """
        Duplicate the notes in the specified region to the destination_time. Only notes of the specified pitch are duplicated or all if pitch is -1. If the transposition_amount is not 0, the notes in the region will be transposed by the transpose_amount of semitones.Raises an error on audio clips.
        """
        ...

    def end_marker_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "end_marker".
        """
        ...

    def end_time_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "end_time".
        """
        ...

    def file_path_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "file_path".
        """
        ...

    def fire(self) -> None:
        """
        (Re)Start playing this Clip.
        """
        ...

    def gain_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "gain".
        """
        ...

    def get_all_notes_extended(self) -> MidiNoteVector:
        """
        Returns a list of all MIDI notes from the clip, regardless of their position relative to the start and end markers/loop start and loop end. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
        """
        ...

    def get_notes(self, from_time: float, from_pitch: int, time_span: float, pitch_span: int) -> tuple:
        """
        Returns a tuple of tuples where each inner tuple represents a note starting in the given pitch- and time range. The inner tuple contains pitch, time, duration, velocity, and mute state.
        """
        ...

    def get_notes_by_id(self, note_ids: object) -> MidiNoteVector:
        """
        Return a list of MIDI notes matching the given note IDs.
        """
        ...

    def get_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> MidiNoteVector:
        """
        Returns a list of MIDI notes from the given pitch and time range. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
        """
        ...

    def get_selected_notes(self) -> tuple:
        """
        Returns a tuple of tuples where each inner tuple represents a selected note. The inner tuple contains pitch, time, duration, velocity, and mute state.
        """
        ...

    def get_selected_notes_extended(self) -> MidiNoteVector:
        """
        Returns a list of all MIDI notes from the clip that are currently selected. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
        """
        ...

    def groove_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "groove".
        """
        ...

    def has_envelopes_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_envelopes".
        """
        ...

    def is_overdubbing_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_overdubbing".
        """
        ...

    def is_recording_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_recording".
        """
        ...

    def launch_mode_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "launch_mode".
        """
        ...

    def launch_quantization_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "launch_quantization".
        """
        ...

    def legato_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "legato".
        """
        ...

    def loop_end_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop_end".
        """
        ...

    def loop_jump_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop_jump".
        """
        ...

    def loop_start_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop_start".
        """
        ...

    def looping_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "looping".
        """
        ...

    def move_playing_pos(self, arg2: float) -> None:
        """
        Jump forward or backward by the specified relative amount in beats. Will do nothing, if the Clip is not playing.
        """
        ...

    def move_warp_marker(self, marker_beat_time: float, beat_time_distance: float) -> None:
        """
        Available for AudioClips only. Moves the specified warp marker by the specified beat time amount, if possible.
        """
        ...

    def muted_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "muted".
        """
        ...

    def name_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        ...

    def note_number_to_name(self, midi_pitch: int) -> str:
        """
        Return a human-readable name for the given MIDI note number. Takes into account the scale and tonal spelling settings of the clip, as well as the current tuning system (if any)
        """
        ...

    def notes_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "notes".
        """
        ...

    def pitch_coarse_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "pitch_coarse".
        """
        ...

    def pitch_fine_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "pitch_fine".
        """
        ...

    def playing_position_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "playing_position".
        """
        ...

    def playing_status_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "playing_status".
        """
        ...

    def position_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "position".
        """
        ...

    def quantize(self, arg2: int, arg3: float) -> None:
        """
        Quantize all notes in a clip or align warp markers.
        """
        ...

    def quantize_pitch(self, arg2: int, arg3: int, arg4: float) -> None:
        """
        Quantize all the notes of a given pitch.  Raises an error on audio clips.
        """
        ...

    def ram_mode_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "ram_mode".
        """
        ...

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color_index".
        """
        ...

    def remove_color_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color".
        """
        ...

    def remove_end_marker_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "end_marker".
        """
        ...

    def remove_end_time_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "end_time".
        """
        ...

    def remove_file_path_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "file_path".
        """
        ...

    def remove_gain_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "gain".
        """
        ...

    def remove_groove_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "groove".
        """
        ...

    def remove_has_envelopes_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "has_envelopes".
        """
        ...

    def remove_is_overdubbing_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_overdubbing".
        """
        ...

    def remove_is_recording_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_recording".
        """
        ...

    def remove_launch_mode_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "launch_mode".
        """
        ...

    def remove_launch_quantization_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "launch_quantization".
        """
        ...

    def remove_legato_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "legato".
        """
        ...

    def remove_loop_end_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "loop_end".
        """
        ...

    def remove_loop_jump_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "loop_jump".
        """
        ...

    def remove_loop_start_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "loop_start".
        """
        ...

    def remove_looping_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "looping".
        """
        ...

    def remove_muted_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "muted".
        """
        ...

    def remove_name_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        ...

    def remove_notes(self, arg2: float, arg3: int, arg4: float, arg5: int) -> None:
        """
        Delete all notes starting in the given pitch- and time range.
        """
        ...

    def remove_notes_by_id(self, arg2: object) -> None:
        """
        Delete all notes matching the given note IDs. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.
        """
        ...

    def remove_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> None:
        """
        Delete all notes starting in the given pitch and time range. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.
        """
        ...

    def remove_notes_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "notes".
        """
        ...

    def remove_pitch_coarse_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "pitch_coarse".
        """
        ...

    def remove_pitch_fine_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "pitch_fine".
        """
        ...

    def remove_playing_position_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "playing_position".
        """
        ...

    def remove_playing_status_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "playing_status".
        """
        ...

    def remove_position_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "position".
        """
        ...

    def remove_ram_mode_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "ram_mode".
        """
        ...

    def remove_signature_denominator_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "signature_denominator".
        """
        ...

    def remove_signature_numerator_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "signature_numerator".
        """
        ...

    def remove_start_marker_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "start_marker".
        """
        ...

    def remove_start_time_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "start_time".
        """
        ...

    def remove_velocity_amount_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "velocity_amount".
        """
        ...

    def remove_warp_marker(self, beat_time: float) -> None:
        """
        Available for AudioClips only. Removes the specified warp marker, if possible.
        """
        ...

    def remove_warp_markers_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "warp_markers".
        """
        ...

    def remove_warp_mode_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "warp_mode".
        """
        ...

    def remove_warping_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "warping".
        """
        ...

    def replace_selected_notes(self, arg2: tuple) -> None:
        """
        Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_selected_notes. The notes described that way will then be used to replace the old selection.
        """
        ...

    def sample_to_beat_time(self, sample_time: float) -> float:
        """
        Available for AudioClips only. Converts the given sample time to beat time. Raises an error if the sample is not warped.
        """
        ...

    def scrub(self, scrub_position: float) -> None:
        """
        Scrubs inside a clip. scrub_position defines the position in beats that the scrub will start from. The scrub will continue until stop_scrub is called. Global quantization applies to the scrub's position and length.
        """
        ...

    def seconds_to_sample_time(self, seconds: float) -> float:
        """
        Available for AudioClips only. Converts the given seconds to sample time. Raises an error if the sample is warped.
        """
        ...

    def select_all_notes(self) -> None:
        """
        Selects all notes present in the clip.
        """
        ...

    def select_notes_by_id(self, arg2: object) -> None:
        """
        Selects all notes matching the given note IDs.
        """
        ...

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        Set the clip's fire button state directly. Supports all launch modes.
        """
        ...

    def set_notes(self, arg2: tuple) -> None:
        """
        Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_notes. The notes described that way will then be added to the clip.
        """
        ...

    def signature_denominator_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "signature_denominator".
        """
        ...

    def signature_numerator_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "signature_numerator".
        """
        ...

    def start_marker_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "start_marker".
        """
        ...

    def start_time_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "start_time".
        """
        ...

    def stop(self) -> None:
        """
        Stop playing this Clip.
        """
        ...

    def stop_scrub(self) -> None:
        """
        Stops the current scrub.
        """
        ...

    def velocity_amount_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "velocity_amount".
        """
        ...

    def warp_markers_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warp_markers".
        """
        ...

    def warp_mode_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warp_mode".
        """
        ...

    def warping_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warping".
        """
        ...


    class View:
        """
        Representing the view aspects of a Clip.
        """

        @property
        def _live_ptr(self):
            ...

        @property
        def canonical_parent(self):
            """
            Get the canonical parent of the clip view.
            """
            ...

        @property
        def grid_is_triplet(self):
            """
            Get/set wether the grid is showing in triplet mode.
            """
            ...

        @property
        def grid_quantization(self):
            """
            Get/set clip grid quantization resolution.
            """
            ...

        def hide_envelope(self) -> None:
            """
            Hide the envelope view.
            """
            ...

        def select_envelope_parameter(self, arg2: DeviceParameter) -> None:
            """
            Select the given device parameter in the envelope view.
            """
            ...

        def show_envelope(self) -> None:
            """
            Show the envelope view.
            """
            ...

        def show_loop(self) -> None:
            """
            Show the entire loop in the detail view.
            """
            ...


__all__ = ['Clip']

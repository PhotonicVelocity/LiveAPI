# Clip (Module)

## Clip (Class)

> `Live.Clip.Clip`

This class represents a Clip in Live. It can be either an Audio Clip or a MIDI Clip, in an Arrangement or the Session, depending on the Track (Slot) it lives in.

**Live Object:** `yes`

**Access via:**

- `ClipSlot.clip`
- `ClipSlot.create_audio_clip()`
- `ClipSlot.create_clip()`
- `Song.View.detail_clip`
- `TakeLane.create_audio_clip()`
- `TakeLane.create_midi_clip()`
- `Track.create_audio_clip()`
- `Track.create_midi_clip()`
- `Track.duplicate_clip_to_arrangement()`

### Properties

| Property                                          | Type                          | Supports             |
| ------------------------------------------------- | ----------------------------- | -------------------- |
| [`automation_envelopes`](#automation_envelopes)   | `tuple`                       | `get`                |
| [`available_warp_modes`](#available_warp_modes)   | `tuple[int, Ellipsis]`        | `get`                |
| [`canonical_parent`](#canonical_parent)           | `ClipSlot`                    | `get`                |
| [`color`](#color)                                 | `int`                         | `get`/`set`/`listen` |
| [`color_index`](#color_index)                     | `int`                         | `get`/`set`/`listen` |
| [`end_marker`](#end_marker)                       | `float`                       | `get`/`set`/`listen` |
| [`end_time`](#end_time)                           | `float`                       | `get`/`listen`       |
| [`file_path`](#file_path)                         | `str`                         | `get`/`listen`       |
| [`gain`](#gain)                                   | `float`                       | `get`/`set`/`listen` |
| [`gain_display_string`](#gain_display_string)     | `str`                         | `get`                |
| [`groove`](#groove)                               | `None`                        | `get`/`set`/`listen` |
| [`has_envelopes`](#has_envelopes)                 | `bool`                        | `get`/`listen`       |
| [`has_groove`](#has_groove)                       | `bool`                        | `get`                |
| [`is_arrangement_clip`](#is_arrangement_clip)     | `bool`                        | `get`                |
| [`is_audio_clip`](#is_audio_clip)                 | `bool`                        | `get`                |
| [`is_midi_clip`](#is_midi_clip)                   | `bool`                        | `get`                |
| [`is_overdubbing`](#is_overdubbing)               | `bool`                        | `get`/`listen`       |
| [`is_playing`](#is_playing)                       | `bool`                        | `get`/`set`          |
| [`is_recording`](#is_recording)                   | `bool`                        | `get`/`listen`       |
| [`is_session_clip`](#is_session_clip)             | `bool`                        | `get`                |
| [`is_take_lane_clip`](#is_take_lane_clip)         | `bool`                        | `get`                |
| [`is_triggered`](#is_triggered)                   | `bool`                        | `get`                |
| [`launch_mode`](#launch_mode)                     | `int`                         | `get`/`set`/`listen` |
| [`launch_quantization`](#launch_quantization)     | `int`                         | `get`/`set`/`listen` |
| [`legato`](#legato)                               | `bool`                        | `get`/`set`/`listen` |
| [`length`](#length)                               | `float`                       | `get`                |
| [`loop_end`](#loop_end)                           | `float`                       | `get`/`set`/`listen` |
| [`loop_start`](#loop_start)                       | `float`                       | `get`/`set`/`listen` |
| [`looping`](#looping)                             | `bool`                        | `get`/`set`/`listen` |
| [`muted`](#muted)                                 | `bool`                        | `get`/`set`/`listen` |
| [`name`](#name)                                   | `str`                         | `get`/`set`/`listen` |
| [`pitch_coarse`](#pitch_coarse)                   | `int`                         | `get`/`set`/`listen` |
| [`pitch_fine`](#pitch_fine)                       | `float`                       | `get`/`set`/`listen` |
| [`playing_position`](#playing_position)           | `float`                       | `get`/`listen`       |
| [`position`](#position)                           | `float`                       | `get`/`set`/`listen` |
| [`ram_mode`](#ram_mode)                           | `bool`                        | `get`/`set`/`listen` |
| [`sample_length`](#sample_length)                 | `int`                         | `get`                |
| [`sample_rate`](#sample_rate)                     | `float`                       | `get`                |
| [`signature_denominator`](#signature_denominator) | `int`                         | `get`/`set`/`listen` |
| [`signature_numerator`](#signature_numerator)     | `int`                         | `get`/`set`/`listen` |
| [`start_marker`](#start_marker)                   | `float`                       | `get`/`set`/`listen` |
| [`start_time`](#start_time)                       | `float`                       | `get`/`listen`       |
| [`velocity_amount`](#velocity_amount)             | `float`                       | `get`/`set`/`listen` |
| [`view`](#view)                                   | `View`                        | `get`                |
| [`warp_markers`](#warp_markers)                   | `tuple[WarpMarker, Ellipsis]` | `get`/`listen`       |
| [`warp_mode`](#warp_mode)                         | `int`                         | `get`/`set`/`listen` |
| [`warping`](#warping)                             | `bool`                        | `get`/`set`/`listen` |
| [`will_record_on_start`](#will_record_on_start)   | `bool`                        | `get`                |

#### `automation_envelopes`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `no`

Const access to a list of all automation envelopes for this clip.

#### `available_warp_modes`

- **Type:** `tuple[int, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Available for AudioClips only. Get/Set the available warp modes, that can be used.

#### `canonical_parent`

- **Type:** `ClipSlot`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the Clip.

#### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the color of the Clip (RGB).

#### `color_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the color index of the Clip.

#### `end_marker`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).

#### `end_time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Get the clip's end time.

#### `file_path`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Get the path of the file represented by the Audio Clip.

#### `gain`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Read/write access to the gain setting of the Audio Clip

#### `gain_display_string`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return a string with the gain as dB value

#### `groove`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Get the groove associated with this clip.

#### `has_envelopes`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Will notify if the clip gets his first envelope or the last envelope is removed.

#### `has_groove`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if a groove is associated with this clip.

#### `is_arrangement_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return true if this Clip is an Arrangement Clip. A Clip can be either a Session or Arrangement Clip.

#### `is_audio_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return true if this Clip is an Audio Clip. A Clip can be either an Audioclip or a MIDI Clip.

#### `is_midi_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return true if this Clip is a MIDI Clip. A Clip can be either an Audioclip or a MIDI Clip.

#### `is_overdubbing`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

returns true if the Clip is recording overdubs

#### `is_playing`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set if this Clip is currently playing. If the Clips trigger mode is set to a quantization value, the Clip will not start playing immediately. If you need to know wether the Clip was triggered, use the is_triggered property.

#### `is_recording`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

returns true if the Clip was triggered to record or is recording.

#### `is_session_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return true if this Clip is a Session Clip. A Clip can be either a Session or Arrangement Clip.

#### `is_take_lane_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return true if this Clip is a Take Lane Clip. A Take Lane Clip is also always an Arrangement Clip.

#### `is_triggered`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

returns true if the Clip was triggered or is playing.

#### `launch_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the launch mode setting of the Clip.

#### `launch_quantization`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the launch quantization setting of the Clip.

#### `legato`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the legato setting of the Clip

#### `length`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Get to the Clips length in beats/seconds (unit depends on warping).

#### `loop_end`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).

#### `loop_start`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).

#### `looping`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the Clips 'loop is enabled' flag .Only Warped Audio Clips or MIDI Clip can be looped.

#### `muted`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write access to the mute state of the Clip.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write access to the name of the Clip.

#### `pitch_coarse`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Read/write access to the pitch (in halftones) setting of the Audio Clip, ranging from -48 to 48

#### `pitch_fine`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Read/write access to the pitch fine setting of the Audio Clip, ranging from -500 to 500

#### `playing_position`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Constant access to the current playing position of the clip. The returned value is the position in beats for midi and warped audio clips, or in seconds for unwarped audio clips. Stopped clips will return 0.

#### `position`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).

#### `ram_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Read/write access to the Ram mode setting of the Audio Clip

#### `sample_length`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Available for AudioClips only. Get the sample length in sample time or -1 if there is no sample available.

#### `sample_rate`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Available for AudioClips only. Read-only access to the Clip's sampling rate.

#### `signature_denominator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the global signature denominator of the Clip.

#### `signature_numerator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the global signature numerator of the Clip.

#### `start_marker`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).

#### `start_time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement View clips, this is the offset within the arrangement.

#### `velocity_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the velocity to volume amount of the Clip.

#### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Get the view of the Clip.

#### `warp_markers`

- **Type:** `tuple[WarpMarker, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Available for AudioClips only. Get the warp markers for this audio clip.

#### `warp_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Get/Set the warp mode for this audio clip.

#### `warping`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Available for AudioClips only. Get/Set if this Clip is timestreched.

#### `will_record_on_start`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

returns true if the Clip will record on being started.

### Methods

| Method                                                                                                                                         | Returns          |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [`add_new_notes()`](#add_new_notesnotes-object)                                                                                                | `IntU64Vector`   |
| [`add_warp_marker()`](#add_warp_markerwarp_marker-warpmarker)                                                                                  | `None`           |
| [`apply_note_modifications()`](#apply_note_modificationsnotes-midinotevector)                                                                  | `None`           |
| [`automation_envelope()`](#automation_envelopeparameter-deviceparameter)                                                                       | `Envelope`       |
| [`beat_to_sample_time()`](#beat_to_sample_timebeat_time-float)                                                                                 | `float`          |
| [`clear_all_envelopes()`](#clear_all_envelopes)                                                                                                | `None`           |
| [`clear_envelope()`](#clear_envelopeparameter-deviceparameter)                                                                                 | `None`           |
| [`create_automation_envelope()`](#create_automation_envelopeparameter-deviceparameter)                                                         | `Envelope`       |
| [`crop()`](#crop)                                                                                                                              | `None`           |
| [`deselect_all_notes()`](#deselect_all_notes)                                                                                                  | `None`           |
| [`duplicate_loop()`](#duplicate_loop)                                                                                                          | `None`           |
| [`duplicate_notes_by_id()`](#duplicate_notes_by_idnote_ids-listint-destination_time-float-none-transposition_amount-int-0)                     | `IntU64Vector`   |
| [`duplicate_region()`](#duplicate_regionregion_start-float-region_length-float-destination_time-float-pitch-int--1-transposition_amount-int-0) | `None`           |
| [`fire()`](#fire)                                                                                                                              | `None`           |
| [`get_all_notes_extended()`](#get_all_notes_extended)                                                                                          | `MidiNoteVector` |
| [`get_notes()`](#get_notesfrom_time-float-from_pitch-int-time_span-float-pitch_span-int)                                                       | `tuple`          |
| [`get_notes_by_id()`](#get_notes_by_idnote_ids-listint)                                                                                        | `MidiNoteVector` |
| [`get_notes_extended()`](#get_notes_extendedfrom_pitch-int-pitch_span-int-from_time-float-time_span-float)                                     | `MidiNoteVector` |
| [`get_selected_notes()`](#get_selected_notes)                                                                                                  | `tuple`          |
| [`get_selected_notes_extended()`](#get_selected_notes_extended)                                                                                | `MidiNoteVector` |
| [`move_playing_pos()`](#move_playing_posbeats-float)                                                                                           | `None`           |
| [`move_warp_marker()`](#move_warp_markermarker_beat_time-float-beat_time_distance-float)                                                       | `None`           |
| [`note_number_to_name()`](#note_number_to_namemidi_pitch-int)                                                                                  | `str`            |
| [`quantize()`](#quantizequantization_grid-int-amount-float)                                                                                    | `None`           |
| [`quantize_pitch()`](#quantize_pitchnote-int-source-int-amount-float)                                                                          | `None`           |
| [`remove_notes()`](#remove_notesstart_time-float-pitch-int-length-float-pitch_span-int)                                                        | `None`           |
| [`remove_notes_by_id()`](#remove_notes_by_idnote_ids-object)                                                                                   | `None`           |
| [`remove_notes_extended()`](#remove_notes_extendedfrom_pitch-int-pitch_span-int-from_time-float-time_span-float)                               | `None`           |
| [`remove_warp_marker()`](#remove_warp_markerbeat_time-float)                                                                                   | `None`           |
| [`replace_selected_notes()`](#replace_selected_notesnotes-tuple)                                                                               | `None`           |
| [`sample_to_beat_time()`](#sample_to_beat_timesample_time-float)                                                                               | `float`          |
| [`scrub()`](#scrubscrub_position-float)                                                                                                        | `None`           |
| [`seconds_to_sample_time()`](#seconds_to_sample_timeseconds-float)                                                                             | `float`          |
| [`select_all_notes()`](#select_all_notes)                                                                                                      | `None`           |
| [`select_notes_by_id()`](#select_notes_by_idnote_ids-object)                                                                                   | `None`           |
| [`set_fire_button_state()`](#set_fire_button_statestate-bool)                                                                                  | `None`           |
| [`set_notes()`](#set_notesnotes-tuple)                                                                                                         | `None`           |
| [`stop()`](#stop)                                                                                                                              | `None`           |
| [`stop_scrub()`](#stop_scrub)                                                                                                                  | `None`           |

#### `add_new_notes(notes: object)`

- **Returns:** `IntU64Vector`
- **Args:**
  - `notes: object`

Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification objects. The objects will be used to construct new notes in the clip.

#### `add_warp_marker(warp_marker: WarpMarker)`

- **Returns:** `None`
- **Args:**
  - `warp_marker: WarpMarker`

Available for AudioClips only. Adds the specified warp marker, if possible.

#### `apply_note_modifications(notes: MidiNoteVector)`

- **Returns:** `None`
- **Args:**
  - `notes: MidiNoteVector`

Expects a list of notes as returned from get_notes_extended. The content of the list will be used to modify existing notes in the clip, based on matching note IDs. This function should be used when modifying existing notes, e.g. changing the velocity or start time. The function ensures that per-note events attached to the modified notes are preserved. This is NOT the case when replacing notes via a combination of remove_notes_extended and add_new_notes. The given list can be a subset of the notes in the clip, but it must not contain any notes that are not present in the clip.

#### `automation_envelope(parameter: DeviceParameter)`

- **Returns:** `Envelope`
- **Args:**
  - `parameter: DeviceParameter`

Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.

#### `beat_to_sample_time(beat_time: float)`

- **Returns:** `float`
- **Args:**
  - `beat_time: float`

Available for AudioClips only. Converts the given beat time to sample time. Raises an error if the sample is not warped.

#### `clear_all_envelopes()`

- **Returns:** `None`

Clears all envelopes for this clip.

#### `clear_envelope(parameter: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `parameter: DeviceParameter`

Clears the envelope of this clips given parameter.

#### `create_automation_envelope(parameter: DeviceParameter)`

- **Returns:** `Envelope`
- **Args:**
  - `parameter: DeviceParameter`

Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.

#### `crop()`

- **Returns:** `None`

Crops the clip. The region that is cropped depends on whether the clip is looped or not. If looped, the region outside of the loop is removed. If not looped, the region outside the start and end markers is removed.

#### `deselect_all_notes()`

- **Returns:** `None`

De-selects all notes present in the clip.

#### `duplicate_loop()`

- **Returns:** `None`

Make the loop two times longer and duplicates notes and envelopes. Duplicates the clip start/end range if the clip is not looped.

#### `duplicate_notes_by_id(note_ids: list[int], destination_time: float = None, transposition_amount: int = 0)`

- **Returns:** `IntU64Vector`
- **Args:**
  - `note_ids: list[int]`
  - `destination_time: float = None`
  - `transposition_amount: int = 0`

Duplicate all notes matching the given note IDs. If the optional destination_time is not provided, new notes will be inserted after the last selected note. This behavior can be observed when duplicating notes in the Live GUI. If the transposition_amount is specified, the notes in the region will be transposed by the number of semitones. Raises an error on audio clips.

#### `duplicate_region(region_start: float, region_length: float, destination_time: float, pitch: int = -1, transposition_amount: int = 0)`

- **Returns:** `None`
- **Args:**
  - `region_start: float`
  - `region_length: float`
  - `destination_time: float`
  - `pitch: int = -1`
  - `transposition_amount: int = 0`

Duplicate the notes in the specified region to the destination_time. Only notes of the specified pitch are duplicated or all if pitch is -1. If the transposition_amount is not 0, the notes in the region will be transposed by the transpose_amount of semitones.Raises an error on audio clips.

#### `fire()`

- **Returns:** `None`

(Re)Start playing this Clip.

#### `get_all_notes_extended()`

- **Returns:** `MidiNoteVector`

Returns a list of all MIDI notes from the clip, regardless of their position relative to the start and end markers/loop start and loop end. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.

#### `get_notes(from_time: float, from_pitch: int, time_span: float, pitch_span: int)`

- **Returns:** `tuple`
- **Args:**
  - `from_time: float`
  - `from_pitch: int`
  - `time_span: float`
  - `pitch_span: int`

Returns a tuple of tuples where each inner tuple represents a note starting in the given pitch- and time range. The inner tuple contains pitch, time, duration, velocity, and mute state.

#### `get_notes_by_id(note_ids: list[int])`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `note_ids: list[int]`

Return a list of MIDI notes matching the given note IDs.

#### `get_notes_extended(from_pitch: int, pitch_span: int, from_time: float, time_span: float)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `from_pitch: int`
  - `pitch_span: int`
  - `from_time: float`
  - `time_span: float`

Returns a list of MIDI notes from the given pitch and time range. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.

#### `get_selected_notes()`

- **Returns:** `tuple`

Returns a tuple of tuples where each inner tuple represents a selected note. The inner tuple contains pitch, time, duration, velocity, and mute state.

#### `get_selected_notes_extended()`

- **Returns:** `MidiNoteVector`

Returns a list of all MIDI notes from the clip that are currently selected. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.

#### `move_playing_pos(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float`

Jump forward or backward by the specified relative amount in beats. Will do nothing, if the Clip is not playing.

#### `move_warp_marker(marker_beat_time: float, beat_time_distance: float)`

- **Returns:** `None`
- **Args:**
  - `marker_beat_time: float`
  - `beat_time_distance: float`

Available for AudioClips only. Moves the specified warp marker by the specified beat time amount, if possible.

#### `note_number_to_name(midi_pitch: int)`

- **Returns:** `str`
- **Args:**
  - `midi_pitch: int`

Return a human-readable name for the given MIDI note number. Takes into account the scale and tonal spelling settings of the clip, as well as the current tuning system (if any)

#### `quantize(quantization_grid: int, amount: float)`

- **Returns:** `None`
- **Args:**
  - `quantization_grid: int`
  - `amount: float`

Quantize all notes in a clip or align warp markers.

#### `quantize_pitch(note: int, source: int, amount: float)`

- **Returns:** `None`
- **Args:**
  - `note: int`
  - `source: int`
  - `amount: float`

Quantize all the notes of a given pitch. Raises an error on audio clips.

#### `remove_notes(start_time: float, pitch: int, length: float, pitch_span: int)`

- **Returns:** `None`
- **Args:**
  - `start_time: float`
  - `pitch: int`
  - `length: float`
  - `pitch_span: int`

Delete all notes starting in the given pitch- and time range.

#### `remove_notes_by_id(note_ids: object)`

- **Returns:** `None`
- **Args:**
  - `note_ids: object`

Delete all notes matching the given note IDs. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.

#### `remove_notes_extended(from_pitch: int, pitch_span: int, from_time: float, time_span: float)`

- **Returns:** `None`
- **Args:**
  - `from_pitch: int`
  - `pitch_span: int`
  - `from_time: float`
  - `time_span: float`

Delete all notes starting in the given pitch and time range. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.

#### `remove_warp_marker(beat_time: float)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float`

Available for AudioClips only. Removes the specified warp marker, if possible.

#### `replace_selected_notes(notes: tuple)`

- **Returns:** `None`
- **Args:**
  - `notes: tuple`

Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_selected_notes. The notes described that way will then be used to replace the old selection.

#### `sample_to_beat_time(sample_time: float)`

- **Returns:** `float`
- **Args:**
  - `sample_time: float`

Available for AudioClips only. Converts the given sample time to beat time. Raises an error if the sample is not warped.

#### `scrub(scrub_position: float)`

- **Returns:** `None`
- **Args:**
  - `scrub_position: float`

Scrubs inside a clip. scrub_position defines the position in beats that the scrub will start from. The scrub will continue until stop_scrub is called. Global quantization applies to the scrub's position and length.

#### `seconds_to_sample_time(seconds: float)`

- **Returns:** `float`
- **Args:**
  - `seconds: float`

Available for AudioClips only. Converts the given seconds to sample time. Raises an error if the sample is warped.

#### `select_all_notes()`

- **Returns:** `None`

Selects all notes present in the clip.

#### `select_notes_by_id(note_ids: object)`

- **Returns:** `None`
- **Args:**
  - `note_ids: object`

Selects all notes matching the given note IDs.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`

Set the clip's fire button state directly. Supports all launch modes.

#### `set_notes(notes: tuple)`

- **Returns:** `None`
- **Args:**
  - `notes: tuple`

Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_notes. The notes described that way will then be added to the clip.

#### `stop()`

- **Returns:** `None`

Stop playing this Clip.

#### `stop_scrub()`

- **Returns:** `None`

Stops the current scrub.

## Clip.View (Subclass)

> `Live.Clip.Clip.View`

Representing the view aspects of a Clip.

**Live Object:** `yes`

### Properties

| Property                                  | Type               | Supports    |
| ----------------------------------------- | ------------------ | ----------- |
| [`canonical_parent`](#canonical_parent)   | `Clip`             | `get`       |
| [`grid_is_triplet`](#grid_is_triplet)     | `bool`             | `get`/`set` |
| [`grid_quantization`](#grid_quantization) | `GridQuantization` | `get`/`set` |

#### `canonical_parent`

- **Type:** `Clip`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the clip view.

#### `grid_is_triplet`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set wether the grid is showing in triplet mode.

#### `grid_quantization`

- **Type:** `GridQuantization`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set clip grid quantization resolution.

### Methods

| Method                                                                               | Returns |
| ------------------------------------------------------------------------------------ | ------- |
| [`hide_envelope()`](#hide_envelope)                                                  | `None`  |
| [`select_envelope_parameter()`](#select_envelope_parameterparameter-deviceparameter) | `None`  |
| [`show_envelope()`](#show_envelope)                                                  | `None`  |
| [`show_loop()`](#show_loop)                                                          | `None`  |

#### `hide_envelope()`

- **Returns:** `None`

Hide the envelope view.

#### `select_envelope_parameter(parameter: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `parameter: DeviceParameter`

Select the given device parameter in the envelope view.

#### `show_envelope()`

- **Returns:** `None`

Show the envelope view.

#### `show_loop()`

- **Returns:** `None`

Show the entire loop in the detail view.

## Enums

### `ClipLaunchQuantization`

| Value | Name                  |
| ----- | --------------------- |
| `0`   | `q_global`            |
| `1`   | `q_none`              |
| `2`   | `q_8_bars`            |
| `3`   | `q_4_bars`            |
| `4`   | `q_2_bars`            |
| `5`   | `q_bar`               |
| `6`   | `q_half`              |
| `7`   | `q_half_triplet`      |
| `8`   | `q_quarter`           |
| `9`   | `q_quarter_triplet`   |
| `10`  | `q_eighth`            |
| `11`  | `q_eighth_triplet`    |
| `12`  | `q_sixteenth`         |
| `13`  | `q_sixteenth_triplet` |
| `14`  | `q_thirtysecond`      |

### `GridQuantization`

| Value | Name             |
| ----- | ---------------- |
| `0`   | `no_grid`        |
| `1`   | `g_8_bars`       |
| `2`   | `g_4_bars`       |
| `3`   | `g_2_bars`       |
| `4`   | `g_bar`          |
| `5`   | `g_half`         |
| `6`   | `g_quarter`      |
| `7`   | `g_eighth`       |
| `8`   | `g_sixteenth`    |
| `9`   | `g_thirtysecond` |
| `10`  | `count`          |

### `LaunchMode`

| Value | Name      |
| ----- | --------- |
| `0`   | `trigger` |
| `1`   | `gate`    |
| `2`   | `toggle`  |
| `3`   | `repeat`  |

### `WarpMode`

| Value | Name          |
| ----- | ------------- |
| `0`   | `beats`       |
| `1`   | `tones`       |
| `2`   | `texture`     |
| `3`   | `repitch`     |
| `4`   | `complex`     |
| `5`   | `rex`         |
| `6`   | `complex_pro` |
| `7`   | `count`       |

## Types

### MidiNote

> `Live.Clip.MidiNote`

An object representing a MIDI Note

#### Properties

| Property                                    | Type    | Supports    |
| ------------------------------------------- | ------- | ----------- |
| [`duration`](#duration)                     | `float` | `get`/`set` |
| [`mute`](#mute)                             | `bool`  | `get`/`set` |
| [`note_id`](#note_id)                       | `int`   | `get`       |
| [`pitch`](#pitch)                           | `int`   | `get`/`set` |
| [`probability`](#probability)               | `float` | `get`/`set` |
| [`release_velocity`](#release_velocity)     | `float` | `get`/`set` |
| [`start_time`](#start_time)                 | `float` | `get`/`set` |
| [`velocity`](#velocity)                     | `float` | `get`/`set` |
| [`velocity_deviation`](#velocity_deviation) | `float` | `get`/`set` |

##### `duration`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

##### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

##### `note_id`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

A numerical ID that's unique within the originating clip of the note. Not to be used directly, but important for other API calls, namely apply_note_modifications.

##### `pitch`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

##### `probability`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

##### `release_velocity`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

##### `start_time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

##### `velocity`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

##### `velocity_deviation`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

### MidiNoteSpecification

> `Live.Clip.MidiNoteSpecification`

An object specifying the data for creating a MIDI note. To be used with the add_new_notes function.

**Constructor:** `MidiNoteSpecification(pitch: int, start_time: float, duration: float, velocity: float = 100.0, mute: bool = False, probability: float = 1.0, velocity_deviation: float = 0.0, release_velocity: float = 64.0)`

### MidiNoteVector

> `Live.Clip.MidiNoteVector`

A container for holding MIDI notes from Live.

#### Methods

| Method                               | Returns |
| ------------------------------------ | ------- |
| [`append()`](#appendvalue-midinote)  | `None`  |
| [`extend()`](#extendvalues-midinote) | `None`  |

##### `append(value: MidiNote)`

- **Returns:** `None`
- **Args:**
  - `value: MidiNote`

##### `extend(values: MidiNote)`

- **Returns:** `None`
- **Args:**
  - `values: MidiNote`

### WarpMarker

> `Live.Clip.WarpMarker`

This class represents a WarpMarker type.

**Constructor:** `WarpMarker(sample_time: float, beat_time: float)`

#### Properties

| Property                      | Type    | Supports |
| ----------------------------- | ------- | -------- |
| [`beat_time`](#beat_time)     | `float` | `get`    |
| [`sample_time`](#sample_time) | `float` | `get`    |

##### `beat_time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

A WarpMarker's beat time.

##### `sample_time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

A WarpMarker's sample time.

### WarpMarkerVector

> `Live.Clip.WarpMarkerVector`

A container for returning warp markers from Live.

#### Methods

| Method                                 | Returns |
| -------------------------------------- | ------- |
| [`append()`](#appendvalue-warpmarker)  | `None`  |
| [`extend()`](#extendvalues-warpmarker) | `None`  |

##### `append(value: WarpMarker)`

- **Returns:** `None`
- **Args:**
  - `value: WarpMarker`

##### `extend(values: WarpMarker)`

- **Returns:** `None`
- **Args:**
  - `values: WarpMarker`

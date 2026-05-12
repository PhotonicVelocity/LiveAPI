---
module: Clip
---

## Classes

### Clip

```yaml
kind: class
path: Live.Clip.Clip
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: |-
  This class represents a Clip in Live. It can be either an Audio
  Clip or a MIDI Clip, in an Arrangement or the Session, depending
  on the Track (Slot) it lives in.
```

#### Properties

##### automation_envelopes

```yaml
kind: property
type: Live.Base.Vector[Live.Envelope.Envelope]
settable: false
raw_doc: Const access to a list of all automation envelopes for this clip.
```

##### available_warp_modes

```yaml
kind: property
type: Live.Base.IntVector
settable: false
raw_doc: |-
  Available for AudioClips only.
  Get/Set the available warp modes, that can be used.
```

##### canonical_parent

```yaml
kind: property
type: Live.ClipSlot.ClipSlot
settable: false
raw_doc: Get the canonical parent of the Clip.
```

##### color

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/set access to the color of the Clip (RGB).
```

##### color_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/set access to the color index of the Clip.
```

##### end_marker

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).
```

##### end_time

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Get the clip's end time.
```

##### file_path

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: Get the path of the file represented by the Audio Clip.
```

##### gain

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Read/write access to the gain setting of the
  Audio Clip
```

##### gain_display_string

```yaml
kind: property
type: str
settable: false
raw_doc: Return a string with the gain as dB value
```

##### groove

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Get the groove associated with this clip.
```

##### has_envelopes

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Will notify if the clip gets his first envelope or the last envelope is removed.
```

##### has_groove

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if a groove is associated with this clip.
```

##### is_arrangement_clip

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return true if this Clip is an Arrangement Clip.
  A Clip can be either a Session or Arrangement Clip.
```

##### is_audio_clip

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  Return true if this Clip is an Audio Clip.
  A Clip can be either an Audioclip or a MIDI Clip.
```

##### is_midi_clip

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return true if this Clip is a MIDI Clip.
  A Clip can be either an Audioclip or a MIDI Clip.
```

##### is_overdubbing

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: returns true if the Clip is recording overdubs
```

##### is_playing

```yaml
kind: property
type: bool
settable: true
raw_doc: |-
  Get/Set if this Clip is currently playing. If the Clips trigger mode
  is set to a quantization value, the Clip will not start playing immediately.
  If you need to know wether the Clip was triggered, use the is_triggered property.
```

##### is_recording

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: returns true if the Clip was triggered to record or is recording.
```

##### is_session_clip

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return true if this Clip is a Session Clip.
  A Clip can be either a Session or Arrangement Clip.
```

##### is_take_lane_clip

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return true if this Clip is a Take Lane Clip.
  A Take Lane Clip is also always an Arrangement Clip.
```

##### is_triggered

```yaml
kind: property
type: bool
settable: false
raw_doc: returns true if the Clip was triggered or is playing.
```

##### launch_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the launch mode setting of the Clip.
```

##### launch_quantization

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the launch quantization setting of the Clip.
```

##### legato

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set access to the legato setting of the Clip
```

##### length

```yaml
kind: property
type: float
settable: false
raw_doc: Get to the Clips length in beats/seconds (unit depends on warping).
```

##### loop_end

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).
```

##### loop_start

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).
```

##### looping

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the Clips 'loop is enabled' flag
  .Only Warped Audio Clips or MIDI Clip can be looped.
```

##### muted

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Read/write access to the mute state of the Clip.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write access to the name of the Clip.
```

##### pitch_coarse

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Read/write access to the pitch (in halftones) setting of the
  Audio Clip, ranging from -48 to 48
```

##### pitch_fine

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Read/write access to the pitch fine setting of the
  Audio Clip, ranging from -500 to 500
```

##### playing_position

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Constant access to the current playing position of the clip.
  The returned value is the position in beats for midi and warped audio clips,
  or in seconds for unwarped audio clips. Stopped clips will return 0.
```

##### position

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
```

##### ram_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Read/write access to the Ram mode setting of the Audio Clip
```

##### sample_length

```yaml
kind: property
type: int
settable: false
raw_doc: |-
  Available for AudioClips only.
  Get the sample length in sample time or -1 if there is no sample available.
```

##### sample_rate

```yaml
kind: property
type: float
settable: false
raw_doc: |-
  Available for AudioClips only.
  Read-only access to the Clip's sampling rate.
```

##### signature_denominator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the global signature denominator of the Clip.
```

##### signature_numerator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the global signature numerator of the Clip.
```

##### start_marker

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).
```

##### start_time

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement
  View clips, this is the offset within the arrangement.
```

##### velocity_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set access to the velocity to volume amount of the Clip.
```

##### view

```yaml
kind: property
type: Live.Clip.Clip.View
settable: false
raw_doc: Get the view of the Clip.
```

##### warp_markers

```yaml
kind: property
type: Live.Clip.WarpMarkerVector
settable: false
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Get the warp markers for this audio clip.
```

##### warp_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Get/Set the warp mode for this audio clip.
```

##### warping

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Available for AudioClips only.
  Get/Set if this Clip is timestreched.
```

##### will_record_on_start

```yaml
kind: property
type: bool
settable: false
raw_doc: returns true if the Clip will record on being started.
```

##### loop_jump

```yaml
kind: property
listenable: true
```

##### notes

```yaml
kind: property
listenable: true
```

##### playing_status

```yaml
kind: property
listenable: true
```

#### Methods

##### add_new_notes

```yaml
kind: method
signature: 'add_new_notes( (Clip)arg1, (object)arg2) -> IntU64Vector :'
cpp_signature: std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)
args:
- name: arg2
  type: object
returns:
  type: Live.Base.IntU64Vector
raw_doc: |-
  Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification
  objects. The objects will be used to construct new notes in the clip.
```

##### add_warp_marker

```yaml
kind: method
signature: 'add_warp_marker( (Clip)self, (object)warp_marker) -> None :'
cpp_signature: void add_warp_marker(TPyHandle<AClip>,boost::python::api::object)
args:
- name: warp_marker
  type: object
returns:
  type: None
raw_doc: |-
  Available for AudioClips only.
  Adds the specified warp marker, if possible.
```

##### apply_note_modifications

```yaml
kind: method
signature: 'apply_note_modifications( (Clip)arg1, (MidiNoteVector)arg2) -> None :'
cpp_signature: void apply_note_modifications(TPyHandle<AClip>,std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>>)
args:
- name: arg2
  type: Live.Clip.MidiNoteVector
returns:
  type: None
raw_doc: |-
  Expects a list of notes as returned from get_notes_extended. The content
  of the list will be used to modify existing notes in the clip, based on
  matching note IDs.
  This function should be used when modifying existing notes, e.g. changing the
  velocity or start time. The function ensures that per-note events attached to
  the modified notes are preserved. This is NOT the case when replacing notes
  via a combination of remove_notes_extended and add_new_notes.
  The given list can be a subset of the notes in the clip, but it must not
  contain any notes that are not present in the clip.
```

##### automation_envelope

```yaml
kind: method
signature: 'automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :'
cpp_signature: TWeakPtr<TPyHandle<AAutomation>> automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
args:
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: Live.Envelope.Envelope
raw_doc: Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement
  clips.Returns None for parameters from a different track.
```

##### beat_to_sample_time

```yaml
kind: method
signature: 'beat_to_sample_time( (Clip)self, (float)beat_time) -> float :'
cpp_signature: double beat_to_sample_time(TPyHandle<AClip>,double)
args:
- name: beat_time
  type: float
returns:
  type: float
raw_doc: |-
  Available for AudioClips only.
  Converts the given beat time to sample time. Raises an error if the sample is not warped.
```

##### clear_all_envelopes

```yaml
kind: method
signature: 'clear_all_envelopes( (Clip)arg1) -> None :'
cpp_signature: void clear_all_envelopes(TPyHandle<AClip>)
returns:
  type: None
raw_doc: Clears all envelopes for this clip.
```

##### clear_envelope

```yaml
kind: method
signature: 'clear_envelope( (Clip)arg1, (DeviceParameter)arg2) -> None :'
cpp_signature: void clear_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
args:
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: None
raw_doc: Clears the envelope of this clips given parameter.
```

##### create_automation_envelope

```yaml
kind: method
signature: 'create_automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :'
cpp_signature: TWeakPtr<TPyHandle<AAutomation>> create_automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
args:
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: Live.Envelope.Envelope
raw_doc: Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises
  an error if the envelope can't be created.
```

##### crop

```yaml
kind: method
signature: 'crop( (Clip)arg1) -> None :'
cpp_signature: void crop(TPyHandle<AClip>)
returns:
  type: None
raw_doc: |-
  Crops the clip. The region that is cropped depends on whether the clip is
  looped or not. If looped, the region outside of the loop is removed.
  If not looped, the region outside the start and end markers is removed.
```

##### deselect_all_notes

```yaml
kind: method
signature: 'deselect_all_notes( (Clip)arg1) -> None :'
cpp_signature: void deselect_all_notes(TPyHandle<AClip>)
returns:
  type: None
raw_doc: De-selects all notes present in the clip.
```

##### duplicate_loop

```yaml
kind: method
signature: 'duplicate_loop( (Clip)arg1) -> None :'
cpp_signature: void duplicate_loop(TPyHandle<AClip>)
returns:
  type: None
raw_doc: |-
  Make the loop two times longer and duplicates notes and envelopes.
  Duplicates the clip start/end range if the clip is not looped.
```

##### duplicate_notes_by_id

```yaml
kind: method
signature: 'duplicate_notes_by_id( (Clip)self, (object)note_ids [, (object)destination_time=None [, (int)transposition_amount=0]])
  -> IntU64Vector :'
cpp_signature: std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object
  [,boost::python::api::object=None [,int=0]])
args:
- name: note_ids
  type: object
- name: destination_time
  type: object | None
  optional: true
  default: None
- name: transposition_amount
  type: int
  optional: true
  default: '0'
returns:
  type: Live.Base.IntU64Vector
raw_doc: |-
  Duplicate all notes matching the given note IDs.
  If the optional destination_time is not provided, new notes will be inserted
  after the last selected note. This behavior can be observed when duplicating
  notes in the Live GUI.
  If the transposition_amount is specified, the notes in the region will be
  transposed by the number of semitones.
  Raises an error on audio clips.
```

##### duplicate_region

```yaml
kind: method
signature: 'duplicate_region( (Clip)self, (float)region_start, (float)region_length, (float)destination_time [, (int)pitch=-1
  [, (int)transposition_amount=0]]) -> None :'
cpp_signature: void duplicate_region(TPyHandle<AClip>,double,double,double [,int=-1 [,int=0]])
args:
- name: region_start
  type: float
- name: region_length
  type: float
- name: destination_time
  type: float
- name: pitch
  type: int
  optional: true
  default: '-1'
- name: transposition_amount
  type: int
  optional: true
  default: '0'
returns:
  type: None
raw_doc: |-
  Duplicate the notes in the specified region to the destination_time.
  Only notes of the specified pitch are duplicated or all if pitch is -1.
  If the transposition_amount is not 0, the notes in the region will
  be transposed by the transpose_amount of semitones.Raises an error on audio clips.
```

##### fire

```yaml
kind: method
signature: 'fire( (Clip)arg1) -> None :'
cpp_signature: void fire(TPyHandle<AClip>)
returns:
  type: None
raw_doc: (Re)Start playing this Clip.
```

##### get_all_notes_extended

```yaml
kind: method
signature: 'get_all_notes_extended( (Clip)arg1) -> MidiNoteVector :'
cpp_signature: std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_all_notes_extended(TPyHandle<AClip>)
returns:
  type: Live.Clip.MidiNoteVector
raw_doc: |-
  Returns a list of all MIDI notes from the clip, regardless of their position
  relative to the start and end markers/loop start and loop end.
  Each note is represented by a Live.Clip.MidiNote object.
  The returned list can be modified freely, but modifications will not
  be reflected in the MIDI clip until apply_note_modifications is called.
```

##### get_notes

```yaml
kind: method
signature: 'get_notes( (Clip)self, (float)from_time, (int)from_pitch, (float)time_span, (int)pitch_span) -> tuple :'
cpp_signature: boost::python::tuple get_notes(TPyHandle<AClip>,double,int,double,int)
args:
- name: from_time
  type: float
- name: from_pitch
  type: int
- name: time_span
  type: float
- name: pitch_span
  type: int
returns:
  type: tuple
raw_doc: |-
  Returns a tuple of tuples where each inner tuple represents
  a note starting in the given pitch- and time range.
  The inner tuple contains pitch, time, duration, velocity, and mute state.
```

##### get_notes_by_id

```yaml
kind: method
signature: 'get_notes_by_id( (Clip)arg1, (object)note_ids) -> MidiNoteVector :'
cpp_signature: std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
args:
- name: note_ids
  type: object
returns:
  type: Live.Clip.MidiNoteVector
raw_doc: Return a list of MIDI notes matching the given note IDs.
```

##### get_notes_extended

```yaml
kind: method
signature: 'get_notes_extended( (Clip)arg1, (int)from_pitch, (int)pitch_span, (float)from_time, (float)time_span) -> MidiNoteVector
  :'
cpp_signature: std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_extended(TPyHandle<AClip>,int,int,double,double)
args:
- name: from_pitch
  type: int
- name: pitch_span
  type: int
- name: from_time
  type: float
- name: time_span
  type: float
returns:
  type: Live.Clip.MidiNoteVector
raw_doc: |-
  Returns a list of MIDI notes from the given pitch and time range.
  Each note is represented by a Live.Clip.MidiNote object.
  The returned list can be modified freely, but modifications will not
  be reflected in the MIDI clip until apply_note_modifications is called.
```

##### get_selected_notes

```yaml
kind: method
signature: 'get_selected_notes( (Clip)arg1) -> tuple :'
cpp_signature: boost::python::tuple get_selected_notes(TPyHandle<AClip>)
returns:
  type: tuple
raw_doc: |-
  Returns a tuple of tuples where each inner tuple
  represents a selected note. The inner tuple contains
  pitch, time, duration, velocity, and mute state.
```

##### get_selected_notes_extended

```yaml
kind: method
signature: 'get_selected_notes_extended( (Clip)arg1) -> MidiNoteVector :'
cpp_signature: std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_selected_notes_extended(TPyHandle<AClip>)
returns:
  type: Live.Clip.MidiNoteVector
raw_doc: |-
  Returns a list of all MIDI notes from the clip that are currently selected.
  Each note is represented by a Live.Clip.MidiNote object.
  The returned list can be modified freely, but modifications will not
  be reflected in the MIDI clip until apply_note_modifications is called.
```

##### move_playing_pos

```yaml
kind: method
signature: 'move_playing_pos( (Clip)arg1, (float)arg2) -> None :'
cpp_signature: void move_playing_pos(TPyHandle<AClip>,double)
args:
- name: arg2
  type: float
returns:
  type: None
raw_doc: |-
  Jump forward or backward by the specified relative amount in beats.
  Will do nothing, if the Clip is not playing.
```

##### move_warp_marker

```yaml
kind: method
signature: 'move_warp_marker( (Clip)self, (float)marker_beat_time, (float)beat_time_distance) -> None :'
cpp_signature: void move_warp_marker(TPyHandle<AClip>,double,double)
args:
- name: marker_beat_time
  type: float
- name: beat_time_distance
  type: float
returns:
  type: None
raw_doc: |-
  Available for AudioClips only.
  Moves the specified warp marker by the specified beat time amount, if possible.
```

##### note_number_to_name

```yaml
kind: method
signature: 'note_number_to_name( (Clip)self, (int)midi_pitch) -> str :'
cpp_signature: TString note_number_to_name(TPyHandle<AClip>,int)
args:
- name: midi_pitch
  type: int
returns:
  type: str
raw_doc: |-
  Return a human-readable name for the given MIDI note number.
  Takes into account the scale and tonal spelling settings of the clip,
  as well as the current tuning system (if any)
```

##### quantize

```yaml
kind: method
signature: 'quantize( (Clip)arg1, (int)arg2, (float)arg3) -> None :'
cpp_signature: void quantize(TPyHandle<AClip>,int,float)
args:
- name: arg2
  type: int
- name: arg3
  type: float
returns:
  type: None
raw_doc: Quantize all notes in a clip or align warp markers.
```

##### quantize_pitch

```yaml
kind: method
signature: 'quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :'
cpp_signature: void quantize_pitch(TPyHandle<AClip>,int,int,float)
args:
- name: arg2
  type: int
- name: arg3
  type: int
- name: arg4
  type: float
returns:
  type: None
raw_doc: Quantize all the notes of a given pitch. Raises an error on audio clips.
```

##### remove_notes

```yaml
kind: method
signature: 'remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :'
cpp_signature: void remove_notes(TPyHandle<AClip>,double,int,double,int)
args:
- name: arg2
  type: float
- name: arg3
  type: int
- name: arg4
  type: float
- name: arg5
  type: int
returns:
  type: None
raw_doc: Delete all notes starting in the given pitch- and time range.
```

##### remove_notes_by_id

```yaml
kind: method
signature: 'remove_notes_by_id( (Clip)arg1, (object)arg2) -> None :'
cpp_signature: void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
args:
- name: arg2
  type: object
returns:
  type: None
raw_doc: |-
  Delete all notes matching the given note IDs.
  This function should NOT be used to implement modification of existing notes
  (i.e. in combination with add_new_notes), as that leads to loss of per-note
  events. apply_note_modifications must be used instead for modifying existing
  notes.
```

##### remove_notes_extended

```yaml
kind: method
signature: 'remove_notes_extended( (Clip)arg1, (int)from_pitch, (int)pitch_span, (float)from_time, (float)time_span) -> None
  :'
cpp_signature: void remove_notes_extended(TPyHandle<AClip>,int,int,double,double)
args:
- name: from_pitch
  type: int
- name: pitch_span
  type: int
- name: from_time
  type: float
- name: time_span
  type: float
returns:
  type: None
raw_doc: |-
  Delete all notes starting in the given pitch and time range.
  This function should NOT be used to implement modification of existing notes
  (i.e. in combination with add_new_notes), as that leads to loss of per-note
  events. apply_note_modifications must be used instead for modifying existing
  notes.
```

##### remove_warp_marker

```yaml
kind: method
signature: 'remove_warp_marker( (Clip)self, (float)beat_time) -> None :'
cpp_signature: void remove_warp_marker(TPyHandle<AClip>,double)
args:
- name: beat_time
  type: float
returns:
  type: None
raw_doc: |-
  Available for AudioClips only.
  Removes the specified warp marker, if possible.
```

##### replace_selected_notes

```yaml
kind: method
signature: 'replace_selected_notes( (Clip)arg1, (tuple)arg2) -> None :'
cpp_signature: void replace_selected_notes(TPyHandle<AClip>,boost::python::tuple)
args:
- name: arg2
  type: tuple
returns:
  type: None
raw_doc: |-
  Called with a tuple of tuples where each inner tuple represents
  a note in the same format as returned by get_selected_notes. The
  notes described that way will then be used to replace the old selection.
```

##### sample_to_beat_time

```yaml
kind: method
signature: 'sample_to_beat_time( (Clip)self, (float)sample_time) -> float :'
cpp_signature: double sample_to_beat_time(TPyHandle<AClip>,double)
args:
- name: sample_time
  type: float
returns:
  type: float
raw_doc: |-
  Available for AudioClips only.
  Converts the given sample time to beat time. Raises an error if the sample is not warped.
```

##### scrub

```yaml
kind: method
signature: 'scrub( (Clip)self, (float)scrub_position) -> None :'
cpp_signature: void scrub(TPyHandle<AClip>,double)
args:
- name: scrub_position
  type: float
returns:
  type: None
raw_doc: |-
  Scrubs inside a clip.
  scrub_position defines the position in beats that the scrub will start from.
  The scrub will continue until stop_scrub is called.
  Global quantization applies to the scrub's position and length.
```

##### seconds_to_sample_time

```yaml
kind: method
signature: 'seconds_to_sample_time( (Clip)self, (float)seconds) -> float :'
cpp_signature: double seconds_to_sample_time(TPyHandle<AClip>,double)
args:
- name: seconds
  type: float
returns:
  type: float
raw_doc: |-
  Available for AudioClips only.
  Converts the given seconds to sample time. Raises an error if the sample is warped.
```

##### select_all_notes

```yaml
kind: method
signature: 'select_all_notes( (Clip)arg1) -> None :'
cpp_signature: void select_all_notes(TPyHandle<AClip>)
returns:
  type: None
raw_doc: Selects all notes present in the clip.
```

##### select_notes_by_id

```yaml
kind: method
signature: 'select_notes_by_id( (Clip)arg1, (object)arg2) -> None :'
cpp_signature: void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
args:
- name: arg2
  type: object
returns:
  type: None
raw_doc: Selects all notes matching the given note IDs.
```

##### set_fire_button_state

```yaml
kind: method
signature: 'set_fire_button_state( (Clip)arg1, (bool)arg2) -> None :'
cpp_signature: void set_fire_button_state(TPyHandle<AClip>,bool)
args:
- name: arg2
  type: bool
returns:
  type: None
raw_doc: Set the clip's fire button state directly. Supports all launch modes.
```

##### set_notes

```yaml
kind: method
signature: 'set_notes( (Clip)arg1, (tuple)arg2) -> None :'
cpp_signature: void set_notes(TPyHandle<AClip>,boost::python::tuple)
args:
- name: arg2
  type: tuple
returns:
  type: None
raw_doc: |-
  Called with a tuple of tuples where each inner tuple represents
  a note in the same format as returned by get_notes. The
  notes described that way will then be added to the clip.
```

##### stop

```yaml
kind: method
signature: 'stop( (Clip)arg1) -> None :'
cpp_signature: void stop(TPyHandle<AClip>)
returns:
  type: None
raw_doc: Stop playing this Clip.
```

##### stop_scrub

```yaml
kind: method
signature: 'stop_scrub( (Clip)arg1) -> None :'
cpp_signature: void stop_scrub(TPyHandle<AClip>)
returns:
  type: None
raw_doc: Stops the current scrub.
```

### MidiNote

```yaml
kind: class
path: Live.Clip.MidiNote
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: An object representing a MIDI Note
```

#### Properties

##### duration

```yaml
kind: property
type: float
settable: true
```

##### mute

```yaml
kind: property
type: bool
settable: true
```

##### note_id

```yaml
kind: property
type: int
settable: false
raw_doc: |-
  A numerical ID that's unique within the originating clip of the note. Not to be
  used directly, but important for other API calls, namely apply_note_modifications.
```

##### pitch

```yaml
kind: property
type: int
settable: true
```

##### probability

```yaml
kind: property
type: float
settable: true
```

##### release_velocity

```yaml
kind: property
type: float
settable: true
```

##### start_time

```yaml
kind: property
type: float
settable: true
```

##### velocity

```yaml
kind: property
type: float
settable: true
```

##### velocity_deviation

```yaml
kind: property
type: float
settable: true
```

### MidiNoteSpecification

```yaml
kind: class
path: Live.Clip.MidiNoteSpecification
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (int)pitch, (float)start_time, (float)duration [, (float)velocity=100.0 [, (bool)mute=False [, (float)probability=1.0 [, (float)velocity_deviation=0.0 [, (float)release_velocity=64.0]]]]]) -> None :
      Create a new note specification. Only pitch, start_time and duration are
      mandatory. All other arguments will take on default values if not specified.

      C++ signature :
          void __init__(_object*,int,double,double [,float=100.0 [,bool=False [,float=1.0 [,float=0.0 [,float=64.0]]]]])
constructable: true
raw_doc: |-
  An object specifying the data for creating a MIDI note. To be used with the
  add_new_notes function.
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: pitch
  type: int
- name: start_time
  type: float
- name: duration
  type: float
- name: velocity
  type: float
  optional: true
  default: '100.0'
- name: mute
  type: bool
  optional: true
  default: 'False'
- name: probability
  type: float
  optional: true
  default: '1.0'
- name: velocity_deviation
  type: float
  optional: true
  default: '0.0'
- name: release_velocity
  type: float
  optional: true
  default: '64.0'
returns:
  type: None
```

### MidiNoteVector

```yaml
kind: class
path: Live.Clip.MidiNoteVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Clip.MidiNote
raw_doc: A container for holding MIDI notes from Live.
```

### WarpMarker

```yaml
kind: class
path: Live.Clip.WarpMarker
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (float)sample_time, (float)beat_time) -> None :
      Create a new warp marker specification.

      C++ signature :
          void __init__(_object*,double,double)
constructable: true
raw_doc: This class represents a WarpMarker type.
```

#### Properties

##### beat_time

```yaml
kind: property
type: float
settable: false
raw_doc: A WarpMarker's beat time.
```

##### sample_time

```yaml
kind: property
type: float
settable: false
raw_doc: A WarpMarker's sample time.
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: sample_time
  type: float
- name: beat_time
  type: float
returns:
  type: None
```

### WarpMarkerVector

```yaml
kind: class
path: Live.Clip.WarpMarkerVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Clip.WarpMarker
raw_doc: A container for returning warp markers from Live.
```

### View

```yaml
kind: class
path: Live.Clip.Clip.View
parent: Clip
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of a Clip.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Clip.Clip
settable: false
raw_doc: Get the canonical parent of the clip view.
```

##### grid_is_triplet

```yaml
kind: property
type: bool
settable: true
raw_doc: Get/set wether the grid is showing in triplet mode.
```

##### grid_quantization

```yaml
kind: property
type: Live.Clip.GridQuantization
settable: true
raw_doc: Get/set clip grid quantization resolution.
```

#### Methods

##### hide_envelope

```yaml
kind: method
signature: 'hide_envelope( (View)arg1) -> None :'
cpp_signature: void hide_envelope(TPyViewData<AClip>)
returns:
  type: None
raw_doc: Hide the envelope view.
```

##### select_envelope_parameter

```yaml
kind: method
signature: 'select_envelope_parameter( (View)arg1, (DeviceParameter)arg2) -> None :'
cpp_signature: void select_envelope_parameter(TPyViewData<AClip>,TPyHandle<ATimeableValue>)
args:
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: None
raw_doc: Select the given device parameter in the envelope view.
```

##### show_envelope

```yaml
kind: method
signature: 'show_envelope( (View)arg1) -> None :'
cpp_signature: void show_envelope(TPyViewData<AClip>)
returns:
  type: None
raw_doc: Show the envelope view.
```

##### show_loop

```yaml
kind: method
signature: 'show_loop( (View)arg1) -> None :'
cpp_signature: void show_loop(TPyViewData<AClip>)
returns:
  type: None
raw_doc: Show the entire loop in the detail view.
```

## Enums

### ClipLaunchQuantization

```yaml
kind: enum
members:
  q_global: 0
  q_none: 1
  q_8_bars: 2
  q_4_bars: 3
  q_2_bars: 4
  q_bar: 5
  q_half: 6
  q_half_triplet: 7
  q_quarter: 8
  q_quarter_triplet: 9
  q_eighth: 10
  q_eighth_triplet: 11
  q_sixteenth: 12
  q_sixteenth_triplet: 13
  q_thirtysecond: 14
```

### GridQuantization

```yaml
kind: enum
members:
  no_grid: 0
  g_8_bars: 1
  g_4_bars: 2
  g_2_bars: 3
  g_bar: 4
  g_half: 5
  g_quarter: 6
  g_eighth: 7
  g_sixteenth: 8
  g_thirtysecond: 9
  count: 10
```

### LaunchMode

```yaml
kind: enum
members:
  trigger: 0
  gate: 1
  toggle: 2
  repeat: 3
```

### WarpMode

```yaml
kind: enum
members:
  beats: 0
  complex: 4
  complex_pro: 6
  repitch: 3
  rex: 5
  texture: 2
  tones: 1
  count: 7
```

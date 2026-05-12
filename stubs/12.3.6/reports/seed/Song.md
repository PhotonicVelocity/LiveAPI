---
module: Song
---

## Classes

### Song

```yaml
kind: class
path: Live.Song.Song
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Live set.
```

#### Properties

##### appointed_device

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Read, write, and listen access to the appointed Device
```

##### arrangement_overdub

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set the global arrangement overdub state.
```

##### back_to_arranger

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set if triggering a Clip in the Session, disabled the playback of
  Clips in the Arranger.
```

##### can_capture_midi

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Get whether there currently is material to be captured on any tracks.
```

##### can_jump_to_next_cue

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Returns true when there is a cue marker right to the playing pos that
  we could jump to.
```

##### can_jump_to_prev_cue

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Returns true when there is a cue marker left to the playing pos that
  we could jump to.
```

##### can_redo

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if there is an undone action that we can redo.
```

##### can_undo

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if there is an action that we can restore.
```

##### canonical_parent

```yaml
kind: property
type: None
settable: false
raw_doc: Get the canonical parent of the song.
```

##### clip_trigger_quantization

```yaml
kind: property
type: Live.Song.Quantization
settable: true
listenable: true
raw_doc: |-
  Get/Set access to the quantization settings that are used to fire
  Clips in the Session.
```

##### count_in_duration

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: |-
  Get the count in duration. Returns an index, mapped as follows:
  0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
```

##### cue_points

```yaml
kind: property
type: Live.Base.Vector[Live.Song.CuePoint]
settable: false
listenable: true
raw_doc: Const access to a list of all cue points of the Live Song.
```

##### current_song_time

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set access to the songs current playing position in beats.
```

##### exclusive_arm

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Get if Tracks should be armed exclusively by default.
```

##### exclusive_solo

```yaml
kind: property
type: bool
settable: false
raw_doc: Get if Tracks should be soloed exclusively by default.
```

##### file_path

```yaml
kind: property
type: str
settable: false
raw_doc: Get the current Live Set's path on disk.
```

##### groove_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Get/Set the global groove amount, that adjust all setup grooves
  in all clips.
```

##### groove_pool

```yaml
kind: property
type: Live.GroovePool.GroovePool
settable: false
raw_doc: Get the groove pool.
```

##### is_ableton_link_enabled

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Enable/disable Ableton Link.
```

##### is_ableton_link_start_stop_sync_enabled

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Enable/disable Ableton Link Start Stop Sync.
```

##### is_counting_in

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Get whether currently counting in.
```

##### is_playing

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Returns true if the Song is currently playing.
```

##### last_event_time

```yaml
kind: property
type: float
settable: false
raw_doc: |-
  Return the time of the last set event in the song. In contrary to
  song_length, this will not add some extra beats that are mostly needed
  for Display purposes in the Arrangerview.
```

##### loop

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the looping flag that en/disables the usage of the global
  loop markers in the song.
```

##### loop_length

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the length of the global loop marker position in beats.
```

##### loop_start

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the start of the global loop marker position in beats.
```

##### master_track

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Access to the Main Track (always available)
```

##### metronome

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set if the metronom is audible.
```

##### midi_recording_quantization

```yaml
kind: property
type: Live.Song.RecordingQuantization
settable: true
listenable: true
raw_doc: |-
  Get/Set access to the settings that are used to quantize
  MIDI recordings.
```

##### name

```yaml
kind: property
type: str
settable: false
raw_doc: Get the current Live Set's name.
```

##### nudge_down

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set the status of the nudge down button.
```

##### nudge_up

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set the status of the nudge up button.
```

##### overdub

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Legacy hook for Live 8 overdub state. Now hooks to
  session record, but never starts playback.
```

##### punch_in

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the flag that will enable recording as soon as the Song plays
  and hits the global loop start region.
```

##### punch_out

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the flag that will disable recording as soon as the Song plays
  and hits the global loop end region.
```

##### re_enable_automation_enabled

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if some automated parameter has been overriden
```

##### record_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set the state of the global recording flag.
```

##### return_tracks

```yaml
kind: property
type: Live.Base.Vector[Live.Track.Track]
settable: false
listenable: true
raw_doc: Const access to the list of available Return Tracks.
```

##### root_note

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Set and access the root (i.e. key) of the song. The root can be a number between 0 and 11, with 0 corresponding to
  C and 11 corresponding to B.
```

##### scale_intervals

```yaml
kind: property
type: Live.Base.IntVector
settable: false
listenable: true
raw_doc: Reports the current scale's intervals as a list of integers, starting with the root and representing the number of
  halfsteps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)
```

##### scale_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Access to the Scale Mode setting in Live. When on, key tracks that belong to the currently selected scale are highlighted
  in Live's MIDI Note Editor, and pitch-based parameters in MIDI Tools and Devices can be edited in scale degrees rather than
  semitones.
```

##### scale_name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: |-
  Set and access the currently selected scale by name. The default scale names that can be saved with a set and recalled are
  'Major', 'Minor', 'Dorian', 'Mixolydian' ,'Lydian' ,'Phrygian' ,'Locrian',
  'Whole Tone', 'Half-whole Dim.', 'Whole-half Dim.', 'Minor Blues',
  'Minor Pentatonic', 'Major Pentatonic', 'Harmonic Minor', 'Harmonic Major',
  'Dorian #4', 'Phrygian Dominant', 'Melodic Minor', 'Lydian Augmented',
  'Lydian Dominant', 'Super Locrian', 'Bhairav', 'Hungarian Minor',
  '8-Tone Spanish', 'Hirajoshi', 'In-Sen', 'Iwato', 'Kumoi', 'Pelog Selisir',
  'Pelog Tembung', 'Messiaen 3', 'Messiaen 4', 'Messiaen 5', 'Messiaen 6',
  'Messiaen 7'
```

##### scenes

```yaml
kind: property
type: Live.Base.Vector[Live.Scene.Scene]
settable: false
listenable: true
raw_doc: Const access to a list of all Scenes in the Live Song.
```

##### select_on_launch

```yaml
kind: property
type: bool
settable: false
raw_doc: Get if Scenes and Clips should be selected when fired.
```

##### session_automation_record

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Returns true if automation recording is enabled.
```

##### session_record

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set the session record state.
```

##### session_record_status

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Get the session slot-recording state.
```

##### signature_denominator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the global signature denominator of the Song.
```

##### signature_numerator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the global signature numerator of the Song.
```

##### song_length

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Return the time of the last set event in the song, plus som extra beats
  that are usually added for better navigation in the arrangerview.
```

##### start_time

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Get/Set access to the songs current start time in beats. The set time
  may be overridden by the current loop/locator start time.
```

##### swing_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set access to the amount of swing that is applied when adding or quantizing notes to MIDI clips
```

##### tempo

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Get/Set the global project tempo.
```

##### tempo_follower_enabled

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set whether the Tempo Follower is controlling the tempo. The Tempo Follower Toggle must be made visible in the
  preferences for this property to be effective.
```

##### tracks

```yaml
kind: property
type: Live.Base.Vector[Live.Track.Track]
settable: false
listenable: true
raw_doc: |-
  Const access to a list of all Player Tracks in the Live Song, excluding
  the return and Main Track (see also Song.send_tracks and Song.master_track).
  At least one MIDI or Audio Track is always available.
```

##### tuning_system

```yaml
kind: property
type: Live.TuningSystem.TuningSystem
settable: false
listenable: true
raw_doc: Access the currently active tuning system.
```

##### view

```yaml
kind: property
type: Live.Song.Song.View
settable: false
raw_doc: |-
  Representing the view aspects of a Live document:
  The Session and Arrangerview.
```

##### visible_tracks

```yaml
kind: property
type: Live.Base.Vector[Live.Track.Track]
settable: false
listenable: true
raw_doc: |-
  Const access to a list of all visible Player Tracks in the Live Song, excluding
  the return and Main Track (see also Song.send_tracks and Song.master_track).
  At least one MIDI or Audio Track is always available.
```

##### data

```yaml
kind: property
listenable: true
```

##### scale_information

```yaml
kind: property
listenable: true
```

#### Methods

##### begin_undo_step

```yaml
kind: method
signature: 'begin_undo_step( (Song)arg1) -> None :'
cpp_signature: void begin_undo_step(TPyHandle<ASong>)
returns:
  type: None
```

##### capture_and_insert_scene

```yaml
kind: method
signature: 'capture_and_insert_scene( (Song)arg1 [, (int)CaptureMode=Song.CaptureMode.all]) -> None :'
cpp_signature: void capture_and_insert_scene(TPyHandle<ASong> [,int=Song.CaptureMode.all])
args:
- name: capture_mode
  type: Live.Song.CaptureMode | int
  optional: true
  default: Song.CaptureMode.all
returns:
  type: None
raw_doc: |-
  Capture currently playing clips and insert them as a new scene after
  the selected scene. Raises a runtime error if creating a new scene would exceed the limitations.
```

##### capture_midi

```yaml
kind: method
signature: 'capture_midi( (Song)arg1 [, (int)Destination=Song.CaptureDestination.auto]) -> None :'
cpp_signature: void capture_midi(TPyHandle<ASong> [,int=Song.CaptureDestination.auto])
args:
- name: destination
  type: Live.Song.CaptureDestination | int
  optional: true
  default: Song.CaptureDestination.auto
returns:
  type: None
raw_doc: |-
  Capture recently played MIDI material from audible tracks.
  If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible.
  If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively.
  Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations.
```

##### continue_playing

```yaml
kind: method
signature: 'continue_playing( (Song)arg1) -> None :'
cpp_signature: void continue_playing(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Continue playing the song from the current position
```

##### create_audio_track

```yaml
kind: method
signature: 'create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :'
cpp_signature: TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])
args:
- name: index
  type: object | None
  optional: true
  default: None
returns:
  type: Live.Track.Track
raw_doc: |-
  Create a new audio track at the optional given index and return it.If the index is -1,
  the new track is added at the end. It will create a default audio track if possible.
  If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
```

##### create_midi_track

```yaml
kind: method
signature: 'create_midi_track( (Song)arg1 [, (object)Index=None]) -> Track :'
cpp_signature: TWeakPtr<TTrackPyHandle> create_midi_track(TPyHandle<ASong> [,boost::python::api::object=None])
args:
- name: index
  type: object | None
  optional: true
  default: None
returns:
  type: Live.Track.Track
raw_doc: |-
  Create a new midi track at the optional given index and return it.If the index is -1,
  the new track is added at the end.It will create a default midi track if possible.
  If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
```

##### create_return_track

```yaml
kind: method
signature: 'create_return_track( (Song)arg1) -> Track :'
cpp_signature: TWeakPtr<TTrackPyHandle> create_return_track(TPyHandle<ASong>)
returns:
  type: Live.Track.Track
raw_doc: |-
  Create a new return track at the end and return it. If the new track would exceed
  the limitations, a limitation error is raised.
  If the maximum number of return tracks is exceeded, a RuntimeError is raised.
```

##### create_scene

```yaml
kind: method
signature: 'create_scene( (Song)arg1, (int)arg2) -> Scene :'
cpp_signature: TWeakPtr<TPyHandle<AScene>> create_scene(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: Live.Scene.Scene
raw_doc: |-
  Create a new scene at the given index. If the index is -1,
  the new scene is added at the end. If the index is invalid or
  the new scene would exceed the limitations, a limitation error is raised.
```

##### delete_return_track

```yaml
kind: method
signature: 'delete_return_track( (Song)arg1, (int)arg2) -> None :'
cpp_signature: void delete_return_track(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: |-
  Delete the return track with the given index. If no track with this index
  exists, an exception will be raised.
```

##### delete_scene

```yaml
kind: method
signature: 'delete_scene( (Song)arg1, (int)arg2) -> None :'
cpp_signature: void delete_scene(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: |-
  Delete the scene with the given index. If no scene with this index
  exists, an exception will be raised.
```

##### delete_track

```yaml
kind: method
signature: 'delete_track( (Song)arg1, (int)arg2) -> None :'
cpp_signature: void delete_track(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: |-
  Delete the track with the given index. If no track with this index
  exists, an exception will be raised.
```

##### duplicate_scene

```yaml
kind: method
signature: 'duplicate_scene( (Song)arg1, (int)arg2) -> None :'
cpp_signature: void duplicate_scene(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: |-
  Duplicates a scene and selects the new one.
  Raises a limitation error if creating a new scene would exceed the limitations.
```

##### duplicate_track

```yaml
kind: method
signature: 'duplicate_track( (Song)arg1, (int)arg2) -> None :'
cpp_signature: void duplicate_track(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: |-
  Duplicates a track and selects the new one.
  If the track is inside a folded group track, the group track is unfolded.
  Raises a limitation error if creating a new track would exceed the limitations.
```

##### end_undo_step

```yaml
kind: method
signature: 'end_undo_step( (Song)arg1) -> None :'
cpp_signature: void end_undo_step(TPyHandle<ASong>)
returns:
  type: None
```

##### find_device_position

```yaml
kind: method
signature: 'find_device_position( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :'
cpp_signature: int find_device_position(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)
args:
- name: device
  type: Live.Device.Device
- name: target
  type: Live.LomObject.LomObject
- name: target_position
  type: int
returns:
  type: int
raw_doc: |-
  Returns the closest possible position to the given target, where the
  device can be inserted. If inserting is not possible at all (i.e. if
  the device type is wrong), -1 is returned.
```

##### force_link_beat_time

```yaml
kind: method
signature: 'force_link_beat_time( (Song)arg1) -> None :'
cpp_signature: void force_link_beat_time(TPyHandle<ASong>)
returns:
  type: None
raw_doc: |-
  Force the Link timeline to jump to Lives current beat time.
  Danger: This can cause beat time discontinuities in other connected apps.
```

##### get_beats_loop_length

```yaml
kind: method
signature: 'get_beats_loop_length( (Song)arg1) -> BeatTime :'
cpp_signature: NSongApi::TBeatTime get_beats_loop_length(TPyHandle<ASong>)
returns:
  type: Live.Song.BeatTime
raw_doc: |-
  Get const access to the songs loop length, using a
  BeatTime class with the current global set signature.
```

##### get_beats_loop_start

```yaml
kind: method
signature: 'get_beats_loop_start( (Song)arg1) -> BeatTime :'
cpp_signature: NSongApi::TBeatTime get_beats_loop_start(TPyHandle<ASong>)
returns:
  type: Live.Song.BeatTime
raw_doc: |-
  Get const access to the songs loop start, using a
  BeatTime class with the current global set signature.
```

##### get_current_beats_song_time

```yaml
kind: method
signature: 'get_current_beats_song_time( (Song)arg1) -> BeatTime :'
cpp_signature: NSongApi::TBeatTime get_current_beats_song_time(TPyHandle<ASong>)
returns:
  type: Live.Song.BeatTime
raw_doc: |-
  Get const access to the songs current playing position, using a
  BeatTime class with the current global set signature.
```

##### get_current_smpte_song_time

```yaml
kind: method
signature: 'get_current_smpte_song_time( (Song)arg1, (int)arg2) -> SmptTime :'
cpp_signature: NSongApi::TSmptTime get_current_smpte_song_time(TPyHandle<ASong>,int)
args:
- name: arg2
  type: int
returns:
  type: Live.Song.SmptTime
raw_doc: |-
  Get const access to the songs current playing position, by specifying
  the SMPTE format in which you would like to receive the time.
```

##### get_data

```yaml
kind: method
signature: 'get_data( (Song)arg1, (object)key, (object)default_value) -> object :'
cpp_signature: boost::python::api::object get_data(TPyHandle<ASong>,TString,boost::python::api::object)
args:
- name: key
  type: str
- name: default_value
  type: object
returns:
  type: object
raw_doc: Get data for the given key, that was previously stored using set_data.
```

##### is_cue_point_selected

```yaml
kind: method
signature: 'is_cue_point_selected( (Song)arg1) -> bool :'
cpp_signature: bool is_cue_point_selected(TPyHandle<ASong>)
returns:
  type: bool
raw_doc: Return true if the global playing pos is currently on a cue point.
```

##### jump_by

```yaml
kind: method
signature: 'jump_by( (Song)arg1, (float)arg2) -> None :'
cpp_signature: void jump_by(TPyHandle<ASong>,double)
args:
- name: arg2
  type: float
returns:
  type: None
raw_doc: Set a new playing pos, relative to the current one.
```

##### jump_to_next_cue

```yaml
kind: method
signature: 'jump_to_next_cue( (Song)arg1) -> None :'
cpp_signature: void jump_to_next_cue(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Jump to the next cue (marker) if possible.
```

##### jump_to_prev_cue

```yaml
kind: method
signature: 'jump_to_prev_cue( (Song)arg1) -> None :'
cpp_signature: void jump_to_prev_cue(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Jump to the prior cue (marker) if possible.
```

##### move_device

```yaml
kind: method
signature: 'move_device( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :'
cpp_signature: int move_device(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)
args:
- name: device
  type: Live.Device.Device
- name: target
  type: Live.LomObject.LomObject
- name: target_position
  type: int
returns:
  type: int
raw_doc: Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves
  it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen.
  If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.
```

##### play_selection

```yaml
kind: method
signature: 'play_selection( (Song)arg1) -> None :'
cpp_signature: void play_selection(TPyHandle<ASong>)
returns:
  type: None
raw_doc: |-
  Start playing the current set selection, or do nothing if
  no selection is set.
```

##### re_enable_automation

```yaml
kind: method
signature: 're_enable_automation( (Song)arg1) -> None :'
cpp_signature: void re_enable_automation(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Discards overrides of automated parameters.
```

##### redo

```yaml
kind: method
signature: 'redo( (Song)arg1) -> str :'
cpp_signature: TString redo(TPyHandle<ASong>)
returns:
  type: str
raw_doc: Redo the last action that was undone.
```

##### scrub_by

```yaml
kind: method
signature: 'scrub_by( (Song)arg1, (float)arg2) -> None :'
cpp_signature: void scrub_by(TPyHandle<ASong>,double)
args:
- name: arg2
  type: float
returns:
  type: None
raw_doc: Same as jump_by, but does not stop playback.
```

##### set_data

```yaml
kind: method
signature: 'set_data( (Song)arg1, (object)key, (object)value) -> None :'
cpp_signature: void set_data(TPyHandle<ASong>,TString,boost::python::api::object)
args:
- name: key
  type: str
- name: value
  type: object
returns:
  type: None
raw_doc: Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
```

##### set_or_delete_cue

```yaml
kind: method
signature: 'set_or_delete_cue( (Song)arg1) -> None :'
cpp_signature: void set_or_delete_cue(TPyHandle<ASong>)
returns:
  type: None
raw_doc: |-
  When a cue is selected, it gets deleted. If no cue is selected,
  a new cue is created at the current global songtime.
```

##### start_playing

```yaml
kind: method
signature: 'start_playing( (Song)arg1) -> None :'
cpp_signature: void start_playing(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Start playing from the startmarker
```

##### stop_all_clips

```yaml
kind: method
signature: 'stop_all_clips( (Song)arg1 [, (bool)Quantized=True]) -> None :'
cpp_signature: void stop_all_clips(TPyHandle<ASong> [,bool=True])
args:
- name: quantized
  type: bool
  optional: true
  default: 'True'
returns:
  type: None
raw_doc: Stop all playing Clips (if any) but continue playing the Song.
```

##### stop_playing

```yaml
kind: method
signature: 'stop_playing( (Song)arg1) -> None :'
cpp_signature: void stop_playing(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Stop playing the Song.
```

##### tap_tempo

```yaml
kind: method
signature: 'tap_tempo( (Song)arg1) -> None :'
cpp_signature: void tap_tempo(TPyHandle<ASong>)
returns:
  type: None
raw_doc: Trigger the tap tempo function.
```

##### trigger_session_record

```yaml
kind: method
signature: 'trigger_session_record( (Song)self [, (float)record_length=1.7976931348623157e+308]) -> None :'
cpp_signature: void trigger_session_record(TPyHandle<ASong> [,double=1.7976931348623157e+308])
args:
- name: record_length
  type: float
  optional: true
  default: '1.7976931348623157e+308'
returns:
  type: None
raw_doc: Triggers a new session recording.
```

##### undo

```yaml
kind: method
signature: 'undo( (Song)arg1) -> str :'
cpp_signature: TString undo(TPyHandle<ASong>)
returns:
  type: str
raw_doc: Undo the last action that was made.
```

### BeatTime

```yaml
kind: class
path: Live.Song.BeatTime
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.
```

#### Properties

##### bars

```yaml
kind: property
type: int
settable: true
```

##### beats

```yaml
kind: property
type: int
settable: true
```

##### sub_division

```yaml
kind: property
type: int
settable: true
```

##### ticks

```yaml
kind: property
type: int
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

### CuePoint

```yaml
kind: class
path: Live.Song.CuePoint
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Represents a 'Marker' in the arrangement.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the cue point.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Get/Set/Listen to the name of this CuePoint, as visible in the arranger.
```

##### time

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Get/Listen to the CuePoint's time in beats.
```

#### Methods

##### jump

```yaml
kind: method
signature: 'jump( (CuePoint)arg1) -> None :'
cpp_signature: void jump(TPyHandle<ACuePoint>)
returns:
  type: None
raw_doc: |-
  When the Song is playing, set the playing-position quantized to
  this Cuepoint's time. When not playing, simply move the start
  playing position.
```

### SmptTime

```yaml
kind: class
path: Live.Song.SmptTime
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: |-
  Represents a Time, split into Hours, Minutes, Seconds and Frames.
  The frame type must be specified when calling a function that returns
  a SmptTime.
```

#### Properties

##### frames

```yaml
kind: property
type: int
settable: true
```

##### hours

```yaml
kind: property
type: int
settable: true
```

##### minutes

```yaml
kind: property
type: int
settable: true
```

##### seconds

```yaml
kind: property
type: int
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

### View

```yaml
kind: class
path: Live.Song.Song.View
parent: Song
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: 'Representing the view aspects of a Live document: The Session and Arrangerview.'
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the song view.
```

##### detail_clip

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Get/Set the Clip that is currently visible in Lives Detailview.
```

##### draw_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set if the Envelope/Note draw mode is enabled.
```

##### follow_song

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set if the Arrangerview should scroll to show the playmarker.
```

##### highlighted_clip_slot

```yaml
kind: property
type: Live.ClipSlot.ClipSlot
settable: true
raw_doc: Get/Set the clip slot, defined via the selected track and scene in the Session.Will be None for Main- and Sendtracks.
```

##### selected_chain

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Get the highlighted chain if available.
```

##### selected_parameter

```yaml
kind: property
type: None
settable: false
listenable: true
raw_doc: Get the currently selected device parameter.
```

##### selected_scene

```yaml
kind: property
type: Live.Scene.Scene
settable: true
listenable: true
raw_doc: Get/Set the current selected scene in Lives Sessionview.
```

##### selected_track

```yaml
kind: property
type: Live.Track.Track
settable: true
listenable: true
raw_doc: Get/Set the current selected Track in Lives Session or Arrangerview.
```

#### Methods

##### select_device

```yaml
kind: method
signature: 'select_device( (View)arg1, (Device)arg2 [, (bool)ShouldAppointDevice=True]) -> None :'
cpp_signature: void select_device(TPyViewData<ASong>,TPyHandle<ADevice> [,bool=True])
args:
- name: arg2
  type: Live.Device.Device
- name: should_appoint_device
  type: bool
  optional: true
  default: 'True'
returns:
  type: None
raw_doc: Select the given device.
```

## Enums

### CaptureDestination

```yaml
kind: enum
members:
  auto: 0
  session: 1
  arrangement: 2
raw_doc: The destination for MIDI capture.
```

### CaptureMode

```yaml
kind: enum
members:
  all: 0
  all_except_selected: 1
raw_doc: The capture mode that is used for capture and insert scene.
```

### Quantization

```yaml
kind: enum
members:
  q_no_q: 0
  q_8_bars: 1
  q_4_bars: 2
  q_2_bars: 3
  q_bar: 4
  q_half: 5
  q_half_triplet: 6
  q_quarter: 7
  q_quarter_triplet: 8
  q_eight: 9
  q_eight_triplet: 10
  q_sixtenth: 11
  q_sixtenth_triplet: 12
  q_thirtytwoth: 13
```

### RecordingQuantization

```yaml
kind: enum
members:
  rec_q_no_q: 0
  rec_q_quarter: 1
  rec_q_eight: 2
  rec_q_eight_triplet: 3
  rec_q_eight_eight_triplet: 4
  rec_q_sixtenth: 5
  rec_q_sixtenth_triplet: 6
  rec_q_sixtenth_sixtenth_triplet: 7
  rec_q_thirtysecond: 8
```

### SessionRecordStatus

```yaml
kind: enum
members:
  'off': 0
  transition: 2
  'on': 1
```

### TimeFormat

```yaml
kind: enum
members:
  ms_time: 0
  smpte_24: 1
  smpte_25: 2
  smpte_30: 3
  smpte_30_drop: 4
  smpte_29: 5
```

## Functions

### get_all_scales_ordered

```yaml
kind: function
signature: 'get_all_scales_ordered() -> tuple :'
cpp_signature: boost::python::tuple get_all_scales_ordered()
returns:
  type: tuple[tuple, ...]
raw_doc: Get an ordered tuple of tuples of all available scale names to intervals.
```

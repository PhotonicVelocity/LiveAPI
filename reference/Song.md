# Song

> `Live.Song.Song`

This class represents a Live set.

## View

> `Live.Song.Song.View`

Representing the view aspects of a Live document: The Session and Arrangerview.

### Properties

| Property                | Type       | Settable | Listenable | Description                                                                      |
| ----------------------- | ---------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `canonical_parent`      | `Song`     | `no`     | `no`       | Get the canonical parent of the song view.                                       |
| `detail_clip`           | `Clip`     | `yes`    | `yes`      | Get/Set the Clip that is currently visible in Lives Detailview.                  |
| `draw_mode`             | `bool`     | `yes`    | `yes`      | Get/Set if the Envelope/Note draw mode is enabled.                               |
| `follow_song`           | `bool`     | `yes`    | `yes`      | Get/Set if the Arrangerview should scroll to show the playmarker.                |
| `highlighted_clip_slot` | `ClipSlot` | `yes`    | `no`       | Get/Set the clip slot, defined via the selected track and scene in the Sessio... |
| `selected_chain`        | `None`     | `yes`    | `yes`      | Get the highlighted chain if available.                                          |
| `selected_parameter`    | `None`     | `no`     | `yes`      | Get the currently selected device parameter.                                     |
| `selected_scene`        | `Scene`    | `yes`    | `yes`      | Get/Set the current selected scene in Lives Sessionview.                         |
| `selected_track`        | `Track`    | `yes`    | `yes`      | Get/Set the current selected Track in Lives Session or Arrangerview.             |

#### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the song view.

#### `detail_clip`

- **Type:** `Clip`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the Clip that is currently visible in Lives Detailview.

#### `draw_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set if the Envelope/Note draw mode is enabled.

#### `follow_song`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set if the Arrangerview should scroll to show the playmarker.

#### `highlighted_clip_slot`

- **Type:** `ClipSlot`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set the clip slot, defined via the selected track and scene in the Session.Will be None for Main- and Sendtracks.

#### `selected_chain`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Get the highlighted chain if available.

#### `selected_parameter`

- **Type:** `None`
- **Settable:** `no`
- **Listenable:** `yes`

Get the currently selected device parameter.

#### `selected_scene`

- **Type:** `Scene`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current selected scene in Lives Sessionview.

#### `selected_track`

- **Type:** `Track`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current selected Track in Lives Session or Arrangerview.

### Methods

| Method                                                            | Returns | Description              |
| ----------------------------------------------------------------- | ------- | ------------------------ |
| `select_device(device: Device, ShouldAppointDevice: bool = True)` | `None`  | Select the given device. |

#### `select_device(device: Device, ShouldAppointDevice: bool = True)`

- **Returns:** `None`
- **Args:**
  - `device: Device`
  - `ShouldAppointDevice: bool = True`

Select the given device.

## Properties

| Property                                  | Type                    | Settable | Listenable | Description                                                                      |
| ----------------------------------------- | ----------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `appointed_device`                        | `None`                  | `yes`    | `yes`      | Read, write, and listen access to the appointed Device.                          |
| `arrangement_overdub`                     | `bool`                  | `yes`    | `yes`      | Get/Set the global arrangement overdub state.                                    |
| `back_to_arranger`                        | `bool`                  | `yes`    | `yes`      | Get/Set if triggering a Clip in the Session, disabled the playback of Clips i... |
| `can_capture_midi`                        | `bool`                  | `no`     | `yes`      | Get whether there currently is material to be captured on any tracks.            |
| `can_jump_to_next_cue`                    | `bool`                  | `no`     | `yes`      | Returns true when there is a cue marker right to the playing pos that we coul... |
| `can_jump_to_prev_cue`                    | `bool`                  | `no`     | `yes`      | Returns true when there is a cue marker left to the playing pos that we could... |
| `can_redo`                                | `bool`                  | `no`     | `no`       | Returns true if there is an undone action that we can redo.                      |
| `can_undo`                                | `bool`                  | `no`     | `no`       | Returns true if there is an action that we can restore.                          |
| `canonical_parent`                        | `None`                  | `no`     | `no`       | Get the canonical parent of the song.                                            |
| `clip_trigger_quantization`               | `Quantization`          | `yes`    | `yes`      | Get/Set access to the quantization settings that are used to fire Clips in th... |
| `count_in_duration`                       | `int`                   | `no`     | `yes`      | Get the count in duration.                                                       |
| `cue_points`                              | `tuple`                 | `no`     | `yes`      | Const access to a list of all cue points of the Live Song.                       |
| `current_song_time`                       | `float`                 | `yes`    | `yes`      | Get/Set access to the songs current playing position in beats.                   |
| `exclusive_arm`                           | `bool`                  | `no`     | `yes`      | Get if Tracks should be armed exclusively by default.                            |
| `exclusive_solo`                          | `bool`                  | `no`     | `no`       | Get if Tracks should be soloed exclusively by default.                           |
| `file_path`                               | `str`                   | `no`     | `no`       | Get the current Live Set's path on disk.                                         |
| `groove_amount`                           | `float`                 | `yes`    | `yes`      | Get/Set the global groove amount, that adjust all setup grooves in all clips.    |
| `groove_pool`                             | `GroovePool`            | `no`     | `no`       | Get the groove pool.                                                             |
| `is_ableton_link_enabled`                 | `bool`                  | `yes`    | `yes`      | Enable/disable Ableton Link.                                                     |
| `is_ableton_link_start_stop_sync_enabled` | `bool`                  | `yes`    | `yes`      | Enable/disable Ableton Link Start Stop Sync.                                     |
| `is_counting_in`                          | `bool`                  | `no`     | `yes`      | Get whether currently counting in.                                               |
| `is_playing`                              | `bool`                  | `yes`    | `yes`      | Returns true if the Song is currently playing.                                   |
| `last_event_time`                         | `float`                 | `no`     | `no`       | Return the time of the last set event in the song.                               |
| `loop`                                    | `bool`                  | `yes`    | `yes`      | Get/Set the looping flag that en/disables the usage of the global loop marker... |
| `loop_length`                             | `float`                 | `yes`    | `yes`      | Get/Set the length of the global loop marker position in beats.                  |
| `loop_start`                              | `float`                 | `yes`    | `yes`      | Get/Set the start of the global loop marker position in beats.                   |
| `master_track`                            | `Track`                 | `no`     | `no`       | Access to the Main Track (always available).                                     |
| `metronome`                               | `bool`                  | `yes`    | `yes`      | Get/Set if the metronom is audible.                                              |
| `midi_recording_quantization`             | `RecordingQuantization` | `yes`    | `yes`      | Get/Set access to the settings that are used to quantize MIDI recordings.        |
| `name`                                    | `str`                   | `no`     | `no`       | Get the current Live Set's name.                                                 |
| `nudge_down`                              | `bool`                  | `yes`    | `yes`      | Get/Set the status of the nudge down button.                                     |
| `nudge_up`                                | `bool`                  | `yes`    | `yes`      | Get/Set the status of the nudge up button.                                       |
| `overdub`                                 | `bool`                  | `yes`    | `yes`      | Legacy hook for Live 8 overdub state.                                            |
| `punch_in`                                | `bool`                  | `yes`    | `yes`      | Get/Set the flag that will enable recording as soon as the Song plays and hit... |
| `punch_out`                               | `bool`                  | `yes`    | `yes`      | Get/Set the flag that will disable recording as soon as the Song plays and hi... |
| `re_enable_automation_enabled`            | `bool`                  | `no`     | `yes`      | Returns true if some automated parameter has been overriden.                     |
| `record_mode`                             | `bool`                  | `yes`    | `yes`      | Get/Set the state of the global recording flag.                                  |
| `return_tracks`                           | `tuple`                 | `no`     | `yes`      | Const access to the list of available Return Tracks.                             |
| `root_note`                               | `int`                   | `yes`    | `yes`      | Set and access the root (i.e.                                                    |
| `scale_intervals`                         | `tuple[int, Ellipsis]`  | `no`     | `yes`      | Reports the current scale's intervals as a list of integers, starting with th... |
| `scale_mode`                              | `bool`                  | `yes`    | `yes`      | Access to the Scale Mode setting in Live.                                        |
| `scale_name`                              | `str`                   | `yes`    | `yes`      | Set and access the currently selected scale by name.                             |
| `scenes`                                  | `tuple`                 | `no`     | `yes`      | Const access to a list of all Scenes in the Live Song.                           |
| `select_on_launch`                        | `bool`                  | `no`     | `no`       | Get if Scenes and Clips should be selected when fired.                           |
| `session_automation_record`               | `bool`                  | `yes`    | `yes`      | Returns true if automation recording is enabled.                                 |
| `session_record`                          | `bool`                  | `yes`    | `yes`      | Get/Set the session record state.                                                |
| `session_record_status`                   | `int`                   | `no`     | `yes`      | Get the session slot-recording state.                                            |
| `signature_denominator`                   | `int`                   | `yes`    | `yes`      | Get/Set access to the global signature denominator of the Song.                  |
| `signature_numerator`                     | `int`                   | `yes`    | `yes`      | Get/Set access to the global signature numerator of the Song.                    |
| `song_length`                             | `float`                 | `no`     | `yes`      | Return the time of the last set event in the song, plus som extra beats that ... |
| `start_time`                              | `float`                 | `yes`    | `yes`      | Get/Set access to the songs current start time in beats.                         |
| `swing_amount`                            | `float`                 | `yes`    | `yes`      | Get/Set access to the amount of swing that is applied when adding or quantizi... |
| `tempo`                                   | `float`                 | `yes`    | `yes`      | Get/Set the global project tempo.                                                |
| `tempo_follower_enabled`                  | `bool`                  | `yes`    | `yes`      | Get/Set whether the Tempo Follower is controlling the tempo.                     |
| `tracks`                                  | `tuple`                 | `no`     | `yes`      | Const access to a list of all Player Tracks in the Live Song, excluding the r... |
| `tuning_system`                           | `TuningSystem`          | `no`     | `yes`      | Access the currently active tuning system.                                       |
| `view`                                    | `View`                  | `no`     | `no`       | Representing the view aspects of a Live document: The Session and Arrangerview.  |
| `visible_tracks`                          | `tuple`                 | `no`     | `yes`      | Const access to a list of all visible Player Tracks in the Live Song, excludi... |

### `appointed_device`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Read, write, and listen access to the appointed Device

### `arrangement_overdub`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the global arrangement overdub state.

### `back_to_arranger`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set if triggering a Clip in the Session, disabled the playback of Clips in the Arranger.

### `can_capture_midi`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Get whether there currently is material to be captured on any tracks.

### `can_jump_to_next_cue`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true when there is a cue marker right to the playing pos that we could jump to.

### `can_jump_to_prev_cue`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true when there is a cue marker left to the playing pos that we could jump to.

### `can_redo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if there is an undone action that we can redo.

### `can_undo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if there is an action that we can restore.

### `canonical_parent`

- **Type:** `None`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the song.

### `clip_trigger_quantization`

- **Type:** `Quantization`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the quantization settings that are used to fire Clips in the Session.

### `count_in_duration`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Get the count in duration. Returns an index, mapped as follows: 0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.

### `cue_points`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all cue points of the Live Song.

### `current_song_time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the songs current playing position in beats.

### `exclusive_arm`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Get if Tracks should be armed exclusively by default.

### `exclusive_solo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Get if Tracks should be soloed exclusively by default.

### `file_path`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Get the current Live Set's path on disk.

### `groove_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the global groove amount, that adjust all setup grooves in all clips.

### `groove_pool`

- **Type:** `GroovePool`
- **Settable:** `no`
- **Listenable:** `no`

Get the groove pool.

### `is_ableton_link_enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Enable/disable Ableton Link.

### `is_ableton_link_start_stop_sync_enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Enable/disable Ableton Link Start Stop Sync.

### `is_counting_in`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Get whether currently counting in.

### `is_playing`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Returns true if the Song is currently playing.

### `last_event_time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Return the time of the last set event in the song. In contrary to song_length, this will not add some extra beats that are mostly needed for Display purposes in the Arrangerview.

### `loop`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the looping flag that en/disables the usage of the global loop markers in the song.

### `loop_length`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the length of the global loop marker position in beats.

### `loop_start`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the start of the global loop marker position in beats.

### `master_track`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Access to the Main Track (always available)

### `metronome`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set if the metronom is audible.

### `midi_recording_quantization`

- **Type:** `RecordingQuantization`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the settings that are used to quantize MIDI recordings.

### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Get the current Live Set's name.

### `nudge_down`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the status of the nudge down button.

### `nudge_up`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the status of the nudge up button.

### `overdub`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Legacy hook for Live 8 overdub state. Now hooks to session record, but never starts playback.

### `punch_in`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the flag that will enable recording as soon as the Song plays and hits the global loop start region.

### `punch_out`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the flag that will disable recording as soon as the Song plays and hits the global loop end region.

### `re_enable_automation_enabled`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if some automated parameter has been overriden

### `record_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the state of the global recording flag.

### `return_tracks`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the list of available Return Tracks.

### `root_note`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Set and access the root (i.e. key) of the song. The root can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B.

### `scale_intervals`

- **Type:** `tuple[int, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Reports the current scale's intervals as a list of integers, starting with the root and representing the number of halfsteps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)

### `scale_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Scale Mode setting in Live. When on, key tracks that belong to the currently selected scale are highlighted in Live's MIDI Note Editor, and pitch-based parameters in MIDI Tools and Devices can be edited in scale degrees rather than semitones.

### `scale_name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Set and access the currently selected scale by name. The default scale names that can be saved with a set and recalled are 'Major', 'Minor', 'Dorian', 'Mixolydian' ,'Lydian' ,'Phrygian' ,'Locrian', 'Whole Tone', 'Half-whole Dim.', 'Whole-half Dim.', 'Minor Blues', 'Minor Pentatonic', 'Major Pentatonic', 'Harmonic Minor', 'Harmonic Major', 'Dorian #4', 'Phrygian Dominant', 'Melodic Minor', 'Lydian Augmented', 'Lydian Dominant', 'Super Locrian', 'Bhairav', 'Hungarian Minor', '8-Tone Spanish', 'Hirajoshi', 'In-Sen', 'Iwato', 'Kumoi', 'Pelog Selisir', 'Pelog Tembung', 'Messiaen 3', 'Messiaen 4', 'Messiaen 5', 'Messiaen 6', 'Messiaen 7'

### `scenes`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all Scenes in the Live Song.

### `select_on_launch`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Get if Scenes and Clips should be selected when fired.

### `session_automation_record`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Returns true if automation recording is enabled.

### `session_record`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the session record state.

### `session_record_status`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Get the session slot-recording state.

### `signature_denominator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the global signature denominator of the Song.

### `signature_numerator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the global signature numerator of the Song.

### `song_length`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Return the time of the last set event in the song, plus som extra beats that are usually added for better navigation in the arrangerview.

### `start_time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the songs current start time in beats. The set time may be overridden by the current loop/locator start time.

### `swing_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the amount of swing that is applied when adding or quantizing notes to MIDI clips

### `tempo`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the global project tempo.

### `tempo_follower_enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set whether the Tempo Follower is controlling the tempo. The Tempo Follower Toggle must be made visible in the preferences for this property to be effective.

### `tracks`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all Player Tracks in the Live Song, excluding the return and Main Track (see also Song.send_tracks and Song.master_track). At least one MIDI or Audio Track is always available.

### `tuning_system`

- **Type:** `TuningSystem`
- **Settable:** `no`
- **Listenable:** `yes`

Access the currently active tuning system.

### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a Live document: The Session and Arrangerview.

### `visible_tracks`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all visible Player Tracks in the Live Song, excluding the return and Main Track (see also Song.send_tracks and Song.master_track). At least one MIDI or Audio Track is always available.

## Methods

| Method                                                                          | Returns    | Description                                                                      |
| ------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------- |
| `begin_undo_step()`                                                             | `None`     |                                                                                  |
| `capture_and_insert_scene(CaptureMode: CaptureMode \| int = 0)`                 | `None`     | Capture currently playing clips and insert them as a new scene after the sele... |
| `capture_midi(Destination: CaptureDestination \| int = 0)`                      | `None`     | Capture recently played MIDI material from audible tracks.                       |
| `continue_playing()`                                                            | `None`     | Continue playing the song from the current position.                             |
| `create_audio_track(Index: int = None)`                                         | `Track`    | Create a new audio track at the optional given index and return it.If the ind... |
| `create_midi_track(Index: int = None)`                                          | `Track`    | Create a new midi track at the optional given index and return it.If the inde... |
| `create_return_track()`                                                         | `Track`    | Create a new return track at the end and return it.                              |
| `create_scene(index: int)`                                                      | `Scene`    | Create a new scene at the given index.                                           |
| `delete_return_track(index: int)`                                               | `None`     | Delete the return track with the given index.                                    |
| `delete_scene(index: int)`                                                      | `None`     | Delete the scene with the given index.                                           |
| `delete_track(index: int)`                                                      | `None`     | Delete the track with the given index.                                           |
| `duplicate_scene(index: int)`                                                   | `None`     | Duplicates a scene and selects the new one.                                      |
| `duplicate_track(index: int)`                                                   | `None`     | Duplicates a track and selects the new one.                                      |
| `end_undo_step()`                                                               | `None`     |                                                                                  |
| `find_device_position(device: Device, target: LomObject, target_position: int)` | `int`      | Returns the closest possible position to the given target, where the device c... |
| `force_link_beat_time()`                                                        | `None`     | Force the Link timeline to jump to Lives current beat time.                      |
| `get_beats_loop_length()`                                                       | `BeatTime` | Get const access to the songs loop length, using a BeatTime class with the cu... |
| `get_beats_loop_start()`                                                        | `BeatTime` | Get const access to the songs loop start, using a BeatTime class with the cur... |
| `get_current_beats_song_time()`                                                 | `BeatTime` | Get const access to the songs current playing position, using a BeatTime clas... |
| `get_current_smpte_song_time(format: int)`                                      | `SmptTime` | Get const access to the songs current playing position, by specifying the SMP... |
| `get_data(key: str, default_value: Any)`                                        | `Any`      | Get data for the given key, that was previously stored using set_data.           |
| `is_cue_point_selected()`                                                       | `bool`     | Return true if the global playing pos is currently on a cue point.               |
| `jump_by(beats: float)`                                                         | `None`     | Set a new playing pos, relative to the current one.                              |
| `jump_to_next_cue()`                                                            | `None`     | Jump to the next cue (marker) if possible.                                       |
| `jump_to_prev_cue()`                                                            | `None`     | Jump to the prior cue (marker) if possible.                                      |
| `move_device(device: Device, target: LomObject, target_position: int)`          | `int`      | Move a device into the target at the given position, where 0 moves it before ... |
| `play_selection()`                                                              | `None`     | Start playing the current set selection, or do nothing if no selection is set.   |
| `re_enable_automation()`                                                        | `None`     | Discards overrides of automated parameters.                                      |
| `redo()`                                                                        | `str`      | Redo the last action that was undone.                                            |
| `scrub_by(beats: float)`                                                        | `None`     | Same as jump_by, but does not stop playback.                                     |
| `set_data(key: str, value: Any)`                                                | `None`     | Store data for the given key in this object.                                     |
| `set_or_delete_cue()`                                                           | `None`     | When a cue is selected, it gets deleted.                                         |
| `start_playing()`                                                               | `None`     | Start playing from the startmarker.                                              |
| `stop_all_clips(Quantized: bool = True)`                                        | `None`     | Stop all playing Clips (if any) but continue playing the Song.                   |
| `stop_playing()`                                                                | `None`     | Stop playing the Song.                                                           |
| `tap_tempo()`                                                                   | `None`     | Trigger the tap tempo function.                                                  |
| `trigger_session_record(record_length: float = 1.7976931348623157e+308)`        | `None`     | Triggers a new session recording.                                                |
| `undo()`                                                                        | `str`      | Undo the last action that was made.                                              |

### `begin_undo_step()`

- **Returns:** `None`

### `capture_and_insert_scene(CaptureMode: CaptureMode | int = 0)`

- **Returns:** `None`
- **Args:**
  - `CaptureMode: CaptureMode | int = 0`

Capture currently playing clips and insert them as a new scene after the selected scene. Raises a runtime error if creating a new scene would exceed the limitations.

### `capture_midi(Destination: CaptureDestination | int = 0)`

- **Returns:** `None`
- **Args:**
  - `Destination: CaptureDestination | int = 0`

Capture recently played MIDI material from audible tracks. If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible. If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively. Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations.

### `continue_playing()`

- **Returns:** `None`

Continue playing the song from the current position

### `create_audio_track(Index: int = None)`

- **Returns:** `Track`
- **Args:**
  - `Index: int = None`

Create a new audio track at the optional given index and return it.If the index is -1, the new track is added at the end. It will create a default audio track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item

### `create_midi_track(Index: int = None)`

- **Returns:** `Track`
- **Args:**
  - `Index: int = None`

Create a new midi track at the optional given index and return it.If the index is -1, the new track is added at the end.It will create a default midi track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item

### `create_return_track()`

- **Returns:** `Track`

Create a new return track at the end and return it. If the new track would exceed the limitations, a limitation error is raised. If the maximum number of return tracks is exceeded, a RuntimeError is raised.

### `create_scene(index: int)`

- **Returns:** `Scene`
- **Args:**
  - `index: int`

Create a new scene at the given index. If the index is -1, the new scene is added at the end. If the index is invalid or the new scene would exceed the limitations, a limitation error is raised.

### `delete_return_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Delete the return track with the given index. If no track with this index exists, an exception will be raised.

### `delete_scene(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Delete the scene with the given index. If no scene with this index exists, an exception will be raised.

### `delete_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Delete the track with the given index. If no track with this index exists, an exception will be raised.

### `duplicate_scene(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Duplicates a scene and selects the new one. Raises a limitation error if creating a new scene would exceed the limitations.

### `duplicate_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Duplicates a track and selects the new one. If the track is inside a folded group track, the group track is unfolded. Raises a limitation error if creating a new track would exceed the limitations.

### `end_undo_step()`

- **Returns:** `None`

### `find_device_position(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int`
- **Args:**
  - `device: Device`
  - `target: LomObject`
  - `target_position: int`

Returns the closest possible position to the given target, where the device can be inserted. If inserting is not possible at all (i.e. if the device type is wrong), -1 is returned.

### `force_link_beat_time()`

- **Returns:** `None`

Force the Link timeline to jump to Lives current beat time. Danger: This can cause beat time discontinuities in other connected apps.

### `get_beats_loop_length()`

- **Returns:** `BeatTime`

Get const access to the songs loop length, using a BeatTime class with the current global set signature.

### `get_beats_loop_start()`

- **Returns:** `BeatTime`

Get const access to the songs loop start, using a BeatTime class with the current global set signature.

### `get_current_beats_song_time()`

- **Returns:** `BeatTime`

Get const access to the songs current playing position, using a BeatTime class with the current global set signature.

### `get_current_smpte_song_time(format: int)`

- **Returns:** `SmptTime`
- **Args:**
  - `format: int`

Get const access to the songs current playing position, by specifying the SMPTE format in which you would like to receive the time.

### `get_data(key: str, default_value: Any)`

- **Returns:** `Any`
- **Args:**
  - `key: str`
  - `default_value: Any`

Get data for the given key, that was previously stored using set_data.

### `is_cue_point_selected()`

- **Returns:** `bool`

Return true if the global playing pos is currently on a cue point.

### `jump_by(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float`

Set a new playing pos, relative to the current one.

### `jump_to_next_cue()`

- **Returns:** `None`

Jump to the next cue (marker) if possible.

### `jump_to_prev_cue()`

- **Returns:** `None`

Jump to the prior cue (marker) if possible.

### `move_device(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int`
- **Args:**
  - `device: Device`
  - `target: LomObject`
  - `target_position: int`

Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.

### `play_selection()`

- **Returns:** `None`

Start playing the current set selection, or do nothing if no selection is set.

### `re_enable_automation()`

- **Returns:** `None`

Discards overrides of automated parameters.

### `redo()`

- **Returns:** `str`

Redo the last action that was undone.

### `scrub_by(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float`

Same as jump_by, but does not stop playback.

### `set_data(key: str, value: Any)`

- **Returns:** `None`
- **Args:**
  - `key: str`
  - `value: Any`

Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

### `set_or_delete_cue()`

- **Returns:** `None`

When a cue is selected, it gets deleted. If no cue is selected, a new cue is created at the current global songtime.

### `start_playing()`

- **Returns:** `None`

Start playing from the startmarker

### `stop_all_clips(Quantized: bool = True)`

- **Returns:** `None`
- **Args:**
  - `Quantized: bool = True`

Stop all playing Clips (if any) but continue playing the Song.

### `stop_playing()`

- **Returns:** `None`

Stop playing the Song.

### `tap_tempo()`

- **Returns:** `None`

Trigger the tap tempo function.

### `trigger_session_record(record_length: float = 1.7976931348623157e+308)`

- **Returns:** `None`
- **Args:**
  - `record_length: float = 1.7976931348623157e+308`

Triggers a new session recording.

### `undo()`

- **Returns:** `str`

Undo the last action that was made.

## Enums

### `CaptureDestination`

The destination for MIDI capture.

| Value | Name          |
| ----- | ------------- |
| `0`   | `auto`        |
| `1`   | `session`     |
| `2`   | `arrangement` |

### `CaptureMode`

The capture mode that is used for capture and insert scene.

| Value | Name                  |
| ----- | --------------------- |
| `0`   | `all`                 |
| `1`   | `all_except_selected` |

### `Quantization`

| Value | Name                 |
| ----- | -------------------- |
| `0`   | `q_no_q`             |
| `1`   | `q_8_bars`           |
| `2`   | `q_4_bars`           |
| `3`   | `q_2_bars`           |
| `4`   | `q_bar`              |
| `5`   | `q_half`             |
| `6`   | `q_half_triplet`     |
| `7`   | `q_quarter`          |
| `8`   | `q_quarter_triplet`  |
| `9`   | `q_eight`            |
| `10`  | `q_eight_triplet`    |
| `11`  | `q_sixtenth`         |
| `12`  | `q_sixtenth_triplet` |
| `13`  | `q_thirtytwoth`      |

### `RecordingQuantization`

| Value | Name                              |
| ----- | --------------------------------- |
| `0`   | `rec_q_no_q`                      |
| `1`   | `rec_q_quarter`                   |
| `2`   | `rec_q_eight`                     |
| `3`   | `rec_q_eight_triplet`             |
| `4`   | `rec_q_eight_eight_triplet`       |
| `5`   | `rec_q_sixtenth`                  |
| `6`   | `rec_q_sixtenth_triplet`          |
| `7`   | `rec_q_sixtenth_sixtenth_triplet` |
| `8`   | `rec_q_thirtysecond`              |

### `SessionRecordStatus`

| Value | Name         |
| ----- | ------------ |
| `0`   | `off`        |
| `1`   | `on`         |
| `2`   | `transition` |

### `TimeFormat`

| Value | Name            |
| ----- | --------------- |
| `0`   | `ms_time`       |
| `1`   | `smpte_24`      |
| `2`   | `smpte_25`      |
| `3`   | `smpte_30`      |
| `4`   | `smpte_30_drop` |
| `5`   | `smpte_29`      |

## BeatTime

> `Live.Song.BeatTime`

Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.

**Constructor:** `BeatTime()`

### Properties

| Property       | Type  | Settable | Listenable | Description |
| -------------- | ----- | -------- | ---------- | ----------- |
| `bars`         | `int` | `yes`    | `no`       |             |
| `beats`        | `int` | `yes`    | `no`       |             |
| `sub_division` | `int` | `yes`    | `no`       |             |
| `ticks`        | `int` | `yes`    | `no`       |             |

#### `bars`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `beats`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `sub_division`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `ticks`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

## CuePoint

> `Live.Song.CuePoint`

Represents a 'Marker' in the arrangement.

### Properties

| Property           | Type    | Settable | Listenable | Description                                                              |
| ------------------ | ------- | -------- | ---------- | ------------------------------------------------------------------------ |
| `canonical_parent` | `Song`  | `no`     | `no`       | Get the canonical parent of the cue point.                               |
| `name`             | `str`   | `yes`    | `yes`      | Get/Set/Listen to the name of this CuePoint, as visible in the arranger. |
| `time`             | `float` | `no`     | `yes`      | Get/Listen to the CuePoint's time in beats.                              |

#### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the cue point.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set/Listen to the name of this CuePoint, as visible in the arranger.

#### `time`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Get/Listen to the CuePoint's time in beats.

### Methods

| Method   | Returns | Description                                                                      |
| -------- | ------- | -------------------------------------------------------------------------------- |
| `jump()` | `None`  | When the Song is playing, set the playing-position quantized to this Cuepoint... |

#### `jump()`

- **Returns:** `None`

When the Song is playing, set the playing-position quantized to this Cuepoint's time. When not playing, simply move the start playing position.

## SmptTime

> `Live.Song.SmptTime`

Represents a Time, split into Hours, Minutes, Seconds and Frames. The frame type must be specified when calling a function that returns a SmptTime.

**Constructor:** `SmptTime()`

### Properties

| Property  | Type  | Settable | Listenable | Description |
| --------- | ----- | -------- | ---------- | ----------- |
| `frames`  | `int` | `yes`    | `no`       |             |
| `hours`   | `int` | `yes`    | `no`       |             |
| `minutes` | `int` | `yes`    | `no`       |             |
| `seconds` | `int` | `yes`    | `no`       |             |

#### `frames`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `hours`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `minutes`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `seconds`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

## Module Functions

| Function                   | Returns | Description                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------- |
| `get_all_scales_ordered()` | `tuple` | Get an ordered tuple of tuples of all available scale names to intervals. |

### `get_all_scales_ordered()`

- **Returns:** `tuple`

Get an ordered tuple of tuples of all available scale names to intervals.

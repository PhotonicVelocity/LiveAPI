# Song

> `Live.Song.Song`

This class represents a Live Set. The current Live Set is reachable by the root path `live_set`.

??? note "Raw probe notes (temporary)"

    - `can_undo` / `can_redo` visibility is asynchronous after mutations and often appears on a later application
      scheduler turn.
    - `begin_undo_step()` / `end_undo_step()` groups undo-tracked actions into one undo step; grouping does not
      force non-undo-tracked actions to become undo-tracked.
    - `undo()` / `redo()` return Live-managed label text; labels are UI/history/locale dependent. In current probes,
      API-originated mutations commonly report `Undo Custom Action` / `Redo Custom Action`.
    - Setting `tempo` is confirmed undo-tracked in current probes.
    - `jump_by()` and `scrub_by()` were observed to work while playing and while stopped, with equivalent movement
      behavior.
    - Runtime probe (Live 12.3.5): BeatTime tick grid is `60` ticks per sixteenth, `4` sixteenths per beat, `240`
      ticks per beat. All components are **1-based** — position `0.0` beats = `1.1.1.1`.
    - Runtime probe (Live 12.3.5, BBST vs time signature): **The denominator affects BBST beat size.** Each BBST
      "beat" is the note value specified by the denominator. Tested across 8 signatures. See BeatTime section.
    - `overdub` vs `arrangement_overdub` (probed 2026-02-17): they are **distinct states**.
      `arrangement_overdub` is always settable and sticks independently. `overdub` silently ignores `set` when no
      track is armed / no session recording is active — it controls session MIDI overdub, not arrangement overdub.
    - Runtime probe (Live 12.3.5): `set_data(key, None)` followed by `get_data(key, default)` returns `None`
      rather than `default`.
    - Not all actions are undo-tracked. Undo/redo history is global to the Live document, not scoped to one script
      client.

### Open Questions

- ~~Full numeric mapping for `Song.CaptureMode`.~~ **Resolved:** `0`=all, `1`=all except selected track.
  Values >= 2 fall back to `all`.
- ~~Numeric mapping for `Song.SessionRecordStatus`.~~ **Resolved:** `0`=off, `1`=recording, `2`=triggered.
- Member-by-member matrix of which mutating Song actions are undo-tracked vs non-undo-tracked.

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `cue_points` | `Sequence[CuePoint]` | `list` | `yes` | Arrangement locator markers. |
| `return_tracks` | `Sequence[Track]` | `list` | `yes` | Return tracks. |
| `scenes` | `Sequence[Scene]` | `list` | `yes` | Scenes. |
| `tracks` | `Sequence[Track]` | `list` | `yes` | All main tracks. |
| `visible_tracks` | `Sequence[Track]` | `list` | `yes` | Tracks not hidden by a folded group. |
| `master_track` | `Track` | `single` | `no` | The master track. |
| `view` | `Song.View` | `single` | `no` | View aspects of the song. |
| `groove_pool` | `GroovePool` | `single` | `no` | Live's groove pool. |
| `tuning_system` | `TuningSystem` | `single` | `yes` | Live's currently active tuning system. |

#### `cue_points`

- **Returns:** `Sequence[CuePoint]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

Cue points are the markers in the Arrangement to which you can jump.

#### `return_tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of return tracks.

#### `scenes`

- **Returns:** `Sequence[Scene]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of scenes.

#### `tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of all main tracks.

#### `visible_tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

A track is visible if it's not part of a folded group. If a track is scrolled out of view it's still considered
visible.

#### `master_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The master track.

#### `view`

- **Returns:** `Song.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

View aspects of the song.

#### `groove_pool`

- **Returns:** `GroovePool`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `11.0`

Live's groove pool.

#### `tuning_system`

- **Returns:** `TuningSystem`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `12.0`

Live's currently active tuning system.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `appointed_device` | `Device` | `no` | `yes` | The device marked with the blue hand. |
| `arrangement_overdub` | `bool` | `yes` | `yes` | State of the MIDI Arrangement Overdub button. |
| `back_to_arranger` | `bool` | `yes` | `yes` | State of the Back to Arrangement button. |
| `can_capture_midi` | `bool` | `no` | `yes` | `True` if recently played MIDI can be captured. |
| `can_jump_to_next_cue` | `bool` | `no` | `yes` | `True` if there is a cue point to the right. |
| `can_jump_to_prev_cue` | `bool` | `no` | `yes` | `True` if there is a cue point to the left. |
| `can_redo` | `bool` | `no` | `no` | `True` if there is something to redo. |
| `can_undo` | `bool` | `no` | `no` | `True` if there is something to undo. |
| `canonical_parent` | `object` | `no` | `no` | The canonical parent of the song. |
| `clip_trigger_quantization` | `Song.Quantization` | `yes` | `yes` | Global launch quantization in the transport bar. |
| `count_in_duration` | `int` | `no` | `yes` | Metronome count-in setting index. |
| `current_song_time` | `float` | `yes` | `yes` | Playback position in beats. |
| `exclusive_arm` | `bool` | `no` | `no` | Exclusive Arm preference status. |
| `exclusive_solo` | `bool` | `no` | `no` | Exclusive Solo preference status. |
| `file_path` | `str` | `no` | `no` | Path to the current Live Set. Empty if unsaved. |
| `groove_amount` | `float` | `yes` | `yes` | Global Groove Amount (0.0-1.0). |
| `is_ableton_link_enabled` | `bool` | `yes` | `yes` | Enable/disable Ableton Link. |
| `is_ableton_link_start_stop_sync_enabled` | `bool` | `yes` | `yes` | Enable/disable Link Start Stop Sync. |
| `is_counting_in` | `bool` | `no` | `yes` | `True` if the metronome is counting in. |
| `is_playing` | `bool` | `yes` | `yes` | `True` if the transport is running. |
| `last_event_time` | `float` | `no` | `no` | Beat time of the last event in the Arrangement. |
| `loop` | `bool` | `yes` | `yes` | Arrangement loop enabled state. |
| `loop_length` | `float` | `yes` | `yes` | Arrangement loop length in beats. |
| `loop_start` | `float` | `yes` | `yes` | Arrangement loop start in beats. |
| `metronome` | `bool` | `yes` | `yes` | Metronome enabled state. |
| `midi_recording_quantization` | `Song.RecordingQuantization` | `yes` | `yes` | Record Quantization value. |
| `name` | `str` | `no` | `no` | Name of the current Live Set. Empty if unsaved. |
| `nudge_down` | `bool` | `yes` | `yes` | Tempo Nudge Down button state. |
| `nudge_up` | `bool` | `yes` | `yes` | Tempo Nudge Up button state. |
| `overdub` | `bool` | `yes` | `yes` | Session MIDI overdub toggle. |
| `punch_in` | `bool` | `yes` | `yes` | Punch-In button state. |
| `punch_out` | `bool` | `yes` | `yes` | Punch-Out button state. |
| `re_enable_automation_enabled` | `bool` | `no` | `yes` | `True` if Re-Enable Automation button is on. |
| `record_mode` | `bool` | `yes` | `yes` | Arrangement Record button state. |
| `root_note` | `int` | `yes` | `yes` | Root note of the current scale (0=C, 11=B). |
| `scale_intervals` | `list` | `no` | `yes` | Intervals in the current scale. |
| `scale_mode` | `bool` | `yes` | `yes` | Scale Mode setting. |
| `scale_name` | `str` | `yes` | `yes` | Name of the current scale. |
| `select_on_launch` | `bool` | `no` | `no` | "Select on Launch" preference. |
| `session_automation_record` | `bool` | `yes` | `yes` | Automation Arm button state. |
| `session_record` | `bool` | `yes` | `yes` | Session Record / Overdub button state. |
| `session_record_status` | `Song.SessionRecordStatus` | `no` | `yes` | Session recording state: 0=off, 1=recording, 2=triggered. |
| `signature_denominator` | `int` | `yes` | `yes` | Global time signature denominator. |
| `signature_numerator` | `int` | `yes` | `yes` | Global time signature numerator. |
| `song_length` | `float` | `no` | `yes` | A little more than `last_event_time`, in beats. |
| `start_time` | `float` | `yes` | `yes` | Position where playing will start, in beats. |
| `swing_amount` | `float` | `yes` | `yes` | Swing amount, 0.0-1.0. |
| `tempo` | `float` | `yes` | `yes` | Tempo in BPM (20.0-999.0). May be automated. |
| `tempo_follower_enabled` | `bool` | `yes` | `yes` | `True` if the Tempo Follower controls the tempo. |

#### `appointed_device`

- **Type:** `Device`
- **Listenable:** `yes`
- **Since:** `<11`

The appointed device is the one used by a control surface unless the control surface itself chooses which device to
use. It is marked by a blue hand in the UI.

- **Quirks:** `appointed_device` is independent from both the selected device (white outline) and
  `Browser.hotswap_target`. See `Song.View.select_device()` for the distinction between selection and appointment.

#### `arrangement_overdub`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the state of the MIDI Arrangement Overdub button. When enabled, existing notes in MIDI clips in the
Arrangement will be mixed with newly recorded notes. Always settable independently — does not require
`record_mode` or an armed track. Distinct from `overdub` (which is session MIDI overdub).

#### `back_to_arranger`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the state of the Back to Arrangement button in the transport bar (`1` = highlighted). Setting to `0` makes
Live go back to playing the arrangement content.

#### `can_capture_midi`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if recently played MIDI material exists that can be captured into a Live Track. See `capture_midi`.

#### `can_jump_to_next_cue`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`False` if there is no cue point to the right of the current one, or none at all.

#### `can_jump_to_prev_cue`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`False` if there is no cue point to the left of the current one, or none at all.

#### `can_redo`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if there is something in the history to redo.

- **Quirks:** Visibility may update on a later scheduler turn after stack mutations.

#### `can_undo`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if there is something in the history to undo.

- **Quirks:** Visibility may update on a later scheduler turn after stack mutations.

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the song.

#### `clip_trigger_quantization`

- **Type:** `Song.Quantization`
- **Listenable:** `yes`
- **Since:** `<11`

The global launch quantization setting in the transport bar. Values: `0`=None, `1`=8 Bars, `2`=4 Bars, `3`=2 Bars,
`4`=1 Bar, `5`=1/2, `6`=1/2T, `7`=1/4, `8`=1/4T, `9`=1/8, `10`=1/8T, `11`=1/16, `12`=1/16T, `13`=1/32.

#### `count_in_duration`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The duration of the Metronome's Count-In setting as an index. Values: `0`=None, `1`=1 Bar, `2`=2 Bars, `3`=4 Bars.

#### `current_song_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

The playing position in the Live Set, in beats.

#### `exclusive_arm`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Current status of the exclusive Arm option set in the Live preferences.

#### `exclusive_solo`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Current status of the exclusive Solo option set in the Live preferences.

#### `file_path`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `11.3`

The path to the current Live Set, in OS-native format. Empty if the Live Set hasn't been saved.

#### `groove_amount`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

The Global Groove Amount from the current set's groove pool (0.0-1.0). Scales the overall intensity of Timing,
Random, and Velocity for all grooves in the Pool. Values above 1.0 push parameters beyond their assigned values.

#### `is_ableton_link_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `11.1`

Enable/disable Ableton Link. The Link toggle in Live's transport bar must be visible to enable Link.

#### `is_ableton_link_start_stop_sync_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `11.1`

Enable/disable Ableton Link Start Stop Sync.

#### `is_counting_in`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Metronome is currently counting in.

#### `is_playing`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set if Live's transport is running.

#### `last_event_time`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

The beat time of the last event (automation breakpoint, clip end, cue point, loop end) in the Arrangement.

#### `loop`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the enabled state of the Arrangement loop.

#### `loop_length`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Arrangement loop length in beats.

#### `loop_start`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Arrangement loop start in beats.

#### `metronome`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the enabled state of the metronome. The metronome's volume is controlled by the Preview/Cue Volume knob in
the Main track's mixer. See also `count_in_duration`.

#### `midi_recording_quantization`

- **Type:** `Song.RecordingQuantization`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current Record Quantization value. Values: `0`=None, `1`=1/4, `2`=1/8, `3`=1/8T, `4`=1/8+1/8T,
`5`=1/16, `6`=1/16T, `7`=1/16+1/16T, `8`=1/32.

#### `name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `11.3`

The name of the current Live Set. Empty if the Live Set hasn't been saved.

#### `nudge_down`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Tempo Nudge Down button in the transport bar is currently pressed.

#### `nudge_up`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Tempo Nudge Up button in the transport bar is currently pressed.

#### `overdub`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Session MIDI overdub toggle. Setting to `True` silently does nothing unless a track is armed and session recording
is active. Distinct from `arrangement_overdub` (which is always settable). Despite the stub description mentioning
"Arrangement Overdub", probing confirms this controls session overdub behavior.

#### `punch_in`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Punch-In button is enabled in the transport. Prevents Arrangement recording prior to the punch-in
point (left edge of the loop brace).

#### `punch_out`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Punch-Out button is enabled in the transport. Prevents Arrangement recording after the punch-out
point (right edge of the loop brace).

#### `re_enable_automation_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when the Re-Enable Automation button is on. Only `True` when at least one automated parameter has been
manually overridden. See `re_enable_automation()`.

#### `record_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

The Arrangement Record button state. If "Start Transport With Record" preference is enabled, setting to `True`
also starts the transport. Setting to `False` does not stop playback. See also `trigger_session_record`.

#### `root_note`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The root note of the current scale, 0-11 (0=C, 11=B).

#### `scale_intervals`

- **Type:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

A list of integers representing the intervals in Live's current scale. An interval is the difference between the
scale degree at the list index and the first scale degree.

#### `scale_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `12.0`

Access to the Scale Mode setting in Live. When enabled, `root_note` and `scale_name` reflect the active scale.

#### `scale_name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

The name of the scale selected in Live, as displayed in the Current Scale Name chooser.

#### `select_on_launch`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the "Select on Launch" option is set in Live's preferences.

#### `session_automation_record`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

The state of the Automation Arm button. When enabled, manual parameter changes can be recorded to Session clips and
the Arrangement.

#### `session_record`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

The state of the Session Record / Overdub button. When enabled, overdub recording is active for currently playing
clips on armed tracks.

#### `session_record_status`

- **Type:** `Song.SessionRecordStatus`
- **Listenable:** `yes`
- **Since:** `<11`

Session slot-recording state: `0`=off, `1`=recording, `2`=triggered.

- **Quirks:** During the triggered phase (`status == 2`), `session_record` remains `False` and the target slot
  reports `is_triggered = True`. Once the quantization boundary is reached, status transitions to `1`,
  `session_record` becomes `True`, and the slot reports `is_recording = True`.

#### `signature_denominator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The global signature denominator. Determines the BBST beat unit size: `/4` = one BBST beat = 1 quarter-note beat;
`/8` = one BBST beat = 1 eighth-note beat. Formula: `beat_unit = 4 / denominator`. See BeatTime section.

#### `signature_numerator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The global signature numerator. Determines the number of BBST beats per bar. Bar length in internal beats =
`numerator * (4 / denominator)`. See BeatTime section.

#### `song_length`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

A little more than `last_event_time`, in beats.

#### `start_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.1`

The position in the Live Set where playing will start, in beats.

#### `swing_amount`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Range: 0.0-1.0; affects MIDI Recording Quantization and all direct calls to `Clip.quantize`.

#### `tempo`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Current tempo of the Live Set in BPM, 20.0-999.0. The tempo may be automated, so it can change depending on the
current song time.

#### `tempo_follower_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the Tempo Follower controls the tempo. The Tempo Follower Toggle must be visible in the preferences for
this property to be effective.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `begin_undo_step()` | `None` | Begin an undo group. |
| `capture_and_insert_scene(capture_mode: Song.CaptureMode = all)` | `None` | Capture playing clips into a new scene. |
| `capture_midi(destination: Song.CaptureDestination = auto)` | `None` | Capture recently played MIDI into a clip. |
| `continue_playing()` | `None` | Resume playback from current position. |
| `create_audio_track(index: int)` | `Track` | Create a new audio track. |
| `create_midi_track(index: int)` | `Track` | Create a new MIDI track. |
| `create_return_track()` | `Track` | Add a new return track at the end. |
| `create_scene(index: int)` | `Scene` | Create a new scene. |
| `delete_return_track(index: int)` | `None` | Delete a return track. |
| `delete_scene(index: int)` | `None` | Delete a scene. |
| `delete_track(index: int)` | `None` | Delete a track. |
| `duplicate_scene(index: int)` | `None` | Duplicate a scene. |
| `duplicate_track(index: int)` | `None` | Duplicate a track. |
| `end_undo_step()` | `None` | End the current undo group. |
| `find_device_position(device, target, target_position: int)` | `int` | Query nearest valid device insertion position. |
| `force_link_beat_time()` | `None` | Force the Link timeline to jump to Live's beat time. |
| `get_beats_loop_length()` | `Song.BeatTime` | Arrangement loop length in BBST. |
| `get_beats_loop_start()` | `Song.BeatTime` | Arrangement loop start in BBST. |
| `get_current_beats_song_time()` | `Song.BeatTime` | Current playback position in BBST. |
| `get_current_smpte_song_time(format: Song.TimeFormat)` | `Song.SmptTime` | Current position in SMPTE format. |
| `get_data(key: object, default_value: object)` | `object` | Get persistent data for the given key. |
| `is_cue_point_selected()` | `bool` | `True` if playback is at a cue point. |
| `jump_by(beats: float)` | `None` | Relative jump from current position. |
| `jump_to_next_cue()` | `None` | Jump to the next cue point. |
| `jump_to_prev_cue()` | `None` | Jump to the previous cue point. |
| `move_device(device, target, target_position: int)` | `int` | Move a device to a new position. |
| `play_selection()` | `None` | Play the current Arrangement selection. |
| `re_enable_automation()` | `None` | Re-enable overridden automation. |
| `redo()` | `str` | Redo last undone action; returns label text. |
| `scrub_by(beats: float)` | `None` | Scrub relative to current position. |
| `set_data(key: object, value: object)` | `None` | Store persistent data for the given key. |
| `set_or_delete_cue()` | `None` | Toggle cue point at current position. |
| `start_playing()` | `None` | Start playback from the insert marker. |
| `stop_all_clips(quantized: bool)` | `None` | Stop all playing clips. |
| `stop_playing()` | `None` | Stop playback. |
| `tap_tempo()` | `None` | Tap tempo. |
| `trigger_session_record(record_length: float)` | `None` | Start session recording. |
| `undo()` | `str` | Undo last action; returns label text. |
| `get_all_scales_ordered()` | `tuple` | Static. Returns all available scales. |

#### `begin_undo_step()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Begins an undo group. Subsequent undo-tracked actions are committed as one step when `end_undo_step()` is called.
Does not force non-undo-tracked actions to become undo-tracked.

#### `capture_and_insert_scene(capture_mode: Song.CaptureMode = Song.CaptureMode.all)`

- **Returns:** `None`
- **Args:**
  - `capture_mode: Song.CaptureMode` -- `0`=all (default), `1`=all except selected track
- **Since:** `<11`

Captures currently playing clips and inserts them as a new scene below the selected scene. Playback switches to
the newly inserted scene. Arm state does not affect which tracks are captured.

- **Quirks:** Values >= 2 and negative values all fall back to `all` behavior. The `CaptureMode` class is not
  accessible as a `Song` attribute at runtime.

#### `capture_midi(destination: Song.CaptureDestination = Song.CaptureDestination.auto)`

- **Returns:** `None`
- **Args:**
  - `destination: Song.CaptureDestination` -- `0`=auto, `1`=session, `2`=arrangement
- **Since:** `<11`

Capture recently played MIDI material from audible tracks into a Live Clip. If `destination` is `auto`, the clip is
inserted into the view currently visible. If the transport is stopped, the Set's tempo updates to match the
detected tempo. See `can_capture_midi`.

#### `continue_playing()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Resume playback from the current playback position.

#### `create_audio_track(index: int)`

- **Returns:** `Track`
- **Args:**
  - `index: int` -- position for the new track (0 to `len(song.tracks)`; `-1` = end)
- **Since:** `<11`

Create a new audio track at the given index.

#### `create_midi_track(index: int)`

- **Returns:** `Track`
- **Args:**
  - `index: int` -- position for the new track (0 to `len(song.tracks)`; `-1` = end)
- **Since:** `<11`

Create a new MIDI track at the given index.

#### `create_return_track()`

- **Returns:** `Track`
- **Args:** None
- **Since:** `<11`

Adds a new return track at the end.

#### `create_scene(index: int)`

- **Returns:** `Scene`
- **Args:**
  - `index: int` -- position for the new scene (0 to `len(song.scenes)`; `-1` = end)
- **Since:** `<11`

Create a new scene at the given index.

#### `delete_return_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- index of the return track to delete
- **Since:** `<11`

Delete the return track at the given index.

#### `delete_scene(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- index of the scene to delete
- **Since:** `<11`

Delete the scene at the given index.

#### `delete_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- index of the track to delete
- **Since:** `<11`

Delete the track at the given index.

#### `duplicate_scene(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- index of the scene to duplicate
- **Since:** `<11`

Duplicate the scene at the given index.

#### `duplicate_track(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- index of the track to duplicate
- **Since:** `<11`

Duplicate the track at the given index.

#### `end_undo_step()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Ends the current undo group and commits grouped undo-tracked actions as one step.

#### `find_device_position(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int` -- the nearest valid insertion position
- **Args:**
  - `device: Device` -- the device to query
  - `target: LomObject` -- the target Track or Chain
  - `target_position: int` -- desired position
- **Since:** `<11`

Queries the nearest valid insertion position without actually moving the device. Useful for validating
`move_device` targets before performing the move.

#### `force_link_beat_time()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Force the Link timeline to jump to Live's current beat time.

#### `get_beats_loop_length()`

- **Returns:** `Song.BeatTime`
- **Args:** None
- **Since:** `<11`

The Arrangement loop length as a BeatTime value (bars.beats.sixteenths.ticks).

#### `get_beats_loop_start()`

- **Returns:** `Song.BeatTime`
- **Args:** None
- **Since:** `<11`

The Arrangement loop start as a BeatTime value.

#### `get_current_beats_song_time()`

- **Returns:** `Song.BeatTime`
- **Args:** None
- **Since:** `<11`

The current Arrangement playback position as a BeatTime value.

#### `get_current_smpte_song_time(format: Song.TimeFormat)`

- **Returns:** `Song.SmptTime`
- **Args:**
  - `format: Song.TimeFormat` -- `0`=milliseconds, `1`=Smpte24, `2`=Smpte25, `3`=Smpte30, `4`=Smpte30Drop,
    `5`=Smpte29
- **Since:** `<11`

The current Arrangement playback position in the specified SMPTE format.

#### `get_data(key: object, default_value: object)`

- **Returns:** `object`
- **Args:**
  - `key: object` -- the key to look up
  - `default_value: object` -- returned if the key was never set
- **Since:** `<11`

Get persistent data for the given key. Data is restored when loading the Live Set.

- **Quirks:** After `set_data(key, None)`, `get_data(key, default)` returns `None` rather than the provided
  default.

#### `is_cue_point_selected()`

- **Returns:** `bool`
- **Args:** None
- **Since:** `<11`

`True` if the global playing position is currently on a cue point.

#### `jump_by(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- amount to jump relative to current position
- **Since:** `<11`

Jump relative to the current position in beats. Works while playing and while stopped.

#### `jump_to_next_cue()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Jump to the next cue point to the right, if possible.

#### `jump_to_prev_cue()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Jump to the previous cue point to the left, if possible.

#### `move_device(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int` -- the actual insertion position (may differ from `target_position`)
- **Args:**
  - `device: Device` -- the device to move
  - `target: LomObject` -- the destination Track or Chain
  - `target_position: int` -- desired position in the target's device chain
- **Raises:** `InternalError: Couldn't move device. target_index out of range.` if `target_position` is invalid.
- **Since:** `<11`

Moves a device to the specified position in the target's device chain. Works across tracks and into nested rack
chains. Use `find_device_position()` to validate targets before moving.

#### `play_selection()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Play the current selection in the Arrangement, or do nothing if no selection is set.

#### `re_enable_automation()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Re-enable automation for any parameters that are currently overridden. Only has an effect when
`re_enable_automation_enabled` is `True`.

#### `redo()`

- **Returns:** `str` -- Live-provided redo label text
- **Args:** None
- **Since:** `<11`

Redo the last undone action. Returns the label text (e.g. `"Redo Custom Action"`).

#### `scrub_by(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- amount to scrub relative to current position
- **Since:** `<11`

Scrub relative to the current Arrangement playback position. Same behavior as `jump_by` in current probes.

#### `set_data(key: object, value: object)`

- **Returns:** `None`
- **Args:**
  - `key: object` -- the key to store under
  - `value: object` -- the value to store
- **Since:** `<11`

Store data for the given key. The data is persistent and will be restored when loading the Live Set.

#### `set_or_delete_cue()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Toggle cue point at the current Arrangement playback position.

#### `start_playing()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Start playback from the insert marker.

#### `stop_all_clips(quantized: bool)`

- **Returns:** `None`
- **Args:**
  - `quantized: bool` -- `False` stops immediately, `True` (default) respects launch quantization
- **Since:** `<11`

Stop all playing clips.

#### `stop_playing()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Stop playback.

#### `tap_tempo()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Same as pressing the Tap Tempo button in the transport bar. The new tempo is calculated based on the time between
subsequent calls. If "Start Playback with Tap Tempo" is enabled, this can count in and start playback.

#### `trigger_session_record(record_length: float)`

- **Returns:** `None`
- **Args:**
  - `record_length: float (optional)` -- recording length in beats
- **Since:** `<11`

Equivalent to pressing the Session Record button. Starts recording in the selected slot or the next empty slot if
the track is armed. Always starts the transport (not affected by "Start Transport With Record" preference).
Complete no-op when no track is armed. If `record_length` is provided, recording stops after that many beats.

#### `undo()`

- **Returns:** `str` -- Live-provided undo label text
- **Args:** None
- **Since:** `<11`

Undo the last action. Returns the label text (e.g. `"Undo Custom Action"`).

#### `get_all_scales_ordered()`

- **Returns:** `tuple[tuple[str, tuple[int, ...]]]`
- **Args:** None
- **Since:** `<11`

Static method. Returns an ordered tuple of `(scale_name, intervals)` pairs for all scales available in Live.

---

## Song.View

> `Live.Song.Song.View`

Represents the view aspects of a Live document: the Session and Arrangement views.

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `detail_clip` | `Clip` | `single` | `yes` | The clip currently displayed in Detail View. |
| `highlighted_clip_slot` | `ClipSlot` | `single` | `no` | The slot highlighted in Session View. |
| `selected_chain` | `Chain` | `single` | `yes` | The highlighted chain, or `id 0`. |
| `selected_parameter` | `DeviceParameter` | `single` | `yes` | The selected parameter, or `id 0`. |
| `selected_scene` | `Scene` | `single` | `yes` | The currently selected scene. |
| `selected_track` | `Track` | `single` | `yes` | The currently selected track. |

#### `detail_clip`

- **Returns:** `Clip`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The clip currently displayed in Live's Detail View.

#### `highlighted_clip_slot`

- **Returns:** `ClipSlot`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The slot highlighted in Session View. Can be `None` for Main and Return tracks.

- **Quirks:** The highlighted slot is effectively the intersection of `selected_track` and `selected_scene`.

#### `selected_chain`

- **Returns:** `Chain`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The highlighted chain, or `id 0` when unavailable.

#### `selected_parameter`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The selected parameter, or `id 0`.

#### `selected_scene`

- **Returns:** `Scene`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected scene in Session View.

#### `selected_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected track in Session or Arrangement View.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `canonical_parent` | `Song` | `no` | `no` | The canonical parent of the song view. |
| `draw_mode` | `bool` | `yes` | `yes` | State of Draw Mode in the transport bar. |
| `follow_song` | `bool` | `yes` | `yes` | Whether Arrangement view follows playback. |

#### `canonical_parent`

- **Type:** `Song`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the song view.

#### `draw_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Reflects the state of the Draw Mode switch in the transport bar (`0` = breakpoint editing, `1` = drawing). Used
for drawing envelopes, MIDI, and automation curves.

#### `follow_song`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Reflects the state of the Follow switch in the transport bar. When enabled, the display scrolls during playback to
keep the current song position visible.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `select_device(device: Device, ShouldAppointDevice: bool = True)` | `None` | Select a device in Live's UI. |

#### `select_device(device: Device, ShouldAppointDevice: bool = True)`

- **Returns:** `None`
- **Args:**
  - `device: Device`
  - `ShouldAppointDevice: bool = True`
- **Since:** `<11`

Selects the given device in its track. The containing track is not automatically shown. The device is appointed
(blue hand) only if its track is selected and `ShouldAppointDevice` is `True`.

- **Quirks:** Live maintains two separate device states: the **selected** device (white outline, no public getter)
  and the **appointed** device (blue hand, via `Song.appointed_device`). `select_device(dev, True)` sets both;
  `select_device(dev, False)` sets only the selection. The selected device is what
  `Application.View.toggle_browse()` targets for hotswap — not `appointed_device`.

---

## BeatTime

> `Live.Song.BeatTime`

Represents a time split into bars, beats, subdivision, and ticks (BBST). All four components are **1-based** — the
origin (internal beat position 0.0) is represented as `1.1.1.1`.

### Tick Grid Constants

- **Ticks per sixteenth:** `60` (tick range per sixteenth: 1-60)
- **Sixteenths per beat:** `4` (sixteenth range per beat: 1-4)
- **Ticks per beat:** `240` (= 4 x 60)
- **Beats per bar:** `signature_numerator` (beat range per bar: 1-numerator)

### Time Signature Effect on BeatTime

**The denominator changes the BBST beat unit size.** Each BBST "beat" corresponds to the note value specified by
the denominator. The beat unit in internal (quarter-note) beats is `4 / denominator`.

| Signature | Beat unit (internal beats) | Beats per bar | Bar length (internal beats) |
| --- | --- | --- | --- |
| 4/4 | 1.0 | 4 | 4.0 |
| 3/4 | 1.0 | 3 | 3.0 |
| 5/4 | 1.0 | 5 | 5.0 |
| 6/4 | 1.0 | 6 | 6.0 |
| 6/8 | 0.5 | 6 | 3.0 |
| 3/8 | 0.5 | 3 | 1.5 |
| 7/8 | 0.5 | 7 | 3.5 |
| 12/8 | 0.5 | 12 | 6.0 |

Conversion formulas:

```
beat_unit         = 4.0 / denominator       # internal beats per BBST beat
bar_length        = numerator * beat_unit    # internal beats per bar
ticks_per_bar     = numerator * 240          # BBST ticks per bar
```

Position to BBST (0-based intermediate, then +1 for each component):

```
total_ticks  = round(position / beat_unit * 240)
bars_0       = total_ticks // ticks_per_bar
bar_ticks    = total_ticks %  ticks_per_bar
beats_0      = bar_ticks   // 240
beat_ticks   = bar_ticks   %  240
sixteenths_0 = beat_ticks  // 60
ticks_0      = beat_ticks  %  60
-> (bars_0+1, beats_0+1, sixteenths_0+1, ticks_0+1)
```

BBST to position:

```
total_ticks = (bars-1)*numerator*240 + (beats-1)*240 + (sixteenths-1)*60 + (ticks-1)
position    = total_ticks / 240 * beat_unit
```

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `bars` | `int` | `no` | `no` | Bar component (1-based). |
| `beats` | `int` | `no` | `no` | Beat component (1-based). Range: 1-numerator. |
| `sub_division` | `int` | `no` | `no` | Sixteenth component (1-based). Range: 1-4. |
| `ticks` | `int` | `no` | `no` | Tick component (1-based). Range: 1-60. |

#### `bars`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Bar component. 1-based.

#### `beats`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Beat component. 1-based. Range is 1 to `signature_numerator`. The beat unit size depends on the denominator.

#### `sub_division`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Sixteenth subdivision component. 1-based. Range is always 1-4. Each subdivision spans 60 ticks.

#### `ticks`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Tick component. 1-based. Range is 1-60.

---

## SmptTime

> `Live.Song.SmptTime`

Represents a time split into hours, minutes, seconds, and frames. The frame type is specified by the format passed
to `Song.get_current_smpte_song_time(format)`.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `hours` | `int` | `no` | `no` | Hour component. |
| `minutes` | `int` | `no` | `no` | Minute component. |
| `seconds` | `int` | `no` | `no` | Second component. |
| `frames` | `int` | `no` | `no` | Frame component. |

#### `hours`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Hour component of the SMPTE time value.

#### `minutes`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Minute component of the SMPTE time value.

#### `seconds`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Second component of the SMPTE time value.

#### `frames`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Frame component of the SMPTE time value.

---

## TimeFormat

> `Live.Song.TimeFormat`

Enumeration used by `Song.get_current_smpte_song_time(format)`. Values: `0`=milliseconds, `1`=Smpte24,
`2`=Smpte25, `3`=Smpte30, `4`=Smpte30Drop, `5`=Smpte29.

---

## CuePoint

> `Live.Song.CuePoint`

This class represents a locator (marker) in Live's Arrangement View. CuePoints are accessed via
`Song.cue_points` and provide a name and a time position in beats. You can call `jump()` on a CuePoint to
move the playback position to that marker.

CuePoint is defined as an inner class of `Song` in the stub (`Song.CuePoint`), but is documented as a
standalone object in the Max for Live reference under `live_set cue_points N`.

### Properties

| Property | Type    | Settable | Listenable | Summary                                                   |
| -------- | ------- | -------- | ---------- | --------------------------------------------------------- |
| `name`   | `str`   | yes      | yes        | The display name of the locator as shown in the arranger. |
| `time`   | `float` | no       | yes        | Arrangement position of the locator in beats.             |

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** yes
- **Since:** `<11`

The display name of this locator as it appears in the Arrangement View. Read/write. The listener fires when
the name is changed, either via the API or through the Live UI.

#### `time`

- **Type:** `float`
- **Listenable:** yes
- **Since:** `<11`

The position of the locator in the Arrangement, measured in beats. Read-only according to both the stub and
the Max docs. The listener fires when the marker is moved in the Arrangement View.

### Methods

| Method   | Returns | Summary                                                                   |
| -------- | ------- | ------------------------------------------------------------------------- |
| `jump()` | `None`  | Move the playback position to this locator, quantized if song is playing. |

#### `jump()`

- **Returns:** `None`
- **Args:** None
- **Raises:** Unknown
- **Since:** `<11`

Moves the Arrangement playback position to this locator's time. If the Song is currently playing, the jump is
quantized (snapped to the global quantization grid). If the Song is stopped, the start-playing position is
moved directly to the locator's time without quantization.

### Open Questions

- Is `time` truly read-only, or can it be set via the Python API? The stub docstring says "Get/Listen"
  (no "Set"), and the Max docs say `read-only`. But it would be worth probing to confirm there is no hidden
  setter.
- What happens when calling `jump()` while recording in the Arrangement -- does it interrupt the recording or
  is the call ignored?
- Can `name` be set to an empty string? If so, how does the marker appear in the Arrangement View?
- Does the `cue_points` list on Song update immediately when a marker is created or deleted in the UI, or is
  there a listener delay?

---

## CaptureDestination

> `Live.Song.CaptureDestination`

Enumeration for `Song.capture_midi(destination)`. Values: `0`=auto, `1`=session, `2`=arrangement.

---

## CaptureMode

> `Live.Song.CaptureMode`

Enumeration for `Song.capture_and_insert_scene(capture_mode)`. Values: `0`=all (default), `1`=all except selected
track. Values >= 2 fall back to `all`.

- **Quirks:** The `CaptureMode` class is not accessible as a `Song` attribute at runtime
  (`Song.CaptureMode` raises `AttributeError`).

---

## Quantization

> `Live.Song.Quantization`

Enumeration for Song clip trigger quantization values. Values: `0`=None, `1`=8 Bars, `2`=4 Bars, `3`=2 Bars,
`4`=1 Bar, `5`=1/2, `6`=1/2T, `7`=1/4, `8`=1/4T, `9`=1/8, `10`=1/8T, `11`=1/16, `12`=1/16T, `13`=1/32.

---

## RecordingQuantization

> `Live.Song.RecordingQuantization`

Enumeration for Song MIDI recording quantization values. Values: `0`=None, `1`=1/4, `2`=1/8, `3`=1/8T,
`4`=1/8+1/8T, `5`=1/16, `6`=1/16T, `7`=1/16+1/16T, `8`=1/32.

---

## SessionRecordStatus

> `Live.Song.SessionRecordStatus`

Enumeration for session recording state. Values: `0`=off, `1`=recording, `2`=triggered. Note: the value ordering
differs from `ClipSlot.playing_status` (where `1`=playing, `2`=recording).

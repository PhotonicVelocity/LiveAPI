# Song (Live API)

## Song

This class represents a Live Set. The current Live Set is reachable by the root path live_set.

### Sources

- **Primary:** `Live/classes/Song.py`
- **Secondary:** `MaxForLive/song.md`, `MaxForLive/song_view.md`, `MaxForLive/cuepoint.md`
- **Probes:** `tests/integration/test_song.py::test_song_history_unique_live_member_contracts`,
  `doc/contributing/testing.md` notes

### Probe Notes

- `can_undo` / `can_redo` visibility is asynchronous after mutations and often appears on a later application scheduler
  turn.
- `begin_undo_step()` / `end_undo_step()` groups undo-tracked actions into one undo step; grouping does not force
  non-undo-tracked actions to become undo-tracked.
- `undo()` / `redo()` return Live-managed label text; labels are UI/history/locale dependent. In current probes,
  API-originated mutations commonly report `Undo Custom Action` / `Redo Custom Action`.
- Setting `tempo` is confirmed undo-tracked in current probes.
- `jump_by()` and `scrub_by()` were observed to work while playing and while stopped, with equivalent movement behavior.
- Runtime probe (Live 12.3.5): BeatTime tick grid is `60` ticks per sixteenth, `4` sixteenths per beat, `240` ticks per
  beat. All components are **1-based** — position `0.0` beats = `1.1.1.1` (bar 1, beat 1, sixteenth 1, tick 1).
- Runtime probe (Live 12.3.5, BBST vs time signature): **The denominator affects BBST beat size.** Each BBST "beat" is
  the note value specified by the denominator: in `/4` signatures, one beat = 1.0 internal quarter-note beats; in `/8`
  signatures, one beat = 0.5 internal beats (an eighth note). Beats per bar = `signature_numerator` (always). Bar
  length in internal beats = `numerator × (4 / denominator)`. Tested across 8 signatures (4/4, 3/4, 6/8, 3/8, 7/8,
  5/4, 6/4, 12/8). See BeatTime section for full probe matrix.
- `overdub` vs `arrangement_overdub` (probed 2026-02-17): they are **distinct states**. `arrangement_overdub` is always
  settable and sticks independently. `overdub` silently ignores `set` when no track is armed / no session recording is
  active — it controls session MIDI overdub, not arrangement overdub despite the stub's misleading description.
  `record_mode` and `session_record` also silently ignore `set` without an armed track.
- Runtime probe (Live 12.3.5): `set_data(key, None)` followed by `get_data(key, default)` returns `None` rather than
  `default`.
- Not all actions are undo-tracked.
- Undo/redo history is global to the Live document, not scoped to one script client.

### Open Questions

- ~~Full numeric mapping for `Song.CaptureMode`.~~ **Resolved (probed, Live 12.3.5):** `0`=all, `1`=all except selected track. Values ≥2 fall back to `all`.
- ~~Numeric mapping for `Song.SessionRecordStatus`.~~ **Resolved (probed, Live 12.3.5):** `0`=off, `1`=recording, `2`=triggered.
- Member-by-member matrix of which mutating Song actions are undo-tracked vs non-undo-tracked.

### Children

| Child            | Returns              | Shape    | Access | Listenable | Available Since | Summary                                                                                                                  |
| ---------------- | -------------------- | -------- | ------ | ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `cue_points`     | `Sequence[CuePoint]` | `list`   | `get`  | `yes`      | `<11`           | Cue points are the markers in the Arrangement to which you can jump.                                                     |
| `return_tracks`  | `Sequence[Track]`    | `list`   | `get`  | `yes`      | `<11`           | return_tracks child.                                                                                                     |
| `scenes`         | `Sequence[Scene]`    | `list`   | `get`  | `yes`      | `<11`           | scenes child.                                                                                                            |
| `tracks`         | `Sequence[Track]`    | `list`   | `get`  | `yes`      | `<11`           | tracks child.                                                                                                            |
| `visible_tracks` | `Sequence[Track]`    | `list`   | `get`  | `yes`      | `<11`           | A track is visible if it's not part of a folded group. If a track is scrolled out of view it's still considered visible. |
| `master_track`   | `Track`              | `single` | `get`  | `no`       | `<11`           | master_track child.                                                                                                      |
| `view`           | `Song.View`          | `single` | `get`  | `no`       | `<11`           | view child.                                                                                                              |
| `groove_pool`    | `GroovePool`         | `single` | `get`  | `no`       | `11.0`          | Live's groove pool.                                                                                                      |
| `tuning_system`  | `TuningSystem`       | `single` | `get`  | `yes`      | `12.0`          | Live's currently active tuning system.                                                                                   |

#### `cue_points`

- **Returns:** `Sequence[CuePoint]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Cue points are the markers in the Arrangement to which you can jump.

#### `return_tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** return_tracks child.

#### `scenes`

- **Returns:** `Sequence[Scene]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** scenes child.

#### `tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** tracks child.

#### `visible_tracks`

- **Returns:** `Sequence[Track]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** A track is visible if it's not part of a folded group. If a track is scrolled out of view it's still
considered visible.

#### `master_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** master_track child.

#### `view`

- **Returns:** `Song.View`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** view child.

#### `groove_pool`

- **Returns:** `GroovePool`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `11.0`

**Description:** Live's groove pool. _Available since Live 11.0._

#### `tuning_system`

- **Returns:** `TuningSystem`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `12.0`

**Description:** Live's currently active tuning system.

### Properties

| Property                                  | Get Returns                  | Set Accepts                  | Listenable | Available Since | Summary                                                                                                                                                                                                                                       |
| ----------------------------------------- | ---------------------------- | ---------------------------- | ---------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_live_ptr`                               | `Unknown`                    | —                            | `no`       | `<11`           | \_live_ptr property.                                                                                                                                                                                                                          |
| `appointed_device`                        | `Device`                     | —                            | `yes`      | `<11`           | The appointed device is the one used by a control surface unless the control surface itself chooses which device to use. It is marked by a blue hand.                                                                                         |
| `arrangement_overdub`                     | `bool`                       | `bool`                       | `yes`      | `<11`           | Get/set the state of the MIDI Arrangement Overdub button.                                                                                                                                                                                     |
| `back_to_arranger`                        | `bool`                       | `bool`                       | `yes`      | `<11`           | Get/set/observe the current state of the Back to Arrangement button located in Live's transport bar (1 = highlighted). This button is used to indicate that the current state of the playback differs from what is stored in the Arrangement. |
| `can_capture_midi`                        | `bool`                       | —                            | `yes`      | `<11`           | 1 = Recently played MIDI material exists that can be captured into a Live Track. See _capture_midi_.                                                                                                                                          |
| `can_jump_to_next_cue`                    | `bool`                       | —                            | `yes`      | `<11`           | 0 = there is no cue point to the right of the current one, or none at all.                                                                                                                                                                    |
| `can_jump_to_prev_cue`                    | `bool`                       | —                            | `yes`      | `<11`           | 0 = there is no cue point to the left of the current one, or none at all.                                                                                                                                                                     |
| `can_redo`                                | `bool`                       | —                            | `no`       | `<11`           | 1 = there is something in the history to redo.                                                                                                                                                                                                |
| `can_undo`                                | `bool`                       | —                            | `no`       | `<11`           | 1 = there is something in the history to undo.                                                                                                                                                                                                |
| `canonical_parent`                        | `Unknown`                    | —                            | `no`       | `<11`           | Get the canonical parent of the song.                                                                                                                                                                                                         |
| `clip_trigger_quantization`               | `Song.Quantization`          | `Song.Quantization`          | `yes`      | `<11`           | Reflects the quantization setting in the transport bar.                                                                                                                                                                                       |
| `count_in_duration`                       | `int`                        | —                            | `yes`      | `<11`           | The duration of the Metronome's Count-In setting as an index, mapped as follows:                                                                                                                                                              |
| `current_song_time`                       | `float`                      | `float`                      | `yes`      | `<11`           | The playing position in the Live Set, in beats.                                                                                                                                                                                               |
| `exclusive_arm`                           | `bool`                       | —                            | `no`       | `<11`           | Current status of the exclusive Arm option set in the Live preferences.                                                                                                                                                                       |
| `exclusive_solo`                          | `bool`                       | —                            | `no`       | `<11`           | Current status of the exclusive Solo option set in the Live preferences.                                                                                                                                                                      |
| `file_path`                               | `symbol`                     | —                            | `no`       | `11.3`          | The path to the current Live Set, in OS-native format. If the Live Set hasn't been saved, the path is empty.                                                                                                                                  |
| `groove_amount`                           | `float`                      | `float`                      | `yes`      | `<11`           | The groove amount from the current set's groove pool (0. - 1.0).                                                                                                                                                                              |
| `is_ableton_link_enabled`                 | `bool`                       | `bool`                       | `yes`      | `11.1`          | Enable/disable Ableton Link. The Link toggle in the Live's transport bar must be visible to enable Link.                                                                                                                                      |
| `is_ableton_link_start_stop_sync_enabled` | `bool`                       | `bool`                       | `yes`      | `11.1`          | Enable/disable Ableton Link Start Stop Sync.                                                                                                                                                                                                  |
| `is_counting_in`                          | `bool`                       | —                            | `yes`      | `<11`           | 1 = the Metronome is currently counting in.                                                                                                                                                                                                   |
| `is_playing`                              | `bool`                       | `bool`                       | `yes`      | `<11`           | Get/set if Live's transport is running.                                                                                                                                                                                                       |
| `last_event_time`                         | `float`                      | —                            | `no`       | `<11`           | The beat time of the last event (i.e. automation breakpoint, clip end, cue point, loop end) in the Arrangement.                                                                                                                               |
| `loop`                                    | `bool`                       | `bool`                       | `yes`      | `<11`           | Get/set the enabled state of the Arrangement loop.                                                                                                                                                                                            |
| `loop_length`                             | `float`                      | `float`                      | `yes`      | `<11`           | Arrangement loop length in beats.                                                                                                                                                                                                             |
| `loop_start`                              | `float`                      | `float`                      | `yes`      | `<11`           | Arrangement loop start in beats.                                                                                                                                                                                                              |
| `metronome`                               | `bool`                       | `bool`                       | `yes`      | `<11`           | Get/set the enabled state of the metronome.                                                                                                                                                                                                   |
| `midi_recording_quantization`             | `Song.RecordingQuantization` | `Song.RecordingQuantization` | `yes`      | `<11`           | Get/set the current Record Quantization value.                                                                                                                                                                                                |
| `name`                                    | `symbol`                     | —                            | `no`       | `11.3`          | The name of the current Live Set. If the Live Set hasn't been saved, the name is empty.                                                                                                                                                       |
| `nudge_down`                              | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Tempo Nudge Down button in the transport bar is currently pressed.                                                                                                                                                                    |
| `nudge_up`                                | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Tempo Nudge Up button in the transport bar is currently pressed.                                                                                                                                                                      |
| `overdub`                                 | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = MIDI Arrangement Overdub is enabled in the transport.                                                                                                                                                                                     |
| `punch_in`                                | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Punch-In button is enabled in the transport.                                                                                                                                                                                          |
| `punch_out`                               | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Punch-Out button is enabled in the transport.                                                                                                                                                                                         |
| `re_enable_automation_enabled`            | `bool`                       | —                            | `yes`      | `<11`           | 1 = the Re-Enable Automation button is on.                                                                                                                                                                                                    |
| `record_mode`                             | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Arrangement Record button is on.                                                                                                                                                                                                      |
| `root_note`                               | `int`                        | `int`                        | `yes`      | `<11`           | The root note of the scale currently selected in Live. The root note can be a number between 0 and 11, where 0 = C and 11 = B.                                                                                                                |
| `scale_intervals`                         | `list`                       | —                            | `yes`      | `<11`           | A list of integers representing the intervals in Live's current scale (see _scale_name_ and _scale_mode_). An interval is expressed as the difference between the scale degree at the list index and the first scale degree.                  |
| `scale_mode`                              | `bool`                       | `bool`                       | `yes`      | `12.0`          | Access to the Scale Mode setting in Live.                                                                                                                                                                                                     |
| `scale_name`                              | `unicode`                    | `unicode`                    | `yes`      | `<11`           | The name of the scale selected in Live, as displayed in the Current Scale Name chooser.                                                                                                                                                       |
| `select_on_launch`                        | `bool`                       | —                            | `no`       | `<11`           | 1 = the "Select on Launch" option is set in Live's preferences.                                                                                                                                                                               |
| `session_automation_record`               | `bool`                       | `bool`                       | `yes`      | `<11`           | The state of the Automation Arm button.                                                                                                                                                                                                       |
| `session_record_status`                   | `Song.SessionRecordStatus`   | —                            | `yes`      | `<11`           | Session slot-recording state: `0`=off, `1`=recording, `2`=triggered.                                                                                                                                                                          |
| `signature_denominator`                   | `int`                        | `int`                        | `yes`      | `<11`           | Get/Set access to the global signature denominator of the Song.                                                                                                                                                                               |
| `signature_numerator`                     | `int`                        | `int`                        | `yes`      | `<11`           | Get/Set access to the global signature numerator of the Song.                                                                                                                                                                                 |
| `song_length`                             | `float`                      | —                            | `yes`      | `<11`           | A little more than last_event_time, in beats.                                                                                                                                                                                                 |
| `start_time`                              | `float`                      | `float`                      | `yes`      | `11.1`          | The position in the Live Set where playing will start, in beats.                                                                                                                                                                              |
| `swing_amount`                            | `float`                      | `float`                      | `yes`      | `<11`           | Range: 0.0 - 1.0; affects MIDI Recording Quantization and all direct calls to Clip.quantize.                                                                                                                                                  |
| `tempo`                                   | `float`                      | `float`                      | `yes`      | `<11`           | Current tempo of the Live Set in BPM, 20.0 ... 999.0. The tempo may be automated, so it can change depending on the current song time.                                                                                                        |
| `tempo_follower_enabled`                  | `bool`                       | `bool`                       | `yes`      | `<11`           | 1 = the Tempo Follower controls the tempo. The Tempo Follower Toggle must be made visible in the preferences for this property to be effective.                                                                                               |
| `session_record`                          | `bool`                       | `bool`                       | `yes`      | `<11`           | The state of the Session Overdub button.                                                                                                                                                                                                      |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** \_live_ptr property.

#### `appointed_device`

- **Get Returns:** `Device`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The appointed device is the one used by a control surface unless the control surface itself chooses
which device to use. It is marked by a blue hand in the UI.

**Probe Notes (12.3.5, MS33):** `appointed_device` is independent from both the selected device (white outline)
and `Browser.hotswap_target`. Setting `hotswap_target` does not change `appointed_device`, and vice versa.
See `Song.View.select_device()` for the distinction between selection and appointment.

#### `arrangement_overdub`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set the state of the MIDI Arrangement Overdub button. When enabled, existing notes in MIDI clips in
the Arrangement will be mixed with, rather than replaced by, newly recorded notes. Always settable independently — does
not require `record_mode` or an armed track. Distinct from `overdub` (which is session MIDI overdub). See probe notes.

#### `back_to_arranger`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set/observe the current state of the Back to Arrangement button located in Live's transport bar (1
= highlighted). This button is used to indicate that the current state of the playback differs from what is stored in
the Arrangement. Setting this property to 0 will make Live go back to playing the content of the arrangement.

#### `can_capture_midi`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = Recently played MIDI material exists that can be captured into a Live Track. See _capture_midi_.

#### `can_jump_to_next_cue`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 0 = there is no cue point to the right of the current one, or none at all.

#### `can_jump_to_prev_cue`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 0 = there is no cue point to the left of the current one, or none at all.

#### `can_redo`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = there is something in the history to redo. Visibility may update on a later scheduler turn after
stack mutations.

#### `can_undo`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = there is something in the history to undo. Visibility may update on a later scheduler turn after
stack mutations.

#### `canonical_parent`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the canonical parent of the song.

#### `clip_trigger_quantization`

- **Get Returns:** `Song.Quantization`
- **Set Accepts:** `Song.Quantization`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The global launch quantization setting in the transport bar (`Song.Quantization`). Quantization is used
to avoid rhythmical error when playing clips. It also determines when playback will begin when using Link. 0 = None 1 =
8 Bars 2 = 4 Bars 3 = 2 Bars 4 = 1 Bar 5 = 1/2 6 = 1/2T 7 = 1/4 8 = 1/4T 9 = 1/8 10 = 1/8T 11 = 1/16 12 = 1/16T
13 = 1/32

#### `count_in_duration`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The duration of the Metronome's Count-In setting as an index, mapped as follows: 0 = None 1 = 1 Bar 2 =
2 Bars 3 = 4 Bars

#### `current_song_time`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `no`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The playing position in the Live Set, in beats.

#### `exclusive_arm`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Current status of the exclusive Arm option set in the Live preferences.

#### `exclusive_solo`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Current status of the exclusive Solo option set in the Live preferences.

#### `file_path`

- **Get Returns:** `symbol`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `11.3`

**Description:** The path to the current Live Set, in OS-native format. If the Live Set hasn't been saved, the path is
empty.

#### `groove_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The Global Groove Amount from the current set's groove pool (0.0 – 1.0). Scales the overall intensity
of Timing, Random, and Velocity for all grooves in the Pool. At 1.0 (100%), each groove's parameters are applied at
their assigned values. Values above 1.0 push parameters beyond their assigned values.

#### `is_ableton_link_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.1`

**Description:** Enable/disable Ableton Link. The Link toggle in Live's transport bar must be visible to enable Link.
When enabled, the button displays the number of connected Link-enabled devices. If external sync or Tempo Follower is
active, Link follows the external source and sends timing information to all connected peers. See also
`is_ableton_link_start_stop_sync_enabled`.

#### `is_ableton_link_start_stop_sync_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.1`

**Description:** Enable/disable Ableton Link Start Stop Sync. When enabled, start and stop commands are synced across
all connected apps that also have Start Stop Sync enabled.

#### `is_counting_in`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Metronome is currently counting in.

#### `is_playing`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set if Live's transport is running.

#### `last_event_time`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The beat time of the last event (i.e. automation breakpoint, clip end, cue point, loop end) in the
Arrangement.

#### `loop`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set the enabled state of the Arrangement loop.

#### `loop_length`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Arrangement loop length in beats.

#### `loop_start`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Arrangement loop start in beats.

#### `metronome`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set the enabled state of the metronome. The metronome's volume is controlled by the Preview/Cue
Volume knob in the Main track's mixer. See also `count_in_duration` for the count-in setting.

#### `midi_recording_quantization`

- **Get Returns:** `Song.RecordingQuantization`
- **Set Accepts:** `Song.RecordingQuantization`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/set the current Record Quantization value (`Song.RecordingQuantization`). 0 = None 1 = 1/4 2 = 1/8
3 = 1/8T 4 = 1/8 + 1/8T 5 = 1/16 6 = 1/16T 7 = 1/16 + 1/16T 8 = 1/32

#### `name`

- **Get Returns:** `symbol`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `11.3`

**Description:** The name of the current Live Set. If the Live Set hasn't been saved, the name is empty.

#### `nudge_down`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Tempo Nudge Down button in the transport bar is currently pressed. Temporarily decreases song
tempo to synchronize to external music.

#### `nudge_up`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Tempo Nudge Up button in the transport bar is currently pressed. Temporarily increases song
tempo to synchronize to external music.

#### `overdub`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Session MIDI overdub toggle. Setting to `True` silently does nothing unless
a track is armed and session recording is active. Distinct from `arrangement_overdub` (which
is always settable). Despite the stub description mentioning "Arrangement Overdub", probing
confirms this controls session overdub behavior. See probe notes.

#### `punch_in`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Punch-In button is enabled in the transport. Prevents Arrangement recording prior to the
punch-in point, which is defined by the left edge of the loop brace.

#### `punch_out`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Punch-Out button is enabled in the transport. Prevents Arrangement recording after the
punch-out point, which is defined by the right edge of the loop brace.

#### `re_enable_automation_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Re-Enable Automation button is on. This is only `True` when at least one automated parameter
has been manually overridden. See `re_enable_automation()`.

#### `record_mode`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Arrangement Record button is on. If the "Start Transport With Record" preference is enabled
(Record, Warp & Launch Settings), setting this to `True` will also start the transport. When the preference is off, the
transport will not start until `start_playing()` is called or a Session clip is launched. Setting to `False` does not
stop playback. See also `trigger_session_record`.

#### `root_note`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The root note of the scale currently selected in Live. The root note can be a number between 0 and 11,
where 0 = C and 11 = B.

#### `scale_intervals`

- **Get Returns:** `list`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** A list of integers representing the intervals in Live's current scale (see _scale_name_ and
_scale_mode_). An interval is expressed as the difference between the scale degree at the list index and the first scale
degree.

#### `scale_mode`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `12.0`

**Description:** Access to the Scale Mode setting in Live. When enabled, the `root_note` and `scale_name` reflect the
active scale in selected clips, and can also be used to set a scale for new clips or change the scale of existing
selected clips. Key tracks that belong to the currently selected scale are highlighted in Live's MIDI Note Editor, and
pitch-based parameters in MIDI Tools and Devices can be edited in scale degrees rather than semitones. See also
_root_note_, _scale_name_, and _scale_intervals_.

#### `scale_name`

- **Get Returns:** `unicode`
- **Set Accepts:** `unicode`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The name of the scale selected in Live, as displayed in the Current Scale Name chooser.

#### `select_on_launch`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the "Select on Launch" option is set in Live's preferences.

#### `session_automation_record`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `next_tick`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The state of the Automation Arm button. When enabled, manual parameter changes can be recorded to
Session clips and the Arrangement. The "Record Session Automation" preference determines whether automation is recorded
in all playing clips or only in armed tracks. Automation in Session clips is always recorded to the Arrangement, as are
any manual changes to parameters in tracks recorded from the Session.

#### `session_record_status`

- **Get Returns:** `Song.SessionRecordStatus`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the session slot-recording state (`Song.SessionRecordStatus`). Probed values
(Live 12.3.5): `0` = off (no session slot-recording active), `1` = recording (actively recording
into a session slot), `2` = triggered (recording queued, waiting for launch quantization to start).
During the triggered phase (`status == 2`), `session_record` remains `False` and the target slot
reports `is_triggered = True`. Once the quantization boundary is reached, status transitions to `1`,
`session_record` becomes `True`, and the slot reports `is_recording = True`.

#### `signature_denominator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set access to the global signature denominator of the Song. The denominator determines the BBST
beat unit size: `/4` → one BBST beat = 1 quarter-note beat (1.0 internal beats); `/8` → one BBST beat = 1 eighth-note
beat (0.5 internal beats). Formula: `beat_unit = 4 / denominator` internal beats. See BeatTime section.

#### `signature_numerator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set access to the global signature numerator of the Song. The numerator determines the number of
BBST beats per bar. Bar length in internal beats = `numerator × (4 / denominator)`. See BeatTime section.

#### `song_length`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** A little more than last_event_time, in beats.

#### `start_time`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.1`

**Description:** The position in the Live Set where playing will start, in beats.

#### `swing_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Range: 0.0 - 1.0; affects MIDI Recording Quantization and all direct calls to Clip.quantize.

#### `tempo`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Current tempo of the Live Set in BPM, 20.0 ... 999.0. The tempo may be automated, so it can change
depending on the current song time. In current probes, setting tempo creates an undo-tracked step.

#### `tempo_follower_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the Tempo Follower controls the tempo. The Tempo Follower Toggle must be made visible in the
preferences for this property to be effective.

#### `session_record`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The state of the Session Record / Overdub button. When enabled, overdub recording is active for
currently playing clips on armed tracks — in MIDI clips both notes and automation are overdubbed, in audio clips only
automation. With the "Start Transport With Record" preference disabled, this only affects already-playing clips and does
not start playback or create new clips. With the preference enabled, setting this to `True` also starts recording into
the selected scene's slots on all armed tracks. Needs probing to confirm the API (`set`) behaves identically to the
UI button.

### Methods

| Signature                                                                           | Returns                              | Available Since | Summary                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------- | ------------------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `__init__(*a, **k)`                                                                 | `Unknown`                            | `N/A`           | This class represents a Live set.                                                                                                                                                                      |
| `begin_undo_step()`                                                                 | `None`                               | `<11`           | Begin an undo group for subsequent undo-tracked actions.                                                                                                                                               |
| `capture_and_insert_scene(capture_mode: Song.CaptureMode = Song.CaptureMode.all)`   | `None`                               | `<11`           | Capture playing clips into a new scene below selected scene. `0`=all, `1`=all except selected track.                                                                                                   |
| `capture_midi(destination: Song.CaptureDestination = Song.CaptureDestination.auto)` | `None`                               | `<11`           | 0 = auto, 1 = session, 2 = arrangement                                                                                                                                                                 |
| `continue_playing()`                                                                | `None`                               | `<11`           | From the current playback position.                                                                                                                                                                    |
| `create_audio_track(Index: object)`                                                 | `Track`                              | `<11`           | Index determines where the track is added, it is only valid between 0 and len(song.tracks). Using an index of -1 will add the new track at the end of the list.                                        |
| `create_midi_track(Index: object)`                                                  | `Track`                              | `<11`           | Index determines where the track is added, it is only valid between 0 and len(song.tracks). Using an index of -1 will add the new track at the end of the list.                                        |
| `create_return_track()`                                                             | `Track`                              | `<11`           | Adds a new return track at the end.                                                                                                                                                                    |
| `create_scene(arg2: int)`                                                           | `Scene`                              | `<11`           | Index determines where the scene is added. It is only valid between 0 and len(song.scenes). Using an index of -1 will add the new scene at the end of the list.                                        |
| `delete_return_track(arg2: int)`                                                    | `None`                               | `<11`           | Delete the return track at the given index.                                                                                                                                                            |
| `delete_scene(arg2: int)`                                                           | `None`                               | `<11`           | Delete the scene at the given index.                                                                                                                                                                   |
| `delete_track(arg2: int)`                                                           | `None`                               | `<11`           | Delete the track at the given index.                                                                                                                                                                   |
| `duplicate_scene(arg2: int)`                                                        | `None`                               | `<11`           | Index determines which scene to duplicate.                                                                                                                                                             |
| `duplicate_track(arg2: int)`                                                        | `None`                               | `<11`           | Index determines which track to duplicate.                                                                                                                                                             |
| `end_undo_step()`                                                                   | `None`                               | `<11`           | End the current undo group and commit grouped actions as one step.                                                                                                                                     |
| `find_device_position(device: Device, target: LomObject, target_position: int)`     | `int`                                | `<11`           | device [live object]                                                                                                                                                                                   |
| `force_link_beat_time()`                                                            | `None`                               | `<11`           | Force the Link timeline to jump to Live's current beat time.                                                                                                                                           |
| `get_beats_loop_length()`                                                           | `Song.BeatTime`                      | `<11`           | The Arrangement loop length.                                                                                                                                                                           |
| `get_beats_loop_start()`                                                            | `Song.BeatTime`                      | `<11`           | The Arrangement loop start.                                                                                                                                                                            |
| `get_current_beats_song_time()`                                                     | `Song.BeatTime`                      | `<11`           | The current Arrangement playback position.                                                                                                                                                             |
| `get_current_smpte_song_time(format: Song.TimeFormat)`                              | `Song.SmptTime`                      | `<11`           | format [Song.TimeFormat] selects the time code type to be returned                                                                                                                                     |
| `get_data(key: object, default_value: object)`                                      | `object`                             | `<11`           | Get data for the given key, that was previously stored using set_data. C++ signature : boost::python::api::object get_data(TPyHandle<ASong>,TString,boost::python::api::object)                        |
| `is_cue_point_selected()`                                                           | `bool`                               | `<11`           | Return true if the global playing pos is currently on a cue point. C++ signature : bool is_cue_point_selected(TPyHandle<ASong>)                                                                        |
| `jump_by(arg2: float)`                                                              | `None`                               | `<11`           | beats [float] is the amount to jump relatively to the current position                                                                                                                                 |
| `jump_to_next_cue()`                                                                | `None`                               | `<11`           | Jump to the right, if possible.                                                                                                                                                                        |
| `jump_to_prev_cue()`                                                                | `None`                               | `<11`           | Jump to the left, if possible.                                                                                                                                                                         |
| `move_device(device: Device, target: LomObject, target_position: int)`              | `int`                                | `<11`           | device [live object]                                                                                                                                                                                   |
| `play_selection()`                                                                  | `None`                               | `<11`           | Do nothing if no selection is set in Arrangement, or play the current selection.                                                                                                                       |
| `re_enable_automation()`                                                            | `None`                               | `<11`           | Trigger 'Re-Enable Automation', re-activating automation in all running Session clips.                                                                                                                 |
| `redo()`                                                                            | `str`                                | `<11`           | Redo last undone action and return Live-provided label text.                                                                                                                                           |
| `scrub_by(arg2: float)`                                                             | `None`                               | `<11`           | beats [float] the amount to scrub relative to the current Arrangement playback position                                                                                                                |
| `set_data(key: object, value: object)`                                              | `None`                               | `<11`           | Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set. C++ signature : void set_data(TPyHandle<ASong>,TString,boost::python::api::object) |
| `set_or_delete_cue()`                                                               | `None`                               | `<11`           | Toggle cue point at current Arrangement playback position.                                                                                                                                             |
| `start_playing()`                                                                   | `None`                               | `<11`           | Start playback from the insert marker.                                                                                                                                                                 |
| `stop_all_clips(Quantized: bool)`                                                   | `None`                               | `<11`           | Parameter (optional): quantized                                                                                                                                                                        |
| `stop_playing()`                                                                    | `None`                               | `<11`           | Stop the playback.                                                                                                                                                                                     |
| `tap_tempo()`                                                                       | `None`                               | `<11`           | Same as pressing the Tap Tempo button in the transport bar. The new tempo is calculated based on the time between subsequent calls of this function.                                                   |
| `trigger_session_record(record_length: float)`                                      | `None`                               | `<11`           | Starts recording in either the selected slot or the next empty slot, if the track is armed. If _record_length_ is provided, the slot will record for the given length in beats.                        |
| `undo()`                                                                            | `str`                                | `<11`           | Undo last action and return Live-provided label text.                                                                                                                                                  |
| `get_all_scales_ordered()`                                                          | `tuple[tuple[str, tuple[int, ...]]]` | `N/A`           | Static method. Returns ordered tuple of all available `(scale_name, intervals)` pairs.                                                                                                                 |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** `*a, **k`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** This class represents a Live set.

#### `begin_undo_step()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Opens an undo-group boundary for subsequent undo-tracked actions.`
- **Async visibility:** `variable`
- **Available Since:** `<11`

**Description:** Begins an undo group. This does not force non-undo-tracked actions to become undo-tracked.

#### `capture_and_insert_scene(capture_mode: Song.CaptureMode = Song.CaptureMode.all)`

- **Returns:** `None`
- **Args:** `capture_mode: Song.CaptureMode = Song.CaptureMode.all`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Capture the currently playing clips and insert them as a new scene below the selected scene.
The new scene is inserted immediately below the currently selected scene, and selection moves to
the new scene after capture. Captures clips from all tracks regardless of which scenes they are
playing from — the clips are duplicated into a single new scene row. Playback switches to the
newly inserted scene (captured clips begin playing from the new scene row). Track arm state has
no effect on capture behavior.

Probed `CaptureMode` values (Live 12.3.5):

- `0` (`all`, default) — capture all playing clips.
- `1` (`all_except_selected`) — capture all playing clips except the clip on the selected track.
  The excluded track stops playing (no clip in the new scene). Useful for re-recording one track
  while preserving the rest.
- Values ≥ 2 and negative values all fall back to `all` behavior.
- Arm state does not affect which tracks are captured for any mode.

#### `capture_midi(destination: Song.CaptureDestination = Song.CaptureDestination.auto)`

- **Returns:** `None`
- **Args:** `destination: Song.CaptureDestination = Song.CaptureDestination.auto`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: destination [Song.CaptureDestination] 0 = auto, 1 = session, 2 = arrangement. Capture
recently played MIDI material from audible tracks into a Live Clip. "Recently played" refers to MIDI input from
controllers/keyboards — Live keeps a rolling buffer of incoming MIDI on tracks that were monitoring input. If
_destination_ is not set or is set to _auto_, the Clip is inserted into the view currently visible in the focused Live
window. Otherwise, it is inserted into the specified view. If the transport is stopped, the Set's tempo updates to match
the detected tempo of the playing. If the transport is running or the tempo is synced or automated, the tempo remains
unchanged. Can also be called while a clip is playing to add notes to an existing clip. See `can_capture_midi`.

**Needs probing:** Exact placement behavior — which scene receives the clip in session mode? Does it create a new scene
or use the selected scene? Does it create clips on all tracks that received MIDI input, or only armed tracks?

#### `continue_playing()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** From the current playback position.

#### `create_audio_track(Index: object)`

- **Returns:** `Track`
- **Args:** `Index: object`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Index determines where the track is added, it is only valid between 0 and
len(song.tracks). Using an index of -1 will add the new track at the end of the list.

#### `create_midi_track(Index: object)`

- **Returns:** `Track`
- **Args:** `Index: object`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Index determines where the track is added, it is only valid between 0 and
len(song.tracks). Using an index of -1 will add the new track at the end of the list.

#### `create_return_track()`

- **Returns:** `Track`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Adds a new return track at the end.

#### `create_scene(arg2: int)`

- **Returns:** `Scene`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `yes`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Returns: The new scene Index determines where the scene is added. It is only valid
between 0 and len(song.scenes). Using an index of -1 will add the new scene at the end of the list.

#### `delete_return_track(arg2: int)`

- **Returns:** `None`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Delete the return track at the given index.

#### `delete_scene(arg2: int)`

- **Returns:** `None`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Delete the scene at the given index.

#### `delete_track(arg2: int)`

- **Returns:** `None`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Delete the track at the given index.

#### `duplicate_scene(arg2: int)`

- **Returns:** `None`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Index determines which scene to duplicate.

#### `duplicate_track(arg2: int)`

- **Returns:** `None`
- **Args:** `arg2: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: index Index determines which track to duplicate.

#### `end_undo_step()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Closes the current undo-group boundary and commits grouped undo-tracked actions as one step.`
- **Async visibility:** `variable`
- **Available Since:** `<11`

**Description:** Ends the current undo group.

#### `find_device_position(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int`
- **Args:** `device: Device, target: LomObject, target_position: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `N/A` (read-only query)
- **Side Effects:** None — dry-run only.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Probe Status:** `probed 12.3.5`

**Description:** Queries the nearest valid insertion position without actually moving the device. Returns the
position in the target's device chain where the device can be inserted closest to `target_position`. Target can
be a `Track` or `Chain`.

**Probe Results:** Works for both track and chain targets. Returns `0` for position `0` on empty targets.
Useful for validating `move_device` targets before performing the move.

#### `force_link_beat_time()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Force the Link timeline to jump to Live's current beat time.

#### `get_beats_loop_length()`

- **Returns:** `Song.BeatTime`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Returns: bars.beats.sixteenths.ticks [symbol] The Arrangement loop length.

#### `get_beats_loop_start()`

- **Returns:** `Song.BeatTime`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Returns: bars.beats.sixteenths.ticks [symbol] The Arrangement loop start.

#### `get_current_beats_song_time()`

- **Returns:** `Song.BeatTime`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Returns: bars.beats.sixteenths.ticks [symbol] The current Arrangement playback position.

#### `get_current_smpte_song_time(format: Song.TimeFormat)`

- **Returns:** `Song.SmptTime`
- **Args:** `format: Song.TimeFormat`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: format [Song.TimeFormat] selects the time code type to be returned 0 = the frame position
shows the milliseconds 1 = Smpte24 2 = Smpte25 3 = Smpte30 4 = Smpte30Drop 5 = Smpte29 Returns: _hours:min:sec_ [symbol]
The current Arrangement playback position.

#### `get_data(key: object, default_value: object)`

- **Returns:** `object`
- **Args:** `key: object, default_value: object`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Get data for the given key, that was previously stored using set_data. C++ signature :
boost::python::api::object get_data(TPyHandle<ASong>,TString,boost::python::api::object)

In current probes (Live 12.3.5), after `set_data(key, None)`, `get_data(key, default_value)` returned `None` rather than
the provided default.

#### `is_cue_point_selected()`

- **Returns:** `bool`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Returns: bool 1 = the current Arrangement playback position is at a cue point

#### `jump_by(arg2: float)`

- **Returns:** `None`
- **Args:** `arg2: float`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: beats beats [float] is the amount to jump relatively to the current position.

Observed in current probes to work while playing and while stopped.

#### `jump_to_next_cue()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Jump to the right, if possible.

#### `jump_to_prev_cue()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Jump to the left, if possible.

#### `move_device(device: Device, target: LomObject, target_position: int)`

- **Returns:** `int`
- **Args:** `device: Device, target: LomObject, target_position: int`
- **Raises/Errors:** Raises `InternalError: Couldn't move device. target_index out of range.` if `target_position`
  is invalid (e.g. `-1`). Use `len(chain.devices)` to append, or `find_device_position()` to validate.
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes the device from its current location and inserts it at the target.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Probe Status:** `probed 12.3.5`

**Description:** Moves a device to the specified position in the target's device chain. Target can be a `Track` or
`Chain`. Returns the actual insertion position (may differ from `target_position` if the exact position is not valid —
the nearest possible position is chosen).

**Probe Results:** Works for moving devices between tracks, from tracks into chains, and into arbitrarily nested
rack chains. Tested with both native devices and M4L devices (`MxDeviceAudioEffect`). Position must be a valid
non-negative index — use the chain's current device count to append. No observed side effects on view selection state.

#### `play_selection()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Do nothing if no selection is set in Arrangement, or play the current selection.

#### `re_enable_automation()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Trigger 'Re-Enable Automation', re-enabling automation for any parameters that are currently overridden
in the Arrangement or in Session clips. Only has an effect when `re_enable_automation_enabled` is `True`.

#### `redo()`

- **Returns:** `str`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Reapplies the last undone action and updates the global undo/redo stack.`
- **Async visibility:** `variable`
- **Available Since:** `<11`

**Description:** Causes the Live application to redo the last operation and returns the full Live-provided redo label text.
In current probes, API-originated mutations commonly return `Redo Custom Action`.

#### `scrub_by(arg2: float)`

- **Returns:** `None`
- **Args:** `arg2: float`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: beats beats [float] the amount to scrub relative to the current Arrangement playback
position. Same as `jump_by`, at the moment.

Observed in current probes to work while playing and while stopped, with equivalent movement behavior to `jump_by`.

#### `set_data(key: object, value: object)`

- **Returns:** `None`
- **Args:** `key: object, value: object`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Store data for the given key in this object. The data is persistent and will be restored when loading
the Live Set. C++ signature : void set_data(TPyHandle<ASong>,TString,boost::python::api::object)

#### `set_or_delete_cue()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Toggle cue point at current Arrangement playback position.

#### `start_playing()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Start playback from the insert marker.

#### `stop_all_clips(Quantized: bool)`

- **Returns:** `None`
- **Args:** `Quantized: bool`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter (optional): quantized Calling the function with 0 will stop all clips immediately,
independent of the launch quantization. The default is '1'.

#### `stop_playing()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Stop the playback.

#### `tap_tempo()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Same as pressing the Tap Tempo button in the transport bar. The new tempo is calculated based on the
time between subsequent calls of this function. If the "Start Playback with Tap Tempo" preference is enabled, calling
this function can also count in and start playback (e.g. four taps in 4/4 time).

#### `trigger_session_record(record_length: float)`

- **Returns:** `None`
- **Args:** `record_length: float`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: record*length (optional). Equivalent to pressing the Session Record button. Starts recording
in either the selected slot or the next empty slot, if the track is armed. Always starts the transport (not affected by
the "Start Transport With Record" preference). Complete no-op when no track is armed. If \_record_length* is provided,
the slot will record for the given length in beats. If triggered while recording, recording will stop and clip playback
will start.

#### `undo()`

- **Returns:** `str`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Reverts the last undo-tracked action and updates the global undo/redo stack.`
- **Async visibility:** `variable`
- **Available Since:** `<11`

**Description:** Causes the Live application to undo the last operation and returns the full Live-provided undo label text.
In current probes, API-originated mutations commonly return `Undo Custom Action`.

#### `get_all_scales_ordered()`

- **Returns:** `tuple[tuple[str, tuple[int, ...]]]`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None`
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:** Static method. Returns an ordered tuple of `(scale_name, intervals)` pairs for all scales available in
Live. Each `intervals` value is a tuple of integers representing the half-step intervals of the scale (e.g. Major = `(0,
2, 4, 5, 7, 9, 11)`).

## Song.View

This class represents the view aspects of a Live document: the Session and Arrangement views.

### Children

| Child                   | Returns           | Shape    | Access    | Listenable | Available Since | Summary                                                      |
| ----------------------- | ----------------- | -------- | --------- | ---------- | --------------- | ------------------------------------------------------------ |
| `detail_clip`           | `Clip`            | `single` | `get/set` | `yes`      | `<11`           | The clip currently displayed in Live's Detail View.          |
| `highlighted_clip_slot` | `ClipSlot`        | `single` | `get/set` | `no`       | `<11`           | The slot highlighted in Session View.                        |
| `selected_chain`        | `Chain`           | `single` | `get`     | `yes`      | `<11`           | The highlighted chain, or `id 0` when unavailable.           |
| `selected_parameter`    | `DeviceParameter` | `single` | `get`     | `yes`      | `<11`           | The selected parameter, or `id 0`.                           |
| `selected_scene`        | `Scene`           | `single` | `get/set` | `yes`      | `<11`           | The currently selected scene in Session View.                |
| `selected_track`        | `Track`           | `single` | `get/set` | `yes`      | `<11`           | The currently selected track in Session or Arrangement View. |

#### `detail_clip`

- **Returns:** `Clip`
- **Shape:** `single`
- **Access:** `get/set`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The clip currently displayed in Live's Detail View.

#### `highlighted_clip_slot`

- **Returns:** `ClipSlot`
- **Shape:** `single`
- **Access:** `get/set`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The slot highlighted in Session View. According to the stub, this can be `None` for Main and Return
tracks.

**Probe notes (2026-02-17):** When a slot is selected in Session View, `highlighted_clip_slot`, `selected_track`, and
`selected_scene` all agree — the highlighted slot's `canonical_parent` matches `selected_track`, and the slot's index
within `track.clip_slots` matches `selected_scene`'s position in `song.scenes`. The highlighted slot is effectively the
intersection of `selected_track` and `selected_scene`.

#### `selected_chain`

- **Returns:** `Chain`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The highlighted chain, or `id 0` when unavailable.

#### `selected_parameter`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The selected parameter, or `id 0`.

#### `selected_scene`

- **Returns:** `Scene`
- **Shape:** `single`
- **Access:** `get/set`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The currently selected scene in Session View.

#### `selected_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Access:** `get/set`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The currently selected track in Session or Arrangement View.

### Properties

| Property           | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                      |
| ------------------ | ----------- | ----------- | ---------- | --------------- | ------------------------------------------------------------ |
| `_live_ptr`        | `Unknown`   | —           | `no`       | `<11`           | `_live_ptr` property.                                        |
| `canonical_parent` | `Song`      | —           | `no`       | `<11`           | Get the canonical parent of the song view.                   |
| `draw_mode`        | `bool`      | `bool`      | `yes`      | `<11`           | Reflects the state of Draw Mode in the transport bar.        |
| `follow_song`      | `bool`      | `bool`      | `yes`      | `<11`           | Reflects whether Arrangement view follows playback position. |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** `_live_ptr` property.

#### `canonical_parent`

- **Get Returns:** `Song`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the canonical parent of the song view.

#### `draw_mode`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Reflects the state of the Draw Mode switch in the transport bar (`0` = breakpoint editing, `1` =
drawing). Draw Mode is used in the Clip View for drawing envelopes and MIDI, and in the Arrangement View for drawing
automation curves.

#### `follow_song`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Reflects the state of the Follow switch in the transport bar (`0` = do not follow playback position,
`1` = follow playback position). When enabled, the display scrolls during playback to keep the current song position
visible. Follow behavior (continuous or page-by-page) is configured in the Display & Input Settings.

### Methods

| Signature                                                         | Returns | Available Since | Summary                               |
| ----------------------------------------------------------------- | ------- | --------------- | ------------------------------------- |
| `select_device(device: Device, ShouldAppointDevice: bool = True)` | `None`  | `<11`           | Select the given device in Live's UI. |

#### `select_device(device: Device, ShouldAppointDevice: bool = True)`

- **Returns:** `None`
- **Args:** `device: Device`, `ShouldAppointDevice: bool = True`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Selects the given device and can appoint it as the blue hand device.`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Selects the given device in its track. The containing track is not automatically shown. The device is
appointed only if its track is selected and `ShouldAppointDevice` is true.

**Probe Notes (12.3.5, MS33):** Live maintains two separate device states: the **selected** device (white outline,
no public getter) and the **appointed** device (blue hand, read via `Song.appointed_device`).
`select_device(dev, True)` sets both; `select_device(dev, False)` sets only the selection. The selected device
is what `Application.View.toggle_browse()` targets for hotswap — not `appointed_device`. Neither selection nor
appointment affects an already-active `Browser.hotswap_target`.

## BeatTime

Represents a time split into bars, beats, subdivision, and ticks (BBST). All four components are **1-based** — the
origin (internal beat position 0.0) is represented as `1.1.1.1`.

### Tick Grid Constants

Probed on Live 12.3.5. These values are constant regardless of time signature:

- **Ticks per sixteenth:** `60` (tick range per sixteenth: 1–60)
- **Sixteenths per beat:** `4` (sixteenth range per beat: 1–4)
- **Ticks per beat:** `240` (= 4 × 60)
- **Beats per bar:** `signature_numerator` (beat range per bar: 1–numerator)

### Time Signature Effect on BeatTime

**The denominator changes the BBST beat unit size.** Each BBST "beat" corresponds to the note value specified by the
denominator, not always a quarter note. The beat unit in internal (quarter-note) beats is `4 / denominator`.

| Signature | Beat unit (internal beats) | Beats per bar | Bar length (internal beats) |
| --------- | -------------------------- | ------------- | --------------------------- |
| 4/4       | 1.0                        | 4             | 4.0                         |
| 3/4       | 1.0                        | 3             | 3.0                         |
| 5/4       | 1.0                        | 5             | 5.0                         |
| 6/4       | 1.0                        | 6             | 6.0                         |
| 6/8       | 0.5                        | 6             | 3.0                         |
| 3/8       | 0.5                        | 3             | 1.5                         |
| 7/8       | 0.5                        | 7             | 3.5                         |
| 12/8      | 0.5                        | 12            | 6.0                         |

Conversion formulas:

```
beat_unit         = 4.0 / denominator       # internal beats per BBST beat
bar_length        = numerator * beat_unit    # internal beats per bar
ticks_per_bar     = numerator * 240          # BBST ticks per bar
```

Position → BBST (0-based intermediate, then +1 for each component):

```
total_ticks  = round(position / beat_unit * 240)
bars_0       = total_ticks // ticks_per_bar
bar_ticks    = total_ticks %  ticks_per_bar
beats_0      = bar_ticks   // 240
beat_ticks   = bar_ticks   %  240
sixteenths_0 = beat_ticks  // 60
ticks_0      = beat_ticks  %  60
→ (bars_0+1, beats_0+1, sixteenths_0+1, ticks_0+1)
```

BBST → position:

```
total_ticks = (bars-1)*numerator*240 + (beats-1)*240 + (sixteenths-1)*60 + (ticks-1)
position    = total_ticks / 240 * beat_unit
```

### Probe Matrix (Live 12.3.5)

Probed by setting `signature_numerator`/`signature_denominator`, setting `current_song_time` to known positions, and
reading `get_current_beats_song_time()`. All positions are internal quarter-note beats.

#### 4/4

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 0.25     | 1.1.2.1 |
| 0.5      | 1.1.3.1 |
| 1.0      | 1.2.1.1 |
| 3.0      | 1.4.1.1 |
| 4.0      | 2.1.1.1 |
| 12.0     | 4.1.1.1 |

#### 3/4

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 1.0      | 1.2.1.1 |
| 3.0      | 2.1.1.1 |
| 6.0      | 3.1.1.1 |
| 12.0     | 5.1.1.1 |

#### 6/8

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 0.25     | 1.1.2.1 |
| 0.5      | 1.2.1.1 |
| 1.0      | 1.3.1.1 |
| 2.0      | 1.5.1.1 |
| 3.0      | 2.1.1.1 |
| 5.0      | 2.5.1.1 |
| 6.0      | 3.1.1.1 |
| 12.0     | 5.1.1.1 |

#### 3/8

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 0.5      | 1.2.1.1 |
| 1.0      | 1.3.1.1 |
| 2.0      | 2.2.1.1 |
| 3.0      | 3.1.1.1 |
| 6.0      | 5.1.1.1 |
| 12.0     | 9.1.1.1 |

#### 7/8

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 0.5      | 1.2.1.1 |
| 3.0      | 1.7.1.1 |
| 3.5      | 2.1.1.1 |
| 7.0      | 3.1.1.1 |
| 12.0     | 4.4.1.1 |

#### 12/8

| Position | BBST     |
| -------- | -------- |
| 0.0      | 1.1.1.1  |
| 0.5      | 1.2.1.1  |
| 3.0      | 1.7.1.1  |
| 5.0      | 1.11.1.1 |
| 6.0      | 2.1.1.1  |
| 12.0     | 3.1.1.1  |

#### 5/4

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 1.0      | 1.2.1.1 |
| 4.0      | 1.5.1.1 |
| 5.0      | 2.1.1.1 |
| 12.0     | 3.3.1.1 |

#### 6/4

| Position | BBST    |
| -------- | ------- |
| 0.0      | 1.1.1.1 |
| 1.0      | 1.2.1.1 |
| 5.0      | 1.6.1.1 |
| 6.0      | 2.1.1.1 |
| 12.0     | 3.1.1.1 |

### Children

None.

### Properties

| Property       | Get Returns | Set Accepts | Listenable | Available Since | Summary                                       |
| -------------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------- |
| `bars`         | `int`       | —           | `no`       | `<11`           | Bar component (1-based). Range: 1–∞.          |
| `beats`        | `int`       | —           | `no`       | `<11`           | Beat component (1-based). Range: 1–numerator. |
| `sub_division` | `int`       | —           | `no`       | `<11`           | Sixteenth component (1-based). Range: 1–4.    |
| `ticks`        | `int`       | —           | `no`       | `<11`           | Tick component (1-based). Range: 1–60.        |

#### `bars`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Bar component of the time value. 1-based — bar 1 is the first bar.

#### `beats`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Beat component of the time value. 1-based — beat 1 is the first beat in the bar. Range is
1–`signature_numerator`. The beat unit size depends on the denominator: in `/4` signatures each beat is a quarter note
(1.0 internal beats); in `/8` each beat is an eighth note (0.5 internal beats).

#### `sub_division`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Sixteenth subdivision component of the time value. 1-based — subdivision 1 is the first sixteenth
within the beat. Range is always 1–4 regardless of time signature. Each subdivision spans 60 ticks.

#### `ticks`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Tick component of the time value. 1-based — tick 1 is the first tick within the sixteenth. Range is
1–60.

### Methods

None.

## SmptTime

Represents a time split into hours, minutes, seconds, and frames. The frame type is specified by the format passed to
`Song.get_current_smpte_song_time(format)`.

### Children

None.

### Properties

| Property  | Get Returns | Set Accepts | Listenable | Available Since | Summary                                   |
| --------- | ----------- | ----------- | ---------- | --------------- | ----------------------------------------- |
| `hours`   | `int`       | —           | `no`       | `<11`           | Hour component of the SMPTE time value.   |
| `minutes` | `int`       | —           | `no`       | `<11`           | Minute component of the SMPTE time value. |
| `seconds` | `int`       | —           | `no`       | `<11`           | Second component of the SMPTE time value. |
| `frames`  | `int`       | —           | `no`       | `<11`           | Frame component of the SMPTE time value.  |

#### `hours`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Hour component of the SMPTE time value.

#### `minutes`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Minute component of the SMPTE time value.

#### `seconds`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Second component of the SMPTE time value.

#### `frames`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Frame component of the SMPTE time value.

### Methods

None.

## TimeFormat

Enumeration used by `Song.get_current_smpte_song_time(format)`.

Known values from the Max for Live Song documentation:

- `0`: frame position reports milliseconds
- `1`: `Smpte24`
- `2`: `Smpte25`
- `3`: `Smpte30`
- `4`: `Smpte30Drop`
- `5`: `Smpte29`

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

## CuePoint

Represents a locator in Arrangement view.

### Children

None.

### Properties

| Property           | Get Returns | Set Accepts | Listenable | Available Since | Summary                                     |
| ------------------ | ----------- | ----------- | ---------- | --------------- | ------------------------------------------- |
| `_live_ptr`        | `Unknown`   | —           | `no`       | `<11`           | `_live_ptr` property.                       |
| `canonical_parent` | `Song`      | —           | `no`       | `<11`           | Get the canonical parent of the cue point.  |
| `name`             | `symbol`    | `symbol`    | `yes`      | `11.3`          | Name of the cue point shown in Arrangement. |
| `time`             | `float`     | —           | `yes`      | `<11`           | Cue point time in beats.                    |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** `_live_ptr` property.

#### `canonical_parent`

- **Get Returns:** `Song`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the canonical parent of the cue point.

#### `name`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.3`

**Description:** Name of the cue point shown in Arrangement.

#### `time`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Cue point time in beats.

### Methods

| Signature | Returns | Available Since | Summary                                         |
| --------- | ------- | --------------- | ----------------------------------------------- |
| `jump()`  | `None`  | `<11`           | Jump playback/start position to this cue point. |

#### `jump()`

- **Returns:** `None`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Moves transport position to this cue point.`
- **Async visibility:** `variable`
- **Available Since:** `<11`

**Description:** When the Song is playing, set the playing position quantized to this cue point's time. When not
playing, move the start playing position.

## CaptureDestination

Enumeration for `Song.capture_midi(destination)`.

Known values from Max for Live Song documentation:

- `0`: `auto`
- `1`: `session`
- `2`: `arrangement`

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

## CaptureMode

Enumeration for `Song.capture_and_insert_scene(capture_mode)`.

Probed values (Live 12.3.5):

| Value | Label (inferred)    | Description                                                 |
| ----- | ------------------- | ----------------------------------------------------------- |
| `0`   | all                 | Capture all currently playing clips (default).              |
| `1`   | all_except_selected | Capture all playing clips except the selected track's clip. |

Values ≥ 2 and negative values all fall back to `all` behavior. Arm state does not affect which
tracks are captured for any mode. Playback switches to the newly inserted scene after capture.
The `CaptureMode` class is not accessible as a `Song` attribute at runtime
(`Song.CaptureMode` raises `AttributeError`).

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

## Quantization

Enumeration for Song clip trigger quantization values.

Known values from Max for Live Song documentation:

- `0`: `None`
- `1`: `8 Bars`
- `2`: `4 Bars`
- `3`: `2 Bars`
- `4`: `1 Bar`
- `5`: `1/2`
- `6`: `1/2T`
- `7`: `1/4`
- `8`: `1/4T`
- `9`: `1/8`
- `10`: `1/8T`
- `11`: `1/16`
- `12`: `1/16T`
- `13`: `1/32`

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

## RecordingQuantization

Enumeration for Song MIDI recording quantization values.

Known values from Max for Live Song documentation:

- `0`: `None`
- `1`: `1/4`
- `2`: `1/8`
- `3`: `1/8T`
- `4`: `1/8 + 1/8T`
- `5`: `1/16`
- `6`: `1/16T`
- `7`: `1/16 + 1/16T`
- `8`: `1/32`

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

## SessionRecordStatus

Enumeration that reflects Song session recording state (`Song.session_record_status`).

Probed values (Live 12.3.5):

| Value | Label (inferred) | Description                                                 |
| ----- | ---------------- | ----------------------------------------------------------- |
| `0`   | off              | No session slot-recording active.                           |
| `1`   | recording        | Actively recording into a session slot.                     |
| `2`   | triggered        | Recording queued, waiting for launch quantization to start. |

Note: the value ordering differs from `ClipSlot.playing_status` (where `1` = playing, `2` = recording).

### Children

None.

### Properties

None.

### Methods

| Signature         | Returns | Available Since | Summary                                        |
| ----------------- | ------- | --------------- | ---------------------------------------------- |
| `from_bytes(...)` | `int`   | `N/A`           | Convert a byte sequence into an integer value. |

#### `from_bytes(...)`

- **Returns:** `int`
- **Args:** `bytes: object`, `byteorder: str = 'big'`, `signed: bool = False`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `None.`
- **Async visibility:** `immediate`
- **Available Since:** `<11`

**Description:** Standard integer conversion helper exposed by generated enum-like classes.

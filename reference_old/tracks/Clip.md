# Clip

> `Live.Clip.Clip`

Represents a clip in Live — either audio or MIDI, in either Session View or Arrangement View. The full
property/method surface is available on all clips, but many members are only meaningful for one clip type (audio vs
MIDI) or one context (session vs arrangement). Those are marked in each detail entry.

??? note "Raw probe notes (temporary)"

    **Color behavior (probed 2026-02-17):**

    - Setting `color` to `None` raises an `InternalError` (C++ type mismatch: expected `int`). Matches Track and
      Scene behavior.
    - Setting `color_index` to `None` raises an `InternalError`. Clips always have a color in the Live UI — there
      is no "no color" option — so `None` is not a valid value.

    **Arrangement clip playback (probed 2026-02-17):**

    All playback state properties and playback control methods are session-only. On arrangement clips they don't
    error, but they silently no-op:

    - Properties always `False`/`0.0`: `is_playing`, `is_triggered`, `is_recording`, `is_overdubbing`,
      `playing_position` — even while the transport plays through the clip's time range.
    - Methods no-op: `fire()`, `stop()`, `move_playing_pos()`, `scrub()`, `stop_scrub()`.

    **move_playing_pos / scrub / stop_scrub behavior (probed 2026-02-17):**

    - `move_playing_pos(beats)`: relative unquantized jump within the clip's local playhead. While playing,
      `move_playing_pos(2.0)` jumps ~2 beats forward; negative values jump backwards. While stopped: no-op.
    - `scrub(beat_time)`: auditions a looping snippet at an absolute position. While playing, clip transitions to
      `is_triggered=True`. While stopped, starts playback.
    - `stop_scrub()`: ends a scrub session. Clip remains in `is_triggered=True` state.

    **will_record_on_start (probed 2026-02-17):**

    Always returns `False` through the Python API regardless of conditions tested. Same non-functional behavior as
    `ClipSlot.will_record_on_start`. Skipped from the public API spec.

### Open Questions

- `warping`: stub notes that setting this property is internally deferred. What does this mean for listeners —
  does the listener fire before or after the deferred apply?
- ~~`start_time` on session clips: can it be negative when playback was offset?~~
  **Answered:** Session `start_time` is the song time (beat position) when the clip was fired. Updates on each
  launch.
- ~~`position` vs `loop_start`: Max docs say `position` always equals `loop_start` on get, but setting `position`
  preserves loop length whereas setting `loop_start` does not.~~
  **Answered:** Confirmed. `position` always equals `loop_start` on get. Setting `position` slides the loop
  window (preserves length); setting `loop_start` changes only the start (length changes).
- `loop_jump`: fires when the playhead crosses the loop start. Is this a real observable property in the PFL
  bridge, or does it require a listener-only approach?
- `notes`: fires when the note list changes. Does the bridge surface this as a listenable?
- `sample_rate` / `sample_length`: are these available on arrangement audio clips, or session audio clips only?
- ~~What is the sentinel for `playing_position` on a stopped clip?~~
  **Answered:** `0.0` for stopped session clips. Arrangement clips always return `0.0`.

### Mental Model For Live API Clip Properties

**API Parameters:** loop_start, loop_end, start_marker, end_marker, start_time, end_time, length
**UI Handles:** Start Marker, End Marker, Loop Start, Loop End, Loop Brace (the bar between start and end)
**UI Parameter Boxes:** Start, End, Loop Position, Loop Length

#### UI Behavior

The UI parameter boxes are the source-of-truth for all values. The handles and boxes are always in sync with the
following mapping:

**Handle to Box Mapping**

| Dragging Handle | Changes Parameter Box |
| --- | --- |
| Loop Start | Loop Position, Loop Length |
| Loop End | Loop Length |
| Loop Brace | Loop Position |
| Start Marker | Start |
| End Marker | End |

**Box to Handle Mapping**

| Changing Box Value | Moves Handle |
| --- | --- |
| Start | Start Marker |
| End | End Marker |
| Loop Position | Loop Brace (Start and End) |
| Loop Length | Loop End |

**Other Behavior:**

- When looping is on, dragging a Loop Handle will also move the Start/End Marker Handle if they are at the same
  position. This coupling breaks once they are separated.
- When looping is turned off, the end marker and timeline extent are reconciled: if the clip length in the
  timeline is shorter than the marker span, the end marker is clamped to fit within the timeline; if longer, it
  is shortened to match the end marker. The resulting timeline extent equals the marker span, and the clip will
  never grow larger on the timeline.

#### Clean API model

**When Looping is On:**

Both handle sets may be controlled.

| API name | Mental Name | Description |
| --- | --- | --- |
| loop_start | Loop Start | Controls the Loop Start Handle. |
| loop_end | Loop End | Controls the Loop End Handle. |
| start_marker | Start Marker | Controls where clip playback will start from, followed by normal loop range. |
| end_marker | End Marker | Has no effect during loop playback, but will move the inactive handle. |

**When Looping is Off:**

Only the start/end marker handles may be controlled.

| API name | Mental Name | Description |
| --- | --- | --- |
| loop_start | Start Marker | Controls the Start Marker Handle. |
| loop_end | End Marker | Controls the End Marker Handle. |
| start_marker | N/A | Invalid when looping off. |
| end_marker | N/A | Invalid when looping off. |

**At All Times:**

| API name | Mental Name | Description |
| --- | --- | --- |
| looping | Looping Toggle | Enable (or Disable) the looping mode. |
| length | Loop Length | The length of the looping region, whether active or not. |

**In Arrangements:**

| API name | Mental Name | Description |
| --- | --- | --- |
| start_time | Clip Start Time | When the clip starts in the Timeline. |
| end_time | Clip End Time | When the clip ends in the Timeline. |

**In Sessions:**

| API name | Mental Name | Description |
| --- | --- | --- |
| start_time | Fired At | Song time when the clip was fired. |
| end_time | N/A | Not super useful. |

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `view` | `Clip.View` | `single` | `no` | View aspects of this clip. |

#### `view`

- **Returns:** `Clip.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

Provides access to view-related state: grid quantization settings and envelope visibility controls. See the
`Clip.View` section at the bottom of this file.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `automation_envelopes` | `list` | `no` | `no` | Read-only list of all automation envelopes. |
| `available_warp_modes` | `list[int]` | `no` | `no` | Audio only. Available warp mode indexes. |
| `canonical_parent` | `object` | `no` | `no` | The clip's parent object (ClipSlot or Track). |
| `color` | `int` | `yes` | `yes` | Clip color as packed RGB `0x00rrggbb`. |
| `color_index` | `int` | `yes` | `yes` | Clip color palette index. |
| `end_marker` | `float` | `yes` | `yes` | End marker position in beats. Only functional when looping is ON. |
| `end_time` | `float` | `no` | `yes` | Arrangement: timeline end. Session: derived, not very useful. |
| `file_path` | `str` | `no` | `no` | Audio only. Absolute path to the referenced audio file. |
| `gain` | `float` | `yes` | `yes` | Audio only. Clip gain, range `0.0` to `1.0`. |
| `gain_display_string` | `str` | `no` | `no` | Audio only. Gain as a human-readable string. |
| `groove` | `Groove\|None` | `yes` | `yes` | Groove object associated with this clip, or `None`. |
| `has_envelopes` | `bool` | `no` | `yes` | `True` if the clip has any automation envelopes. |
| `has_groove` | `bool` | `no` | `no` | `True` if a groove is associated with this clip. |
| `is_arrangement_clip` | `bool` | `no` | `no` | `True` for clips in Arrangement View. |
| `is_audio_clip` | `bool` | `no` | `no` | `True` for audio clips. |
| `is_midi_clip` | `bool` | `no` | `no` | `True` for MIDI clips. Opposite of `is_audio_clip`. |
| `is_overdubbing` | `bool` | `no` | `yes` | Session only. `True` while overdubbing. |
| `is_playing` | `bool` | `no` | `no` | Session only. `True` if playing or recording. |
| `is_recording` | `bool` | `no` | `yes` | Session only. `True` if recording. |
| `is_session_clip` | `bool` | `no` | `no` | `True` for clips in Session View. |
| `is_take_lane_clip` | `bool` | `no` | `no` | `True` for Take Lane clips (also arrangement clips). |
| `is_triggered` | `bool` | `no` | `no` | Session only. `True` while the launch button is blinking. |
| `launch_mode` | `int` | `yes` | `yes` | Launch mode (0=Trigger, 1=Gate, 2=Toggle, 3=Repeat). |
| `launch_quantization` | `int` | `yes` | `yes` | Per-clip launch quantization override. |
| `legato` | `bool` | `yes` | `yes` | `True` if the Legato switch is on. |
| `length` | `float` | `no` | `no` | Always `loop_end - loop_start`, regardless of loop state. |
| `loop_end` | `float` | `yes` | `yes` | Loop region end (loop ON), or end marker alias (loop OFF). |
| `loop_jump` | `bang` | `no` | `yes` | Fires when the playhead crosses the loop start. |
| `loop_start` | `float` | `yes` | `yes` | Loop region start (loop ON), or start marker alias (loop OFF). |
| `looping` | `bool` | `yes` | `yes` | `True` if looping is enabled. |
| `muted` | `bool` | `yes` | `yes` | `True` if the clip's Clip Activator is off (muted). |
| `name` | `str` | `yes` | `yes` | Clip display name. |
| `notes` | `bang` | `no` | `yes` | MIDI only. Fires when the note list changes. |
| `pitch_coarse` | `int` | `yes` | `yes` | Audio only. Transpose in semitones, `-48` to `48`. |
| `pitch_fine` | `float` | `yes` | `yes` | Audio only. Detune in cents, `-50` to `49`. |
| `playing_position` | `float` | `no` | `yes` | Session only. Current playhead position. |
| `playing_status` | `bang` | `no` | `yes` | Fires when playing/trigger status changes. |
| `position` | `float` | `yes` | `yes` | Always equals `loop_start` on get; set slides loop window. |
| `ram_mode` | `bool` | `yes` | `yes` | Audio only. `True` if RAM switch is enabled. |
| `sample_length` | `int` | `no` | `no` | Audio only. Sample length in samples. |
| `sample_rate` | `float` | `no` | `no` | Audio only. Sample rate of the clip's audio file. |
| `signature_denominator` | `int` | `yes` | `yes` | Clip time signature denominator. |
| `signature_numerator` | `int` | `yes` | `yes` | Clip time signature numerator. |
| `start_marker` | `float` | `yes` | `yes` | Start marker position in beats. Setter ignored when loop OFF. |
| `start_time` | `float` | `no` | `yes` | Arrangement: timeline start. Session: song time when fired. |
| `velocity_amount` | `float` | `yes` | `yes` | How much trigger velocity affects clip volume, `0.0` to `1.0`. |
| `warp_markers` | `list[WarpMarker]` | `no` | `yes` | Audio only. Warp markers; observable fires bang on change. |
| `warp_mode` | `int` | `yes` | `yes` | Audio only. Warp mode index. |
| `warping` | `bool` | `yes` | `yes` | Audio only. `True` if warping is enabled. Setting is deferred. |
| `will_record_on_start` | `bool` | `no` | `no` | Always returns `False` via Python API (non-functional). |

#### `automation_envelopes`

- **Type:** `list`
- **Listenable:** `no`
- **Since:** `12.2`

Read-only list of all automation envelopes on this clip. Returns `Envelope` objects. Use
`automation_envelope(parameter)` to get the envelope for a specific parameter, or
`create_automation_envelope(parameter)` to create one.

#### `available_warp_modes`

- **Type:** `list[int]`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. List of integer indexes of warp modes available for this clip. Cross-reference with `warp_mode`.

- **Quirks:** Returns `[0, 1, 2, 3, 4, 6]` for a standard audio clip — REX mode (5) is not available.

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `<11`

The clip's canonical parent. For session clips this is the `ClipSlot`; for arrangement clips this is the `Track`.

#### `color`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip color as a packed RGB value `0x00rrggbb`. When setting, Live snaps to the nearest color in the clip color
chooser.

- **Quirks:** Setting to `None` raises an `InternalError` (C++ type mismatch).

#### `color_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Palette-based color index. Clips always have a color in the Live UI.

- **Quirks:** Setting to `None` raises an `InternalError`.

#### `end_marker`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** Position of the clip's end marker in beats. The end marker has no effect on loop playback but
its handle position is maintained.
**When loop is OFF:** Invalid parameter. The setter is accepted (value changes on readback) but the UI handle does
not move, and the API value is overwritten when looping is toggled back on. Use `loop_end` to control the end
bound when looping is off.

#### `end_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Context-dependent read-only value:

- **Arrangement:** timeline end position in beats.
- **Session:** a derived value that is not particularly useful. Equals
  `max(loop_end - start_marker, loop_end - loop_start)` when looping is on; equals
  `end_marker - start_marker` when looping is off. Not recommended for direct use.

#### `file_path`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Absolute path to the audio file referenced by this clip.

#### `gain`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Clip gain, range `0.0` to `1.0`.

#### `gain_display_string`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Gain as a human-readable display string (e.g. `"1.3 dB"`). Read-only.

#### `groove`

- **Type:** `Groove | None`
- **Listenable:** `yes`
- **Since:** `11.0`

The Groove object applied to this clip. Groove objects are accessed via `Song.groove_pool`.

- **Limitations:** Setting to `None` to remove the groove is not possible via the Python API — the C++ setter
  requires `TPyHandle<AAbstractGroove>` and rejects `NoneType`. The UI's "Commit Groove" button is also not
  exposed.

#### `has_envelopes`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the clip contains any automation envelopes. Fires listener when envelopes are added or removed.

#### `has_groove`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `11.0`

`True` if a groove is associated with this clip.

#### `is_arrangement_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for clips in Arrangement View. Take Lane clips are also arrangement clips (`is_take_lane_clip` and
`is_arrangement_clip` can both be `True`).

#### `is_audio_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio clips. Use to gate audio-only members before accessing them.

#### `is_midi_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI clips. Exact opposite of `is_audio_clip`.

#### `is_overdubbing`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. `True` while the clip is overdubbing. Always `False` on arrangement clips.

#### `is_playing`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Session only. `True` if the clip is currently playing or recording. Always `False` on arrangement clips, even
while the transport plays through the clip's time range. Use `fire()` and `stop()` to control playback.

#### `is_recording`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. `True` if the clip is currently recording. Always `False` on arrangement clips.

#### `is_session_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.2`

`True` for clips in Session View.

#### `is_take_lane_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.2`

`True` for Take Lane clips. These are a subtype of arrangement clips; `is_arrangement_clip` is also `True`.

#### `is_triggered`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Session only. `True` while the Clip Launch button is blinking (launch queued, waiting on quantization). Always
`False` on arrangement clips.

#### `launch_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.0`

Launch mode: `0` = Trigger (default), `1` = Gate, `2` = Toggle, `3` = Repeat.

#### `launch_quantization`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.0`

Per-clip launch quantization, overrides the song's global quantization when set. Values: `0`=Global (default),
`1`=None, `2`=8 Bars, `3`=4 Bars, `4`=2 Bars, `5`=1 Bar, `6`=1/2, `7`=1/2T, `8`=1/4, `9`=1/4T, `10`=1/8,
`11`=1/8T, `12`=1/16, `13`=1/16T, `14`=1/32.

#### `legato`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `11.0`

`True` when the Legato switch in the clip's Launch settings is on.

#### `length`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

Always equals `loop_end - loop_start`, regardless of whether looping is enabled and regardless of marker
positions. This is NOT `end_marker - start_marker`. Units are beats for MIDI and warped audio; seconds for
unwarped audio.

#### `loop_end`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** controls the Loop End Handle (right edge of the loop brace). Independent of `end_marker`.
**When loop is OFF:** aliases the End Marker Handle — setting `loop_end` moves the end marker and adjusts the
clip's timeline extent. This is the **only** way to control the end bound when looping is off. Units are beats
for MIDI and warped audio; seconds for unwarped audio.

#### `loop_jump`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

Observable that fires when the clip playhead crosses the loop start marker. Used to detect loop cycles.

#### `loop_start`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** controls the Loop Start Handle (left edge of the loop brace). Independent of `start_marker`.
**When loop is OFF:** aliases the Start Marker Handle — setting `loop_start` moves the start marker. This is the
**only** way to control the start bound when looping is off; `start_marker` writes are silently ignored. Units
are beats for MIDI and warped audio; seconds for unwarped audio. Beat time `0` corresponds to position `1.1.1`
in the clip view ruler.

#### `looping`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if clip looping is enabled. Toggling this switches which marker system is active — with loop ON,
`loop_start`/`loop_end` control the loop brace independently of the markers; with loop OFF, they alias the
start/end markers.

- **Quirks:** **Toggle ON -> OFF (arrangement):** The end marker and timeline extent are reconciled — if the
  timeline is shorter than the marker span, the end marker is clamped; if longer, the timeline shrinks. The clip
  never grows on toggle. **Toggle OFF -> ON:** the UI's saved loop marker positions are restored. Unwarped audio
  clips cannot be looped.

#### `muted`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when the clip's Clip Activator button is off (clip is deactivated/muted).

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Display name of the clip.

#### `notes`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

MIDI only. Observable that fires when the clip's note list changes. Use `get_notes_extended()` or
`get_all_notes_extended()` to retrieve current notes after receiving this notification.

#### `pitch_coarse`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Pitch transposition in semitones (Transpose knob). Range: `-48` to `48`.

#### `pitch_fine`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Fine pitch adjustment in cents (Detune knob). Range: `-50` to `49`.

#### `playing_position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. Current playhead position. For MIDI and warped audio: beats of absolute clip time (beat `0` =
position `1` in the clip ruler). For unwarped audio: seconds from clip start. Stopped clips return `0.0`. Always
`0.0` on arrangement clips.

#### `playing_status`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

Observable that fires when the clip's playing or trigger status changes. Has no readable value; use `is_playing`,
`is_recording`, `is_triggered` to read current state after receiving the notification.

#### `position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Loop position / window slide control. On get, always equals `loop_start`. On set, moves `loop_start` to the
specified position and adjusts `loop_end` to preserve `length` (unlike setting `loop_start` directly, which
changes `length`). Works in both loop ON and OFF modes.

- **Quirks:** When the new loop window extends past `start_marker` or `end_marker`, those markers are auto-pushed
  to stay within/at the loop bounds.

#### `ram_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. `True` when the clip's RAM mode switch is enabled.

#### `sample_length`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Length of the clip's audio sample in samples (not beats).

#### `sample_rate`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `11.0`

Audio only. Sample rate of the clip's audio file in Hz.

#### `signature_denominator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip time signature denominator.

#### `signature_numerator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip time signature numerator.

#### `start_marker`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** Position of the clip's start marker in beats. Fully independent of `loop_start`. Playback
starts here and goes until `loop_end` before looping back to `loop_start` — can define an "intro" or shorter
first loop.
**When loop is OFF:** setter is **silently ignored** — the API value does not change. Use `loop_start` to control
the start bound in this state.

#### `start_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Context-dependent start time in beats (read-only):

- **Arrangement clips:** start position within the arrangement timeline.
- **Session clips:** song time (beat position) when the clip was fired. Updates each time the clip is launched.

#### `velocity_amount`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.0`

Controls how much the velocity of the MIDI note triggering the clip affects the clip's volume. `0.0` = no effect;
`1.0` = full effect.

#### `warp_markers`

- **Type:** `list[WarpMarker]` (WarpMarkerVector)
- **Listenable:** `yes`
- **Since:** `11.0`

Audio only. The clip's warp markers as a list. Returns `WarpMarker` objects, each with `beat_time: float` and
`sample_time: float`. The observable fires a bang when markers change.

- **Quirks:** The last marker in the list is a phantom marker (1/32 beat after the last visible marker) used
  internally to derive the final-segment BPM — it is not shown in the Live UI. `WarpMarker.sample_time` is in
  **seconds**, not samples, despite the field name. This differs from `beat_to_sample_time()` which returns
  samples.

#### `warp_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Warp mode as an integer. Must be one of the values in `available_warp_modes`. Values: `0` = Beats,
`1` = Tones, `2` = Texture, `3` = Re-Pitch, `4` = Complex, `5` = REX, `6` = Complex Pro.

#### `warping`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. `True` when the Warp switch is enabled.

- **Quirks:** Setting this property is internally deferred by Live. In sequences of API calls within a single
  event, the actual order of operations may differ from the call order. Introduce a tick delay between the set
  and any dependent operation.

#### `will_record_on_start`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Documented as `True` when recording will start on armed MIDI tracks. However, probing shows it always returns
`False` through the Python API. Recording state is covered by `is_recording` and `is_overdubbing`.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `add_new_notes(notes: tuple[MidiNoteSpecification, ...])` | `list[int]` | MIDI only. Add new notes; returns assigned note IDs. |
| `add_warp_marker(warp_marker: WarpMarker)` | `None` | Audio only. Add a warp marker. |
| `apply_note_modifications(notes: MidiNoteVector)` | `None` | MIDI only. Modify existing notes in-place by note ID. |
| `automation_envelope(device_parameter)` | `Envelope\|None` | Return the envelope for a parameter, or `None`. |
| `beat_to_sample_time(beat_time: float)` | `float` | Audio only. Convert beat time to sample time (warped). |
| `clear_all_envelopes()` | `None` | Remove all automation envelopes. |
| `clear_envelope(device_parameter)` | `None` | Remove the envelope for a specific parameter. |
| `create_automation_envelope(device_parameter)` | `Envelope` | Create and return an envelope for a parameter. |
| `crop()` | `None` | Crop clip to loop or start/end markers. |
| `deselect_all_notes()` | `None` | MIDI only. Deselect all notes. |
| `duplicate_loop()` | `None` | MIDI only. Double the loop length and duplicate content. |
| `duplicate_notes_by_id(note_ids, destination_time, transposition_amount)` | `list[int]` | MIDI only. Duplicate notes by ID. Returns new IDs. |
| `duplicate_region(region_start, region_length, destination_time, pitch, transposition_amount)` | `None` | MIDI only. Duplicate notes in a region. |
| `fire()` | `None` | Session only. Launch this clip. |
| `get_all_notes_extended(return_fields)` | `MidiNoteVector` | MIDI only. Return all notes. |
| `get_notes(from_time, from_pitch, time_span, pitch_span)` | `tuple` | **Deprecated.** MIDI only. Return notes as tuples. |
| `get_notes_by_id(note_ids, return_fields)` | `MidiNoteVector` | MIDI only. Return notes by ID. |
| `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields)` | `MidiNoteVector` | MIDI only. Return notes in a region. |
| `get_selected_notes()` | `tuple` | **Deprecated.** MIDI only. Return selected notes. |
| `get_selected_notes_extended(return_fields)` | `MidiNoteVector` | MIDI only. Return selected notes. |
| `move_playing_pos(beats: float)` | `None` | Session only. Relative jump of clip playhead. |
| `move_warp_marker(beat_time: float, beat_time_distance: float)` | `None` | Audio only. Move a warp marker. |
| `note_number_to_name(midi_pitch: int)` | `str` | MIDI only. Convert MIDI note number to name. |
| `quantize(quantization_grid: int, amount: float)` | `None` | MIDI only. Quantize all notes. |
| `quantize_pitch(pitch: int, quantization_grid: int, amount: float)` | `None` | MIDI only. Quantize notes of one pitch. |
| `remove_notes(from_time, from_pitch, time_span, pitch_span)` | `None` | **Deprecated.** MIDI only. Delete notes in a region. |
| `remove_notes_by_id(note_ids: list[int])` | `None` | MIDI only. Delete notes by ID. |
| `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)` | `None` | MIDI only. Delete notes in a region. |
| `remove_warp_marker(beat_time: float)` | `None` | Audio only. Remove a warp marker. |
| `replace_selected_notes(notes_tuple)` | `None` | **Deprecated.** MIDI only. Replace selected notes. |
| `sample_to_beat_time(sample_time: float)` | `float` | Audio only. Convert sample time to beat time (warped). |
| `scrub(beat_time: float)` | `None` | Session only. Audition a looping snippet at a position. |
| `seconds_to_sample_time(seconds: float)` | `float` | Audio only. Convert seconds to sample time (unwarped). |
| `select_all_notes()` | `None` | MIDI only. Select all notes. |
| `select_notes_by_id(note_ids: list[int])` | `None` | MIDI only. Select specific notes by ID. |
| `set_fire_button_state(state: bool)` | `None` | Simulate holding/releasing the clip launch button. |
| `set_notes(notes_tuple)` | `None` | **Deprecated.** MIDI only. Add notes from tuple data. |
| `stop()` | `None` | Session only. Stop this clip. |
| `stop_scrub()` | `None` | Session only. End an active scrub session. |

#### `add_new_notes(notes)`

- **Returns:** `list[int]` -- list of note IDs for the added notes
- **Args:**
  - `notes: tuple[MidiNoteSpecification, ...]` -- a **tuple** of `Live.Clip.MidiNoteSpecification` objects
- **Raises:** `InternalError` if passed dicts or a list instead of a tuple of `MidiNoteSpecification`
- **Since:** `11.0`

Adds notes to the clip. The argument must be a **tuple** of `Live.Clip.MidiNoteSpecification` objects — **not** a
list of dicts.

`MidiNoteSpecification` is constructed with keyword args:

```python
import Live
spec = Live.Clip.MidiNoteSpecification(
    pitch=60,          # int, required: MIDI note number 0-127
    start_time=0.0,    # float, required: start in beats of absolute clip time
    duration=0.5,      # float, required: note length in beats
    velocity=100.0,    # float, optional, default 100
    release_velocity=64.0,  # float, optional, default 64
    velocity_deviation=0.0, # float, optional, default 0.0
    mute=False,        # bool, optional, default False
    probability=1.0,   # float, optional, default 1.0
)
clip.add_new_notes((spec,))  # must be a tuple
```

Returns the list of integer note IDs assigned to the new notes.

#### `add_warp_marker(warp_marker)`

- **Returns:** `None`
- **Args:**
  - `warp_marker: Live.Clip.WarpMarker` -- native C++ `TWarpMarker` type
- **Raises:** `Segment length out of range` if resulting segment BPM exceeds `[5, 999]` or a marker already
  exists at the same `beat_time` with a different `sample_time`; `Warp marker sample time is out of range` if
  `sample_time` exceeds clip duration.
- **Since:** `11.0.5`

Adds a warp marker. The argument is a `Live.Clip.WarpMarker` object, **not** a dict. Constructor:
`Live.Clip.WarpMarker(sample_time, beat_time)` — note `sample_time` comes **first**. Does **not** accept keyword
arguments.

- **Quirks:** `sample_time` is in **seconds** (not samples). Adding a duplicate marker with the same `beat_time`
  and `sample_time` as an existing marker is a silent no-op.

#### `apply_note_modifications(notes)`

- **Returns:** `None`
- **Args:**
  - `notes: MidiNoteVector` -- the **original vector** returned by `get_all_notes_extended`, with attributes
    modified in-place
- **Raises:** `InternalError` if passed a Python `list` instead of the native `MidiNoteVector`
- **Since:** `11.0`

In-place modification of existing notes. The intended workflow is:

1. `notes = clip.get_all_notes_extended()` -- returns a `MidiNoteVector`
2. Modify note attributes in-place: `notes[0].velocity = 50`
3. `clip.apply_note_modifications(notes)` -- pass the **same vector** back

The argument must be the original `MidiNoteVector` object (Boost.Python-wrapped `std::vector`). Passing a plain
Python `list` raises `InternalError`.

#### `automation_envelope(device_parameter)`

- **Returns:** `Envelope | None`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Returns the automation envelope for the given device parameter, or `None` if no envelope exists. Always returns
`None` for Arrangement clips and for parameters on a different track.

#### `beat_to_sample_time(beat_time)`

- **Returns:** `float` -- sample time in **samples** (not seconds)
- **Args:**
  - `beat_time: float`
- **Raises:** Error if clip is not warped.
- **Since:** `<11`

Audio only. Converts beat time to sample time for warped clips. Returns the value in **samples** (not seconds).

- **Quirks:** The return unit (samples) differs from `WarpMarker.sample_time` which is in seconds. Divide by
  `sample_rate` to convert.

#### `clear_all_envelopes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Deletes all clip-level automation envelopes.

#### `clear_envelope(device_parameter)`

- **Returns:** `None`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Removes the clip's automation envelope for a specific device parameter.

#### `create_automation_envelope(device_parameter)`

- **Returns:** `Envelope`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Creates and returns an automation envelope for the given device parameter. Use `automation_envelope(parameter)`
first to check if one already exists.

#### `crop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

If the clip is looped, removes content outside the loop. If not looped, removes content outside the start/end
markers.

#### `deselect_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Deselects all notes in the clip.

#### `duplicate_loop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Doubles the loop by moving `loop_end` to the right and duplicating all notes and envelopes into the new
region. If not looped, doubles the start/end range instead.

#### `duplicate_notes_by_id(note_ids, destination_time=None, transposition_amount=0)`

- **Returns:** `list[int]` -- note IDs of the newly created duplicate notes
- **Args:**
  - `note_ids: list[int]` -- IDs of notes to duplicate
  - `destination_time: float (optional)` -- beat time to place duplicates
  - `transposition_amount: int (optional)` -- semitones to transpose duplicates
- **Since:** `11.1.2`

MIDI only. Duplicates notes matching the given IDs. Preserves per-note expression envelopes (MDE) on the copies.

#### `duplicate_region(region_start, region_length, destination_time, pitch=-1, transposition_amount=0)`

- **Returns:** `None`
- **Args:**
  - `region_start: float` -- start of the region in beats
  - `region_length: float` -- length in beats
  - `destination_time: float` -- beat time to place the duplicated notes
  - `pitch: int (optional)` -- only duplicate this pitch; `-1` = all pitches (default)
  - `transposition_amount: int (optional)` -- semitones to transpose
- **Since:** `<11`

MIDI only. Duplicates all notes in the specified time region. Preserves per-note expression envelopes (MDE).

#### `fire()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Launches this clip. Equivalent to pressing the Clip Launch button. No-op on arrangement clips.

#### `get_all_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector` -- native C++ vector of `MidiNote` objects
- **Args:**
  - `return_fields: dict (optional)` -- `{"return": [field_names]}` to limit returned fields
- **Since:** `11.1`

MIDI only. Returns all notes in the clip regardless of marker positions. Each element is a `MidiNote` object with
writable attributes: `note_id`, `pitch`, `start_time`, `duration`, `velocity`, `mute`, `probability`,
`velocity_deviation`, `release_velocity`. The returned vector is the same type expected by
`apply_note_modifications()`.

#### `get_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `tuple` -- tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:**
  - `from_time: float`, `from_pitch: int`, `time_span: float`, `pitch_span: int`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `get_notes_extended()`.

#### `get_notes_by_id(note_ids, return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `note_ids: object` -- list of note IDs
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns notes matching the given IDs.

#### `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `from_pitch: int`, `pitch_span: int`, `from_time: float`, `time_span: float`
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns notes whose start times fall within the given region. Replaces the deprecated `get_notes`.

#### `get_selected_notes()`

- **Returns:** `tuple` -- tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:** None
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `get_selected_notes_extended()`.

#### `get_selected_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns the currently selected notes.

#### `move_playing_pos(beats)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- relative jump in beats; negative = backwards
- **Since:** `<11`

Session only. Relative unquantized jump from the current playhead position within the clip's local timeline. Does
not affect the global song playhead. No-op when stopped or on arrangement clips.

#### `move_warp_marker(beat_time, beat_time_distance)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- beat time of the marker to move
  - `beat_time_distance: float` -- relative distance to move it
- **Since:** `11.0`

Audio only. Moves the warp marker at `beat_time` by `beat_time_distance`.

#### `note_number_to_name(midi_pitch)`

- **Returns:** `str`
- **Args:**
  - `midi_pitch: int` -- MIDI note number `0-127`
- **Since:** `12.1`

MIDI only. Returns a human-readable name for the given MIDI note number (e.g. `"C3"`, `"F#4"`). Takes into account
the clip's scale, tonal spelling settings, and current tuning system.

#### `quantize(quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `quantization_grid: int` -- `GridQuantization` enum value **1-8**
  - `amount: float` -- quantization strength `0.0-1.0`
- **Raises:** `InternalError: Invalid quantization.` for values outside 1-8
- **Since:** `<11`

MIDI only. Quantizes all notes to the given grid using the song's current swing setting. Values: `1`=8 Bars,
`2`=4 Bars, `3`=2 Bars, `4`=1 Bar, `5`=1/2, `6`=1/4, `7`=1/8, `8`=1/16.

#### `quantize_pitch(pitch, quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `pitch: int` -- MIDI pitch to quantize (0-127)
  - `quantization_grid: int` -- `GridQuantization` enum value **1-8**
  - `amount: float` -- quantization strength `0.0-1.0`
- **Since:** `<11`

MIDI only. Same as `quantize` but restricted to notes of a single pitch.

#### `remove_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `None`
- **Args:**
  - `from_time: float`, `from_pitch: int`, `time_span: float`, `pitch_span: int`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `remove_notes_extended()` and `remove_notes_by_id()`.

#### `remove_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:**
  - `note_ids: list[int]`
- **Since:** `11.0`

MIDI only. Deletes all notes matching the given IDs.

#### `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)`

- **Returns:** `None`
- **Args:**
  - `from_pitch: int`, `pitch_span: int`, `from_time: float`, `time_span: float`
- **Since:** `11.0`

MIDI only. Deletes all notes whose start times fall in the given region.

#### `remove_warp_marker(beat_time)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- beat time of the marker to remove
- **Since:** `11.0`

Audio only. Removes the warp marker at `beat_time`.

#### `replace_selected_notes(notes_tuple)`

- **Returns:** `None`
- **Args:**
  - `notes_tuple: tuple`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `apply_note_modifications()` or `remove_notes_extended()` +
`add_new_notes()`.

#### `sample_to_beat_time(sample_time)`

- **Returns:** `float`
- **Args:**
  - `sample_time: float` -- sample time in **samples** (not seconds)
- **Raises:** Error if clip is not warped.
- **Since:** `<11`

Audio only. Converts sample time to beat time for warped clips. Inverse of `beat_to_sample_time`.

#### `scrub(beat_time)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- absolute clip beat time to scrub to
- **Since:** `<11`

Session only. Auditions a looping snippet at an absolute beat position. The snippet size is determined by the
global `clip_trigger_quantization` setting. No-op on arrangement clips.

#### `seconds_to_sample_time(seconds)`

- **Returns:** `float`
- **Args:**
  - `seconds: float`
- **Raises:** Error if clip is warped.
- **Since:** `<11`

Audio only. Converts seconds to sample time for **unwarped** clips. Note: this is the opposite requirement from
`beat_to_sample_time`/`sample_to_beat_time` which require warped clips.

#### `select_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Selects all notes in the clip.

#### `select_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:**
  - `note_ids: list[int]`
- **Since:** `11.0.6`

MIDI only. Selects notes matching the given IDs.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`
- **Since:** `<11`

Simulates pressing and holding the clip launch button until `state=False` or the clip is otherwise stopped.

#### `set_notes(notes_tuple)`

- **Returns:** `None`
- **Args:**
  - `notes_tuple: tuple`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `add_new_notes()`.

#### `stop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Stops the clip if it is currently playing or recording. No-op on arrangement clips.

#### `stop_scrub()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Ends a scrub initiated with `scrub()`. No-op on arrangement clips.

---

## Clip.View

> `Live.Clip.Clip.View`

Provides access to view aspects of a clip: grid display settings and envelope visibility controls in the Clip
Detail View.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `grid_is_triplet` | `bool` | `yes` | `no` | Whether the clip displays a triplet grid. |
| `grid_quantization` | `int` | `yes` | `no` | Grid quantization resolution (`GridQuantization` enum). |

#### `grid_is_triplet`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Controls whether the clip's detail view displays a triplet grid. Works on any clip regardless of whether it is the
detail clip.

#### `grid_quantization`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Grid quantization resolution for the clip's detail view. Uses the `Clip.GridQuantization` enum (not
`Song.Quantization`). Values: `0`=No grid (off), `1`=8 Bars, `2`=4 Bars, `3`=2 Bars, `4`=1 Bar, `5`=1/2,
`6`=1/4, `7`=1/8, `8`=1/16, `9`=1/32. Triplet variants are controlled separately by `grid_is_triplet`.

- **Quirks:** `Clip.quantize()` and `Clip.quantize_pitch()` use the same enum but only accept values **1-8**
  (0 and 9 raise `Invalid quantization`). The value is an int enum; passing a float raises a type mismatch error.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `hide_envelope()` | `None` | Hide the Envelopes box in Clip Detail View. |
| `select_envelope_parameter(parameter: DeviceParameter)` | `None` | Select a parameter for envelope display. |
| `show_envelope()` | `None` | Show the Envelopes box in Clip Detail View. |
| `show_loop()` | `None` | Scroll the Detail View to show the loop region. |

#### `hide_envelope()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Switches the clip detail view away from the Envelopes tab. Only has an effect when the clip is the detail clip;
silently no-ops otherwise.

#### `select_envelope_parameter(parameter)`

- **Returns:** `None`
- **Args:**
  - `parameter: DeviceParameter`
- **Since:** `<11`

Selects the specified device parameter in the Envelopes box for display/editing. Only has an effect when the clip
is the detail clip; silently no-ops otherwise.

#### `show_envelope()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Switches the clip detail view to the Envelopes tab. Only has an effect when the clip is the detail clip.

#### `show_loop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Scrolls the clip detail view to show the current loop region. Only has an effect when the clip is the detail clip.

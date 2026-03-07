# Clip

## Clip

Represents a clip in Live — either audio or MIDI, in either Session View or Arrangement View.
The full property/method surface is available on all clips, but many members are only meaningful
for one clip type (audio vs MIDI) or one context (session vs arrangement). Those are marked
`Applicable to` in each detail entry.

### Sources

- **Primary:** `Live/classes/Clip.py` (stub dump)
- **Secondary:** `MaxForLive/clip.md`, `MaxForLive/clip_view.md`
- **Probes:** `.tmp/probe_color_none.py`, `.tmp/probe_clip_will_record.py`, `.tmp/probe_arrangement_clip.py`,
  `.tmp/probe_clip_scrub.py`, `.tmp/probe_clip_timing.py`, `.tmp/probe_clip_timing2.py`, `.tmp/probe_clip_timing3.py`,
  `.tmp/probe_start_time.py`, `.tmp/probe_timing.py` (Live 12.3.5)
- **Probe Findings:** `.tmp/Probe_timing_findings.md`

### Probe Notes

#### Color behavior (probed 2026-02-17)

- Setting `color` to `None` raises an `InternalError` (C++ type mismatch: expected `int`). Matches Track and Scene
  behavior.
- Setting `color_index` to `None` raises an `InternalError` (C++ type mismatch: expected `int`). Like tracks, clips
  always have a color in the Live UI — there is no "no color" option — so `None` is not a valid value. (Scenes are the
  exception: they can have no color assigned.)

#### Arrangement clip playback (probed 2026-02-17)

All playback state properties and playback control methods are **session-only**. On arrangement
clips they don't error, but they silently no-op:

- **Properties always `False`/`0.0`:** `is_playing`, `is_triggered`, `is_recording`,
  `is_overdubbing`, `playing_position` — even while the transport is playing through the clip's
  time range in the arrangement.
- **Methods no-op:** `fire()` (doesn't start transport or trigger clip), `stop()` (doesn't stop
  transport), `move_playing_pos()` (position unchanged), `scrub()` / `stop_scrub()` (no effect).
- Arrangement clip was created via `Track.create_midi_clip(0.0, 4.0)`, confirmed
  `is_arrangement_clip=True`, `is_session_clip=False`.
- Transport was started at the clip's `start_time` and confirmed playing (`song.is_playing=True`),
  yet clip-level playback state remained all-False.

#### move_playing_pos / scrub / stop_scrub behavior (probed 2026-02-17)

**`move_playing_pos(beats)`** — relative unquantized jump within the clip's local playhead:

- While playing: `move_playing_pos(2.0)` jumps ~2 beats forward; negative values jump backwards.
- While stopped: no-op (position stays `0.0`).
- Does not affect the global song playhead — only the clip's internal position.

**`scrub(beat_time)`** — auditions a looping snippet at an absolute position:

- While playing: clip transitions from `is_playing=True` to `is_playing=False, is_triggered=True`.
  The `playing_position` does not jump to the target — it continues advancing linearly. The
  audible output scrubs to the target, looping a snippet whose size matches the global
  `clip_trigger_quantization` setting.
- While stopped: starts playback (`is_playing=True`).
- Repeated `scrub()` calls change the target position.

**`stop_scrub()`** — ends a scrub session:

- After calling, clip remains in `is_triggered=True` state (probe observation). The exact
  transition back to normal playback is unclear.

Scrub is a niche live-performance feature (cf. the "eb.Scrubber" Max for Live device). Deferred
from the public API spec due to confusing behavior and limited documentation.

#### will_record_on_start (probed 2026-02-17)

- Always returns `False` through the Python API regardless of conditions tested:
  - Armed/unarmed track, overdub on/off
  - Transport stopped and playing
  - Clip actively recording and overdubbing (`is_recording=True`, `is_overdubbing=True`)
  - `session_record` on/off
- Same non-functional behavior as `ClipSlot.will_record_on_start`. May only function through
  the Max LOM path or within listener callback contexts. **Skipped** from the public API spec.
  Recording state is already covered by `is_recording` and `is_overdubbing`.

### Open Questions

- `warping`: stub notes that setting this property is internally deferred. What does this
  mean for listeners — does the listener fire before or after the deferred apply?
- ~~`start_time` on session clips: can it be negative when playback was offset? Max docs say yes.
  What is the lower bound?~~
  **Answered:** Session `start_time` is the song time (beat position) when the clip was fired.
  Updates on each launch. Earlier probes at `loop_start=0` showed it always as `0.0`, but
  further testing confirmed it tracks the fire time. Negative values may be possible if fired
  before the song start, but not yet tested.
- ~~`position` vs `loop_start`: Max docs say `position` always equals `loop_start` on get, but
  setting `position` preserves loop length whereas setting `loop_start` does not. Is this
  confirmed by probe?~~
  **Answered:** Confirmed. `position` always equals `loop_start` on get. Setting `position`
  slides the loop window (preserves length); setting `loop_start` changes only the start
  (length changes). Additionally, setting `position` auto-pushes markers when the loop extends
  past them. Setting `loop_start` with loop OFF also one-way aliases `start_marker`.
- `loop_jump`: Max docs describe it as a `bang observe` — it fires when the playhead crosses
  the loop start. Is this a real observable property in the PFL bridge, or does it require a
  listener-only approach?
- `notes`: also described as a `bang observe` — fires when the note list changes. Does the
  bridge surface this as a listenable, or is it note-change-only?
- `sample_rate` / `sample_length`: are these available on arrangement audio clips, or session
  audio clips only?
- ~~What is the sentinel for `playing_position` on a stopped clip — is it always exactly `0.0`?~~
  **Answered:** Yes, `0.0` for stopped session clips. Arrangement clips always return `0.0`.

### Mental Model For Live API Clip Properties

**API Parameters:** loop_start, loop_end, start_marker, end_marker, start_time, end_time, length
**UI Handles:** Start Marker, End Marker, Loop Start, Loop End, Loop Brace (the bar between start and end)
**UI Parameter Boxes:** Start, End, Loop Position, Loop Length

#### UI Behavior

The UI parameter boxes are the source-of-truth for all values. The handles and boxes are always in sync with the
following mapping:

**Handle to Box Mapping**
| Dragging Handle | Changes Parameter Box |
| --------------- | -------------------------- |
| Loop Start | Loop Position, Loop Length |
| Loop End | Loop Length |
| Loop Brace | Loop Position |
| Start Marker | Start |
| End Marker | End |

**Box to Handle Mapping**
| Changing Box Value | Moves Handle |
| ------------------ | -------------------------- |
| Start | Start Marker |
| End | End Marker |
| Loop Position | Loop Brace (Start and End) |
| Loop Length | Loop End |

**Other Behavior:**

- When looping is on, dragging a Loop Handle will also move the Start/End Marker Handle if they are at the same
  position. This coupling breaks once they are separated.
- When looping is turned off, the end marker and timeline extent are reconciled:
  - If the clip length in the timeline is shorter than the marker span, the end marker is clamped to fit within the
    timeline
  - If the clip length in the timeline is longer, it is shortened to match the end marker.
  - In either case, the resulting timeline extent equals the marker span, and the clip will never grow larger on the
    timeline.

#### Clean API model

The strange (and frankly buggy) behaviors of the API can be reconciled by reframing the parameter names in the following
way:

**When Looping is On:**

Both handle sets may be controlled.

| API name     | Mental Name  | Description                                                                  |
| ------------ | ------------ | ---------------------------------------------------------------------------- |
| loop_start   | Loop Start   | Controls the Loop Start Handle.                                              |
| loop_end     | Loop End     | Controls the Loop End Handle.                                                |
| start_marker | Start Marker | Controls where clip playback will start from, followed by normal loop range. |
| end_marker   | End Marker   | Has no effect in during loop playback, but will move the inactive handle.    |

**When Looping is Off:**

Only the start/end marker handles may be controlled.

| API name     | Mental Name  | Description                       |
| ------------ | ------------ | --------------------------------- |
| loop_start   | Start Marker | Controls the Start Marker Handle. |
| loop_end     | End Marker   | Controls the End Marker Handle.   |
| start_marker | N/A          | Invalid when looping off.         |
| end_marker   | N/A          | Invalid when looping off.         |

**At All Times:**

| API name | Mental Name    | Description                                              |
| -------- | -------------- | -------------------------------------------------------- |
| looping  | Looping Toggle | Enable (or Disable) the looping mode.                    |
| length   | Loop Length    | The length of the looping region, whether active or not. |

**In Arrangements:**

| API name   | Mental Name     | Description                           |
| ---------- | --------------- | ------------------------------------- |
| start_time | Clip Start Time | When the clip starts in the Timeline. |
| end_time   | Clip End Time   | When the clip ends in the Timeline.   |

**In Sessions:**

| API name   | Mental Name | Description                        |
| ---------- | ----------- | ---------------------------------- |
| start_time | Fired At    | Song time when the clip was fired. |
| end_time   | N/A         | Not super useful.                  |

Full details: `.tmp/Probe_timing_findings.md`.

### Children

| Child  | Returns     | Shape    | Access | Listenable | Available Since | Summary                    |
| ------ | ----------- | -------- | ------ | ---------- | --------------- | -------------------------- |
| `view` | `Clip.View` | `single` | `get`  | `no`       | `<11`           | View aspects of this clip. |

#### `view`

- **Returns:** `Clip.View`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Provides access to view-related state: grid quantization settings and envelope visibility
controls. See the `Clip.View` section at the bottom of this file.

### Properties

| Property                | Get Returns        | Set Accepts    | Listenable | Available Since | Summary                                                                                           |
| ----------------------- | ------------------ | -------------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------- |
| `automation_envelopes`  | `list`             | —              | `no`       | `12.2`          | Read-only list of all automation envelopes for this clip.                                         |
| `available_warp_modes`  | `list[int]`        | —              | `no`       | `<11`           | Audio only. Indexes of warp modes available for this clip.                                        |
| `canonical_parent`      | `object`           | —              | `no`       | `<11`           | The clip's parent object (ClipSlot or Track).                                                     |
| `color`                 | `int`              | `int`          | `yes`      | `<11`           | Clip color as packed RGB `0x00rrggbb`.                                                            |
| `color_index`           | `int`              | `int`          | `yes`      | `<11`           | Clip color palette index.                                                                         |
| `end_marker`            | `float`            | `float`        | `yes`      | `<11`           | End marker position in beats. Only functional when looping is ON.                                 |
| `end_time`              | `float`            | —              | `yes`      | `<11`           | Arrangement: timeline end position. Session: derived, not very useful.                            |
| `file_path`             | `str`              | —              | `no`       | `<11`           | Audio only. Absolute path to the referenced audio file.                                           |
| `gain`                  | `float`            | `float`        | `yes`      | `<11`           | Audio only. Clip gain, range `0.0` to `1.0`.                                                      |
| `gain_display_string`   | `str`              | —              | `no`       | `<11`           | Audio only. Gain as a human-readable string (e.g. `"1.3 dB"`).                                    |
| `groove`                | `Groove\|None`     | `Groove\|None` | `yes`      | `11.0`          | Groove object associated with this clip, or `None`.                                               |
| `has_envelopes`         | `bool`             | —              | `yes`      | `<11`           | `True` if the clip has any automation envelopes.                                                  |
| `has_groove`            | `bool`             | —              | `no`       | `11.0`          | `True` if a groove is associated with this clip.                                                  |
| `is_arrangement_clip`   | `bool`             | —              | `no`       | `<11`           | `True` for clips in Arrangement View (includes Take Lane clips).                                  |
| `is_audio_clip`         | `bool`             | —              | `no`       | `<11`           | `True` for audio clips.                                                                           |
| `is_midi_clip`          | `bool`             | —              | `no`       | `<11`           | `True` for MIDI clips. Opposite of `is_audio_clip`.                                               |
| `is_overdubbing`        | `bool`             | —              | `yes`      | `<11`           | Session only. `True` while the clip is overdubbing.                                               |
| `is_playing`            | `bool`             | —              | `no`       | `<11`           | Session only. `True` if the clip is playing or recording.                                         |
| `is_recording`          | `bool`             | —              | `yes`      | `<11`           | Session only. `True` if the clip is recording.                                                    |
| `is_session_clip`       | `bool`             | —              | `no`       | `12.2`          | `True` for clips in Session View.                                                                 |
| `is_take_lane_clip`     | `bool`             | —              | `no`       | `12.2`          | `True` for Take Lane clips (also arrangement clips).                                              |
| `is_triggered`          | `bool`             | —              | `no`       | `<11`           | Session only. `True` while the Clip Launch button is blinking (queued).                           |
| `launch_mode`           | `int`              | `int`          | `yes`      | `11.0`          | Launch mode (0=Trigger, 1=Gate, 2=Toggle, 3=Repeat).                                              |
| `launch_quantization`   | `int`              | `int`          | `yes`      | `11.0`          | Per-clip launch quantization override (0=Global, 1=None, 2–14=grids).                             |
| `legato`                | `bool`             | `bool`         | `yes`      | `11.0`          | `True` if the Legato switch is on for this clip.                                                  |
| `length`                | `float`            | —              | `no`       | `<11`           | Always `loop_end - loop_start`, regardless of loop state or markers.                              |
| `loop_end`              | `float`            | `float`        | `yes`      | `<11`           | Loop region end (loop ON), or end marker alias (loop OFF).                                        |
| `loop_jump`             | `bang`             | —              | `yes`      | `<11`           | Fires when the playhead crosses the loop start marker.                                            |
| `loop_start`            | `float`            | `float`        | `yes`      | `<11`           | Loop region start (loop ON), or start marker alias (loop OFF).                                    |
| `looping`               | `bool`             | `bool`         | `yes`      | `<11`           | `True` if looping is enabled. Unwarped audio cannot be looped.                                    |
| `muted`                 | `bool`             | `bool`         | `yes`      | `<11`           | `True` if the clip's Clip Activator is off (muted).                                               |
| `name`                  | `str`              | `str`          | `yes`      | `<11`           | Clip display name.                                                                                |
| `notes`                 | `bang`             | —              | `yes`      | `<11`           | MIDI only. Fires when the note list changes.                                                      |
| `pitch_coarse`          | `int`              | `int`          | `yes`      | `<11`           | Audio only. Transpose in semitones, `-48` to `48`.                                                |
| `pitch_fine`            | `float`            | `float`        | `yes`      | `<11`           | Audio only. Detune in cents, `-50` to `49`.                                                       |
| `playing_position`      | `float`            | —              | `yes`      | `<11`           | Session only. Current playhead position in beats or seconds.                                      |
| `playing_status`        | `bang`             | —              | `yes`      | `<11`           | Fires when playing/trigger status changes.                                                        |
| `position`              | `float`            | `float`        | `yes`      | `<11`           | Always equals `loop_start` on get; set slides loop window preserving length.                      |
| `ram_mode`              | `bool`             | `bool`         | `yes`      | `<11`           | Audio only. `True` if the RAM switch is enabled.                                                  |
| `sample_length`         | `int`              | —              | `no`       | `<11`           | Audio only. Sample length in samples.                                                             |
| `sample_rate`           | `float`            | —              | `no`       | `11.0`          | Audio only. Sample rate of the clip's audio file.                                                 |
| `signature_denominator` | `int`              | `int`          | `yes`      | `<11`           | Clip time signature denominator.                                                                  |
| `signature_numerator`   | `int`              | `int`          | `yes`      | `<11`           | Clip time signature numerator.                                                                    |
| `start_marker`          | `float`            | `float`        | `yes`      | `<11`           | Start marker position in beats. Setter silently ignored when loop OFF.                            |
| `start_time`            | `float`            | —              | `yes`      | `<11`           | Arrangement: timeline start position. Session: song time when fired.                              |
| `velocity_amount`       | `float`            | `float`        | `yes`      | `11.0`          | How much trigger note velocity affects clip volume, `0.0` to `1.0`.                               |
| `warp_markers`          | `list[WarpMarker]` | —              | `yes`      | `11.0`          | Audio only. Warp markers as a list (not dict); observable fires bang on change.                   |
| `warp_mode`             | `int`              | `int`          | `yes`      | `<11`           | Audio only. Warp mode (0=Beats, 1=Tones, 2=Texture, 3=Re-Pitch, 4=Complex, 5=REX, 6=Complex Pro). |
| `warping`               | `bool`             | `bool`         | `yes`      | `<11`           | Audio only. `True` if the Warp switch is on. Setting is internally deferred by Live.              |
| `will_record_on_start`  | `bool`             | —              | `no`       | `<11`           | Documented as `True` when recording will start. Currently always returns `False`.                 |

#### `automation_envelopes`

- **Get Returns:** `list`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `12.2`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Read-only list of all automation envelopes currently present on this clip. Returns `Envelope`
objects. Use `automation_envelope(parameter)` to get the envelope for a specific parameter,
or `create_automation_envelope(parameter)` to create one.

#### `available_warp_modes`

- **Get Returns:** `list[int]`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
List of integer indexes of warp modes available for this clip. Cross-reference with the
`warp_mode` value table. Not all warp modes are available for all audio material.

**Probe results:** Returns `[0, 1, 2, 3, 4, 6]` for a standard audio clip — REX mode (5)
is not available.

#### `canonical_parent`

- **Get Returns:** `object`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns the clip's canonical parent object. For session clips this is the `ClipSlot`; for
arrangement clips this is the `Track`.

#### `color`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Clip color as a packed RGB value `0x00rrggbb`. When setting, Live snaps to the nearest
color in the clip color chooser. Setting `color` to `None` raises an `InternalError`
(C++ type mismatch; confirmed in probes).

#### `color_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Palette-based color index for the clip. Clips always have a color in the Live UI, so `None`
is not a valid value — setting to `None` raises an `InternalError` (confirmed in probes).

#### `end_marker`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**

**When loop is ON:** Position of the clip's end marker in beats (the lower bar of the clip detail
view). The end marker has no effect on loop playback but its handle position is maintained.
**When loop is OFF:** Invalid parameter. setter is accepted by the API (value changes on readback)
but the UI handle does not move, and the API value is overwritten by the UI handle position when
looping is toggled back on. Effectively a phantom write — use `loop_end` to control the end bound
when looping is off.

#### `end_time`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Context-dependent read-only value with very different semantics per context:

- **Arrangement:** timeline end position in beats. Will change when looping is turned off
  and the current `end_marker - start_marker` is less than the clip timeline length.
- **Session:** a derived value that is not particularly useful. Equals
  `max(loop_end - start_marker, loop_end - loop_start)` when looping is on (i.e. the loop
  iteration length, extended by the intro if `start_marker < loop_start`). Equals
  `end_marker - start_marker` when looping is off. Not recommended for direct use.

#### `file_path`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Absolute path to the audio file referenced by this clip. Not available for MIDI clips.

#### `gain`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Clip gain, range `0.0` to `1.0`. Only available for audio clips.

#### `gain_display_string`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Gain as a human-readable display string (e.g. `"1.3 dB"`). Read-only.

#### `groove`

- **Get Returns:** `Groove | None`
- **Set Accepts:** `Groove | None`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `probed`

**Description:**
The Groove object applied to this clip. Groove objects are accessed via `Song.groove_pool`.
Setting to `None` to remove the groove is **not possible** via the Python API — the C++ setter
requires `TPyHandle<AAbstractGroove>` and rejects `NoneType`. The Live UI's "None" dropdown
uses an internal code path. The UI's "Commit Groove" button (which bakes groove offsets into
note data / warp markers) is also not exposed — `commit_groove`, `apply_groove`, `bake_groove`,
`flatten_groove` all probed and do not exist. Confirmed limitations.

#### `has_envelopes`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` if the clip contains any automation envelopes. Fires listener when envelopes are added
or removed.

#### `has_groove`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
`True` if a groove is associated with this clip. Convenience check; prefer `groove is not None`.

#### `is_arrangement_clip`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for clips in Arrangement View. Take Lane clips are also arrangement clips
(`is_take_lane_clip` and `is_arrangement_clip` can both be `True`).

#### `is_audio_clip`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for audio clips. Use to gate audio-only members before accessing them.

#### `is_midi_clip`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for MIDI clips. Exact opposite of `is_audio_clip`.

#### `is_overdubbing`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `session`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` while the clip is overdubbing (playing while recording additional material).
Always `False` on arrangement clips (confirmed by probe).

#### `is_playing`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `session`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` if the clip is currently playing or recording. Always `False` on arrangement clips,
even while the transport plays through the clip's time range (confirmed by probe). Treat as
read-only; use `fire()` and `stop()` to control playback.

#### `is_recording`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `session`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` if the clip is currently recording. Always `False` on arrangement clips (confirmed by probe).

#### `is_session_clip`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `12.2`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for clips in Session View. A clip is either a session clip or an arrangement clip.

#### `is_take_lane_clip`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `12.2`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
`True` for Take Lane clips. These are a subtype of arrangement clips;
`is_arrangement_clip` is also `True` for these.

#### `is_triggered`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `session`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` while the Clip Launch button is blinking (launch queued, waiting on quantization).
Always `False` on arrangement clips (confirmed by probe).

#### `launch_mode`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Launch mode as an integer. Values:

- `0` = Trigger (default)
- `1` = Gate
- `2` = Toggle
- `3` = Repeat

#### `launch_quantization`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Per-clip launch quantization, overrides the song's global quantization when set. Values:
`0`=Global (default), `1`=None, `2`=8 Bars, `3`=4 Bars, `4`=2 Bars, `5`=1 Bar, `6`=1/2,
`7`=1/2T, `8`=1/4, `9`=1/4T, `10`=1/8, `11`=1/8T, `12`=1/16, `13`=1/16T, `14`=1/32.

#### `legato`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
`True` when the Legato switch in the clip's Launch settings is on.

#### `length`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Always equals `loop_end - loop_start`, regardless of whether looping is enabled and regardless
of marker positions. This is NOT `end_marker - start_marker`. Units are beats for MIDI and
warped audio; seconds for unwarped audio.

#### `loop_end`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**  
**When loop is ON:** controls the Loop End Handle (top marker bar, right edge of the loop
brace). Independent of `end_marker`.  
**When loop is OFF:** aliases the End Marker Handle — setting `loop_end` moves the end marker
and adjusts the clip's timeline extent (arrangement) or playback length. This is the **only**
way to control the end bound when looping is off.  
Units are beats for MIDI and warped audio; seconds (from first sample) for unwarped audio.

#### `loop_jump`

- **Get Returns:** `bang` (no value)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Observable that fires when the clip playhead crosses the loop start marker (or its projection
into the loop for nested loop scenarios). Used to detect loop cycles. Confirmed firing on
short looping clips (probed 12.3.5).

#### `loop_start`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**  
**When loop is ON:** controls the Loop Start Handle (top marker bar, left edge of the loop
brace). Independent of `start_marker`.  
**When loop is OFF:** aliases the Start Marker Handle — setting `loop_start` moves the start
marker and adjusts the clip's timeline extent (arrangement) or playback start. This is the **only**
way to control the start bound when looping is off; `start_marker` writes are silently ignored in
that state.  
Units are beats for MIDI and warped audio; seconds for unwarped audio (where `0` = first sample).  
Beat time `0` corresponds to position `1.1.1` in the clip view ruler.

#### `looping`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**  
`True` if clip looping is enabled. Toggling this switches which marker system is "active" —
with loop ON, `loop_start`/`loop_end` control the loop brace independently of the markers;
with loop OFF, they alias the start/end markers.  
**Toggle ON -> OFF clamping (arrangement):** The end marker and timeline extent are reconciled — if
the timeline is shorter than the marker span, the end marker is clamped; if longer, the timeline
shrinks. The clip never grows on toggle.  
**Toggle OFF -> ON:** the UI's saved loop marker positions are restored (the loop brace
returns to where it was before looping was disabled). MIDI and warped audio behave identically.  
Unwarped audio clips cannot be looped.

#### `muted`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
`True` when the clip's Clip Activator button is off (clip is deactivated/muted).

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Display name of the clip.

#### `notes`

- **Get Returns:** `bang` (no value)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Observable that fires when the clip's note list changes. Use `get_notes_extended()` or
`get_all_notes_extended()` to retrieve the current notes after receiving this notification.
Confirmed firing on note add (probed 12.3.5).

#### `pitch_coarse`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Pitch transposition in semitones (Transpose knob). Range: `-48` to `48`.

#### `pitch_fine`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Fine pitch adjustment in cents (Detune knob). Range: `-50` to `49`.

#### `playing_position`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `session`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Current playhead position. For MIDI and warped audio clips: beats of absolute clip time,
where beat `0` = position `1` in the clip ruler. For unwarped audio: seconds from clip
start. Stopped clips return `0`. Always `0.0` on arrangement clips, even during transport
playback (confirmed by probe).

#### `playing_status`

- **Get Returns:** `bang` (no value)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Observable that fires when the clip's playing or trigger status changes. Has no readable value
itself; use `is_playing`, `is_recording`, `is_triggered` to read current state after receiving
the notification. Confirmed firing on clip launch (probed 12.3.5).

#### `position`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Loop position / window slide control. On get, always equals `loop_start` (confirmed in every
state tested). On set, moves `loop_start` to the specified position and adjusts `loop_end` to
preserve `length` (unlike setting `loop_start` directly, which changes `length`). Works in
both loop ON and OFF modes. **Side effect:** when the new loop window extends past
`start_marker` or `end_marker`, those markers are auto-pushed to stay within/at the loop bounds.

#### `ram_mode`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` when the clip's RAM mode switch is enabled. Only available for audio clips.

#### `sample_length`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Length of the clip's audio sample in samples (not beats). Useful for `add_warp_marker`
range validation.

#### `sample_rate`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `audio`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Sample rate of the clip's audio file in Hz.

#### `signature_denominator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Clip time signature denominator. Controls the clip's internal meter display.

#### `signature_numerator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Clip time signature numerator.

#### `start_marker`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**  
**When loop is ON:** Position of the clip's start marker in beats (lower bar of the clip
detail view). Fully independent of `loop_start`. Playback always starts here and goes until
`loop_end` before looping back to `loop_start`. Used in this way, it can definie an "intro"
or shorter first loop.  
**When loop is OFF:** setter is **silently ignored** — the API value does not change. Use
`loop_start` to control the start bound in this state.

#### `start_time`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**  
Context-dependent start time in beats (read-only):

- **Arrangement clips:** start position within the arrangement timeline.
- **Session clips:** song time (beat position) when the clip was fired. Updates each time
  the clip is launched.

#### `velocity_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `session`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Controls how much the velocity of the MIDI note triggering the clip affects the clip's
volume. `0.0` = no effect; `1.0` = full effect.

#### `warp_markers`

- **Get Returns:** `list[WarpMarker]` (WarpMarkerVector)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
The clip's warp markers as a **list** (not dict as Max docs state). Returns a
`WarpMarkerVector` containing `WarpMarker` objects, each with `beat_time: float` and
`sample_time: float` fields. The bridge encodes these as typed dicts with
`_pfl_type: "WarpMarker"`.

The last marker in the list is a **phantom marker** (1/32 beat after the last visible marker)
used internally to derive the BPM of the final segment — it is not shown in the Live UI.
Attempting to `move_warp_marker` or `remove_warp_marker` on the phantom marker raises a runtime
error.

**Important:** `WarpMarker.sample_time` is in **seconds**, not samples, despite the field
name. This differs from `beat_to_sample_time()` which returns values in samples.

The observable fires a bang when markers change; re-read the property to get the updated value.

#### `warp_mode`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Warp mode as an integer. Must be one of the values in `available_warp_modes`. Values:

- `0` = Beats
- `1` = Tones
- `2` = Texture
- `3` = Re-Pitch
- `4` = Complex
- `5` = REX
- `6` = Complex Pro

#### `warping`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Yes`
  - **Async visibility:** `deferred`
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
`True` when the Warp switch is enabled. **Known quirk (from Live documentation):** setting
this property is internally deferred. In sequences of API calls within a single event, the
actual order of operations may differ from the call order. If sequencing with other calls
that depend on `warping`, introduce a tick delay between the set and the dependent operation.

#### `will_record_on_start`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `midi`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5) — non-functional`

**Description:**
Documented as `True` for MIDI clips in triggered state when the track is armed and MIDI
Arrangement Overdub is enabled. However, probing shows it **always returns `False`** through
the Python API — even while the clip is actively recording/overdubbing (`is_recording=True`,
`is_overdubbing=True`). Same non-functional behavior as `ClipSlot.will_record_on_start`. May
only function through the Max LOM path or within listener callback contexts. Recording state
is already covered by `is_recording` and `is_overdubbing`.

### Methods

| Signature                                                                                | Returns          | Available Since | Summary                                                             |
| ---------------------------------------------------------------------------------------- | ---------------- | --------------- | ------------------------------------------------------------------- |
| `add_new_notes(notes: tuple[MidiNoteSpecification, ...])`                                | `list[int]`      | `11.0`          | MIDI only. Add new notes; returns list of assigned note IDs.        |
| `add_warp_marker(warp_marker: WarpMarker)`                                               | `None`           | `11.0.5`        | Audio only. Add a warp marker.                                      |
| `apply_note_modifications(notes: MidiNoteVector)`                                        | `None`           | `11.0`          | MIDI only. Modify existing notes in-place by note ID.               |
| `automation_envelope(device_parameter)`                                                  | `Envelope\|None` | `<11`           | Return the envelope for a given parameter, or `None`.               |
| `beat_to_sample_time(beat_time)`                                                         | `float`          | `<11`           | Audio only. Convert beat time to sample time (warped clips).        |
| `clear_all_envelopes()`                                                                  | `None`           | `<11`           | Remove all automation envelopes from the clip.                      |
| `clear_envelope(device_parameter)`                                                       | `None`           | `<11`           | Remove the automation envelope for a specific parameter.            |
| `create_automation_envelope(device_parameter)`                                           | `Envelope`       | `<11`           | Create and return an envelope for a given parameter.                |
| `crop()`                                                                                 | `None`           | `<11`           | Crop clip to loop or start/end markers.                             |
| `deselect_all_notes()`                                                                   | `None`           | `<11`           | MIDI only. Deselect all notes.                                      |
| `duplicate_loop()`                                                                       | `None`           | `<11`           | MIDI only. Double the loop length and duplicate notes/envelopes.    |
| `duplicate_notes_by_id(note_ids, destination_time=None, transposition_amount=0)`         | `list[int]`      | `11.1.2`        | MIDI only. Duplicate specific notes by ID. Returns new IDs.         |
| `duplicate_region(region_start, region_length, destination_time, pitch=-1, transpose=0)` | `None`           | `<11`           | MIDI only. Duplicate all notes in a region to a destination time.   |
| `fire()`                                                                                 | `None`           | `<11`           | Session only. Same as pressing the Clip Launch button.              |
| `get_all_notes_extended(return_fields=None)`                                             | `MidiNoteVector` | `11.1`          | MIDI only. Return all notes regardless of markers.                  |
| `get_notes(from_time, from_pitch, time_span, pitch_span)`                                | `tuple`          | `<11`           | **Deprecated.** MIDI only. Return notes as tuples.                  |
| `get_notes_by_id(note_ids, return_fields=None)`                                          | `MidiNoteVector` | `11.0`          | MIDI only. Return notes matching the given IDs.                     |
| `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields=None)`   | `MidiNoteVector` | `11.0`          | MIDI only. Return notes in a pitch/time region.                     |
| `get_selected_notes()`                                                                   | `tuple`          | `<11`           | **Deprecated.** MIDI only. Return selected notes as tuples.         |
| `get_selected_notes_extended(return_fields=None)`                                        | `MidiNoteVector` | `11.0`          | MIDI only. Return currently selected notes.                         |
| `move_playing_pos(beats)`                                                                | `None`           | `<11`           | Session only. Relative jump of clip playhead in beats, unquantized. |
| `move_warp_marker(beat_time, beat_time_distance)`                                        | `None`           | `11.0`          | Audio only. Move a warp marker by a relative beat distance.         |
| `note_number_to_name(midi_pitch)`                                                        | `str`            | `12.1`          | MIDI only. Convert MIDI note number to human-readable name.         |
| `quantize(quantization_grid, amount)`                                                    | `None`           | `<11`           | MIDI only. Quantize all notes.                                      |
| `quantize_pitch(pitch, quantization_grid, amount)`                                       | `None`           | `<11`           | MIDI only. Quantize notes of a specific pitch.                      |
| `remove_notes(from_time, from_pitch, time_span, pitch_span)`                             | `None`           | `<11`           | **Deprecated.** MIDI only. Delete notes in a region.                |
| `remove_notes_by_id(note_ids)`                                                           | `None`           | `11.0`          | MIDI only. Delete specific notes by ID.                             |
| `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)`                    | `None`           | `11.0`          | MIDI only. Delete all notes starting in a region.                   |
| `remove_warp_marker(beat_time)`                                                          | `None`           | `11.0`          | Audio only. Remove a warp marker at the given beat time.            |
| `replace_selected_notes(notes_tuple)`                                                    | `None`           | `<11`           | **Deprecated.** MIDI only. Replace selected notes with tuple data.  |
| `sample_to_beat_time(sample_time)`                                                       | `float`          | `<11`           | Audio only. Convert sample time to beat time (warped clips).        |
| `scrub(beat_time)`                                                                       | `None`           | `<11`           | Session only. Audition a looping snippet at a position.             |
| `seconds_to_sample_time(seconds)`                                                        | `float`          | `<11`           | Audio only. Convert seconds to sample time (unwarped clips).        |
| `select_all_notes()`                                                                     | `None`           | `<11`           | MIDI only. Select all notes.                                        |
| `select_notes_by_id(note_ids)`                                                           | `None`           | `11.0.6`        | MIDI only. Select specific notes by ID.                             |
| `set_fire_button_state(state: bool)`                                                     | `None`           | `<11`           | Programmatically hold or release the clip launch button.            |
| `set_notes(notes_tuple)`                                                                 | `None`           | `<11`           | **Deprecated.** MIDI only. Add notes from tuple data.               |
| `stop()`                                                                                 | `None`           | `<11`           | Session only. Stop this clip if it is playing or recording.         |
| `stop_scrub()`                                                                           | `None`           | `<11`           | Session only. End an active scrub session.                          |

#### `add_new_notes(notes)`

- **Returns:** `list[int]` — list of note IDs for the added notes
- **Args:** `notes: tuple[MidiNoteSpecification, ...]` — a **tuple** of `Live.Clip.MidiNoteSpecification` objects
- **Raises/Errors:** `InternalError` if passed dicts or a list instead of a tuple of `MidiNoteSpecification`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Adds new notes to the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Adds notes to the clip. The argument must be a **tuple** of `Live.Clip.MidiNoteSpecification`
objects — **not** a list of dicts. The Max for Live documentation describes a dict-based API,
but that is a Max-specific convenience; the raw Python API requires the native C++ type.

`MidiNoteSpecification` is constructed with keyword args:

```python
import Live
spec = Live.Clip.MidiNoteSpecification(
    pitch=60,          # int, required: MIDI note number 0–127
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

Returns the list of integer note IDs assigned to the new notes. The bridge converts
client-side note dicts into `MidiNoteSpecification` objects automatically.

#### `add_warp_marker(warp_marker)`

- **Returns:** `None`
- **Args:** `warp_marker: Live.Clip.WarpMarker` — native C++ `TWarpMarker` type
- **Raises/Errors:** `Segment length out of range` if resulting segment BPM exceeds `[5, 999]` or if a marker already
  exists at the same `beat_time` with a different `sample_time`; `Warp marker sample time is out of range` if
  sample_time exceeds clip duration. Adding a duplicate marker with the same `beat_time` and `sample_time` as an
  existing marker is a silent no-op.
- **Applicable to:** `audio`
- **Undo-tracked:** `Yes`
- **Side Effects:** Adds a warp marker to the clip.
- **Async visibility:** `immediate`
- **Available Since:** `11.0.5`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Adds a warp marker. The argument is a `Live.Clip.WarpMarker` object, **not** a dict.

**Constructor:** `Live.Clip.WarpMarker(sample_time, beat_time)` — note the argument order:
`sample_time` comes **first**. Does **not** accept keyword arguments. The C++ signature is:

```
__init__(_object*, double sample_time, double beat_time)
```

**Important:** `sample_time` is in **seconds** (not samples). The bridge transform converts
client-side dicts `{"beat_time": float, "sample_time": float}` into native `WarpMarker`
objects automatically.

When the client omits `sample_time`, the typed API computes it via `beat_to_sample_time()`
divided by `sample_rate` to get seconds, preserving the current warp mapping.

#### `apply_note_modifications(notes)`

- **Returns:** `None`
- **Args:** `notes: MidiNoteVector` — the **original vector** returned by `get_all_notes_extended` (or similar), with
  attributes modified in-place
- **Raises/Errors:** `InternalError: Python argument types did not match C++ signature` if passed a Python `list`
  instead of the native `MidiNoteVector`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Modifies existing notes matched by note ID.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
In-place modification of existing notes. The intended workflow is:

1. `notes = clip.get_all_notes_extended()` — returns a `MidiNoteVector`
2. Modify note attributes in-place: `notes[0].velocity = 50`
3. `clip.apply_note_modifications(notes)` — pass the **same vector** back

**Critical:** The argument must be the original `MidiNoteVector` object (a Boost.Python-wrapped
`std::vector<NClipApi::TNoteInfo>`). Passing a plain Python `list` of `MidiNote` objects raises
`InternalError` because Boost.Python cannot convert `list` to the native vector type. The Max
for Live documentation describes a dict-based API, but that is a Max-specific convenience layer;
the raw Python API requires the native C++ type.

The bridge handles this automatically: it fetches the real `MidiNoteVector` from the clip,
applies the requested modifications to matching notes (by `note_id`), and passes the original
vector back to Live. Unmodified notes in the vector retain their values harmlessly.

#### `automation_envelope(device_parameter)`

- **Returns:** `Envelope | None`
- **Args:** `device_parameter: DeviceParameter`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session` (returns `None` for Arrangement clips)
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns the automation envelope for the given device parameter, or `None` if no envelope
exists for that parameter. Always returns `None` for Arrangement clips. Also returns `None`
if the parameter belongs to a device on a different track.

#### `beat_to_sample_time(beat_time)`

- **Returns:** `float` — sample time in **samples** (not seconds)
- **Args:** `beat_time: float`
- **Raises/Errors:** Error if clip is not warped.
- **Applicable to:** `audio`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Converts a beat time to the corresponding sample time for warped audio clips. Returns the
value in **samples** (not seconds). At 120 BPM with 48kHz sample rate,
`beat_to_sample_time(1.0)` returns `24000.0`. Raises an error if the clip is not warped.

**Important:** The return unit (samples) differs from `WarpMarker.sample_time` which is in
seconds. Divide by `sample_rate` to convert.

#### `clear_all_envelopes()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes all automation envelopes from the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Deletes all clip-level automation envelopes.

#### `clear_envelope(device_parameter)`

- **Returns:** `None`
- **Args:** `device_parameter: DeviceParameter`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes the automation envelope for the given parameter.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Removes the clip's automation envelope for a specific device parameter.

#### `create_automation_envelope(device_parameter)`

- **Returns:** `Envelope`
- **Args:** `device_parameter: DeviceParameter`
- **Raises/Errors:** Error if the envelope can't be created.
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Creates an automation envelope on the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Creates and returns an automation envelope for the given device parameter. Should only be
called if the envelope doesn't already exist — use `automation_envelope(parameter)` first to
check. Raises an error if the envelope can't be created.

#### `crop()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Trims the clip content to the loop region (if looped) or the start/end marker region.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
If the clip is looped, removes content outside the loop. If not looped, removes content
outside the start/end markers.

#### `deselect_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** Deselects all notes in the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Deselects all notes in the clip. Useful before calling `replace_selected_notes` when you
only want to add notes rather than replace existing selected ones.

#### `duplicate_loop()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Doubles the loop length; duplicates notes and envelopes into the new half.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Doubles the loop by moving `loop_end` to the right and duplicating all notes and envelopes
into the new region. If not looped, doubles the clip start/end range instead.

#### `duplicate_notes_by_id(note_ids, destination_time=None, transposition_amount=0)`

- **Returns:** `list[int]` — note IDs of the newly created duplicate notes
- **Args:**
  - `note_ids: list[int]` — IDs of notes to duplicate (or a dict with `"note_ids"` key)
  - `destination_time: float (optional)` — beat time to place duplicates; defaults to after the last selected note
  - `transposition_amount: int (optional)` — semitones to transpose duplicates; defaults to `0`
- **Raises/Errors:** Error on audio clips. Error if note IDs don't match existing notes.
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Creates duplicate notes in the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `11.1.2`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Duplicates all notes matching the given IDs. If `destination_time` is not provided, the
duplicates are placed after the last selected note (same behavior as duplicating notes in
the Live GUI). If `transposition_amount` is specified, the duplicated notes are transposed
by that many semitones. Returns the note IDs assigned to the new copies. **Preserves
per-note expression envelopes (MDE)** on the copies (confirmed by probe).

#### `duplicate_region(region_start, region_length, destination_time, pitch=-1, transposition_amount=0)`

- **Returns:** `None`
- **Args:**
  - `region_start: float` — start of the region in beats
  - `region_length: float` — length of the region in beats
  - `destination_time: float` — beat time to place the duplicated notes
  - `pitch: int (optional)` — only duplicate notes of this pitch; `-1` = all pitches (default)
  - `transposition_amount: int (optional)` — semitones to transpose; defaults to `0`
- **Raises/Errors:** Error on audio clips.
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Creates duplicate notes in the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Duplicates all notes in the specified time region to `destination_time`. If `pitch` is
specified (not `-1`), only notes of that pitch are duplicated. If `transposition_amount`
is non-zero, the duplicated notes are transposed by that many semitones. **Preserves
per-note expression envelopes (MDE)** on the copies (confirmed by probe).

#### `fire()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session`
- **Undo-tracked:** `no`
- **Side Effects:** Same as pressing the Clip Launch button.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Launches this clip. Equivalent to pressing the Clip Launch button in the UI. No-op on
arrangement clips — does not start transport or trigger the clip (confirmed by probe).

#### `get_all_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector` — a Boost.Python-wrapped `std::vector<NClipApi::TNoteInfo>` of `MidiNote` objects
- **Args:** `return_fields: dict (optional)` — `{"return": [field_names]}` to limit returned fields
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `11.1`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Returns all notes in the clip regardless of their position relative to start/end markers and
loop markers. Returns a `MidiNoteVector` — a native C++ vector type, NOT a Python dict with a
`"notes"` key (the Max for Live docs describe a dict-based return, but that is a Max-specific
convenience layer). Each element is a `MidiNote` object with writable attributes: `note_id`,
`pitch`, `start_time`, `duration`, `velocity`, `mute`, `probability`, `velocity_deviation`,
`release_velocity`.

The bridge encodes these as a list of dicts (with `_pfl_type: "MidiNote"`) for JSON transport.

The returned vector is the same type expected by `apply_note_modifications()` — modify
attributes in-place and pass the vector back to commit changes.

#### `get_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `tuple` — tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:**
  - `from_time: float` — start of time region
  - `from_pitch: int` — lowest pitch
  - `time_span: float` — length of time region
  - `pitch_span: int` — number of pitches
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
**Deprecated.** Returns notes as a tuple of 5-element tuples `(pitch, time, duration,
velocity, mute)`. Superseded by `get_notes_extended()` which returns richer note dicts
with `note_id`, `probability`, `velocity_deviation`, and `release_velocity`.

#### `get_notes_by_id(note_ids, return_fields=None)`

- **Returns:** `MidiNoteVector` — same native vector type as `get_all_notes_extended`
- **Args:**
  - `note_ids: object` — list of note IDs
  - `return_fields: dict (optional)` — `{"return": [field_names]}`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Returns the notes matching the given IDs. Note IDs must correspond to existing notes.

#### `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields=None)`

- **Returns:** `MidiNoteVector` — native Boost.Python `std::vector<NClipApi::TNoteInfo>`
- **Args:**
  - `from_pitch: int` — lowest pitch to include
  - `pitch_span: int` — number of pitches to include
  - `from_time: float` — start of time region in beats
  - `time_span: float` — length of time region in beats
  - `return_fields: dict (optional)`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Returns notes whose start times fall within the given region as a `MidiNoteVector` — the
same native C++ vector type returned by `get_all_notes_extended()`. Replaces the deprecated
`get_notes`. Can also be called with a single dict argument containing all parameter names
as keys.

The bridge encodes these as a list of dicts (with `_pfl_type: "MidiNote"`) for JSON transport.

#### `get_selected_notes()`

- **Returns:** `tuple` — tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
**Deprecated.** Returns selected notes as a tuple of 5-element tuples. Superseded by
`get_selected_notes_extended()`.

#### `get_selected_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector` — native Boost.Python `std::vector<NClipApi::TNoteInfo>`
- **Args:** `return_fields: dict (optional)`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Returns the currently selected notes in the clip as a `MidiNoteVector` — the same native
C++ vector type returned by `get_all_notes_extended()`. Replaces the deprecated
`get_selected_notes`.

The bridge encodes these as a list of dicts (with `_pfl_type: "MidiNote"`) for JSON transport.

#### `move_playing_pos(beats)`

- **Returns:** `None`
- **Args:** `beats: float` — relative jump in beats; negative = backwards
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session`
- **Undo-tracked:** `no`
- **Side Effects:** Moves the clip's internal playhead by the given amount.
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Relative unquantized jump from the current playhead position within the clip's local timeline.
Does not affect the global song playhead. Positive values jump forward, negative values jump
backward. Probing confirms: `move_playing_pos(2.0)` moves ~2 beats forward, `move_playing_pos(-1.0)`
moves ~1 beat backward. No-op when the clip is stopped (position stays `0.0`). Cannot be called
on unwarped audio clips, recording audio clips, or recording non-overdub MIDI clips. No-op on
arrangement clips (confirmed by probe).

#### `move_warp_marker(beat_time, beat_time_distance)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` — beat time of the marker to move
  - `beat_time_distance: float` — relative distance to move it
- **Raises/Errors:** Error if no marker at `beat_time`, or if move would create an invalid segment.
- **Applicable to:** `audio`
- **Undo-tracked:** `Yes`
- **Side Effects:** Moves the warp marker at `beat_time` by `beat_time_distance`.
- **Async visibility:** `immediate`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Moves the warp marker located at the given beat time by the specified beat distance.

#### `note_number_to_name(midi_pitch)`

- **Returns:** `str`
- **Args:** `midi_pitch: int` — MIDI note number `0–127`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `12.1`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns a human-readable name for the given MIDI note number (e.g. `"C3"`, `"F#4"`). Takes
into account the clip's scale and tonal spelling settings, as well as the current tuning
system (if any).

#### `quantize(quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `quantization_grid: int` — `GridQuantization` enum value **1–8** (see below)
  - `amount: float` — quantization strength `0.0–1.0`
- **Raises/Errors:** `InternalError: Invalid quantization.` for values outside 1–8
- **Applicable to:** `midi`
- **Undo-tracked:** `yes`
- **Side Effects:** Quantizes all notes to the grid, taking the song's swing amount into account.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `probed`

**Description:**
Quantizes all notes to the given grid using the song's current swing setting.

Uses the same `GridQuantization` enum as `Clip.View.grid_quantization`, but only values **1–8** are valid. Value 0 (No
grid / off) and value 9 (1/32) both raise `Invalid quantization`.

| Value | Grid   |
| ----- | ------ |
| 1     | 8 Bars |
| 2     | 4 Bars |
| 3     | 2 Bars |
| 4     | 1 Bar  |
| 5     | 1/2    |
| 6     | 1/4    |
| 7     | 1/8    |
| 8     | 1/16   |

#### `quantize_pitch(pitch, quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `pitch: int` — MIDI pitch to quantize (0–127)
  - `quantization_grid: int` — `GridQuantization` enum value **1–8**
  - `amount: float` — quantization strength `0.0–1.0`
- **Raises/Errors:** `InternalError: Invalid quantization.` for grid values outside 1–8
- **Applicable to:** `midi`
- **Undo-tracked:** `yes`
- **Side Effects:** Quantizes only notes of the specified pitch.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `probed`

**Description:**
Same as `quantize` but restricted to notes of a single pitch. Uses the same `GridQuantization` enum values 1–8 (see
`quantize` above).

#### `remove_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `None`
- **Args:**
  - `from_time: float`
  - `from_pitch: int`
  - `time_span: float`
  - `pitch_span: int`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Deletes notes in the given region.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
**Deprecated.** Deletes all notes starting in the given pitch/time range. Superseded by
`remove_notes_extended()` (same functionality, different parameter order) and
`remove_notes_by_id()` (ID-based targeting).

#### `remove_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:** `note_ids: list[int]`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Deletes notes matching the given IDs.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Deletes all notes associated with the provided note IDs.

#### `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)`

- **Returns:** `None`
- **Args:**
  - `from_pitch: int`
  - `pitch_span: int`
  - `from_time: float` — in beats
  - `time_span: float` — in beats
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Deletes all notes whose start times fall in the given region.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Replaces the deprecated `remove_notes`.

#### `remove_warp_marker(beat_time)`

- **Returns:** `None`
- **Args:** `beat_time: float` — beat time of the marker to remove
- **Raises/Errors:** Error if no marker at `beat_time`.
- **Applicable to:** `audio`
- **Undo-tracked:** `Yes`
- **Side Effects:** Removes the warp marker at the given beat time.
- **Async visibility:** `immediate`
- **Available Since:** `11.0`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Removes the warp marker located at `beat_time`.

#### `replace_selected_notes(notes_tuple)`

- **Returns:** `None`
- **Args:** `notes_tuple: tuple` — tuple of tuples in the format returned by `get_selected_notes`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Replaces the currently selected notes with the provided notes.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
**Deprecated.** Replaces selected notes with the provided tuple data. Superseded by
`apply_note_modifications()` for modifying existing notes (preserves per-note expression
data) or `remove_notes_extended()` + `add_new_notes()` for replacement.

#### `sample_to_beat_time(sample_time)`

- **Returns:** `float`
- **Args:** `sample_time: float` — sample time in **samples** (not seconds)
- **Raises/Errors:** Error if clip is not warped.
- **Applicable to:** `audio`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Converts a sample time (in **samples**, not seconds) to the corresponding beat time for
warped audio clips. Raises an error if the clip is not warped. Inverse of
`beat_to_sample_time`.

#### `scrub(beat_time)`

- **Returns:** `None`
- **Args:** `beat_time: float` — absolute clip beat time to scrub to
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session`
- **Undo-tracked:** `no`
- **Side Effects:** Starts a scrub at the specified position, respecting Global Quantization.
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Auditions a looping snippet at an absolute beat position within the clip. The snippet size
is determined by the global `clip_trigger_quantization` setting. While playing, the clip
transitions from `is_playing=True` to `is_playing=False, is_triggered=True`. The reported
`playing_position` continues advancing linearly rather than jumping to the target — the
audible output scrubs to the target position. While stopped, starts playback
(`is_playing=True`). Repeated `scrub()` calls change the target position. Continues until
`stop_scrub()` is called. No-op on arrangement clips (confirmed by probe).

#### `seconds_to_sample_time(seconds)`

- **Returns:** `float`
- **Args:** `seconds: float`
- **Raises/Errors:** Error if clip is warped.
- **Applicable to:** `audio`
- **Undo-tracked:** `no`
- **Side Effects:** None
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Converts seconds to sample time for **unwarped** audio clips. Note: this is the opposite
requirement from `beat_to_sample_time`/`sample_to_beat_time` which require warped clips.
Raises an error if the clip is warped.

#### `select_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** Selects all notes in the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Selects all notes in the clip. Use before `replace_selected_notes` when you want to process
all notes regardless of current selection state.

#### `select_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:** `note_ids: list[int]`
- **Raises/Errors:** `Unknown` (does not warn on nonexistent IDs per Max docs)
- **Applicable to:** `midi`
- **Undo-tracked:** `no`
- **Side Effects:** Selects the specified notes.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0.6`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Selects notes matching the given IDs. Does not print a warning or error if any IDs do not
exist in the clip.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:** `state: bool`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** Simulates holding (`True`) or releasing (`False`) the clip start button.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max`
- **Probe Status:** `unprobed`

**Description:**
Simulates pressing and holding the clip launch button until `state=False` or the clip is
otherwise stopped.

#### `set_notes(notes_tuple)`

- **Returns:** `None`
- **Args:** `notes_tuple: tuple` — tuple of tuples in the same format as returned by `get_notes`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `midi`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Adds notes to the clip.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
**Deprecated.** Adds notes to the clip from tuple data. Superseded by `add_new_notes()`
which accepts note specification dicts and returns the assigned note IDs.

#### `stop()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session`
- **Undo-tracked:** `no`
- **Side Effects:** Stops this clip if it is playing or recording.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Stops the clip only if it is currently playing or recording. Has no effect if the clip is
triggered (blinking) or if a different clip on the same track is playing. No-op on
arrangement clips (confirmed by probe).

#### `stop_scrub()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Applicable to:** `session`
- **Undo-tracked:** `no`
- **Side Effects:** Stops an active scrub.
- **Async visibility:** `immediate`
- **Available Since:** `<11`
- **Sources:** `max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Ends a scrub initiated with `scrub()`. Probing shows the clip remains in `is_triggered=True`
state after calling — the exact transition back to normal playback is unclear. No-op on
arrangement clips (confirmed by probe).

---

## Clip.View

Provides access to view aspects of a clip: grid display settings and envelope visibility
controls in the Clip Detail View.

### Sources

- **Primary:** `Live/classes/Clip.py` (nested `View` class)
- **Secondary:** `MaxForLive/clip_view.md`
- **Probes:** None

### Probe Notes

None yet.

### Open Questions

None yet.

### Properties

| Property            | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                    |
| ------------------- | ----------- | ----------- | ---------- | --------------- | ---------------------------------------------------------- |
| `grid_is_triplet`   | `bool`      | `bool`      | `no`       | `<11`           | Whether the clip is displayed with a triplet grid.         |
| `grid_quantization` | `int`       | `int`       | `no`       | `<11`           | Grid quantization resolution. See `GridQuantization` enum. |

#### `grid_is_triplet`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Controls whether the clip's detail view displays a triplet grid. Works on any clip regardless of whether it is the
detail clip — read and write both succeed on non-detail clips (probed: Live 12.3.5).

#### `grid_quantization`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Grid quantization resolution for the clip's detail view. Uses the `Clip.GridQuantization`
enum (not `Song.Quantization` — this is a separate enum). Values confirmed by probe
(Live 12.3.5):

| Value | Grid Size     |
| ----- | ------------- |
| 0     | No grid (off) |
| 1     | 8 Bars        |
| 2     | 4 Bars        |
| 3     | 2 Bars        |
| 4     | 1 Bar         |
| 5     | 1/2           |
| 6     | 1/4           |
| 7     | 1/8           |
| 8     | 1/16          |
| 9     | 1/32          |

Triplet variants are controlled separately by `grid_is_triplet`. `Clip.quantize()` and
`Clip.quantize_pitch()` use the same enum but only accept values **1–8** (0 and 9 raise
`Invalid quantization`).

Works on any clip regardless of whether it is the detail clip — read and write both succeed on non-detail clips
(probed: Live 12.3.5). The value is an int enum, not a float; passing a float raises a type mismatch error.

### Methods

| Signature                              | Returns | Available Since | Summary                                                       |
| -------------------------------------- | ------- | --------------- | ------------------------------------------------------------- |
| `hide_envelope()`                      | `None`  | `<11`           | Hide the Envelopes box in Clip Detail View.                   |
| `select_envelope_parameter(parameter)` | `None`  | `<11`           | Select a parameter for envelope display in the Envelopes box. |
| `show_envelope()`                      | `None`  | `<11`           | Show the Envelopes box in Clip Detail View.                   |
| `show_loop()`                          | `None`  | `<11`           | Scroll the Detail View to show the current loop region.       |

#### `hide_envelope()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None observed
- **Undo-tracked:** `no`
- **Side Effects:** Switches the detail view tab away from Envelopes (to Sample for audio clips, Notes for MIDI clips).
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Switches the clip detail view away from the Envelopes tab. Only has an effect when the clip is the detail clip;
silently no-ops otherwise (probed: Live 12.3.5). Does not affect clip data.

#### `select_envelope_parameter(parameter)`

- **Returns:** `None`
- **Args:** `parameter: DeviceParameter`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `no`
- **Side Effects:** Selects the given parameter in the Envelopes box and shows its automation curve.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Selects the specified device parameter in the Envelopes box for display/editing. Only has an effect when the clip is
the detail clip; silently no-ops otherwise (probed: Live 12.3.5). The C++ signature shows the parameter type as
`TPyHandle<ATimeableValue>`, but `DeviceParameter` objects are accepted.

#### `show_envelope()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None observed
- **Undo-tracked:** `no`
- **Side Effects:** Switches the detail view to the Envelopes tab.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Switches the clip detail view to the Envelopes tab. Only has an effect when the clip is the detail clip; silently
no-ops otherwise (probed: Live 12.3.5). Does not affect clip data.

#### `show_loop()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None observed
- **Undo-tracked:** `no`
- **Side Effects:** Scrolls the Detail View to make the current loop region visible.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Scrolls the clip detail view to show the current loop region. Only has an effect when the clip is the detail clip;
silently no-ops otherwise (probed: Live 12.3.5). Does not affect clip data.

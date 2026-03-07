# LooperDevice

## LooperDevice

This class represents an instance of the Looper audio effect device in Live. A
LooperDevice is a subclass of Device -- it has all the children, properties, and methods
of Device plus additional members for controlling Looper's transport, buffer, and
recording behavior.

Looper is an audio effect that records incoming audio into a buffer and plays it back
in a loop. It supports overdubbing, speed/length manipulation, and exporting its
content to a clip slot.

### Sources

- **Primary:** `Live/classes/devices/LooperDevice.py` (stub dump)
- **Secondary:** `MaxForLive/looperdevice.md`
- **Probes:** 2026-02-25 (all properties and methods, listener support, export error)

### Probe Notes

- **Bridge type:** `"LooperDevice"`.
- **class_name:** `"Looper"`.
- **class_display_name:** `"Looper"`.
- **Device type:** Audio Effect.
- `loop_length` with no content: `0.0`. `tempo` with no content: `0.0`.
- `overdub_after_record` default: `True`. Settable, round-trips.
- `record_length_index` default: `10` (variable length). Range: 0–10.
- `record_length_list`: 11 entries: `[' 1 bar', ' 2 bars', ..., '16 bars', ' x bars (variable length)']`.
  Note leading spaces in entry strings.
- All 4 properties with listeners confirmed working (loop_length, overdub_after_record,
  record_length_index, tempo). `record_length_list` is NOT listenable.
- All 11 methods return `None` and succeed (even on empty buffer for most).
- `export_to_clip_slot`: raises `InternalError` if Looper has no audio content or audio
  engine is off. Takes a ClipSlot OID reference as argument.

### Open Questions

- ~~What does `loop_length` return when no content?~~ **Resolved:** `0.0`.
- ~~What does `tempo` return when no content?~~ **Resolved:** `0.0`.
- ~~What are valid values for `record_length_index`?~~ **Resolved:** 0–10 (11 entries).
- ~~Can `overdub_after_record` be set at any time?~~ **Resolved:** Yes, settable anytime.
- ~~What happens calling `export_to_clip_slot()` with empty looper?~~ **Resolved:** Raises
  `InternalError` with descriptive message.
- Does `undo()` toggle on successive calls? — Confirmed per Max docs: acts as undo/redo toggle.

### Children

None beyond those inherited from Device (`parameters`, `view`).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
LooperDevice adds:

| Property               | Get Returns    | Set Accepts | Listenable | Available Since | Summary                                             |
| ---------------------- | -------------- | ----------- | ---------- | --------------- | --------------------------------------------------- |
| `loop_length`          | `float`        | —           | `yes`      | `12.0`          | Length of Looper's recorded buffer. 0.0 when empty. |
| `overdub_after_record` | `bool`         | `bool`      | `yes`      | `12.0`          | Whether Looper enters overdub mode after recording. |
| `record_length_index`  | `int`          | `int`       | `yes`      | `12.0`          | Selected index in the Record Length chooser (0–10). |
| `record_length_list`   | `StringVector` | —           | `no`       | `12.0`          | Available Record Length chooser entries (11 items). |
| `tempo`                | `float`        | —           | `yes`      | `12.0`          | Tempo of Looper's recorded buffer. 0.0 when empty.  |

#### `loop_length`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (2026-02-25)

**Description:**
The length of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer length changes (e.g., after recording, or after calling
`double_length()` or `half_length()`).

#### `overdub_after_record`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (2026-02-25)

**Description:**
When `True`, Looper switches to overdub mode after finishing a fixed-length recording.
When `False`, Looper switches to playback without overdubbing after recording completes.
Default: `True`. Can be set at any time.

#### `record_length_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (2026-02-25)

**Description:**
The currently selected index in the Record Length chooser (0–10). Corresponds to the
entries in `record_length_list`. Default: `10` (variable length). Controls how many bars
Looper will record before automatically stopping or switching to overdub/playback.

#### `record_length_list`

- **Get Returns:** `StringVector` (list of strings)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (2026-02-25)

**Description:**
Read-only list of the available Record Length chooser entry strings. Static 11 entries:
`[' 1 bar', ' 2 bars', ' 3 bars', ' 4 bars', ' 5 bars', ' 6 bars', ' 7 bars', ' 8 bars', '12 bars', '16 bars', ' x bars (variable length)']`.
Note: entries have leading spaces for UI formatting alignment.

#### `tempo`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (2026-02-25)

**Description:**
The tempo of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer tempo changes (e.g., after calling `double_speed()` or
`half_speed()`).

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`), LooperDevice adds:

| Signature                                  | Returns | Available Since | Summary                                       |
| ------------------------------------------ | ------- | --------------- | --------------------------------------------- |
| `clear()`                                  | `None`  | `12.0`          | Erase all recorded content.                   |
| `double_length()`                          | `None`  | `12.0`          | Double the buffer length.                     |
| `double_speed()`                           | `None`  | `12.0`          | Double the playback speed.                    |
| `export_to_clip_slot(clip_slot: ClipSlot)` | `None`  | `12.1`          | Export buffer content to a session clip slot. |
| `half_length()`                            | `None`  | `12.0`          | Halve the buffer length.                      |
| `half_speed()`                             | `None`  | `12.0`          | Halve the playback speed.                     |
| `overdub()`                                | `None`  | `12.0`          | Switch to overdub mode.                       |
| `play()`                                   | `None`  | `12.0`          | Switch to playback mode.                      |
| `record()`                                 | `None`  | `12.0`          | Start recording incoming audio.               |
| `stop()`                                   | `None`  | `12.0`          | Stop playback.                                |
| `undo()`                                   | `None`  | `12.0`          | Undo or redo the last overdub layer.          |

All methods probed (2026-02-25). All return `None` and succeed on empty buffer (except
`export_to_clip_slot` which requires audio content and audio engine). `export_to_clip_slot`
takes a ClipSlot object reference (passed as OID dict via bridge).

# LooperDevice

> `Live.LooperDevice.LooperDevice`

This class represents an instance of the Looper audio effect device in Live. A
LooperDevice is a subclass of Device -- it has all the children, properties, and methods
of Device plus additional members for controlling Looper's transport, buffer, and
recording behavior.

Looper is an audio effect that records incoming audio into a buffer and plays it back
in a loop. It supports overdubbing, speed/length manipulation, and exporting its
content to a clip slot.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"LooperDevice"`.
    - **class_name:** `"Looper"`.
    - **class_display_name:** `"Looper"`.
    - **Device type:** Audio Effect.
    - `loop_length` with no content: `0.0`. `tempo` with no content: `0.0`.
    - `overdub_after_record` default: `True`. Settable, round-trips.
    - `record_length_index` default: `10` (variable length). Range: 0-10.
    - `record_length_list`: 11 entries: `[' 1 bar', ' 2 bars', ..., '16 bars',
      ' x bars (variable length)']`. Note leading spaces in entry strings.
    - All 4 properties with listeners confirmed working (loop_length, overdub_after_record,
      record_length_index, tempo). `record_length_list` is NOT listenable.
    - All 11 methods return `None` and succeed (even on empty buffer for most).
    - `export_to_clip_slot`: raises `InternalError` if Looper has no audio content or audio
      engine is off. Takes a ClipSlot OID reference as argument.

### Children

None beyond those inherited from Device (`parameters`, `view`).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
LooperDevice adds:

| Property               | Type           | Settable | Listenable | Summary                                             |
| ---------------------- | -------------- | -------- | ---------- | --------------------------------------------------- |
| `loop_length`          | `float`        | no       | `yes`      | Length of Looper's recorded buffer. 0.0 when empty. |
| `overdub_after_record` | `bool`         | yes      | `yes`      | Whether Looper enters overdub mode after recording. |
| `record_length_index`  | `int`          | yes      | `yes`      | Selected index in the Record Length chooser (0-10). |
| `record_length_list`   | `StringVector` | no       | `no`       | Available Record Length chooser entries (11 items).  |
| `tempo`                | `float`        | no       | `yes`      | Tempo of Looper's recorded buffer. 0.0 when empty.  |

#### `loop_length`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `12.0`

The length of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer length changes (e.g., after recording, or after calling
`double_length()` or `half_length()`).

#### `overdub_after_record`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `12.0`

When `True`, Looper switches to overdub mode after finishing a fixed-length recording.
When `False`, Looper switches to playback without overdubbing after recording completes.
Default: `True`. Can be set at any time.

#### `record_length_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `12.0`

The currently selected index in the Record Length chooser (0-10). Corresponds to the
entries in `record_length_list`. Default: `10` (variable length). Controls how many bars
Looper will record before automatically stopping or switching to overdub/playback.

#### `record_length_list`

- **Type:** `StringVector` (serializes as `list[str]`)
- **Listenable:** `no`
- **Since:** `12.0`

Read-only list of the available Record Length chooser entry strings. Static 11 entries:
`[' 1 bar', ' 2 bars', ' 3 bars', ' 4 bars', ' 5 bars', ' 6 bars', ' 7 bars', ' 8 bars',
'12 bars', '16 bars', ' x bars (variable length)']`.
Note: entries have leading spaces for UI formatting alignment.

#### `tempo`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `12.0`

The tempo of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer tempo changes (e.g., after calling `double_speed()` or
`half_speed()`).

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`), LooperDevice adds:

| Method                                     | Returns | Summary                                       |
| ------------------------------------------ | ------- | --------------------------------------------- |
| `clear()`                                  | `None`  | Erase all recorded content.                   |
| `double_length()`                          | `None`  | Double the buffer length.                     |
| `double_speed()`                           | `None`  | Double the playback speed.                    |
| `export_to_clip_slot(clip_slot: ClipSlot)` | `None`  | Export buffer content to a session clip slot.  |
| `half_length()`                            | `None`  | Halve the buffer length.                      |
| `half_speed()`                             | `None`  | Halve the playback speed.                     |
| `overdub()`                                | `None`  | Switch to overdub mode.                       |
| `play()`                                   | `None`  | Switch to playback mode.                      |
| `record()`                                 | `None`  | Start recording incoming audio.               |
| `stop()`                                   | `None`  | Stop playback.                                |
| `undo()`                                   | `None`  | Undo or redo the last overdub layer.          |

#### `clear()`

- **Returns:** `None`
- **Since:** `12.0`

Erase all recorded content from Looper's buffer.

#### `double_length()`

- **Returns:** `None`
- **Since:** `12.0`

Double the buffer length by duplicating the current content.

#### `double_speed()`

- **Returns:** `None`
- **Since:** `12.0`

Double the playback speed of the loop.

#### `export_to_clip_slot(clip_slot: ClipSlot)`

- **Returns:** `None`
- **Args:**
  - `clip_slot: ClipSlot` -- the session clip slot to export the buffer into
- **Raises:** `InternalError` if Looper has no audio content or audio engine is off.
- **Since:** `12.1`

Export the contents of Looper's buffer to the specified session clip slot.

#### `half_length()`

- **Returns:** `None`
- **Since:** `12.0`

Halve the buffer length by truncating.

#### `half_speed()`

- **Returns:** `None`
- **Since:** `12.0`

Halve the playback speed of the loop.

#### `overdub()`

- **Returns:** `None`
- **Since:** `12.0`

Switch Looper to overdub mode. Incoming audio is layered on top of the existing buffer content.

#### `play()`

- **Returns:** `None`
- **Since:** `12.0`

Switch Looper to playback mode.

#### `record()`

- **Returns:** `None`
- **Since:** `12.0`

Start recording incoming audio into the buffer.

#### `stop()`

- **Returns:** `None`
- **Since:** `12.0`

Stop playback.

#### `undo()`

- **Returns:** `None`
- **Since:** `12.0`

Undo or redo the last overdub layer. Acts as an undo/redo toggle on successive calls.

### Open Questions

- Does `undo()` toggle on successive calls? -- Confirmed per Max docs: acts as undo/redo toggle.

# SimplerDevice

> `Live.SimplerDevice.SimplerDevice`

This class represents an instance of Simpler in Live. A SimplerDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for sample playback, warping, slicing, and voice management.

Simpler has three playback modes: Classic, One-Shot, and Slicing. The available properties
and methods vary depending on the active mode.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"SimplerDevice"`.
    - **`class_name`:** `"OriginalSimpler"`. **`class_display_name`:** `"Simpler"`.
    - **`type`:** 1 (`INSTRUMENT`).
    - **Insert name:** `"Simpler"` (matches `class_display_name`).
    - **7 settable properties** round-trip confirmed: `note_pitch_bend_range` (default 48),
      `pad_slicing` (default False), `pitch_bend_range` (default 5), `playback_mode` (default 0,
      range 0–2), `retrigger` (default True), `slicing_playback_mode` (default 0, range 0–2),
      `voices` (default 6, valid: 1,2,3,4,6,8,12,16,24,32).
    - **6 read-only properties:** `can_warp_as` (False), `can_warp_double` (False), `can_warp_half`
      (False), `multi_sample_mode` (False), `playing_position` (0.0), `playing_position_enabled`
      (False). All return defaults when no sample is loaded.
    - **All 13 properties are listenable.**
    - **`sample` child:** Returns `None` when no sample is loaded (confirmed — does not throw).
    - **All 6 methods** raise `InternalError` when no sample is loaded. This is expected — they
      require an active sample.
    - **`playback_mode`:** 0=Classic, 1=One-Shot, 2=Slicing. Plain `int`, not an enum.
    - **`slicing_playback_mode`:** 0=Mono, 1=Poly, 2=Thru. Plain `int`, not an enum.
    - **`voices`:** Valid values are 1,2,3,4,6,8,12,16,24,32 (not arbitrary). Invalid values throw.
    - **View:** 8 read-only listenable `int` properties. All return `-1` when no sample is loaded.
      `selected_slice` throws `AttributeError` when no sample is loaded and Simpler is not in
      Slicing mode.

### Children

In addition to Device children (`parameters`, `view`), SimplerDevice adds:

| Child    | Returns  | Shape    | Listenable | Summary                                 |
| -------- | -------- | -------- | ---------- | --------------------------------------- |
| `sample` | `Sample` | `single` | `yes`      | The sample currently loaded in Simpler. |

#### `sample`

- **Type:** `Sample` or `None`
- **Listenable:** `yes`
- **Since:** `<11`

The sample currently loaded into Simpler. The listener fires when a new sample is loaded
or the sample is replaced. Returns `None` if no sample is loaded.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), SimplerDevice adds:

| Property                   | Type    | Settable | Listenable | Summary                                                     |
| -------------------------- | ------- | -------- | ---------- | ----------------------------------------------------------- |
| `can_warp_as`              | `bool`  | no       | `yes`      | Whether `warp_as` is currently available.                   |
| `can_warp_double`          | `bool`  | no       | `yes`      | Whether `warp_double` is currently available.               |
| `can_warp_half`            | `bool`  | no       | `yes`      | Whether `warp_half` is currently available.                 |
| `multi_sample_mode`        | `bool`  | no       | `yes`      | Whether Simpler is in multi-sample mode.                    |
| `note_pitch_bend_range`    | `int`   | yes      | `yes`      | The per-note pitch bend range in semitones. Default 48.     |
| `pad_slicing`              | `bool`  | yes      | `yes`      | Whether slices can be added by playing unassigned notes.    |
| `pitch_bend_range`         | `int`   | yes      | `yes`      | The global pitch bend range in semitones. Default 5.        |
| `playback_mode`            | `int`   | yes      | `yes`      | 0=Classic, 1=One-Shot, 2=Slicing. Default 0.               |
| `playing_position`         | `float` | no       | `yes`      | Normalized playback position between start and end markers. |
| `playing_position_enabled` | `bool`  | no       | `yes`      | Whether Simpler is currently playing back the sample.       |
| `retrigger`                | `bool`  | yes      | `yes`      | Whether retrigger mode is enabled. Default True.            |
| `slicing_playback_mode`    | `int`   | yes      | `yes`      | 0=Mono, 1=Poly, 2=Thru. Default 0.                         |
| `voices`                   | `int`   | yes      | `yes`      | Polyphony voice count. Valid: 1,2,3,4,6,8,12,16,24,32.     |

#### `can_warp_as`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_as` is currently available. Returns `False` when no sample is loaded.

#### `can_warp_double`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_double` is currently available. Returns `False` when no sample is loaded.

#### `can_warp_half`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_half` is currently available. Returns `False` when no sample is loaded.

#### `multi_sample_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether Simpler is in multi-sample mode. Returns `False` when no sample is loaded.

#### `note_pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The per-note pitch bend range in semitones. Default 48.

#### `pad_slicing`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether slices can be added by playing unassigned notes on the MIDI controller.

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The global pitch bend range in semitones. Default 5.

#### `playback_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

0=Classic, 1=One-Shot, 2=Slicing. Default 0. Plain `int`, not an enum.

#### `playing_position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Normalized playback position between start and end markers. Returns `0.0` when no sample is loaded.

#### `playing_position_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether Simpler is currently playing back the sample. Returns `False` when no sample is loaded.

#### `retrigger`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether retrigger mode is enabled. Default True.

#### `slicing_playback_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

0=Mono, 1=Poly, 2=Thru. Default 0. Plain `int`, not an enum.

#### `voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Polyphony voice count. Valid values are 1, 2, 3, 4, 6, 8, 12, 16, 24, 32 (not arbitrary). Invalid values throw.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
SimplerDevice adds:

| Method                      | Returns | Summary                                                      |
| --------------------------- | ------- | ------------------------------------------------------------ |
| `crop()`                    | `None`  | Crop the sample to the region between start and end markers. |
| `guess_playback_length()`   | `float` | Estimate the playback length in beats between the markers.   |
| `reverse()`                 | `None`  | Reverse the loaded sample.                                   |
| `warp_as(beat_time: float)` | `None`  | Warp the active region to fit the given beat length.         |
| `warp_double()`             | `None`  | Double the playback tempo of the active region.              |
| `warp_half()`               | `None`  | Halve the playback tempo of the active region.               |

All methods raise `InternalError` when no sample is loaded.

#### `crop()`

- **Returns:** `None`
- **Since:** `<11`

Crop the sample to the region between start and end markers.

#### `guess_playback_length()`

- **Returns:** `float`
- **Since:** `<11`

Estimate the playback length in beats between the markers.

#### `reverse()`

- **Returns:** `None`
- **Since:** `<11`

Reverse the loaded sample.

#### `warp_as(beat_time: float)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- the target beat length for the active region
- **Since:** `<11`

Warp the active region to fit the given beat length.

#### `warp_double()`

- **Returns:** `None`
- **Since:** `<11`

Double the playback tempo of the active region.

#### `warp_half()`

- **Returns:** `None`
- **Since:** `<11`

Halve the playback tempo of the active region.

---

## SimplerDevice.View

Represents the view aspects of a Simpler device. Extends Device.View with sample display
properties for visualizing the waveform, loop region, and slices.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property              | Type  | Settable | Listenable | Summary                                                      |
| --------------------- | ----- | -------- | ---------- | ------------------------------------------------------------ |
| `sample_end`          | `int` | no       | `yes`      | Modulated sample end position in samples. -1 if no sample.   |
| `sample_env_fade_in`  | `int` | no       | `yes`      | Envelope fade-in time in samples. -1 if no sample.           |
| `sample_env_fade_out` | `int` | no       | `yes`      | Envelope fade-out time in samples. -1 if no sample.          |
| `sample_loop_end`     | `int` | no       | `yes`      | Modulated loop end position in samples. -1 if no sample.     |
| `sample_loop_fade`    | `int` | no       | `yes`      | Modulated loop crossfade length in samples. -1 if no sample. |
| `sample_loop_start`   | `int` | no       | `yes`      | Modulated loop start position in samples. -1 if no sample.   |
| `sample_start`        | `int` | no       | `yes`      | Modulated sample start position in samples. -1 if no sample. |
| `selected_slice`      | `int` | no       | `yes`      | Currently selected slice time. Errors if no sample.          |

#### `sample_end`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated sample end position in samples. Returns `-1` if no sample is loaded.

#### `sample_env_fade_in`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Envelope fade-in time in samples. Returns `-1` if no sample is loaded.

#### `sample_env_fade_out`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Envelope fade-out time in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_end`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop end position in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_fade`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop crossfade length in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_start`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop start position in samples. Returns `-1` if no sample is loaded.

#### `sample_start`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated sample start position in samples. Returns `-1` if no sample is loaded.

#### `selected_slice`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Currently selected slice time.

- **Quirks:**
    - Throws `AttributeError` when no sample is loaded and Simpler is not in Slicing mode.

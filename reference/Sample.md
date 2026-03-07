# Sample

## Sample

This class represents a sample file loaded into a Simpler instrument. It exposes warp
settings, slice controls, marker positions, and various warp-mode-specific parameters
(Beats, Tones, Texture, Complex Pro). The sample object is accessible from the Simpler
device via its `sample` property.

### Sources

- **Primary:** `Live/classes/Sample.py` (stub dump)
- **Secondary:** `MaxForLive/sample.md`
- **Probes:** None

### Probe Notes

None yet.

### Open Questions

- What type does `warp_markers` actually return in Python? The Max docs say "dict/bang" and
  describe it as a dict of warp markers. The stub just declares a property with no type hint.
  Need to probe the actual structure.
- Is `slicing_sensitivity` clamped automatically when set outside 0.0–1.0, or does it raise
  an error?
- Can `end_marker` be set to a value greater than `length`? What happens if it's set below
  `start_marker`?
- Does `beat_to_sample_time` / `sample_to_beat_time` raise immediately when warping is off,
  or only when the method is called?
- What are the valid range boundaries for `gain`? The Max docs don't specify min/max values.
- Does `move_slice` return the actual new position (which may differ from `new_time` due to
  snapping), or the input value?
- Can `insert_slice` / `remove_slice` be called when `slicing_style` is not Manual (3)?
- The stub lists `sample_rate` with no listener, but the Max docs say "read-only." Is it
  truly never observable, or was the listener simply omitted?

### Properties

| Property                       | Get Returns        | Set Accepts | Listenable | Available Since | Summary                                                 |
| ------------------------------ | ------------------ | ----------- | ---------- | --------------- | ------------------------------------------------------- |
| `beats_granulation_resolution` | `int`              | `int`       | `yes`      | `<11`           | Granulation resolution in Beats warp mode.              |
| `beats_transient_envelope`     | `float`            | `float`     | `yes`      | `<11`           | Transient envelope decay in Beats warp mode.            |
| `beats_transient_loop_mode`    | `int`              | `int`       | `yes`      | `<11`           | Transient loop mode in Beats warp mode.                 |
| `complex_pro_envelope`         | `float`            | `float`     | `yes`      | `<11`           | Envelope parameter in Complex Pro warp mode.            |
| `complex_pro_formants`         | `float`            | `float`     | `yes`      | `<11`           | Formants parameter in Complex Pro warp mode.            |
| `end_marker`                   | `int`              | `int`       | `yes`      | `<11`           | Position of the sample's end marker in sample frames.   |
| `file_path`                    | `str`              | —           | `yes`      | `<11`           | Absolute file path of the loaded sample.                |
| `gain`                         | `float`            | `float`     | `yes`      | `<11`           | Sample gain level.                                      |
| `length`                       | `int`              | —           | `no`       | `<11`           | Length of the sample file in sample frames.             |
| `sample_rate`                  | `int`              | —           | `no`       | `11.0`          | Audio sample rate of the loaded sample in Hz.           |
| `slices`                       | `list[int]`        | —           | `yes`      | `11.0`          | Positions of all playable slices in sample frames.      |
| `slicing_beat_division`        | `int`              | `int`       | `yes`      | `<11`           | Slice step size in Beat slicing mode.                   |
| `slicing_region_count`         | `int`              | `int`       | `yes`      | `<11`           | Number of slice regions in Region slicing mode.         |
| `slicing_sensitivity`          | `float`            | `float`     | `yes`      | `<11`           | Slicing sensitivity (0.0–1.0). Higher = more slices.    |
| `slicing_style`                | `int`              | `int`       | `yes`      | `<11`           | Slicing mode selector.                                  |
| `start_marker`                 | `int`              | `int`       | `yes`      | `<11`           | Position of the sample's start marker in sample frames. |
| `texture_flux`                 | `float`            | `float`     | `yes`      | `<11`           | Flux parameter in Texture warp mode.                    |
| `texture_grain_size`           | `float`            | `float`     | `yes`      | `<11`           | Grain size parameter in Texture warp mode.              |
| `tones_grain_size`             | `float`            | `float`     | `yes`      | `<11`           | Grain size parameter in Tones warp mode.                |
| `warp_markers`                 | `list[WarpMarker]` | —           | `yes`      | `11.0`          | Warp markers list; same structure as Clip.warp_markers. |
| `warp_mode`                    | `int`              | `int`       | `yes`      | `<11`           | Active warp mode.                                       |
| `warping`                      | `bool`             | `bool`      | `yes`      | `<11`           | Whether warping is enabled for this sample.             |

#### `beats_granulation_resolution`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls which beat divisions are preserved when the sample is stretched in Beats warp mode.
Values: `0` = 1 Bar, `1` = 1/2, `2` = 1/4, `3` = 1/8, `4` = 1/16, `5` = 1/32,
`6` = Transients.

#### `beats_transient_envelope`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls the duration of the volume fade applied to each audio segment in Beats warp mode.
`0` = fastest decay, `100` = no fade.

#### `beats_transient_loop_mode`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls the loop mode applied to each audio segment in Beats warp mode.
Values: `0` = Off, `1` = Loop Forward, `2` = Loop Back-and-Forth.

#### `complex_pro_envelope`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The Envelope parameter in Complex Pro warp mode.

#### `complex_pro_formants`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The Formants parameter in Complex Pro warp mode. Controls how much the formant structure
of the sound is preserved during pitch-shifting.

#### `end_marker`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The position of the sample's end marker, in sample frames. Playback stops at this position.

#### `file_path`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The absolute file system path of the loaded sample file. Read-only. The listener fires
when a different sample is loaded.

#### `gain`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The gain level applied to the sample. Use `gain_display_string()` to get the formatted
display value (e.g. `"0.0 dB"`).

#### `length`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The total length of the sample file in sample frames. Divide by `sample_rate` to get
the duration in seconds.

#### `sample_rate`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The audio sample rate of the loaded sample file, in Hz (e.g. `44100`, `48000`).

#### `slices`

- **Get Returns:** `list[int]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The positions of all playable slices in the sample, in sample frames. Divide each value by
`sample_rate` to get the slice time in seconds. The listener fires when slices are added,
removed, or moved.

#### `slicing_beat_division`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The beat division used for slicing in Beat slicing mode (`slicing_style` = `1`).
Values: `0` = 1/16, `1` = 1/16T, `2` = 1/8, `3` = 1/8T, `4` = 1/4, `5` = 1/4T,
`6` = 1/2, `7` = 1/2T, `8` = 1 Bar, `9` = 2 Bars, `10` = 4 Bars.

#### `slicing_region_count`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The number of equally spaced slice regions in Region slicing mode
(`slicing_style` = `2`).

#### `slicing_sensitivity`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls how aggressively transients are detected for slicing. Range is 0.0 to 1.0. Higher
values produce more slices. Applies when `slicing_style` is Transient (`0`).

#### `slicing_style`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The active slicing mode.
Values: `0` = Transient, `1` = Beat, `2` = Region, `3` = Manual.

#### `start_marker`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The position of the sample's start marker, in sample frames. Playback begins at this
position.

#### `texture_flux`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The Flux parameter in Texture warp mode. Controls the amount of random variation in the
grain playback.

#### `texture_grain_size`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The Grain Size parameter in Texture warp mode. Controls the size of the granular
synthesis grains.

#### `tones_grain_size`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The Grain Size parameter in Tones warp mode.

#### `warp_markers`

- **Get Returns:** `list[WarpMarker]` (WarpMarkerVector)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The sample's warp markers. Returns a list of `WarpMarker` objects, each with `beat_time: float` and
`sample_time: float` — identical structure to `Clip.warp_markers`. The listener fires (as a bang,
with no value) when warp markers change. The last warp marker in the returned data is a hidden
phantom "shadow" marker (1/32 beat after the last visible marker) used internally to derive
the final-segment BPM; it is not shown in the Live UI.

#### `warp_mode`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The active warp mode for the sample. Values: `0` = Beats, `1` = Tones, `2` = Texture,
`3` = Re-Pitch, `4` = Complex, `6` = Complex Pro. Note: there is no mode `5`.

#### `warping`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Whether warping is enabled for this sample. When `True`, the sample is time-stretched
to match the project tempo using the selected `warp_mode`.

### Methods

| Signature                                  | Returns | Available Since | Summary                                              |
| ------------------------------------------ | ------- | --------------- | ---------------------------------------------------- |
| `beat_to_sample_time(beat_time: float)`    | `float` | `<11`           | Convert beat time to sample time. Requires warping.  |
| `clear_slices()`                           | `None`  | `<11`           | Remove all slices created in Manual slicing mode.    |
| `gain_display_string()`                    | `str`   | `<11`           | Get the gain value as a formatted display string.    |
| `insert_slice(slice_time: int)`            | `None`  | `<11`           | Add a slice point at the given sample time.          |
| `move_slice(old_time: int, new_time: int)` | `int`   | `<11`           | Move a slice point from one position to another.     |
| `remove_slice(slice_time: int)`            | `None`  | `<11`           | Remove the slice point at the given sample time.     |
| `reset_slices()`                           | `None`  | `<11`           | Reset all edited slices to their original positions. |
| `sample_to_beat_time(sample_time: float)`  | `float` | `<11`           | Convert sample time to beat time. Requires warping.  |

#### `beat_to_sample_time(beat_time: float)`

- **Returns:** `float`
- **Args:**
  - `beat_time: float` — the beat time to convert
- **Raises/Errors:** Raises an error if the sample is not warped (`warping` is `False`).
- **Undo-tracked:** `N/A`
- **Side Effects:** None.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Converts a beat time value to the corresponding sample time value. Only works when warping
is enabled. Raises an error if `warping` is `False`.

#### `clear_slices()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes all manually created slices.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Clears all slices that were created in Manual slicing mode (`slicing_style` = `3`).
The `slices` listener fires after the slices are cleared.

#### `gain_display_string()`

- **Returns:** `str`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the current gain value as a human-readable display string (e.g. `"0.0 dB"`).

#### `insert_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int` — the sample time position at which to insert a slice
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Adds a new slice point. Does nothing if a slice already exists at that position.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Inserts a new slice point at the specified sample time position. If a slice already exists
at that time, no change is made.

#### `move_slice(old_time: int, new_time: int)`

- **Returns:** `int`
- **Args:**
  - `old_time: int` — current position of the slice to move
  - `new_time: int` — desired new position for the slice
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Moves the slice from one position to another.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Moves an existing slice point from `old_time` to `new_time`. Returns an `int` — likely the
actual new position of the slice (which may differ from `new_time` if snapping applies).

#### `remove_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int` — the sample time position of the slice to remove
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes the slice point at the given position.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Removes the slice point at the specified sample time position. If no slice exists at that
time, no change is made.

#### `reset_slices()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Restores all slices to their original positions.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Resets all edited slices back to their original auto-detected positions.

#### `sample_to_beat_time(sample_time: float)`

- **Returns:** `float`
- **Args:**
  - `sample_time: float` — the sample time to convert
- **Raises/Errors:** Raises an error if the sample is not warped (`warping` is `False`).
- **Undo-tracked:** `N/A`
- **Side Effects:** None.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Converts a sample time value to the corresponding beat time value. Only works when warping
is enabled. Raises an error if `warping` is `False`.

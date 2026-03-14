# Sample (Module)

## Sample (Class)

> `Live.Sample.Sample`

This class represents a sample file loaded into a Simpler instance.

**Live Object:** `yes`

**Access via:**

- `SimplerDevice.sample`

### Properties

| Property                                                        | Type                          | Supports             |
| --------------------------------------------------------------- | ----------------------------- | -------------------- |
| [`beats_granulation_resolution`](#beats_granulation_resolution) | `int`                         | `get`/`set`/`listen` |
| [`beats_transient_envelope`](#beats_transient_envelope)         | `float`                       | `get`/`set`/`listen` |
| [`beats_transient_loop_mode`](#beats_transient_loop_mode)       | `int`                         | `get`/`set`/`listen` |
| [`canonical_parent`](#canonical_parent)                         | `SimplerDevice`               | `get`                |
| [`complex_pro_envelope`](#complex_pro_envelope)                 | `float`                       | `get`/`set`/`listen` |
| [`complex_pro_formants`](#complex_pro_formants)                 | `float`                       | `get`/`set`/`listen` |
| [`end_marker`](#end_marker)                                     | `int`                         | `get`/`set`/`listen` |
| [`file_path`](#file_path)                                       | `str`                         | `get`/`listen`       |
| [`gain`](#gain)                                                 | `float`                       | `get`/`set`/`listen` |
| [`length`](#length)                                             | `int`                         | `get`                |
| [`sample_rate`](#sample_rate)                                   | `float`                       | `get`                |
| [`slices`](#slices)                                             | `tuple`                       | `get`/`listen`       |
| [`slicing_beat_division`](#slicing_beat_division)               | `int`                         | `get`/`set`/`listen` |
| [`slicing_region_count`](#slicing_region_count)                 | `int`                         | `get`/`set`/`listen` |
| [`slicing_sensitivity`](#slicing_sensitivity)                   | `float`                       | `get`/`set`/`listen` |
| [`slicing_style`](#slicing_style)                               | `int`                         | `get`/`set`/`listen` |
| [`start_marker`](#start_marker)                                 | `int`                         | `get`/`set`/`listen` |
| [`texture_flux`](#texture_flux)                                 | `float`                       | `get`/`set`/`listen` |
| [`texture_grain_size`](#texture_grain_size)                     | `float`                       | `get`/`set`/`listen` |
| [`tones_grain_size`](#tones_grain_size)                         | `float`                       | `get`/`set`/`listen` |
| [`warp_markers`](#warp_markers)                                 | `tuple[WarpMarker, Ellipsis]` | `get`/`listen`       |
| [`warp_mode`](#warp_mode)                                       | `int`                         | `get`/`set`/`listen` |
| [`warping`](#warping)                                           | `bool`                        | `get`/`set`/`listen` |

#### `beats_granulation_resolution`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Granulation Resolution parameter in Beats Warp Mode.

#### `beats_transient_envelope`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Transient Envelope parameter in Beats Warp Mode.

#### `beats_transient_loop_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Transient Loop Mode parameter in Beats Warp Mode.

#### `canonical_parent`

- **Type:** `SimplerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Access to the sample's canonical parent.

#### `complex_pro_envelope`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Envelope parameter in Complex Pro Mode.

#### `complex_pro_formants`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Formants parameter in Complex Pro Warp Mode.

#### `end_marker`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the position of the sample's end marker.

#### `file_path`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Get the path of the sample file.

#### `gain`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample gain.

#### `length`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the length of the sample file in sample frames.

#### `sample_rate`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Access to the audio sample rate of the sample.

#### `slices`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the list of slice points in sample time in the sample.

#### `slicing_beat_division`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing step size.

#### `slicing_region_count`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing split count.

#### `slicing_sensitivity`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0. The higher the sensitivity, the more slices will be available.

#### `slicing_style`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing style.

#### `start_marker`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the position of the sample's start marker.

#### `texture_flux`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Flux parameter in Texture Warp Mode.

#### `texture_grain_size`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Grain Size parameter in Texture Warp Mode.

#### `tones_grain_size`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Grain Size parameter in Tones Warp Mode.

#### `warp_markers`

- **Type:** `tuple[WarpMarker, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Get the warp markers for this sample.

#### `warp_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample's warp mode.

#### `warping`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample's warping property.

### Methods

| Method                                                                             | Returns |
| ---------------------------------------------------------------------------------- | ------- |
| [`beat_to_sample_time(beat_time: float)`](#beat_to_sample_timebeat_time-float)     | `float` |
| [`clear_slices()`](#clear_slices)                                                  | `None`  |
| [`gain_display_string()`](#gain_display_string)                                    | `str`   |
| [`insert_slice(slice_time: int)`](#insert_sliceslice_time-int)                     | `None`  |
| [`move_slice(old_time: int, new_time: int)`](#move_sliceold_time-int-new_time-int) | `int`   |
| [`remove_slice(slice_time: int)`](#remove_sliceslice_time-int)                     | `None`  |
| [`reset_slices()`](#reset_slices)                                                  | `None`  |
| [`sample_to_beat_time(sample_time: float)`](#sample_to_beat_timesample_time-float) | `float` |

#### `beat_to_sample_time(beat_time: float)`

- **Returns:** `float`
- **Args:**
  - `beat_time: float`

Converts the given beat time to sample time. Raises an error if the sample is not warped.

#### `clear_slices()`

- **Returns:** `None`

Clears all slices created in Simpler's manual mode.

#### `gain_display_string()`

- **Returns:** `str`

Get the gain's display value as a string.

#### `insert_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int`

Add a slice point at the provided time if there is none.

#### `move_slice(old_time: int, new_time: int)`

- **Returns:** `int`
- **Args:**
  - `old_time: int`
  - `new_time: int`

Move the slice point at the provided time.

#### `remove_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int`

Remove the slice point at the provided time if there is one.

#### `reset_slices()`

- **Returns:** `None`

Resets all edited slices to their original positions.

#### `sample_to_beat_time(sample_time: float)`

- **Returns:** `float`
- **Args:**
  - `sample_time: float`

Converts the given sample time to beat time. Raises an error if the sample is not warped.

## Enums

### `SlicingBeatDivision`

| Value | Name                 |
| ----- | -------------------- |
| `0`   | `sixteenth`          |
| `1`   | `sixteenth_triplett` |
| `2`   | `eighth`             |
| `3`   | `eighth_triplett`    |
| `4`   | `quarter`            |
| `5`   | `quarter_triplett`   |
| `6`   | `half`               |
| `7`   | `half_triplett`      |
| `8`   | `one_bar`            |
| `9`   | `two_bars`           |
| `10`  | `four_bars`          |

### `SlicingStyle`

| Value | Name        |
| ----- | ----------- |
| `0`   | `transient` |
| `1`   | `beat`      |
| `2`   | `region`    |
| `3`   | `manual`    |

### `TransientLoopMode`

| Value | Name        |
| ----- | ----------- |
| `0`   | `off`       |
| `1`   | `forward`   |
| `2`   | `alternate` |

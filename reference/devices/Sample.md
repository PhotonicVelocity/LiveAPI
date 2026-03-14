# Sample

> `Live.Sample.Sample`

This class represents a sample file loaded into a Simpler instance.

**Live Object:** `yes`

## Properties

| Property                       | Type                          | Settable | Listenable | Description                                                                      |
| ------------------------------ | ----------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `beats_granulation_resolution` | `int`                         | `yes`    | `yes`      | Access to the Granulation Resolution parameter in Beats Warp Mode.               |
| `beats_transient_envelope`     | `float`                       | `yes`    | `yes`      | Access to the Transient Envelope parameter in Beats Warp Mode.                   |
| `beats_transient_loop_mode`    | `int`                         | `yes`    | `yes`      | Access to the Transient Loop Mode parameter in Beats Warp Mode.                  |
| `canonical_parent`             | `SimplerDevice`               | `no`     | `no`       | Access to the sample's canonical parent.                                         |
| `complex_pro_envelope`         | `float`                       | `yes`    | `yes`      | Access to the Envelope parameter in Complex Pro Mode.                            |
| `complex_pro_formants`         | `float`                       | `yes`    | `yes`      | Access to the Formants parameter in Complex Pro Warp Mode.                       |
| `end_marker`                   | `int`                         | `yes`    | `yes`      | Access to the position of the sample's end marker.                               |
| `file_path`                    | `str`                         | `no`     | `yes`      | Get the path of the sample file.                                                 |
| `gain`                         | `float`                       | `yes`    | `yes`      | Access to the sample gain.                                                       |
| `length`                       | `int`                         | `no`     | `no`       | Get the length of the sample file in sample frames.                              |
| `sample_rate`                  | `float`                       | `no`     | `no`       | Access to the audio sample rate of the sample.                                   |
| `slices`                       | `tuple`                       | `no`     | `yes`      | Access to the list of slice points in sample time in the sample.                 |
| `slicing_beat_division`        | `int`                         | `yes`    | `yes`      | Access to sample's slicing step size.                                            |
| `slicing_region_count`         | `int`                         | `yes`    | `yes`      | Access to sample's slicing split count.                                          |
| `slicing_sensitivity`          | `float`                       | `yes`    | `yes`      | Access to sample's slicing sensitivity whose sensitivity is in between 0.0 an... |
| `slicing_style`                | `int`                         | `yes`    | `yes`      | Access to sample's slicing style.                                                |
| `start_marker`                 | `int`                         | `yes`    | `yes`      | Access to the position of the sample's start marker.                             |
| `texture_flux`                 | `float`                       | `yes`    | `yes`      | Access to the Flux parameter in Texture Warp Mode.                               |
| `texture_grain_size`           | `float`                       | `yes`    | `yes`      | Access to the Grain Size parameter in Texture Warp Mode.                         |
| `tones_grain_size`             | `float`                       | `yes`    | `yes`      | Access to the Grain Size parameter in Tones Warp Mode.                           |
| `warp_markers`                 | `tuple[WarpMarker, Ellipsis]` | `no`     | `yes`      | Get the warp markers for this sample.                                            |
| `warp_mode`                    | `int`                         | `yes`    | `yes`      | Access to the sample's warp mode.                                                |
| `warping`                      | `bool`                        | `yes`    | `yes`      | Access to the sample's warping property.                                         |

### `beats_granulation_resolution`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Granulation Resolution parameter in Beats Warp Mode.

### `beats_transient_envelope`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Transient Envelope parameter in Beats Warp Mode.

### `beats_transient_loop_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Transient Loop Mode parameter in Beats Warp Mode.

### `canonical_parent`

- **Type:** `SimplerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Access to the sample's canonical parent.

### `complex_pro_envelope`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Envelope parameter in Complex Pro Mode.

### `complex_pro_formants`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Formants parameter in Complex Pro Warp Mode.

### `end_marker`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the position of the sample's end marker.

### `file_path`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Get the path of the sample file.

### `gain`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample gain.

### `length`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the length of the sample file in sample frames.

### `sample_rate`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Access to the audio sample rate of the sample.

### `slices`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the list of slice points in sample time in the sample.

### `slicing_beat_division`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing step size.

### `slicing_region_count`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing split count.

### `slicing_sensitivity`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0. The higher the sensitivity, the more slices will be available.

### `slicing_style`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to sample's slicing style.

### `start_marker`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the position of the sample's start marker.

### `texture_flux`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Flux parameter in Texture Warp Mode.

### `texture_grain_size`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Grain Size parameter in Texture Warp Mode.

### `tones_grain_size`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Grain Size parameter in Tones Warp Mode.

### `warp_markers`

- **Type:** `tuple[WarpMarker, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Get the warp markers for this sample.

### `warp_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample's warp mode.

### `warping`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the sample's warping property.

## Methods

| Method                                     | Returns | Description                                                  |
| ------------------------------------------ | ------- | ------------------------------------------------------------ |
| `beat_to_sample_time(beat_time: float)`    | `float` | Converts the given beat time to sample time.                 |
| `clear_slices()`                           | `None`  | Clears all slices created in Simpler's manual mode.          |
| `gain_display_string()`                    | `str`   | Get the gain's display value as a string.                    |
| `insert_slice(slice_time: int)`            | `None`  | Add a slice point at the provided time if there is none.     |
| `move_slice(old_time: int, new_time: int)` | `int`   | Move the slice point at the provided time.                   |
| `remove_slice(slice_time: int)`            | `None`  | Remove the slice point at the provided time if there is one. |
| `reset_slices()`                           | `None`  | Resets all edited slices to their original positions.        |
| `sample_to_beat_time(sample_time: float)`  | `float` | Converts the given sample time to beat time.                 |

### `beat_to_sample_time(beat_time: float)`

- **Returns:** `float`
- **Args:**
  - `beat_time: float`

Converts the given beat time to sample time. Raises an error if the sample is not warped.

### `clear_slices()`

- **Returns:** `None`

Clears all slices created in Simpler's manual mode.

### `gain_display_string()`

- **Returns:** `str`

Get the gain's display value as a string.

### `insert_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int`

Add a slice point at the provided time if there is none.

### `move_slice(old_time: int, new_time: int)`

- **Returns:** `int`
- **Args:**
  - `old_time: int`
  - `new_time: int`

Move the slice point at the provided time.

### `remove_slice(slice_time: int)`

- **Returns:** `None`
- **Args:**
  - `slice_time: int`

Remove the slice point at the provided time if there is one.

### `reset_slices()`

- **Returns:** `None`

Resets all edited slices to their original positions.

### `sample_to_beat_time(sample_time: float)`

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

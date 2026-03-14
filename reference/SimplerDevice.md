# SimplerDevice

> `Live.SimplerDevice.SimplerDevice`

This class represents a Simpler device.

## View

> `Live.SimplerDevice.SimplerDevice.View`

Representing the view aspects of a simpler device.

### Properties

| Property              | Type            | Settable | Listenable | Description                                                          |
| --------------------- | --------------- | -------- | ---------- | -------------------------------------------------------------------- |
| `canonical_parent`    | `SimplerDevice` | `no`     | `no`       | Get the canonical parent of the View.                                |
| `is_collapsed`        | `bool`          | `yes`    | `no`       | Get/Set/Listen if the device is shown collapsed in the device chain. |
| `sample_end`          | `int`           | `no`     | `yes`      | Access to the modulated samples end position in samples.             |
| `sample_env_fade_in`  | `int`           | `no`     | `yes`      | Access to the envelope fade-in time in samples.                      |
| `sample_env_fade_out` | `int`           | `no`     | `yes`      | Access to the envelope fade-out time in samples.                     |
| `sample_loop_end`     | `int`           | `no`     | `yes`      | Access to the modulated samples loop end position in samples.        |
| `sample_loop_fade`    | `int`           | `no`     | `yes`      | Access to the modulated samples loop fade position in samples.       |
| `sample_loop_start`   | `int`           | `no`     | `yes`      | Access to the modulated samples loop start position in samples.      |
| `sample_start`        | `int`           | `no`     | `yes`      | Access to the modulated samples start position in samples.           |
| `selected_slice`      | `int`           | `yes`    | `yes`      | Access to the selected slice.                                        |

#### `canonical_parent`

- **Type:** `SimplerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the View.

#### `is_collapsed`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set/Listen if the device is shown collapsed in the device chain.

#### `sample_end`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.

#### `sample_env_fade_in`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.

#### `sample_env_fade_out`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.

#### `sample_loop_end`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.

#### `sample_loop_fade`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.

#### `sample_loop_start`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.

#### `sample_start`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.

#### `selected_slice`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the selected slice.

## Properties

| Property                    | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`                             | `no`     | `no`       | Returns true if the Device has the capability to AB compare.                     |
| `can_have_chains`           | `bool`                             | `no`     | `no`       | Returns true if the device is a rack.                                            |
| `can_have_drum_pads`        | `bool`                             | `no`     | `no`       | Returns true if the device is a drum rack.                                       |
| `can_warp_as`               | `bool`                             | `no`     | `yes`      | Returns true if warp_as is available.                                            |
| `can_warp_double`           | `bool`                             | `no`     | `yes`      | Returns true if warp_double is available.                                        |
| `can_warp_half`             | `bool`                             | `no`     | `yes`      | Returns true if warp_half is available.                                          |
| `canonical_parent`          | `Track`                            | `no`     | `no`       | Get the canonical parent of the Device.                                          |
| `class_display_name`        | `str`                              | `no`     | `no`       | Return const access to the name of the device's class name as displayed in Li... |
| `class_name`                | `str`                              | `no`     | `no`       | Return const access to the name of the device's class.                           |
| `is_active`                 | `bool`                             | `no`     | `no`       | Return const access to whether this device is active.                            |
| `is_using_compare_preset_b` | `bool`                             | `yes`    | `no`       | Returns whether the Device has loaded the preset in compare slot B.              |
| `latency_in_ms`             | `float`                            | `no`     | `no`       | Returns the latency of the device in ms.                                         |
| `latency_in_samples`        | `int`                              | `no`     | `no`       | Returns the latency of the device in samples.                                    |
| `multi_sample_mode`         | `bool`                             | `no`     | `yes`      | Returns whether Simpler is in mulit-sample mode.                                 |
| `name`                      | `str`                              | `yes`    | `no`       | Return access to the name of the device.                                         |
| `note_pitch_bend_range`     | `int`                              | `yes`    | `yes`      | Access to the Note Pitch Bend Range in Simpler.                                  |
| `pad_slicing`               | `bool`                             | `yes`    | `yes`      | When set to true, slices can be added in slicing mode by playing notes .that ... |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `no`     | `no`       | Const access to the list of available automatable parameters for this device.    |
| `pitch_bend_range`          | `int`                              | `yes`    | `yes`      | Access to the Pitch Bend Range in Simpler.                                       |
| `playback_mode`             | `int`                              | `yes`    | `yes`      | Access to Simpler's playback mode.                                               |
| `playing_position`          | `float`                            | `no`     | `yes`      | Constant access to the current playing position in the sample.                   |
| `playing_position_enabled`  | `bool`                             | `no`     | `yes`      | Returns whether Simpler is showing the playing position.                         |
| `retrigger`                 | `bool`                             | `yes`    | `yes`      | Access to Simpler's retrigger mode.                                              |
| `sample`                    | `Sample`                           | `no`     | `yes`      | Get the loaded Sample.                                                           |
| `slicing_playback_mode`     | `int`                              | `yes`    | `yes`      | Access to Simpler's slicing playback mode.                                       |
| `type`                      | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `view`                      | `View`                             | `no`     | `no`       | Representing the view aspects of a device.                                       |
| `voices`                    | `int`                              | `yes`    | `yes`      | Access to the number of voices in Simpler.                                       |

### `can_compare_ab`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the Device has the capability to AB compare.

### `can_have_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a rack.

### `can_have_drum_pads`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a drum rack.

### `can_warp_as`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if warp_as is available.

### `can_warp_double`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if warp_double is available.

### `can_warp_half`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if warp_half is available.

### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the Device.

### `class_display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class name as displayed in Live's browser and device chain

### `class_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class.

### `is_active`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in ms.

### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in samples.

### `multi_sample_mode`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns whether Simpler is in mulit-sample mode.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

### `note_pitch_bend_range`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Note Pitch Bend Range in Simpler.

### `pad_slicing`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

When set to true, slices can be added in slicing mode by playing notes .that are not assigned to slices, yet.

### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

### `pitch_bend_range`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Pitch Bend Range in Simpler.

### `playback_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Simpler's playback mode.

### `playing_position`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Constant access to the current playing position in the sample. The returned value is the normalized position between sample start and end.

### `playing_position_enabled`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns whether Simpler is showing the playing position. The returned value is True while the sample is played back

### `retrigger`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Simpler's retrigger mode.

### `sample`

- **Type:** `Sample`
- **Settable:** `no`
- **Listenable:** `yes`

Get the loaded Sample.

### `slicing_playback_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Simpler's slicing playback mode.

### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

### `voices`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the number of voices in Simpler.

## Methods

| Method                      | Returns | Description                                                                      |
| --------------------------- | ------- | -------------------------------------------------------------------------------- |
| `crop()`                    | `None`  | Crop the loaded sample to the active area between start- and end marker.         |
| `guess_playback_length()`   | `float` | Return an estimated beat time for the playback length between start- and end-... |
| `reverse()`                 | `None`  | Reverse the loaded sample.                                                       |
| `warp_as(beat_time: float)` | `None`  | Warp the playback region between start- and end-marker as the given length.      |
| `warp_double()`             | `None`  | Doubles the tempo for region between start- and end-marker.                      |
| `warp_half()`               | `None`  | Halves the tempo for region between start- and end-marker.                       |

### `crop()`

- **Returns:** `None`

Crop the loaded sample to the active area between start- and end marker. Calling this method on an empty simpler raises an error.

### `guess_playback_length()`

- **Returns:** `float`

Return an estimated beat time for the playback length between start- and end-marker. Calling this method on an empty simpler raises an error.

### `reverse()`

- **Returns:** `None`

Reverse the loaded sample. Calling this method on an empty simpler raises an error.

### `warp_as(beat_time: float)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float`

Warp the playback region between start- and end-marker as the given length. Calling this method on an empty simpler raises an error.

### `warp_double()`

- **Returns:** `None`

Doubles the tempo for region between start- and end-marker.

### `warp_half()`

- **Returns:** `None`

Halves the tempo for region between start- and end-marker.

## Enums

### `PlaybackMode`

| Value | Name       |
| ----- | ---------- |
| `0`   | `classic`  |
| `1`   | `one_shot` |
| `2`   | `slicing`  |

### `SlicingPlaybackMode`

| Value | Name   |
| ----- | ------ |
| `0`   | `mono` |
| `1`   | `poly` |
| `2`   | `thru` |

## Module Functions

| Function                        | Returns     | Description                                  |
| ------------------------------- | ----------- | -------------------------------------------- |
| `get_available_voice_numbers()` | `IntVector` | Get a vector of valid Simpler voice numbers. |

### `get_available_voice_numbers()`

- **Returns:** `IntVector`

Get a vector of valid Simpler voice numbers.

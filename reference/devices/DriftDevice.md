# DriftDevice (Module)

## DriftDevice (Class)

> `Live.DriftDevice.DriftDevice`

This class represents a Drift device.

**Live Object:** `yes`

### Properties

| Property                           | Type                               | Supports             |
| ---------------------------------- | ---------------------------------- | -------------------- |
| `can_compare_ab`                   | `bool`                             | `get`                |
| `can_have_chains`                  | `bool`                             | `get`                |
| `can_have_drum_pads`               | `bool`                             | `get`                |
| `canonical_parent`                 | `Track`                            | `get`                |
| `class_display_name`               | `str`                              | `get`                |
| `class_name`                       | `str`                              | `get`                |
| `is_active`                        | `bool`                             | `get`                |
| `is_using_compare_preset_b`        | `bool`                             | `get`/`set`          |
| `latency_in_ms`                    | `float`                            | `get`                |
| `latency_in_samples`               | `int`                              | `get`                |
| `mod_matrix_filter_source_1_index` | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_filter_source_1_list`  | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_filter_source_2_index` | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_filter_source_2_list`  | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_lfo_source_index`      | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_lfo_source_list`       | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_pitch_source_1_index`  | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_pitch_source_1_list`   | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_pitch_source_2_index`  | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_pitch_source_2_list`   | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_shape_source_index`    | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_shape_source_list`     | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_source_1_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_source_1_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_source_2_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_source_2_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_source_3_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_source_3_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_target_1_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_target_1_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_target_2_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_target_2_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `mod_matrix_target_3_index`        | `int`                              | `get`/`set`/`listen` |
| `mod_matrix_target_3_list`         | `tuple[str, Ellipsis]`             | `get`                |
| `name`                             | `str`                              | `get`/`set`          |
| `parameters`                       | `tuple[DeviceParameter, Ellipsis]` | `get`                |
| `pitch_bend_range`                 | `int`                              | `get`/`set`/`listen` |
| `type`                             | `DeviceType`                       | `get`                |
| `view`                             | `Device.View`                      | `get`                |
| `voice_count_index`                | `int`                              | `get`/`set`/`listen` |
| `voice_count_list`                 | `tuple[str, Ellipsis]`             | `get`                |
| `voice_mode_index`                 | `int`                              | `get`/`set`/`listen` |
| `voice_mode_list`                  | `tuple[str, Ellipsis]`             | `get`                |

#### `can_compare_ab`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the Device has the capability to AB compare.

#### `can_have_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a rack.

#### `can_have_drum_pads`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a drum rack.

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the Device.

#### `class_display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class name as displayed in Live's browser and device chain

#### `class_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class.

#### `is_active`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

#### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in ms.

#### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in samples.

#### `mod_matrix_filter_source_1_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the filter mod source 1 index

#### `mod_matrix_filter_source_1_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the filter mod source 1 list

#### `mod_matrix_filter_source_2_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the filter mod source 2 index

#### `mod_matrix_filter_source_2_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the filter mod source 2 list

#### `mod_matrix_lfo_source_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the lfo mod source index

#### `mod_matrix_lfo_source_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the lfo mod source list

#### `mod_matrix_pitch_source_1_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the pitch mod source 1 index

#### `mod_matrix_pitch_source_1_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the pitch mod source 1 list

#### `mod_matrix_pitch_source_2_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the pitch mod source 2 index

#### `mod_matrix_pitch_source_2_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the pitch mod source 2 list

#### `mod_matrix_shape_source_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the shape mod source index

#### `mod_matrix_shape_source_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the shape mod source list

#### `mod_matrix_source_1_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod source 1 index

#### `mod_matrix_source_1_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod source 1 list

#### `mod_matrix_source_2_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod source 2 index

#### `mod_matrix_source_2_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod source 2 list

#### `mod_matrix_source_3_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod source 3 index

#### `mod_matrix_source_3_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod source 3 list

#### `mod_matrix_target_1_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod target 1 index

#### `mod_matrix_target_1_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod target 1 list

#### `mod_matrix_target_2_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod target 2 index

#### `mod_matrix_target_2_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod target 2 list

#### `mod_matrix_target_3_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the custom mod target 3 index

#### `mod_matrix_target_3_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the custom mod target 3 list

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

#### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

#### `pitch_bend_range`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the Pitch Bend Range

#### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

#### `view`

- **Type:** `Device.View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

#### `voice_count_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the voice count index

#### `voice_count_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the voice count list

#### `voice_mode_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the voice mode index

#### `voice_mode_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the voice mode list

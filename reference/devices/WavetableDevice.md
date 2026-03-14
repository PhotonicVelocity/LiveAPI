# WavetableDevice

> `Live.WavetableDevice.WavetableDevice`

This class represents a Wavetable device.

**Live Object:** `yes`

## Properties

| Property                          | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `can_compare_ab`                  | `bool`                             | `no`     | `no`       | Returns true if the Device has the capability to AB compare.                     |
| `can_have_chains`                 | `bool`                             | `no`     | `no`       | Returns true if the device is a rack.                                            |
| `can_have_drum_pads`              | `bool`                             | `no`     | `no`       | Returns true if the device is a drum rack.                                       |
| `canonical_parent`                | `Track`                            | `no`     | `no`       | Get the canonical parent of the Device.                                          |
| `class_display_name`              | `str`                              | `no`     | `no`       | Return const access to the name of the device's class name as displayed in Li... |
| `class_name`                      | `str`                              | `no`     | `no`       | Return const access to the name of the device's class.                           |
| `filter_routing`                  | `int`                              | `yes`    | `yes`      | Return the current filter routing.                                               |
| `is_active`                       | `bool`                             | `no`     | `no`       | Return const access to whether this device is active.                            |
| `is_using_compare_preset_b`       | `bool`                             | `yes`    | `no`       | Returns whether the Device has loaded the preset in compare slot B.              |
| `latency_in_ms`                   | `float`                            | `no`     | `no`       | Returns the latency of the device in ms.                                         |
| `latency_in_samples`              | `int`                              | `no`     | `no`       | Returns the latency of the device in samples.                                    |
| `mono_poly`                       | `int`                              | `yes`    | `yes`      | Return the current voicing mode.                                                 |
| `name`                            | `str`                              | `yes`    | `no`       | Return access to the name of the device.                                         |
| `oscillator_1_effect_mode`        | `int`                              | `yes`    | `yes`      | Return the current effect mode of the oscillator 1.                              |
| `oscillator_1_wavetable_category` | `int`                              | `yes`    | `yes`      | Return the current wavetable category of the oscillator 1.                       |
| `oscillator_1_wavetable_index`    | `int`                              | `yes`    | `yes`      | Return the current wavetable index of the oscillator 1.                          |
| `oscillator_1_wavetables`         | `tuple[str, Ellipsis]`             | `no`     | `yes`      | Get a vector of oscillator 1's wavetable names.                                  |
| `oscillator_2_effect_mode`        | `int`                              | `yes`    | `yes`      | Return the current effect mode of the oscillator 2.                              |
| `oscillator_2_wavetable_category` | `int`                              | `yes`    | `yes`      | Return the current wavetable category of the oscillator 2.                       |
| `oscillator_2_wavetable_index`    | `int`                              | `yes`    | `yes`      | Return the current wavetable index of the oscillator 2.                          |
| `oscillator_2_wavetables`         | `tuple[str, Ellipsis]`             | `no`     | `yes`      | Get a vector of oscillator 2's wavetable names.                                  |
| `oscillator_wavetable_categories` | `tuple[str, Ellipsis]`             | `no`     | `no`       | Get a vector of the available wavetable categories.                              |
| `parameters`                      | `tuple[DeviceParameter, Ellipsis]` | `no`     | `no`       | Const access to the list of available automatable parameters for this device.    |
| `poly_voices`                     | `int`                              | `yes`    | `yes`      | Return the current number of polyphonic voices.                                  |
| `type`                            | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `unison_mode`                     | `int`                              | `yes`    | `yes`      | Return the current unison mode.                                                  |
| `unison_voice_count`              | `int`                              | `yes`    | `yes`      | Return the current number of unison voices.                                      |
| `view`                            | `Device.View`                      | `no`     | `no`       | Representing the view aspects of a device.                                       |
| `visible_modulation_target_names` | `tuple[str, Ellipsis]`             | `no`     | `yes`      | Get the names of all the visible modulation targets.                             |

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

### `filter_routing`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current filter routing.

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

### `mono_poly`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current voicing mode.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

### `oscillator_1_effect_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current effect mode of the oscillator 1.

### `oscillator_1_wavetable_category`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable category of the oscillator 1.

### `oscillator_1_wavetable_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable index of the oscillator 1.

### `oscillator_1_wavetables`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Get a vector of oscillator 1's wavetable names.

### `oscillator_2_effect_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current effect mode of the oscillator 2.

### `oscillator_2_wavetable_category`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable category of the oscillator 2.

### `oscillator_2_wavetable_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable index of the oscillator 2.

### `oscillator_2_wavetables`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Get a vector of oscillator 2's wavetable names.

### `oscillator_wavetable_categories`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Get a vector of the available wavetable categories.

### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

### `poly_voices`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current number of polyphonic voices. Uses the VoiceCount enumeration.

### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

### `unison_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current unison mode.

### `unison_voice_count`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current number of unison voices.

### `view`

- **Type:** `Device.View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

### `visible_modulation_target_names`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Get the names of all the visible modulation targets.

## Methods

| Method                                                               | Returns | Description                                                                  |
| -------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------- |
| `add_parameter_to_modulation_matrix(parameter: DeviceParameter)`     | `int`   | Add a non-pitch parameter to the modulation matrix.                          |
| `get_modulation_target_parameter_name(target_index: int)`            | `str`   | Get the parameter name of the modulation target at the given index.          |
| `get_modulation_value(target_index: int, source: int)`               | `float` | Get the value of a modulation amount for the given target-source connection. |
| `is_parameter_modulatable(parameter: DeviceParameter)`               | `bool`  | Indicate whether the parameter is modulatable.                               |
| `set_modulation_value(target_index: int, source: int, value: float)` | `None`  | Set the value of a modulation amount for the given target-source connection. |

### `add_parameter_to_modulation_matrix(parameter: DeviceParameter)`

- **Returns:** `int`
- **Args:**
  - `parameter: DeviceParameter`

Add a non-pitch parameter to the modulation matrix.

### `get_modulation_target_parameter_name(target_index: int)`

- **Returns:** `str`
- **Args:**
  - `target_index: int`

Get the parameter name of the modulation target at the given index.

### `get_modulation_value(target_index: int, source: int)`

- **Returns:** `float`
- **Args:**
  - `target_index: int`
  - `source: int`

Get the value of a modulation amount for the given target-source connection.

### `is_parameter_modulatable(parameter: DeviceParameter)`

- **Returns:** `bool`
- **Args:**
  - `parameter: DeviceParameter`

Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.

### `set_modulation_value(target_index: int, source: int, value: float)`

- **Returns:** `None`
- **Args:**
  - `target_index: int`
  - `source: int`
  - `value: float`

Set the value of a modulation amount for the given target-source connection.

## Enums

### `EffectMode`

| Value | Name                   |
| ----- | ---------------------- |
| `0`   | `none`                 |
| `1`   | `frequency_modulation` |
| `2`   | `sync_and_pulse_width` |
| `3`   | `warp_and_fold`        |

### `FilterRouting`

| Value | Name       |
| ----- | ---------- |
| `0`   | `serial`   |
| `1`   | `parallel` |
| `2`   | `split`    |

### `ModulationSource`

| Value | Name                    |
| ----- | ----------------------- |
| `0`   | `amp_envelope`          |
| `1`   | `envelope_2`            |
| `2`   | `envelope_3`            |
| `3`   | `lfo_1`                 |
| `4`   | `lfo_2`                 |
| `5`   | `midi_velocity`         |
| `6`   | `midi_note`             |
| `7`   | `midi_pitch_bend`       |
| `8`   | `midi_channel_pressure` |
| `9`   | `midi_mod_wheel`        |
| `10`  | `midi_random`           |

### `UnisonMode`

| Value | Name              |
| ----- | ----------------- |
| `0`   | `none`            |
| `1`   | `classic`         |
| `2`   | `slow_shimmer`    |
| `3`   | `fast_shimmer`    |
| `4`   | `phase_sync`      |
| `5`   | `position_spread` |
| `6`   | `random_note`     |

### `VoiceCount`

| Value | Name    |
| ----- | ------- |
| `0`   | `two`   |
| `1`   | `three` |
| `2`   | `four`  |
| `3`   | `five`  |
| `4`   | `six`   |
| `5`   | `seven` |
| `6`   | `eight` |

### `Voicing`

| Value | Name   |
| ----- | ------ |
| `0`   | `mono` |
| `1`   | `poly` |

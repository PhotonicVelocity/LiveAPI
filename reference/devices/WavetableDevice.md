# WavetableDevice (Module)

## WavetableDevice (Class)

> `Live.WavetableDevice.WavetableDevice`

This class represents a Wavetable device.

**Live Object:** `yes`

### Properties

| Property                                                              | Type                   | Supports             |
| --------------------------------------------------------------------- | ---------------------- | -------------------- |
| [`can_compare_ab`](#can_compare_ab)                                   | `bool`                 | `get`                |
| [`can_have_chains`](#can_have_chains)                                 | `bool`                 | `get`                |
| [`can_have_drum_pads`](#can_have_drum_pads)                           | `bool`                 | `get`                |
| [`canonical_parent`](#canonical_parent)                               | `Track`                | `get`                |
| [`class_display_name`](#class_display_name)                           | `str`                  | `get`                |
| [`class_name`](#class_name)                                           | `str`                  | `get`                |
| [`filter_routing`](#filter_routing)                                   | `int`                  | `get`/`set`/`listen` |
| [`is_active`](#is_active)                                             | `bool`                 | `get`                |
| [`is_using_compare_preset_b`](#is_using_compare_preset_b)             | `bool`                 | `get`/`set`          |
| [`latency_in_ms`](#latency_in_ms)                                     | `float`                | `get`                |
| [`latency_in_samples`](#latency_in_samples)                           | `int`                  | `get`                |
| [`mono_poly`](#mono_poly)                                             | `int`                  | `get`/`set`/`listen` |
| [`name`](#name)                                                       | `str`                  | `get`/`set`          |
| [`oscillator_1_effect_mode`](#oscillator_1_effect_mode)               | `int`                  | `get`/`set`/`listen` |
| [`oscillator_1_wavetable_category`](#oscillator_1_wavetable_category) | `int`                  | `get`/`set`/`listen` |
| [`oscillator_1_wavetable_index`](#oscillator_1_wavetable_index)       | `int`                  | `get`/`set`/`listen` |
| [`oscillator_1_wavetables`](#oscillator_1_wavetables)                 | `StringVector`         | `get`/`listen`       |
| [`oscillator_2_effect_mode`](#oscillator_2_effect_mode)               | `int`                  | `get`/`set`/`listen` |
| [`oscillator_2_wavetable_category`](#oscillator_2_wavetable_category) | `int`                  | `get`/`set`/`listen` |
| [`oscillator_2_wavetable_index`](#oscillator_2_wavetable_index)       | `int`                  | `get`/`set`/`listen` |
| [`oscillator_2_wavetables`](#oscillator_2_wavetables)                 | `StringVector`         | `get`/`listen`       |
| [`oscillator_wavetable_categories`](#oscillator_wavetable_categories) | `StringVector`         | `get`                |
| [`parameters`](#parameters)                                           | `ATimeableValueVector` | `get`                |
| [`poly_voices`](#poly_voices)                                         | `int`                  | `get`/`set`/`listen` |
| [`type`](#type)                                                       | `DeviceType`           | `get`                |
| [`unison_mode`](#unison_mode)                                         | `int`                  | `get`/`set`/`listen` |
| [`unison_voice_count`](#unison_voice_count)                           | `int`                  | `get`/`set`/`listen` |
| [`view`](#view)                                                       | `Device.View`          | `get`                |
| [`visible_modulation_target_names`](#visible_modulation_target_names) | `StringVector`         | `get`/`listen`       |

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

#### `filter_routing`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current filter routing.

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

#### `mono_poly`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current voicing mode.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

#### `oscillator_1_effect_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current effect mode of the oscillator 1.

#### `oscillator_1_wavetable_category`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable category of the oscillator 1.

#### `oscillator_1_wavetable_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable index of the oscillator 1.

#### `oscillator_1_wavetables`

- **Type:** `StringVector`
- **Settable:** `no`
- **Listenable:** `yes`

Get a vector of oscillator 1's wavetable names.

#### `oscillator_2_effect_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current effect mode of the oscillator 2.

#### `oscillator_2_wavetable_category`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable category of the oscillator 2.

#### `oscillator_2_wavetable_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current wavetable index of the oscillator 2.

#### `oscillator_2_wavetables`

- **Type:** `StringVector`
- **Settable:** `no`
- **Listenable:** `yes`

Get a vector of oscillator 2's wavetable names.

#### `oscillator_wavetable_categories`

- **Type:** `StringVector`
- **Settable:** `no`
- **Listenable:** `no`

Get a vector of the available wavetable categories.

#### `parameters`

- **Type:** `ATimeableValueVector`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

#### `poly_voices`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current number of polyphonic voices. Uses the VoiceCount enumeration.

#### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

#### `unison_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current unison mode.

#### `unison_voice_count`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current number of unison voices.

#### `view`

- **Type:** `Device.View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

#### `visible_modulation_target_names`

- **Type:** `StringVector`
- **Settable:** `no`
- **Listenable:** `yes`

Get the names of all the visible modulation targets.

### Methods

| Method                                                                                                 | Returns |
| ------------------------------------------------------------------------------------------------------ | ------- |
| [`add_parameter_to_modulation_matrix()`](#add_parameter_to_modulation_matrixparameter-deviceparameter) | `int`   |
| [`get_modulation_target_parameter_name()`](#get_modulation_target_parameter_nametarget_index-int)      | `str`   |
| [`get_modulation_value()`](#get_modulation_valuetarget_index-int-source-int)                           | `float` |
| [`is_parameter_modulatable()`](#is_parameter_modulatableparameter-deviceparameter)                     | `bool`  |
| [`set_modulation_value()`](#set_modulation_valuetarget_index-int-source-int-value-float)               | `None`  |

#### `add_parameter_to_modulation_matrix(parameter: DeviceParameter)`

- **Returns:** `int`
- **Args:**
  - `parameter: DeviceParameter`

Add a non-pitch parameter to the modulation matrix.

#### `get_modulation_target_parameter_name(target_index: int)`

- **Returns:** `str`
- **Args:**
  - `target_index: int`

Get the parameter name of the modulation target at the given index.

#### `get_modulation_value(target_index: int, source: int)`

- **Returns:** `float`
- **Args:**
  - `target_index: int`
  - `source: int`

Get the value of a modulation amount for the given target-source connection.

#### `is_parameter_modulatable(parameter: DeviceParameter)`

- **Returns:** `bool`
- **Args:**
  - `parameter: DeviceParameter`

Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.

#### `set_modulation_value(target_index: int, source: int, value: float)`

- **Returns:** `None`
- **Args:**
  - `target_index: int`
  - `source: int`
  - `value: float`

Set the value of a modulation amount for the given target-source connection.

## Enums

### EffectMode

> `Live.WavetableDevice.EffectMode`

| Value | Name                   |
| ----- | ---------------------- |
| `0`   | `none`                 |
| `1`   | `frequency_modulation` |
| `2`   | `sync_and_pulse_width` |
| `3`   | `warp_and_fold`        |

### FilterRouting

> `Live.WavetableDevice.FilterRouting`

| Value | Name       |
| ----- | ---------- |
| `0`   | `serial`   |
| `1`   | `parallel` |
| `2`   | `split`    |

### ModulationSource

> `Live.WavetableDevice.ModulationSource`

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

### UnisonMode

> `Live.WavetableDevice.UnisonMode`

| Value | Name              |
| ----- | ----------------- |
| `0`   | `none`            |
| `1`   | `classic`         |
| `2`   | `slow_shimmer`    |
| `3`   | `fast_shimmer`    |
| `4`   | `phase_sync`      |
| `5`   | `position_spread` |
| `6`   | `random_note`     |

### VoiceCount

> `Live.WavetableDevice.VoiceCount`

| Value | Name    |
| ----- | ------- |
| `0`   | `two`   |
| `1`   | `three` |
| `2`   | `four`  |
| `3`   | `five`  |
| `4`   | `six`   |
| `5`   | `seven` |
| `6`   | `eight` |

### Voicing

> `Live.WavetableDevice.Voicing`

| Value | Name   |
| ----- | ------ |
| `0`   | `mono` |
| `1`   | `poly` |

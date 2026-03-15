# HybridReverbDevice (Module)

## HybridReverbDevice (Class)

> `Live.HybridReverbDevice.HybridReverbDevice`

This class represents a Hybrid Reverb device.

**Live Object:** `yes`

### Properties

| Property                                                  | Type                      | Supports             |
| --------------------------------------------------------- | ------------------------- | -------------------- |
| [`can_compare_ab`](#can_compare_ab)                       | `bool`                    | `get`                |
| [`can_have_chains`](#can_have_chains)                     | `bool`                    | `get`                |
| [`can_have_drum_pads`](#can_have_drum_pads)               | `bool`                    | `get`                |
| [`canonical_parent`](#canonical_parent)                   | `Track`                   | `get`                |
| [`class_display_name`](#class_display_name)               | `str`                     | `get`                |
| [`class_name`](#class_name)                               | `str`                     | `get`                |
| [`ir_attack_time`](#ir_attack_time)                       | `float`                   | `get`/`set`/`listen` |
| [`ir_category_index`](#ir_category_index)                 | `int`                     | `get`/`set`/`listen` |
| [`ir_category_list`](#ir_category_list)                   | `Vector[str]`             | `get`                |
| [`ir_decay_time`](#ir_decay_time)                         | `float`                   | `get`/`set`/`listen` |
| [`ir_file_index`](#ir_file_index)                         | `int`                     | `get`/`set`/`listen` |
| [`ir_file_list`](#ir_file_list)                           | `Vector[str]`             | `get`/`listen`       |
| [`ir_size_factor`](#ir_size_factor)                       | `float`                   | `get`/`set`/`listen` |
| [`ir_time_shaping_on`](#ir_time_shaping_on)               | `bool`                    | `get`/`set`/`listen` |
| [`is_active`](#is_active)                                 | `bool`                    | `get`                |
| [`is_using_compare_preset_b`](#is_using_compare_preset_b) | `bool`                    | `get`/`set`          |
| [`latency_in_ms`](#latency_in_ms)                         | `float`                   | `get`                |
| [`latency_in_samples`](#latency_in_samples)               | `int`                     | `get`                |
| [`name`](#name)                                           | `str`                     | `get`/`set`          |
| [`parameters`](#parameters)                               | `Vector[DeviceParameter]` | `get`                |
| [`type`](#type)                                           | `DeviceType`              | `get`                |
| [`view`](#view)                                           | `Device.View`             | `get`                |

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

#### `ir_attack_time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IrAttackTime

#### `ir_category_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IR category index

#### `ir_category_list`

- **Type:** `Vector[str]`
- **Settable:** `no`
- **Listenable:** `no`

Return the current IR categories list

#### `ir_decay_time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IrDecayTime

#### `ir_file_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IR file index

#### `ir_file_list`

- **Type:** `Vector[str]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current IR file list

#### `ir_size_factor`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IrSizeFactor

#### `ir_time_shaping_on`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current IrTimeShapingOn

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

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

#### `parameters`

- **Type:** `Vector[DeviceParameter]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

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

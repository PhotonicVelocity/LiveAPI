# Device (Module)

## Device (Class)

> `Live.Device.Device`

This class represents a MIDI or Audio DSP-Device in Live.

**Live Object:** `yes`

**Access via:**

- `Track.View.selected_device`

### Properties

| Property                                                  | Type                               | Supports             |
| --------------------------------------------------------- | ---------------------------------- | -------------------- |
| [`can_compare_ab`](#can_compare_ab)                       | `bool`                             | `get`                |
| [`can_have_chains`](#can_have_chains)                     | `bool`                             | `get`                |
| [`can_have_drum_pads`](#can_have_drum_pads)               | `bool`                             | `get`                |
| [`canonical_parent`](#canonical_parent)                   | `Track`                            | `get`                |
| [`class_display_name`](#class_display_name)               | `str`                              | `get`                |
| [`class_name`](#class_name)                               | `str`                              | `get`                |
| [`is_active`](#is_active)                                 | `bool`                             | `get`/`listen`       |
| [`is_using_compare_preset_b`](#is_using_compare_preset_b) | `bool`                             | `get`/`set`/`listen` |
| [`latency_in_ms`](#latency_in_ms)                         | `float`                            | `get`/`listen`       |
| [`latency_in_samples`](#latency_in_samples)               | `int`                              | `get`/`listen`       |
| [`name`](#name)                                           | `str`                              | `get`/`set`/`listen` |
| [`parameters`](#parameters)                               | `tuple[DeviceParameter, Ellipsis]` | `get`/`listen`       |
| [`type`](#type)                                           | `DeviceType`                       | `get`                |
| [`view`](#view)                                           | `View`                             | `get`                |

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
- **Listenable:** `yes`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

#### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the latency of the device in ms.

#### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the latency of the device in samples.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Return access to the name of the device.

#### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the list of available automatable parameters for this device.

#### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

#### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

### Methods

| Method                                                                     | Returns |
| -------------------------------------------------------------------------- | ------- |
| [`save_preset_to_compare_ab_slot()`](#save_preset_to_compare_ab_slot)      | `None`  |
| [`store_chosen_bank()`](#store_chosen_bankscript_index-int-bank_index-int) | `None`  |

#### `save_preset_to_compare_ab_slot()`

- **Returns:** `None`

Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.

#### `store_chosen_bank(script_index: int, bank_index: int)`

- **Returns:** `None`
- **Args:**
  - `script_index: int`
  - `bank_index: int`

Set the selected bank in the device for persistency.

## Device.View (Subclass)

> `Live.Device.Device.View`

Representing the view aspects of a device.

**Live Object:** `yes`

### Properties

| Property                                | Type     | Supports             |
| --------------------------------------- | -------- | -------------------- |
| [`canonical_parent`](#canonical_parent) | `Device` | `get`                |
| [`is_collapsed`](#is_collapsed)         | `bool`   | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `Device`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the View.

#### `is_collapsed`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set/Listen if the device is shown collapsed in the device chain.

## Enums

### DeviceType

> `Live.Device.DeviceType`

The type of the device.

| Value | Name           |
| ----- | -------------- |
| `0`   | `undefined`    |
| `1`   | `instrument`   |
| `2`   | `audio_effect` |
| `4`   | `midi_effect`  |

## ATimeableValueVector (Type)

> `Live.Device.ATimeableValueVector`

### Methods

| Method                                      | Returns |
| ------------------------------------------- | ------- |
| [`append()`](#appendvalue-deviceparameter)  | `None`  |
| [`extend()`](#extendvalues-deviceparameter) | `None`  |

#### `append(value: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `value: DeviceParameter`

#### `extend(values: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `values: DeviceParameter`

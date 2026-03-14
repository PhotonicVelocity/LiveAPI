# Device

> `Live.Device.Device`

This class represents a MIDI or Audio DSP-Device in Live.

## View

> `Live.Device.Device.View`

Representing the view aspects of a device.

### Properties

| Property           | Type     | Settable | Listenable | Description                                                          |
| ------------------ | -------- | -------- | ---------- | -------------------------------------------------------------------- |
| `canonical_parent` | `Device` | `no`     | `no`       | Get the canonical parent of the View.                                |
| `is_collapsed`     | `bool`   | `yes`    | `yes`      | Get/Set/Listen if the device is shown collapsed in the device chain. |

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

## Properties

| Property                    | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`                             | `no`     | `no`       | Returns true if the Device has the capability to AB compare.                     |
| `can_have_chains`           | `bool`                             | `no`     | `no`       | Returns true if the device is a rack.                                            |
| `can_have_drum_pads`        | `bool`                             | `no`     | `no`       | Returns true if the device is a drum rack.                                       |
| `canonical_parent`          | `Track`                            | `no`     | `no`       | Get the canonical parent of the Device.                                          |
| `class_display_name`        | `str`                              | `no`     | `no`       | Return const access to the name of the device's class name as displayed in Li... |
| `class_name`                | `str`                              | `no`     | `no`       | Return const access to the name of the device's class.                           |
| `is_active`                 | `bool`                             | `no`     | `yes`      | Return const access to whether this device is active.                            |
| `is_using_compare_preset_b` | `bool`                             | `yes`    | `yes`      | Returns whether the Device has loaded the preset in compare slot B.              |
| `latency_in_ms`             | `float`                            | `no`     | `yes`      | Returns the latency of the device in ms.                                         |
| `latency_in_samples`        | `int`                              | `no`     | `yes`      | Returns the latency of the device in samples.                                    |
| `name`                      | `str`                              | `yes`    | `yes`      | Return access to the name of the device.                                         |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `no`     | `yes`      | Const access to the list of available automatable parameters for this device.    |
| `type`                      | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `view`                      | `View`                             | `no`     | `no`       | Representing the view aspects of a device.                                       |

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

### `is_active`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the latency of the device in ms.

### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the latency of the device in samples.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Return access to the name of the device.

### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the list of available automatable parameters for this device.

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

## Methods

| Method                                                  | Returns | Description                                                   |
| ------------------------------------------------------- | ------- | ------------------------------------------------------------- |
| `save_preset_to_compare_ab_slot()`                      | `None`  | Saves the current state of the device to the compare AB slot. |
| `store_chosen_bank(script_index: int, bank_index: int)` | `None`  | Set the selected bank in the device for persistency.          |

### `save_preset_to_compare_ab_slot()`

- **Returns:** `None`

Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.

### `store_chosen_bank(script_index: int, bank_index: int)`

- **Returns:** `None`
- **Args:**
  - `script_index: int`
  - `bank_index: int`

Set the selected bank in the device for persistency.

## Enums

### `DeviceType`

The type of the device.

| Value | Name           |
| ----- | -------------- |
| `0`   | `undefined`    |
| `1`   | `instrument`   |
| `2`   | `audio_effect` |
| `4`   | `midi_effect`  |

## ATimeableValueVector

> `Live.Device.ATimeableValueVector`

### Methods

| Method                            | Returns | Description |
| --------------------------------- | ------- | ----------- |
| `append(value: DeviceParameter)`  | `None`  |             |
| `extend(values: DeviceParameter)` | `None`  |             |

#### `append(value: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `value: DeviceParameter`

#### `extend(values: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `values: DeviceParameter`

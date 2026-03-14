# MaxDevice (Module)

## MaxDevice (Class)

> `Live.MaxDevice.MaxDevice`

This class represents a Max for Live device.

**Live Object:** `yes`

### Properties

| Property                    | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `audio_inputs`              | `tuple`                            | `no`     | `yes`      | Const access to a list of all audio inputs of the device.                        |
| `audio_outputs`             | `tuple`                            | `no`     | `yes`      | Const access to a list of all audio outputs of the device.                       |
| `can_compare_ab`            | `bool`                             | `no`     | `no`       | Returns true if the Device has the capability to AB compare.                     |
| `can_have_chains`           | `bool`                             | `no`     | `no`       | Returns true if the device is a rack.                                            |
| `can_have_drum_pads`        | `bool`                             | `no`     | `no`       | Returns true if the device is a drum rack.                                       |
| `canonical_parent`          | `Track`                            | `no`     | `no`       | Get the canonical parent of the Device.                                          |
| `class_display_name`        | `str`                              | `no`     | `no`       | Return const access to the name of the device's class name as displayed in Li... |
| `class_name`                | `str`                              | `no`     | `no`       | Return const access to the name of the device's class.                           |
| `is_active`                 | `bool`                             | `no`     | `no`       | Return const access to whether this device is active.                            |
| `is_using_compare_preset_b` | `bool`                             | `yes`    | `no`       | Returns whether the Device has loaded the preset in compare slot B.              |
| `latency_in_ms`             | `float`                            | `no`     | `no`       | Returns the latency of the device in ms.                                         |
| `latency_in_samples`        | `int`                              | `no`     | `no`       | Returns the latency of the device in samples.                                    |
| `midi_inputs`               | `tuple`                            | `no`     | `yes`      | Const access to a list of all midi outputs of the device.                        |
| `midi_outputs`              | `tuple`                            | `no`     | `yes`      | Const access to a list of all midi outputs of the device.                        |
| `name`                      | `str`                              | `yes`    | `no`       | Return access to the name of the device.                                         |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `no`     | `no`       | Const access to the list of available automatable parameters for this device.    |
| `type`                      | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `view`                      | `Device.View`                      | `no`     | `no`       | Representing the view aspects of a device.                                       |

#### `audio_inputs`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all audio inputs of the device.

#### `audio_outputs`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all audio outputs of the device.

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

#### `midi_inputs`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all midi outputs of the device.

#### `midi_outputs`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of all midi outputs of the device.

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

### Methods

| Method                                             | Returns | Description                                                                      |
| -------------------------------------------------- | ------- | -------------------------------------------------------------------------------- |
| `get_bank_count()`                                 | `int`   | Get the number of parameter banks.                                               |
| `get_bank_name(bank_index: int)`                   | `str`   | Get the name of a parameter bank given by index.                                 |
| `get_bank_parameters(bank_index: int)`             | `list`  | Get the indices of parameters of the given bank index.                           |
| `get_value_item_icons(parameter: DeviceParameter)` | `list`  | Get a list of icon identifier strings for a list parameter's values.An empty ... |

#### `get_bank_count()`

- **Returns:** `int`

Get the number of parameter banks. This is related to hardware control surfaces.

#### `get_bank_name(bank_index: int)`

- **Returns:** `str`
- **Args:**
  - `bank_index: int`

Get the name of a parameter bank given by index. This is related to hardware control surfaces.

#### `get_bank_parameters(bank_index: int)`

- **Returns:** `list`
- **Args:**
  - `bank_index: int`

Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.

#### `get_value_item_icons(parameter: DeviceParameter)`

- **Returns:** `list`
- **Args:**
  - `parameter: DeviceParameter`

Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.

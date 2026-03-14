# MeldDevice

> `Live.MeldDevice.MeldDevice`

This class represents a Meld device.

**Live Object:** `yes`

## Properties

| Property                    | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
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
| `mono_poly`                 | `int`                              | `yes`    | `yes`      | Returns the mode of Polyphony.                                                   |
| `name`                      | `str`                              | `yes`    | `no`       | Return access to the name of the device.                                         |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `no`     | `no`       | Const access to the list of available automatable parameters for this device.    |
| `poly_voices`               | `int`                              | `yes`    | `yes`      | Return the Poly Voice count.                                                     |
| `selected_engine`           | `bool`                             | `yes`    | `yes`      | Return what Voice Engine is selected.                                            |
| `type`                      | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `unison_voices`             | `int`                              | `yes`    | `yes`      | Return the Unison Voice count.                                                   |
| `view`                      | `Device.View`                      | `no`     | `no`       | Representing the view aspects of a device.                                       |

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

Returns the mode of Polyphony

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

### `poly_voices`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the Poly Voice count

### `selected_engine`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Return what Voice Engine is selected

### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

### `unison_voices`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the Unison Voice count

### `view`

- **Type:** `Device.View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

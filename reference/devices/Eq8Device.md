# Eq8Device (Module)

## Eq8Device (Class)

> `Live.Eq8Device.Eq8Device`

This class represents an Eq8 device.

**Live Object:** `yes`

### Properties

| Property                    | Type                               | Settable | Listenable | Description                                                                      |
| --------------------------- | ---------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`                             | `no`     | `no`       | Returns true if the Device has the capability to AB compare.                     |
| `can_have_chains`           | `bool`                             | `no`     | `no`       | Returns true if the device is a rack.                                            |
| `can_have_drum_pads`        | `bool`                             | `no`     | `no`       | Returns true if the device is a drum rack.                                       |
| `canonical_parent`          | `Track`                            | `no`     | `no`       | Get the canonical parent of the Device.                                          |
| `class_display_name`        | `str`                              | `no`     | `no`       | Return const access to the name of the device's class name as displayed in Li... |
| `class_name`                | `str`                              | `no`     | `no`       | Return const access to the name of the device's class.                           |
| `edit_mode`                 | `bool`                             | `yes`    | `yes`      | Access to Eq8's edit mode.                                                       |
| `global_mode`               | `int`                              | `yes`    | `yes`      | Access to Eq8's global mode.                                                     |
| `is_active`                 | `bool`                             | `no`     | `no`       | Return const access to whether this device is active.                            |
| `is_using_compare_preset_b` | `bool`                             | `yes`    | `no`       | Returns whether the Device has loaded the preset in compare slot B.              |
| `latency_in_ms`             | `float`                            | `no`     | `no`       | Returns the latency of the device in ms.                                         |
| `latency_in_samples`        | `int`                              | `no`     | `no`       | Returns the latency of the device in samples.                                    |
| `name`                      | `str`                              | `yes`    | `no`       | Return access to the name of the device.                                         |
| `oversample`                | `bool`                             | `yes`    | `yes`      | Access to Eq8's oversample value.                                                |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `no`     | `no`       | Const access to the list of available automatable parameters for this device.    |
| `type`                      | `DeviceType`                       | `no`     | `no`       | Return the type of the device.                                                   |
| `view`                      | `View`                             | `no`     | `no`       | Representing the view aspects of a device.                                       |

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

#### `edit_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Eq8's edit mode.

#### `global_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Eq8's global mode.

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

#### `oversample`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to Eq8's oversample value.

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

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

## Eq8Device.View (Subclass)

> `Live.Eq8Device.Eq8Device.View`

Representing the view aspects of an Eq8 device.

**Live Object:** `yes`

### Properties

| Property           | Type        | Settable | Listenable | Description                                                          |
| ------------------ | ----------- | -------- | ---------- | -------------------------------------------------------------------- |
| `canonical_parent` | `Eq8Device` | `no`     | `no`       | Get the canonical parent of the View.                                |
| `is_collapsed`     | `bool`      | `yes`    | `no`       | Get/Set/Listen if the device is shown collapsed in the device chain. |
| `selected_band`    | `int`       | `yes`    | `yes`      | Access to the selected filter band.                                  |

#### `canonical_parent`

- **Type:** `Eq8Device`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the View.

#### `is_collapsed`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set/Listen if the device is shown collapsed in the device chain.

#### `selected_band`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the selected filter band.

## Enums

### `EditMode`

| Value | Name |
| ----- | ---- |
| `0`   | `a`  |
| `1`   | `b`  |

### `GlobalMode`

| Value | Name         |
| ----- | ------------ |
| `0`   | `stereo`     |
| `1`   | `left_right` |
| `2`   | `mid_side`   |

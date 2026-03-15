# Eq8Device (Module)

## Eq8Device (Class)

> `Live.Eq8Device.Eq8Device`

This class represents an Eq8 device.

**Live Object:** `yes`

### Properties

| Property                                                  | Type                               | Supports             |
| --------------------------------------------------------- | ---------------------------------- | -------------------- |
| [`can_compare_ab`](#can_compare_ab)                       | `bool`                             | `get`                |
| [`can_have_chains`](#can_have_chains)                     | `bool`                             | `get`                |
| [`can_have_drum_pads`](#can_have_drum_pads)               | `bool`                             | `get`                |
| [`canonical_parent`](#canonical_parent)                   | `Track`                            | `get`                |
| [`class_display_name`](#class_display_name)               | `str`                              | `get`                |
| [`class_name`](#class_name)                               | `str`                              | `get`                |
| [`edit_mode`](#edit_mode)                                 | `bool`                             | `get`/`set`/`listen` |
| [`global_mode`](#global_mode)                             | `int`                              | `get`/`set`/`listen` |
| [`is_active`](#is_active)                                 | `bool`                             | `get`                |
| [`is_using_compare_preset_b`](#is_using_compare_preset_b) | `bool`                             | `get`/`set`          |
| [`latency_in_ms`](#latency_in_ms)                         | `float`                            | `get`                |
| [`latency_in_samples`](#latency_in_samples)               | `int`                              | `get`                |
| [`name`](#name)                                           | `str`                              | `get`/`set`          |
| [`oversample`](#oversample)                               | `bool`                             | `get`/`set`/`listen` |
| [`parameters`](#parameters)                               | `tuple[DeviceParameter, Ellipsis]` | `get`                |
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

| Property                                | Type        | Supports             |
| --------------------------------------- | ----------- | -------------------- |
| [`canonical_parent`](#canonical_parent) | `Eq8Device` | `get`                |
| [`is_collapsed`](#is_collapsed)         | `bool`      | `get`/`set`          |
| [`selected_band`](#selected_band)       | `int`       | `get`/`set`/`listen` |

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

### EditMode

> `Live.Eq8Device.EditMode`

| Value | Name |
| ----- | ---- |
| `0`   | `a`  |
| `1`   | `b`  |

### GlobalMode

> `Live.Eq8Device.GlobalMode`

| Value | Name         |
| ----- | ------------ |
| `0`   | `stereo`     |
| `1`   | `left_right` |
| `2`   | `mid_side`   |

# DeviceParameter

> `Live.DeviceParameter.DeviceParameter`

This class represents a (automatable) parameter within a MIDI or Audio DSP-Device.

## Properties

| Property            | Type                   | Settable | Listenable | Description                                                                      |
| ------------------- | ---------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `automation_state`  | `int`                  | `no`     | `yes`      | Returns state of type AutomationState.                                           |
| `canonical_parent`  | `Device`               | `no`     | `no`       | Get the canonical parent of the device parameter.                                |
| `default_value`     | `float`                | `no`     | `no`       | Return the default value for this parameter.                                     |
| `display_value`     | `float`                | `yes`    | `yes`      | Get/Set the current value (as visible in the GUI) this parameter.                |
| `is_enabled`        | `bool`                 | `no`     | `no`       | Returns false if the parameter has been macro mapped or disabled by Max.         |
| `is_quantized`      | `bool`                 | `no`     | `no`       | Returns True, if this value is a boolean or integer like switch.                 |
| `max`               | `float`                | `no`     | `no`       | Returns const access to the upper value of the allowed range for this parameter. |
| `min`               | `float`                | `no`     | `no`       | Returns const access to the lower value of the allowed range for this parameter. |
| `name`              | `str`                  | `no`     | `yes`      | Returns const access the name of this parameter, as visible in Lives automati... |
| `original_name`     | `str`                  | `no`     | `no`       | Returns const access the original name of this parameter, unaffected of any r... |
| `short_value_items` | `tuple[str, Ellipsis]` | `no`     | `no`       | Return the list of possible values for this parameter.                           |
| `state`             | `int`                  | `no`     | `yes`      | Returns the state of the parameter: - enabled - the parameter's value can be ... |
| `value`             | `float`                | `yes`    | `yes`      | Get/Set the current internal value of this parameter.                            |
| `value_items`       | `tuple[str, Ellipsis]` | `no`     | `no`       | Return the list of possible values for this parameter.                           |

### `automation_state`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns state of type AutomationState.

### `canonical_parent`

- **Type:** `Device`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the device parameter.

### `default_value`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Return the default value for this parameter. A Default value is only available for non-quantized parameter types (see 'is_quantized').

### `display_value`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current value (as visible in the GUI) this parameter. The value must be inside the min/max properties of this device.

### `is_enabled`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns false if the parameter has been macro mapped or disabled by Max.

### `is_quantized`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns True, if this value is a boolean or integer like switch. Non quantized values are continues float values.

### `max`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns const access to the upper value of the allowed range for this parameter

### `min`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns const access to the lower value of the allowed range for this parameter

### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Returns const access the name of this parameter, as visible in Lives automation choosers.

### `original_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Returns const access the original name of this parameter, unaffected of any renamings.

### `short_value_items`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the list of possible values for this parameter. Like value_items, but prefers short value names if available. Raises an error if 'is_quantized' is False.

### `state`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the state of the parameter: - enabled - the parameter's value can be changed, - irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled, - disabled - the parameter's value cannot be changed.

### `value`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current internal value of this parameter. The value must be inside the min/max properties of this device.

### `value_items`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.

## Methods

| Method                        | Returns | Description                                                                      |
| ----------------------------- | ------- | -------------------------------------------------------------------------------- |
| `begin_gesture()`             | `None`  | Notify the begin of a modification of the parameter, when a sequence of modif... |
| `end_gesture()`               | `None`  | Notify the end of a modification of the parameter.                               |
| `re_enable_automation()`      | `None`  | Reenable automation for this parameter.                                          |
| `str_for_value(value: float)` | `str`   | Return a string representation of the given value.                               |

### `begin_gesture()`

- **Returns:** `None`

Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent group -- for Sexample, when recording automation.

### `end_gesture()`

- **Returns:** `None`

Notify the end of a modification of the parameter. See begin_gesture.

### `re_enable_automation()`

- **Returns:** `None`

Reenable automation for this parameter.

### `str_for_value(value: float)`

- **Returns:** `str`
- **Args:**
  - `value: float`

Return a string representation of the given value. To be used for display purposes only. This value can include characters like 'db' or 'hz', depending on the type of the parameter.

## Enums

### `AutomationState`

| Value | Name         |
| ----- | ------------ |
| `0`   | `none`       |
| `1`   | `playing`    |
| `2`   | `overridden` |

### `ParameterState`

| Value | Name         |
| ----- | ------------ |
| `0`   | `enabled`    |
| `1`   | `irrelevant` |
| `2`   | `disabled`   |

# SpectralResonatorDevice (Module)

## SpectralResonatorDevice (Class)

> `Live.SpectralResonatorDevice.SpectralResonatorDevice`

This class represents a Spectral Resonator device.

**Live Object:** `yes`

### Properties

| Property                    | Type                               | Supports             |
| --------------------------- | ---------------------------------- | -------------------- |
| `can_compare_ab`            | `bool`                             | `get`                |
| `can_have_chains`           | `bool`                             | `get`                |
| `can_have_drum_pads`        | `bool`                             | `get`                |
| `canonical_parent`          | `Track`                            | `get`                |
| `class_display_name`        | `str`                              | `get`                |
| `class_name`                | `str`                              | `get`                |
| `frequency_dial_mode`       | `int`                              | `get`/`set`/`listen` |
| `frequency_dial_mode_list`  | `tuple[str, Ellipsis]`             | `get`/`listen`       |
| `is_active`                 | `bool`                             | `get`                |
| `is_using_compare_preset_b` | `bool`                             | `get`/`set`          |
| `latency_in_ms`             | `float`                            | `get`                |
| `latency_in_samples`        | `int`                              | `get`                |
| `midi_gate`                 | `int`                              | `get`/`set`/`listen` |
| `midi_gate_list`            | `tuple[str, Ellipsis]`             | `get`/`listen`       |
| `mod_mode`                  | `int`                              | `get`/`set`/`listen` |
| `mod_mode_list`             | `tuple[str, Ellipsis]`             | `get`/`listen`       |
| `mono_poly`                 | `int`                              | `get`/`set`/`listen` |
| `mono_poly_list`            | `tuple[str, Ellipsis]`             | `get`/`listen`       |
| `name`                      | `str`                              | `get`/`set`          |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `get`                |
| `pitch_bend_range`          | `int`                              | `get`/`set`/`listen` |
| `pitch_mode`                | `int`                              | `get`/`set`/`listen` |
| `pitch_mode_list`           | `tuple[str, Ellipsis]`             | `get`/`listen`       |
| `polyphony`                 | `int`                              | `get`/`set`/`listen` |
| `type`                      | `DeviceType`                       | `get`                |
| `view`                      | `Device.View`                      | `get`                |

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

#### `frequency_dial_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current frequency dial mode index

#### `frequency_dial_mode_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current frequency dial mode list

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

#### `midi_gate`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current midi gate index

#### `midi_gate_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current midi gate list

#### `mod_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current mod mode index

#### `mod_mode_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current mod mode list

#### `mono_poly`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current mono poly mode index

#### `mono_poly_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current mono poly mode list

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

#### `pitch_bend_range`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current pitch bend range

#### `pitch_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current pitch mode index

#### `pitch_mode_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return the current pitch mode list

#### `polyphony`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Return the current polyphony

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

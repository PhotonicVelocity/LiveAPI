# CompressorDevice (Module)

## CompressorDevice (Class)

> `Live.CompressorDevice.CompressorDevice`

This class represents a Compressor device.

**Live Object:** `yes`

### Properties

| Property                           | Type                               | Supports             |
| ---------------------------------- | ---------------------------------- | -------------------- |
| `available_input_routing_channels` | `tuple[RoutingChannel, Ellipsis]`  | `get`/`listen`       |
| `available_input_routing_types`    | `tuple[RoutingType, Ellipsis]`     | `get`/`listen`       |
| `can_compare_ab`                   | `bool`                             | `get`                |
| `can_have_chains`                  | `bool`                             | `get`                |
| `can_have_drum_pads`               | `bool`                             | `get`                |
| `canonical_parent`                 | `Track`                            | `get`                |
| `class_display_name`               | `str`                              | `get`                |
| `class_name`                       | `str`                              | `get`                |
| `input_routing_channel`            | `RoutingChannel`                   | `get`/`set`/`listen` |
| `input_routing_type`               | `RoutingType`                      | `get`/`set`/`listen` |
| `is_active`                        | `bool`                             | `get`                |
| `is_using_compare_preset_b`        | `bool`                             | `get`/`set`          |
| `latency_in_ms`                    | `float`                            | `get`                |
| `latency_in_samples`               | `int`                              | `get`                |
| `name`                             | `str`                              | `get`/`set`          |
| `parameters`                       | `tuple[DeviceParameter, Ellipsis]` | `get`                |
| `type`                             | `DeviceType`                       | `get`                |
| `view`                             | `Device.View`                      | `get`                |

#### `available_input_routing_channels`

- **Type:** `tuple[RoutingChannel, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of source channels for input routing in the sidechain.

#### `available_input_routing_types`

- **Type:** `tuple[RoutingType, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of source types for input routing in the sidechain.

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

#### `input_routing_channel`

- **Type:** `RoutingChannel`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current source channel for input routing in the sidechain. Raises ValueError if the channel isn't one of the current values in available_input_routing_channels.

#### `input_routing_type`

- **Type:** `RoutingType`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current source type for input routing in the sidechain. Raises ValueError if the type isn't one of the current values in available_input_routing_types.

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

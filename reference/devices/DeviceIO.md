# DeviceIO (Module)

## DeviceIO (Class)

> `Live.DeviceIO.DeviceIO`

This class represents a specific input or output bus of a device.

**Live Object:** `yes`

### Properties

| Property                                                                                | Type                   | Supports             |
| --------------------------------------------------------------------------------------- | ---------------------- | -------------------- |
| [`available_routing_channels`](#available_routing_channels)                             | `RoutingChannelVector` | `get`/`listen`       |
| [`available_routing_types`](#available_routing_types)                                   | `RoutingTypeVector`    | `get`/`listen`       |
| [`canonical_parent`](#canonical_parent)                                                 | `MaxDevice`            | `get`                |
| [`default_external_routing_channel_is_none`](#default_external_routing_channel_is_none) | `bool`                 | `get`/`set`          |
| [`routing_channel`](#routing_channel)                                                   | `RoutingChannel`       | `get`/`set`/`listen` |
| [`routing_type`](#routing_type)                                                         | `RoutingType`          | `get`/`set`/`listen` |

#### `available_routing_channels`

- **Type:** `RoutingChannelVector`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of channels for this IO endpoint.

#### `available_routing_types`

- **Type:** `RoutingTypeVector`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of available routing types for this IO endpoint.

#### `canonical_parent`

- **Type:** `MaxDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the device IO.

#### `default_external_routing_channel_is_none`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get and set whether the default routing channel for External routing types is none.

#### `routing_channel`

- **Type:** `RoutingChannel`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current routing channel. Raises ValueError if the channel isn't one of the current values in available_routing_channels.

#### `routing_type`

- **Type:** `RoutingType`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current routing type. Raises ValueError if the type isn't one of the current values in available_routing_types.

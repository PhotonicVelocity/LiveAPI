# DeviceIO

> `Live.DeviceIO.DeviceIO`

This class represents a specific input or output bus of a device.

## Properties

| Property                                   | Type                              | Settable | Listenable | Description                                                                      |
| ------------------------------------------ | --------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `available_routing_channels`               | `tuple[RoutingChannel, Ellipsis]` | `no`     | `yes`      | Return a list of channels for this IO endpoint.                                  |
| `available_routing_types`                  | `tuple[RoutingType, Ellipsis]`    | `no`     | `yes`      | Return a list of available routing types for this IO endpoint.                   |
| `canonical_parent`                         | `MaxDevice`                       | `no`     | `no`       | Get the canonical parent of the device IO.                                       |
| `default_external_routing_channel_is_none` | `bool`                            | `yes`    | `no`       | Get and set whether the default routing channel for External routing types is... |
| `routing_channel`                          | `RoutingChannel`                  | `yes`    | `yes`      | Get and set the current routing channel.                                         |
| `routing_type`                             | `RoutingType`                     | `yes`    | `yes`      | Get and set the current routing type.                                            |

### `available_routing_channels`

- **Type:** `tuple[RoutingChannel, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of channels for this IO endpoint.

### `available_routing_types`

- **Type:** `tuple[RoutingType, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of available routing types for this IO endpoint.

### `canonical_parent`

- **Type:** `MaxDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the device IO.

### `default_external_routing_channel_is_none`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get and set whether the default routing channel for External routing types is none.

### `routing_channel`

- **Type:** `RoutingChannel`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current routing channel. Raises ValueError if the channel isn't one of the current values in available_routing_channels.

### `routing_type`

- **Type:** `RoutingType`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current routing type. Raises ValueError if the type isn't one of the current values in available_routing_types.

# DeviceIO

> `Live.DeviceIO.DeviceIO`

This class represents a specific input or output bus of a device. DeviceIO objects expose
the routing configuration for a device endpoint -- the routing type (e.g., which track or
external input to use) and the routing channel within that type. DeviceIO is a standalone
class, not a Device subclass.

??? note "Raw probe notes (temporary)"
    Probed with Live 12.3.5 using a Max Audio Effect device inserted on a MIDI track.

    - Bridge returns `type: "DeviceIO"` for I/O bus objects. Each DeviceIO has its own OID.
    - `routing_type` and `routing_channel` use the **same** `RoutingType` / `RoutingChannel`
      serialization as Track routing -- `_pfl_type` markers with `display_name`, `category`/`layout`,
      and `attached_object`.
    - `available_routing_types` returns a list of `RoutingType` objects. Entries include external
      sources (`"Ext. In"`, `"Ext. Out"`), other tracks (with `attached_object` pointing to the
      Track OID), and `"No Input"` / `"No Output"` (category 6).
    - `available_routing_channels` returns a list of `RoutingChannel` objects. Contents depend on
      the selected routing type.
    - All four routing properties support listeners.
    - `default_external_routing_channel_is_none` is gettable and settable. Default is `False`.
      Setting to `True` round-trips correctly.
    - **Setter caveat:** The bridge's `_decode_routing_type_for_set` /
      `_decode_routing_channel_for_set` only map Track property names (`input_routing_type` ->
      `available_input_routing_types`). DeviceIO uses bare names (`routing_type` ->
      `available_routing_types`). Bridge needs two additional entries in its property-name maps to
      support DeviceIO setters.

### Properties

| Property                                   | Type                   | Settable | Listenable | Summary                                                         |
| ------------------------------------------ | ---------------------- | -------- | ---------- | --------------------------------------------------------------- |
| `available_routing_channels`               | `list[RoutingChannel]` | no       | `yes`      | Available routing channels for this bus.                        |
| `available_routing_types`                  | `list[RoutingType]`    | no       | `yes`      | Available routing types for this bus.                           |
| `default_external_routing_channel_is_none` | `bool`                 | yes      | `no`       | Whether the default channel for External routing types is none. |
| `routing_channel`                          | `RoutingChannel`       | yes      | `yes`      | The currently selected routing channel.                         |
| `routing_type`                             | `RoutingType`          | yes      | `yes`      | The currently selected routing type.                            |

#### `available_routing_channels`

- **Type:** `list[RoutingChannel]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available routing channels for this input/output bus. Each entry uses the same
`RoutingChannel` serialization as Track routing (`display_name`, `layout`). The contents depend on
the currently selected `routing_type`. The listener fires when the available channels change.

#### `available_routing_types`

- **Type:** `list[RoutingType]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available routing types for this input/output bus. Each entry uses the same
`RoutingType` serialization as Track routing (`display_name`, `category`, `attached_object`).
Listener fires when the available types change.

#### `default_external_routing_channel_is_none`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `no`
- **Since:** `11.0`

When `True`, the default routing channel for External routing types is set to none. Default is
`False`.

#### `routing_channel`

- **Type:** `RoutingChannel` (get) · `RoutingChannel` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected routing channel for this input/output bus. Uses the same `RoutingChannel`
serialization as Track routing. Can be set to any value found in `available_routing_channels`.

#### `routing_type`

- **Type:** `RoutingType` (get) · `RoutingType` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected routing type for this input/output bus. Uses the same `RoutingType`
serialization as Track routing. Can be set to any value found in `available_routing_types`.
Changing the routing type may cause `available_routing_channels` to update.

### Open Questions

- ~~What is the actual return type of `available_routing_channels` and `available_routing_types`?~~
  **Resolved:** Same `RoutingType`/`RoutingChannel` objects as Track routing, serialized identically.
- ~~What is the return type of `routing_channel` and `routing_type`?~~
  **Resolved:** Same serialization as Track routing with `_pfl_type` markers.
- ~~What does `default_external_routing_channel_is_none` do when set?~~
  **Resolved:** Settable, round-trips correctly, default `False`.
- ~~Does setting `routing_channel` or `routing_type` to an invalid value raise `ValueError`
  immediately, or is it deferred?~~ **Partially resolved:** Setter currently fails because bridge
  doesn't map DeviceIO property names. Once bridge is updated, error behavior should match Track
  routing (immediate `ValueError` from bridge's scan-and-match logic).

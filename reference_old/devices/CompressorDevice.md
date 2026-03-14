# CompressorDevice

> `Live.CompressorDevice.CompressorDevice`

This class represents a Compressor device in Live. A CompressorDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for sidechain input routing.

The sidechain routing properties let you select the audio source feeding the compressor's
sidechain detector. The available routing options mirror those shown in Live's sidechain
section of the Compressor UI.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"CompressorDevice"`.
    - **class_name:** `"Compressor2"`.
    - **class_display_name:** `"Compressor"`.
    - **Device type:** Audio Effect.
    - Routing properties use the same `RoutingType`/`RoutingChannel` serialization as track routing
      (bridge encodes with `_pfl_type` markers, `display_name`, `category`/`layout`, `attached_object`).
    - Default `input_routing_type`: `"No Input"` (category 6, no attached object).
    - Default `input_routing_channel`: `""` (layout 2).
    - `available_input_routing_types` in a fresh 4-track set: `["3-Audio", "4-Audio", "A-Reverb",
      "B-Delay", "Main", "No Input"]` — same routing type categories as track routing.
    - Setting `input_routing_type` to a value from `available_input_routing_types` works; read-back
      matches the set value.
    - All 4 properties are listenable (confirmed via `listen`/`unlisten` round-trip).
    - In a default set, all routing types show a single channel with `display_name=""`, `layout=2`.
      Multi-channel routing (e.g., L/R sub-channels) would appear with multi-output tracks.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), CompressorDevice adds:

| Property                           | Type                   | Settable | Listenable | Summary                                                |
| ---------------------------------- | ---------------------- | -------- | ---------- | ------------------------------------------------------ |
| `available_input_routing_channels` | `list[RoutingChannel]` | no       | `yes`      | Available source channels for sidechain input routing. |
| `available_input_routing_types`    | `list[RoutingType]`    | no       | `yes`      | Available source types for sidechain input routing.    |
| `input_routing_channel`            | `RoutingChannel`       | yes      | `yes`      | Currently selected sidechain source channel.           |
| `input_routing_type`               | `RoutingType`          | yes      | `yes`      | Currently selected sidechain source type.              |

#### `available_input_routing_channels`

- **Type:** `list[RoutingChannel]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source channels for input routing in the compressor's sidechain.
Each entry is a `RoutingChannel` with `display_name` and `layout` fields. The list updates
when the available routing options change (e.g., tracks are added or removed, or the routing
type changes). The listener fires when the list contents change.

#### `available_input_routing_types`

- **Type:** `list[RoutingType]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source types for input routing in the compressor's sidechain. Each
entry is a `RoutingType` with `display_name`, `category`, and `attached_object` fields.
The list updates when available routing options change (e.g., tracks added/removed). The
listener fires when the list contents change.

#### `input_routing_channel`

- **Type:** `RoutingChannel` (get) · `RoutingChannel` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source channel for the compressor's sidechain input routing. The
value is a `RoutingChannel` object with `display_name` and `layout` fields. Can be set to
any value found in `available_input_routing_channels`. Default: `RoutingChannel("", layout=2)`.

#### `input_routing_type`

- **Type:** `RoutingType` (get) · `RoutingType` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source type for the compressor's sidechain input routing. The value
is a `RoutingType` object with `display_name`, `category`, and `attached_object` fields.
Can be set to any value found in `available_input_routing_types`. Default:
`RoutingType("No Input", category=6, attached_object=None)`.

### Methods

No additional methods beyond those inherited from Device (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`).

### Open Questions

- Does setting `input_routing_channel` or `input_routing_type` to an invalid value raise
  `ValueError` immediately, or is the error deferred? (Untested -- would require constructing
  an invalid routing object.)

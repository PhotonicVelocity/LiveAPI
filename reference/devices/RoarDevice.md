# RoarDevice

> `Live.RoarDevice.RoarDevice`

This class represents a Roar distortion device in Live. RoarDevice is a subclass of Device -- it has all the
children, properties, and methods of Device plus additional members for selecting the routing mode and
toggling envelope input listening.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"RoarDevice"`. `class_name`: `"Roar"`.
    - `routing_mode_index` returns `int`. Default is 3 ("Multi Band"). Settable, round-trips correctly.
    - `routing_mode_list` returns `list[str]` (StringVector serializes as plain list through bridge).
      Values: `["Single", "Serial", "Parallel", "Multi Band", "Mid Side", "Feedback", "Delay"]`.
      Not listenable (static list).
    - `env_listen` returns `bool`. Settable, round-trips correctly.
    - All properties except `routing_mode_list` are listenable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), RoarDevice adds:

| Property             | Type        | Settable | Listenable | Summary                               |
| -------------------- | ----------- | -------- | ---------- | ------------------------------------- |
| `env_listen`         | `bool`      | yes      | yes        | Envelope Input Listen toggle state.   |
| `routing_mode_index` | `int`       | yes      | yes        | Index of the selected routing mode.   |
| `routing_mode_list`  | `list[str]` | no       | no         | List of available routing mode names. |

#### `env_listen`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** yes
- **Since:** `12.0`

The state of the Envelope Input Listen toggle. When enabled, the envelope follower listens to the input
signal.

#### `routing_mode_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

The index into `routing_mode_list` for the currently selected routing mode. Default is 3 ("Multi Band").

#### `routing_mode_list`

- **Type:** `list[str]`
- **Listenable:** no
- **Since:** `12.0`

The list of available routing mode names for the Roar device. Static list, not listenable.
Values: `["Single", "Serial", "Parallel", "Multi Band", "Mid Side", "Feedback", "Delay"]`.

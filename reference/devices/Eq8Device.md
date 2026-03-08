# Eq8Device

> `Live.Eq8Device.Eq8Device`

This class represents an EQ Eight device in Live. An Eq8Device is a subclass of Device --
it has all the children, properties, and methods of Device plus additional members for
controlling the EQ's global mode, edit mode, and oversampling.

EQ Eight can operate in three global modes (Stereo, L/R, M/S), each of which provides two
edit channels. The `edit_mode` and `global_mode` properties expose these settings
programmatically.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"Eq8Device"`. `class_name`: `"Eq8"`.
    - `edit_mode` returns `bool` through the bridge (not `int`), despite the stub declaring it as
      `EditMode`. Setting `1` reads back as `True`, setting `0`/`False` reads back as `False`.
    - `global_mode` returns `int` (0, 1, 2). Settable and round-trips correctly.
    - `oversample` returns `bool`. Settable, round-trips correctly.
    - `view.selected_band` returns `int` (default 2 on fresh device). Settable (0-7), round-trips
      correctly.
    - All properties are listenable.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), Eq8Device adds:

| Property      | Type   | Settable | Listenable | Summary                                                         |
| ------------- | ------ | -------- | ---------- | --------------------------------------------------------------- |
| `edit_mode`   | `bool` | yes      | `yes`      | Which channel is selected for editing (depends on global mode). |
| `global_mode` | `int`  | yes      | `yes`      | The EQ's stereo processing mode (Stereo, L/R, or M/S).         |
| `oversample`  | `bool` | yes      | `yes`      | Whether oversampling is enabled.                                |

#### `edit_mode`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Controls which channel is currently available for editing. The meaning of the value depends
on the current `global_mode`:

- In L/R mode: `False` = Left, `True` = Right
- In M/S mode: `False` = Mid, `True` = Side
- In Stereo mode: `False` = channel A, `True` = channel B (inactive)

- **Quirks:**
    - Despite the stub declaring this as `EditMode`, the bridge serializes it as `bool`.

#### `global_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The EQ's stereo processing mode. The modes are encoded as:

- `0` = Stereo
- `1` = L/R
- `2` = M/S

Changing the global mode affects the available edit modes (see `edit_mode`).

#### `oversample`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether oversampling is enabled for the EQ. When on, the EQ processes at a higher internal
sample rate for improved accuracy at the cost of increased CPU usage.

### Methods

No additional methods beyond those inherited from Device (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`).

---

## Eq8Device.View

Represents the view aspects of an EQ Eight device. Extends Device.View with an additional
property for the selected filter band.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property        | Type  | Settable | Listenable | Summary                                          |
| --------------- | ----- | -------- | ---------- | ------------------------------------------------ |
| `selected_band` | `int` | yes      | `yes`      | The index of the currently selected filter band. |

#### `selected_band`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The index of the currently selected filter band in the EQ Eight UI. EQ Eight has 8 bands
(indices 0-7). The listener fires when the user selects a different band in the device UI.
Default value on a fresh device is 2.

### Open Questions

None -- all resolved by probing.

# RackDevice

## RackDevice

This class represents a rack device in Live (Instrument Rack, Audio Effect Rack, MIDI Effect
Rack, or Drum Rack). A RackDevice is a subclass of Device — it has all the children,
properties, and methods of Device plus additional members for managing chains, macros,
drum pads, and macro variations.

A rack contains one or more chains, each with its own device list and mixer. It may also
contain return chains. Drum Racks additionally expose drum pads.

### Sources

- **Primary:** `Live/classes/devices/RackDevice.py` (stub dump)
- **Secondary:** `MaxForLive/rackdevice.md`
- **Probes:** `probe_rack_macros.py`, `probe_rack_macros2.py`

### Probe Notes

Probed against Live 12.3.5 with self-inserted Instrument Rack and Drum Rack.

**Parameter layout (fixed-size):**

- `[0]` = Device On (toggle, quantized)
- `[1]`–`[16]` = Macro 1–16 (continuous, 0.0–127.0). Always 16, regardless of `visible_macro_count`.
- `[17]` = Chain Selector (Instrument/Audio/MIDI Effect Racks only; Drum Racks have 17 params total, no
  Chain Selector in the parameter list).
- `add_macro()` / `remove_macro()` only change `visible_macro_count`, never the parameter list.

**Macro count limits:**

- Default: 8 visible macros.
- Maximum: 16 (`add_macro()` throws `"The maximum number of macro controls is already reached!"`).
- Minimum: 1 (`remove_macro()` throws `"The minimum number of macro controls is already reached!"`).
- Increment pattern: 1→2 (delta=1), then 2→4→6→8→10→12→14→16 (delta=2 each).

**macros_mapped:** Always returns a list of 16 booleans (all macros, not just visible ones).

**selected_variation_index:** Returns `-1` when no variations exist. `delete_selected_variation()` is a no-op
when `selected_variation_index = -1`.

**has_drum_pads:** Throws `"Only drum racks can have pads!"` on non-Drum Racks where `can_have_drum_pads=False`.

**chain_selector:** Accessible via both `get` (returns handle dict `{oid, type: "DeviceParameter"}`) and
`children` (returns `kind: 'object'` with single item). Also present as parameter [17] in the parameter list
(Instrument Rack only).

**View:** Returned as `kind: 'object'` with type `"View"` (not a Rack-specific type name). `selected_chain`
returns `None` when the rack has no chains. `selected_drum_pad` works on Drum Racks via both `get` and `children`.

**insert_chain:** Works on all rack types:

- Instrument Rack: returns `{oid, type: "Chain"}`.
- Drum Rack: returns `{oid, type: "DrumChain"}`.

**DrumPad:** Type name is `"DrumPad"`. Empty pads show musical note names as their `name` (e.g. `"C-2"`,
`"C♯-2"`, `"D-2"`). `note` = 0–127 (MIDI note number). `mute` and `solo` default to `False`.
128 drum pads total, 16 visible at a time. Default `drum_pads_scroll_position` = 9.

### Open Questions

- ~~What is the maximum number of macros (`add_macro()` limit)?~~ **Answered: 16.**
- ~~What is the minimum number of macros (`remove_macro()` limit)?~~ **Answered: 1.**
- ~~Does `macros_mapped` include hidden macros, or only visible ones?~~ **Answered: all 16 macros (hidden included).**
- ~~What does `selected_variation_index` return when no variations exist?~~ **Answered: `-1`.**
- ~~Can `insert_chain()` be called on non-Drum Racks, or only on Drum Racks?~~ **Answered: works on all rack
  types. Returns `Chain` for non-Drum, `DrumChain` for Drum Rack.**

### Children

| Child               | Returns             | Shape    | Access | Listenable | Available Since | Summary                                                    |
| ------------------- | ------------------- | -------- | ------ | ---------- | --------------- | ---------------------------------------------------------- |
| `chain_selector`    | `DeviceParameter`   | `single` | `get`  | `no`       | `11.2`          | The chain selector parameter for zone-based chain routing. |
| `chains`            | `Sequence[Chain]`   | `list`   | `get`  | `yes`      | `<11`           | The rack's chains.                                         |
| `drum_pads`         | `Sequence[DrumPad]` | `list`   | `get`  | `yes`      | `<11`           | All 128 drum pads. Drum Racks only.                        |
| `return_chains`     | `Sequence[Chain]`   | `list`   | `get`  | `yes`      | `<11`           | The rack's return chains.                                  |
| `visible_drum_pads` | `Sequence[DrumPad]` | `list`   | `get`  | `yes`      | `<11`           | The 16 currently visible drum pads. Drum Racks only.       |

#### `chain_selector`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Available Since:** `11.2`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Convenience accessor for the rack's chain selector parameter. The chain selector controls
which chain(s) are active based on the chain zone mapping. This is a `DeviceParameter`
object, so it can be automated and mapped. Probed: accessible via both `get` (returns handle
dict) and `children` (`kind: 'object'`). Also present as parameter [17] in the parameter list
(Instrument Rack only; Drum Racks have no Chain Selector parameter).

#### `chains`

- **Returns:** `Sequence[Chain]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The ordered list of chains in this rack. Throws an exception if `can_have_chains` is
`False` (which should never happen for a RackDevice). The listener fires when chains are
added, removed, or reordered. Probed: empty Instrument Rack returns 0 chains.

#### `drum_pads`

- **Returns:** `Sequence[DrumPad]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
All 128 drum pads for the topmost Drum Rack. Inner (nested) Drum Racks return an empty
list. Throws an exception if `can_have_drum_pads` is `False`. The listener fires when
pad assignments change. Probed: returns 128 `DrumPad` items.

#### `return_chains`

- **Returns:** `Sequence[Chain]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The list of return chains in this rack. Return chains receive audio from send amounts on
the main chains. Throws an exception if `can_have_chains` is `False`. Probed: empty
Instrument Rack returns 0 return chains.

#### `visible_drum_pads`

- **Returns:** `Sequence[DrumPad]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The 16 drum pads currently visible in the Drum Rack pad grid. Only applies to the topmost
Drum Rack — inner Drum Racks return an empty list. Throws an exception if
`can_have_drum_pads` is `False`. The visible range is controlled by
`view.drum_pads_scroll_position`. Probed: returns 16 `DrumPad` items.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), RackDevice adds:

| Property                   | Get Returns      | Set Accepts | Listenable | Available Since | Summary                                                        |
| -------------------------- | ---------------- | ----------- | ---------- | --------------- | -------------------------------------------------------------- |
| `can_show_chains`          | `bool`           | —           | `no`       | `<11`           | `True` if the rack instrument can show chains in Session View. |
| `has_drum_pads`            | `bool`           | —           | `yes`      | `<11`           | `True` for top-level Drum Racks with pads.                     |
| `has_macro_mappings`       | `bool`           | —           | `yes`      | `<11`           | `True` if any macro is mapped to a parameter.                  |
| `is_showing_chains`        | `bool`           | —           | `yes`      | `<11`           | `True` if chains are shown in Session View.                    |
| `macros_mapped`            | `Sequence[bool]` | —           | `yes`      | `<11`           | Per-macro boolean list: `True` if that macro is mapped.        |
| `selected_variation_index` | `int`            | `int`       | `no`       | `11.0`          | Index of the currently selected macro variation.               |
| `variation_count`          | `int`            | —           | `yes`      | `11.0`          | Number of stored macro variations.                             |
| `visible_macro_count`      | `int`            | —           | `yes`      | `11.2`          | Number of currently visible macros.                            |

#### `can_show_chains`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` if this rack contains an instrument device that is capable of showing its chains in
Session View (e.g., an Instrument Rack where chains can appear as rows in the Session View
grid for individual clip launching). Probed: `False` for both empty Instrument Rack and
Drum Rack.

#### `has_drum_pads`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` if the device is a Drum Rack that has pads. A nested (inner) Drum Rack returns
`False` because only the topmost Drum Rack owns the pad grid. **Throws** if
`can_have_drum_pads` is `False` — probed: accessing on an Instrument Rack throws
`"Only drum racks can have pads!"`. Guard with `can_have_drum_pads` check first.

#### `has_macro_mappings`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` if any of the rack's macro knobs are mapped to a parameter inside the rack.
Probed: `False` for a fresh rack with no mappings.

#### `is_showing_chains`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` if the rack is currently showing its chains in Session View. Only meaningful when
`can_show_chains` is `True`. Probed: `False` for an empty Instrument Rack.

#### `macros_mapped`

- **Get Returns:** `Sequence[bool]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
A list of booleans, one per macro parameter, where `True` indicates that the corresponding
macro is mapped to a device parameter inside the rack. Probed: **always returns 16 booleans**
(all macros, not just visible ones). Length is fixed at 16 regardless of `visible_macro_count`.

#### `selected_variation_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `no`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The index of the currently selected macro variation. Setting an out-of-range index throws
an exception. Probed: returns **`-1`** when no variations exist.

#### `variation_count`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The number of macro variations currently stored for this rack. Use `store_variation()` to
add variations and `delete_selected_variation()` to remove them. Probed: `0` for a fresh
rack. `store_variation()` increments to 1.

#### `visible_macro_count`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.2`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The number of macro knobs currently visible in the rack UI. Use `add_macro()` and
`remove_macro()` to change this count. Probed: default = **8**. Range: **1–16**.
`add_macro()` increments: 1→2 (+1), then +2 each step (2→4→6→…→16).

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
RackDevice adds:

| Signature                                      | Returns | Available Since | Summary                                          |
| ---------------------------------------------- | ------- | --------------- | ------------------------------------------------ |
| `add_macro()`                                  | `None`  | `11.0`          | Increase visible macro count by one.             |
| `copy_pad(source_index: int, dest_index: int)` | `None`  | `<11`           | Copy all contents from one drum pad to another.  |
| `delete_selected_variation()`                  | `None`  | `11.0`          | Delete the currently selected macro variation.   |
| `insert_chain(index: int = -1)`                | `Chain` | `12.3`          | Insert a new empty chain at the given index.     |
| `randomize_macros()`                           | `None`  | `11.0`          | Randomize all eligible macro values.             |
| `recall_last_used_variation()`                 | `None`  | `11.0`          | Recall the most recently used macro variation.   |
| `recall_selected_variation()`                  | `None`  | `11.0`          | Recall the currently selected macro variation.   |
| `remove_macro()`                               | `None`  | `11.0`          | Decrease visible macro count by one.             |
| `store_variation()`                            | `None`  | `11.0`          | Store a new macro variation from current values. |

#### `add_macro()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** Throws `"The maximum number of macro controls is already reached!"` at 16.
- **Undo-tracked:** `Unknown`
- **Side Effects:** Increases the visible macro count. Does **not** change the parameter list.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Increases the number of visible macro controls in the rack. Probed: increment is +1 from 1→2,
then +2 for all subsequent steps (2→4→6→8→10→12→14→16). Maximum is **16**.

#### `copy_pad(source_index: int, dest_index: int)`

- **Returns:** `None`
- **Args:**
  - `source_index: int` — note number (0–127) of the source pad
  - `dest_index: int` — note number (0–127) of the destination pad
- **Raises/Errors:** Throws if the source pad is empty, or if either index is outside 0–127.
- **Undo-tracked:** `Unknown`
- **Side Effects:** Copies all contents (devices, chains) from source pad to destination pad.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed` (not probed — requires pad with content)

**Description:**
Copies all contents of a Drum Rack pad from a source pad into a destination pad. The indices
correspond to MIDI note numbers (0–127). Only applicable to Drum Racks.

#### `delete_selected_variation()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None (does nothing if no variation is selected).
- **Undo-tracked:** `Unknown`
- **Side Effects:** Deletes the currently selected macro variation.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Deletes the currently selected macro variation. Probed: no-op when `selected_variation_index`
is `-1` (no variations or none selected). `variation_count` stays unchanged in that case.

#### `insert_chain(index: int = -1)`

- **Returns:** `Chain` (the newly inserted chain)
- **Args:**
  - `index: int = -1` — position in the chain list; `-1` means end
- **Raises/Errors:** Throws if insertion is not possible.
- **Undo-tracked:** `Unknown`
- **Side Effects:** Inserts a new empty chain into the rack.
- **Async visibility:** `Unknown`
- **Available Since:** `12.3`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Inserts a new chain at the specified index in the rack's chain list, or at the end if no
index is provided. Probed: works on all rack types. Returns `{oid, type: "Chain"}` for
Instrument Racks and `{oid, type: "DrumChain"}` for Drum Racks. For Drum Racks, the newly
inserted chain will have an initial MIDI In Note setting of "All Notes" — you likely want to
set `DrumChain.in_note` to the note value that corresponds to the target pad.

#### `randomize_macros()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Randomizes the values of all macro controls not excluded from randomization.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed` (not probed — need to verify exclusion behavior)

**Description:**
Randomizes the values for all macro controls that are eligible for randomization. Macros
excluded from randomization (via the rack UI) are not affected.

#### `recall_last_used_variation()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None (does nothing if no variation has been recalled yet).
- **Undo-tracked:** `Unknown`
- **Side Effects:** Recalls the macro variation that was most recently recalled.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed` (not probed — need to verify recall behavior)

**Description:**
Recalls the macro variation that was recalled most recently. Does nothing if no variation
has been recalled yet during this session.

#### `recall_selected_variation()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None (does nothing if no variations exist).
- **Undo-tracked:** `Unknown`
- **Side Effects:** Recalls the currently selected macro variation, setting all mapped macros to the stored values.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed` (not probed — need to verify recall behavior)

**Description:**
Recalls the currently selected macro variation, setting all mapped macro parameters to
their stored values. Does nothing if there are no variations.

#### `remove_macro()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** Throws `"The minimum number of macro controls is already reached!"` at 1.
- **Undo-tracked:** `Unknown`
- **Side Effects:** Decreases the visible macro count. Does **not** change the parameter list.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Decreases the number of visible macro controls in the rack. Probed: decrement is -2 for most
steps (16→14→12→…→2), then -1 from 2→1. Minimum is **1**.

#### `store_variation()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Stores the current values of all mapped macros as a new variation.
- **Async visibility:** `Unknown`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Stores a new variation of the current values of all mapped macro parameters. The new
variation is appended to the variation list and `variation_count` increases by one.
Probed: `variation_count` goes from 0→1 after first call. `selected_variation_index`
stays at `-1` after store (does not auto-select).

---

## RackDevice.View

Represents the view aspects of a rack device. Extends Device.View with rack-specific view
properties.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property                    | Get Returns | Set Accepts | Listenable | Available Since | Summary                                           |
| --------------------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------------------------- |
| `drum_pads_scroll_position` | `int`       | `int`       | `yes`      | `<11`           | Index of the lowest visible row of drum pads.     |
| `is_showing_chain_devices`  | `bool`      | —           | `yes`      | `<11`           | Whether the selected chain's devices are visible. |
| `selected_chain`            | `Chain`     | —           | `yes`      | `<11`           | The currently selected chain in the rack.         |
| `selected_drum_pad`         | `DrumPad`   | —           | `yes`      | `<11`           | The currently selected drum pad. Drum Racks only. |

#### `drum_pads_scroll_position`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The index of the lowest visible row of drum pads in the Drum Rack pad grid. Controls which
16 pads are shown in `visible_drum_pads`. Throws an exception if `can_have_drum_pads` is
`False`. Probed: default value is **9** on a fresh Drum Rack.

#### `is_showing_chain_devices`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` when the devices in the currently selected chain are visible in the rack's expanded
view. Throws an exception if `can_have_chains` is `False`. Probed: `True` for both empty
Instrument Rack and Drum Rack (default state).

#### `selected_chain`

- **Get Returns:** `Chain`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The currently selected chain in the rack. The listener fires when the selection changes
(e.g., the user clicks a different chain in the rack UI). Probed: returns `None` when the
rack has no chains. Accessible via both `get` and `children` (`kind: 'none'` when null).

#### `selected_drum_pad`

- **Get Returns:** `DrumPad`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The currently selected drum pad in the Drum Rack. Throws an exception if
`can_have_drum_pads` is `False`. Probed: returns a `DrumPad` object. Accessible via both
`get` (returns handle dict) and `children` (`kind: 'object'` with single item).

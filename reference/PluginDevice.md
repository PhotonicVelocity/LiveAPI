# PluginDevice

## PluginDevice

This class represents a third-party plug-in device (VST or Audio Unit) in Live. A
PluginDevice is a subclass of Device -- it has all the children, properties, and methods
of Device plus additional members for accessing plug-in presets and parameter names.

Plug-in devices wrap external instrument or effect plug-ins. Their parameters are
exposed through the standard `parameters` list (inherited from Device), but PluginDevice
adds methods to query plug-in-specific parameter names and a preset system that is
separate from Live's native preset browser.

### Sources

- **Primary:** `Live/classes/devices/PluginDevice.py` (stub dump)
- **Secondary:** `MaxForLive/plugindevice.md`
- **Probes:** `.tmp/probe_plugin_device.py`

### Probe Notes

- Bridge type name: `"PluginDevice"` (generic for all VST/AU plug-ins).
- `class_name` = `"PluginDevice"` (same for all VST2/VST3 plug-ins — not plug-in-specific).
- **AU uses a distinct class name:** `class_name='AuPluginDevice'`. VST2 and VST3 both use `'PluginDevice'`
  (no distinction between VST versions). Both resolve to the same `PluginDevice` Python class.
- `class_display_name` = the plug-in's own name (e.g. `"Raum"`).
- Device type = 2 (Audio Effect) for effect plug-ins; would be 1 (Instrument) for instrument plug-ins.
- **Cannot be inserted via `insert_device`** — only native devices are accepted. Plug-ins must be loaded via
  `browser_load` (targeting the `plugins` browser root).
- **`move_device` works** — a loaded plug-in device can be moved into an Audio Effect Rack chain via
  `Song.move_device()`. Confirmed with TDR Nova into a rack chain.
- **Dual preset model** — two completely separate preset systems coexist:
  - **Runtime presets** (`PluginDevice.presets`): reported by the plug-in to Live via the VST/AU protocol.
    Probed all installed plug-ins (12+ across VST2, VST3, AUv2, third-party, and Apple built-ins): **every one
    returns `['Default']` only**. Plug-in-internal preset browsers (e.g. Vital's patch browser) are not accessible
    through Live's API.
  - **Browser presets** (user-saved): `.aupreset` and `.vstpreset` files that appear as children of the plug-in's
    browser item under the `plugins` root (`source='User Library'`). These are format-bound — `.aupreset` only
    appears under the AUv2 entry, `.vstpreset` only under VST3. User-saved browser presets do **not** appear in
    the runtime `presets` list.
- **Hotswap cross-format behavior** (via `browser.hotswap_target` + `browser_load`):
  - Same-format preset (e.g. VST3 `.vstpreset` → VST3 device): preset applied in-place, **same OID**.
  - Cross-format preset (e.g. AU `.aupreset` → VST3 device): replaced in-place with AU version
    (`AuPluginDevice`), **new OID**, device count unchanged.
  - Cross-device swap (e.g. Raum VST3 → Ozone AU): completely different plug-in swapped in-place, **new OID**.
  - Raw `browser_load` without hotswap always appends a new device (not useful for preset application).
- `presets` serializes as plain `list[str]` through the bridge (StringVector → list).
- `selected_preset_index` is **settable** — confirmed by probe.
- `get_parameter_names(begin, end)` returns `list[str]`. `end` is **exclusive** (Python slicing semantics):
  `get_parameter_names(0, 3)` returns 3 names (indices 0, 1, 2). `get_parameter_names(0, -1)` returns all.
- Some parameter names may be `"-"` (unnamed/placeholder parameters).

### Open Questions

- Does changing `selected_preset_index` actually load the preset in the plug-in? (Likely yes, but not
  confirmed with a multi-preset plug-in.)
- What happens when setting `selected_preset_index` to an out-of-range value? (Not tested — only 1 preset
  available.)

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), PluginDevice adds:

| Property                | Get Returns    | Set Accepts | Listenable | Available Since | Summary                                          |
| ----------------------- | -------------- | ----------- | ---------- | --------------- | ------------------------------------------------ |
| `presets`               | `StringVector` | —           | `yes`      | `<11`           | The list of preset names exposed by the plug-in. |
| `selected_preset_index` | `int`          | `int`       | `yes`      | `<11`           | Index of the currently selected plug-in preset.  |

#### `presets`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of preset names offered by the plug-in. These are the presets reported by the
plug-in itself (not Live's preset browser). The listener fires when the plug-in updates
its preset list (e.g., after scanning or user action inside the plug-in).
Probed value: `['Default']` (for NI Raum with a single preset).

#### `selected_preset_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index of the currently selected preset in the plug-in's preset list. Setting this
value selects a different preset. The listener fires when the preset selection changes,
whether from the API or from user interaction inside the plug-in. Settable — confirmed by probe.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
PluginDevice adds:

| Signature                                   | Returns        | Available Since | Summary                                 |
| ------------------------------------------- | -------------- | --------------- | --------------------------------------- |
| `get_parameter_names(begin: int, end: int)` | `StringVector` | `<11`           | Get a range of plug-in parameter names. |

#### `get_parameter_names(begin: int, end: int)`

- **Returns:** `StringVector` (serializes as `list[str]`)
- **Args:**
  - `begin: int` -- starting index of the parameter range (default `0`)
  - `end: int` -- ending index of the parameter range (exclusive); if less than `0`, returns all
    parameters from `begin` to the end (default `-1`)
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** N/A (read-only operation)
- **Side Effects:** None
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | probe`
- **Probe Status:** `probed`

**Description:**
Returns a list of plug-in parameter names for the given index range. The `end` parameter
is exclusive (Python slicing semantics): `get_parameter_names(0, 3)` returns names at
indices 0, 1, 2. Passing `end=-1` returns all parameters from `begin` onward.
Some parameter names may be `"-"` (unnamed/placeholder slots).
Probed: `get_parameter_names(0, -1)` returned 19 names for NI Raum;
`get_parameter_names(0, 3)` returned 3 names; `get_parameter_names(5, 8)` returned 3 names.

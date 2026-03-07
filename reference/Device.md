# Device

## Device

This class represents a MIDI or audio DSP device in Live. A device lives in a track's
device chain (or inside a rack chain). All native Live instruments, audio effects, MIDI
effects, Max for Live devices, and third-party plug-ins are represented as Device objects.
Rack devices (`can_have_chains=True`) contain chains which themselves contain devices.

### Sources

- **Primary:** `Live/classes/Device.py` (stub dump)
- **Secondary:** `MaxForLive/device.md`, `MaxForLive/device_view.md`
- **Probes:** `probe_all_devices.py`, `probe_device_name.py`

### Probe Notes

- **`name` IS settable** — `set name='Probe_Test'` succeeded with correct readback. Confirmed
  writable via the API. Restore also works.
- **`type` values confirmed** — Drift returns `1` (instrument), Audio Effect Rack returns `2`
  (audio_effect).
- **`class_name` examples** — Drift: `'Drift'`, Audio Effect Rack: `'AudioEffectGroupDevice'`.
- **`can_compare_ab`** — Drift: `True`, Audio Effect Rack: `False`.

### Open Questions

- What does `type` return for Max for Live devices vs third-party plug-ins?
- Does `is_active` reflect the device's own on/off state, the enclosing rack's state, or both? The stub says
  "false both when the device is off and when it's inside a rack device which is off" — but does toggling the
  device's own activator from off to on fire the `is_active` listener even when the enclosing rack is off?
- What happens when calling `save_preset_to_compare_ab_slot()` on a device where `can_compare_ab` is `False`?

### Children

| Child        | Returns                     | Shape    | Access | Listenable | Available Since | Summary                                        |
| ------------ | --------------------------- | -------- | ------ | ---------- | --------------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | `get`  | `yes`      | `<11`           | Automatable parameters exposed by this device. |
| `view`       | `Device.View`               | `single` | `get`  | `no`       | `<11`           | View aspects of the device (collapse state).   |

#### `parameters`

- **Returns:** `Sequence[DeviceParameter]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The list of automatable parameters for this device. Only automatable parameters are accessible —
not all internal device state is exposed. The listener fires when the parameter list changes
(e.g., when a rack macro configuration changes). Index 0 is conventionally the device's on/off
toggle parameter.

#### `view`

- **Returns:** `Device.View`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
View aspects of the device. Currently exposes only `is_collapsed`.

### Properties

| Property                    | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                                     |
| --------------------------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`      | —           | `no`       | `12.3`          | Whether the device supports AB comparison.                                  |
| `can_have_chains`           | `bool`      | —           | `no`       | `<11`           | `True` for rack devices.                                                    |
| `can_have_drum_pads`        | `bool`      | —           | `no`       | `<11`           | `True` for Drum Racks.                                                      |
| `class_display_name`        | `str`       | —           | `no`       | `<11`           | Original device name as shown in browser (e.g. `"Operator"`).               |
| `class_name`                | `str`       | —           | `no`       | `<11`           | Internal class name (e.g. `"Operator"`, `"PluginDevice"`).                  |
| `is_active`                 | `bool`      | —           | `yes`      | `<11`           | `False` when device is off or enclosing rack is off.                        |
| `is_using_compare_preset_b` | `bool`      | —           | `yes`      | `12.3`          | Whether preset B is loaded. Only valid if `can_compare_ab`.                 |
| `latency_in_ms`             | `float`     | —           | `yes`      | `11.2`          | Device latency in milliseconds.                                             |
| `latency_in_samples`        | `int`       | —           | `yes`      | `11.2`          | Device latency in samples.                                                  |
| `name`                      | `str`       | `str`       | `yes`      | `<11`           | Device name as shown in title bar. Settable.                                |
| `type`                      | `int`       | —           | `no`       | `<11`           | Device type enum: 0=undefined, 1=instrument, 2=audio_effect, 4=midi_effect. |

#### `can_compare_ab`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.3`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — Drift→`True`, Audio Effect Rack→`False`

**Description:**
`True` if the device supports the AB Compare feature. `False` for rack devices and devices
that don't have this capability (third-party plug-ins, Max for Live devices). Accessing
`is_using_compare_preset_b` or calling `save_preset_to_compare_ab_slot()` on a device where
this is `False` raises an error.

#### `can_have_chains`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for rack devices (Instrument Rack, Audio Effect Rack, MIDI Effect Rack, Drum Rack).
`False` for single devices (Operator, Compressor, plug-ins, etc.). When `True`, the device
has `chains` and/or `return_chains` children (accessible on the RackDevice subclass).

#### `can_have_drum_pads`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` only for Drum Racks. Drum Racks have `drum_pads` children in addition to chains.

#### `class_display_name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The original display name of the device class as shown in Live's browser and device header
(e.g. `"Operator"`, `"Auto Filter"`, `"Compressor"`). Does not change when the user renames
the device — use `name` for the user-visible name.

#### `class_name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — Drift→`'Drift'`, Audio Effect Rack→`'AudioEffectGroupDevice'`

**Description:**
The internal Live class name for this device type. Examples: `"Drift"`, `"Operator"`,
`"Limiter"`, `"AudioEffectGroupDevice"` (Audio Effect Rack), `"MxDeviceAudioEffect"` (Max for
Live audio effect), `"PluginDevice"` (third-party VST/AU plug-in). Useful for programmatically
identifying device types.

#### `is_active`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`False` when the device is turned off (device activator) **or** when it's inside a rack
device that is turned off. This means a device can have `is_active=False` even if its own
activator is on — because the parent rack is off. The Max docs note: "0 = either the device
itself or its enclosing Rack device is off."

#### `is_using_compare_preset_b`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `12.3`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` if the device has loaded the preset from compare slot B. Only relevant when
`can_compare_ab` is `True` — accessing this property on a device that doesn't support
AB comparison raises an error.

#### `latency_in_ms`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.2`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The latency introduced by this device in milliseconds. Changes when the device's latency
compensation changes (e.g., oversampling, look-ahead settings).

#### `latency_in_samples`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.2`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The latency introduced by this device in samples. Sample-accurate companion to
`latency_in_ms`.

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — set/readback works

**Description:**
The name of the device as shown in the device title bar. For unmodified devices, this
matches `class_display_name`. Users can rename devices in the Live UI, and this property
can also be set programmatically to rename a device.

#### `type`

- **Get Returns:** `int` (`Device.DeviceType`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — Drift→`1` (instrument), Audio Effect Rack→`2` (audio_effect)

**Description:**
The type of the device as a `DeviceType` enum value:

- `0` = undefined
- `1` = instrument
- `2` = audio_effect
- `4` = midi_effect

Note the gap: there is no value `3`. The Max docs confirm these values.

### Methods

| Signature                                     | Returns | Available Since | Summary                                                 |
| --------------------------------------------- | ------- | --------------- | ------------------------------------------------------- |
| `save_preset_to_compare_ab_slot()`            | `None`  | `12.3`          | Save current state to the AB compare slot.              |
| `store_chosen_bank(script_index, bank_index)` | `None`  | `<11`           | Set selected bank for hardware control surface mapping. |

#### `save_preset_to_compare_ab_slot()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** Error if `can_compare_ab` is `False`.
- **Undo-tracked:** `Unknown`
- **Side Effects:** Saves the current device state to the other AB compare slot.
- **Async visibility:** `Unknown`
- **Available Since:** `12.3`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Saves the device's current parameter state to the AB compare slot. After calling this, the
user can switch between preset A and preset B using the AB Compare button. Only works on
devices where `can_compare_ab` is `True`.

#### `store_chosen_bank(script_index, bank_index)`

- **Returns:** `None`
- **Args:**
  - `script_index: int`
  - `bank_index: int`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Persists the selected bank for a hardware control surface.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Sets the selected bank in the device for persistency with a hardware control surface. The
Max docs note this is "usually not relevant" for general use. `script_index` identifies the
control surface script and `bank_index` identifies the bank within that script's mapping.

---

## Device.View

Represents the view aspects of a device.

### Properties

| Property       | Get Returns | Set Accepts | Listenable | Available Since | Summary                                             |
| -------------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------- |
| `is_collapsed` | `bool`      | `bool`      | `yes`      | `<11`           | Whether the device is shown collapsed in the chain. |

#### `is_collapsed`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls whether the device is shown collapsed (minimized) in the device chain. `True` means
the device is collapsed to a narrow strip showing only its title bar; `False` means the full
device UI is visible.

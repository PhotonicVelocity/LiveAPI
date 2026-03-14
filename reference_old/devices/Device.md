# Device

> `Live.Device.Device`

This class represents a MIDI or audio DSP device in Live. A device lives in a track's
device chain (or inside a rack chain). All native Live instruments, audio effects, MIDI
effects, Max for Live devices, and third-party plug-ins are represented as Device objects.
Rack devices (`can_have_chains=True`) contain chains which themselves contain devices.

??? note "Raw probe notes (temporary)"
    - **`name` IS settable** -- `set name='Probe_Test'` succeeded with correct readback. Confirmed
      writable via the API. Restore also works.
    - **`type` values confirmed** -- Drift returns `1` (instrument), Audio Effect Rack returns `2`
      (audio_effect).
    - **`class_name` examples** -- Drift: `'Drift'`, Audio Effect Rack: `'AudioEffectGroupDevice'`.
    - **`can_compare_ab`** -- Drift: `True`, Audio Effect Rack: `False`.

### Open Questions

- What does `type` return for Max for Live devices vs third-party plug-ins?
- Does `is_active` reflect the device's own on/off state, the enclosing rack's state, or both? The stub
  says "false both when the device is off and when it's inside a rack device which is off" -- but does
  toggling the device's own activator from off to on fire the `is_active` listener even when the
  enclosing rack is off?
- What happens when calling `save_preset_to_compare_ab_slot()` on a device where `can_compare_ab`
  is `False`?

### Children

| Child        | Returns                     | Shape    | Listenable | Summary                                        |
| ------------ | --------------------------- | -------- | ---------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | `yes`      | Automatable parameters exposed by this device. |
| `view`       | `Device.View`               | `single` | `no`       | View aspects of the device (collapse state).   |

#### `parameters`

- **Type:** `Sequence[DeviceParameter]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of automatable parameters for this device. Only automatable parameters are accessible --
not all internal device state is exposed. The listener fires when the parameter list changes
(e.g., when a rack macro configuration changes). Index 0 is conventionally the device's on/off
toggle parameter.

#### `view`

- **Type:** `Device.View`
- **Listenable:** `no`
- **Since:** `<11`

View aspects of the device. Currently exposes only `is_collapsed`.

### Properties

| Property                    | Type    | Settable | Listenable | Summary                                                                     |
| --------------------------- | ------- | -------- | ---------- | --------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`  | no       | `no`       | Whether the device supports AB comparison.                                  |
| `can_have_chains`           | `bool`  | no       | `no`       | `True` for rack devices.                                                    |
| `can_have_drum_pads`        | `bool`  | no       | `no`       | `True` for Drum Racks.                                                      |
| `class_display_name`        | `str`   | no       | `no`       | Original device name as shown in browser (e.g. `"Operator"`).               |
| `class_name`                | `str`   | no       | `no`       | Internal class name (e.g. `"Operator"`, `"PluginDevice"`).                  |
| `is_active`                 | `bool`  | no       | `yes`      | `False` when device is off or enclosing rack is off.                        |
| `is_using_compare_preset_b` | `bool`  | no       | `yes`      | Whether preset B is loaded. Only valid if `can_compare_ab`.                 |
| `latency_in_ms`             | `float` | no       | `yes`      | Device latency in milliseconds.                                             |
| `latency_in_samples`        | `int`   | no       | `yes`      | Device latency in samples.                                                  |
| `name`                      | `str`   | `str`    | `yes`      | Device name as shown in title bar. Settable.                                |
| `type`                      | `int`   | no       | `no`       | Device type enum: 0=undefined, 1=instrument, 2=audio_effect, 4=midi_effect. |

#### `can_compare_ab`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.3`

`True` if the device supports the AB Compare feature. `False` for rack devices and devices
that don't have this capability (third-party plug-ins, Max for Live devices). Accessing
`is_using_compare_preset_b` or calling `save_preset_to_compare_ab_slot()` on a device where
this is `False` raises an error.

#### `can_have_chains`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for rack devices (Instrument Rack, Audio Effect Rack, MIDI Effect Rack, Drum Rack).
`False` for single devices (Operator, Compressor, plug-ins, etc.). When `True`, the device
has `chains` and/or `return_chains` children (accessible on the RackDevice subclass).

#### `can_have_drum_pads`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` only for Drum Racks. Drum Racks have `drum_pads` children in addition to chains.

#### `class_display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The original display name of the device class as shown in Live's browser and device header
(e.g. `"Operator"`, `"Auto Filter"`, `"Compressor"`). Does not change when the user renames
the device -- use `name` for the user-visible name.

#### `class_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The internal Live class name for this device type. Examples: `"Drift"`, `"Operator"`,
`"Limiter"`, `"AudioEffectGroupDevice"` (Audio Effect Rack), `"MxDeviceAudioEffect"` (Max for
Live audio effect), `"PluginDevice"` (third-party VST/AU plug-in). Useful for programmatically
identifying device types.

#### `is_active`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`False` when the device is turned off (device activator) **or** when it's inside a rack
device that is turned off. This means a device can have `is_active=False` even if its own
activator is on -- because the parent rack is off. The Max docs note: "0 = either the device
itself or its enclosing Rack device is off."

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `12.3`

`True` if the device has loaded the preset from compare slot B. Only relevant when
`can_compare_ab` is `True` -- accessing this property on a device that doesn't support
AB comparison raises an error.

#### `latency_in_ms`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.2`

The latency introduced by this device in milliseconds. Changes when the device's latency
compensation changes (e.g., oversampling, look-ahead settings).

#### `latency_in_samples`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.2`

The latency introduced by this device in samples. Sample-accurate companion to
`latency_in_ms`.

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The name of the device as shown in the device title bar. For unmodified devices, this
matches `class_display_name`. Users can rename devices in the Live UI, and this property
can also be set programmatically to rename a device.

#### `type`

- **Type:** `int` (`Device.DeviceType`)
- **Listenable:** `no`
- **Since:** `<11`

The type of the device as a `DeviceType` enum value:

- `0` = undefined
- `1` = instrument
- `2` = audio_effect
- `4` = midi_effect

Note the gap: there is no value `3`. The Max docs confirm these values.

### Methods

| Method                                        | Returns | Summary                                                 |
| --------------------------------------------- | ------- | ------------------------------------------------------- |
| `save_preset_to_compare_ab_slot()`            | `None`  | Save current state to the AB compare slot.              |
| `store_chosen_bank(script_index, bank_index)` | `None`  | Set selected bank for hardware control surface mapping. |

#### `save_preset_to_compare_ab_slot()`

- **Returns:** `None`
- **Raises:** Error if `can_compare_ab` is `False`.
- **Since:** `12.3`

Saves the device's current parameter state to the AB compare slot. After calling this, the
user can switch between preset A and preset B using the AB Compare button. Only works on
devices where `can_compare_ab` is `True`.

#### `store_chosen_bank(script_index, bank_index)`

- **Returns:** `None`
- **Args:**
    - `script_index: int`
    - `bank_index: int`
- **Since:** `<11`

Sets the selected bank in the device for persistency with a hardware control surface. The
Max docs note this is "usually not relevant" for general use. `script_index` identifies the
control surface script and `bank_index` identifies the bank within that script's mapping.

---

## Device.View

> `Live.Device.Device.View`

Represents the view aspects of a device.

### Properties

| Property       | Type   | Settable | Listenable | Summary                                             |
| -------------- | ------ | -------- | ---------- | --------------------------------------------------- |
| `is_collapsed` | `bool` | `bool`   | `yes`      | Whether the device is shown collapsed in the chain. |

#### `is_collapsed`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Controls whether the device is shown collapsed (minimized) in the device chain. `True` means
the device is collapsed to a narrow strip showing only its title bar; `False` means the full
device UI is visible.

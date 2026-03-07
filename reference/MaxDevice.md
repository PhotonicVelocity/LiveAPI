# MaxDevice

## MaxDevice

This class represents a Max for Live device in Live. A MaxDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for accessing the device's audio and MIDI I/O routing and parameter bank
configuration.

Max for Live devices can expose audio and MIDI inputs and outputs that are accessible
through the API, unlike standard Live devices.

### Sources

- **Primary:** `Live/classes/devices/MaxDevice.py` (stub dump)
- **Secondary:** `MaxForLive/maxdevice.md`
- **Probes:** `.tmp/probe_device_io3.py`, `.tmp/probe_device_io4.py` (Live 12.3.5)

### Probe Notes

Probed with Live 12.3.5 using "Max Audio Effect", "Max Instrument", and "Max MIDI Effect".

- Bridge returns `type: "MaxDevice"` for all M4L device types.
- `class_name` is always `"MxDeviceAudioEffect"` regardless of M4L device kind (audio effect,
  instrument, or MIDI effect). The standard `Device.type` property distinguishes them.
- All M4L devices expose `audio_inputs` and `audio_outputs` (at least one `DeviceIO` each for a blank
  device). `midi_inputs` and `midi_outputs` are empty for blank M4L devices — they only appear when
  the Max patch exposes MIDI I/O objects.
- All four I/O list properties are listenable (listener fires when the I/O configuration changes).
- Each I/O list item is a `DeviceIO` object with its own OID and full routing capabilities.
- `bank_parameters_changed` listener fires successfully (event-only, no readable property).
- `get_bank_count()` returns `0` for blank M4L devices. `get_bank_name(0)` and `get_bank_parameters(0)`
  raise `InternalError` when bank count is 0. `get_bank_parameters(-1)` raises
  `"this device has no best-of bank"` for devices without configured banks.

### Open Questions

- ~~What type do the `audio_inputs` / `audio_outputs` / `midi_inputs` / `midi_outputs`
  lists contain?~~ **Resolved:** `DeviceIO` objects with their own OIDs and routing properties.
- ~~What triggers the `bank_parameters_changed` event?~~ **Partially resolved:** Listener registers
  successfully. Trigger condition not tested (would require editing a Max patch's bank configuration).
- ~~Does `get_value_item_icons()` work for all parameter types?~~ **Unprobed.** Needs an M4L device
  with list-style parameters.
- Bank methods (`get_bank_name`, `get_bank_parameters`) fail with `InternalError` when called with
  invalid indices or on devices with no banks. Need to test with an M4L device that has configured
  parameter banks.

### Children

None beyond those inherited from Device (`parameters`, `view`).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
MaxDevice adds:

| Property        | Get Returns      | Set Accepts | Listenable | Available Since | Summary                                   |
| --------------- | ---------------- | ----------- | ---------- | --------------- | ----------------------------------------- |
| `audio_inputs`  | `list[DeviceIO]` | —           | `yes`      | `<11`           | Audio inputs exposed by this M4L device.  |
| `audio_outputs` | `list[DeviceIO]` | —           | `yes`      | `<11`           | Audio outputs exposed by this M4L device. |
| `midi_inputs`   | `list[DeviceIO]` | —           | `yes`      | `11.0`          | MIDI inputs exposed by this M4L device.   |
| `midi_outputs`  | `list[DeviceIO]` | —           | `yes`      | `11.0`          | MIDI outputs exposed by this M4L device.  |

#### `audio_inputs`

- **Get Returns:** `list[DeviceIO]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed`

**Description:**
Read-only list of all audio inputs that this Max for Live device offers. Each item is a
`DeviceIO` object with its own OID and routing properties. Blank M4L devices have at least one
audio input. Listener fires when the set of audio inputs changes.

#### `audio_outputs`

- **Get Returns:** `list[DeviceIO]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed`

**Description:**
Read-only list of all audio outputs that this Max for Live device offers. Each item is a
`DeviceIO` object. Blank M4L devices have at least one audio output. Listener fires when the
set of audio outputs changes.

#### `midi_inputs`

- **Get Returns:** `list[DeviceIO]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed`

**Description:**
Read-only list of all MIDI inputs that this Max for Live device offers. Empty for blank M4L
devices — only populated when the Max patch exposes MIDI I/O objects. Listener fires when the
set of MIDI inputs changes.

#### `midi_outputs`

- **Get Returns:** `list[DeviceIO]`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed`

**Description:**
Read-only list of all MIDI outputs that this Max for Live device offers. Empty for blank M4L
devices — only populated when the Max patch exposes MIDI I/O objects. Listener fires when the
set of MIDI outputs changes.

### Events

| Event                     | Listenable | Available Since | Summary                                                |
| ------------------------- | ---------- | --------------- | ------------------------------------------------------ |
| `bank_parameters_changed` | `yes`      | `N/A`           | Fires when the device's parameter bank layout changes. |

#### `bank_parameters_changed`

- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | probed`
- **Probe Status:** `probed` (listener registration confirmed)

**Description:**
An event-only listenable with no corresponding readable property. The listener fires
when the parameter bank configuration changes. There is no property to read -- only
add/remove/has listener methods exist.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`), MaxDevice adds:

| Signature                                          | Returns | Available Since | Summary                                         |
| -------------------------------------------------- | ------- | --------------- | ----------------------------------------------- |
| `get_bank_count()`                                 | `int`   | `<11`           | Number of parameter banks.                      |
| `get_bank_name(bank_index: int)`                   | `str`   | `<11`           | Name of a parameter bank by index.              |
| `get_bank_parameters(bank_index: int)`             | `list`  | `<11`           | Parameter indices for a given bank.             |
| `get_value_item_icons(parameter: DeviceParameter)` | `list`  | `<11`           | Icon identifiers for a list parameter's values. |

#### `get_bank_count()`

- **Returns:** `int`
- **Args:** None
- **Raises/Errors:** None observed.
- **Undo-tracked:** `N/A`
- **Side Effects:** None (read-only query).
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed`

**Description:**
Returns the number of parameter banks for this device. Returns `0` for blank M4L devices
(no configured banks). Related to hardware control surface integration.

#### `get_bank_name(bank_index: int)`

- **Returns:** `str`
- **Args:**
  - `bank_index: int` -- index of the bank to query
- **Raises/Errors:** `InternalError` if index is out of range or device has no banks.
- **Undo-tracked:** `N/A`
- **Side Effects:** None (read-only query).
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (error case only — no M4L device with banks tested)

**Description:**
Returns the name of the parameter bank at the given index. Raises `InternalError` when called
on a device with zero banks.

#### `get_bank_parameters(bank_index: int)`

- **Returns:** `list[int]`
- **Args:**
  - `bank_index: int` -- index of the bank to query; `-1` refers to the "Best of" bank
- **Raises/Errors:** `InternalError` if index is out of range. `"this device has no best-of bank"` for `-1` on devices without configured banks.
- **Undo-tracked:** `N/A`
- **Side Effects:** None (read-only query).
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max | probed`
- **Probe Status:** `probed` (error cases — no M4L device with banks tested)

**Description:**
Returns the parameter indices for the bank at the given index. Empty slots are marked
as `-1`. Passing `-1` as the bank index returns the "Best of" bank.

#### `get_value_item_icons(parameter: DeviceParameter)`

- **Returns:** `list[str]`
- **Args:**
  - `parameter: DeviceParameter` -- the parameter to query for icons
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None (read-only query).
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns a list of icon identifier strings for a list-style parameter's values. An empty
string indicates no icon should be displayed for that value. An empty list means no icons
should be displayed at all. Related to hardware control surface integration.

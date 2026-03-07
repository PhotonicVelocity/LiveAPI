# ShifterDevice

## ShifterDevice

This class represents a Shifter audio effect device in Live. ShifterDevice is a subclass
of Device -- it has all the children, properties, and methods of Device plus additional
members for selecting the pitch mode and adjusting the MIDI pitch bend range.

Shifter is a pitch-shifting and frequency-shifting audio effect. The pitch mode
determines whether pitch is controlled internally or via MIDI input.

### Sources

- **Primary:** `Live/classes/devices/ShifterDevice.py` (stub dump)
- **Secondary:** `MaxForLive/shifterdevice.md`
- **Probes:** `tools/probes/probe_device_subclasses_trivial.py`

### Probe Notes

- Bridge type: `"ShifterDevice"`. `class_name`: `"Shifter"`.
- `pitch_mode_index` returns `int`. Default is 0 ("Internal"). Settable, round-trips correctly.
- `pitch_mode_list` returns `list[str]` (StringVector serializes as plain list through bridge).
  Values: `["Internal", "MIDI"]`. Not listenable (static list).
- `pitch_bend_range` returns `int`. Default is 2. Settable (set to 24, read back 24), round-trips.
- All properties except `pitch_mode_list` are listenable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
ShifterDevice adds:

| Property           | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                   |
| ------------------ | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------------- |
| `pitch_bend_range` | `int`       | `int`       | `yes`      | `11.1`          | MIDI pitch bend range used in MIDI pitch mode.            |
| `pitch_mode_index` | `int`       | `int`       | `yes`      | `11.1`          | Index of the current pitch mode (0 = Internal, 1 = MIDI). |
| `pitch_mode_list`  | `list[str]` | —           | `no`       | `11.1`          | List of available pitch mode names.                       |

#### `pitch_bend_range`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `11.1`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The pitch bend range in semitones, used when the pitch mode is set to MIDI. Default is 2.

#### `pitch_mode_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `11.1`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The index of the current pitch mode. Values: 0 = Internal, 1 = MIDI.

#### `pitch_mode_list`

- **Get Returns:** `list[str]` (StringVector, serialized as plain list by bridge)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.1`
- **Sources:** `stub`
- **Probe Status:** `probed`

**Description:**
The list of available pitch mode names. Static list, not listenable.
Values: `["Internal", "MIDI"]`.

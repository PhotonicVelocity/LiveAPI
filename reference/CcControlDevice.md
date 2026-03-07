# CcControlDevice

## CcControlDevice

This class represents a CC Control device in Live. CcControlDevice is a Device subclass
that sends MIDI CC (Continuous Controller) messages. It exposes 12 continuous CC target
slots (`custom_float_target_0` through `_11`) and 1 toggle CC target slot (`custom_bool_target`),
each with a corresponding options list. All 13 targets select from the same 120-item MIDI CC
name list. A `resend()` method retransmits all current CC values.

### Sources

- **Primary:** `Live/classes/devices/CcControlDevice.py` (stub dump)
- **Secondary:** None (no Max for Live docs found)
- **Probes:** 2026-02-25 (Live 12.3.5)

### Probe Notes

- **Bridge type:** `"CcControlDevice"`.
- **`class_name`:** `"MidiCcControl"`. **`class_display_name`:** `"CC Control"`.
- **`type`:** 4 (`MIDI_EFFECT`).
- **Insert name:** `"CC Control"` (matches `class_display_name`).
- **All 13 target properties** are `int` (index into the CC name list). Default: `0` for float targets,
  `64` for bool target. All settable, all listenable.
- **All 13 list properties** return identical `list[str]` of 120 MIDI CC names:
  `["None", "1: Modulation Wheel", "2: Breath Controller", ..., "119: Undefined"]`.
- **`resend()`** returns `None`, executes without error.
- **ChoiceProperty pattern:** Each target + list pair is a natural fit for `ChoiceProperty`.

### Children

| Child        | Returns                     | Shape    | Access | Listenable | Available Since | Summary                                        |
| ------------ | --------------------------- | -------- | ------ | ---------- | --------------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | `get`  | `yes`      | `12.0`          | Automatable parameters exposed by this device. |
| `view`       | `CcControlDevice.View`      | `single` | `get`  | `no`       | `12.0`          | View aspects of the device (collapse state).   |

### Properties

| Property                      | Get Returns | Set Accepts | Listenable | Available Since | Summary                        |
| ----------------------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------ |
| `custom_float_target_0`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 0 (index).      |
| `custom_float_target_0_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 0.  |
| `custom_float_target_1`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 1 (index).      |
| `custom_float_target_1_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 1.  |
| `custom_float_target_2`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 2.              |
| `custom_float_target_2_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 2.  |
| `custom_float_target_3`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 3.              |
| `custom_float_target_3_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 3.  |
| `custom_float_target_4`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 4.              |
| `custom_float_target_4_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 4.  |
| `custom_float_target_5`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 5.              |
| `custom_float_target_5_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 5.  |
| `custom_float_target_6`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 6.              |
| `custom_float_target_6_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 6.  |
| `custom_float_target_7`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 7.              |
| `custom_float_target_7_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 7.  |
| `custom_float_target_8`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 8.              |
| `custom_float_target_8_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 8.  |
| `custom_float_target_9`       | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 9.              |
| `custom_float_target_9_list`  | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 9.  |
| `custom_float_target_10`      | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 10.             |
| `custom_float_target_10_list` | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 10. |
| `custom_float_target_11`      | `int`       | `int`       | `yes`      | `12.0`          | CC target slot 11.             |
| `custom_float_target_11_list` | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for slot 11. |
| `custom_bool_target`          | `int`       | `int`       | `yes`      | `12.0`          | Toggle CC target (index).      |
| `custom_bool_target_list`     | `list[str]` | —           | `no`       | `12.0`          | 120 MIDI CC names for toggle.  |

All 13 lists are identical — 120 entries from `"None"` through `"119: Undefined"`, covering
standard MIDI CC assignments (Modulation Wheel, Breath Controller, Volume, Pan, Sustain, etc.).

### Methods

| Signature  | Returns | Available Since | Summary                           |
| ---------- | ------- | --------------- | --------------------------------- |
| `resend()` | `None`  | `12.0`          | Retransmit all current CC values. |

---

## CcControlDevice.View

Represents the view aspects of a CcControlDevice. Identical to `Device.View`.

### Properties

| Property       | Get Returns | Set Accepts | Listenable | Available Since | Summary                                             |
| -------------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------- |
| `is_collapsed` | `bool`      | `bool`      | `yes`      | `12.0`          | Whether the device is shown collapsed in the chain. |

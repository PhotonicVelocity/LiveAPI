# CCFeedbackRule

> `Live.MidiMap.CCFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `CCFeedbackRule()`

## Properties

| Property       | Type    | Settable | Listenable | Description |
| -------------- | ------- | -------- | ---------- | ----------- |
| `cc_no`        | `int`   | `yes`    | `no`       |             |
| `cc_value_map` | `tuple` | `yes`    | `no`       |             |
| `channel`      | `int`   | `yes`    | `no`       |             |
| `delay_in_ms`  | `float` | `yes`    | `no`       |             |
| `enabled`      | `bool`  | `yes`    | `no`       |             |

### `cc_no`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

### `cc_value_map`

- **Type:** `tuple`
- **Settable:** `yes`
- **Listenable:** `no`

### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

# NoteFeedbackRule

> `Live.MidiMap.NoteFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `NoteFeedbackRule()`

## Properties

| Property      | Type    | Settable | Listenable | Description |
| ------------- | ------- | -------- | ---------- | ----------- |
| `channel`     | `int`   | `yes`    | `no`       |             |
| `delay_in_ms` | `float` | `yes`    | `no`       |             |
| `enabled`     | `bool`  | `yes`    | `no`       |             |
| `note_no`     | `int`   | `yes`    | `no`       |             |
| `vel_map`     | `tuple` | `yes`    | `no`       |             |

### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

### `note_no`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

### `vel_map`

- **Type:** `tuple`
- **Settable:** `yes`
- **Listenable:** `no`

# PitchBendFeedbackRule

> `Live.MidiMap.PitchBendFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `PitchBendFeedbackRule()`

## Properties

| Property         | Type    | Settable | Listenable | Description |
| ---------------- | ------- | -------- | ---------- | ----------- |
| `channel`        | `int`   | `yes`    | `no`       |             |
| `delay_in_ms`    | `float` | `yes`    | `no`       |             |
| `enabled`        | `bool`  | `yes`    | `no`       |             |
| `value_pair_map` | `tuple` | `yes`    | `no`       |             |

### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

### `value_pair_map`

- **Type:** `tuple`
- **Settable:** `yes`
- **Listenable:** `no`

## Enums

### `MapMode`

| Value | Name                             |
| ----- | -------------------------------- |
| `0`   | `absolute`                       |
| `1`   | `relative_signed_bit`            |
| `2`   | `relative_binary_offset`         |
| `3`   | `relative_two_compliment`        |
| `4`   | `relative_signed_bit2`           |
| `5`   | `absolute_14_bit`                |
| `6`   | `relative_smooth_signed_bit`     |
| `7`   | `relative_smooth_binary_offset`  |
| `8`   | `relative_smooth_two_compliment` |
| `9`   | `relative_smooth_signed_bit2`    |

## Module Functions

| Function                                                                                                                                                                                                                       | Returns | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ----------- |
| `forward_midi_cc(script_handle: int, midi_map_handle: int, channel: int, cc_no: int, ShouldConsumeEvent: bool = True)`                                                                                                         | `bool`  |             |
| `forward_midi_note(script_handle: int, midi_map_handle: int, channel: int, note: int, ShouldConsumeEvent: bool = True)`                                                                                                        | `bool`  |             |
| `forward_midi_pitchbend(script_handle: int, midi_map_handle: int, channel: int)`                                                                                                                                               | `bool`  |             |
| `map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float = 1.0)`                                                  | `bool`  |             |
| `map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float = 1.0)` | `bool`  |             |
| `map_midi_note(midi_map_handle: int, parameter: DeviceParameter, channel: int, note: int)`                                                                                                                                     | `bool`  |             |
| `map_midi_note_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, channel: int, note: int, feedback_rule: NoteFeedbackRule)`                                                                                  | `bool`  |             |
| `map_midi_pitchbend(midi_map_handle: int, parameter: DeviceParameter, channel: int, avoid_takeover: bool)`                                                                                                                     | `bool`  |             |
| `map_midi_pitchbend_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, channel: int, feedback_rule: PitchBendFeedbackRule, avoid_takeover: bool)`                                                             | `bool`  |             |
| `send_feedback_for_parameter(midi_map_handle: int, parameter: DeviceParameter)`                                                                                                                                                | `None`  |             |

### `forward_midi_cc(script_handle: int, midi_map_handle: int, channel: int, cc_no: int, ShouldConsumeEvent: bool = True)`

- **Returns:** `bool`
- **Args:**
  - `script_handle: int`
  - `midi_map_handle: int`
  - `channel: int`
  - `cc_no: int`
  - `ShouldConsumeEvent: bool = True`

### `forward_midi_note(script_handle: int, midi_map_handle: int, channel: int, note: int, ShouldConsumeEvent: bool = True)`

- **Returns:** `bool`
- **Args:**
  - `script_handle: int`
  - `midi_map_handle: int`
  - `channel: int`
  - `note: int`
  - `ShouldConsumeEvent: bool = True`

### `forward_midi_pitchbend(script_handle: int, midi_map_handle: int, channel: int)`

- **Returns:** `bool`
- **Args:**
  - `script_handle: int`
  - `midi_map_handle: int`
  - `channel: int`

### `map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float = 1.0)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `midi_channel: int`
  - `controller_number: int`
  - `map_mode: MapMode`
  - `avoid_takeover: bool`
  - `sensitivity: float = 1.0`

### `map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float = 1.0)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `midi_channel: int`
  - `controller_number: int`
  - `map_mode: MapMode`
  - `feedback_rule: CCFeedbackRule`
  - `avoid_takeover: bool`
  - `sensitivity: float = 1.0`

### `map_midi_note(midi_map_handle: int, parameter: DeviceParameter, channel: int, note: int)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `channel: int`
  - `note: int`

### `map_midi_note_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, channel: int, note: int, feedback_rule: NoteFeedbackRule)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `channel: int`
  - `note: int`
  - `feedback_rule: NoteFeedbackRule`

### `map_midi_pitchbend(midi_map_handle: int, parameter: DeviceParameter, channel: int, avoid_takeover: bool)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `channel: int`
  - `avoid_takeover: bool`

### `map_midi_pitchbend_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, channel: int, feedback_rule: PitchBendFeedbackRule, avoid_takeover: bool)`

- **Returns:** `bool`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`
  - `channel: int`
  - `feedback_rule: PitchBendFeedbackRule`
  - `avoid_takeover: bool`

### `send_feedback_for_parameter(midi_map_handle: int, parameter: DeviceParameter)`

- **Returns:** `None`
- **Args:**
  - `midi_map_handle: int`
  - `parameter: DeviceParameter`

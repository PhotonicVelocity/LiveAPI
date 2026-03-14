# MidiMap (Module)

## CCFeedbackRule (Class)

> `Live.MidiMap.CCFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `CCFeedbackRule()`

### Properties

| Property                        | Type    | Supports    |
| ------------------------------- | ------- | ----------- |
| [`cc_no`](#cc_no)               | `int`   | `get`/`set` |
| [`cc_value_map`](#cc_value_map) | `tuple` | `get`/`set` |
| [`channel`](#channel)           | `int`   | `get`/`set` |
| [`delay_in_ms`](#delay_in_ms)   | `float` | `get`/`set` |
| [`enabled`](#enabled)           | `bool`  | `get`/`set` |

#### `cc_no`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `cc_value_map`

- **Type:** `tuple`
- **Settable:** `yes`
- **Listenable:** `no`

#### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

## NoteFeedbackRule (Class)

> `Live.MidiMap.NoteFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `NoteFeedbackRule()`

### Properties

| Property                      | Type    | Supports    |
| ----------------------------- | ------- | ----------- |
| [`channel`](#channel)         | `int`   | `get`/`set` |
| [`delay_in_ms`](#delay_in_ms) | `float` | `get`/`set` |
| [`enabled`](#enabled)         | `bool`  | `get`/`set` |
| [`note_no`](#note_no)         | `int`   | `get`/`set` |
| [`vel_map`](#vel_map)         | `tuple` | `get`/`set` |

#### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

#### `note_no`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `vel_map`

- **Type:** `tuple`
- **Settable:** `yes`
- **Listenable:** `no`

## PitchBendFeedbackRule (Class)

> `Live.MidiMap.PitchBendFeedbackRule`

Structure to define feedback properties of MIDI mappings.

**Constructor:** `PitchBendFeedbackRule()`

### Properties

| Property                            | Type    | Supports    |
| ----------------------------------- | ------- | ----------- |
| [`channel`](#channel)               | `int`   | `get`/`set` |
| [`delay_in_ms`](#delay_in_ms)       | `float` | `get`/`set` |
| [`enabled`](#enabled)               | `bool`  | `get`/`set` |
| [`value_pair_map`](#value_pair_map) | `tuple` | `get`/`set` |

#### `channel`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

#### `delay_in_ms`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

#### `value_pair_map`

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

| Function                                                                                                                                                                                                                                       | Returns |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [`forward_midi_cc()`](#forward_midi_ccscript_handle-int-midi_map_handle-int-channel-int-cc_no-int-shouldconsumeevent-bool-true)                                                                                                                | `bool`  |
| [`forward_midi_note()`](#forward_midi_notescript_handle-int-midi_map_handle-int-channel-int-note-int-shouldconsumeevent-bool-true)                                                                                                             | `bool`  |
| [`forward_midi_pitchbend()`](#forward_midi_pitchbendscript_handle-int-midi_map_handle-int-channel-int)                                                                                                                                         | `bool`  |
| [`map_midi_cc()`](#map_midi_ccmidi_map_handle-int-parameter-deviceparameter-midi_channel-int-controller_number-int-map_mode-mapmode-avoid_takeover-bool-sensitivity-float-10)                                                                  | `bool`  |
| [`map_midi_cc_with_feedback_map()`](#map_midi_cc_with_feedback_mapmidi_map_handle-int-parameter-deviceparameter-midi_channel-int-controller_number-int-map_mode-mapmode-feedback_rule-ccfeedbackrule-avoid_takeover-bool-sensitivity-float-10) | `bool`  |
| [`map_midi_note()`](#map_midi_notemidi_map_handle-int-parameter-deviceparameter-channel-int-note-int)                                                                                                                                          | `bool`  |
| [`map_midi_note_with_feedback_map()`](#map_midi_note_with_feedback_mapmidi_map_handle-int-parameter-deviceparameter-channel-int-note-int-feedback_rule-notefeedbackrule)                                                                       | `bool`  |
| [`map_midi_pitchbend()`](#map_midi_pitchbendmidi_map_handle-int-parameter-deviceparameter-channel-int-avoid_takeover-bool)                                                                                                                     | `bool`  |
| [`map_midi_pitchbend_with_feedback_map()`](#map_midi_pitchbend_with_feedback_mapmidi_map_handle-int-parameter-deviceparameter-channel-int-feedback_rule-pitchbendfeedbackrule-avoid_takeover-bool)                                             | `bool`  |
| [`send_feedback_for_parameter()`](#send_feedback_for_parametermidi_map_handle-int-parameter-deviceparameter)                                                                                                                                   | `None`  |

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

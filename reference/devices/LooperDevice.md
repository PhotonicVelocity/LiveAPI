# LooperDevice (Module)

## LooperDevice (Class)

> `Live.LooperDevice.LooperDevice`

This class represents a Looper device.

**Live Object:** `yes`

### Properties

| Property                                                  | Type                               | Supports             |
| --------------------------------------------------------- | ---------------------------------- | -------------------- |
| [`can_compare_ab`](#can_compare_ab)                       | `bool`                             | `get`                |
| [`can_have_chains`](#can_have_chains)                     | `bool`                             | `get`                |
| [`can_have_drum_pads`](#can_have_drum_pads)               | `bool`                             | `get`                |
| [`canonical_parent`](#canonical_parent)                   | `Track`                            | `get`                |
| [`class_display_name`](#class_display_name)               | `str`                              | `get`                |
| [`class_name`](#class_name)                               | `str`                              | `get`                |
| [`is_active`](#is_active)                                 | `bool`                             | `get`                |
| [`is_using_compare_preset_b`](#is_using_compare_preset_b) | `bool`                             | `get`/`set`          |
| [`latency_in_ms`](#latency_in_ms)                         | `float`                            | `get`                |
| [`latency_in_samples`](#latency_in_samples)               | `int`                              | `get`                |
| [`loop_length`](#loop_length)                             | `float`                            | `get`/`listen`       |
| [`name`](#name)                                           | `str`                              | `get`/`set`          |
| [`overdub_after_record`](#overdub_after_record)           | `bool`                             | `get`/`set`/`listen` |
| [`parameters`](#parameters)                               | `tuple[DeviceParameter, Ellipsis]` | `get`                |
| [`record_length_index`](#record_length_index)             | `int`                              | `get`/`set`/`listen` |
| [`record_length_list`](#record_length_list)               | `tuple[str, Ellipsis]`             | `get`                |
| [`tempo`](#tempo)                                         | `float`                            | `get`/`listen`       |
| [`type`](#type)                                           | `DeviceType`                       | `get`                |
| [`view`](#view)                                           | `Device.View`                      | `get`                |

#### `can_compare_ab`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the Device has the capability to AB compare.

#### `can_have_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a rack.

#### `can_have_drum_pads`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a drum rack.

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the Device.

#### `class_display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class name as displayed in Live's browser and device chain

#### `class_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class.

#### `is_active`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

#### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in ms.

#### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in samples.

#### `loop_length`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

The length of Looper's buffer.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

#### `overdub_after_record`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch will be to playback without overdubbing.

#### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

#### `record_length_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Record Length chooser entry index.

#### `record_length_list`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Read-only access to the list of Record Length chooser entry strings.

#### `tempo`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

The tempo of Looper's buffer.

#### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

#### `view`

- **Type:** `Device.View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

### Methods

| Method                                                            | Returns |
| ----------------------------------------------------------------- | ------- |
| [`clear()`](#clear)                                               | `None`  |
| [`double_length()`](#double_length)                               | `None`  |
| [`double_speed()`](#double_speed)                                 | `None`  |
| [`export_to_clip_slot()`](#export_to_clip_slotclip_slot-clipslot) | `None`  |
| [`half_length()`](#half_length)                                   | `None`  |
| [`half_speed()`](#half_speed)                                     | `None`  |
| [`overdub()`](#overdub)                                           | `None`  |
| [`play()`](#play)                                                 | `None`  |
| [`record()`](#record)                                             | `None`  |
| [`stop()`](#stop)                                                 | `None`  |
| [`undo()`](#undo)                                                 | `None`  |

#### `clear()`

- **Returns:** `None`

Erase Looper's recorded content.

#### `double_length()`

- **Returns:** `None`

Double the length of Looper's buffer.

#### `double_speed()`

- **Returns:** `None`

Double the speed of Looper's playback.

#### `export_to_clip_slot(clip_slot: ClipSlot)`

- **Returns:** `None`
- **Args:**
  - `clip_slot: ClipSlot`

Export Looper's content to a Session Clip Slot.

#### `half_length()`

- **Returns:** `None`

Halve the length of Looper's buffer.

#### `half_speed()`

- **Returns:** `None`

Halve the speed of Looper's playback.

#### `overdub()`

- **Returns:** `None`

Play back while adding additional layers of incoming audio.

#### `play()`

- **Returns:** `None`

Play back without overdubbing.

#### `record()`

- **Returns:** `None`

Record incoming audio.

#### `stop()`

- **Returns:** `None`

Stop Looper's playback.

#### `undo()`

- **Returns:** `None`

Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undooperation.

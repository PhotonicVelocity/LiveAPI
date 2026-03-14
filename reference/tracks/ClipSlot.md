# ClipSlot (Module)

## ClipSlot (Class)

> `Live.ClipSlot.ClipSlot`

This class represents an entry in Lives Session view matrix.

**Live Object:** `yes`

**Access via:**

- `Song.View.highlighted_clip_slot`

### Properties

| Property                                        | Type                   | Supports             |
| ----------------------------------------------- | ---------------------- | -------------------- |
| [`canonical_parent`](#canonical_parent)         | `Track`                | `get`                |
| [`clip`](#clip)                                 | `Clip`                 | `get`                |
| [`color`](#color)                               | `int`                  | `get`/`listen`       |
| [`color_index`](#color_index)                   | `int`                  | `get`/`listen`       |
| [`controls_other_clips`](#controls_other_clips) | `bool`                 | `get`/`listen`       |
| [`has_clip`](#has_clip)                         | `bool`                 | `get`/`listen`       |
| [`has_stop_button`](#has_stop_button)           | `bool`                 | `get`/`set`/`listen` |
| [`is_group_slot`](#is_group_slot)               | `bool`                 | `get`                |
| [`is_playing`](#is_playing)                     | `bool`                 | `get`                |
| [`is_recording`](#is_recording)                 | `bool`                 | `get`                |
| [`is_triggered`](#is_triggered)                 | `bool`                 | `get`/`listen`       |
| [`playing_status`](#playing_status)             | `ClipSlotPlayingState` | `get`/`listen`       |
| [`will_record_on_start`](#will_record_on_start) | `bool`                 | `get`                |

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the ClipSlot.

#### `clip`

- **Type:** `Clip`
- **Settable:** `no`
- **Listenable:** `no`

Returns the Clip which this clipslots currently owns. Might be None.

#### `color`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the canonical color for the clip slot or None if it does not exist.

#### `color_index`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Returns the canonical color index for the clip slot or None if it does not exist.

#### `controls_other_clips`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if firing this slot will fire clips in other slots. Can only be true for slots in group tracks.

#### `has_clip`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if this Clipslot owns a Clip.

#### `has_stop_button`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set if this Clip has a stop button, which will, if fired, stop any other Clip that is currently playing the Track we do belong to.

#### `is_group_slot`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns whether this clip slot is a group track slot (group slot).

#### `is_playing`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns whether the clip associated with the slot is playing.

#### `is_recording`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns whether the clip associated with the slot is recording.

#### `is_triggered`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the triggering state of the clip slot.

#### `playing_status`

- **Type:** `ClipSlotPlayingState`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the playing state of the clip slot. Can be either stopped, playing, or recording.

#### `will_record_on_start`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

returns true if the clip slot will record on being fired.

### Methods

| Method                                                                                         | Returns | Description                                                                      |
| ---------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------- |
| [`create_audio_clip(path: str)`](#create_audio_clippath-str)                                   | `Clip`  | Creates an audio clip referencing the file at the given absolute path in the ... |
| [`create_clip(pages: float)`](#create_clippages-float)                                         | `Clip`  | Creates an empty clip with the given length in the slot.                         |
| [`delete_clip()`](#delete_clip)                                                                | `None`  | Removes the clip contained in the slot.                                          |
| [`duplicate_clip_to(target_clip_slot: ClipSlot)`](#duplicate_clip_totarget_clip_slot-clipslot) | `None`  | Duplicates the slot's clip to the passed in target slot.                         |
| [`fire()`](#fire)                                                                              | `None`  | Fire a Clip if this Clipslot owns one, else trigger the stop button, if we ha... |
| [`set_fire_button_state(state: bool)`](#set_fire_button_statestate-bool)                       | `None`  | Set the clipslot's fire button state directly.                                   |
| [`stop()`](#stop)                                                                              | `None`  | Stop playing the contained Clip, if there is a Clip and its currently playing.   |

#### `create_audio_clip(path: str)`

- **Returns:** `Clip`
- **Args:**
  - `path: str`

Creates an audio clip referencing the file at the given absolute path in the slot. Throws an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.

#### `create_clip(pages: float)`

- **Returns:** `Clip`
- **Args:**
  - `pages: float`

Creates an empty clip with the given length in the slot. Throws an error when called on non-empty slots or slots in non-MIDI tracks.

#### `delete_clip()`

- **Returns:** `None`

Removes the clip contained in the slot. Raises an exception if the slot was empty.

#### `duplicate_clip_to(target_clip_slot: ClipSlot)`

- **Returns:** `None`
- **Args:**
  - `target_clip_slot: ClipSlot`

Duplicates the slot's clip to the passed in target slot. Overrides the target's clip if it's not empty. Raises an exception if the (source) slot itself is empty, or if source and target have different track types (audio vs. MIDI). Also raises if the source or target slot is in a group track (so called group slot).

#### `fire()`

- **Returns:** `None`

Fire a Clip if this Clipslot owns one, else trigger the stop button, if we have one.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`

Set the clipslot's fire button state directly. Supports all launch modes.

#### `stop()`

- **Returns:** `None`

Stop playing the contained Clip, if there is a Clip and its currently playing.

## Enums

### `ClipSlotPlayingState`

| Value | Name        |
| ----- | ----------- |
| `0`   | `stopped`   |
| `1`   | `started`   |
| `2`   | `recording` |

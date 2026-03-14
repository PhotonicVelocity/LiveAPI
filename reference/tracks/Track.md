# Track

> `Live.Track.Track`

This class represents a track in Live. It can be either an Audio track, a MIDI Track, a Return Track or the Main track. The Main Track and at least one Audio or MIDI track will be always present. Return Tracks are optional.

**Live Object:** `yes`

**Access via:**

- `RoutingType.attached_object`
- `Song.create_audio_track()`
- `Song.create_midi_track()`
- `Song.create_return_track()`
- `Song.master_track`
- `Song.View.selected_track`
- `Track.group_track`

## View

> `Live.Track.Track.View`

Representing the view aspects of a Track.

**Live Object:** `yes`

### Properties

| Property             | Type     | Settable | Listenable | Description                                                          |
| -------------------- | -------- | -------- | ---------- | -------------------------------------------------------------------- |
| `canonical_parent`   | `Track`  | `no`     | `no`       | Get the canonical parent of the track view.                          |
| `device_insert_mode` | `bool`   | `yes`    | `yes`      | Get/Listen the device insertion mode of the track.                   |
| `is_collapsed`       | `bool`   | `yes`    | `yes`      | Get/Set/Listen if the track is shown collapsed in the arranger view. |
| `selected_device`    | `Device` | `no`     | `yes`      | Get/Set/Listen the insertion mode of the device.                     |

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the track view.

#### `device_insert_mode`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Listen the device insertion mode of the track. By default, it will insert devices at the end, but it can be changed to make it relative to current selection.

#### `is_collapsed`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set/Listen if the track is shown collapsed in the arranger view.

#### `selected_device`

- **Type:** `Device`
- **Settable:** `no`
- **Listenable:** `yes`

Get/Set/Listen the insertion mode of the device. While in insertion mode, loading new devices from the browser will place devices at the selected position.

### Methods

| Method                | Returns | Description                                   |
| --------------------- | ------- | --------------------------------------------- |
| `select_instrument()` | `bool`  | Selects the track's instrument if it has one. |

#### `select_instrument()`

- **Returns:** `bool`

Selects the track's instrument if it has one.

## Properties

| Property                            | Type                              | Settable | Listenable | Description                                                                      |
| ----------------------------------- | --------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `arm`                               | `bool`                            | `yes`    | `yes`      | Arm the track for recording.                                                     |
| `arrangement_clips`                 | `tuple`                           | `no`     | `yes`      | const access to the list of clips in arrangement viewThe list will be empty f... |
| `available_input_routing_channels`  | `tuple[RoutingChannel, Ellipsis]` | `no`     | `yes`      | Return a list of source channels for input routing.                              |
| `available_input_routing_types`     | `tuple[RoutingType, Ellipsis]`    | `no`     | `yes`      | Return a list of source types for input routing.                                 |
| `available_output_routing_channels` | `tuple[RoutingChannel, Ellipsis]` | `no`     | `yes`      | Return a list of destination channels for output routing.                        |
| `available_output_routing_types`    | `tuple[RoutingType, Ellipsis]`    | `no`     | `yes`      | Return a list of destination types for output routing.                           |
| `back_to_arranger`                  | `bool`                            | `yes`    | `yes`      | Indicates if it's possible to go back to playing back the clips in the Arrang... |
| `can_be_armed`                      | `bool`                            | `no`     | `no`       | return True, if this Track has a valid arm property.                             |
| `can_be_frozen`                     | `bool`                            | `no`     | `no`       | return True, if this Track can be frozen.                                        |
| `can_show_chains`                   | `bool`                            | `no`     | `no`       | return True, if this Track contains a rack instrument device that is capable ... |
| `canonical_parent`                  | `Song`                            | `no`     | `no`       | Get the canonical parent of the track.                                           |
| `clip_slots`                        | `tuple`                           | `no`     | `yes`      | const access to the list of clipslots (see class AClipSlot) for this track.      |
| `color`                             | `int`                             | `yes`    | `yes`      | Get/set access to the color of the Track (RGB).                                  |
| `color_index`                       | `int`                             | `yes`    | `yes`      | Get/Set access to the color index of the track.                                  |
| `current_input_routing`             | `str`                             | `yes`    | `yes`      | Get/Set the name of the current active input routing.                            |
| `current_input_sub_routing`         | `str`                             | `yes`    | `yes`      | Get/Set the current active input sub routing.                                    |
| `current_monitoring_state`          | `int`                             | `yes`    | `yes`      | Get/Set the track's current monitoring state.                                    |
| `current_output_routing`            | `str`                             | `yes`    | `yes`      | Get/Set the current active output routing.                                       |
| `current_output_sub_routing`        | `str`                             | `yes`    | `yes`      | Get/Set the current active output sub routing.                                   |
| `devices`                           | `tuple`                           | `no`     | `yes`      | Return const access to all available Devices that are present in the Tracks D... |
| `fired_slot_index`                  | `int`                             | `no`     | `yes`      | const access to the index of the fired (and thus blinking) clipslot in this t... |
| `fold_state`                        | `bool`                            | `yes`    | `no`       | Get/Set whether the track is folded or not.                                      |
| `group_track`                       | `Track`                           | `no`     | `no`       | return the group track if is_grouped.                                            |
| `has_audio_input`                   | `bool`                            | `no`     | `yes`      | return True, if this Track can be feed with an Audio signal.                     |
| `has_audio_output`                  | `bool`                            | `no`     | `yes`      | return True, if this Track sends out an Audio signal.                            |
| `has_midi_input`                    | `bool`                            | `no`     | `yes`      | return True, if this Track can be feed with an Audio signal.                     |
| `has_midi_output`                   | `bool`                            | `no`     | `yes`      | return True, if this Track sends out MIDI events.                                |
| `implicit_arm`                      | `bool`                            | `yes`    | `yes`      | Arm the track for recording.                                                     |
| `input_meter_left`                  | `float`                           | `no`     | `yes`      | Momentary value of left input channel meter, 0.0 to 1.0.                         |
| `input_meter_level`                 | `float`                           | `no`     | `yes`      | Return the MIDI or Audio meter value of the Tracks input, depending on the ty... |
| `input_meter_right`                 | `float`                           | `no`     | `yes`      | Momentary value of right input channel meter, 0.0 to 1.0.                        |
| `input_routing_channel`             | `RoutingChannel`                  | `yes`    | `yes`      | Get and set the current source channel for input routing.                        |
| `input_routing_type`                | `RoutingType`                     | `yes`    | `yes`      | Get and set the current source type for input routing.                           |
| `input_routings`                    | `tuple[str, Ellipsis]`            | `no`     | `yes`      | Const access to the list of available input routings.                            |
| `input_sub_routings`                | `tuple[str, Ellipsis]`            | `no`     | `yes`      | Return a list of all available input sub routings.                               |
| `is_foldable`                       | `bool`                            | `no`     | `no`       | return True if the track can be (un)folded to hide/reveal contained tracks.      |
| `is_frozen`                         | `bool`                            | `no`     | `yes`      | return True if this Track is currently frozen.                                   |
| `is_grouped`                        | `bool`                            | `no`     | `no`       | return True if this Track is current part of a group track.                      |
| `is_part_of_selection`              | `bool`                            | `no`     | `no`       | return False if the track is not selected.                                       |
| `is_showing_chains`                 | `bool`                            | `yes`    | `yes`      | Get/Set whether a track with a rack device is showing its chains in session v... |
| `is_visible`                        | `bool`                            | `no`     | `no`       | return False if the track is hidden within a folded group track.                 |
| `mixer_device`                      | `MixerDevice`                     | `no`     | `no`       | Return access to the special Device that every Track has: This Device contain... |
| `mute`                              | `bool`                            | `yes`    | `yes`      | Mute/unmute the track.                                                           |
| `muted_via_solo`                    | `bool`                            | `no`     | `yes`      | Returns true if the track is muted because another track is soloed.              |
| `name`                              | `str`                             | `yes`    | `yes`      | Read/write access to the name of the Track, as visible in the track header.      |
| `output_meter_left`                 | `float`                           | `no`     | `yes`      | Momentary value of left output channel meter, 0.0 to 1.0.                        |
| `output_meter_level`                | `float`                           | `no`     | `yes`      | Return the MIDI or Audio meter value of the Track output (behind the mixer_de... |
| `output_meter_right`                | `float`                           | `no`     | `yes`      | Momentary value of right output channel meter, 0.0 to 1.0.                       |
| `output_routing_channel`            | `RoutingChannel`                  | `yes`    | `yes`      | Get and set the current destination channel for output routing.                  |
| `output_routing_type`               | `RoutingType`                     | `yes`    | `yes`      | Get and set the current destination type for output routing.                     |
| `output_routings`                   | `tuple[str, Ellipsis]`            | `no`     | `yes`      | Const access to the list of all available output routings.                       |
| `output_sub_routings`               | `tuple[str, Ellipsis]`            | `no`     | `yes`      | Return a list of all available output sub routings.                              |
| `performance_impact`                | `float`                           | `no`     | `yes`      | Reports the performance impact of this track.                                    |
| `playing_slot_index`                | `int`                             | `no`     | `yes`      | const access to the index of the currently playing clip in the track.            |
| `solo`                              | `bool`                            | `yes`    | `yes`      | Get/Set the solo status of the track.                                            |
| `take_lanes`                        | `tuple`                           | `no`     | `yes`      | returns the take lanes.                                                          |
| `view`                              | `View`                            | `no`     | `no`       | Representing the view aspects of a Track.                                        |

### `arm`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Arm the track for recording. Not available for Main- and Send Tracks.

### `arrangement_clips`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

const access to the list of clips in arrangement viewThe list will be empty for the main, send and group tracks.

### `available_input_routing_channels`

- **Type:** `tuple[RoutingChannel, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of source channels for input routing.

### `available_input_routing_types`

- **Type:** `tuple[RoutingType, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of source types for input routing.

### `available_output_routing_channels`

- **Type:** `tuple[RoutingChannel, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of destination channels for output routing.

### `available_output_routing_types`

- **Type:** `tuple[RoutingType, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of destination types for output routing.

### `back_to_arranger`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Indicates if it's possible to go back to playing back the clips in the Arranger.Setting a value 0 will go back to the Arranger playback. Setting on grouptracks will go back to the Arranger on all grouped tracks.

### `can_be_armed`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Track has a valid arm property. Not all tracks can be armed (for example return Tracks or the Main Tracks).

### `can_be_frozen`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Track can be frozen.

### `can_show_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Track contains a rack instrument device that is capable of showing its chains in session view.

### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the track.

### `clip_slots`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

const access to the list of clipslots (see class AClipSlot) for this track. The list will be empty for the main and sendtracks.

### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the color of the Track (RGB).

### `color_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set access to the color index of the track. Can be None for no color.

### `current_input_routing`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the name of the current active input routing. When setting a new routing, the new routing must be one of the available ones.

### `current_input_sub_routing`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current active input sub routing. When setting a new routing, the new routing must be one of the available ones.

### `current_monitoring_state`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the track's current monitoring state.

### `current_output_routing`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current active output routing. When setting a new routing, the new routing must be one of the available ones.

### `current_output_sub_routing`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the current active output sub routing. When setting a new routing, the new routing must be one of the available ones.

### `devices`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to all available Devices that are present in the Tracks Devicechain. This tuple will also include the 'mixer_device' that every Track always has.

### `fired_slot_index`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

const access to the index of the fired (and thus blinking) clipslot in this track. This index is -1 if no slot is fired and -2 if the track's stop button has been fired.

### `fold_state`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set whether the track is folded or not. Only available if is_foldable is True.

### `group_track`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

return the group track if is_grouped.

### `has_audio_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

return True, if this Track can be feed with an Audio signal. This is true for all Audio Tracks.

### `has_audio_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

return True, if this Track sends out an Audio signal. This is true for all Audio Tracks, and MIDI tracks with an Instrument.

### `has_midi_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

return True, if this Track can be feed with an Audio signal. This is true for all MIDI Tracks.

### `has_midi_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

return True, if this Track sends out MIDI events. This is true for all MIDI Tracks with no Instruments.

### `implicit_arm`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Arm the track for recording. When The track is implicitly armed, it showsin a weaker color in the live GUI and is not saved in the set.

### `input_meter_left`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Momentary value of left input channel meter, 0.0 to 1.0. For Audio Tracks only.

### `input_meter_level`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Return the MIDI or Audio meter value of the Tracks input, depending on the type of the Track input. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.

### `input_meter_right`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Momentary value of right input channel meter, 0.0 to 1.0. For Audio Tracks only.

### `input_routing_channel`

- **Type:** `RoutingChannel`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current source channel for input routing. Raises ValueError if the type isn't one of the current values in available_input_routing_channels.

### `input_routing_type`

- **Type:** `RoutingType`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current source type for input routing. Raises ValueError if the type isn't one of the current values in available_input_routing_types.

### `input_routings`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the list of available input routings.

### `input_sub_routings`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of all available input sub routings.

### `is_foldable`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True if the track can be (un)folded to hide/reveal contained tracks.

### `is_frozen`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

return True if this Track is currently frozen. No changes should be applied to the track's devices or clips while it is frozen.

### `is_grouped`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True if this Track is current part of a group track.

### `is_part_of_selection`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return False if the track is not selected.

### `is_showing_chains`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set whether a track with a rack device is showing its chains in session view.

### `is_visible`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return False if the track is hidden within a folded group track.

### `mixer_device`

- **Type:** `MixerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Return access to the special Device that every Track has: This Device contains the Volume, Pan, Sendamounts, and Crossfade assignment parameters.

### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Mute/unmute the track.

### `muted_via_solo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if the track is muted because another track is soloed.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write access to the name of the Track, as visible in the track header.

### `output_meter_left`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Momentary value of left output channel meter, 0.0 to 1.0. For tracks with audio output only.

### `output_meter_level`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Return the MIDI or Audio meter value of the Track output (behind the mixer_device), depending on the type of the Track input, this can be a MIDI or Audio meter. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.

### `output_meter_right`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Momentary value of right output channel meter, 0.0 to 1.0. For tracks with audio output only.

### `output_routing_channel`

- **Type:** `RoutingChannel`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current destination channel for output routing. Raises ValueError if the channel isn't one of the current values in available_output_routing_channels.

### `output_routing_type`

- **Type:** `RoutingType`
- **Settable:** `yes`
- **Listenable:** `yes`

Get and set the current destination type for output routing. Raises ValueError if the type isn't one of the current values in available_output_routing_types.

### `output_routings`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the list of all available output routings.

### `output_sub_routings`

- **Type:** `tuple[str, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Return a list of all available output sub routings.

### `performance_impact`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Reports the performance impact of this track.

### `playing_slot_index`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

const access to the index of the currently playing clip in the track. Will be -1 when no clip is playing.

### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the solo status of the track. Note that this will not disable the solo state of any other track. If you want exclusive solo, you have to disable the solo state of the other Tracks manually.

### `take_lanes`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

returns the take lanes.

### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a Track.

## Methods

| Method                                                               | Returns     | Description                                                                      |
| -------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------- |
| `create_audio_clip(file_path: str, position: float)`                 | `Clip`      | Creates an audio clip referencing the file at the given path and inserts it i... |
| `create_midi_clip(start_time: float, length: float)`                 | `Clip`      | Creates an empty MIDI clip and inserts it into the arrangement at the specifi... |
| `create_take_lane()`                                                 | `LomObject` | Create a new TakeLane for this track.                                            |
| `delete_clip(slot: Clip)`                                            | `None`      | Delete the given clip.                                                           |
| `delete_device(device: int)`                                         | `None`      | Delete a device identified by the index in the 'devices' list.                   |
| `duplicate_clip_slot(index: int)`                                    | `int`       | Duplicate a clip and put it into the next free slot and return the index of t... |
| `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)` | `Clip`      | Duplicate the given clip into the arrangement of this track at the provided d... |
| `duplicate_device(index: int)`                                       | `None`      | Duplicate a device at a given index in the 'devices' list.                       |
| `get_data(key: str, default_value: Any)`                             | `Any`       | Get data for the given key, that was previously stored using set_data.           |
| `insert_device(DeviceName: str, DeviceIndex: int = -1)`              | `LomObject` | Add a device at a given index in the 'devices' list.                             |
| `jump_in_running_session_clip(beats: float)`                         | `None`      | Jump forward or backward in the currently running Sessionclip (if any) by the... |
| `set_data(key: str, value: Any)`                                     | `None`      | Store data for the given key in this object.                                     |
| `stop_all_clips(Quantized: bool = True)`                             | `None`      | Stop running and triggered clip and slots on this track.                         |

### `create_audio_clip(file_path: str, position: float)`

- **Returns:** `Clip`
- **Args:**
  - `file_path: str`
  - `position: float`

Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.

### `create_midi_clip(start_time: float, length: float)`

- **Returns:** `Clip`
- **Args:**
  - `start_time: float`
  - `length: float`

Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.

### `create_take_lane()`

- **Returns:** `LomObject`

Create a new TakeLane for this track.

### `delete_clip(slot: Clip)`

- **Returns:** `None`
- **Args:**
  - `slot: Clip`

Delete the given clip. Raises a runtime error when the clip belongs to another track.

### `delete_device(device: int)`

- **Returns:** `None`
- **Args:**
  - `device: int`

Delete a device identified by the index in the 'devices' list.

### `duplicate_clip_slot(index: int)`

- **Returns:** `int`
- **Args:**
  - `index: int`

Duplicate a clip and put it into the next free slot and return the index of the destination slot. A new scene is created if no free slot is available. If creating the new scene would exceed the limitations, a runtime error is raised.

### `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)`

- **Returns:** `Clip`
- **Args:**
  - `clip: Clip`
  - `destination_time: float`

Duplicate the given clip into the arrangement of this track at the provided destination time and return it. When the type of the clip and the type of the track are incompatible, a runtime error is raised.

### `duplicate_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Duplicate a device at a given index in the 'devices' list.

### `get_data(key: str, default_value: Any)`

- **Returns:** `Any`
- **Args:**
  - `key: str`
  - `default_value: Any`

Get data for the given key, that was previously stored using set_data.

### `insert_device(DeviceName: str, DeviceIndex: int = -1)`

- **Returns:** `LomObject`
- **Args:**
  - `DeviceName: str`
  - `DeviceIndex: int = -1`

Add a device at a given index in the 'devices' list. At end if -1.

### `jump_in_running_session_clip(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float`

Jump forward or backward in the currently running Sessionclip (if any) by the specified relative amount in beats. Does nothing if no Session Clip is currently running.

### `set_data(key: str, value: Any)`

- **Returns:** `None`
- **Args:**
  - `key: str`
  - `value: Any`

Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

### `stop_all_clips(Quantized: bool = True)`

- **Returns:** `None`
- **Args:**
  - `Quantized: bool = True`

Stop running and triggered clip and slots on this track.

## Enums

### `monitoring_states`

| Value | Name   |
| ----- | ------ |
| `0`   | `IN`   |
| `1`   | `AUTO` |
| `2`   | `OFF`  |

### `DeviceInsertMode`

| Value | Name             |
| ----- | ---------------- |
| `0`   | `default`        |
| `1`   | `selected_left`  |
| `2`   | `selected_right` |
| `3`   | `count`          |

### `RoutingChannelLayout`

| Value | Name     |
| ----- | -------- |
| `0`   | `midi`   |
| `1`   | `mono`   |
| `2`   | `stereo` |

### `RoutingTypeCategory`

| Value | Name                 |
| ----- | -------------------- |
| `0`   | `external`           |
| `1`   | `rewire`             |
| `2`   | `resampling`         |
| `3`   | `master`             |
| `4`   | `track`              |
| `5`   | `parent_group_track` |
| `6`   | `none`               |
| `7`   | `invalid`            |

## DeviceContainer

> `Live.Track.DeviceContainer`

This class is a common super class of Track and Chain

**Live Object:** `yes`

## RoutingChannel

> `Live.Track.RoutingChannel`

This class represents a routing channel.

### Properties

| Property       | Type                   | Settable | Listenable | Description                                         |
| -------------- | ---------------------- | -------- | ---------- | --------------------------------------------------- |
| `display_name` | `str`                  | `no`     | `no`       | Display name of routing channel.                    |
| `layout`       | `RoutingChannelLayout` | `no`     | `no`       | The routing channel's Layout, e.g., mono or stereo. |

#### `display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Display name of routing channel.

#### `layout`

- **Type:** `RoutingChannelLayout`
- **Settable:** `no`
- **Listenable:** `no`

The routing channel's Layout, e.g., mono or stereo.

## RoutingChannelVector

> `Live.Track.RoutingChannelVector`

A container for returning routing channels from Live.

### Methods

| Method                           | Returns | Description |
| -------------------------------- | ------- | ----------- |
| `append(value: RoutingChannel)`  | `None`  |             |
| `extend(values: RoutingChannel)` | `None`  |             |

#### `append(value: RoutingChannel)`

- **Returns:** `None`
- **Args:**
  - `value: RoutingChannel`

#### `extend(values: RoutingChannel)`

- **Returns:** `None`
- **Args:**
  - `values: RoutingChannel`

## RoutingType

> `Live.Track.RoutingType`

This class represents a routing type.

### Properties

| Property          | Type    | Settable | Listenable | Description                                   |
| ----------------- | ------- | -------- | ---------- | --------------------------------------------- |
| `attached_object` | `Track` | `no`     | `no`       | Live object associated with the routing type. |
| `category`        | `int`   | `no`     | `no`       | Category of the routing type.                 |
| `display_name`    | `str`   | `no`     | `no`       | Display name of routing type.                 |

#### `attached_object`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Live object associated with the routing type.

#### `category`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Category of the routing type.

#### `display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Display name of routing type.

## RoutingTypeVector

> `Live.Track.RoutingTypeVector`

A container for returning routing types from Live.

### Methods

| Method                        | Returns | Description |
| ----------------------------- | ------- | ----------- |
| `append(value: RoutingType)`  | `None`  |             |
| `extend(values: RoutingType)` | `None`  |             |

#### `append(value: RoutingType)`

- **Returns:** `None`
- **Args:**
  - `value: RoutingType`

#### `extend(values: RoutingType)`

- **Returns:** `None`
- **Args:**
  - `values: RoutingType`

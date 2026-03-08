# Track

> `Live.Track.Track`

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master
track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.
Not all properties are supported by all types of tracks. The properties are marked accordingly.

??? note "Raw probe notes (temporary)"

    - Current probe set included `midi`, `audio`, `group`, `return`, and `master` tracks (grouped-track layout).
    - Dictionary routing members (`input_routing_type/channel`, `output_routing_type/channel`, and `available_*`) were
      readable and settable on all probed track kinds.
    - On several non-master tracks, `available_output_routing_channels` had only one option, so alternate channel
      selection was not always possible.
    - In current probes, setting track color by known palette values round-trips as expected.
    - In current probes, setting `color` to `None` raised an `InternalError` (C++ type mismatch: expected `int`).
    - In current probes, setting `color_index` to `None` returned OK but had no effect — value read back unchanged.
      Tracks always have a color in the Live UI (no "no color" option), so `None` is not a meaningful value and is
      silently discarded.
    - In current probes, `fired_slot_index` and `playing_slot_index` sentinel behavior matched documented values
      (`-2`, `-1`).
    - In current probes, `current_monitoring_state` accepted values `0`, `1`, `2`; setting `>=3` returned
      `Invalid monitoring state!`.
    - In current probes on a MIDI track, immediate read-after-set matched for `name`, `mute`, `solo`, `color_index`,
      `current_monitoring_state`, and `arm`.
    - Legacy string routing members (`current_*`, `*_routings`, `*_sub_routings`) remain in Live API for compatibility,
      but dictionary routing members are the modern replacement:
        - `current_input_routing` -> `input_routing_type`
        - `current_input_sub_routing` -> `input_routing_channel`
        - `input_routings` -> `available_input_routing_types`
        - `input_sub_routings` -> `available_input_routing_channels`
        - `current_output_routing` -> `output_routing_type`
        - `current_output_sub_routing` -> `output_routing_channel`
        - `output_routings` -> `available_output_routing_types`
        - `output_sub_routings` -> `available_output_routing_channels`

### Open Questions

- Semantic naming for `Track.monitoring_states` values (`0/1/2`) is still unconfirmed from raw docs.
- Full validity/error constraints for routing setters by track type.
- Per-member async visibility behavior for mutable track properties beyond the currently probed subset (which updates
  are immediate vs scheduler-delayed).

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `take_lanes` | `Sequence[TakeLane]` | `list` | `yes` | The list of this track's take lanes. |
| `clip_slots` | `Sequence[ClipSlot]` | `list` | `yes` | The list of clip slots for this track. Empty for main and return tracks. |
| `arrangement_clips` | `Sequence[Clip]` | `list` | `yes` | The list of this track's Arrangement View clips. |
| `devices` | `Sequence[Device]` | `list` | `yes` | Includes mixer device. |
| `group_track` | `Track` | `single` | `no` | The Group Track, if the Track is grouped. |
| `mixer_device` | `MixerDevice` | `single` | `no` | The track's mixer device (Volume, Pan, Sends, Crossfade). |
| `view` | `Track.View` | `single` | `no` | View aspects of the track. |

#### `take_lanes`

- **Returns:** `Sequence[TakeLane]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `12.2`

The list of this track's take lanes.

#### `clip_slots`

- **Returns:** `Sequence[ClipSlot]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of clip slots for this track. The list will be empty for the main and return tracks.

#### `arrangement_clips`

- **Returns:** `Sequence[Clip]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `11.0`

The list of this track's Arrangement View clips. The list is empty for the main track, send/return tracks, and
group tracks.

#### `devices`

- **Returns:** `Sequence[Device]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

Includes mixer device.

#### `group_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The Group Track, if the Track is grouped. If it is not, `id 0` is returned.

#### `mixer_device`

- **Returns:** `MixerDevice`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The special Device that every Track has: contains the Volume, Pan, Send amounts, and Crossfade assignment
parameters.

#### `view`

- **Returns:** `Track.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

Representing the view aspects of a Track.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `arm` | `bool` | `yes` | `yes` | `True` if track is armed for recording. |
| `available_input_routing_channels` | `dictionary` | `no` | `yes` | Available source channels for input routing. |
| `available_input_routing_types` | `dictionary` | `no` | `yes` | Available source types for input routing. |
| `available_output_routing_channels` | `dictionary` | `no` | `yes` | Available target channels for output routing. |
| `available_output_routing_types` | `dictionary` | `no` | `yes` | Available target types for output routing. |
| `back_to_arranger` | `bool` | `yes` | `yes` | State of the Single Track Back to Arrangement button. |
| `can_be_armed` | `bool` | `no` | `no` | `False` for return and master tracks. |
| `can_be_frozen` | `bool` | `no` | `no` | `True` if the track can be frozen. |
| `can_show_chains` | `bool` | `no` | `no` | `True` if an Instrument Rack can show chains in Session View. |
| `canonical_parent` | `LomObject` | `no` | `no` | The canonical parent of the track. |
| `color` | `int` | `yes` | `yes` | Track color as packed RGB `0x00rrggbb`. |
| `color_index` | `int` | `yes` | `yes` | Track color palette index. |
| `current_input_routing` | `str` | `yes` | `yes` | Legacy input routing name. Prefer `input_routing_type`. |
| `current_input_sub_routing` | `str` | `yes` | `yes` | Legacy input sub-routing name. Prefer `input_routing_channel`. |
| `current_monitoring_state` | `int` | `yes` | `yes` | Monitoring state: `0`, `1`, or `2`. |
| `current_output_routing` | `str` | `yes` | `yes` | Legacy output routing name. Prefer `output_routing_type`. |
| `current_output_sub_routing` | `str` | `yes` | `yes` | Legacy output sub-routing name. Prefer `output_routing_channel`. |
| `fired_slot_index` | `int` | `no` | `yes` | Index of the blinking clip slot. |
| `fold_state` | `int` | `yes` | `no` | `0` = unfolded (children visible), `1` = folded. Group tracks only. |
| `has_audio_input` | `bool` | `no` | `no` | `True` for audio tracks. |
| `has_audio_output` | `bool` | `no` | `no` | `True` for audio tracks and MIDI tracks with instruments. |
| `has_midi_input` | `bool` | `no` | `no` | `True` for MIDI tracks. |
| `has_midi_output` | `bool` | `no` | `no` | `True` for MIDI tracks with no instruments and no audio effects. |
| `implicit_arm` | `bool` | `yes` | `yes` | A second arm state, only used by Push so far. |
| `input_meter_left` | `float` | `no` | `yes` | Smoothed left channel input meter, 0.0 to 1.0. Audio input tracks only. |
| `input_meter_level` | `float` | `no` | `yes` | Hold peak of input meter, 0.0 to 1.0. |
| `input_meter_right` | `float` | `no` | `yes` | Smoothed right channel input meter, 0.0 to 1.0. Audio input tracks only. |
| `input_routing_channel` | `dictionary` | `yes` | `yes` | Currently selected input routing source channel. |
| `input_routing_type` | `dictionary` | `yes` | `yes` | Currently selected input routing source type. |
| `input_routings` | `list[str]` | `yes` | `yes` | Legacy input routing list. Prefer `available_input_routing_types`. |
| `input_sub_routings` | `list[str]` | `yes` | `yes` | Legacy input sub-routing list. Prefer `available_input_routing_channels`. |
| `is_foldable` | `bool` | `no` | `no` | `True` if the track can be folded (Group Tracks). |
| `is_frozen` | `bool` | `no` | `yes` | `True` if the track is currently frozen. |
| `is_grouped` | `bool` | `no` | `no` | `True` if the track is inside a Group Track. |
| `is_part_of_selection` | `bool` | `no` | `no` | Unknown. |
| `is_showing_chains` | `bool` | `yes` | `yes` | Whether an Instrument Rack's chains are showing in Session View. |
| `is_visible` | `bool` | `no` | `no` | `False` if hidden in a folded Group Track. |
| `mute` | `bool` | `yes` | `yes` | Track mute state. Not available on master track. |
| `muted_via_solo` | `bool` | `no` | `yes` | `True` if muted because another track is soloed. |
| `name` | `str` | `yes` | `yes` | Track name as shown in the track header. |
| `output_meter_left` | `float` | `no` | `yes` | Smoothed left channel output meter, 0.0 to 1.0. |
| `output_meter_level` | `float` | `no` | `yes` | Hold peak of output meter, 0.0 to 1.0. |
| `output_meter_right` | `float` | `no` | `yes` | Smoothed right channel output meter, 0.0 to 1.0. |
| `output_routing_channel` | `dictionary` | `yes` | `yes` | Currently selected output routing target channel. |
| `output_routing_type` | `dictionary` | `yes` | `yes` | Currently selected output routing target type. |
| `output_routings` | `list[str]` | `yes` | `yes` | Legacy output routing list. Prefer `available_output_routing_types`. |
| `output_sub_routings` | `list[str]` | `yes` | `yes` | Legacy output sub-routing list. Prefer `available_output_routing_channels`. |
| `performance_impact` | `float` | `no` | `yes` | Performance impact of this track. |
| `playing_slot_index` | `int` | `no` | `yes` | Index of the currently playing clip slot. |
| `solo` | `bool` | `yes` | `yes` | Track solo state. Bypasses exclusive solo logic on set. |

#### `arm`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track is armed for recording. Not available on return/master tracks.

#### `available_input_routing_channels`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source channels for the track's input routing, as a dictionary containing a list of
dictionaries (same structure as `input_routing_channel`). Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks.

#### `available_input_routing_types`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source types for the track's input routing, as a dictionary containing a list of dictionaries
(same structure as `input_routing_type`). Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks.

#### `available_output_routing_channels`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available target channels for the track's output routing, as a dictionary containing a list of
dictionaries (same structure as `output_routing_channel`). Documented as unavailable on master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well. On several non-master
  tracks, only one output channel option was available.

#### `available_output_routing_types`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available target types for the track's output routing, as a dictionary containing a list of dictionaries
(same structure as `output_routing_type`). Documented as unavailable on master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well.

#### `back_to_arranger`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `12.0`

Get/set the current state of the Single Track Back to Arrangement button (`1` = highlighted). Setting to `0` makes
Live go back to playing the track's arrangement content. For group tracks, this means all tracks within the group
and any subgroups will go back to playing the arrangement.

#### `can_be_armed`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`False` for return and master tracks.

#### `can_be_frozen`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track can be frozen.

#### `can_show_chains`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track contains an Instrument Rack device that can show chains in Session View.

#### `canonical_parent`

- **Type:** `LomObject`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the track.

#### `color`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The RGB value of the track's color in the form `0x00rrggbb`. When setting, Live snaps to the nearest color from
the track color chooser.

- **Quirks:** Setting to `None` raises an `InternalError` (C++ type mismatch: expected `int`).

#### `color_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Track color palette index. Tracks always have a color in the Live UI — there is no "no color" option.

- **Quirks:** Setting to `None` is accepted without error but silently discarded; the value remains unchanged.

#### `current_input_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the name of the current active input routing. The new routing must be one of the available ones. Legacy
compatibility property. Prefer `input_routing_type`.

#### `current_input_sub_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active input sub routing. Legacy compatibility property. Prefer `input_routing_channel`.

#### `current_monitoring_state`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The track's current monitoring state. Values `0`, `1`, and `2` are accepted.

- **Quirks:** Setting values `>=3` returns `Invalid monitoring state!`. Semantic labels for `0`/`1`/`2` are
  unconfirmed in raw docs.

#### `current_output_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active output routing. Legacy compatibility property. Prefer `output_routing_type`.

#### `current_output_sub_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active output sub routing. Legacy compatibility property. Prefer `output_routing_channel`.

#### `fired_slot_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Reflects the blinking clip slot. `-1` = no slot fired, `-2` = Clip Stop Button fired. First clip slot has index
`0`. Not available on return/master tracks.

#### `fold_state`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

`0` = tracks within the Group Track are visible, `1` = Group Track is folded and the tracks within are hidden.
Only available if `is_foldable` is `True`.

#### `has_audio_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio tracks.

#### `has_audio_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio tracks and MIDI tracks with instruments.

#### `has_midi_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI tracks.

#### `has_midi_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI tracks with no instruments and no audio effects.

#### `implicit_arm`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

A second arm state, only used by Push so far.

#### `input_meter_left`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio input only.

#### `input_meter_level`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Hold peak value of input meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks it is the maximum of the
left and right channels. The hold time is 1 second.

#### `input_meter_right`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio input only.

#### `input_routing_channel`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source channel for the track's input routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_input_routing_channels`. Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks. Set/get
  round-trip succeeded across all probed track kinds.

#### `input_routing_type`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source type for the track's input routing. A dictionary with `display_name` and `identifier`
keys. Can be set to any value from `available_input_routing_types`. Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks. Set/get
  round-trip succeeded across all probed track kinds.

#### `input_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available input routings. Legacy compatibility property. Prefer `available_input_routing_types`.

#### `input_sub_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available input sub routings. Legacy compatibility property. Prefer `available_input_routing_channels`.

#### `is_foldable`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track can be (un)folded to hide or reveal the contained tracks. This is currently the case for Group
Tracks. Instrument and Drum Racks return `False` although they can be opened/closed.

#### `is_frozen`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track is currently frozen.

#### `is_grouped`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track is contained within a Group Track.

#### `is_part_of_selection`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Unknown.

#### `is_showing_chains`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.

#### `is_visible`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`False` if the track is hidden in a folded Group Track.

#### `mute`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Track mute state. Not available on master track.

#### `muted_via_solo`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track or chain is muted due to Solo being active on at least one other track.

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

As shown in track header.

#### `output_meter_left`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output only. Note
that the left/right audio meters add a significant load to Live GUI resource usage.

#### `output_meter_level`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the maximum of the
left and right channels. The hold time is 1 second.

#### `output_meter_right`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output only.

#### `output_routing_channel`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected target channel for the track's output routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_output_routing_channels`. Documented as unavailable on
master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well. On several non-master
  tracks, only one output channel option was available.

#### `output_routing_type`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected target type for the track's output routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_output_routing_types`. Documented as unavailable on
master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well.

#### `output_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of all available output routings. Legacy compatibility property. Prefer `available_output_routing_types`.

#### `output_sub_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of all available output sub routings. Legacy compatibility property. Prefer
`available_output_routing_channels`.

#### `performance_impact`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.1`

Reports the performance impact of this track.

#### `playing_slot_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

First slot has index `0`. `-2` = Clip Stop slot fired in Session View, `-1` = Arrangement recording with no
Session clip playing. Not available on return/master tracks.

#### `solo`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Track solo state. Not available on master track.

- **Quirks:** When setting this property, the exclusive Solo logic is bypassed — you have to unsolo the other tracks
  yourself.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `create_audio_clip(file_path: str, position: float)` | `Clip` | Create an arrangement audio clip from a file. |
| `create_midi_clip(start_time: float, length: float)` | `Clip` | Create an empty arrangement MIDI clip. |
| `create_take_lane()` | `LomObject` | Create a take lane for this track. |
| `delete_clip(clip: Clip)` | `None` | Delete the given clip. |
| `delete_device(index: int)` | `None` | Delete the device at the given index. |
| `duplicate_clip_slot(index: int)` | `int` | Duplicate a clip slot (like context menu Duplicate). |
| `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)` | `Clip` | Duplicate a clip to the Arrangement at the given time. |
| `duplicate_device(index: int)` | `None` | Duplicate a device at the given index. |
| `get_data(key: object, default_value: object)` | `object` | Get persistent data for the given key. |
| `insert_device(device_name: str, device_index: int)` | `LomObject` | Insert a native device at the given index. |
| `jump_in_running_session_clip(beats: float)` | `None` | Relative jump in the running session clip. |
| `set_data(key: object, value: object)` | `None` | Store persistent data for the given key. |
| `stop_all_clips(quantized: bool)` | `None` | Stop all playing and fired clips in this track. |

#### `create_audio_clip(file_path: str, position: float)`

- **Returns:** `Clip`
- **Args:**
  - `file_path: str` -- absolute path to a valid audio file
  - `position: float` -- arrangement position in beats (range `[0, 1576800]`)
- **Since:** `11.3`

Creates an audio clip referencing the file at the specified position in the arrangement view. Errors if the track is
not audio, is frozen, or is being recorded into. See `ClipSlot.create_audio_clip` for session view clips.

#### `create_midi_clip(start_time: float, length: float)`

- **Returns:** `Clip`
- **Args:**
  - `start_time: float` -- arrangement position in beats (range `[0, 1576800]`)
  - `length: float` -- clip length in beats
- **Since:** `12.1`

Creates an empty MIDI clip in the arrangement at the specified time. Errors on non-MIDI tracks, frozen tracks, or
tracks being recorded into. See `ClipSlot.create_clip` for session view clips.

#### `create_take_lane()`

- **Returns:** `LomObject`
- **Args:** None
- **Since:** `12.2`

Creates a take lane for this track.

#### `delete_clip(clip: Clip)`

- **Returns:** `None`
- **Args:**
  - `clip: Clip` -- the clip to delete
- **Since:** `<11`

Delete the given clip.

#### `delete_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- device index to delete
- **Since:** `<11`

Delete the device at the given index.

#### `duplicate_clip_slot(index: int)`

- **Returns:** `int`
- **Args:**
  - `index: int` -- clip slot index to duplicate
- **Since:** `<11`

Works like 'Duplicate' in a clip's context menu.

#### `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)`

- **Returns:** `Clip`
- **Args:**
  - `clip: Clip` -- the clip to duplicate
  - `destination_time: float` -- arrangement position in beats
- **Since:** `<11`

Duplicate the given clip to the Arrangement, placing it at the given destination time in beats.

#### `duplicate_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- device index to duplicate
- **Since:** `12.3`

Duplicate a device at the given index in the device chain.

#### `get_data(key: object, default_value: object)`

- **Returns:** `object`
- **Args:**
  - `key: object` -- the key to look up
  - `default_value: object` -- returned if the key was never set
- **Since:** `<11`

Get data for the given key, that was previously stored using `set_data`. Data is persistent across save/load.

- **Quirks:** After `set_data(key, None)`, `get_data(key, default)` returns `None` rather than the provided
  default.

#### `insert_device(device_name: str, device_index: int)`

- **Returns:** `LomObject`
- **Args:**
  - `device_name: str` -- exact `class_display_name` (e.g. `"EQ Eight"`, not `"Eq8"`); case-sensitive
  - `device_index: int` -- position in the device chain (optional; defaults to end)
- **Raises:** `ValidationError: Device {name} not found.` if the name doesn't match any native device.
- **Since:** `12.3`

Inserts a native Live device at the given index. Only native devices are supported — third-party plug-ins (VST/AU)
and Max for Live devices are not (the empty M4L container shell can be inserted as it is native). Not all indices
are valid; structural constraints apply (e.g., a MIDI effect cannot be inserted after an instrument).

#### `jump_in_running_session_clip(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- amount to jump relative to the current clip position
- **Since:** `<11`

Modify playback position in the running Session clip on this track, if any.

#### `set_data(key: object, value: object)`

- **Returns:** `None`
- **Args:**
  - `key: object` -- the key to store under
  - `value: object` -- the value to store
- **Since:** `<11`

Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

#### `stop_all_clips(quantized: bool)`

- **Returns:** `None`
- **Args:**
  - `quantized: bool` -- `False` stops immediately, `True` (default) respects launch quantization
- **Since:** `<11`

Stops all playing and fired clips in this track.

---

## Track.View

> `Live.Track.Track.View`

Representing the view aspects of a track.

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `selected_device` | `Device` | `single` | `yes` | The selected device (or first in a multi-selection). |

#### `selected_device`

- **Returns:** `Device`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The selected device or the first selected device (in case of multi/group selection).

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `canonical_parent` | `Track` | `no` | `no` | The canonical parent of the track view. |
| `device_insert_mode` | `int` | `yes` | `yes` | Where a device is inserted when loaded from the browser. |
| `is_collapsed` | `bool` | `yes` | `yes` | In Arrangement View: `True` = track collapsed. |

#### `canonical_parent`

- **Type:** `Track`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the track view.

#### `device_insert_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Determines where a device will be inserted when loaded from the browser. `0` = add at end, `1` = left of selected
device, `2` = right of selected device.

#### `is_collapsed`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

In Arrangement View: `True` = track collapsed, `False` = track opened.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `select_instrument()` | `bool` | Select the track's instrument or first device. |

#### `select_instrument()`

- **Returns:** `bool` -- `False` if there are no devices to select
- **Args:** None
- **Since:** `<11`

Selects the track's instrument or first device, makes it visible and focuses on it.

---

## Track.DeviceContainer

> `Live.Track.Track.DeviceContainer`

Common super class of Track and Chain. No user-facing properties or methods beyond the internal `_live_ptr`.

---

## Track.DeviceInsertMode

> `Live.Track.Track.DeviceInsertMode`

Enumeration used by `Track.View.device_insert_mode`. Values: `0` = add at end, `1` = insert left of selected
device, `2` = insert right of selected device.

---

## Track.RoutingChannel

> `Live.Track.Track.RoutingChannel`

Represents a routing channel with `display_name` and `layout` properties.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `display_name` | `str` | `no` | `no` | Display name of the routing channel. |
| `layout` | `Track.RoutingChannelLayout` | `no` | `no` | The channel layout (e.g., mono or stereo). |

#### `display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Display name of the routing channel.

#### `layout`

- **Type:** `Track.RoutingChannelLayout`
- **Listenable:** `no`
- **Since:** `<11`

The routing channel's layout, e.g., mono or stereo.

---

## Track.RoutingChannelLayout

> `Live.Track.Track.RoutingChannelLayout`

Enumeration for routing channel layout (e.g., mono/stereo).

---

## Track.RoutingChannelVector

> `Live.Track.Track.RoutingChannelVector`

A container for returning routing channels from Live. Supports `append()` and `extend()`.

---

## Track.RoutingType

> `Live.Track.Track.RoutingType`

Represents a routing type with `attached_object`, `category`, and `display_name` properties.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `attached_object` | `LomObject` | `no` | `no` | Live object associated with the routing type. |
| `category` | `Track.RoutingTypeCategory` | `no` | `no` | Category of the routing type. |
| `display_name` | `str` | `no` | `no` | Display name of the routing type. |

#### `attached_object`

- **Type:** `LomObject`
- **Listenable:** `no`
- **Since:** `<11`

Live object associated with the routing type.

#### `category`

- **Type:** `Track.RoutingTypeCategory`
- **Listenable:** `no`
- **Since:** `<11`

Category of the routing type.

#### `display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Display name of the routing type.

---

## Track.RoutingTypeCategory

> `Live.Track.Track.RoutingTypeCategory`

Enumeration for routing type categories.

---

## Track.RoutingTypeVector

> `Live.Track.Track.RoutingTypeVector`

A container for returning routing types from Live. Supports `append()` and `extend()`.

---

## Track.monitoring_states

> `Live.Track.Track.monitoring_states`

Enumeration used by `Track.current_monitoring_state`. Values `0`, `1`, `2` are accepted; `>=3` returns
`Invalid monitoring state!`. Semantic labels for the three states are unconfirmed in raw docs.

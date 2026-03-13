## Unresolved Items

```json
[
  {
    "path": "Live.Track.DeviceContainer._live_ptr",
    "kind": "property_type",
    "current_type": null
  },
  {
    "path": "Live.Track.RoutingChannelVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingChannel",
    "signature": "append( (RoutingChannelVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingChannelVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingChannel",
    "signature": "extend( (RoutingChannelVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingTypeVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingType",
    "signature": "append( (RoutingTypeVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingTypeVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingType",
    "signature": "extend( (RoutingTypeVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.create_audio_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "str",
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)"
  },
  {
    "path": "Live.Track.Track.create_audio_clip",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)"
  },
  {
    "path": "Live.Track.Track.create_midi_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)"
  },
  {
    "path": "Live.Track.Track.create_midi_clip",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)"
  },
  {
    "path": "Live.Track.Track.delete_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "Clip",
    "description": "Delete the given clip. Raises a runtime error when the clip belongs to another track.",
    "signature": "delete_clip( (Track)arg1, (Clip)arg2) -> None :",
    "cpp_signature": "void delete_clip(TTrackPyHandle,TPyHandle<AClip>)"
  },
  {
    "path": "Live.Track.Track.delete_device",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Delete a device identified by the index in the 'devices' list.",
    "signature": "delete_device( (Track)arg1, (int)arg2) -> None :",
    "cpp_signature": "void delete_device(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.duplicate_clip_slot",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Duplicate a clip and put it into the next free slot and return the index\nof the destination slot. A new scene is created if no free slot is\navailable. If creating the new scene would exceed the limitations,\na runtime error is raised.",
    "signature": "duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :",
    "cpp_signature": "int duplicate_clip_slot(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.duplicate_device",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Duplicate a device at a given index in the 'devices' list.",
    "signature": "duplicate_device( (Track)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_device(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.get_data",
    "kind": "arg_type",
    "arg_name": "default_value",
    "current_type": "object",
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.get_data",
    "kind": "return_type",
    "current_type": "object",
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.jump_in_running_session_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Jump forward or backward in the currently running Sessionclip (if any)\nby the specified relative amount in beats. Does nothing if no Session Clip\nis currently running.",
    "signature": "jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :",
    "cpp_signature": "void jump_in_running_session_clip(TTrackPyHandle,double)"
  },
  {
    "path": "Live.Track.Track.set_data",
    "kind": "arg_type",
    "arg_name": "value",
    "current_type": "object",
    "description": "Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.",
    "signature": "set_data( (Track)arg1, (object)key, (object)value) -> None :",
    "cpp_signature": "void set_data(TTrackPyHandle,TString,boost::python::api::object)"
  }
]
```

## MaxForLive Documentation

These are the official Ableton MaxForLive docs for the Live Object Model. Use them to find parameter names, types, and descriptions.

### device.md

# Device

This class represents a MIDI or audio device in Live.

## Canonical Paths

```
live_set tracks N devices M
```

```
live_set tracks N devices M chains L devices K
```

```
live_set tracks N devices M return_chains L devices K
```

## Children

### parameters list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

Only automatable parameters are accessible. See [DeviceParameter](#DeviceParameter) to learn how to modify them.

### view [Device.View](/apiref/lom/device_view/ "Device.View") read-only

## Properties

### can_have_chains bool read-only

0 for a single device   
1 for a device Rack

### can_have_drum_pads bool read-only

1 for Drum Racks

### class_display_name symbol read-only

Get the original name of the device (e.g. `Operator`, `Auto Filter`).

### class_name symbol read-only

Live device type such as `MidiChord`, `Operator`, `Limiter`, `MxDeviceAudioEffect`, or `PluginDevice`.

### is_active bool read-onlyobserve

0 = either the device itself or its enclosing Rack device is off.

### name symbol observe

This is the string shown in the title bar of the device.

### type int read-only

The type of the device. Possible types are: 0 = undefined, 1 = instrument, 2 = audio_effect, 4 = midi_effect.

### latency_in_samples int read-onlyobserve

Device latency in samples.

### latency_in_ms float read-onlyobserve

Device latency in milliseconds.

### can_compare_ab bool read-only

1 for devices that support the AB Compare feature. 0 otherwise.   
  
*Available since Live 12.3.*

### is_using_compare_preset_b bool observe

1 if the device has compare preset B loaded. 0 otherwise.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*

## Functions

### store_chosen_bank

Parameters:   
`script_index` [int]   
`bank_index` [int]   
(This is related to hardware control surfaces and is usually not relevant.)

### save_preset_to_compare_ab_slot

Save the device state to the other compare AB slot.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*


### track.md

# Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.   
  
Not all properties are supported by all types of tracks. The properties are marked accordingly.

## Canonical Path

```
live_set tracks N
```

## Children

### take_lanes list of [TakeLane](/apiref/lom/takelane/ "TakeLane") read-onlyobserve

The list of this track's take lanes

### clip_slots list of [ClipSlot](/apiref/lom/clipslot/ "ClipSlot") read-onlyobserve

### arrangement_clips list of [Clip](/apiref/lom/clip/ "Clip") read-onlyobserve

The list of this track's Arrangement View clip IDs   
  
*Available since Live 11.0.*

### devices list of [Device](/apiref/lom/device/ "Device") read-onlyobserve

Includes mixer device.

### group_track [Track](/apiref/lom/track/ "Track") read-only

The Group Track, if the Track is grouped. If it is not, *id 0* is returned.

### mixer_device [MixerDevice](/apiref/lom/mixerdevice/ "MixerDevice") read-only

### view [Track.View](/apiref/lom/track_view/ "Track.View") read-only

## Properties

### arm bool observe

1 = track is armed for recording. [not in return/master tracks]

### available_input_routing_channels dictionary read-onlyobserve

The list of available source channels for the track's input routing. It's represented as a *dictionary* with the following key:  
`available_input_routing_channels` [list]   
The list contains *dictionaries* as described in *input_routing_channel*.   
Only available on MIDI and audio tracks.

### available_input_routing_types dictionary read-onlyobserve

The list of available source types for the track's input routing. It's represented as a *dictionary* with the following key:  
`available_input_routing_types` [list]   
The list contains *dictionaries* as described in *input_routing_type*.   
Only available on MIDI and audio tracks.

### available_output_routing_channels dictionary read-onlyobserve

The list of available target channels for the track's output routing. It's represented as a *dictionary* with the following key:  
`available_output_routing_channels` [list]   
The list contains *dictionaries* as described in *output_routing_channel*.   
Not available on the master track.

### available_output_routing_types dictionary read-onlyobserve

The list of available target types for the track's output routing. It's represented as a *dictionary* with the following key:  
`available_output_routing_types` [list]   
The list contains *dictionaries* as described in *output_routing_type*.   
Not available on the master track.

### back_to_arranger bool observe

Get/set/observe the current state of the Single Track Back to Arrangement button (1 = highlighted). This button is used to indicate that the current state of the playback differs from what is stored in the Arrangement.   
  
Setting this property to 0 will make Live go back to playing the track's arrangement content. For group tracks, this means that all of the tracks that belong to the group and any subgroups will go back to playing the arrangement.

### can_be_armed bool read-only

0 for return and master tracks.

### can_be_frozen bool read-only

1 = the track can be frozen, 0 = otherwise.

### can_show_chains bool read-only

1 = the track contains an Instrument Rack device that can show chains in Session View.

### color int observe

The RGB value of the track's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).   
  
When setting the RGB value, the nearest color from the track color chooser is taken.

### color_index long observe

The color index of the track.

### fired_slot_index int read-onlyobserve

Reflects the blinking clip slot.   
-1 = no slot fired, -2 = Clip Stop Button fired   
First clip slot has index 0.   
[not in return/master tracks]

### fold_state int

0 = tracks within the Group Track are visible, 1 = Group Track is folded and the tracks within the Group Track are hidden   
[only available if `is_foldable` = 1]

### has_audio_input bool read-only

1 for audio tracks.

### has_audio_output bool read-only

1 for audio tracks and MIDI tracks with instruments.

### has_midi_input bool read-only

1 for MIDI tracks.

### has_midi_output bool read-only

1 for MIDI tracks with no instruments and no audio effects.

### implicit_arm bool observe

A second arm state, only used by Push so far.

### input_meter_left float read-onlyobserve

Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters put a significant load onto the GUI part of Live.

### input_meter_level float read-onlyobserve

Hold peak value of input meters of audio and MIDI tracks, 0.0 ... 1.0. For audio tracks it is the maximum of the left and right channels. The hold time is 1 second.

### input_meter_right float read-onlyobserve

Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### input_routing_channel dictionary observe

The currently selected source channel for the track's input routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_input_routing_channels*.   
Only available on MIDI and audio tracks.

### input_routing_type dictionary observe

The currently selected source type for the track's input routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_input_routing_types*.   
Only available on MIDI and audio tracks.

### is_foldable bool read-only

1 = track can be (un)folded to hide or reveal the contained tracks. This is currently the case for Group Tracks. Instrument and Drum Racks return 0 although they can be opened/closed. This will be fixed in a later release.

### is_frozen bool read-onlyobserve

1 = the track is currently frozen.

### is_grouped bool read-only

1 = the track is contained within a Group Track.

### is_part_of_selection bool read-only

### is_showing_chains bool observe

Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.

### is_visible bool read-only

0 = track is hidden in a folded Group Track.

### mute bool observe

[not in master track]

### muted_via_solo bool read-onlyobserve

1 = the track or chain is muted due to Solo being active on at least one other track.

### name symbol observe

As shown in track header.

### output_meter_left float read-onlyobserve

Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters add a significant load to Live GUI resource usage.

### output_meter_level float read-onlyobserve

Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the maximum of the left and right channels. The hold time is 1 second.

### output_meter_right float read-onlyobserve

Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### performance_impact float read-onlyobserve

Reports the performance impact of this track.

### output_routing_channel dictionary observe

The currently selected target channel for the track's output routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_output_routing_channels*.   
Not available on the master track.

### output_routing_type dictionary observe

The currently selected target type for the track's output routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_output_routing_types*.   
Not available on the master track.

### playing_slot_index int read-onlyobserve

First slot has index 0, -2 = Clip Stop slot fired in Session View, -1 = Arrangement recording with no Session clip playing. [not in return/master tracks]

### solo bool observe

Remark: when setting this property, the exclusive Solo logic is bypassed, so you have to unsolo the other tracks yourself. [not in master track]

## Functions

### create_audio_clip

Parameters:   
`file_path` [symbol]   
`position` [float]   
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at the specified position in the arrangement view. Prints an error if the track is not an audio track, if the track is frozen, or if the track is being recorded into. The position must be within the range [0., 1576800].   
  
See the `ClipSlot.create_audio_clip` function if you need to create audio clips in session view instead.

### create_midi_clip

Parameters:   
`start_time` [float]   
`length` [float]   
Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.   
  
See the `ClipSlot.create_clip` function if you need to create audio clips in session view instead.

### create_take_lane

Creates a take lane for this track.

### delete_clip

Parameter: `clip`  
Delete the given clip.

### delete_device

Parameter: `index`  
Delete the device at the given index.

### duplicate_clip_slot

Parameter: `index`  
  
Works like 'Duplicate' in a clip's context menu.

### duplicate_clip_to_arrangement

Parameters: ``` clip``destination_time ``` [float]   
  
Duplicate the given clip to the Arrangement, placing it at the given *destination_time* in beats.

### insert_device

Parameters: `device_name` [symbol] `target_index` [int] (optional)   
  
Attempts to insert the device specified by `device_name` at the given index in the track's device chain. If no index is provided, attempts to insert the device at the end of the chain. Throws an error if insertion is not possible.   
`device_name` is the name as it appears in the UI of Live.   
Not all indices are valid. As can be expected, indices outside of the range defined by the current length of the device chain are invalid, but there are other limitations: for example, a MIDI effect can't be inserted after an instrument. The rule of thumb is that if an index would be invalid when inserting using the mouse, it's invalid here.   
  
At the moment, only native Live devices can be inserted. Max for Live devices and plug-in are not supported.   
  
*Available since Live 12.3.*

### jump_in_running_session_clip

Parameter: `beats`  
  
`beats` [float] is the amount to jump relatively to the current clip position.   
Modify playback position in running Session clip, if any.

### stop_all_clips

Stops all playing and fired clips in this track.


### track_view.md

# Track.View

Representing the view aspects of a track.

## Canonical Path

```
live_set tracks N view
```

## Children

### selected_device [Device](/apiref/lom/device/ "Device") read-onlyobserve

The selected device or the first selected device (in case of multi/group selection).

## Properties

### device_insert_mode int observe

Determines where a device will be inserted when loaded from the browser. 0 = add device at the end, 1 = add device to the left of the selected device, 2 = add device to the right of the selected device.

### is_collapsed bool observe

In Arrangement View: 1 = track collapsed, 0 = track opened.

## Functions

### select_instrument

Returns: bool 0 = there are no devices to select   
Selects track's instrument or first device, makes it visible and focuses on it.


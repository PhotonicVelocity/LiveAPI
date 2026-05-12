---
module: Track
---

Represents an audio, MIDI, return, or main track in a Live Set. The `Track`
class hosts the track's clip slots, devices, mixer, and routing — not all
properties are supported by every track type, and individual members are
marked accordingly.

## Classes

### Track

```yaml
kind: class
path: Live.Track.Track
ancestors:
- Live.Track.DeviceContainer
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: |-
  This class represents a track in Live. It can be either an Audio
  track, a MIDI Track, a Return Track or the Main track. The Main
  Track and at least one Audio or MIDI track will be always present.
  Return Tracks are optional.
```

#### Properties

##### arm

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Arm the track for recording. Not available for Main- and Send Tracks.
```

##### arrangement_clips

```yaml
kind: property
type: Live.Base.Vector[Live.Clip.Clip]
settable: false
listenable: true
raw_doc: const access to the list of clips in arrangement viewThe list will be empty for the main, send and group tracks.
```

##### available_input_routing_channels

```yaml
kind: property
type: Live.Track.RoutingChannelVector
settable: false
listenable: true
raw_doc: Return a list of source channels for input routing.
```

##### available_input_routing_types

```yaml
kind: property
type: Live.Track.RoutingTypeVector
settable: false
listenable: true
raw_doc: Return a list of source types for input routing.
```

##### available_output_routing_channels

```yaml
kind: property
type: Live.Track.RoutingChannelVector
settable: false
listenable: true
raw_doc: Return a list of destination channels for output routing.
```

##### available_output_routing_types

```yaml
kind: property
type: Live.Track.RoutingTypeVector
settable: false
listenable: true
raw_doc: Return a list of destination types for output routing.
```

##### back_to_arranger

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Indicates if it's possible to go back to playing back the clips in the Arranger.Setting a value 0 will go back to
  the Arranger playback. Setting on grouptracks will go back to the Arranger on all grouped tracks.
```

##### can_be_armed

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Track has a valid arm property. Not all tracks
  can be armed (for example return Tracks or the Main Tracks).
```

##### can_be_frozen

```yaml
kind: property
type: bool
settable: false
raw_doc: return True, if this Track can be frozen.
```

##### can_show_chains

```yaml
kind: property
type: bool
settable: false
raw_doc: return True, if this Track contains a rack instrument device that is capable of showing its chains in session view.
```

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the track.
```

##### clip_slots

```yaml
kind: property
type: Live.Base.Vector[Live.ClipSlot.ClipSlot]
settable: false
listenable: true
raw_doc: |-
  const access to the list of clipslots (see class AClipSlot) for this track.
  The list will be empty for the main and sendtracks.
```

##### color

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/set access to the color of the Track (RGB).
```

##### color_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set access to the color index of the track. Can be None for no color.
```

##### current_input_routing

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: |-
  Get/Set the name of the current active input routing.
  When setting a new routing, the new routing must be one of the available ones.
```

##### current_input_sub_routing

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: |-
  Get/Set the current active input sub routing.
  When setting a new routing, the new routing must be one of the available ones.
```

##### current_monitoring_state

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/Set the track's current monitoring state.
```

##### current_output_routing

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: |-
  Get/Set the current active output routing.
  When setting a new routing, the new routing must be one of the available ones.
```

##### current_output_sub_routing

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: |-
  Get/Set the current active output sub routing.
  When setting a new routing, the new routing must be one of the available ones.
```

##### devices

```yaml
kind: property
type: Live.Base.Vector[Live.Device.Device]
settable: false
listenable: true
raw_doc: |-
  Return const access to all available Devices that are present in the Tracks
  Devicechain. This tuple will also include the 'mixer_device' that every Track
  always has.
```

##### fired_slot_index

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: |-
  const access to the index of the fired (and thus blinking) clipslot in this track.
  This index is -1 if no slot is fired and -2 if the track's stop button has been fired.
```

##### fold_state

```yaml
kind: property
type: bool
settable: true
raw_doc: Get/Set whether the track is folded or not. Only available if is_foldable is True.
```

##### group_track

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: return the group track if is_grouped.
```

##### has_audio_input

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  return True, if this Track can be feed with an Audio signal. This is
  true for all Audio Tracks.
```

##### has_audio_output

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  return True, if this Track sends out an Audio signal. This is
  true for all Audio Tracks, and MIDI tracks with an Instrument.
```

##### has_midi_input

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  return True, if this Track can be feed with an Audio signal. This is
  true for all MIDI Tracks.
```

##### has_midi_output

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  return True, if this Track sends out MIDI events. This is
  true for all MIDI Tracks with no Instruments.
```

##### implicit_arm

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Arm the track for recording. When The track is implicitly armed, it showsin a weaker color in the live GUI and is
  not saved in the set.
```

##### input_meter_left

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Momentary value of left input channel meter, 0.0 to 1.0. For Audio Tracks only.
```

##### input_meter_level

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Return the MIDI or Audio meter value of the Tracks input, depending on the
  type of the Track input. Meter values (MIDI or Audio) are always scaled
  from 0.0 to 1.0.
```

##### input_meter_right

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Momentary value of right input channel meter, 0.0 to 1.0. For Audio Tracks only.
```

##### input_routing_channel

```yaml
kind: property
type: Live.Track.RoutingChannel
settable: true
listenable: true
raw_doc: |-
  Get and set the current source channel for input routing.
  Raises ValueError if the type isn't one of the current values in
  available_input_routing_channels.
```

##### input_routing_type

```yaml
kind: property
type: Live.Track.RoutingType
settable: true
listenable: true
raw_doc: |-
  Get and set the current source type for input routing.
  Raises ValueError if the type isn't one of the current values in
  available_input_routing_types.
```

##### input_routings

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Const access to the list of available input routings.
```

##### input_sub_routings

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return a list of all available input sub routings.
```

##### is_foldable

```yaml
kind: property
type: bool
settable: false
raw_doc: return True if the track can be (un)folded to hide/reveal contained tracks.
```

##### is_frozen

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: return True if this Track is currently frozen. No changes should be applied to the track's devices or clips while
  it is frozen.
```

##### is_grouped

```yaml
kind: property
type: bool
settable: false
raw_doc: return True if this Track is current part of a group track.
```

##### is_part_of_selection

```yaml
kind: property
type: bool
settable: false
raw_doc: return False if the track is not selected.
```

##### is_showing_chains

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set whether a track with a rack device is showing its chains in session view.
```

##### is_visible

```yaml
kind: property
type: bool
settable: false
raw_doc: return False if the track is hidden within a folded group track.
```

##### mixer_device

```yaml
kind: property
type: Live.MixerDevice.MixerDevice
settable: false
raw_doc: |-
  Return access to the special Device that every Track has: This Device contains
  the Volume, Pan, Sendamounts, and Crossfade assignment parameters.
```

##### mute

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Mute/unmute the track.
```

##### muted_via_solo

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if the track is muted because another track is soloed.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write access to the name of the Track, as visible in the track header.
```

##### output_meter_left

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Momentary value of left output channel meter, 0.0 to 1.0.
  For tracks with audio output only.
```

##### output_meter_level

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Return the MIDI or Audio meter value of the Track output (behind the
  mixer_device), depending on the type of the Track input, this can be a MIDI
  or Audio meter. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.
```

##### output_meter_right

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Momentary value of right output channel meter, 0.0 to 1.0.
  For tracks with audio output only.
```

##### output_routing_channel

```yaml
kind: property
type: Live.Track.RoutingChannel
settable: true
listenable: true
raw_doc: |-
  Get and set the current destination channel for output routing.
  Raises ValueError if the channel isn't one of the current values in
  available_output_routing_channels.
```

##### output_routing_type

```yaml
kind: property
type: Live.Track.RoutingType
settable: true
listenable: true
raw_doc: |-
  Get and set the current destination type for output routing.
  Raises ValueError if the type isn't one of the current values in
  available_output_routing_types.
```

##### output_routings

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Const access to the list of all available output routings.
```

##### output_sub_routings

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return a list of all available output sub routings.
```

##### performance_impact

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Reports the performance impact of this track.
```

##### playing_slot_index

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: |-
  const access to the index of the currently playing clip in the track.
  Will be -1 when no clip is playing.
```

##### solo

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the solo status of the track. Note that this will not disable the
  solo state of any other track. If you want exclusive solo, you have to
  disable the solo state of the other Tracks manually.
```

##### take_lanes

```yaml
kind: property
type: Live.Base.Vector[Live.TakeLane.TakeLane]
settable: false
listenable: true
raw_doc: returns the take lanes.
```

##### view

```yaml
kind: property
type: Live.Track.Track.View
settable: false
raw_doc: Representing the view aspects of a Track.
```

##### data

```yaml
kind: property
listenable: true
```

Fires when the track's underlying data store is modified —
the generic state-change signal for the track's persistent
state. The programmatic trigger is `set_data` (read via
`get_data`); whether other track-level mutations also fire
it is **unverified**.

#### Methods

##### create_audio_clip

```yaml
kind: method
signature: 'create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)
args:
- name: file_path
  type: str
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `file_path`.'
- name: position
  type: float
  refinement:
    name:
      probed: arg3
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `position`.'
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.
  Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
```

##### create_midi_clip

```yaml
kind: method
signature: 'create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)
args:
- name: start_time
  type: float
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `start_time`.'
- name: length
  type: float
  refinement:
    name:
      probed: arg3
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `length`.'
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an empty MIDI clip and inserts it into the arrangement at the specified time.
  Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
```

##### create_take_lane

```yaml
kind: method
signature: 'create_take_lane( (Track)arg1) -> LomObject :'
cpp_signature: TWeakPtr<TPyHandleBase> create_take_lane(TTrackPyHandle)
returns:
  type: Live.TakeLane.TakeLane
  refinement:
    type:
      probed: Live.LomObject.LomObject
      confidence: high
      sources:
      - '[C++ signature] returns `TWeakPtr<TPyHandleBase>` (generic LomObject) — no specific type enforced.'
      - '[docstring] "Create a new TakeLane for this track" names the type.'
      - '[probe] `track.take_lanes` element_repr is `<class ''TakeLane.TakeLane''>` — the runtime returns TakeLane instances
        when iterated, matching the create return.'
raw_doc: Create a new TakeLane for this track.
```

##### delete_clip

```yaml
kind: method
signature: 'delete_clip( (Track)arg1, (Clip)arg2) -> None :'
cpp_signature: void delete_clip(TTrackPyHandle,TPyHandle<AClip>)
args:
- name: clip
  type: Live.Clip.Clip
  refinement:
    name:
      probed: arg2
      sources:
      - '[C++ signature] `void delete_clip(TTrackPyHandle, TPyHandle<AClip>)` — takes a Clip.'
      - '[docstring] "Delete the given clip. Raises a runtime error when the clip belongs to another track."'
      - '[M4L] track.md: `Parameter: clip` — "Delete the given clip".'
      - '[corpus] binding callsites pass a Clip variable: pushbase/actions.py:131 (`selected_track.delete_clip(clip)`), ableton/v3/live/action.py:75
        (`deletable.canonical_parent.delete_clip(deletable)`).'
      - '[corpus] the previous `slot` rename was wrong: its lone def-vote came from Blackstar_Live_Logic/clip_util.py:29 `def
        delete_clip(slot)`, a helper that calls `slot.delete_clip()` — a different binding entirely (`Live.ClipSlot.ClipSlot.delete_clip`,
        no args), not `Track.delete_clip(clip)`.'
returns:
  type: None
raw_doc: Delete the given clip. Raises a runtime error when the clip belongs to another track.
```

##### delete_device

```yaml
kind: method
signature: 'delete_device( (Track)arg1, (int)arg2) -> None :'
cpp_signature: void delete_device(TTrackPyHandle,int)
args:
- name: index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[C++ signature] `void delete_device(TTrackPyHandle, int)` — int.'
      - '[docstring] "Delete a device identified by the index in the ''devices'' list".'
      - '[M4L] track.md: `Parameter: index`.'
      - '[sister method] same situation as Chain.delete_device. The lone def-vote came from Push2/device_navigation.py:151
        — a module-level helper that takes a Device convenience arg and converts to int before calling the binding.'
returns:
  type: None
raw_doc: Delete a device identified by the index in the 'devices' list.
```

##### duplicate_clip_slot

```yaml
kind: method
signature: 'duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :'
cpp_signature: int duplicate_clip_slot(TTrackPyHandle,int)
args:
- name: index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `index`.'
returns:
  type: int
raw_doc: |-
  Duplicate a clip and put it into the next free slot and return the index
  of the destination slot. A new scene is created if no free slot is
  available. If creating the new scene would exceed the limitations,
  a runtime error is raised.
```

##### duplicate_clip_to_arrangement

```yaml
kind: method
signature: 'duplicate_clip_to_arrangement( (Track)self, (Clip)clip, (float)destination_time) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> duplicate_clip_to_arrangement(TTrackPyHandle,TPyHandle<AClip>,double)
args:
- name: clip
  type: Live.Clip.Clip
- name: destination_time
  type: float
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Duplicate the given clip into the arrangement of this track at the provided
  destination time and return it. When the type of the clip and the type of the
  track are incompatible, a runtime error is raised.
```

##### duplicate_device

```yaml
kind: method
signature: 'duplicate_device( (Track)arg1, (int)arg2) -> None :'
cpp_signature: void duplicate_device(TTrackPyHandle,int)
args:
- name: index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[docstring] description mentions ''index in the devices list'' — device position index.'
returns:
  type: None
raw_doc: Duplicate a device at a given index in the 'devices' list.
```

##### get_data

```yaml
kind: method
signature: 'get_data( (Track)arg1, (object)key, (object)default_value) -> object :'
cpp_signature: boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)
args:
- name: key
  type: str
- name: default_value
  type: Any
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[sister method] same pattern as Song.get_data — corpus-confirmed.'
returns:
  type: Any
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[sister method] same pattern as Song.get_data — corpus-confirmed.'
raw_doc: Get data for the given key, that was previously stored using set_data.
```

##### insert_device

```yaml
kind: method
signature: 'insert_device( (Track)arg1, (str)DeviceName [, (int)DeviceIndex=-1]) -> LomObject :'
cpp_signature: TWeakPtr<TPyHandleBase> insert_device(TTrackPyHandle,std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>> [,int=-1])
args:
- name: device_name
  type: str
- name: device_index
  type: int
  optional: true
  default: '-1'
returns:
  type: Live.Device.Device
  refinement:
    type:
      probed: Live.LomObject.LomObject
      confidence: high
      sources:
      - '[sister method] same shape as Chain.insert_device.'
      - '[C++ signature] returns `TWeakPtr<TPyHandleBase>` (generic LomObject) — no specific type enforced.'
      - '[probe] `track.devices` element_repr is `<class ''Device.Device''>` — the runtime returns Device instances when iterated,
        matching the insert return.'
      - '[docstring] + [M4L] confirm semantics ("Add a device at a given index in the ''devices'' list").'
raw_doc: Add a device at a given index in the 'devices' list. At end if -1.
```

##### jump_in_running_session_clip

```yaml
kind: method
signature: 'jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :'
cpp_signature: void jump_in_running_session_clip(TTrackPyHandle,double)
args:
- name: beats
  type: float
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/track.md names the parameter `beats`.'
returns:
  type: None
raw_doc: |-
  Jump forward or backward in the currently running Sessionclip (if any)
  by the specified relative amount in beats. Does nothing if no Session Clip
  is currently running.
```

##### set_data

```yaml
kind: method
signature: 'set_data( (Track)arg1, (object)key, (object)value) -> None :'
cpp_signature: void set_data(TTrackPyHandle,TString,boost::python::api::object)
args:
- name: key
  type: str
- name: value
  type: Any
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[sister method] same pattern as Song.set_data — corpus-confirmed.'
returns:
  type: None
raw_doc: Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
```

##### stop_all_clips

```yaml
kind: method
signature: 'stop_all_clips( (Track)arg1 [, (bool)Quantized=True]) -> None :'
cpp_signature: void stop_all_clips(TTrackPyHandle [,bool=True])
args:
- name: quantized
  type: bool
  optional: true
  default: 'True'
returns:
  type: None
raw_doc: Stop running and triggered clip and slots on this track.
```

### DeviceContainer

```yaml
kind: class
path: Live.Track.DeviceContainer
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class is a common super class of Track and Chain
```

Phantom base in the LOM type system. `Track` and `Chain` both
register `DeviceContainer` as their direct Python superclass via
Boost.Python's `bases<>` mechanism — `Track.__mro__` includes it,
`isinstance(track, DeviceContainer)` is True — but Boost binds the
shared methods and properties on each concrete subclass rather
than on the base. Result: real Python inheritance, structurally
empty class.

**Members are redefined on each subclass.** The shared surface
(`color`, `color_index`, `mute`, `muted_via_solo`, `name`, `solo`,
`delete_device`, `duplicate_device`, `insert_device`) is declared
independently on `Track` and `Chain`, each carrying its own
runtime docstring. The declarations live on the subclasses; this
class is the structural parent that holds them together for
`isinstance` purposes only.

**Idiomatic code ignores it.** Ableton's own corpus and the M4L
docs contain zero references to `DeviceContainer` — the
convention is `isinstance(c, (Live.Track.Track, Live.Chain.Chain))`
rather than testing against the common base. Treat it as an
implementation detail of the LOM type system, not a class to
program against.

### RoutingChannel

```yaml
kind: class
path: Live.Track.RoutingChannel
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a routing channel.
```

#### Properties

##### display_name

```yaml
kind: property
type: str
settable: false
raw_doc: Display name of routing channel.
```

##### layout

```yaml
kind: property
type: Live.Track.RoutingChannelLayout
settable: false
raw_doc: The routing channel's Layout, e.g., mono or stereo.
```

### RoutingChannelVector

```yaml
kind: class
path: Live.Track.RoutingChannelVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Track.RoutingChannel
raw_doc: A container for returning routing channels from Live.
```

### RoutingType

```yaml
kind: class
path: Live.Track.RoutingType
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a routing type.
```

#### Properties

##### attached_object

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Live object associated with the routing type.
```

##### category

```yaml
kind: property
type: Live.Track.RoutingTypeCategory
settable: false
raw_doc: Category of the routing type.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `RoutingTypeCategory` enum in same module (Track). Property is a member of `RoutingType` and names
      a category of routing — direct semantic match.'
```

##### display_name

```yaml
kind: property
type: str
settable: false
raw_doc: Display name of routing type.
```

### RoutingTypeVector

```yaml
kind: class
path: Live.Track.RoutingTypeVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Track.RoutingType
raw_doc: A container for returning routing types from Live.
```

### View

```yaml
kind: class
path: Live.Track.Track.View
parent: Track
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of a Track.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Get the canonical parent of the track view.
```

##### device_insert_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Listen the device insertion mode of the track.  By default, it will insert devices at the end, but it can be
  changed to make it relative to current selection.
```

##### is_collapsed

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set/Listen if the track is shown collapsed in the arranger view.
```

##### selected_device

```yaml
kind: property
type: Live.Device.Device
settable: false
listenable: true
raw_doc: Get/Set/Listen the insertion mode of the device.  While in insertion mode, loading new devices from the browser will
  place devices at the selected position.
```

#### Methods

##### select_instrument

```yaml
kind: method
signature: 'select_instrument( (View)arg1) -> bool :'
cpp_signature: bool select_instrument(TPyViewData<ATrack>)
returns:
  type: bool
raw_doc: Selects the track's instrument if it has one.
```

## Enums

### DeviceInsertMode

```yaml
kind: enum
members:
  default: 0
  selected_left: 1
  selected_right: 2
  count: 3
```

### RoutingChannelLayout

```yaml
kind: enum
members:
  mono: 1
  stereo: 2
  midi: 0
```

### RoutingTypeCategory

```yaml
kind: enum
members:
  external: 0
  rewire: 1
  resampling: 2
  master: 3
  track: 4
  parent_group_track: 5
  none: 6
  invalid: 7
```

### monitoring_states

```yaml
kind: enum
parent: Track
members:
  IN: 0
  AUTO: 1
  'OFF': 2
```

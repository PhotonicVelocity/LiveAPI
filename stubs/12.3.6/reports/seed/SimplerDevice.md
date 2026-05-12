---
module: SimplerDevice
---

## Classes

### SimplerDevice

```yaml
kind: class
path: Live.SimplerDevice.SimplerDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Simpler device.
```

#### Properties

##### can_warp_as

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if warp_as is available.
```

##### can_warp_double

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if warp_double is available.
```

##### can_warp_half

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if warp_half is available.
```

##### is_active

```yaml
kind: property
type: bool
settable: false
raw_doc: Return const access to whether this device is active. This will be false bothwhen the device is off and when it's
  inside a rack device which is off.
```

##### is_using_compare_preset_b

```yaml
kind: property
type: bool
settable: true
raw_doc: Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
```

##### latency_in_ms

```yaml
kind: property
type: float
settable: false
raw_doc: Returns the latency of the device in ms.
```

##### latency_in_samples

```yaml
kind: property
type: int
settable: false
raw_doc: Returns the latency of the device in samples.
```

##### multi_sample_mode

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns whether Simpler is in mulit-sample mode.
```

##### name

```yaml
kind: property
type: str
settable: true
raw_doc: Return access to the name of the device.
```

##### note_pitch_bend_range

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the Note Pitch Bend Range in Simpler.
```

##### pad_slicing

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  When set to true, slices can be added in slicing mode by playing notes
  .that are not assigned to slices, yet.
```

##### parameters

```yaml
kind: property
type: Live.Device.ATimeableValueVector
settable: false
raw_doc: Const access to the list of available automatable parameters for this device.
```

##### pitch_bend_range

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the Pitch Bend Range in Simpler.
```

##### playback_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to Simpler's playback mode.
```

##### playing_position

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: |-
  Constant access to the current playing position in the sample.
  The returned value is the normalized position between sample start and end.
```

##### playing_position_enabled

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Returns whether Simpler is showing the playing position.
  The returned value is True while the sample is played back
```

##### retrigger

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Access to Simpler's retrigger mode.
```

##### sample

```yaml
kind: property
type: Live.Sample.Sample
settable: false
listenable: true
raw_doc: Get the loaded Sample.
```

##### slicing_playback_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to Simpler's slicing playback mode.
```

##### view

```yaml
kind: property
type: Live.SimplerDevice.SimplerDevice.View
settable: false
raw_doc: Representing the view aspects of a device.
```

##### voices

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the number of voices in Simpler.
```

#### Methods

##### crop

```yaml
kind: method
signature: 'crop( (SimplerDevice)self) -> None :'
cpp_signature: void crop(TSimplerDevicePyHandle)
returns:
  type: None
raw_doc: |-
  Crop the loaded sample to the active area between start- and end marker.
  Calling this method on an empty simpler raises an error.
```

##### guess_playback_length

```yaml
kind: method
signature: 'guess_playback_length( (SimplerDevice)self) -> float :'
cpp_signature: double guess_playback_length(TSimplerDevicePyHandle)
returns:
  type: float
raw_doc: |-
  Return an estimated beat time for the playback length between start- and end-marker.
  Calling this method on an empty simpler raises an error.
```

##### reverse

```yaml
kind: method
signature: 'reverse( (SimplerDevice)self) -> None :'
cpp_signature: void reverse(TSimplerDevicePyHandle)
returns:
  type: None
raw_doc: |-
  Reverse the loaded sample.
  Calling this method on an empty simpler raises an error.
```

##### warp_as

```yaml
kind: method
signature: 'warp_as( (SimplerDevice)self, (float)beat_time) -> None :'
cpp_signature: void warp_as(TSimplerDevicePyHandle,double)
args:
- name: beat_time
  type: float
returns:
  type: None
raw_doc: |-
  Warp the playback region between start- and end-marker as the given length.
  Calling this method on an empty simpler raises an error.
```

##### warp_double

```yaml
kind: method
signature: 'warp_double( (SimplerDevice)self) -> None :'
cpp_signature: void warp_double(TSimplerDevicePyHandle)
returns:
  type: None
raw_doc: Doubles the tempo for region between start- and end-marker.
```

##### warp_half

```yaml
kind: method
signature: 'warp_half( (SimplerDevice)self) -> None :'
cpp_signature: void warp_half(TSimplerDevicePyHandle)
returns:
  type: None
raw_doc: Halves the tempo for region between start- and end-marker.
```

### View

```yaml
kind: class
path: Live.SimplerDevice.SimplerDevice.View
parent: SimplerDevice
ancestors:
- Live.Device.Device.View
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of a simpler device.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.SimplerDevice.SimplerDevice
settable: false
raw_doc: Get the canonical parent of the View.
```

##### is_collapsed

```yaml
kind: property
type: bool
settable: true
raw_doc: Get/Set/Listen if the device is shown collapsed in the device chain.
```

##### sample_end

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.
```

##### sample_env_fade_in

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns
  -1 in case there is no sample loaded.
```

##### sample_env_fade_out

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode.
  Returns -1 in case there is no sample loaded.
```

##### sample_loop_end

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.
```

##### sample_loop_fade

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.
```

##### sample_loop_start

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.
```

##### sample_start

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.
```

##### selected_slice

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the selected slice.
```

## Enums

### PlaybackMode

```yaml
kind: enum
members:
  classic: 0
  one_shot: 1
  slicing: 2
```

### SlicingPlaybackMode

```yaml
kind: enum
members:
  mono: 0
  poly: 1
  thru: 2
```

## Functions

### get_available_voice_numbers

```yaml
kind: function
signature: 'get_available_voice_numbers() -> IntVector :'
cpp_signature: std::__1::vector<int, std::__1::allocator<int>> get_available_voice_numbers()
returns:
  type: Live.Base.IntVector
raw_doc: Get a vector of valid Simpler voice numbers.
```

---
module: Sample
---

## Classes

### Sample

```yaml
kind: class
path: Live.Sample.Sample
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a sample file loaded into a Simpler instance.
```

#### Properties

##### beats_granulation_resolution

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the Granulation Resolution parameter in Beats Warp Mode.
```

##### beats_transient_envelope

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Transient Envelope parameter in Beats Warp Mode.
```

##### beats_transient_loop_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the Transient Loop Mode parameter in Beats Warp Mode.
```

##### canonical_parent

```yaml
kind: property
type: Live.SimplerDevice.SimplerDevice
settable: false
raw_doc: Access to the sample's canonical parent.
```

##### complex_pro_envelope

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Envelope parameter in Complex Pro Mode.
```

##### complex_pro_formants

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Formants parameter in Complex Pro Warp Mode.
```

##### end_marker

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the position of the sample's end marker.
```

##### file_path

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: Get the path of the sample file.
```

##### gain

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the sample gain.
```

##### length

```yaml
kind: property
type: int
settable: false
raw_doc: Get the length of the sample file in sample frames.
```

##### sample_rate

```yaml
kind: property
type: float
settable: false
raw_doc: Access to the audio sample rate of the sample.
```

##### slices

```yaml
kind: property
type: tuple
settable: false
listenable: true
raw_doc: Access to the list of slice points in sample time in the sample.
```

##### slicing_beat_division

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to sample's slicing step size.
```

##### slicing_region_count

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to sample's slicing split count.
```

##### slicing_sensitivity

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.
  The higher the sensitivity, the more slices will be available.
```

##### slicing_style

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to sample's slicing style.
```

##### start_marker

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the position of the sample's start marker.
```

##### texture_flux

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Flux parameter in Texture Warp Mode.
```

##### texture_grain_size

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Grain Size parameter in Texture Warp Mode.
```

##### tones_grain_size

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Access to the Grain Size parameter in Tones Warp Mode.
```

##### warp_markers

```yaml
kind: property
type: Live.Clip.WarpMarkerVector
settable: false
listenable: true
raw_doc: Get the warp markers for this sample.
```

##### warp_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the sample's warp mode.
```

##### warping

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Access to the sample's warping property.
```

#### Methods

##### beat_to_sample_time

```yaml
kind: method
signature: 'beat_to_sample_time( (Sample)self, (float)beat_time) -> float :'
cpp_signature: double beat_to_sample_time(TPyHandle<AMultiSamplePart>,double)
args:
- name: beat_time
  type: float
returns:
  type: float
raw_doc: Converts the given beat time to sample time. Raises an error if the sample is not warped.
```

##### clear_slices

```yaml
kind: method
signature: 'clear_slices( (Sample)self) -> None :'
cpp_signature: void clear_slices(TPyHandle<AMultiSamplePart>)
returns:
  type: None
raw_doc: Clears all slices created in Simpler's manual mode.
```

##### gain_display_string

```yaml
kind: method
signature: 'gain_display_string( (Sample)self) -> str :'
cpp_signature: TString gain_display_string(TPyHandle<AMultiSamplePart>)
returns:
  type: str
raw_doc: Get the gain's display value as a string.
```

##### insert_slice

```yaml
kind: method
signature: 'insert_slice( (Sample)self, (int)slice_time) -> None :'
cpp_signature: void insert_slice(TPyHandle<AMultiSamplePart>,int)
args:
- name: slice_time
  type: int
returns:
  type: None
raw_doc: Add a slice point at the provided time if there is none.
```

##### move_slice

```yaml
kind: method
signature: 'move_slice( (Sample)self, (int)old_time, (int)new_time) -> int :'
cpp_signature: int move_slice(TPyHandle<AMultiSamplePart>,int,int)
args:
- name: old_time
  type: int
- name: new_time
  type: int
returns:
  type: int
raw_doc: Move the slice point at the provided time.
```

##### remove_slice

```yaml
kind: method
signature: 'remove_slice( (Sample)self, (int)slice_time) -> None :'
cpp_signature: void remove_slice(TPyHandle<AMultiSamplePart>,int)
args:
- name: slice_time
  type: int
returns:
  type: None
raw_doc: Remove the slice point at the provided time if there is one.
```

##### reset_slices

```yaml
kind: method
signature: 'reset_slices( (Sample)self) -> None :'
cpp_signature: void reset_slices(TPyHandle<AMultiSamplePart>)
returns:
  type: None
raw_doc: Resets all edited slices to their original positions.
```

##### sample_to_beat_time

```yaml
kind: method
signature: 'sample_to_beat_time( (Sample)self, (float)sample_time) -> float :'
cpp_signature: double sample_to_beat_time(TPyHandle<AMultiSamplePart>,double)
args:
- name: sample_time
  type: float
returns:
  type: float
raw_doc: Converts the given sample time to beat time. Raises an error if the sample is not warped.
```

## Enums

### SlicingBeatDivision

```yaml
kind: enum
members:
  sixteenth: 0
  sixteenth_triplett: 1
  eighth: 2
  eighth_triplett: 3
  quarter: 4
  quarter_triplett: 5
  half: 6
  half_triplett: 7
  one_bar: 8
  two_bars: 9
  four_bars: 10
```

### SlicingStyle

```yaml
kind: enum
members:
  transient: 0
  beat: 1
  region: 2
  manual: 3
```

### TransientLoopMode

```yaml
kind: enum
members:
  'off': 0
  forward: 1
  alternate: 2
```

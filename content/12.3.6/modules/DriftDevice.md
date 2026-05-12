---
module: DriftDevice
---

Represents an instance of Drift, Live's monosynth instrument. The
`DriftDevice` class extends `Device` with Drift-specific state alongside
the inherited parameter and preset surface.

## Classes

### DriftDevice

```yaml
kind: class
path: Live.DriftDevice.DriftDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Drift device.
```

#### Properties

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

##### mod_matrix_filter_source_1_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the filter mod source 1 index
```

##### mod_matrix_filter_source_1_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the filter mod source 1 list
```

##### mod_matrix_filter_source_2_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the filter mod source 2 index
```

##### mod_matrix_filter_source_2_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the filter mod source 2 list
```

##### mod_matrix_lfo_source_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the lfo mod source index
```

##### mod_matrix_lfo_source_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the lfo mod source list
```

##### mod_matrix_pitch_source_1_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the pitch mod source 1 index
```

##### mod_matrix_pitch_source_1_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the pitch mod source 1 list
```

##### mod_matrix_pitch_source_2_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the pitch mod source 2 index
```

##### mod_matrix_pitch_source_2_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the pitch mod source 2 list
```

##### mod_matrix_shape_source_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the shape mod source index
```

##### mod_matrix_shape_source_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the shape mod source list
```

##### mod_matrix_source_1_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod source 1 index
```

##### mod_matrix_source_1_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod source 1 list
```

##### mod_matrix_source_2_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod source 2 index
```

##### mod_matrix_source_2_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod source 2 list
```

##### mod_matrix_source_3_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod source 3 index
```

##### mod_matrix_source_3_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod source 3 list
```

##### mod_matrix_target_1_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod target 1 index
```

##### mod_matrix_target_1_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod target 1 list
```

##### mod_matrix_target_2_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod target 2 index
```

##### mod_matrix_target_2_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod target 2 list
```

##### mod_matrix_target_3_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom mod target 3 index
```

##### mod_matrix_target_3_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom mod target 3 list
```

##### name

```yaml
kind: property
type: str
settable: true
raw_doc: Return access to the name of the device.
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
raw_doc: Return the Pitch Bend Range
```

##### voice_count_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the voice count index
```

##### voice_count_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the voice count list
```

##### voice_mode_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the voice mode index
```

##### voice_mode_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the voice mode list
```

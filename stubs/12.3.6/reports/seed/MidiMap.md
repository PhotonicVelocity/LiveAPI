---
module: MidiMap
---

## Classes

### CCFeedbackRule

```yaml
kind: class
path: Live.MidiMap.CCFeedbackRule
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Structure to define feedback properties of MIDI mappings.
```

#### Properties

##### cc_no

```yaml
kind: property
type: int
settable: true
```

##### cc_value_map

```yaml
kind: property
type: tuple
settable: true
```

##### channel

```yaml
kind: property
type: int
settable: true
```

##### delay_in_ms

```yaml
kind: property
type: float
settable: true
```

##### enabled

```yaml
kind: property
type: bool
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

### NoteFeedbackRule

```yaml
kind: class
path: Live.MidiMap.NoteFeedbackRule
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Structure to define feedback properties of MIDI mappings.
```

#### Properties

##### channel

```yaml
kind: property
type: int
settable: true
```

##### delay_in_ms

```yaml
kind: property
type: float
settable: true
```

##### enabled

```yaml
kind: property
type: bool
settable: true
```

##### note_no

```yaml
kind: property
type: int
settable: true
```

##### vel_map

```yaml
kind: property
type: tuple
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

### PitchBendFeedbackRule

```yaml
kind: class
path: Live.MidiMap.PitchBendFeedbackRule
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Structure to define feedback properties of MIDI mappings.
```

#### Properties

##### channel

```yaml
kind: property
type: int
settable: true
```

##### delay_in_ms

```yaml
kind: property
type: float
settable: true
```

##### enabled

```yaml
kind: property
type: bool
settable: true
```

##### value_pair_map

```yaml
kind: property
type: tuple
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

## Enums

### MapMode

```yaml
kind: enum
members:
  absolute: 0
  relative_signed_bit: 1
  relative_binary_offset: 2
  relative_two_compliment: 3
  relative_signed_bit2: 4
  absolute_14_bit: 5
  relative_smooth_signed_bit: 6
  relative_smooth_binary_offset: 7
  relative_smooth_two_compliment: 8
  relative_smooth_signed_bit2: 9
```

## Functions

### forward_midi_cc

```yaml
kind: function
signature: 'forward_midi_cc( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :'
cpp_signature: bool forward_midi_cc(unsigned int,unsigned int,int,int [,bool=True])
args:
- name: arg1
  type: int
- name: arg2
  type: int
- name: arg3
  type: int
- name: arg4
  type: int
- name: should_consume_event
  type: bool
  optional: true
  default: 'True'
returns:
  type: bool
```

### forward_midi_note

```yaml
kind: function
signature: 'forward_midi_note( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :'
cpp_signature: bool forward_midi_note(unsigned int,unsigned int,int,int [,bool=True])
args:
- name: arg1
  type: int
- name: arg2
  type: int
- name: arg3
  type: int
- name: arg4
  type: int
- name: should_consume_event
  type: bool
  optional: true
  default: 'True'
returns:
  type: bool
```

### forward_midi_pitchbend

```yaml
kind: function
signature: 'forward_midi_pitchbend( (int)arg1, (int)arg2, (int)arg3) -> bool :'
cpp_signature: bool forward_midi_pitchbend(unsigned int,unsigned int,int)
args:
- name: arg1
  type: int
- name: arg2
  type: int
- name: arg3
  type: int
returns:
  type: bool
```

### map_midi_cc

```yaml
kind: function
signature: 'map_midi_cc( (int)midi_map_handle, (DeviceParameter)parameter, (int)midi_channel, (int)controller_number, (MapMode)map_mode,
  (bool)avoid_takeover [, (float)sensitivity=1.0]) -> bool :'
cpp_signature: bool map_midi_cc(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,bool
  [,float=1.0])
args:
- name: midi_map_handle
  type: int
- name: parameter
  type: Live.DeviceParameter.DeviceParameter
- name: midi_channel
  type: int
- name: controller_number
  type: int
- name: map_mode
  type: Live.MidiMap.MapMode | int
- name: avoid_takeover
  type: bool
- name: sensitivity
  type: float
  optional: true
  default: '1.0'
returns:
  type: bool
```

### map_midi_cc_with_feedback_map

```yaml
kind: function
signature: 'map_midi_cc_with_feedback_map( (int)midi_map_handle, (DeviceParameter)parameter, (int)midi_channel, (int)controller_number,
  (MapMode)map_mode, (CCFeedbackRule)feedback_rule, (bool)avoid_takeover [, (float)sensitivity=1.0]) -> bool :'
cpp_signature: bool map_midi_cc_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,NPythonMidiMap::TCCFeedbackRule,bool
  [,float=1.0])
args:
- name: midi_map_handle
  type: int
- name: parameter
  type: Live.DeviceParameter.DeviceParameter
- name: midi_channel
  type: int
- name: controller_number
  type: int
- name: map_mode
  type: Live.MidiMap.MapMode | int
- name: feedback_rule
  type: Live.MidiMap.CCFeedbackRule
- name: avoid_takeover
  type: bool
- name: sensitivity
  type: float
  optional: true
  default: '1.0'
returns:
  type: bool
```

### map_midi_note

```yaml
kind: function
signature: 'map_midi_note( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4) -> bool :'
cpp_signature: bool map_midi_note(unsigned int,TPyHandle<ATimeableValue>,int,int)
args:
- name: arg1
  type: int
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
- name: arg3
  type: int
- name: arg4
  type: int
returns:
  type: bool
```

### map_midi_note_with_feedback_map

```yaml
kind: function
signature: 'map_midi_note_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4, (NoteFeedbackRule)arg5)
  -> bool :'
cpp_signature: bool map_midi_note_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NPythonMidiMap::TNoteFeedbackRule)
args:
- name: arg1
  type: int
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
- name: arg3
  type: int
- name: arg4
  type: int
- name: arg5
  type: Live.MidiMap.NoteFeedbackRule
returns:
  type: bool
```

### map_midi_pitchbend

```yaml
kind: function
signature: 'map_midi_pitchbend( (int)arg1, (DeviceParameter)arg2, (int)arg3, (bool)arg4) -> bool :'
cpp_signature: bool map_midi_pitchbend(unsigned int,TPyHandle<ATimeableValue>,int,bool)
args:
- name: arg1
  type: int
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
- name: arg3
  type: int
- name: arg4
  type: bool
returns:
  type: bool
```

### map_midi_pitchbend_with_feedback_map

```yaml
kind: function
signature: 'map_midi_pitchbend_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (PitchBendFeedbackRule)arg4,
  (bool)arg5) -> bool :'
cpp_signature: bool map_midi_pitchbend_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,NPythonMidiMap::TPitchBendFeedbackRule,bool)
args:
- name: arg1
  type: int
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
- name: arg3
  type: int
- name: arg4
  type: Live.MidiMap.PitchBendFeedbackRule
- name: arg5
  type: bool
returns:
  type: bool
```

### send_feedback_for_parameter

```yaml
kind: function
signature: 'send_feedback_for_parameter( (int)arg1, (DeviceParameter)arg2) -> None :'
cpp_signature: void send_feedback_for_parameter(unsigned int,TPyHandle<ATimeableValue>)
args:
- name: arg1
  type: int
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: None
```

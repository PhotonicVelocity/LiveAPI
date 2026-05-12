---
module: MidiMap
---

Defines the binding surface that control surface scripts use to map physical
MIDI controls to Live parameters. Module-level `forward_*` and `map_*`
functions install CC, note, and pitch-bend mappings, while `CCFeedbackRule`,
`NoteFeedbackRule`, and `PitchBendFeedbackRule` describe the feedback values
Live should send back to the controller.

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
element_type: int
settable: true
refinement:
  element_type:
    confidence: high
    sources:
    - '[corpus] int tuples assigned directly: LV2_LX2_LC2_LD2/ParamMap.py:69, SL_MkIII/sl_mkiii.py:117, _Axiom/Encoders.py:38.'
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
element_type: int
settable: true
refinement:
  element_type:
    confidence: high
    sources:
    - '[corpus] int tuples assigned directly: Axiom_AIR_25_49_61.py:594, ableton/v2/control_surface/control_surface.py:420,
      _Framework/ControlSurface.py:471.'
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
element_type: tuple
settable: true
refinement:
  element_type:
    confidence: low
    sources:
    - '[schema] field name + context suggests tuples of value pairs, but element type is bare `tuple` (no inner type info)
      — vague. May want tighter shape if a probe or corpus pattern surfaces it.'
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
- name: script_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] 11/14 callsites use kwarg `script_handle`.'
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] 14/14 callsites use kwarg `midi_map_handle`.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[corpus] callsites use kwarg `midi_channel`.'
- name: controller_number
  type: int
  refinement:
    name:
      probed: arg4
      sources:
      - '[corpus] callsites use kwarg `controller_number`.'
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
- name: script_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] 3/7 callsites use kwarg `script_handle`.'
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] 7/7 callsites use kwarg `midi_map_handle`.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[corpus] callsites use kwarg `midi_channel`.'
- name: note
  type: int
  refinement:
    name:
      probed: arg4
      sources:
      - '[corpus] 3/7 callsites use kwarg `note`.'
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
- name: script_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] 2/2 callsites use kwarg `script_handle`.'
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] 2/2 callsites use kwarg `midi_map_handle`.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[corpus] callsites use kwarg `midi_channel`.'
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
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[sister method] consistent with other MidiMap functions that take the handle as the first arg.'
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[C++ signature] type is DeviceParameter — qualified to distinguish from a generic parameter.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[sister method] MIDI channel parameter, consistent with other MidiMap functions.'
- name: note
  type: int
  refinement:
    name:
      probed: arg4
      sources:
      - '[sister method] MIDI note number parameter, consistent with related note-feedback methods.'
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
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] callsites pass a variable named `midi_map_handle` in the first positional slot (_Framework/ControlSurface.py:485,
        ableton/v2/control_surface/control_surface.py:435, Axiom_AIR_25_49_61/Axiom_AIR_25_49_61.py:608).'
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] callsites use the bare name `parameter`; qualified to `device_parameter` for stub readability since the
        type is DeviceParameter.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[corpus] callsites pass `control.message_channel()` — semantic name `midi_channel`.'
- name: note
  type: int
  refinement:
    name:
      probed: arg4
      sources:
      - '[corpus] callsites pass `control.message_identifier()`, which in the note-feedback context is a MIDI note number.'
- name: feedback_rule
  type: Live.MidiMap.NoteFeedbackRule
  refinement:
    name:
      probed: arg5
      sources:
      - '[corpus] callsites pass a variable named `feedback_rule` in the fifth positional slot.'
returns:
  type: bool
```

### map_midi_pitchbend

```yaml
kind: function
signature: 'map_midi_pitchbend( (int)arg1, (DeviceParameter)arg2, (int)arg3, (bool)arg4) -> bool :'
cpp_signature: bool map_midi_pitchbend(unsigned int,TPyHandle<ATimeableValue>,int,bool)
args:
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[sister method] consistent with other MidiMap functions.'
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[C++ signature] type is DeviceParameter — qualified to distinguish from a generic parameter.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[sister method] MIDI channel parameter, consistent with other MidiMap functions.'
- name: needs_takeover
  type: bool
  refinement:
    name:
      probed: arg4
      sources:
      - '[sister method] manual hints say bools in pitchbend methods indicate whether takeover is needed.'
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
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] callsites all pass a variable named `midi_map_handle` in the first positional slot (_Framework/ControlSurface.py:491,
        ableton/v2/control_surface/control_surface.py:441, Axiom_AIR_25_49_61/Axiom_AIR_25_49_61.py:614, MackieControl/ChannelStrip.py:199,379,
        MackieControl_Classic/ChannelStrip.py:197,377).'
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] callsites use `parameter` / `__fader_parameter`; qualified to `device_parameter` for stub readability since
        the type is DeviceParameter.'
- name: midi_channel
  type: int
  refinement:
    name:
      probed: arg3
      sources:
      - '[corpus] callsites pass `control.message_channel()` (or `__strip_index`) — semantic name `midi_channel`.'
- name: feedback_rule
  type: Live.MidiMap.PitchBendFeedbackRule
  refinement:
    name:
      probed: arg4
      sources:
      - '[corpus] callsites pass a variable named `feedback_rule` (or `feeback_rule` [sic]).'
- name: needs_takeover
  type: bool
  refinement:
    name:
      probed: arg5
      sources:
      - '[corpus] callsites pass `not control.needs_takeover()` — the parameter controls takeover behavior, with the bool
        inverted by the caller.'
returns:
  type: bool
```

### send_feedback_for_parameter

```yaml
kind: function
signature: 'send_feedback_for_parameter( (int)arg1, (DeviceParameter)arg2) -> None :'
cpp_signature: void send_feedback_for_parameter(unsigned int,TPyHandle<ATimeableValue>)
args:
- name: midi_map_handle
  type: int
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] 8/8 callsites use kwarg `midi_map_handle`.'
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[corpus] callsites use kwarg `device_parameter`.'
returns:
  type: None
```

---
module: DeviceParameter
---

Represents a single automatable parameter on a device or mixer in Live. The
`DeviceParameter` class exposes the parameter's current value, range,
display string, automation state, and MIDI/key mapping target.

## Classes

### DeviceParameter

```yaml
kind: class
path: Live.DeviceParameter.DeviceParameter
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: |-
  This class represents a (automatable) parameter within a MIDI or
  Audio DSP-Device.
```

#### Properties

##### automation_state

```yaml
kind: property
type: Live.DeviceParameter.AutomationState
settable: false
listenable: true
raw_doc: Returns state of type AutomationState.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `AutomationState` enum in same module. Property name matches the enum snake-case; raw_doc describes
      automation states (none / playing / overridden) which match `AutomationState` members.'
```

##### canonical_parent

```yaml
kind: property
type: Live.Device.Device
settable: false
raw_doc: Get the canonical parent of the device parameter.
```

##### default_value

```yaml
kind: property
type: float
settable: false
raw_doc: |-
  Return the default value for this parameter.  A Default value is only
  available for non-quantized parameter types (see 'is_quantized').
```

##### display_value

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Get/Set the current value (as visible in the GUI) this parameter.
  The value must be inside the min/max properties of this device.
```

##### is_enabled

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns false if the parameter has been macro mapped or disabled by Max.
```

##### is_quantized

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  Returns True, if this value is a boolean or integer like switch.
  Non quantized values are continues float values.
```

##### max

```yaml
kind: property
type: float
settable: false
raw_doc: |-
  Returns const access to the upper value of the allowed range for
  this parameter
```

##### min

```yaml
kind: property
type: float
settable: false
raw_doc: |-
  Returns const access to the lower value of the allowed range for
  this parameter
```

##### name

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: |-
  Returns const access the name of this parameter, as visible in Lives
  automation choosers.
```

##### original_name

```yaml
kind: property
type: str
settable: false
raw_doc: |-
  Returns const access the original name of this parameter, unaffected of
  any renamings.
```

##### short_value_items

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the list of possible values for this parameter. Like value_items, but prefers short value names if available.
  Raises an error if 'is_quantized' is False.
```

##### state

```yaml
kind: property
type: Live.DeviceParameter.ParameterState
settable: false
listenable: true
raw_doc: |-
  Returns the state of the parameter:
  - enabled - the parameter's value can be changed,
  - irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,
  - disabled - the parameter's value cannot be changed.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] two enums in same module overlap on the name `state`: `AutomationState` and `ParameterState`.'
    - '[docstring] "Returns the state of the parameter: enabled, irrelevant, ..." — those are exactly `ParameterState` member
      names (enabled / irrelevant / disabled). `AutomationState`''s members (none / playing / overridden) describe a different
      concept.'
```

##### value

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Get/Set the current internal value of this parameter.
  The value must be inside the min/max properties of this device.
```

##### value_items

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.
```

#### Methods

##### begin_gesture

```yaml
kind: method
signature: 'begin_gesture( (DeviceParameter)arg1) -> None :'
cpp_signature: void begin_gesture(TPyHandle<ATimeableValue>)
returns:
  type: None
raw_doc: Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent
  group -- for Sexample, when recording automation.
```

##### end_gesture

```yaml
kind: method
signature: 'end_gesture( (DeviceParameter)arg1) -> None :'
cpp_signature: void end_gesture(TPyHandle<ATimeableValue>)
returns:
  type: None
raw_doc: Notify the end of a modification of the parameter. See begin_gesture.
```

##### re_enable_automation

```yaml
kind: method
signature: 're_enable_automation( (DeviceParameter)arg1) -> None :'
cpp_signature: void re_enable_automation(TPyHandle<ATimeableValue>)
returns:
  type: None
raw_doc: Reenable automation for this parameter.
```

##### str_for_value

```yaml
kind: method
signature: 'str_for_value( (DeviceParameter)arg1, (float)arg2) -> str :'
cpp_signature: TString str_for_value(TPyHandle<ATimeableValue>,float)
args:
- name: value
  type: float
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/deviceparameter.md names the parameter `value`.'
returns:
  type: str
raw_doc: |-
  Return a string representation of the given value. To be used
  for display purposes only. This value can include characters like 'db' or
  'hz', depending on the type of the parameter.
```

## Enums

### AutomationState

```yaml
kind: enum
members:
  none: 0
  playing: 1
  overridden: 2
```

### ParameterState

```yaml
kind: enum
members:
  enabled: 0
  irrelevant: 1
  disabled: 2
```

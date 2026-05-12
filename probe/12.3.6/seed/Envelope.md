---
module: Envelope
---

## Classes

### Envelope

```yaml
kind: class
path: Live.Envelope.Envelope
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents an automation or modulation envelope in Live.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Clip.Clip
settable: false
raw_doc: Get the canonical parent of the envelope.
```

#### Methods

##### delete_events_in_range

```yaml
kind: method
signature: 'delete_events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> None :'
cpp_signature: void delete_events_in_range(TPyHandle<AAutomation> {lvalue},double,double)
args:
- name: arg2
  type: float
- name: arg3
  type: float
returns:
  type: None
raw_doc: Deletes the events in the specified time range.
```

##### events_in_range

```yaml
kind: method
signature: 'events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> EnvelopeEventVector :'
cpp_signature: std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> events_in_range(TPyHandle<AAutomation>
  {lvalue},double,double)
args:
- name: arg2
  type: float
- name: arg3
  type: float
returns:
  type: Live.Envelope.EnvelopeEventVector
raw_doc: Returns the events in the specified time range.
```

##### insert_step

```yaml
kind: method
signature: 'insert_step( (Envelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :'
cpp_signature: void insert_step(TPyHandle<AAutomation> {lvalue},double,double,double)
args:
- name: arg2
  type: float
- name: arg3
  type: float
- name: arg4
  type: float
returns:
  type: None
raw_doc: Given a start time, a step length and a value, creates a step in the envelope.
```

##### value_at_time

```yaml
kind: method
signature: 'value_at_time( (Envelope)arg1, (float)arg2) -> float :'
cpp_signature: double value_at_time(TPyHandle<AAutomation> {lvalue},double)
args:
- name: arg2
  type: float
returns:
  type: float
raw_doc: Returns the parameter value at the specified time.
```

### EnvelopeEvent

```yaml
kind: class
path: Live.Envelope.EnvelopeEvent
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (float)time, (float)value, (EnvelopeEventControlCoefficients)control_coefficients) -> None :
      Create a new envelope event.

      C++ signature :
          void __init__(_object*,double,float,NApiHelpers::TEnvelopeEventControlCoefficients)
constructable: true
raw_doc: This is a class that represents an envelope event.
```

#### Properties

##### control_coefficients

```yaml
kind: property
type: Live.Envelope.EnvelopeEventControlCoefficients
settable: true
```

##### time

```yaml
kind: property
type: float
settable: true
```

##### value

```yaml
kind: property
type: float
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: time
  type: float
- name: value
  type: float
- name: control_coefficients
  type: EnvelopeEventControlCoefficients
returns:
  type: None
```

### EnvelopeEventControlCoefficients

```yaml
kind: class
path: Live.Envelope.EnvelopeEventControlCoefficients
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (float)x1, (float)y1, (float)x2, (float)y2) -> None :
      Create new envelope event control coefficients.

      C++ signature :
          void __init__(_object*,double,double,double,double)
constructable: true
raw_doc: This class represents the control coefficients of an envelope event.
```

#### Properties

##### x1

```yaml
kind: property
type: float
settable: true
```

##### x2

```yaml
kind: property
type: float
settable: true
```

##### y1

```yaml
kind: property
type: float
settable: true
```

##### y2

```yaml
kind: property
type: float
settable: true
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: x1
  type: float
- name: y1
  type: float
- name: x2
  type: float
- name: y2
  type: float
returns:
  type: None
```

### EnvelopeEventVector

```yaml
kind: class
path: Live.Envelope.EnvelopeEventVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Envelope.EnvelopeEvent
raw_doc: A container for holding envelope events.
```

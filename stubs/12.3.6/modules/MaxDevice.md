---
module: MaxDevice
---

Represents a Max for Live device hosted on a track or rack chain. The
`MaxDevice` class extends `Device` with hooks specific to M4L — patcher
loading, parameter exposure, and inter-device messaging.

## Classes

### MaxDevice

```yaml
kind: class
path: Live.MaxDevice.MaxDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Max for Live device.
```

#### Properties

##### audio_inputs

```yaml
kind: property
type: Live.Base.Vector[Live.DeviceIO.DeviceIO]
settable: false
listenable: true
raw_doc: Const access to a list of all audio inputs of the device.
```

##### audio_outputs

```yaml
kind: property
type: Live.Base.Vector[Live.DeviceIO.DeviceIO]
settable: false
listenable: true
raw_doc: Const access to a list of all audio outputs of the device.
```

##### is_active

```yaml
kind: property
type: bool
settable: false
raw_doc: Return const access to whether this device is active. This will be false bothwhen the device is off and when it's
  inside a rack device which is off.
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

##### midi_inputs

```yaml
kind: property
type: Live.Base.Vector
element_type: Live.DeviceIO.DeviceIO
settable: false
listenable: true
raw_doc: Const access to a list of all midi outputs of the device.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "Const access to a list of all midi outputs of the device."'
    - '[M4L] maxdevice.md: `midi_inputs list of DeviceIO read-only observe`.'
```

##### midi_outputs

```yaml
kind: property
type: Live.Base.Vector
element_type: Live.DeviceIO.DeviceIO
settable: false
listenable: true
raw_doc: Const access to a list of all midi outputs of the device.
refinement:
  element_type:
    confidence: high
    sources:
    - '[sister method] same shape as midi_inputs.'
    - '[M4L] maxdevice.md: `midi_outputs list of DeviceIO read-only observe`.'
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

##### bank_parameters_changed

```yaml
kind: property
listenable: true
```

Fires when the Max for Live device's bank-parameter mapping
reconfigures — parameter rebinding to a different bank slot
or a structural change to the bank set. Read the new state
via `get_bank_count`, `get_bank_name`, and
`get_bank_parameters`.

#### Methods

##### get_bank_count

```yaml
kind: method
signature: 'get_bank_count( (MaxDevice)arg1) -> int :'
cpp_signature: int get_bank_count(TMaxDevicePyHandle)
returns:
  type: int
raw_doc: Get the number of parameter banks. This is related to hardware control surfaces.
```

##### get_bank_name

```yaml
kind: method
signature: 'get_bank_name( (MaxDevice)arg1, (int)arg2) -> str :'
cpp_signature: TString get_bank_name(TMaxDevicePyHandle,int)
args:
- name: bank_index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/maxdevice.md names the parameter `bank_index`.'
returns:
  type: str
raw_doc: Get the name of a parameter bank given by index. This is related to hardware control surfaces.
```

##### get_bank_parameters

```yaml
kind: method
signature: 'get_bank_parameters( (MaxDevice)arg1, (int)arg2) -> list :'
cpp_signature: boost::python::list get_bank_parameters(TMaxDevicePyHandle,int)
args:
- name: bank_index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
      - '[M4L] external/max-for-live-docs/9.0/maxdevice.md names the parameter `bank_index`.'
returns:
  type: list[int]
  refinement:
    type:
      probed: list
      confidence: high
      sources:
      - '[M4L] maxdevice.md confirms `list[int]`.'
      - '[corpus] uses `parameter_indices = device.get_bank_parameters(bank_index)`.'
raw_doc: Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the
  best-of bank. This function is related to hardware control surfaces.
```

##### get_value_item_icons

```yaml
kind: method
signature: 'get_value_item_icons( (MaxDevice)arg1, (DeviceParameter)arg2) -> list :'
cpp_signature: boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)
args:
- name: device_parameter
  type: Live.DeviceParameter.DeviceParameter
  refinement:
    name:
      probed: arg2
      sources:
      - '[C++ signature] type `DeviceParameter`; method operates on parameter values.'
returns:
  type: list[str]
  refinement:
    type:
      probed: list
      confidence: high
      sources:
      - '[docstring] "list of icon identifier strings".'
raw_doc: Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should
  be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.
```

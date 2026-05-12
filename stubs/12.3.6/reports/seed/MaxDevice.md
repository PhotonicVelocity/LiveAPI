---
module: MaxDevice
---

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
settable: false
listenable: true
raw_doc: Const access to a list of all midi outputs of the device.
```

##### midi_outputs

```yaml
kind: property
type: Live.Base.Vector
settable: false
listenable: true
raw_doc: Const access to a list of all midi outputs of the device.
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
- name: arg2
  type: int
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
- name: arg2
  type: int
returns:
  type: list
raw_doc: Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the
  best-of bank. This function is related to hardware control surfaces.
```

##### get_value_item_icons

```yaml
kind: method
signature: 'get_value_item_icons( (MaxDevice)arg1, (DeviceParameter)arg2) -> list :'
cpp_signature: boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)
args:
- name: arg2
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: list
raw_doc: Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should
  be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.
```

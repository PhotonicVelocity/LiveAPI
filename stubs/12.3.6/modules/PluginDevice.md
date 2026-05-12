---
module: PluginDevice
---

Represents a third-party VST, AU, or CLAP plug-in hosted by Live. The
`PluginDevice` class extends `Device` with the plug-in's program list, the
ability to step through factory presets, and the larger parameter surface
exposed by external plug-ins.

## Classes

### PluginDevice

```yaml
kind: class
path: Live.PluginDevice.PluginDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a plugin device.
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

##### presets

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Get the list of presets the plugin offers.
```

##### selected_preset_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the index of the currently selected preset.
```

#### Methods

##### get_parameter_names

```yaml
kind: method
signature: 'get_parameter_names( (PluginDevice)arg1 [, (int)begin=0 [, (int)end=-1]]) -> StringVector :'
cpp_signature: std::__1::vector<TString, std::__1::allocator<TString>> get_parameter_names(TPluginDevicePyHandle [,int=0 [,int=-1]])
args:
- name: begin
  type: int
  optional: true
  default: '0'
- name: end
  type: int
  optional: true
  default: '-1'
returns:
  type: Live.Base.StringVector
raw_doc: |-
  Get the range of plugin parameter names, bound by begin and end.
  If end is smaller than 0 it is interpreted as the parameter count.
```

---
module: HybridReverbDevice
---

Represents an instance of Hybrid Reverb, Live's convolution-and-algorithm
reverb. The `HybridReverbDevice` class extends `Device` with the impulse-
response selection and reverb-mode state unique to the device.

## Classes

### HybridReverbDevice

```yaml
kind: class
path: Live.HybridReverbDevice.HybridReverbDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Hybrid Reverb device.
```

#### Properties

##### ir_attack_time

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Return the current IrAttackTime
```

##### ir_category_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current IR category index
```

##### ir_category_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the current IR categories list
```

##### ir_decay_time

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Return the current IrDecayTime
```

##### ir_file_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current IR file index
```

##### ir_file_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current IR file list
```

##### ir_size_factor

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Return the current IrSizeFactor
```

##### ir_time_shaping_on

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Return the current IrTimeShapingOn
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

---
module: RoarDevice
---

Represents an instance of Roar, Live's multi-stage saturation and
distortion effect. The `RoarDevice` class extends `Device` with the
routing-mode and stage-arrangement state unique to Roar.

## Classes

### RoarDevice

```yaml
kind: class
path: Live.RoarDevice.RoarDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Roar device.
```

#### Properties

##### env_listen

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Return the Envelope Input Listen toggle state
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

##### routing_mode_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the routing mode index
```

##### routing_mode_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the routing mode list
```

---
module: CompressorDevice
---

## Classes

### CompressorDevice

```yaml
kind: class
path: Live.CompressorDevice.CompressorDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Compressor device.
```

#### Properties

##### available_input_routing_channels

```yaml
kind: property
type: Live.Track.RoutingChannelVector
settable: false
listenable: true
raw_doc: Return a list of source channels for input routing in the sidechain.
```

##### available_input_routing_types

```yaml
kind: property
type: Live.Track.RoutingTypeVector
settable: false
listenable: true
raw_doc: Return a list of source types for input routing in the sidechain.
```

##### input_routing_channel

```yaml
kind: property
type: Live.Track.RoutingChannel
settable: true
listenable: true
raw_doc: |-
  Get and set the current source channel for input routing in the sidechain.
  Raises ValueError if the channel isn't one of the current values in
  available_input_routing_channels.
```

##### input_routing_type

```yaml
kind: property
type: Live.Track.RoutingType
settable: true
listenable: true
raw_doc: |-
  Get and set the current source type for input routing in the sidechain.
  Raises ValueError if the type isn't one of the current values in
  available_input_routing_types.
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

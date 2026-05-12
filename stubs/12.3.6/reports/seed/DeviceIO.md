---
module: DeviceIO
---

## Classes

### DeviceIO

```yaml
kind: class
path: Live.DeviceIO.DeviceIO
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a specific input or output bus of a device.
```

#### Properties

##### available_routing_channels

```yaml
kind: property
type: Live.Track.RoutingChannelVector
settable: false
listenable: true
raw_doc: Return a list of channels for this IO endpoint.
```

##### available_routing_types

```yaml
kind: property
type: Live.Track.RoutingTypeVector
settable: false
listenable: true
raw_doc: Return a list of available routing types for this IO endpoint.
```

##### canonical_parent

```yaml
kind: property
type: Live.MaxDevice.MaxDevice
settable: false
raw_doc: Get the canonical parent of the device IO.
```

##### default_external_routing_channel_is_none

```yaml
kind: property
type: bool
settable: true
raw_doc: Get and set whether the default routing channel for External routing types is none.
```

##### routing_channel

```yaml
kind: property
type: Live.Track.RoutingChannel
settable: true
listenable: true
raw_doc: |-
  Get and set the current routing channel.
  Raises ValueError if the channel isn't one of the current values in
  available_routing_channels.
```

##### routing_type

```yaml
kind: property
type: Live.Track.RoutingType
settable: true
listenable: true
raw_doc: |-
  Get and set the current routing type.
  Raises ValueError if the type isn't one of the current values in
  available_routing_types.
```

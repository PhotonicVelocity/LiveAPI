---
module: DrumChain
---

## Classes

### DrumChain

```yaml
kind: class
path: Live.DrumChain.DrumChain
ancestors:
- Live.Chain.Chain
- Live.Track.DeviceContainer
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a drum group device chain in Live.
```

#### Properties

##### choke_group

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the chain's choke group setting.
```

##### color

```yaml
kind: property
type: int
settable: true
raw_doc: Access the color index of the Chain.
```

##### color_index

```yaml
kind: property
type: int
settable: true
raw_doc: Access the color index of the Chain.
```

##### devices

```yaml
kind: property
type: Live.Base.Vector[Live.RackDevice.RackDevice]
settable: false
raw_doc: Return const access to all available Devices that are present in the chains
```

##### in_note

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the incoming MIDI note that will trigger this chain.
```

##### is_auto_colored

```yaml
kind: property
type: bool
settable: true
raw_doc: |-
  Get/set access to the auto color flag of the Chain.
  If True, the Chain will always have the same color as the containing
  Track or Chain.
```

##### mute

```yaml
kind: property
type: bool
settable: true
raw_doc: Mute/unmute the chain.
```

##### muted_via_solo

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  Return const access to whether this chain is muted due to some other chain
  being soloed.
```

##### name

```yaml
kind: property
type: str
settable: true
raw_doc: Read/write access to the name of the Chain, as visible in the track header.
```

##### out_note

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the MIDI note sent to the devices in the chain.
```

##### solo

```yaml
kind: property
type: bool
settable: true
raw_doc: |-
  Get/Set the solo status of the chain. Note that this will not disable the
  solo state of any other Chain in the same rack. If you want exclusive solo,
  you have to disable the solo state of the other Chains manually.
```

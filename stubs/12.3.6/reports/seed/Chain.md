---
module: Chain
---

## Classes

### Chain

```yaml
kind: class
path: Live.Chain.Chain
ancestors:
- Live.Track.DeviceContainer
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a group device chain in Live.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.RackDevice.RackDevice
settable: false
raw_doc: Get the canonical parent of the chain.
```

##### color

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access the color index of the Chain.
```

##### color_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access the color index of the Chain.
```

##### devices

```yaml
kind: property
type: Live.Base.Vector[Live.LomObject.LomObject]
settable: false
listenable: true
raw_doc: Return const access to all available Devices that are present in the chains
```

##### has_audio_input

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain can be feed with an Audio signal. This is
  true for all Audio Chains.
```

##### has_audio_output

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain sends out an Audio signal. This is
  true for all Audio Chains, and MIDI chains with an Instrument.
```

##### has_midi_input

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain can be feed with an Audio signal. This is
  true for all MIDI Chains.
```

##### has_midi_output

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain sends out MIDI events. This is
  true for all MIDI Chains with no Instruments.
```

##### is_auto_colored

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/set access to the auto color flag of the Chain.
  If True, the Chain will always have the same color as the containing
  Track or Chain.
```

##### mixer_device

```yaml
kind: property
type: Live.ChainMixerDevice.ChainMixerDevice
settable: false
raw_doc: |-
  Return access to the mixer device that holds the chain's mixer parameters:
  the Volume, Pan, and Sendamounts.
```

##### mute

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Mute/unmute the chain.
```

##### muted_via_solo

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Return const access to whether this chain is muted due to some other chain
  being soloed.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write access to the name of the Chain, as visible in the track header.
```

##### solo

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the solo status of the chain. Note that this will not disable the
  solo state of any other Chain in the same rack. If you want exclusive solo,
  you have to disable the solo state of the other Chains manually.
```

#### Methods

##### delete_device

```yaml
kind: method
signature: 'delete_device( (Chain)arg1, (int)arg2) -> None :'
cpp_signature: void delete_device(TChainPyHandle,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: Remove a device identified by its index from the chain. Throws runtime error if bad index.
```

##### duplicate_device

```yaml
kind: method
signature: 'duplicate_device( (Chain)arg1, (int)arg2) -> None :'
cpp_signature: void duplicate_device(TChainPyHandle,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: Duplicate the device at the given index in the chain.
```

##### insert_device

```yaml
kind: method
signature: 'insert_device( (Chain)arg1, (str)DeviceName [, (int)DeviceIndex=-1]) -> LomObject :'
cpp_signature: TWeakPtr<TPyHandleBase> insert_device(TChainPyHandle,std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>> [,int=-1])
args:
- name: device_name
  type: str
- name: device_index
  type: int
  optional: true
  default: '-1'
returns:
  type: Live.LomObject.LomObject
raw_doc: Add a device at a given index in the chain. At end if -1.
```

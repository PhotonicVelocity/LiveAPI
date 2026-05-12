---
module: DrumPad
---

Represents a single pad in a Drum Rack — the per-note address that maps an
incoming MIDI note to a `DrumChain`. The `DrumPad` class exposes the pad's
note, name, mute/solo state, and the chains routed to it.

## Classes

### DrumPad

```yaml
kind: class
path: Live.DrumPad.DrumPad
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a drum group device pad in Live.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.RackDevice.RackDevice
settable: false
raw_doc: Get the canonical parent of the drum pad.
```

##### chains

```yaml
kind: property
type: Live.Base.Vector
element_type: Live.Chain.Chain
settable: false
listenable: true
raw_doc: Return const access to the list of chains in this drum pad.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "Return const access to the list of chains in this drum pad."'
    - '[M4L] drumpad.md: `chains [Chain] read-only observe`.'
    - '[corpus] pushbase/device_chain_utils.py:14 reads `drum_pad.chains[0].devices`.'
```

##### mute

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Mute/unmute the pad.
```

##### name

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: Return const access to the drum pad's name. It depends on the contained chains.
```

##### note

```yaml
kind: property
type: int
settable: false
raw_doc: Get the MIDI note of the drum pad.
```

##### solo

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Solo/unsolo the pad.
```

#### Methods

##### delete_all_chains

```yaml
kind: method
signature: 'delete_all_chains( (DrumPad)arg1) -> None :'
cpp_signature: void delete_all_chains(TPyHandle<ADrumGroupDevicePad>)
returns:
  type: None
raw_doc: Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.
```

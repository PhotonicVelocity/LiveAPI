---
module: ChainMixerDevice
---

Represents the mixer attached to a single rack `Chain`. The
`ChainMixerDevice` class exposes the chain's volume, pan, mute, solo, and
per-chain sends as `DeviceParameter` objects.

## Classes

### ChainMixerDevice

```yaml
kind: class
path: Live.ChainMixerDevice.ChainMixerDevice
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: |-
  This class represents a Chain's Mixer Device in Live, which gives you
  access to the Volume, Panning, and Send properties of a Chain.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Chain.Chain
settable: false
raw_doc: Get the canonical parent of the mixer device.
```

##### chain_activator

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Chain's Activator Device Parameter.
```

##### panning

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Chain's Panning Device Parameter.
```

##### sends

```yaml
kind: property
type: Live.Base.Vector
element_type: Live.DeviceParameter.DeviceParameter
settable: false
listenable: true
raw_doc: Const access to the Chain's list of Send Amount Device Parameters.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "Const access to the Chain''s list of Send Amount Device Parameters."'
    - '[M4L] chainmixerdevice.md: `sends list of DeviceParameter read-only observe`.'
    - '[corpus] pushbase/selected_track_parameter_provider.py:44 does `params += list(mixer.sends)` — params is a list of
      DeviceParameter.'
```

##### volume

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Chain's Volume Device Parameter.
```

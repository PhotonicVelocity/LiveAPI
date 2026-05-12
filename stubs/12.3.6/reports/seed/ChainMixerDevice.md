---
module: ChainMixerDevice
---

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
settable: false
listenable: true
raw_doc: Const access to the Chain's list of Send Amount Device Parameters.
```

##### volume

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Chain's Volume Device Parameter.
```

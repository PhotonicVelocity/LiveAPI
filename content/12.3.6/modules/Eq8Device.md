---
module: Eq8Device
---

Represents an instance of EQ Eight, Live's eight-band parametric equalizer.
The `Eq8Device` class extends `Device` with the per-band frequency, gain,
and Q controls plus EQ Eight's analyzer state.

## Classes

### Eq8Device

```yaml
kind: class
path: Live.Eq8Device.Eq8Device
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents an Eq8 device.
```

#### Properties

##### edit_mode

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Access to Eq8's edit mode.
```

##### global_mode

```yaml
kind: property
type: Live.Eq8Device.GlobalMode
settable: true
listenable: true
raw_doc: Access to Eq8's global mode.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `GlobalMode` enum in same module (Eq8Device). Property name is a direct snake-case match.'
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

##### oversample

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Access to Eq8's oversample value.
```

##### parameters

```yaml
kind: property
type: Live.Device.ATimeableValueVector
settable: false
raw_doc: Const access to the list of available automatable parameters for this device.
```

##### view

```yaml
kind: property
type: Live.Eq8Device.Eq8Device.View
settable: false
raw_doc: Representing the view aspects of a device.
```

### View

```yaml
kind: class
path: Live.Eq8Device.Eq8Device.View
parent: Eq8Device
ancestors:
- Live.Device.Device.View
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of an Eq8 device.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Eq8Device.Eq8Device
settable: false
raw_doc: Get the canonical parent of the View.
```

##### is_collapsed

```yaml
kind: property
type: bool
settable: true
raw_doc: Get/Set/Listen if the device is shown collapsed in the device chain.
```

##### selected_band

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the selected filter band.
```

## Enums

### EditMode

```yaml
kind: enum
members:
  a: 0
  b: 1
```

### GlobalMode

```yaml
kind: enum
members:
  stereo: 0
  left_right: 1
  mid_side: 2
```

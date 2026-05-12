---
module: SpectralResonatorDevice
---

## Classes

### SpectralResonatorDevice

```yaml
kind: class
path: Live.SpectralResonatorDevice.SpectralResonatorDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Spectral Resonator device.
```

#### Properties

##### frequency_dial_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current frequency dial mode index
```

##### frequency_dial_mode_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current frequency dial mode list
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

##### midi_gate

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current midi gate index
```

##### midi_gate_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current midi gate list
```

##### mod_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current mod mode index
```

##### mod_mode_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current mod mode list
```

##### mono_poly

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current mono poly mode index
```

##### mono_poly_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current mono poly mode list
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

##### pitch_bend_range

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current pitch bend range
```

##### pitch_mode

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current pitch mode index
```

##### pitch_mode_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Return the current pitch mode list
```

##### polyphony

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current polyphony
```

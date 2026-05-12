---
module: Device
---

## Classes

### Device

```yaml
kind: class
path: Live.Device.Device
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a MIDI or Audio DSP-Device in Live.
```

#### Properties

##### can_compare_ab

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if the Device has the capability to AB compare.
```

##### can_have_chains

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if the device is a rack.
```

##### can_have_drum_pads

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if the device is a drum rack.
```

##### canonical_parent

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Get the canonical parent of the Device.
```

##### class_display_name

```yaml
kind: property
type: str
settable: false
raw_doc: Return const access to the name of the device's class name as displayed in Live's browser and device chain
```

##### class_name

```yaml
kind: property
type: str
settable: false
raw_doc: Return const access to the name of the device's class.
```

##### is_active

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Return const access to whether this device is active. This will be false bothwhen the device is off and when it's
  inside a rack device which is off.
```

##### is_using_compare_preset_b

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
```

##### latency_in_ms

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Returns the latency of the device in ms.
```

##### latency_in_samples

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Returns the latency of the device in samples.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Return access to the name of the device.
```

##### parameters

```yaml
kind: property
type: Live.Device.ATimeableValueVector
settable: false
listenable: true
raw_doc: Const access to the list of available automatable parameters for this device.
```

##### type

```yaml
kind: property
type: Live.Device.DeviceType
settable: false
raw_doc: Return the type of the device.
```

##### view

```yaml
kind: property
type: Live.Device.Device.View
settable: false
raw_doc: Representing the view aspects of a device.
```

#### Methods

##### save_preset_to_compare_ab_slot

```yaml
kind: method
signature: 'save_preset_to_compare_ab_slot( (Device)arg1) -> None :'
cpp_signature: void save_preset_to_compare_ab_slot(TPyHandle<ADevice>)
returns:
  type: None
raw_doc: Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
```

##### store_chosen_bank

```yaml
kind: method
signature: 'store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :'
cpp_signature: void store_chosen_bank(TPyHandle<ADevice>,int,int)
args:
- name: arg2
  type: int
- name: arg3
  type: int
returns:
  type: None
raw_doc: Set the selected bank in the device for persistency.
```

### ATimeableValueVector

```yaml
kind: class
path: Live.Device.ATimeableValueVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.DeviceParameter.DeviceParameter
```

### View

```yaml
kind: class
path: Live.Device.Device.View
parent: Device
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of a device.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Device.Device
settable: false
raw_doc: Get the canonical parent of the View.
```

##### is_collapsed

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Get/Set/Listen if the device is shown collapsed in the device chain.
```

## Enums

### DeviceType

```yaml
kind: enum
members:
  undefined: 0
  instrument: 1
  audio_effect: 2
  midi_effect: 4
raw_doc: The type of the device.
```

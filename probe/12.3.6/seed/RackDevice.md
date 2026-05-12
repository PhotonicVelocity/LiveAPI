---
module: RackDevice
---

## Classes

### RackDevice

```yaml
kind: class
path: Live.RackDevice.RackDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Rack device.
```

#### Properties

##### can_show_chains

```yaml
kind: property
type: bool
settable: false
raw_doc: return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.
```

##### chain_selector

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the chain selector parameter.
```

##### chains

```yaml
kind: property
type: Live.Base.Vector
settable: false
listenable: true
raw_doc: Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.
```

##### drum_pads

```yaml
kind: property
type: Live.Base.Vector[Live.DrumPad.DrumPad]
settable: false
listenable: true
raw_doc: Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.
```

##### has_drum_pads

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.
```

##### has_macro_mappings

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if any of the rack's macros are mapped to a parameter.
```

##### is_active

```yaml
kind: property
type: bool
settable: false
raw_doc: Return const access to whether this device is active. This will be false bothwhen the device is off and when it's
  inside a rack device which is off.
```

##### is_showing_chains

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Returns True, if it is showing chains.
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

##### macros_mapped

```yaml
kind: property
type: tuple[bool, ...]
settable: false
listenable: true
raw_doc: A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something
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

##### return_chains

```yaml
kind: property
type: Live.Base.Vector
settable: false
listenable: true
raw_doc: Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.
```

##### selected_variation_index

```yaml
kind: property
type: int
settable: true
raw_doc: Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.
```

##### variation_count

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the number of macro variations currently stored.
```

##### view

```yaml
kind: property
type: Live.RackDevice.RackDevice.View
settable: false
raw_doc: Representing the view aspects of a device.
```

##### visible_drum_pads

```yaml
kind: property
type: Live.Base.Vector[Live.DrumPad.DrumPad]
settable: false
listenable: true
raw_doc: Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is
  false.
```

##### visible_macro_count

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Access to the number of macros that are currently visible.
```

#### Methods

##### add_macro

```yaml
kind: method
signature: 'add_macro( (RackDevice)arg1) -> None :'
cpp_signature: void add_macro(TRackDevicePyHandle)
returns:
  type: None
raw_doc: Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls
  is reached.
```

##### copy_pad

```yaml
kind: method
signature: 'copy_pad( (RackDevice)arg1, (int)arg2, (int)arg3) -> None :'
cpp_signature: void copy_pad(TRackDevicePyHandle,int,int)
args:
- name: arg2
  type: int
- name: arg3
  type: int
returns:
  type: None
raw_doc: Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index)
  where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception
  when the source pad is empty, or when the source or destination indices are not between 0 - 127.
```

##### delete_selected_variation

```yaml
kind: method
signature: 'delete_selected_variation( (Device)arg1) -> None :'
cpp_signature: void delete_selected_variation(TPyHandle<ADevice>)
self_type: Live.Device.Device
returns:
  type: None
raw_doc: Deletes the currently selected macro variation.Does nothing if there is no selected variation.
```

##### insert_chain

```yaml
kind: method
signature: 'insert_chain( (RackDevice)arg1 [, (int)Index=-1]) -> LomObject :'
cpp_signature: TWeakPtr<TPyHandleBase> insert_chain(TRackDevicePyHandle [,int=-1])
args:
- name: index
  type: int
  optional: true
  default: '-1'
returns:
  type: Live.LomObject.LomObject
raw_doc: Inserts a new chain, either at the specified index or, if not index was specified, at the end of the chain sequence.
```

##### randomize_macros

```yaml
kind: method
signature: 'randomize_macros( (RackDevice)arg1) -> None :'
cpp_signature: void randomize_macros(TRackDevicePyHandle)
returns:
  type: None
raw_doc: Randomizes the values for all macro controls not excluded from randomization.
```

##### recall_last_used_variation

```yaml
kind: method
signature: 'recall_last_used_variation( (Device)arg1) -> None :'
cpp_signature: void recall_last_used_variation(TPyHandle<ADevice>)
self_type: Live.Device.Device
returns:
  type: None
raw_doc: Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.
```

##### recall_selected_variation

```yaml
kind: method
signature: 'recall_selected_variation( (Device)arg1) -> None :'
cpp_signature: void recall_selected_variation(TPyHandle<ADevice>)
self_type: Live.Device.Device
returns:
  type: None
raw_doc: Recalls the currently selected macro variation.Does nothing if there are no variations.
```

##### remove_macro

```yaml
kind: method
signature: 'remove_macro( (RackDevice)arg1) -> None :'
cpp_signature: void remove_macro(TRackDevicePyHandle)
returns:
  type: None
raw_doc: Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls
  is reached.
```

##### store_variation

```yaml
kind: method
signature: 'store_variation( (Device)arg1) -> None :'
cpp_signature: void store_variation(TPyHandle<ADevice>)
self_type: Live.Device.Device
returns:
  type: None
raw_doc: Stores a new variation of the values of all currently mapped macros
```

### View

```yaml
kind: class
path: Live.RackDevice.RackDevice.View
parent: RackDevice
ancestors:
- Live.Device.Device.View
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Representing the view aspects of a rack device.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.RackDevice.RackDevice
settable: false
raw_doc: Get the canonical parent of the View.
```

##### drum_pads_scroll_position

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.
```

##### is_collapsed

```yaml
kind: property
type: bool
settable: true
raw_doc: Get/Set/Listen if the device is shown collapsed in the device chain.
```

##### is_showing_chain_devices

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is
  false.
```

##### selected_chain

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Return access to the currently selected chain.
```

##### selected_drum_pad

```yaml
kind: property
type: Live.DrumPad.DrumPad
settable: true
listenable: true
raw_doc: Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
```

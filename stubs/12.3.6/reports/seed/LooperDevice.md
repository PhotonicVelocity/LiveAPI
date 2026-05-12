---
module: LooperDevice
---

## Classes

### LooperDevice

```yaml
kind: class
path: Live.LooperDevice.LooperDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Looper device.
```

#### Properties

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

##### loop_length

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: The length of Looper's buffer.
```

##### name

```yaml
kind: property
type: str
settable: true
raw_doc: Return access to the name of the device.
```

##### overdub_after_record

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch
  will be to playback without overdubbing.
```

##### parameters

```yaml
kind: property
type: Live.Device.ATimeableValueVector
settable: false
raw_doc: Const access to the list of available automatable parameters for this device.
```

##### record_length_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access to the Record Length chooser entry index.
```

##### record_length_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Read-only access to the list of Record Length chooser entry strings.
```

##### tempo

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: The tempo of Looper's buffer.
```

#### Methods

##### clear

```yaml
kind: method
signature: 'clear( (LooperDevice)arg1) -> None :'
cpp_signature: void clear(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Erase Looper's recorded content.
```

##### double_length

```yaml
kind: method
signature: 'double_length( (LooperDevice)arg1) -> None :'
cpp_signature: void double_length(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Double the length of Looper's buffer.
```

##### double_speed

```yaml
kind: method
signature: 'double_speed( (LooperDevice)arg1) -> None :'
cpp_signature: void double_speed(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Double the speed of Looper's playback.
```

##### export_to_clip_slot

```yaml
kind: method
signature: 'export_to_clip_slot( (LooperDevice)arg1, (ClipSlot)arg2) -> None :'
cpp_signature: void export_to_clip_slot(TLooperDevicePyHandle,TPyHandle<AGroupAndClipSlotBase>)
args:
- name: arg2
  type: Live.ClipSlot.ClipSlot
returns:
  type: None
raw_doc: Export Looper's content to a Session Clip Slot.
```

##### half_length

```yaml
kind: method
signature: 'half_length( (LooperDevice)arg1) -> None :'
cpp_signature: void half_length(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Halve the length of Looper's buffer.
```

##### half_speed

```yaml
kind: method
signature: 'half_speed( (LooperDevice)arg1) -> None :'
cpp_signature: void half_speed(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Halve the speed of Looper's playback.
```

##### overdub

```yaml
kind: method
signature: 'overdub( (LooperDevice)arg1) -> None :'
cpp_signature: void overdub(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Play back while adding additional layers of incoming audio.
```

##### play

```yaml
kind: method
signature: 'play( (LooperDevice)arg1) -> None :'
cpp_signature: void play(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Play back without overdubbing.
```

##### record

```yaml
kind: method
signature: 'record( (LooperDevice)arg1) -> None :'
cpp_signature: void record(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Record incoming audio.
```

##### stop

```yaml
kind: method
signature: 'stop( (LooperDevice)arg1) -> None :'
cpp_signature: void stop(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Stop Looper's playback.
```

##### undo

```yaml
kind: method
signature: 'undo( (LooperDevice)arg1) -> None :'
cpp_signature: void undo(TLooperDevicePyHandle)
returns:
  type: None
raw_doc: Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the
  material erased by the previous undooperation.
```

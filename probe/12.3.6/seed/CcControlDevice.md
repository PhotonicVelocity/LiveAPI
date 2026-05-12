---
module: CcControlDevice
---

## Classes

### CcControlDevice

```yaml
kind: class
path: Live.CcControlDevice.CcControlDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a CcControl device.
```

#### Properties

##### custom_bool_target

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom bool target
```

##### custom_bool_target_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom bool target list
```

##### custom_float_target_0

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 0
```

##### custom_float_target_0_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 0 list
```

##### custom_float_target_1

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 1
```

##### custom_float_target_10

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 10
```

##### custom_float_target_10_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 10 list
```

##### custom_float_target_11

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 11
```

##### custom_float_target_11_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 11 list
```

##### custom_float_target_1_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 1 list
```

##### custom_float_target_2

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 2
```

##### custom_float_target_2_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 2 list
```

##### custom_float_target_3

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 3
```

##### custom_float_target_3_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 3 list
```

##### custom_float_target_4

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 4
```

##### custom_float_target_4_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 4 list
```

##### custom_float_target_5

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 5
```

##### custom_float_target_5_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 5 list
```

##### custom_float_target_6

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 6
```

##### custom_float_target_6_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 6 list
```

##### custom_float_target_7

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 7
```

##### custom_float_target_7_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 7 list
```

##### custom_float_target_8

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 8
```

##### custom_float_target_8_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 8 list
```

##### custom_float_target_9

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the custom float target 9
```

##### custom_float_target_9_list

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Return the custom float target 9 list
```

#### Methods

##### resend

```yaml
kind: method
signature: 'resend( (CcControlDevice)self) -> None :'
cpp_signature: void resend(TCcControlDevicePyHandle)
returns:
  type: None
raw_doc: Resend all CC values.
```

---
module: WavetableDevice
---

Represents an instance of Wavetable, Live's wavetable synthesizer. The
`WavetableDevice` class extends `Device` with the per-oscillator wavetable
selection and modulation-matrix state unique to the instrument.

## Classes

### WavetableDevice

```yaml
kind: class
path: Live.WavetableDevice.WavetableDevice
ancestors:
- Live.Device.Device
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Wavetable device.
```

#### Properties

##### filter_routing

```yaml
kind: property
type: Live.WavetableDevice.FilterRouting
settable: true
listenable: true
raw_doc: Return the current filter routing.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `FilterRouting` enum in same module (WavetableDevice). Property name is a direct snake-case match.'
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

##### mono_poly

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current voicing mode.
```

##### name

```yaml
kind: property
type: str
settable: true
raw_doc: Return access to the name of the device.
```

##### oscillator_1_effect_mode

```yaml
kind: property
type: Live.WavetableDevice.EffectMode
settable: true
listenable: true
raw_doc: Return the current effect mode of the oscillator 1.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `EffectMode` enum in same module (WavetableDevice). Property name ends in `effect_mode`; the enum is
      the only one matching that suffix.'
```

##### oscillator_1_wavetable_category

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current wavetable category of the oscillator 1.
```

##### oscillator_1_wavetable_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current wavetable index of the oscillator 1.
```

##### oscillator_1_wavetables

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Get a vector of oscillator 1's wavetable names.
```

##### oscillator_2_effect_mode

```yaml
kind: property
type: Live.WavetableDevice.EffectMode
settable: true
listenable: true
raw_doc: Return the current effect mode of the oscillator 2.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] same as oscillator_1_effect_mode — sister property, same enum.'
```

##### oscillator_2_wavetable_category

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current wavetable category of the oscillator 2.
```

##### oscillator_2_wavetable_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current wavetable index of the oscillator 2.
```

##### oscillator_2_wavetables

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Get a vector of oscillator 2's wavetable names.
```

##### oscillator_wavetable_categories

```yaml
kind: property
type: Live.Base.StringVector
settable: false
raw_doc: Get a vector of the available wavetable categories.
```

##### parameters

```yaml
kind: property
type: Live.Device.ATimeableValueVector
settable: false
raw_doc: Const access to the list of available automatable parameters for this device.
```

##### poly_voices

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Return the current number of polyphonic voices. Uses the VoiceCount enumeration.
```

##### unison_mode

```yaml
kind: property
type: Live.WavetableDevice.UnisonMode
settable: true
listenable: true
raw_doc: Return the current unison mode.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `UnisonMode` enum in same module (WavetableDevice). Property name is a direct snake-case match.'
```

##### unison_voice_count

```yaml
kind: property
type: Live.WavetableDevice.VoiceCount
settable: true
listenable: true
raw_doc: Return the current number of unison voices.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[sister method] `VoiceCount` enum in same module (WavetableDevice). Property name ends in `voice_count`; `VoiceCount`
      is the only enum matching that suffix.'
```

##### visible_modulation_target_names

```yaml
kind: property
type: Live.Base.StringVector
settable: false
listenable: true
raw_doc: Get the names of all the visible modulation targets.
```

##### modulation_matrix_changed

```yaml
kind: property
listenable: true
```

Fires when the Wavetable device's modulation matrix is
reconfigured — modulation source / destination wiring
changes. Programmatic triggers include
`add_parameter_to_modulation_matrix` and
`set_modulation_value`. Read the matrix via
`get_modulation_value`,
`get_modulation_target_parameter_name`, and
`is_parameter_modulatable`.

#### Methods

##### add_parameter_to_modulation_matrix

```yaml
kind: method
signature: 'add_parameter_to_modulation_matrix( (WavetableDevice)self, (DeviceParameter)parameter) -> int :'
cpp_signature: int add_parameter_to_modulation_matrix(TWavetableDevicePyHandle,TPyHandle<ATimeableValue>)
args:
- name: parameter
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: int
raw_doc: Add a non-pitch parameter to the modulation matrix.
```

##### get_modulation_target_parameter_name

```yaml
kind: method
signature: 'get_modulation_target_parameter_name( (WavetableDevice)self, (int)target_index) -> str :'
cpp_signature: TString get_modulation_target_parameter_name(TWavetableDevicePyHandle,int)
args:
- name: target_index
  type: int
returns:
  type: str
raw_doc: Get the parameter name of the modulation target at the given index.
```

##### get_modulation_value

```yaml
kind: method
signature: 'get_modulation_value( (WavetableDevice)self, (int)target_index, (int)source) -> float :'
cpp_signature: float get_modulation_value(TWavetableDevicePyHandle,int,int)
args:
- name: target_index
  type: int
- name: source
  type: int
returns:
  type: float
raw_doc: Get the value of a modulation amount for the given target-source connection.
```

##### is_parameter_modulatable

```yaml
kind: method
signature: 'is_parameter_modulatable( (WavetableDevice)self, (DeviceParameter)parameter) -> bool :'
cpp_signature: bool is_parameter_modulatable(TWavetableDevicePyHandle,TPyHandle<ATimeableValue>)
args:
- name: parameter
  type: Live.DeviceParameter.DeviceParameter
returns:
  type: bool
raw_doc: Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled
  there.
```

##### set_modulation_value

```yaml
kind: method
signature: 'set_modulation_value( (WavetableDevice)self, (int)target_index, (int)source, (float)value) -> None :'
cpp_signature: void set_modulation_value(TWavetableDevicePyHandle,int,int,float)
args:
- name: target_index
  type: int
- name: source
  type: int
- name: value
  type: float
returns:
  type: None
raw_doc: Set the value of a modulation amount for the given target-source connection.
```

## Enums

### EffectMode

```yaml
kind: enum
members:
  none: 0
  frequency_modulation: 1
  sync_and_pulse_width: 2
  warp_and_fold: 3
```

### FilterRouting

```yaml
kind: enum
members:
  serial: 0
  parallel: 1
  split: 2
```

### ModulationSource

```yaml
kind: enum
members:
  amp_envelope: 0
  envelope_2: 1
  envelope_3: 2
  lfo_1: 3
  lfo_2: 4
  midi_velocity: 5
  midi_note: 6
  midi_pitch_bend: 7
  midi_channel_pressure: 8
  midi_mod_wheel: 9
  midi_random: 10
```

### UnisonMode

```yaml
kind: enum
members:
  none: 0
  classic: 1
  slow_shimmer: 2
  fast_shimmer: 3
  phase_sync: 4
  position_spread: 5
  random_note: 6
```

### VoiceCount

```yaml
kind: enum
members:
  two: 0
  three: 1
  four: 2
  five: 3
  six: 4
  seven: 5
  eight: 6
```

### Voicing

```yaml
kind: enum
members:
  mono: 0
  poly: 1
```

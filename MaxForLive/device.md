# Device

This class represents a MIDI or audio device in Live.

## Canonical Paths

```
live_set tracks N devices M
```

```
live_set tracks N devices M chains L devices K
```

```
live_set tracks N devices M return_chains L devices K
```

## Children

### parameters list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

Only automatable parameters are accessible. See [DeviceParameter](#DeviceParameter) to learn how to modify them.

### view [Device.View](/apiref/lom/device_view/ "Device.View") read-only

## Properties

### can_have_chains bool read-only

0 for a single device   
1 for a device Rack

### can_have_drum_pads bool read-only

1 for Drum Racks

### class_display_name symbol read-only

Get the original name of the device (e.g. `Operator`, `Auto Filter`).

### class_name symbol read-only

Live device type such as `MidiChord`, `Operator`, `Limiter`, `MxDeviceAudioEffect`, or `PluginDevice`.

### is_active bool read-onlyobserve

0 = either the device itself or its enclosing Rack device is off.

### name symbol observe

This is the string shown in the title bar of the device.

### type int read-only

The type of the device. Possible types are: 0 = undefined, 1 = instrument, 2 = audio_effect, 4 = midi_effect.

### latency_in_samples int read-onlyobserve

Device latency in samples.

### latency_in_ms float read-onlyobserve

Device latency in milliseconds.

### can_compare_ab bool read-only

1 for devices that support the AB Compare feature. 0 otherwise.   
  
*Available since Live 12.3.*

### is_using_compare_preset_b bool observe

1 if the device has compare preset B loaded. 0 otherwise.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*

## Functions

### store_chosen_bank

Parameters:   
`script_index` [int]   
`bank_index` [int]   
(This is related to hardware control surfaces and is usually not relevant.)

### save_preset_to_compare_ab_slot

Save the device state to the other compare AB slot.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*

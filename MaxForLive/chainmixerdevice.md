# ChainMixerDevice

This class represents a chain's mixer device in Live.

## Canonical Paths

```
live_set tracks N devices M chains L mixer_device
```

```
live_set tracks N devices M return_chains L mixer_device
```

## Children

### sends list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

[in Audio Effect Racks and Instrument Racks only]   
For Drum Racks, otherwise empty.

### chain_activator [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### panning [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in Audio Effect Racks and Instrument Racks only]

### volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in Audio Effect Racks and Instrument Racks only]

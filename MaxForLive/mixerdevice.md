# MixerDevice

This class represents a mixer device in Live. It provides access to volume, panning and other [DeviceParameter](#DeviceParameter) objects. See [DeviceParameter](#DeviceParameter) to learn how to modify them.

## Canonical Path

```
live_set tracks N mixer_device
```

## Children

### sends list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

One send per return track.

### cue_volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### crossfader [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### left_split_stereo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

The Track's Left Split Stereo Pan Parameter.

### panning [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### right_split_stereo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

The Track's Right Split Stereo Pan Parameter.

### song_tempo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### track_activator [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

## Properties

### crossfade_assign int observe

0 = A, 1 = none, 2 = B [not in master track]

### panning_mode int observe

Access to the Track mixer's pan mode: 0 = Stereo, 1 = Split Stereo.

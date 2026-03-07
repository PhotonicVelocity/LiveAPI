# SimplerDevice

This class represents an instance of Simpler.   
A SimplerDevice is a type of device, meaning that it has all the children, properties and functions that a device has. Listed below are members unique to SimplerDevice.

## Children

### sample [Sample](/apiref/lom/sample/ "Sample") read-onlyobserve

The sample currently loaded into Simpler.

## Properties

### can_warp_as bool read-onlyobserve

1 = warp_as is available.

### can_warp_double bool read-onlyobserve

1 = warp_double is available.

### can_warp_half bool read-onlyobserve

1 = warp_half is available.

### multi_sample_mode bool read-onlyobserve

1 = Simpler is in multisample mode.

### pad_slicing bool observe

1 = slices can be added in Slicing Mode by playing notes which are not yet assigned to existing slices.

### playback_mode int observe

Get/set Simpler's playback mode.   
0 = Classic Mode   
1 = One-Shot Mode   
2 = Slicing Mode

### playing_position float read-onlyobserve

The current playing position in the sample, expressed as a value between 0. and 1.

### playing_position_enabled bool read-onlyobserve

1 = Simpler is playing back the sample and showing the playing position.

### retrigger bool observe

1 = Retrigger is enabled in Simpler.

### slicing_playback_mode int observe

Get/set Simpler's Slicing Playback Mode.   
0 = Mono   
1 = Poly   
2 = Thru

### voices int observe

Get/set the number of Voices.

## Functions

### crop

Crop the loaded sample to the active region between the start and end markers.

### guess_playback_length

Returns: [float] An estimated beat time for the playback length between the start and end markers.

### reverse

Reverse the loaded sample.

### warp_as

Parameters: `beats` [int]   
Warp the active region between the start and end markers as the specified number of beats.

### warp_double

Double the playback tempo of the active region between the start and end markers.

### warp_half

Halve the playback tempo for the active region between the start and end markers.

# Sample

This class represents a sample file loaded into Simpler.

## Canonical Path

```
live_set tracks N devices N sample
```

## Properties

### beats_granulation_resolution int observe

Get/set which divisions to preserve in the sample in Beats Mode.   
0 = 1 Bar   
1 = 1/2   
2 = 1/4   
3 = 1/8   
4 = 1/16   
5 = 1/32   
6 = Transients

### beats_transient_envelope float observe

Get/set the duration of a volume fade applied to each segment of audio in Beats Mode.   
  
0 = fastest decay   
100 = no fade

### beats_transient_loop_mode int observe

Get/set the Transient Loop Mode applied to each segment of audio in Beats Mode.   
0 = Off   
1 = Loop Forward   
2 = Loop Back-and-Forth

### complex_pro_envelope float observe

Get/set the Envelope parameter in Complex Pro Mode.

### complex_pro_formants float observe

Get/set the Formants parameter in Complex Pro Mode.

### end_marker int observe

Get/set the position of the sample's end marker.

### file_path unicode read-onlyobserve

Get the path of the sample file.

### gain float observe

Get/set the sample gain.

### length int read-only

Get the length of the sample file in sample frames.

### sample_rate int read-only

The sample rate of the loaded sample.   
  
*Available since Live 11.0.*

### slices list of int read-onlyobserve

The positions of all playable slices in the sample, in sample frames. Divide these values by the `sample_rate` to get the slice times in seconds.   
  
*Available since Live 11.0.*

### slicing_sensitivity float observe

Get/set the slicing sensitivity. Values are between 0.0 and 1.0.

### start_marker int observe

Get/set the position of the sample's start marker.

### texture_flux float observe

Get/set the Flux parameter in Texture Mode.

### texture_grain_size float observe

Get/set the Grain Size parameter in Texture Mode.

### tones_grain_size float observe

Get/set the Grain Size parameter in Tones Mode.

### warp_markers dict/bang read-onlyobserve

The Sample's Warp Markers as a dict. Observing this property bangs when the warp_markers change.  
  
The last Warp Marker in the dict is not visible in the Live interface. This hidden, or "shadow" marker is used to calculate the BPM of the last segment.   
  
*Available since Live 11.0.*

### warp_mode int observe

Get/set the Warp Mode.   
0 = Beats Mode   
1 = Tones Mode   
2 = Texture Mode   
3 = Re-Pitch Mode   
4 = Complex Mode   
6 = Complex Pro Mode

### warping bool observe

1 = warping is enabled.

### slicing_style int observe

Get/set the Slicing Mode.   
0 = Transient   
1 = Beat   
2 = Region   
3 = Manual

### slicing_beat_division int observe

Get/set the slice beat division in Beat Slicing Mode.   
0 = 1/16   
1 = 1/16T   
2 = 1/8   
3 = 1/8T   
4 = 1/4   
5 = 1/4T   
6 = 1/2   
7 = 1/2T   
8 = 1 Bar   
9 = 2 Bars   
10 = 4 Bars

### slicing_region_count int observe

Get/set the number of slice regions in Region Slicing Mode.

## Functions

### gain_display_string

Returns: [list of symbols] The sample's gain value as a string, e.g. "0.0 dB".

### insert_slice

Parameters: `slice_time` [int]   
Insert a new slice at the specified time if there is none.

### move_slice

Parameters: `source_time` [int] `destination_time` [int]   
Move an existing slice to a specified time.

### remove_slice

Parameters: `slice_time` [int]   
Remove a slice at the specified time if it exists.

### clear_slices

Clear all slices created in Manual Slicing Mode.

### reset_slices

Reset all edited slices to their original positions.

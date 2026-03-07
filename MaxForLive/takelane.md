# TakeLane

This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, which are used for comping. If take lanes exist for a track, they can be shown by right-clicking on a track and choosing Show Take Lanes.

## Canonical Path

```
live_set tracks N take_lanes M
```

## Children

### arrangement_clips list of [Clip](/apiref/lom/clip/ "Clip") read-onlyobserve

The list of this take lane's Arrangement View clip IDs

## Properties

### name symbol observe

The name as shown in the take lane header.

## Functions

### create_audio_clip

Parameters:   
`file_path` [symbol]   
`start_time` [float]   
Given a valid audio file in a supported format, passing its absolute path (on Mac, starting with `/Volumes/(drive name)/`) creates an audio clip referencing the file in the arrangement view at the specified `start_time` in beats.  
  
Prints an error if the track is not an audio track, if the track is frozen or if the track is being recorded into. `start_time` must be within the range `[0., 1576800]`.

### create_midi_clip

Parameters:   
`start_time` [float]   
`length` [float]   
Creates an empty MIDI clip with the specified `length` in beats and inserts it into the arrangement at the specified `start_time` in beats.  
  
Prints an error if the track is not a MIDI track, if the track is frozen or when the track is currently being recorded into. `start_time` must be within the range `[0., 1576800]`.

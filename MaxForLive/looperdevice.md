# LooperDevice

This class represents an instance of a Looper device in Live.   
An LooperDevice has all the properties, functions and children of a Device. Listed below are members unique to LooperDevice.

## Properties

### loop_length float read-onlyobserve

The length of Looper's buffer.

### overdub_after_record bool observe

1 = Looper will switch to overdub after recording, when recording a fixed number of bars. 0 = switch to playback without overdubbing.

### record_length_index int observe

Access to the Record Length chooser entry index.

### record_length_list StringVector read-only

Access to the list of Record Length chooser entry strings.

### tempo float read-onlyobserve

The tempo of Looper's buffer.

## Functions

### clear

Erase Looper's recorded content.

### double_speed

Double the speed of Looper's playback.

### half_speed

Halve the speed of Looper's playback.

### double_length

Double the length of Looper's buffer.

### half_length

Halve the length of Looper's buffer.

### record

Record incoming audio.

### overdub

Play back while adding additional layers of incoming audio.

### play

Play back without overdubbing.

### stop

Stop Looper's playback.

### undo

Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undo operation.

### export_to_clip_slot

Parameter: `clip_slot` [ClipSlot]   
The target clip slot.   
  
Given a valid LOM ID of an empty clip slot on a non-frozen audio track, will export Looper's content to a clip in that slot. This is similar to using the Drag Me! control on the Looper device, and the same restrictions apply: the audio engine must be turned on, the Looper must actually hold audio content, the content must have a fixed length (i.e. Looper must not be recording), etc.

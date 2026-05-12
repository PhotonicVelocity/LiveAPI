---
module: ClipSlot
---

## Classes

### ClipSlot

```yaml
kind: class
path: Live.ClipSlot.ClipSlot
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents an entry in Lives Session view matrix.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Get the canonical parent of the ClipSlot.
```

##### clip

```yaml
kind: property
type: Live.Clip.Clip
settable: false
raw_doc: Returns the Clip which this clipslots currently owns. Might be None.
```

##### color

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Returns the canonical color for the clip slot or None if it does not exist.
```

##### color_index

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: Returns the canonical color index for the clip slot or None if it does not exist.
```

##### controls_other_clips

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Returns true if firing this slot will fire clips in other slots.
  Can only be true for slots in group tracks.
```

##### has_clip

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Returns true if this Clipslot owns a Clip.
```

##### has_stop_button

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set if this Clip has a stop button, which will, if fired, stop any
  other Clip that is currently playing the Track we do belong to.
```

##### is_group_slot

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns whether this clip slot is a group track slot (group slot).
```

##### is_playing

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns whether the clip associated with the slot is playing.
```

##### is_recording

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns whether the clip associated with the slot is recording.
```

##### is_triggered

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Const access to the triggering state of the clip slot.
```

##### playing_status

```yaml
kind: property
type: Live.ClipSlot.ClipSlotPlayingState
settable: false
listenable: true
raw_doc: |-
  Const access to the playing state of the clip slot.
  Can be either stopped, playing, or recording.
```

##### will_record_on_start

```yaml
kind: property
type: bool
settable: false
raw_doc: returns true if the clip slot will record on being fired.
```

#### Methods

##### create_audio_clip

```yaml
kind: method
signature: 'create_audio_clip( (ClipSlot)arg1, (object)arg2) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<AGroupAndClipSlotBase>,TString)
args:
- name: arg2
  type: str
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an audio clip referencing the file at the given absolute path in the slot.
  Throws an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.
```

##### create_clip

```yaml
kind: method
signature: 'create_clip( (ClipSlot)arg1, (float)arg2) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_clip(TPyHandle<AGroupAndClipSlotBase>,double)
args:
- name: arg2
  type: float
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an empty clip with the given length in the slot.
  Throws an error when called on non-empty slots or slots in non-MIDI tracks.
```

##### delete_clip

```yaml
kind: method
signature: 'delete_clip( (ClipSlot)arg1) -> None :'
cpp_signature: void delete_clip(TPyHandle<AGroupAndClipSlotBase>)
returns:
  type: None
raw_doc: |-
  Removes the clip contained in the slot.
  Raises an exception if the slot was empty.
```

##### duplicate_clip_to

```yaml
kind: method
signature: 'duplicate_clip_to( (ClipSlot)arg1, (ClipSlot)arg2) -> None :'
cpp_signature: void duplicate_clip_to(TPyHandle<AGroupAndClipSlotBase>,TPyHandle<AGroupAndClipSlotBase>)
args:
- name: arg2
  type: Live.ClipSlot.ClipSlot
returns:
  type: None
raw_doc: |-
  Duplicates the slot's clip to the passed in target slot.
  Overrides the target's clip if it's not empty.
  Raises an exception if the (source) slot itself is empty, or if source and
  target have different track types (audio vs. MIDI). Also raises if the source
  or target slot is in a group track (so called group slot).
```

##### fire

```yaml
kind: method
signature: 'fire( (ClipSlot)arg1) -> None :'
cpp_signature: void fire(TPyHandle<AGroupAndClipSlotBase>)
returns:
  type: None
raw_doc: |-
  Fire a Clip if this Clipslot owns one, else trigger the stop button,
  if we have one.
```

##### set_fire_button_state

```yaml
kind: method
signature: 'set_fire_button_state( (ClipSlot)arg1, (bool)arg2) -> None :'
cpp_signature: void set_fire_button_state(TPyHandle<AGroupAndClipSlotBase>,bool)
args:
- name: arg2
  type: bool
returns:
  type: None
raw_doc: Set the clipslot's fire button state directly. Supports all launch modes.
```

##### stop

```yaml
kind: method
signature: 'stop( (ClipSlot)arg1) -> None :'
cpp_signature: void stop(TPyHandle<AGroupAndClipSlotBase>)
returns:
  type: None
raw_doc: |-
  Stop playing the contained Clip, if there is a Clip and its currently
  playing.
```

## Enums

### ClipSlotPlayingState

```yaml
kind: enum
members:
  stopped: 0
  started: 1
  recording: 2
```

---
module: Conversions
---

Module-level functions that turn Live content from one form into another —
audio clips into MIDI, audio clips into a Drum Rack, drum pads into a new
MIDI track, and audio clips into Simpler-backed MIDI tracks.

## Enums

### AudioToMidiType

```yaml
kind: enum
members:
  harmony_to_midi: 0
  melody_to_midi: 1
  drums_to_midi: 2
```

## Functions

### audio_to_midi_clip

```yaml
kind: function
signature: 'audio_to_midi_clip( (Song)song, (Clip)audio_clip, (int)audio_to_midi_type) -> None :'
cpp_signature: void audio_to_midi_clip(TPyHandle<ASong>,TPyHandle<AClip>,int)
args:
- name: song
  type: Live.Song.Song
- name: audio_clip
  type: Live.Clip.Clip
- name: audio_to_midi_type
  type: Live.Conversions.AudioToMidiType | int
  refinement:
    type:
      probed: int
      confidence: high
      sources:
      - '[schema] applied per the enum-arg convention (see schema header).'
      - '[sister method] `AudioToMidiType` enum lives in the same module; the arg name `audio_to_midi_type` is the direct
        snake-case of the enum class name.'
returns:
  type: None
raw_doc: |-
  Creates a MIDI clip in a new MIDI track with the notes extracted from the given
  audio_clip. The `audio_to_midi_type` decides which algorithm is used in
  the process. Raises error when called with an inconvertible clip or invalid
  `audio_to_midi_type`.
```

### create_drum_rack_from_audio_clip

```yaml
kind: function
signature: 'create_drum_rack_from_audio_clip( (Song)song, (Clip)audio_clip) -> None :'
cpp_signature: void create_drum_rack_from_audio_clip(TPyHandle<ASong>,TPyHandle<AClip>)
args:
- name: song
  type: Live.Song.Song
- name: audio_clip
  type: Live.Clip.Clip
returns:
  type: None
raw_doc: |-
  Creates a new track with a drum rack with a simpler on the first pad with
  the specified audio clip.
```

### create_midi_track_from_drum_pad

```yaml
kind: function
signature: 'create_midi_track_from_drum_pad( (Song)song, (DrumPad)drum_pad) -> None :'
cpp_signature: void create_midi_track_from_drum_pad(TPyHandle<ASong>,TPyHandle<ADrumGroupDevicePad>)
args:
- name: song
  type: Live.Song.Song
- name: drum_pad
  type: Live.DrumPad.DrumPad
returns:
  type: None
raw_doc: Creates a new Midi track containing the specified Drum Pad's device chain.
```

### create_midi_track_with_simpler

```yaml
kind: function
signature: 'create_midi_track_with_simpler( (Song)song, (Clip)audio_clip) -> None :'
cpp_signature: void create_midi_track_with_simpler(TPyHandle<ASong>,TPyHandle<AClip>)
args:
- name: song
  type: Live.Song.Song
- name: audio_clip
  type: Live.Clip.Clip
returns:
  type: None
raw_doc: Creates a new Midi track with a simpler including the specified audio clip.
```

### is_convertible_to_midi

```yaml
kind: function
signature: 'is_convertible_to_midi( (Song)song, (Clip)audio_clip) -> bool :'
cpp_signature: bool is_convertible_to_midi(TPyHandle<ASong>,TPyHandle<AClip>)
args:
- name: song
  type: Live.Song.Song
- name: audio_clip
  type: Live.Clip.Clip
returns:
  type: bool
raw_doc: |-
  Returns whether `audio_clip` can be converted to MIDI.
  Raises error when called with a MIDI clip
```

### move_devices_on_track_to_new_drum_rack_pad

```yaml
kind: function
signature: 'move_devices_on_track_to_new_drum_rack_pad( (Song)song, (int)track_index) -> LomObject :'
cpp_signature: TWeakPtr<TPyHandleBase> move_devices_on_track_to_new_drum_rack_pad(TPyHandle<ASong>,int)
args:
- name: song
  type: Live.Song.Song
- name: track_index
  type: int
returns:
  type: Live.DrumPad.DrumPad | None
  refinement:
    type:
      probed: Live.LomObject.LomObject
      confidence: high
      sources:
      - '[M4L] docs list the return as `DrumPad / None`. The function moves devices INTO a drum rack pad and returns that
        pad; the `None` half of the union covers the no-op path that the M4L doc names.'
raw_doc: |-
  Moves the entire device chain of the track according to the track index
  onto the C1 (note 36) drum pad of a new drum rack in a new track.If the track associated with the track index does not contain any devices
  nothing changes (i.e. a new track and new drum rack are not created).
```

### sliced_simpler_to_drum_rack

```yaml
kind: function
signature: 'sliced_simpler_to_drum_rack( (Song)song, (SimplerDevice)simpler) -> None :'
cpp_signature: void sliced_simpler_to_drum_rack(TPyHandle<ASong>,TSimplerDevicePyHandle)
args:
- name: song
  type: Live.Song.Song
- name: simpler
  type: Live.SimplerDevice.SimplerDevice
returns:
  type: None
raw_doc: |-
  Converts the Simpler into a Drum Rack, assigning each slice to a drum pad.
  Calling it on a non-sliced simpler raises an error.
```

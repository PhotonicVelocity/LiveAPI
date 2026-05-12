---
module: TakeLane
---

## Classes

### TakeLane

```yaml
kind: class
path: Live.TakeLane.TakeLane
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a take lane in Live.
```

#### Properties

##### arrangement_clips

```yaml
kind: property
type: Live.Base.Vector[Live.Clip.Clip]
settable: false
listenable: true
raw_doc: Read-only access to the arrangement clips in the take lane.
```

##### canonical_parent

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Get the canonical parent of the take lane.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write access to the name of the TakeLane, as visible in the take lane header.
```

#### Methods

##### create_audio_clip

```yaml
kind: method
signature: 'create_audio_clip( (TakeLane)arg1, (object)arg2, (float)arg3) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<ATakeLane>,TString,double)
args:
- name: arg2
  type: str
- name: arg3
  type: float
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.
  Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
```

##### create_midi_clip

```yaml
kind: method
signature: 'create_midi_clip( (TakeLane)arg1, (float)arg2, (float)arg3) -> Clip :'
cpp_signature: TWeakPtr<TPyHandle<AClip>> create_midi_clip(TPyHandle<ATakeLane>,double,double)
args:
- name: arg2
  type: float
- name: arg3
  type: float
returns:
  type: Live.Clip.Clip
raw_doc: |-
  Creates an empty MIDI clip and inserts it into the arrangement at the specified time.
  Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
```

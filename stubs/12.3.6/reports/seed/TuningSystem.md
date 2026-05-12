---
module: TuningSystem
---

## Classes

### TuningSystem

```yaml
kind: class
path: Live.TuningSystem.TuningSystem
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Represents a Tuning System and its properties.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the TuningSystem.
```

##### highest_note

```yaml
kind: property
type: Live.TuningSystem.PitchClassAndOctave
settable: true
listenable: true
raw_doc: |-
  Get/Set the highest note of the current tuning system, where the first entry is
  the index within the pseudo octave and the second entry is the octave.
```

##### lowest_note

```yaml
kind: property
type: Live.TuningSystem.PitchClassAndOctave
settable: true
listenable: true
raw_doc: |-
  Get/Set the lowest note of the current tuning system, where the first entry is
  the index within the pseudo octave and the second entry is the octave.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Get/Set the name of the currently active tuning system.
```

##### note_tunings

```yaml
kind: property
type: list[float]
settable: true
listenable: true
raw_doc: Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in
  equal temperament.
```

##### number_of_notes_in_pseudo_octave

```yaml
kind: property
type: int
settable: false
raw_doc: Get the number of notes in the pseudo octave.
```

##### pseudo_octave_in_cents

```yaml
kind: property
type: float
settable: false
raw_doc: Get the pseudo octave in cents for the currently active tuning system.
```

##### reference_pitch

```yaml
kind: property
type: Live.TuningSystem.ReferencePitch
settable: true
listenable: true
raw_doc: Get/Set the reference pitch the currently active tuning system.
```

### PitchClassAndOctave

```yaml
kind: class
path: Live.TuningSystem.PitchClassAndOctave
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (int)index_in_octave, (int)octave) -> None :
      Create a new pitch class and octave specification.

      C++ signature :
          void __init__(_object*,int,int)
constructable: true
raw_doc: This class represents a PitchClassAndOctave type.
```

#### Properties

##### index_in_octave

```yaml
kind: property
type: int
settable: false
raw_doc: A PitchClassAndOctave's index within the pseudo octave.
```

##### octave

```yaml
kind: property
type: int
settable: false
raw_doc: A PitchClassAndOctave's octave.
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: index_in_octave
  type: int
- name: octave
  type: int
returns:
  type: None
```

### ReferencePitch

```yaml
kind: class
path: Live.TuningSystem.ReferencePitch
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (int)index_in_octave, (int)octave, (float)frequency) -> None :
      Create a new reference pitch specification.

      C++ signature :
          void __init__(_object*,int,int,double)
constructable: true
raw_doc: This class represents a ReferencePitch type.
```

#### Properties

##### frequency

```yaml
kind: property
type: float
settable: false
raw_doc: A ReferencePitch's frequency in Hz.
```

##### index_in_octave

```yaml
kind: property
type: int
settable: false
raw_doc: A ReferencePitch's index within the pseudo octave.
```

##### octave

```yaml
kind: property
type: int
settable: false
raw_doc: A ReferencePitch's octave.
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: index_in_octave
  type: int
- name: octave
  type: int
- name: frequency
  type: float
returns:
  type: None
```

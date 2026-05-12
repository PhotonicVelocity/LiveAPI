---
module: Scene
---

## Classes

### Scene

```yaml
kind: class
path: Live.Scene.Scene
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents an series of ClipSlots in Lives Sessionview matrix.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the scene.
```

##### clip_slots

```yaml
kind: property
type: Live.Base.Vector[Live.ClipSlot.ClipSlot]
settable: false
listenable: true
raw_doc: return a list of clipslots (see class AClipSlot) that this scene covers.
```

##### color

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Get/set access to the color of the scene (RGB).
```

##### color_index

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Get/set access to the color index of the scene. Can be None for no color.
```

##### is_empty

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns True if all clip slots of this scene are empty.
```

##### is_triggered

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Const access to the scene's trigger state.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Get/Set the name of the scene.
```

##### tempo

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: |-
  Get/Set the tempo value of the scene.
  The song will use the scene's tempo as soon as the scene is fired.
  Returns -1 if the scene has no tempo property.
```

##### tempo_enabled

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the active state of the scene tempo.
  When disabled, the scene will use the song's tempo,and the tempo value returned will be -1Returns a bool indicating the state of the scene's tempo
```

##### time_signature_denominator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: |-
  Get/Set the scene's time signature denominator.
  The song will use the scene's time signature as soon as the scene is fired.
  Returns -1 if the scene has no time signature property.
```

##### time_signature_enabled

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get the active state of the scene time signature.
  When disabled, the scene will use the song's time signature,and the time signature values returned will be -1Returns a bool indicating the state of the scene's time signature
```

##### time_signature_numerator

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: |-
  Get/Set the scene's time signature numerator.
  The song will use the scene's time signature as soon as the scene is fired.
  Returns -1 if the scene has no time signature property.
```

#### Methods

##### fire

```yaml
kind: method
signature: 'fire( (Scene)arg1 [, (bool)force_legato=False [, (bool)can_select_scene_on_launch=True]]) -> None :'
cpp_signature: void fire(TPyHandle<AScene> [,bool=False [,bool=True]])
args:
- name: force_legato
  type: bool
  optional: true
  default: 'False'
- name: can_select_scene_on_launch
  type: bool
  optional: true
  default: 'True'
returns:
  type: None
raw_doc: |-
  Fire the scene directly. Will fire all clipslots that this scene owns and
  select the scene itself.
```

##### fire_as_selected

```yaml
kind: method
signature: 'fire_as_selected( (Scene)arg1 [, (bool)force_legato=False]) -> None :'
cpp_signature: void fire_as_selected(TPyHandle<AScene> [,bool=False])
args:
- name: force_legato
  type: bool
  optional: true
  default: 'False'
returns:
  type: None
raw_doc: |-
  Fire the selected scene. Will fire all clipslots that this scene owns and
  select the next scene if necessary.
```

##### set_fire_button_state

```yaml
kind: method
signature: 'set_fire_button_state( (Scene)arg1, (bool)arg2) -> None :'
cpp_signature: void set_fire_button_state(TPyHandle<AScene>,bool)
args:
- name: arg2
  type: bool
returns:
  type: None
raw_doc: Set the scene's fire button state directly. Supports all launch modes.
```

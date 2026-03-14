# Scene (Module)

## Scene (Class)

> `Live.Scene.Scene`

This class represents an series of ClipSlots in Lives Sessionview matrix.

**Live Object:** `yes`

**Access via:**

- `Song.create_scene()`
- `Song.View.selected_scene`

### Properties

| Property                     | Type    | Supports             |
| ---------------------------- | ------- | -------------------- |
| `canonical_parent`           | `Song`  | `get`                |
| `clip_slots`                 | `tuple` | `get`/`listen`       |
| `color`                      | `int`   | `get`/`set`/`listen` |
| `color_index`                | `None`  | `get`/`set`/`listen` |
| `is_empty`                   | `bool`  | `get`                |
| `is_triggered`               | `bool`  | `get`/`listen`       |
| `name`                       | `str`   | `get`/`set`/`listen` |
| `tempo`                      | `float` | `get`/`set`/`listen` |
| `tempo_enabled`              | `bool`  | `get`/`set`/`listen` |
| `time_signature_denominator` | `int`   | `get`/`set`/`listen` |
| `time_signature_enabled`     | `bool`  | `get`/`set`/`listen` |
| `time_signature_numerator`   | `int`   | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the scene.

#### `clip_slots`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

return a list of clipslots (see class AClipSlot) that this scene covers.

#### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the color of the scene (RGB).

#### `color_index`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the color index of the scene. Can be None for no color.

#### `is_empty`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns True if all clip slots of this scene are empty.

#### `is_triggered`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the scene's trigger state.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the name of the scene.

#### `tempo`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the tempo value of the scene. The song will use the scene's tempo as soon as the scene is fired. Returns -1 if the scene has no tempo property.

#### `tempo_enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the active state of the scene tempo. When disabled, the scene will use the song's tempo,and the tempo value returned will be -1Returns a bool indicating the state of the scene's tempo

#### `time_signature_denominator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the scene's time signature denominator. The song will use the scene's time signature as soon as the scene is fired. Returns -1 if the scene has no time signature property.

#### `time_signature_enabled`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get the active state of the scene time signature. When disabled, the scene will use the song's time signature,and the time signature values returned will be -1Returns a bool indicating the state of the scene's time signature

#### `time_signature_numerator`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the scene's time signature numerator. The song will use the scene's time signature as soon as the scene is fired. Returns -1 if the scene has no time signature property.

### Methods

| Method                                                                      | Returns | Description                                 |
| --------------------------------------------------------------------------- | ------- | ------------------------------------------- |
| `fire(force_legato: bool = False, can_select_scene_on_launch: bool = True)` | `None`  | Fire the scene directly.                    |
| `fire_as_selected(force_legato: bool = False)`                              | `None`  | Fire the selected scene.                    |
| `set_fire_button_state(state: bool)`                                        | `None`  | Set the scene's fire button state directly. |

#### `fire(force_legato: bool = False, can_select_scene_on_launch: bool = True)`

- **Returns:** `None`
- **Args:**
  - `force_legato: bool = False`
  - `can_select_scene_on_launch: bool = True`

Fire the scene directly. Will fire all clipslots that this scene owns and select the scene itself.

#### `fire_as_selected(force_legato: bool = False)`

- **Returns:** `None`
- **Args:**
  - `force_legato: bool = False`

Fire the selected scene. Will fire all clipslots that this scene owns and select the next scene if necessary.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`

Set the scene's fire button state directly. Supports all launch modes.

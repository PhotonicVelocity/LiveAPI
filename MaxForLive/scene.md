# Scene

This class represents a series of clip slots in Live's Session View matrix.

## Canonical Path

```
live_set scenes N
```

## Children

### clip_slots list of [ClipSlot](/apiref/lom/clipslot/ "ClipSlot") read-onlyobserve

## Properties

### color int observe

The RGB value of the scene's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).   
  
When setting the RGB value, the nearest color from the Scene color chooser is taken.

### color_index long observe

The color index of the scene.

### is_empty bool read-only

1 = none of the slots in the scene is filled.

### is_triggered bool read-onlyobserve

1 = scene is blinking.

### name symbol observe

The name of the scene.

### tempo float observe

The scene's tempo.   
Returns -1 if the scene tempo is disabled.

### tempo_enabled bool observe

The active state of the scene tempo.   
When disabled, the scene will use the song's tempo,   
and the tempo value returned will be -1.

### time_signature_numerator int observe

The scene's time signature numerator.   
Returns -1 if the scene time signature is disabled.

### time_signature_denominator int observe

The scene's time signature denominator.   
Returns -1 if the scene time signature is disabled.

### time_signature_enabled bool observe

The active state of the scene time signature.   
When disabled, the scene will use the song's time signature,   
and the time signature values returned will be -1.

## Functions

### fire

Parameter: `force_legato (optional)` [bool]   
`can_select_scene_on_launch (optional)` [bool]   
Fire all clip slots contained within the scene and select this scene.   
Starts recording of armed and empty tracks within a Group Track in this scene if Preferences->Launch->Start Recording on Scene Launch is ON.   
Calling with force_legato = 1 (default = 0) will launch all clips immediately in Legato, independent of their launch mode.   
When calling with can_select_scene_on_launch = 0 (default = 1) the scene is fired without selecting it.

### fire_as_selected

Parameter: `force_legato (optional)` [bool]   
Fire the selected scene, then select the next scene.   
It doesn't matter on which scene you are calling this function.   
Calling with force_legato = 1 (default = 0) will launch all clips immediately in Legato, independent of their launch mode.

### set_fire_button_state

Parameter: `state` [bool]   
If the state is set to 1, Live simulates pressing of scene button until the state is set to 0 or until the scene is stopped otherwise.

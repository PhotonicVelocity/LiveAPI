# Scene

> `Live.Scene.Scene`

Represents a row in Live's Session View matrix. A scene owns one clip slot per track and can fire all of them
simultaneously. Scenes can carry their own tempo and time signature that Live applies when the scene is launched.

??? note "Raw probe notes (temporary)"
    - Setting `color` to `None` raises an `InternalError` (C++ type mismatch: expected `int`, got `NoneType`). Matches
      Track probe behavior.
    - Setting `color_index` to `None` succeeds and reads back as `None`. `None` is the confirmed sentinel for "no palette
      color assigned". Scenes can have no color in the Live UI, which is why `None` is valid here (unlike tracks and
      clips, which always have a color).
    - Setting `time_signature_numerator` or `time_signature_denominator` while `time_signature_enabled` is `False`
      implicitly enables the override. There is no way to stage a value without activating the override.
    - When `time_signature_enabled` is `False`, both `time_signature_numerator` and `time_signature_denominator` read as
      `-1`. However, Live remembers the previously set values internally — disabling and re-enabling restores them.
    - `fire_as_selected()` ignores the scene it is called on and always fires the currently selected scene
      (`Song.view.selected_scene`), then advances the selection to the next scene. Confirmed by selecting scene 0,
      calling `fire_as_selected()` on scene 2 — scene 0 fired and selection advanced to scene 1.

## Children

| Child        | Returns              | Shape  | Listenable | Summary                                 |
| ------------ | -------------------- | ------ | ---------- | --------------------------------------- |
| `clip_slots` | `Sequence[ClipSlot]` | `list` | `yes`      | The clip slots owned by this scene row. |

### `clip_slots`

- **Returns:** `Sequence[ClipSlot]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The ordered list of clip slots in this scene, one per track. Index order matches `Song.tracks` order. The list fires a
listener when tracks are added or removed.

## Properties

| Property                     | Type        | Settable    | Listenable | Summary                                                          |
| ---------------------------- | ----------- | ----------- | ---------- | ---------------------------------------------------------------- |
| `color`                      | `int`       | `int`       | `yes`      | Scene color as packed RGB `0x00rrggbb`.                          |
| `color_index`                | `int\|None` | `int\|None` | `yes`      | Scene color palette index. `None` = no color assigned.           |
| `is_empty`                   | `bool`      | —           | `no`       | `True` if all clip slots in the scene are empty.                 |
| `is_triggered`               | `bool`      | —           | `yes`      | `True` while the scene launch button is blinking (queued).       |
| `name`                       | `str`       | `str`       | `yes`      | Display name of the scene.                                       |
| `tempo`                      | `float`     | `float`     | `yes`      | Scene tempo in BPM. `-1` if disabled.                            |
| `tempo_enabled`              | `bool`      | `bool`      | `yes`      | Whether this scene overrides the song tempo on launch.           |
| `time_signature_numerator`   | `int`       | `int`       | `yes`      | Time signature numerator. `-1` if disabled; setting enables.     |
| `time_signature_denominator` | `int`       | `int`       | `yes`      | Time signature denominator. `-1` if disabled; setting enables.   |
| `time_signature_enabled`     | `bool`      | `bool`      | `yes`      | Whether this scene overrides the song time signature on launch.  |

### `color`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Packed RGB color value in the form `0x00rrggbb`. When setting, Live snaps to the nearest color in the scene color
chooser.

**Quirks:**

- Setting to `None` raises `InternalError` (C++ type mismatch: expected `int`, got `NoneType`). Use `color_index = None`
  to clear the color instead.

### `color_index`

- **Type:** `int | None` (get) · `int | None` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Palette-based color index. `None` is the sentinel for "no palette color assigned" — scenes can have no color in the Live
UI, unlike tracks and clips which always have one. Setting to `None` clears the scene color. Prefer `color_index` over
`color` when working with the Live palette.

### `is_empty`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if none of the clip slots in this scene contain a clip. Does not fire a listener; re-read after clip slot changes.

### `is_triggered`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` while the scene launch button is blinking, indicating launch is queued but has not yet started (launch
quantization pending).

### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Display name of the scene as shown in the Session View. Setting an empty string is allowed.

### `tempo`

- **Type:** `float` (get) · `float` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The tempo the song will use when this scene is launched, in BPM. Returns `-1` when `tempo_enabled` is `False`.

### `tempo_enabled`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `11.0`

Controls whether this scene's `tempo` overrides `Song.tempo` when launched. When `False`, `tempo` returns `-1` and the
song's global tempo is used.

### `time_signature_numerator`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.0`

The time signature numerator applied when this scene launches. Returns `-1` when `time_signature_enabled` is `False`.
Live remembers the value internally even when disabled — disabling and re-enabling restores it.

**Quirks:**

- Setting while `time_signature_enabled` is `False` implicitly enables the override. There is no way to stage a value
  without activating it.

### `time_signature_denominator`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.0`

The time signature denominator applied when this scene launches. Returns `-1` when `time_signature_enabled` is `False`.
Live remembers the value internally even when disabled — disabling and re-enabling restores it.

**Quirks:**

- Setting while `time_signature_enabled` is `False` implicitly enables the override. There is no way to stage a value
  without activating it.

### `time_signature_enabled`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `11.0`

Controls whether this scene's time signature overrides the song's global time signature when launched. When `False`,
`time_signature_numerator` and `time_signature_denominator` both return `-1`, but Live remembers the previously set
values internally — setting back to `True` restores them.

## Methods

| Method                                                      | Returns | Summary                                                          |
| ----------------------------------------------------------- | ------- | ---------------------------------------------------------------- |
| `fire(force_legato, can_select_scene_on_launch)`            | `None`  | Launch all clips in the scene.                                   |
| `fire_as_selected(force_legato)`                            | `None`  | Fire the selected scene and advance selection to the next scene. |
| `set_fire_button_state(state)`                              | `None`  | Programmatically hold or release the scene launch button.        |

### `fire(force_legato=False, can_select_scene_on_launch=True)`

- **Returns:** `None`
- **Args:**
    - `force_legato: bool = False`
    - `can_select_scene_on_launch: bool = True`
- **Since:** `<11`

Launches all clip slots in the scene simultaneously. If `force_legato=True`, all clips start immediately in Legato mode
regardless of their individual launch mode setting. If `can_select_scene_on_launch=False`, the scene fires without
becoming the selected scene.

If "Start Recording on Scene Launch" is enabled in preferences, armed and empty tracks within a Group Track will begin
recording.

### `fire_as_selected(force_legato=False)`

- **Returns:** `None`
- **Args:**
    - `force_legato: bool = False`
- **Since:** `<11`

Fires the currently selected scene and advances the selection to the next scene. Equivalent to pressing the scene launch
button with "Select Next Scene on Launch" enabled.

**Quirks:**

- Ignores the scene object it's called on — always fires `Song.view.selected_scene`. Calling `scene_2.fire_as_selected()`
  while scene 0 is selected fires scene 0, not scene 2.

### `set_fire_button_state(state)`

- **Returns:** `None`
- **Args:**
    - `state: bool`
- **Since:** `<11`

Simulates holding the scene launch button. While `state=True`, Live acts as if the button is being held, respecting the
launch mode (e.g. Gate mode clips will sustain). Set back to `False` to release.

## Open Questions

- Does `tempo` or `time_signature_*` take effect immediately on set, or only on next launch?
- When `tempo_enabled = False`, does setting `tempo` to a value implicitly enable the override? (Time signature properties
  do behave this way — needs probing for tempo.)
- Does `fire()` with `can_select_scene_on_launch=False` suppress the scene highlight in the UI entirely?

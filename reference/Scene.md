# Scene

## Scene

Represents a row in Live's Session View matrix. A scene owns one clip slot per track and can
fire all of them simultaneously. Scenes can carry their own tempo and time signature that Live
applies when the scene is launched.

### Sources

- **Primary:** `Live/classes/Scene.py` (stub dump)
- **Secondary:** `MaxForLive/scene.md`
- **Probes:** `.tmp/probe_color_none.py`, `.tmp/probe_scene_timesig.py`, `.tmp/probe_scene_fire_as_selected.py` (Live
  12.3.5)

### Probe Notes

- Setting `color` to `None` raises an `InternalError` (C++ type mismatch: expected `int`, got `NoneType`). Matches Track
  probe behavior.
- Setting `color_index` to `None` succeeds and reads back as `None`. `None` is the confirmed sentinel for "no palette
  color assigned". Scenes can have no color in the Live UI, which is why `None` is valid here (unlike tracks and clips,
  which always have a color).
- Setting `time_signature_numerator` or `time_signature_denominator` while `time_signature_enabled` is `False`
  implicitly enables the override. There is no way to stage a value without activating the override.
- When `time_signature_enabled` is `False`, both `time_signature_numerator` and `time_signature_denominator` read as
  `-1`. However, Live remembers the previously set values internally — disabling and re-enabling restores them.
- `fire_as_selected()` ignores the scene it is called on and always fires the currently selected scene
  (`Song.view.selected_scene`), then advances the selection to the next scene. Confirmed by selecting scene 0, calling
  `fire_as_selected()` on scene 2 — scene 0 fired and selection advanced to scene 1.

### Open Questions

- Does `tempo` or `time_signature_*` take effect immediately on set, or only on next launch?
- When `tempo_enabled = False`, does setting `tempo` to a value implicitly enable the override? (The time signature
  properties do behave this way — needs probing for tempo.)
- Does `fire()` with `can_select_scene_on_launch=False` suppress the scene highlight in the UI entirely?

### Children

| Child        | Returns              | Shape  | Access | Listenable | Available Since | Summary                                 |
| ------------ | -------------------- | ------ | ------ | ---------- | --------------- | --------------------------------------- |
| `clip_slots` | `Sequence[ClipSlot]` | `list` | `get`  | `yes`      | `<11`           | The clip slots owned by this scene row. |

#### `clip_slots`

- **Returns:** `Sequence[ClipSlot]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The ordered list of clip slots in this scene, one per track. Index order matches
`Song.tracks` order. The list fires a listener when tracks are added or removed.

### Properties

| Property                     | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                                                                |
| ---------------------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------------------------------------------------------------------------------ |
| `color`                      | `int`       | `int`       | `yes`      | `<11`           | Scene color as packed RGB `0x00rrggbb`.                                                                |
| `color_index`                | `int\|None` | `int\|None` | `yes`      | `<11`           | Scene color palette index. `None` means no color assigned.                                             |
| `is_empty`                   | `bool`      | —           | `no`       | `<11`           | `True` if all clip slots in the scene are empty.                                                       |
| `is_triggered`               | `bool`      | —           | `yes`      | `<11`           | `True` while the scene launch button is blinking (queued).                                             |
| `name`                       | `str`       | `str`       | `yes`      | `<11`           | Display name of the scene.                                                                             |
| `tempo`                      | `float`     | `float`     | `yes`      | `<11`           | Scene tempo in BPM. Returns `-1` if `tempo_enabled` is `False`.                                        |
| `tempo_enabled`              | `bool`      | `bool`      | `yes`      | `11.0`          | Whether this scene overrides the song tempo on launch.                                                 |
| `time_signature_numerator`   | `int`       | `int`       | `yes`      | `11.0`          | Time signature numerator. Returns `-1` if disabled; setting implicitly enables.                        |
| `time_signature_denominator` | `int`       | `int`       | `yes`      | `11.0`          | Time signature denominator. Returns `-1` if disabled; setting implicitly enables.                      |
| `time_signature_enabled`     | `bool`      | `bool`      | `yes`      | `11.0`          | Whether this scene overrides the song time signature on launch. Values persist through disable/enable. |

#### `color`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Packed RGB color value in the form `0x00rrggbb`. When setting, Live snaps to the nearest
color in the scene color chooser. Setting `color` to `None` raises an `InternalError`
(C++ type mismatch; confirmed in probes).

#### `color_index`

- **Get Returns:** `int | None`
- **Set Accepts:** `int | None`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Palette-based color index. `None` is the confirmed sentinel for "no palette color assigned"
and can be set explicitly to clear the scene color. Prefer setting `color_index` over
`color` when working with the Live palette.

#### `is_empty`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` if none of the clip slots in this scene contain a clip. Does not fire a listener;
re-read after clip slot changes.

#### `is_triggered`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` while the scene launch button is blinking, indicating launch is queued but has not
yet started (launch quantization pending).

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Display name of the scene as shown in the Session View. Setting an empty string is allowed;
behavior when multiple scenes share a name is not enforced by the API.

#### `tempo`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The tempo the song will use when this scene is launched, in BPM. Returns `-1` when
`tempo_enabled` is `False`. Setting this property while `tempo_enabled` is `False` has
unknown effect (needs probing).

#### `tempo_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Controls whether this scene's `tempo` overrides `Song.tempo` when launched. When `False`,
`tempo` returns `-1` and the song's global tempo is used.

#### `time_signature_numerator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
The time signature numerator applied when this scene launches. Returns `-1` when
`time_signature_enabled` is `False`. Setting this property while disabled implicitly
sets `time_signature_enabled` to `True`. Live remembers the value internally even
when disabled — disabling and re-enabling restores the previously set value.

#### `time_signature_denominator`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
The time signature denominator applied when this scene launches. Returns `-1` when
`time_signature_enabled` is `False`. Setting this property while disabled implicitly
sets `time_signature_enabled` to `True`. Live remembers the value internally even
when disabled — disabling and re-enabling restores the previously set value.

#### `time_signature_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `11.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Controls whether this scene's time signature overrides the song's global time signature
when launched. When `False`, `time_signature_numerator` and `time_signature_denominator`
both return `-1`, but Live remembers the previously set values internally — setting
`time_signature_enabled` back to `True` restores them.

### Methods

| Signature                                                   | Returns | Available Since | Summary                                                          |
| ----------------------------------------------------------- | ------- | --------------- | ---------------------------------------------------------------- |
| `fire(force_legato=False, can_select_scene_on_launch=True)` | `None`  | `<11`           | Launch all clips in the scene.                                   |
| `fire_as_selected(force_legato=False)`                      | `None`  | `<11`           | Fire the selected scene and advance selection to the next scene. |
| `set_fire_button_state(state: bool)`                        | `None`  | `<11`           | Programmatically hold or release the scene launch button.        |

#### `fire(force_legato=False, can_select_scene_on_launch=True)`

- **Returns:** `None`
- **Args:**
  - `force_legato: bool = False`
  - `can_select_scene_on_launch: bool = True`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `no`
- **Side Effects:** Fires all clip slots in the scene; may select the scene and begin recording on armed empty tracks
  within group tracks if the corresponding preference is enabled.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Launches all clip slots in the scene simultaneously. If `force_legato=True`, all clips start
immediately in Legato mode regardless of their individual launch mode setting. If
`can_select_scene_on_launch=False`, the scene fires without becoming the selected scene.

If "Start Recording on Scene Launch" is enabled in preferences, armed and empty tracks within
a Group Track will begin recording.

#### `fire_as_selected(force_legato=False)`

- **Returns:** `None`
- **Args:**
  - `force_legato: bool = False`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `no`
- **Side Effects:** Fires the selected scene and advances the selected scene to the next one.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:**
Fires the currently selected scene **regardless of which scene object** this method is called
on, then advances the selection to the next scene. Equivalent to pressing the scene launch
button with "Select Next Scene on Launch" enabled. `force_legato` behaves the same as in
`fire()`.

**Probe notes (2026-02-17):** Confirmed that calling `scene_2.fire_as_selected()` while
scene 0 is selected fires scene 0 (not scene 2) and advances selection to scene 1. The
`self` scene object is ignored entirely.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `no`
- **Side Effects:** Holds the scene launch button pressed (`True`) or releases it (`False`). Supports all launch modes.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Simulates holding the scene launch button. While `state=True`, Live acts as if the button is
being held, respecting the launch mode (e.g. Gate mode clips will sustain). Set back to
`False` to release.

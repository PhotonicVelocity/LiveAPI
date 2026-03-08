# ClipSlot

> `Live.ClipSlot.ClipSlot`

Represents a single cell in Live's Session View matrix -- the intersection of one track and one
scene row. A slot always exists even when empty; it can contain a clip or be used as a stop
trigger. Group track slots have additional aggregate behavior over the tracks within the group.

??? note "Raw probe notes (temporary)"
    #### Color behavior (probed 2026-02-17)

    - `color` and `color_index` have **no setter** -- `set` raises
      `"property of 'ClipSlot' object has no setter"` on both regular and group slots.
    - **Regular slots** (empty or with clip): both return `None`. Even when `has_clip=True`, the slot's own
      color is `None` -- the clip's color is only accessible via `clip.color`.
    - **Group slots** (empty row): both return `None`.
    - **Group slots** (clips in child tracks): returns the **first** contained clip's color/color_index. In a
      group with children at `color_index=5` (green) and `color_index=22` (blue), the group slot reported
      `color_index=5`.
    - The Live UI allows "setting" a group slot's color, but this is a UI-level composite action that sets
      `Clip.color` on each child clip individually -- it is not exposed through `ClipSlot.color`.

    #### controls_other_clips (probed 2026-02-17)

    - Only meaningful on **group track slots** -- always `False` on regular (non-group) slots.
    - `True` when at least one child track slot at the same scene index contains an **active**
      (non-deactivated) clip. Deactivated clips do not count.
    - Tested scenarios (6-track session: 1-MIDI, 2 Group containing 3 MIDI + 4 Audio, 5 Group containing
      6 Audio):
        - Empty row -> `False`
        - Row with active clip in child track -> `True`
        - Row with deactivated clip in child track -> `False`
    - **Arm state does not affect the value** -- arming a child track does not change the result.
    - **Follow actions do not affect the value** -- clips with "next" follow actions on regular (non-group)
      tracks still report `False`.
    - Visually corresponds to the hatched clip indicator shown on the right side of group slots in the
      Live UI.

    #### will_record_on_start (probed 2026-02-17)

    - Always returns `False` through the Python API regardless of conditions tested:
        - Armed/unarmed track, empty/occupied slots, MIDI and audio tracks
        - Transport playing/stopped
        - `session_record` on/off, `overdub` on/off
        - Group track slots, child track slots, top-level track slots
        - "Start Recording on Scene Launch" preference on/off
    - The property reads without error but never reports `True`. May only function through the Max LOM
      path or within listener callback contexts. **Skipped** from the public API spec.

### Open Questions

- ~~For non-group slots: do `is_playing` and `is_recording` reflect the clip's actual playback
  state, or are they derived from `playing_status` (which would make them always `0` for
  non-group slots)?~~ **Resolved (probed, Live 12.3.5):** `is_playing` and `is_recording`
  reflect the clip's actual state on non-group slots, despite `playing_status` always being `0`
  there. The Max docs' claim that they derive from `playing_status` is incorrect for non-group
  slots -- they appear to have an independent implementation.
- ~~What does `color` / `color_index` return when `has_clip=True` on a non-group slot?~~ **Resolved:**
  returns `None` -- see probe notes.
- What exception type does `delete_clip()` raise when the slot is empty?
- Can `has_stop_button` be set on a group slot, or is it read-only there?

### Children

| Child  | Returns      | Shape    | Listenable | Summary                                          |
| ------ | ------------ | -------- | ---------- | ------------------------------------------------ |
| `clip` | `Clip\|None` | `single` | `yes`      | The clip owned by this slot, or `None` if empty. |

#### `clip`

- **Type:** `Clip | None`
- **Listenable:** `yes` (via `has_clip` listener -- `clip` itself is not directly listenable, but `has_clip`
  fires when a clip is created or deleted)
- **Since:** `<11`

The clip contained in this slot. `None` when the slot is empty (`has_clip=False`). Always
check `has_clip` before accessing `clip` properties. The Max docs note that the Max LOM
returns `id 0` (equivalent to `None`) when the slot is empty.

### Properties

| Property               | Type                   | Settable | Listenable | Summary                                                                                |
| ---------------------- | ---------------------- | -------- | ---------- | -------------------------------------------------------------------------------------- |
| `color`                | `int\|None`            | no       | `yes`      | Color of the first clip in a group slot. `None` for regular empty slots.               |
| `color_index`          | `int\|None`            | no       | `yes`      | Color index of the first clip in a group slot. `None` for regular empty slots.         |
| `controls_other_clips` | `bool`                 | no       | `yes`      | Group slot only: `True` if child tracks have active (non-deactivated) clips.           |
| `has_clip`             | `bool`                 | no       | `yes`      | `True` if a clip exists in this slot.                                                  |
| `has_stop_button`      | `bool`                 | `bool`   | `yes`      | Whether this slot has a stop button. When fired while empty, stops the track.          |
| `is_group_slot`        | `bool`                 | no       | `no`       | `True` if this slot belongs to a group track.                                          |
| `is_playing`           | `bool`                 | no       | `no`       | `True` if the clip in this slot is playing. Works on both group and non-group slots.   |
| `is_recording`         | `bool`                 | no       | `no`       | `True` if the clip in this slot is recording. Works on both group and non-group slots. |
| `is_triggered`         | `bool`                 | no       | `yes`      | `True` while a clip launch, stop, or record button in this slot is blinking.           |
| `playing_status`       | `ClipSlotPlayingState` | no       | `yes`      | Aggregate playback state for group slots only; always `0` for non-group slots.         |
| `will_record_on_start` | `bool`                 | no       | `no`       | `True` if firing this slot will begin recording. Currently always returns `False`.     |

#### `color`

- **Type:** `int | None`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only derived color. Returns `None` on all regular slots -- even when `has_clip=True`.
For group slots: returns the packed RGB color (`0x00rrggbb`) of the first clip in the group;
`None` when no child clips exist in the row. No setter exists on either regular or group
slots -- attempting `set` raises `"property of 'ClipSlot' object has no setter"`. To set a
clip's color, use the clip's own `color` property. Note: the Live UI allows coloring a group
slot (which colors all child clips), but this is an internal composite action not exposed
through the API.

#### `color_index`

- **Type:** `int | None`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only derived color index. Returns `None` on all regular slots -- even when
`has_clip=True`. For group slots: returns the color index of the first clip in the group;
`None` when no child clips exist in the row. No setter exists.

#### `controls_other_clips`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` only for group track slots that have at least one **active** (non-deactivated) clip in
any child track at this scene row. Deactivated clips do not count -- a group slot with only
deactivated child clips reports `False`. When `True`, firing the slot will launch those child
track clips. Always `False` for non-group slots, regardless of follow actions or other
cross-slot relationships. Arm state of child tracks does not affect the value.

#### `has_clip`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when this slot contains a clip. Use this to gate access to `clip` and clip-specific
operations. Fires its listener when a clip is created or deleted in this slot.

#### `has_stop_button`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

When `True`, firing this empty slot (or pressing the stop button for the track) stops any
currently playing or recording clip on this track. For group slots, stops all clips within
child tracks.

#### `is_group_slot`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this slot belongs to a group track. Group slots aggregate the state of child track
slots at the same scene row and expose `controls_other_clips` and `playing_status`.

#### `is_playing`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the clip in this slot is currently playing. Works on both group and non-group slots.
For non-group slots, reflects the clip's actual playback state (not derived from `playing_status`,
which is always `0` for non-group slots -- contradicting the Max docs). For group slots, `True` if
at least one child clip is playing.

#### `is_recording`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the clip in this slot is currently recording. Works on both group and non-group slots.
For non-group slots, reflects the clip's actual recording state (not derived from `playing_status`,
which is always `0` for non-group slots -- contradicting the Max docs). For group slots, `True` if
at least one child clip is recording.

#### `is_triggered`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` while a clip launch button, clip stop button, or clip record button in this slot is
blinking (queued, waiting on launch quantization). Fires listener on state change. Works on
both group and non-group slots. During session recording with launch quantization, `is_triggered`
is `True` in the target slot while `Song.session_record_status == 2` (triggered phase), then
transitions to `False` when recording actually starts.

#### `playing_status`

- **Type:** `ClipSlotPlayingState` (int)
- **Listenable:** `yes`
- **Since:** `<11`

Aggregate playback state for group track slots. Confirmed always `0` for non-group slots,
regardless of the clip's actual playback or recording state. Note that `is_playing` and
`is_recording` still work correctly on non-group slots despite `playing_status` being `0` --
they have an independent implementation.

**Listener behavior (probed 12.3.5):** The listener fires on group slots when child clip
playback state changes (value = new `ClipSlotPlayingState`). On non-group slots, the listener
does not fire -- subscribe succeeds but no events are delivered.

`ClipSlotPlayingState` enum values:

- `0` = stopped (all child track clips stopped, or not a group slot)
- `1` = playing (at least one child clip is playing)
- `2` = recording (at least one child clip is playing or recording)

#### `will_record_on_start`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Documented as `True` when firing this slot will trigger recording rather than playing back an
existing clip. However, probing shows it **always returns `False`** through the Python API
regardless of arm state, clip presence, transport state, session record/overdub toggles, group
track membership, or the "Start Recording on Scene Launch" preference. May only function
through the Max LOM path or within listener callback contexts. The information it claims to
provide is trivially derivable from `track.arm` and `has_clip`.

### Methods

| Method                                                                   | Returns | Summary                                                     |
| ------------------------------------------------------------------------ | ------- | ----------------------------------------------------------- |
| `create_audio_clip(path: str)`                                           | `Clip`  | Create an audio clip from a file in this slot.              |
| `create_clip(length: float)`                                             | `Clip`  | Create an empty MIDI clip of the given length in beats.     |
| `delete_clip()`                                                          | `None`  | Delete the clip in this slot.                               |
| `duplicate_clip_to(target_slot: ClipSlot)`                               | `None`  | Copy this slot's clip to another slot.                      |
| `fire(record_length=None, launch_quantization=None, force_legato=False)` | `None`  | Fire the clip, trigger the stop button, or begin recording. |
| `set_fire_button_state(state: bool)`                                     | `None`  | Programmatically hold or release the clip launch button.    |
| `stop()`                                                                 | `None`  | Stop the playing or recording clip on this track.           |

#### `create_audio_clip(path: str)`

- **Returns:** `Clip`
- **Args:** `path: str` -- absolute path to a valid audio file
- **Raises:** Error if slot is non-empty, track is not an audio track, track is frozen, or path is not a
  valid audio file.
- **Since:** `11.3`

Creates an audio clip referencing the file at the given absolute path. Raises an error if the
slot already contains a clip, if the track is not an audio track, or if the track is frozen.

#### `create_clip(length: float)`

- **Returns:** `Clip`
- **Args:** `length: float` -- clip length in beats, must be `> 0.0`
- **Raises:** Error if slot is non-empty or track is not a MIDI track.
- **Since:** `<11`

Creates an empty MIDI clip. Can only be called on empty slots in MIDI tracks. Length is in
beats and must be greater than `0.0`.

#### `delete_clip()`

- **Returns:** `None`
- **Raises:** Exception if the slot is empty.
- **Since:** `<11`

Deletes the clip contained in this slot. Raises an exception if called on an empty slot.

#### `duplicate_clip_to(target_slot: ClipSlot)`

- **Returns:** `None`
- **Args:** `target_slot: ClipSlot`
- **Raises:** Exception if this slot is empty; if source and target track types differ (audio vs MIDI); if
  source or target is a group slot.
- **Since:** `<11`

Duplicates this slot's clip to another slot. The target clip is replaced if non-empty. Raises
if the source is empty, if source and target have mismatched track types, or if either slot
is a group slot.

#### `fire(record_length=None, launch_quantization=None, force_legato=False)`

- **Returns:** `None`
- **Args:**
    - `record_length: float = 1.7976931348623157e+308` (effectively infinite; omit to record indefinitely)
    - `launch_quantization: int = -2147483648` (sentinel: use global quantization)
    - `force_legato: bool = False`
- **Raises:** Error if `record_length` is passed but the slot already owns a clip.
- **Since:** `<11`

The primary launch action for a slot. Behavior depends on slot state:

- If the slot has a clip: launches it.
- If the slot is empty and `has_stop_button=True`: triggers the stop button.
- If the slot is empty and the track is armed: starts recording.

`record_length` specifies the recording duration in beats, after which the clip will loop
back and play. Must not be provided if the slot already has a clip. `launch_quantization`
overrides the global quantization setting. `force_legato` causes the clip to start
immediately, moving the playhead to stay in sync.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:** `state: bool`
- **Since:** `<11`

Simulates pressing and holding the clip launch button. Supports all launch modes (e.g. Gate
mode clips sustain while state is `True`). Set to `False` to release.

#### `stop()`

- **Returns:** `None`
- **Since:** `<11`

Stops any actively playing or recording clip on this track. For group slots, stops clips in
all child tracks. The Max docs note that it does not matter which slot index on the track you
call this from -- the effect is track-wide.

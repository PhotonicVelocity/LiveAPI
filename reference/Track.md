# Track (Live API)

## Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master
track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.
Not all properties are supported by all types of tracks. The properties are marked accordingly.

### Sources

- **Primary:** `Live/classes/Track.py`
- **Secondary:** `MaxForLive/track.md`, `MaxForLive/track_view.md`
- **Probes:** `tests/integration/test_track.py` + manual probe sessions

### Probe Notes

- Current probe set included `midi`, `audio`, `group`, `return`, and `master` tracks (grouped-track layout).
- Dictionary routing members (`input_routing_type/channel`, `output_routing_type/channel`, and `available_*`) were
  readable and settable on all probed track kinds.
- On several non-master tracks, `available_output_routing_channels` had only one option, so alternate channel selection
  was not always possible.
- In current probes, setting track color by known palette values round-trips as expected.
- In current probes, setting `color` to `None` raised an `InternalError` (C++ type mismatch: expected `int`).
- In current probes, setting `color_index` to `None` returned OK but had no effect — value read back unchanged. Tracks
  always have a color in the Live UI (no "no color" option), so `None` is not a meaningful value and is silently
  discarded.
- In current probes, `fired_slot_index` and `playing_slot_index` sentinel behavior matched documented values (`-2`,
  `-1`).
- In current probes, `current_monitoring_state` accepted values `0`, `1`, `2`; setting `>=3` returned `Invalid
monitoring state!`.
- In current probes on a MIDI track, immediate read-after-set matched for `name`, `mute`, `solo`, `color_index`,
  `current_monitoring_state`, and `arm`.
- Legacy string routing members (`current_*`, `*_routings`, `*_sub_routings`) remain in Live API for compatibility, but
  dictionary routing members are the modern replacement:
  - `current_input_routing` -> `input_routing_type`
  - `current_input_sub_routing` -> `input_routing_channel`
  - `input_routings` -> `available_input_routing_types`
  - `input_sub_routings` -> `available_input_routing_channels`
  - `current_output_routing` -> `output_routing_type`
  - `current_output_sub_routing` -> `output_routing_channel`
  - `output_routings` -> `available_output_routing_types`
  - `output_sub_routings` -> `available_output_routing_channels`

### Open Questions

- Semantic naming for `Track.monitoring_states` values (`0/1/2`) is still unconfirmed from raw docs.
- Full validity/error constraints for routing setters by track type.
- Per-member async visibility behavior for mutable track properties beyond the currently probed subset (which updates
  are immediate vs scheduler-delayed).

### Children

| Child               | Returns              | Shape    | Access | Listenable | Available Since | Summary                                                                                                                                          |
| ------------------- | -------------------- | -------- | ------ | ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `take_lanes`        | `Sequence[TakeLane]` | `list`   | `get`  | `yes`      | `12.2`          | The list of this track's take lanes                                                                                                              |
| `clip_slots`        | `Sequence[ClipSlot]` | `list`   | `get`  | `yes`      | `<11`           | const access to the list of clipslots (see class AClipSlot) for this track.The list will be empty for the main and sendtracks.                   |
| `arrangement_clips` | `Sequence[Clip]`     | `list`   | `get`  | `yes`      | `11.0`          | The list of this track's Arrangement View clip IDs _Available since Live 11.0._                                                                  |
| `devices`           | `Sequence[Device]`   | `list`   | `get`  | `yes`      | `<11`           | Includes mixer device.                                                                                                                           |
| `group_track`       | `Track`              | `single` | `get`  | `no`       | `<11`           | The Group Track, if the Track is grouped.                                                                                                        |
| `mixer_device`      | `MixerDevice`        | `single` | `get`  | `no`       | `<11`           | Return access to the special Device that every Track has: This Device containsthe Volume, Pan, Sendamounts, and Crossfade assignment parameters. |
| `view`              | `Track.View`         | `single` | `get`  | `no`       | `<11`           | Representing the view aspects of a Track.                                                                                                        |

#### `take_lanes`

- **Returns:** `Sequence[TakeLane]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `12.2`

**Description:** The list of this track's take lanes

#### `clip_slots`

- **Returns:** `Sequence[ClipSlot]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** const access to the list of clipslots (see class AClipSlot) for this track.The list will be empty for
the main and sendtracks.

#### `arrangement_clips`

- **Returns:** `Sequence[Clip]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.0`

**Description:** The list of this track's Arrangement View clip IDs. The list is empty for the main track, send/return
tracks, and group tracks.

_Available since Live 11.0._

#### `devices`

- **Returns:** `Sequence[Device]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Includes mixer device.

#### `group_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The Group Track, if the Track is grouped. If it is not, _id 0_ is returned.

#### `mixer_device`

- **Returns:** `MixerDevice`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Return access to the special Device that every Track has: This Device containsthe Volume, Pan,
Sendamounts, and Crossfade assignment parameters.

#### `view`

- **Returns:** `Track.View`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Representing the view aspects of a Track.

### Properties

| Property                            | Get Returns    | Set Accepts    | Listenable | Available Since | Summary                                                                                                                                                                |
| ----------------------------------- | -------------- | -------------- | ---------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_live_ptr`                         | `Unknown`      | —              | `no`       | `<11`           | Unknown                                                                                                                                                                |
| `arm`                               | `bool`         | `bool`         | `yes`      | `<11`           | 1 = track is armed for recording.                                                                                                                                      |
| `available_input_routing_channels`  | `dictionary`   | —              | `yes`      | `<11`           | The list of available source channels for the track's input routing.                                                                                                   |
| `available_input_routing_types`     | `dictionary`   | —              | `yes`      | `<11`           | The list of available source types for the track's input routing.                                                                                                      |
| `available_output_routing_channels` | `dictionary`   | —              | `yes`      | `<11`           | The list of available target channels for the track's output routing.                                                                                                  |
| `available_output_routing_types`    | `dictionary`   | —              | `yes`      | `<11`           | The list of available target types for the track's output routing.                                                                                                     |
| `back_to_arranger`                  | `bool`         | `bool`         | `yes`      | `12.0`          | Get/set/observe the current state of the Single Track Back to Arrangement button (1 = highlighted).                                                                    |
| `can_be_armed`                      | `bool`         | —              | `no`       | `<11`           | 0 for return and master tracks.                                                                                                                                        |
| `can_be_frozen`                     | `bool`         | —              | `no`       | `<11`           | 1 = the track can be frozen, 0 = otherwise.                                                                                                                            |
| `can_show_chains`                   | `bool`         | —              | `no`       | `<11`           | 1 = the track contains an Instrument Rack device that can show chains in Session View.                                                                                 |
| `canonical_parent`                  | `LomObject`    | —              | `no`       | `<11`           | Get the canonical parent of the track.                                                                                                                                 |
| `color`                             | `int`          | `int`          | `yes`      | `<11`           | The RGB value of the track's color in the form `0x00rrggbb` or (2^16 _ red) + (2^8) _ green + blue, where red, green and blue are values from 0 (dark) to 255 (light). |
| `color_index`                       | `long`         | `long`         | `yes`      | `<11`           | The color index of the track.                                                                                                                                          |
| `current_input_routing`             | `symbol`       | `symbol`       | `yes`      | `<11`           | Get/Set the name of the current active input routing.When setting a new routing, the new routing must be one of the available ones.                                    |
| `current_input_sub_routing`         | `symbol`       | `symbol`       | `yes`      | `<11`           | Get/Set the current active input sub routing.When setting a new routing, the new routing must be one of the available ones.                                            |
| `current_monitoring_state`          | `int`          | `int`          | `yes`      | `<11`           | Get/Set the track's current monitoring state.                                                                                                                          |
| `current_output_routing`            | `symbol`       | `symbol`       | `yes`      | `<11`           | Get/Set the current active output routing.When setting a new routing, the new routing must be one of the available ones.                                               |
| `current_output_sub_routing`        | `symbol`       | `symbol`       | `yes`      | `<11`           | Get/Set the current active output sub routing.When setting a new routing, the new routing must be one of the available ones.                                           |
| `fired_slot_index`                  | `int`          | —              | `yes`      | `<11`           | Reflects the blinking clip slot.                                                                                                                                       |
| `fold_state`                        | `int`          | `int`          | `no`       | `<11`           | 0 = tracks within the Group Track are visible, 1 = Group Track is folded and the tracks within the Group Track are hidden [only available if `is_foldable` = 1]        |
| `has_audio_input`                   | `bool`         | —              | `no`       | `<11`           | 1 for audio tracks.                                                                                                                                                    |
| `has_audio_output`                  | `bool`         | —              | `no`       | `<11`           | 1 for audio tracks and MIDI tracks with instruments.                                                                                                                   |
| `has_midi_input`                    | `bool`         | —              | `no`       | `<11`           | 1 for MIDI tracks.                                                                                                                                                     |
| `has_midi_output`                   | `bool`         | —              | `no`       | `<11`           | 1 for MIDI tracks with no instruments and no audio effects.                                                                                                            |
| `implicit_arm`                      | `bool`         | `bool`         | `yes`      | `<11`           | A second arm state, only used by Push so far.                                                                                                                          |
| `input_meter_left`                  | `float`        | —              | `yes`      | `<11`           | Smoothed momentary peak value of left channel input meter, 0.0 to 1.0.                                                                                                 |
| `input_meter_level`                 | `float`        | —              | `yes`      | `<11`           | Hold peak value of input meters of audio and MIDI tracks, 0.0 ...                                                                                                      |
| `input_meter_right`                 | `float`        | —              | `yes`      | `<11`           | Smoothed momentary peak value of right channel input meter, 0.0 to 1.0.                                                                                                |
| `input_routing_channel`             | `dictionary`   | `dictionary`   | `yes`      | `<11`           | The currently selected source channel for the track's input routing.                                                                                                   |
| `input_routing_type`                | `dictionary`   | `dictionary`   | `yes`      | `<11`           | The currently selected source type for the track's input routing.                                                                                                      |
| `input_routings`                    | `list[symbol]` | `list[symbol]` | `yes`      | `<11`           | Const access to the list of available input routings.                                                                                                                  |
| `input_sub_routings`                | `list[symbol]` | `list[symbol]` | `yes`      | `<11`           | Return a list of all available input sub routings.                                                                                                                     |
| `is_foldable`                       | `bool`         | —              | `no`       | `<11`           | 1 = track can be (un)folded to hide or reveal the contained tracks.                                                                                                    |
| `is_frozen`                         | `bool`         | —              | `yes`      | `<11`           | 1 = the track is currently frozen.                                                                                                                                     |
| `is_grouped`                        | `bool`         | —              | `no`       | `<11`           | 1 = the track is contained within a Group Track.                                                                                                                       |
| `is_part_of_selection`              | `bool`         | —              | `no`       | `<11`           | Unknown                                                                                                                                                                |
| `is_showing_chains`                 | `bool`         | `bool`         | `yes`      | `<11`           | Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.                                                             |
| `is_visible`                        | `bool`         | —              | `no`       | `<11`           | 0 = track is hidden in a folded Group Track.                                                                                                                           |
| `mute`                              | `bool`         | `bool`         | `yes`      | `<11`           | [not in master track]                                                                                                                                                  |
| `muted_via_solo`                    | `bool`         | —              | `yes`      | `<11`           | 1 = the track or chain is muted due to Solo being active on at least one other track.                                                                                  |
| `name`                              | `symbol`       | `symbol`       | `yes`      | `<11`           | As shown in track header.                                                                                                                                              |
| `output_meter_left`                 | `float`        | —              | `yes`      | `<11`           | Smoothed momentary peak value of left channel output meter, 0.0 to 1.0.                                                                                                |
| `output_meter_level`                | `float`        | —              | `yes`      | `<11`           | Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0.                                                                                                 |
| `output_meter_right`                | `float`        | —              | `yes`      | `<11`           | Smoothed momentary peak value of right channel output meter, 0.0 to 1.0.                                                                                               |
| `output_routing_channel`            | `dictionary`   | `dictionary`   | `yes`      | `<11`           | The currently selected target channel for the track's output routing.                                                                                                  |
| `output_routing_type`               | `dictionary`   | `dictionary`   | `yes`      | `<11`           | The currently selected target type for the track's output routing.                                                                                                     |
| `output_routings`                   | `list[symbol]` | `list[symbol]` | `yes`      | `<11`           | Const access to the list of all available output routings.                                                                                                             |
| `output_sub_routings`               | `list[symbol]` | `list[symbol]` | `yes`      | `<11`           | Return a list of all available output sub routings.                                                                                                                    |
| `performance_impact`                | `float`        | —              | `yes`      | `11.1`          | Reports the performance impact of this track.                                                                                                                          |
| `playing_slot_index`                | `int`          | —              | `yes`      | `<11`           | First slot has index 0, -2 = Clip Stop slot fired in Session View, -1 = Arrangement recording with no Session clip playing.                                            |
| `solo`                              | `bool`         | `bool`         | `yes`      | `<11`           | Remark: when setting this property, the exclusive Solo logic is bypassed, so you have to unsolo the other tracks yourself.                                             |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Unknown

#### `arm`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group`
- **Available Since:** `<11`

**Description:** 1 = track is armed for recording. [not in return/master tracks]

#### `available_input_routing_channels`

- **Get Returns:** `dictionary`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio`
- **Available Since:** `<11`

**Description:** The list of available source channels for the track's input routing. It's represented as a _dictionary_
with the following key:
`available_input_routing_channels` [list]
The list contains _dictionaries_ as described in _input_routing_channel_.
Only available on MIDI and audio tracks.

Raw docs state MIDI/audio-only, but current probes (Live 12.3.5) also returned this member on group, return, and master
tracks.

#### `available_input_routing_types`

- **Get Returns:** `dictionary`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio`
- **Available Since:** `<11`

**Description:** The list of available source types for the track's input routing. It's represented as a _dictionary_
with the following key:
`available_input_routing_types` [list]
The list contains _dictionaries_ as described in _input_routing_type_.
Only available on MIDI and audio tracks.

Raw docs state MIDI/audio-only, but current probes (Live 12.3.5) also returned this member on group, return, and master
tracks.

#### `available_output_routing_channels`

- **Get Returns:** `dictionary`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** The list of available target channels for the track's output routing. It's represented as a
_dictionary_ with the following key:
`available_output_routing_channels` [list]
The list contains _dictionaries_ as described in _output_routing_channel_.
Not available on the master track.

Raw docs state this is unavailable on master, but current probes (Live 12.3.5) returned this member on the master track
as well.

#### `available_output_routing_types`

- **Get Returns:** `dictionary`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** The list of available target types for the track's output routing. It's represented as a _dictionary_
with the following key:
`available_output_routing_types` [list]
The list contains _dictionaries_ as described in _output_routing_type_.
Not available on the master track.

Raw docs state this is unavailable on master, but current probes (Live 12.3.5) returned this member on the master track
as well.

#### `back_to_arranger`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `12.0`

**Description:** Get/set/observe the current state of the Single Track Back to Arrangement button (1 = highlighted).
This button is used to indicate that the current state of the playback differs from what is stored in the Arrangement.

Setting this property to 0 will make Live go back to playing the track's arrangement content. For group tracks, this
means that all of the tracks that belong to the group and any subgroups will go back to playing the arrangement.

#### `can_be_armed`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 0 for return and master tracks.

#### `can_be_frozen`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the track can be frozen, 0 = otherwise.

#### `can_show_chains`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the track contains an Instrument Rack device that can show chains in Session View.

#### `canonical_parent`

- **Get Returns:** `LomObject`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the canonical parent of the track.

#### `color`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The RGB value of the track's color in the form `0x00rrggbb` or (2^16 _ red) + (2^8) _ green + blue,
where red, green and blue are values from 0 (dark) to 255 (light).

When setting the RGB value, the nearest color from the track color chooser is taken.
In current probes, setting this property to `None` raised an error.

#### `color_index`

- **Get Returns:** `long`
- **Set Accepts:** `long`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The color index of the track. Tracks always have a color in the Live UI —
there is no "no color" option — so `None` is not a meaningful value. Setting to `None` is
accepted without error but silently discarded; the value remains unchanged.

**Default Color Assignment (probed in Live 12.3.5):**

When a new Live Set is created, Live generates a **17-color permutation** selected from the
26 chromatic palette slots (indices 0–12 and 14–26). The two neutral slots — white (index 13)
and light_gray (index 27) — are never used, nor are any colors from the pale, muted, or deep
rows (indices 28–69). The 17-color cycle is a subset of the 26 chromatic slots; which 17 and
in what order varies per set (PRNG-seeded, limited entropy — identical sequences observed
across separate sessions).

Tracks are assigned colors from this cycle using **two independent cursors**:

- **Main tracks** walk **forward** through the cycle. The 4 default tracks consume positions
  0–3. Each subsequent `create_midi_track` / `create_audio_track` gets the next position,
  wrapping after 17.
- **Master track** gets the **last** color in the forward cycle (position 16), which is
  equivalently position 0 of the reversed cycle.
- **Return tracks** walk **backward** from the master. The 2 default return tracks consume
  reverse positions 1–2. Each subsequent `create_return_track` gets the next reverse position,
  wrapping after 17.

This means main and return tracks naturally receive contrasting colors — they approach the
same hue ring from opposite ends. After 17 tracks of either type, colors begin repeating.

_Probed by creating 10 new sets (50 via AppleScript in a prior run), adding 15 main + 5 return
tracks per set, and verifying cycle structure. Confirmed: main-only sequences cycle at length
17, return sequences follow the reversed main cycle, master = reverse position 0._

#### `current_input_routing`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set the name of the current active input routing.When setting a new routing, the new routing must
be one of the available ones.

Legacy compatibility property. Prefer `input_routing_type` (dictionary with `display_name` and `identifier`).

#### `current_input_sub_routing`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set the current active input sub routing.When setting a new routing, the new routing must be one of
the available ones.

Legacy compatibility property. Prefer `input_routing_channel` (dictionary with `display_name` and `identifier`).

#### `current_monitoring_state`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set the track's current monitoring state.

In current probes, accepted values were `0`, `1`, and `2`; setting values `>=3` returned `Invalid monitoring state!`.
Semantic labels for `0/1/2` are still unconfirmed in raw docs.

#### `current_output_routing`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set the current active output routing.When setting a new routing, the new routing must be one of
the available ones.

Legacy compatibility property. Prefer `output_routing_type` (dictionary with `display_name` and `identifier`).

#### `current_output_sub_routing`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get/Set the current active output sub routing.When setting a new routing, the new routing must be one
of the available ones.

Legacy compatibility property. Prefer `output_routing_channel` (dictionary with `display_name` and `identifier`).

#### `fired_slot_index`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group`
- **Available Since:** `<11`

**Description:** Reflects the blinking clip slot.
-1 = no slot fired, -2 = Clip Stop Button fired
First clip slot has index 0.
[not in return/master tracks]
Current probes matched these sentinel values.

#### `fold_state`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `no`
- **Applicable to:** `group`
- **Available Since:** `<11`

**Description:** 0 = tracks within the Group Track are visible, 1 = Group Track is folded and the tracks within the
Group Track are hidden
[only available if `is_foldable` = 1]

#### `has_audio_input`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 for audio tracks.

#### `has_audio_output`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 for audio tracks and MIDI tracks with instruments.

#### `has_midi_input`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 for MIDI tracks.

#### `has_midi_output`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 for MIDI tracks with no instruments and no audio effects.

#### `implicit_arm`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** A second arm state, only used by Push so far.

#### `input_meter_left`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`

**Description:** Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio input
only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters put
a significant load onto the GUI part of Live.

#### `input_meter_level`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Hold peak value of input meters of audio and MIDI tracks, 0.0 ... 1.0. For audio tracks it is the
maximum of the left and right channels. The hold time is 1 second.

#### `input_meter_right`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `audio`
- **Available Since:** `<11`

**Description:** Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio input
only. This value corresponds to the meters shown in Live.

#### `input_routing_channel`

- **Get Returns:** `dictionary`
- **Set Accepts:** `dictionary`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `midi/audio`
- **Available Since:** `<11`

**Description:** The currently selected source channel for the track's input routing. It's represented as a _dictionary_
with the following keys:
`display_name` [symbol]
`identifier` [symbol]
Can be set to all values found in the track's _available_input_routing_channels_.
Only available on MIDI and audio tracks.

Raw docs state MIDI/audio-only, but current probes (Live 12.3.5) also returned this member on group, return, and master
tracks.

Set/get round-trip succeeded in current probes across all probed track kinds.

#### `input_routing_type`

- **Get Returns:** `dictionary`
- **Set Accepts:** `dictionary`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `midi/audio`
- **Available Since:** `<11`

**Description:** The currently selected source type for the track's input routing. It's represented as a _dictionary_
with the following keys:
`display_name` [symbol]
`identifier` [symbol]
Can be set to all values found in the track's _available_input_routing_types_.
Only available on MIDI and audio tracks.

Raw docs state MIDI/audio-only, but current probes (Live 12.3.5) also returned this member on group, return, and master
tracks.

Set/get round-trip succeeded in current probes across all probed track kinds.

#### `input_routings`

- **Get Returns:** `list[symbol]`
- **Set Accepts:** `list[symbol]`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Const access to the list of available input routings.

Legacy compatibility property. Prefer `available_input_routing_types`.

#### `input_sub_routings`

- **Get Returns:** `list[symbol]`
- **Set Accepts:** `list[symbol]`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Return a list of all available input sub routings.

Legacy compatibility property. Prefer `available_input_routing_channels`.

#### `is_foldable`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = track can be (un)folded to hide or reveal the contained tracks. This is currently the case for
Group Tracks. Instrument and Drum Racks return 0 although they can be opened/closed. This will be fixed in a later
release.

#### `is_frozen`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the track is currently frozen.

#### `is_grouped`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the track is contained within a Group Track.

#### `is_part_of_selection`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Unknown

#### `is_showing_chains`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get or set whether a track with an Instrument Rack device is currently showing its chains in Session
View.

#### `is_visible`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 0 = track is hidden in a folded Group Track.

#### `mute`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** [not in master track]

#### `muted_via_solo`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** 1 = the track or chain is muted due to Solo being active on at least one other track.

#### `name`

- **Get Returns:** `symbol`
- **Set Accepts:** `symbol`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** As shown in track header.

#### `output_meter_left`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output
only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters add
a significant load to Live GUI resource usage.

#### `output_meter_level`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the
maximum of the left and right channels. The hold time is 1 second.

#### `output_meter_right`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output
only. This value corresponds to the meters shown in Live.

#### `output_routing_channel`

- **Get Returns:** `dictionary`
- **Set Accepts:** `dictionary`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** The currently selected target channel for the track's output routing. It's represented as a
_dictionary_ with the following keys:
`display_name` [symbol]
`identifier` [symbol]
Can be set to all values found in the track's _available_output_routing_channels_.
Not available on the master track.

Raw docs state this is unavailable on master, but current probes (Live 12.3.5) returned this member on the master track
as well.

Set/get round-trip succeeded in current probes across all probed track kinds.
On several non-master tracks in the probe set, only one output channel option was available.

#### `output_routing_type`

- **Get Returns:** `dictionary`
- **Set Accepts:** `dictionary`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** The currently selected target type for the track's output routing. It's represented as a _dictionary_
with the following keys:
`display_name` [symbol]
`identifier` [symbol]
Can be set to all values found in the track's _available_output_routing_types_.
Not available on the master track.

Raw docs state this is unavailable on master, but current probes (Live 12.3.5) returned this member on the master track
as well.

Set/get round-trip succeeded in current probes across all probed track kinds.

#### `output_routings`

- **Get Returns:** `list[symbol]`
- **Set Accepts:** `list[symbol]`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Const access to the list of all available output routings.

Legacy compatibility property. Prefer `available_output_routing_types`.

#### `output_sub_routings`

- **Get Returns:** `list[symbol]`
- **Set Accepts:** `list[symbol]`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Return a list of all available output sub routings.

Legacy compatibility property. Prefer `available_output_routing_channels`.

#### `performance_impact`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `11.1`

**Description:** Reports the performance impact of this track.

#### `playing_slot_index`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group`
- **Available Since:** `<11`

**Description:** First slot has index 0, -2 = Clip Stop slot fired in Session View, -1 = Arrangement recording with no
Session clip playing. [not in return/master tracks]
Current probes matched these sentinel values.

#### `solo`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `no`
  - **Async visibility:** `immediate` (probed on MIDI track)
- **Listenable:** `yes`
- **Applicable to:** `midi/audio/group/return`
- **Available Since:** `<11`

**Description:** Remark: when setting this property, the exclusive Solo logic is bypassed, so you have to unsolo the
other tracks yourself. [not in master track]

### Methods

| Signature                                                            | Returns     | Available Since | Summary                                                                                                                                                                                                                   |
| -------------------------------------------------------------------- | ----------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__init__(*a, **k)`                                                  | `Unknown`   | `N/A`           | This class represents a track in Live.                                                                                                                                                                                    |
| `create_audio_clip(arg2: object, arg3: float)`                       | `Clip`      | `11.3`          | Parameters: `file_path` [symbol] `position` [float] Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at the specified position in the arrangement view. |
| `create_midi_clip(arg2: float, arg3: float)`                         | `Clip`      | `12.1`          | Parameters: `start_time` [float] `length` [float] Creates an empty MIDI clip and inserts it into the arrangement at the specified time.                                                                                   |
| `create_take_lane()`                                                 | `LomObject` | `12.2`          | Creates a take lane for this track.                                                                                                                                                                                       |
| `delete_clip(arg2: Clip)`                                            | `None`      | `<11`           | Parameter: `clip` Delete the given clip.                                                                                                                                                                                  |
| `delete_device(arg2: int)`                                           | `None`      | `<11`           | Parameter: `index` Delete the device at the given index.                                                                                                                                                                  |
| `duplicate_clip_slot(arg2: int)`                                     | `int`       | `<11`           | Parameter: `index` Works like 'Duplicate' in a clip's context menu.                                                                                                                                                       |
| `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)` | `Clip`      | `<11`           | Parameters: `clip``destination_time` [float] Duplicate the given clip to the Arrangement, placing it at the given _destination_time_ in beats.                                                                            |
| `duplicate_device(arg2: int)`                                        | `None`      | `12.3`          | Duplicate a device at a given index in the 'devices' list.                                                                                                                                                                |
| `get_data(key: object, default_value: object)`                       | `object`    | `<11`           | Get data for the given key, that was previously stored using set_data.                                                                                                                                                    |
| `insert_device(DeviceName: str, DeviceIndex: int)`                   | `LomObject` | `12.3`          | Parameters: `device_name` [symbol] `target_index` [int] (optional) Attempts to insert the device specified by `device_name` at the given index in the track's device chain.                                               |
| `jump_in_running_session_clip(arg2: float)`                          | `None`      | `<11`           | Parameter: `beats` `beats` [float] is the amount to jump relatively to the current clip position.                                                                                                                         |
| `set_data(key: object, value: object)`                               | `None`      | `<11`           | Store data for the given key in this object.                                                                                                                                                                              |
| `stop_all_clips(Quantized: bool)`                                    | `None`      | `<11`           | Stops all playing and fired clips in this track.                                                                                                                                                                          |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** This class represents a track in Live. It can be either an Audio track, a MIDI Track, a Return Track or
the Main track. The Main Track and at least one Audio or MIDI track will be always present.Return Tracks are optional.

#### `create_audio_clip(arg2: object, arg3: float)`

- **Returns:** `Clip`
- **Args:** arg2: object, arg3: float
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `11.3`

**Description:** Parameters:
`file_path` [symbol]
`position` [float]
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at
the specified position in the arrangement view. Prints an error if the track is not an audio track, if the track is
frozen, or if the track is being recorded into. The position must be within the range [0., 1576800].

See the `ClipSlot.create_audio_clip` function if you need to create audio clips in session view instead.

#### `create_midi_clip(arg2: float, arg3: float)`

- **Returns:** `Clip`
- **Args:** arg2: float, arg3: float
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `12.1`

**Description:** Parameters:
`start_time` [float]
`length` [float]
Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a
non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is
currently being recorded into.

See the `ClipSlot.create_clip` function if you need to create audio clips in session view instead.

#### `create_take_lane()`

- **Returns:** `LomObject`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `12.2`

**Description:** Creates a take lane for this track.

#### `delete_clip(arg2: Clip)`

- **Returns:** `None`
- **Args:** arg2: Clip
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: `clip`
Delete the given clip.

#### `delete_device(arg2: int)`

- **Returns:** `None`
- **Args:** arg2: int
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: `index`
Delete the device at the given index.

#### `duplicate_clip_slot(arg2: int)`

- **Returns:** `int`
- **Args:** arg2: int
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: `index`

Works like 'Duplicate' in a clip's context menu.

#### `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)`

- **Returns:** `Clip`
- **Args:** clip: Clip, destination_time: float
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameters: `clip``destination_time` [float]

Duplicate the given clip to the Arrangement, placing it at the given _destination_time_ in beats.

#### `duplicate_device(arg2: int)`

- **Returns:** `None`
- **Args:** arg2: int
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `12.3`

**Description:** Duplicate a device at a given index in the 'devices' list. C++ signature : void
duplicate_device(TTrackPyHandle,int) :param arg2: arg2 :type arg2: int :rtype: None

#### `get_data(key: object, default_value: object)`

- **Returns:** `object`
- **Args:** key: object, default_value: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Get data for the given key, that was previously stored using set_data. C++ signature :
boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object) :param key: key :type key: object
:param default_value: default_value :type default_value: object :rtype: object

In current probes (Live 12.3.5), after `set_data(key, None)`, `get_data(key, default_value)` returned `None` rather than
the provided default.

#### `insert_device(DeviceName: str, DeviceIndex: int)`

- **Returns:** `LomObject`
- **Args:** DeviceName: str, DeviceIndex: int
- **Raises/Errors:** `ValidationError: Device {name} not found.` if the name doesn't match any native device.
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Inserts a new device into the track's device chain.
- **Async visibility:** `Unknown`
- **Available Since:** `12.3`
- **Probe Status:** `probed` (2026-02-26)

**Description:** Parameters: `device_name` [symbol] `target_index` [int] (optional)

Attempts to insert the device specified by `device_name` at the given index in the track's device chain. If no index is
provided, attempts to insert the device at the end of the chain. Throws an error if insertion is not possible.

**`device_name` must be the exact `class_display_name`** — the name shown in the Live browser UI (e.g. `"EQ Eight"`,
not `"Eq8"`). Matching is case-sensitive (`"eq eight"` fails). The internal `class_name` is not accepted.

Not all indices are valid. Indices outside the current device count are invalid, and structural constraints apply —
for example, a MIDI effect cannot be inserted after an instrument. The rule is: if the position would be invalid
when dragging with the mouse, it's invalid here.

Only native Live devices can be inserted. Third-party plug-ins (VST/AU) and Max for Live devices are not supported
(probed: `"Raum"` → `Device Raum not found.`). The empty M4L container shell (`"Max Audio Effect"` etc.) can be
inserted as it is a native device.

_Available since Live 12.3._

#### `jump_in_running_session_clip(arg2: float)`

- **Returns:** `None`
- **Args:** arg2: float
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Parameter: `beats`

`beats` [float] is the amount to jump relatively to the current clip position.
Modify playback position in running Session clip, if any.

#### `set_data(key: object, value: object)`

- **Returns:** `None`
- **Args:** key: object, value: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `no`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Store data for the given key in this object. The data is persistent and will be restored when loading
the Live Set. C++ signature : void set_data(TTrackPyHandle,TString,boost::python::api::object) :param key: key :type
key: object :param value: value :type value: object :rtype: None

#### `stop_all_clips(Quantized: bool)`

- **Returns:** `None`
- **Args:** Quantized: bool
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Stops all playing and fired clips in this track.

## Track.View

Representing the view aspects of a track.

### Children

| Child             | Returns  | Shape    | Access | Listenable | Available Since | Summary                                                                              |
| ----------------- | -------- | -------- | ------ | ---------- | --------------- | ------------------------------------------------------------------------------------ |
| `selected_device` | `Device` | `single` | `get`  | `yes`      | `<11`           | The selected device or the first selected device (in case of multi/group selection). |

#### `selected_device`

- **Returns:** `Device`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The selected device or the first selected device (in case of multi/group selection).

### Properties

| Property             | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                                  |
| -------------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------------------------------------------------ |
| `_live_ptr`          | `Unknown`   | —           | `no`       | `<11`           | Unknown                                                                  |
| `canonical_parent`   | `Track`     | —           | `no`       | `<11`           | Get the canonical parent of the track view.                              |
| `device_insert_mode` | `int`       | `int`       | `yes`      | `<11`           | Determines where a device will be inserted when loaded from the browser. |
| `is_collapsed`       | `bool`      | `bool`      | `yes`      | `<11`           | In Arrangement View: 1 = track collapsed, 0 = track opened.              |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Unknown

#### `canonical_parent`

- **Get Returns:** `Track`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Get the canonical parent of the track view.

#### `device_insert_mode`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Determines where a device will be inserted when loaded from the browser. 0 = add device at the end, 1 =
add device to the left of the selected device, 2 = add device to the right of the selected device.

#### `is_collapsed`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** In Arrangement View: 1 = track collapsed, 0 = track opened.

### Methods

| Signature             | Returns   | Available Since | Summary                                                                                                                          |
| --------------------- | --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `__init__(*a, **k)`   | `Unknown` | `N/A`           | Representing the view aspects of a Track.                                                                                        |
| `select_instrument()` | `bool`    | `<11`           | Returns: bool 0 = there are no devices to select Selects track's instrument or first device, makes it visible and focuses on it. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Representing the view aspects of a Track.

#### `select_instrument()`

- **Returns:** `bool`
- **Args:** `None`
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Returns: bool 0 = there are no devices to select
Selects track's instrument or first device, makes it visible and focuses on it.

## Track.DeviceContainer

Unknown

### Children

None.

### Properties

| Property    | Get Returns | Set Accepts | Listenable | Available Since | Summary |
| ----------- | ----------- | ----------- | ---------- | --------------- | ------- |
| `_live_ptr` | `Unknown`   | —           | `no`       | `<11`           | Unknown |

#### `_live_ptr`

- **Get Returns:** `Unknown`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Unknown

### Methods

| Signature           | Returns   | Available Since | Summary                                               |
| ------------------- | --------- | --------------- | ----------------------------------------------------- |
| `__init__(*a, **k)` | `Unknown` | `N/A`           | This class is a common super class of Track and Chain |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** This class is a common super class of Track and Chain

## Track.DeviceInsertMode

Unknown

Enumeration used by `Track.View.device_insert_mode`.

Known values from current sources:

- `0`: add at end
- `1`: insert left of selected device
- `2`: insert right of selected device

### Children

None.

### Properties

None.

### Methods

| Signature             | Returns   | Available Since | Summary                                                     |
| --------------------- | --------- | --------------- | ----------------------------------------------------------- |
| `__init__(*a, **k)`   | `Unknown` | `N/A`           | Unknown                                                     |
| `from_bytes(*a, **k)` | `None`    | `N/A`           | Return the integer represented by the given array of bytes. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Unknown

#### `from_bytes(*a, **k)`

- **Returns:** `None`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Return the integer represented by the given array of bytes. bytes Holds the array of bytes to convert.
The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are
examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer.
If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the
most significant byte is at the end of the byte array. To request the native byte order of the host system, use
`sys.byteorder' as the byte order value. Default is to use 'big'. signed Indicates whether two's complement is used to
represent the integer.

## Track.RoutingChannel

Unknown

### Children

None.

### Properties

| Property       | Get Returns                  | Set Accepts | Listenable | Available Since | Summary                                             |
| -------------- | ---------------------------- | ----------- | ---------- | --------------- | --------------------------------------------------- |
| `display_name` | `symbol`                     | —           | `no`       | `<11`           | Display name of routing channel.                    |
| `layout`       | `Track.RoutingChannelLayout` | —           | `no`       | `<11`           | The routing channel's Layout, e.g., mono or stereo. |

#### `display_name`

- **Get Returns:** `symbol`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Display name of routing channel.

#### `layout`

- **Get Returns:** `Track.RoutingChannelLayout`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** The routing channel's Layout, e.g., mono or stereo.

### Methods

| Signature           | Returns   | Available Since | Summary                                  |
| ------------------- | --------- | --------------- | ---------------------------------------- |
| `__init__(*a, **k)` | `Unknown` | `N/A`           | This class represents a routing channel. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** This class represents a routing channel.

## Track.RoutingChannelLayout

Unknown

Enumeration for routing channel layout (for example mono/stereo).

### Children

None.

### Properties

None.

### Methods

| Signature             | Returns   | Available Since | Summary                                                     |
| --------------------- | --------- | --------------- | ----------------------------------------------------------- |
| `__init__(*a, **k)`   | `Unknown` | `N/A`           | Unknown                                                     |
| `from_bytes(*a, **k)` | `None`    | `N/A`           | Return the integer represented by the given array of bytes. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Unknown

#### `from_bytes(*a, **k)`

- **Returns:** `None`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Return the integer represented by the given array of bytes. bytes Holds the array of bytes to convert.
The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are
examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer.
If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the
most significant byte is at the end of the byte array. To request the native byte order of the host system, use
`sys.byteorder' as the byte order value. Default is to use 'big'. signed Indicates whether two's complement is used to
represent the integer.

## Track.RoutingChannelVector

Unknown

### Children

None.

### Properties

None.

### Methods

| Signature              | Returns   | Available Since | Summary                                                                                                                                                                                                              |
| ---------------------- | --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__init__(*a, **k)`    | `Unknown` | `N/A`           | A container for returning routing channels from Live.                                                                                                                                                                |
| `append(arg2: object)` | `None`    | `N/A`           | C++ signature : void append(std::**1::vector<NRoutingApi::TRoutingChannel, std::**1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2: object :rtype: None |
| `extend(arg2: object)` | `None`    | `N/A`           | C++ signature : void extend(std::**1::vector<NRoutingApi::TRoutingChannel, std::**1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2: object :rtype: None |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** A container for returning routing channels from Live.

#### `append(arg2: object)`

- **Returns:** `None`
- **Args:** arg2: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** C++ signature : void append(std::**1::vector<NRoutingApi::TRoutingChannel,
std::**1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2:
object :rtype: None

#### `extend(arg2: object)`

- **Returns:** `None`
- **Args:** arg2: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** C++ signature : void extend(std::**1::vector<NRoutingApi::TRoutingChannel,
std::**1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2:
object :rtype: None

## Track.RoutingType

Unknown

### Children

None.

### Properties

| Property          | Get Returns                 | Set Accepts | Listenable | Available Since | Summary                                       |
| ----------------- | --------------------------- | ----------- | ---------- | --------------- | --------------------------------------------- |
| `attached_object` | `LomObject`                 | —           | `no`       | `<11`           | Live object associated with the routing type. |
| `category`        | `Track.RoutingTypeCategory` | —           | `no`       | `<11`           | Category of the routing type.                 |
| `display_name`    | `symbol`                    | —           | `no`       | `<11`           | Display name of routing type.                 |

#### `attached_object`

- **Get Returns:** `LomObject`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Live object associated with the routing type.

#### `category`

- **Get Returns:** `Track.RoutingTypeCategory`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Category of the routing type.

#### `display_name`

- **Get Returns:** `symbol`
- **Set Accepts:** —
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`

**Description:** Display name of routing type.

### Methods

| Signature           | Returns   | Available Since | Summary                               |
| ------------------- | --------- | --------------- | ------------------------------------- |
| `__init__(*a, **k)` | `Unknown` | `N/A`           | This class represents a routing type. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** This class represents a routing type.

## Track.RoutingTypeCategory

Unknown

Enumeration for routing type categories.

### Children

None.

### Properties

None.

### Methods

| Signature             | Returns   | Available Since | Summary                                                     |
| --------------------- | --------- | --------------- | ----------------------------------------------------------- |
| `__init__(*a, **k)`   | `Unknown` | `N/A`           | Unknown                                                     |
| `from_bytes(*a, **k)` | `None`    | `N/A`           | Return the integer represented by the given array of bytes. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Unknown

#### `from_bytes(*a, **k)`

- **Returns:** `None`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Return the integer represented by the given array of bytes. bytes Holds the array of bytes to convert.
The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are
examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer.
If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the
most significant byte is at the end of the byte array. To request the native byte order of the host system, use
`sys.byteorder' as the byte order value. Default is to use 'big'. signed Indicates whether two's complement is used to
represent the integer.

## Track.RoutingTypeVector

Unknown

### Children

None.

### Properties

None.

### Methods

| Signature              | Returns   | Available Since | Summary                                                                                                                                                                                                        |
| ---------------------- | --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `__init__(*a, **k)`    | `Unknown` | `N/A`           | A container for returning routing types from Live.                                                                                                                                                             |
| `append(arg2: object)` | `None`    | `N/A`           | C++ signature : void append(std::**1::vector<NRoutingApi::TRoutingType, std::**1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2: object :rtype: None |
| `extend(arg2: object)` | `None`    | `N/A`           | C++ signature : void extend(std::**1::vector<NRoutingApi::TRoutingType, std::**1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2: object :rtype: None |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** A container for returning routing types from Live.

#### `append(arg2: object)`

- **Returns:** `None`
- **Args:** arg2: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** C++ signature : void append(std::**1::vector<NRoutingApi::TRoutingType,
std::**1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2:
object :rtype: None

#### `extend(arg2: object)`

- **Returns:** `None`
- **Args:** arg2: object
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** C++ signature : void extend(std::**1::vector<NRoutingApi::TRoutingType,
std::**1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object) :param arg2: arg2 :type arg2:
object :rtype: None

## Track.monitoring_states

Enumeration used by `Track.current_monitoring_state`.

Numeric member names are not documented in current raw sources.

Current probe results (Live 12.3.5):

| Value | Set Accepted | Notes                                 |
| ----- | ------------ | ------------------------------------- |
| `0`   | `yes`        | Semantic label unknown.               |
| `1`   | `yes`        | Semantic label unknown.               |
| `2`   | `yes`        | Semantic label unknown.               |
| `>=3` | `no`         | Returned `Invalid monitoring state!`. |

### Children

None.

### Properties

None.

### Methods

| Signature             | Returns   | Available Since | Summary                                                     |
| --------------------- | --------- | --------------- | ----------------------------------------------------------- |
| `__init__(*a, **k)`   | `Unknown` | `N/A`           | Unknown                                                     |
| `from_bytes(*a, **k)` | `None`    | `<11`           | Return the integer represented by the given array of bytes. |

#### `__init__(*a, **k)`

- **Returns:** `Unknown`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Unknown

#### `from_bytes(*a, **k)`

- **Returns:** `None`
- **Args:** \*a, \*\*k
- **Raises/Errors:** `Unknown`
- **Applicable to:** `all`
- **Undo-tracked:** `Unknown`
- **Side Effects:** `Unknown`
- **Async visibility:** `Unknown`
- **Available Since:** `<11`

**Description:** Return the integer represented by the given array of bytes. bytes Holds the array of bytes to convert.
The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are
examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer.
If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the
most significant byte is at the end of the byte array. To request the native byte order of the host system, use
`sys.byteorder' as the byte order value. Default is to use 'big'. signed Indicates whether two's complement is used to
represent the integer.

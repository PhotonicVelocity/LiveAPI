# MixerDevice

## MixerDevice

This class represents a track's mixer device in Live, providing access to volume, panning,
sends, and other mixer-related parameters. Every track has a mixer device. The master track's
mixer device additionally exposes the crossfader, cue volume, and song tempo parameters.

All mixer parameters are exposed as `DeviceParameter` objects, which means they can be
automated, MIDI-mapped, and modified via the API.

### Sources

- **Primary:** `Live/classes/devices/MixerDevice.py` (stub dump)
- **Secondary:** `MaxForLive/mixerdevice.md`
- **Probes:** `probe_mixer_device.py`

### Probe Notes

- **Master-only children raise on regular tracks:**
  - `crossfader` → `InternalError: "Only the main track has a crossfader!"`
  - `cue_volume` → `InternalError: "Cue volume available on the main track only!"`
  - `song_tempo` → `InternalError: "Only the main track has the song tempo!"`
- **`crossfade_assign` raises on master:** `InternalError: "Main track has no crossfader assignment!"`
- **`panning_mode` IS settable:** set to `1` (Split Stereo), readback=`1`. Confirmed writable.
- **Master track has 0 sends** — `sends` returns an empty list on the master track.

### Open Questions

None — all key questions resolved by probing.

### Children

| Child                | Returns                     | Shape    | Access | Listenable | Available Since | Summary                                             |
| -------------------- | --------------------------- | -------- | ------ | ---------- | --------------- | --------------------------------------------------- |
| `crossfader`         | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Crossfader parameter. Master track only.            |
| `cue_volume`         | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Cue/preview volume. Master track only.              |
| `left_split_stereo`  | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Left split stereo pan parameter.                    |
| `panning`            | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Pan parameter.                                      |
| `right_split_stereo` | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Right split stereo pan parameter.                   |
| `sends`              | `Sequence[DeviceParameter]` | `list`   | `get`  | `yes`      | `<11`           | Send amount parameters, one per return track.       |
| `song_tempo`         | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Song tempo as a DeviceParameter. Master track only. |
| `track_activator`    | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Track on/off toggle parameter.                      |
| `volume`             | `DeviceParameter`           | `single` | `get`  | `no`       | `<11`           | Volume parameter.                                   |

#### `crossfader`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `master`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — raises on non-master tracks

**Description:**
The crossfader parameter. Only available on the master track's mixer device. Controls the
A/B crossfade position. Accessing on a non-master track raises
`InternalError: "Only the main track has a crossfader!"`.

#### `cue_volume`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `master`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — raises on non-master tracks

**Description:**
The cue (preview/solo) volume parameter. Only available on the master track's mixer device.
Accessing on a non-master track raises
`InternalError: "Cue volume available on the main track only!"`.

#### `left_split_stereo`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The left channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `panning`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The track's panning parameter. In standard stereo mode, this controls the stereo position.
In split stereo mode, this parameter exists but may not be the active control — use
`left_split_stereo` and `right_split_stereo` instead.

#### `right_split_stereo`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The right channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `sends`

- **Returns:** `Sequence[DeviceParameter]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all` (but master track has 0 sends)
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — master track returns empty list

**Description:**
The list of send amount parameters, one per return track. The order matches
`Song.return_tracks`. The listener fires when return tracks are added or removed (changing
the send count). The master track's sends list is always empty.

#### `song_tempo`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `master`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — raises on non-master tracks

**Description:**
The song's tempo exposed as a `DeviceParameter` on the master track's mixer. This allows
the tempo to be automated via the same parameter mechanism as other mixer controls. Accessing
on a non-master track raises `InternalError: "Only the main track has the song tempo!"`.

#### `track_activator`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The track's on/off toggle (activator) as a `DeviceParameter`. This is the same toggle
controlled by the track's mute state, exposed here for automation and mapping.

#### `volume`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The track's volume fader as a `DeviceParameter`.

### Properties

| Property           | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                   |
| ------------------ | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------------- |
| `crossfade_assign` | `int`       | `int`       | `yes`      | `<11`           | Crossfade assignment: 0=A, 1=none, 2=B. Raises on master. |
| `panning_mode`     | `int`       | `int`       | `yes`      | `<11`           | Panning mode: 0=Stereo, 1=Split Stereo. Settable.         |

#### `crossfade_assign`

- **Get Returns:** `int` (`MixerDevice.crossfade_assignments`)
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Applicable to:** `audio/midi/group/return` (not master)
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — raises on master track

**Description:**
The track's crossfade assignment:

- `0` = A (assigned to crossfader side A)
- `1` = none (not crossfade-assigned)
- `2` = B (assigned to crossfader side B)

Accessing on the master track raises
`InternalError: "Main track has no crossfader assignment!"`.

#### `panning_mode`

- **Get Returns:** `int` (`MixerDevice.panning_modes`)
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — settable, set to 1 with correct readback

**Description:**
The track's panning mode:

- `0` = Stereo — standard single-knob panning
- `1` = Split Stereo — separate left/right pan controls via `left_split_stereo` and
  `right_split_stereo`

Settable. Setting `panning_mode=1` switches the track to split stereo panning.

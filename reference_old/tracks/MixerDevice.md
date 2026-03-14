# MixerDevice

> `Live.MixerDevice.MixerDevice`

This class represents a track's mixer device in Live, providing access to volume, panning,
sends, and other mixer-related parameters. Every track has a mixer device. The master track's
mixer device additionally exposes the crossfader, cue volume, and song tempo parameters.

All mixer parameters are exposed as `DeviceParameter` objects, which means they can be
automated, MIDI-mapped, and modified via the API.

??? note "Raw probe notes (temporary)"
    - **Master-only children raise on regular tracks:**
        - `crossfader` -> `InternalError: "Only the main track has a crossfader!"`
        - `cue_volume` -> `InternalError: "Cue volume available on the main track only!"`
        - `song_tempo` -> `InternalError: "Only the main track has the song tempo!"`
    - **`crossfade_assign` raises on master:** `InternalError: "Main track has no crossfader assignment!"`
    - **`panning_mode` IS settable:** set to `1` (Split Stereo), readback=`1`. Confirmed writable.
    - **Master track has 0 sends** -- `sends` returns an empty list on the master track.

### Open Questions

None -- all key questions resolved by probing.

### Children

| Child                | Returns                     | Shape    | Listenable | Summary                                             |
| -------------------- | --------------------------- | -------- | ---------- | --------------------------------------------------- |
| `crossfader`         | `DeviceParameter`           | `single` | `no`       | Crossfader parameter. Master track only.            |
| `cue_volume`         | `DeviceParameter`           | `single` | `no`       | Cue/preview volume. Master track only.              |
| `left_split_stereo`  | `DeviceParameter`           | `single` | `no`       | Left split stereo pan parameter.                    |
| `panning`            | `DeviceParameter`           | `single` | `no`       | Pan parameter.                                      |
| `right_split_stereo` | `DeviceParameter`           | `single` | `no`       | Right split stereo pan parameter.                   |
| `sends`              | `Sequence[DeviceParameter]` | `list`   | `yes`      | Send amount parameters, one per return track.       |
| `song_tempo`         | `DeviceParameter`           | `single` | `no`       | Song tempo as a DeviceParameter. Master track only. |
| `track_activator`    | `DeviceParameter`           | `single` | `no`       | Track on/off toggle parameter.                      |
| `volume`             | `DeviceParameter`           | `single` | `no`       | Volume parameter.                                   |

#### `crossfader`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The crossfader parameter. Only available on the master track's mixer device. Controls the
A/B crossfade position. Accessing on a non-master track raises
`InternalError: "Only the main track has a crossfader!"`.

#### `cue_volume`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The cue (preview/solo) volume parameter. Only available on the master track's mixer device.
Accessing on a non-master track raises
`InternalError: "Cue volume available on the main track only!"`.

#### `left_split_stereo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The left channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `panning`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's panning parameter. In standard stereo mode, this controls the stereo position.
In split stereo mode, this parameter exists but may not be the active control -- use
`left_split_stereo` and `right_split_stereo` instead.

#### `right_split_stereo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The right channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `sends`

- **Type:** `Sequence[DeviceParameter]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of send amount parameters, one per return track. The order matches
`Song.return_tracks`. The listener fires when return tracks are added or removed (changing
the send count). The master track's sends list is always empty.

#### `song_tempo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The song's tempo exposed as a `DeviceParameter` on the master track's mixer. This allows
the tempo to be automated via the same parameter mechanism as other mixer controls. Accessing
on a non-master track raises `InternalError: "Only the main track has the song tempo!"`.

#### `track_activator`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's on/off toggle (activator) as a `DeviceParameter`. This is the same toggle
controlled by the track's mute state, exposed here for automation and mapping.

#### `volume`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's volume fader as a `DeviceParameter`.

### Properties

| Property           | Type  | Settable | Listenable | Summary                                                   |
| ------------------ | ----- | -------- | ---------- | --------------------------------------------------------- |
| `crossfade_assign` | `int` | `int`    | `yes`      | Crossfade assignment: 0=A, 1=none, 2=B. Raises on master. |
| `panning_mode`     | `int` | `int`    | `yes`      | Panning mode: 0=Stereo, 1=Split Stereo. Settable.         |

#### `crossfade_assign`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The track's crossfade assignment:

- `0` = A (assigned to crossfader side A)
- `1` = none (not crossfade-assigned)
- `2` = B (assigned to crossfader side B)

Accessing on the master track raises
`InternalError: "Main track has no crossfader assignment!"`.

#### `panning_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The track's panning mode:

- `0` = Stereo -- standard single-knob panning
- `1` = Split Stereo -- separate left/right pan controls via `left_split_stereo` and
  `right_split_stereo`

Settable. Setting `panning_mode=1` switches the track to split stereo panning.

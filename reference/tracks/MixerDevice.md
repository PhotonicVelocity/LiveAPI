# MixerDevice

> `Live.MixerDevice.MixerDevice`

This class represents a Mixer Device in Live, which gives you access to the Volume and Panning properties of a Track.

**Live Object:** `yes`

## Properties

| Property             | Type              | Settable | Listenable | Description                                                                  |
| -------------------- | ----------------- | -------- | ---------- | ---------------------------------------------------------------------------- |
| `canonical_parent`   | `Track`           | `no`     | `no`       | Get the canonical parent of the mixer device.                                |
| `crossfade_assign`   | `int`             | `yes`    | `yes`      | Player- and ReturnTracks only: Access to the Track's Crossfade Assign State. |
| `crossfader`         | `DeviceParameter` | `no`     | `no`       | MainTrack only: Const access to the Crossfader.                              |
| `cue_volume`         | `DeviceParameter` | `no`     | `no`       | MainTrack only: Const access to the Cue Volume Parameter.                    |
| `left_split_stereo`  | `DeviceParameter` | `no`     | `no`       | Const access to the Track's Left Split Stereo Panning Device Parameter.      |
| `panning`            | `DeviceParameter` | `no`     | `no`       | Const access to the Tracks Panning Device Parameter.                         |
| `panning_mode`       | `int`             | `yes`    | `yes`      | Access to the Track's Panning Mode.                                          |
| `right_split_stereo` | `DeviceParameter` | `no`     | `no`       | Const access to the Track's Right Split Stereo Panning Device Parameter.     |
| `sends`              | `tuple`           | `no`     | `yes`      | Const access to the Tracks list of Send Amount Device Parameters.            |
| `song_tempo`         | `DeviceParameter` | `no`     | `no`       | MainTrack only: Const access to the Song's Tempo.                            |
| `track_activator`    | `DeviceParameter` | `no`     | `no`       | Const access to the Tracks Activator Device Parameter.                       |
| `volume`             | `DeviceParameter` | `no`     | `no`       | Const access to the Tracks Volume Device Parameter.                          |

### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the mixer device.

### `crossfade_assign`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Player- and ReturnTracks only: Access to the Track's Crossfade Assign State.

### `crossfader`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Crossfader.

### `cue_volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Cue Volume Parameter.

### `left_split_stereo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Track's Left Split Stereo Panning Device Parameter.

### `panning`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Panning Device Parameter.

### `panning_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Track's Panning Mode.

### `right_split_stereo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Track's Right Split Stereo Panning Device Parameter.

### `sends`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the Tracks list of Send Amount Device Parameters.

### `song_tempo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Song's Tempo.

### `track_activator`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Activator Device Parameter.

### `volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Volume Device Parameter.

## Enums

### `crossfade_assignments`

| Value | Name   |
| ----- | ------ |
| `0`   | `A`    |
| `1`   | `NONE` |
| `2`   | `B`    |

### `panning_modes`

| Value | Name           |
| ----- | -------------- |
| `0`   | `stereo`       |
| `1`   | `stereo_split` |

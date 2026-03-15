# MixerDevice (Module)

## MixerDevice (Class)

> `Live.MixerDevice.MixerDevice`

This class represents a Mixer Device in Live, which gives you access to the Volume and Panning properties of a Track.

**Live Object:** `yes`

**Access via:**

- `Track.mixer_device`

### Properties

| Property                                    | Type                      | Supports             |
| ------------------------------------------- | ------------------------- | -------------------- |
| [`canonical_parent`](#canonical_parent)     | `Track`                   | `get`                |
| [`crossfade_assign`](#crossfade_assign)     | `int`                     | `get`/`set`/`listen` |
| [`crossfader`](#crossfader)                 | `DeviceParameter`         | `get`                |
| [`cue_volume`](#cue_volume)                 | `DeviceParameter`         | `get`                |
| [`left_split_stereo`](#left_split_stereo)   | `DeviceParameter`         | `get`                |
| [`panning`](#panning)                       | `DeviceParameter`         | `get`                |
| [`panning_mode`](#panning_mode)             | `int`                     | `get`/`set`/`listen` |
| [`right_split_stereo`](#right_split_stereo) | `DeviceParameter`         | `get`                |
| [`sends`](#sends)                           | `Vector[DeviceParameter]` | `get`/`listen`       |
| [`song_tempo`](#song_tempo)                 | `DeviceParameter`         | `get`                |
| [`track_activator`](#track_activator)       | `DeviceParameter`         | `get`                |
| [`volume`](#volume)                         | `DeviceParameter`         | `get`                |

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the mixer device.

#### `crossfade_assign`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Player- and ReturnTracks only: Access to the Track's Crossfade Assign State.

#### `crossfader`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Crossfader.

#### `cue_volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Cue Volume Parameter.

#### `left_split_stereo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Track's Left Split Stereo Panning Device Parameter.

#### `panning`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Panning Device Parameter.

#### `panning_mode`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the Track's Panning Mode.

#### `right_split_stereo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Track's Right Split Stereo Panning Device Parameter.

#### `sends`

- **Type:** `Vector[DeviceParameter]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the Tracks list of Send Amount Device Parameters.

#### `song_tempo`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

MainTrack only: Const access to the Song's Tempo.

#### `track_activator`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Activator Device Parameter.

#### `volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Tracks Volume Device Parameter.

## Enums

### crossfade_assignments

> `Live.MixerDevice.MixerDevice.crossfade_assignments`

| Value | Name   |
| ----- | ------ |
| `0`   | `A`    |
| `1`   | `NONE` |
| `2`   | `B`    |

### panning_modes

> `Live.MixerDevice.MixerDevice.panning_modes`

| Value | Name           |
| ----- | -------------- |
| `0`   | `stereo`       |
| `1`   | `stereo_split` |

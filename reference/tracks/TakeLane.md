# TakeLane (Module)

## TakeLane (Class)

> `Live.TakeLane.TakeLane`

This class represents a take lane in Live.

**Live Object:** `yes`

### Properties

| Property            | Type    | Supports             |
| ------------------- | ------- | -------------------- |
| `arrangement_clips` | `tuple` | `get`/`listen`       |
| `canonical_parent`  | `Track` | `get`                |
| `name`              | `str`   | `get`/`set`/`listen` |

#### `arrangement_clips`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Read-only access to the arrangement clips in the take lane.

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the take lane.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write access to the name of the TakeLane, as visible in the take lane header.

### Methods

| Method                                                 | Returns | Description                                                                      |
| ------------------------------------------------------ | ------- | -------------------------------------------------------------------------------- |
| `create_audio_clip(file_path: str, start_time: float)` | `Clip`  | Creates an audio clip referencing the file at the given path and inserts it i... |
| `create_midi_clip(start_time: float, length: float)`   | `Clip`  | Creates an empty MIDI clip and inserts it into the arrangement at the specifi... |

#### `create_audio_clip(file_path: str, start_time: float)`

- **Returns:** `Clip`
- **Args:**
  - `file_path: str`
  - `start_time: float`

Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.

#### `create_midi_clip(start_time: float, length: float)`

- **Returns:** `Clip`
- **Args:**
  - `start_time: float`
  - `length: float`

Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.

# TakeLane

> `Live.TakeLane.TakeLane`

This class represents a take lane in Live. Tracks in Arrangement View can have take lanes,
which are used for comping. If take lanes exist for a track, they can be shown by
right-clicking on a track and choosing "Show Take Lanes." Each take lane holds its own
list of arrangement clips and can be used to create new audio or MIDI clips.

### Children

| Child               | Returns          | Shape  | Listenable | Summary                                  |
| ------------------- | ---------------- | ------ | ---------- | ---------------------------------------- |
| `arrangement_clips` | `Sequence[Clip]` | `list` | `yes`      | The arrangement clips in this take lane. |

#### `arrangement_clips`

- **Type:** `Sequence[Clip]`
- **Listenable:** `yes`
- **Since:** `12.2`

The list of arrangement clips contained in this take lane. This is read-only -- clips
cannot be assigned directly, but can be created via `create_audio_clip()` and
`create_midi_clip()`. The listener fires when clips are added or removed from the take
lane.

### Properties

| Property           | Type     | Settable | Listenable | Summary                                     |
| ------------------ | -------- | -------- | ---------- | ------------------------------------------- |
| `canonical_parent` | `object` | no       | `no`       | The parent object that owns this take lane. |
| `name`             | `str`    | yes      | `yes`      | The name shown in the take lane header.     |

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `12.2`

Returns the canonical parent of this take lane. This is expected to be the Track that
contains the take lane.

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `12.2`

The display name of the take lane as shown in the take lane header. Read/write. The
listener fires when the name changes.

### Methods

| Method                                                 | Returns | Summary                                                 |
| ------------------------------------------------------ | ------- | ------------------------------------------------------- |
| `create_audio_clip(file_path: str, start_time: float)` | `Clip`  | Create an audio clip from a file at the given time.     |
| `create_midi_clip(start_time: float, length: float)`   | `Clip`  | Create an empty MIDI clip at the given time and length. |

#### `create_audio_clip(file_path: str, start_time: float)`

- **Returns:** `Clip`
- **Args:**
  - `file_path: str` -- absolute path to a valid audio file in a supported format (on Mac,
    starting with `/Volumes/(drive name)/`)
  - `start_time: float` -- position in beats where the clip should be inserted
- **Raises:** Throws an error if the track is not an audio track, the track is frozen, the track
  is currently being recorded into, `start_time` is outside the range `[0.0, 1576800.0]`, or the
  path does not point to a valid audio file.
- **Since:** `12.2`

Creates an audio clip that references the audio file at the given absolute path and
inserts it into this take lane's arrangement at `start_time` in beats. The file must be
in a format supported by Live. Returns the newly created Clip object.

#### `create_midi_clip(start_time: float, length: float)`

- **Returns:** `Clip`
- **Args:**
  - `start_time: float` -- position in beats where the clip should be inserted
  - `length: float` -- duration of the clip in beats
- **Raises:** Throws an error if the track is not a MIDI track, the track is frozen, the track is
  currently being recorded into, or `start_time` is outside the range `[0.0, 1576800.0]`.
- **Since:** `12.2`

Creates an empty MIDI clip with the specified `length` in beats and inserts it into this
take lane's arrangement at `start_time` in beats. Returns the newly created Clip object.

### Open Questions

- What is the canonical path for a take lane? The Max docs say
  `live_set tracks N take_lanes M` -- does the Python API follow the same structure?
- Can take lanes be created or deleted programmatically, or are they only managed by
  Live's comping workflow?
- Does `create_audio_clip()` return the newly created clip immediately, or is there a
  delay before it appears in `arrangement_clips`?
- What happens if `create_midi_clip()` or `create_audio_clip()` is called with a time
  that overlaps an existing clip in the same take lane?

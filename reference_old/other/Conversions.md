# Conversions

> `Live.Conversions.Conversions`

This module provides static utility functions for converting between audio and MIDI
representations in Live. All functions are class-level static methods -- they operate on
existing objects (clips, tracks, devices) rather than being called on instances.

These functions mirror the audio-to-MIDI conversion workflows available in the Live UI
(right-click an audio clip -> "Convert to MIDI").

??? note "Raw probe notes (temporary)"
    Probed 2026-02-26 on Live 12.3.5 via `call_static` bridge command.

    - **Bridge accessibility**: All functions are importable and callable from the bridge via
      `call_static`.
    - **`AudioToMidiType` enum values**: `0 = Harmony`, `1 = Melody`, `2 = Drums`. Mode 3+ errors
      with `Invalid algorithm.`. Note: the ordering does **not** match the Live UI menu order (which
      shows Drums, Harmony, Melody).
    - **`move_devices_on_track_to_new_drum_rack_pad` return type**: Returns `None` on no-op (no
      devices). Returns a **`DrumPad` handle** when the track has devices. Does **not** create a new
      track -- replaces the device chain in-place with a Drum Rack containing the original devices on
      a pad. `DrumPad` has no `class_name` property.
    - **Undo tracking**: All track-creating operations are undo-tracked (undo description:
      "Custom Action").
    - **Async visibility**: `audio_to_midi_clip` shows a progress dialog and needs ~5s for the
      conversion to complete before the new track is visible. `create_midi_track_with_simpler` and
      `create_drum_rack_from_audio_clip` are synchronous (track visible within 0.5s).
    - **Error behavior**: Invalid mode -> `Invalid algorithm.`. Nonexistent method -> bridge-level
      `ValidationError`. Disallowed module -> `Module not allowed` (security allowlist working).
    - **Silent clip behavior**: `audio_to_midi_clip` on a silent audio clip still creates a new MIDI
      track (with empty MIDI) for all 3 modes, but requires the 5s progress dialog wait.
      `is_convertible_to_midi` returns `True` for silent clips.
    - **Track insertion**: `create_midi_track_with_simpler` inserts the new track immediately after
      the source audio track. `create_drum_rack_from_audio_clip` appends the new track at the end.
      `audio_to_midi_clip` inserts after the source audio track.
    - **`create_midi_track_from_drum_pad`**: Creates 1 new MIDI track with an `OriginalSimpler` device
      (bridge type `SimplerDevice`). Returns `None`. Sync (~0.5s). Undo-tracked.
    - **`sliced_simpler_to_drum_rack`**: Replaces the Simpler **in-place** with a `DrumGroupDevice`
      (bridge type `RackDevice`). Does **not** create a new track -- the device swap happens on the
      existing track. Returns `None`. Sync. **Requires `async_wait()` after setting
      `playback_mode=2`** -- the property readback confirms 2 immediately, but Live's internal slice
      initialization runs asynchronously. Calling the conversion before it finishes crashes Live.

### Open Questions

None -- all 7 functions fully probed.

### Methods

| Method                                                          | Returns            | Summary                                                        |
| --------------------------------------------------------------- | ------------------ | -------------------------------------------------------------- |
| `audio_to_midi_clip(song, audio_clip, audio_to_midi_type)`      | `None`             | Convert an audio clip to MIDI in a new track.                  |
| `create_drum_rack_from_audio_clip(song, audio_clip)`            | `None`             | Create a new track with a Drum Rack containing the audio clip. |
| `create_midi_track_from_drum_pad(song, drum_pad)`               | `None`             | Extract a drum pad's device chain into a new MIDI track.       |
| `create_midi_track_with_simpler(song, audio_clip)`              | `None`             | Create a new MIDI track with a Simpler containing the clip.    |
| `is_convertible_to_midi(song, audio_clip)`                      | `bool`             | Check if an audio clip can be converted to MIDI.               |
| `move_devices_on_track_to_new_drum_rack_pad(song, track_index)` | `DrumPad` / `None` | Wrap a track's devices in a Drum Rack in-place.                |
| `sliced_simpler_to_drum_rack(song, simpler)`                    | `None`             | Convert a sliced Simpler into a Drum Rack.                     |

#### `audio_to_midi_clip(song: Song, audio_clip: Clip, audio_to_midi_type: int)`

- **Returns:** `None`
- **Args:**
    - `song: Song` -- the current song
    - `audio_clip: Clip` -- the audio clip to convert
    - `audio_to_midi_type: int` -- conversion algorithm (`AudioToMidiType` enum)
- **Raises:** `Invalid algorithm.` if `audio_to_midi_type` is not 0, 1, or 2.
- **Since:** `<11`

Converts an audio clip to MIDI using the specified algorithm, creating a new MIDI track with the
resulting MIDI clip. The `audio_to_midi_type` values are: `0 = Harmony`, `1 = Melody`, `2 = Drums`.
On silent audio clips, the conversion still creates a track (with empty MIDI content). The new track is
inserted immediately after the source audio track.

- **Quirks:** Shows a progress dialog and needs ~5s for conversion to complete before the new track is
  visible.

#### `create_drum_rack_from_audio_clip(song: Song, audio_clip: Clip)`

- **Returns:** `None`
- **Args:**
    - `song: Song` -- the current song
    - `audio_clip: Clip` -- the audio clip to use
- **Since:** `<11`

Creates a new track containing a Drum Rack (`DrumGroupDevice`, bridge type `RackDevice`) with a Simpler
device on the first pad, loaded with the specified audio clip. The new track is appended at the end of the
track list. Track name follows the pattern `{index}-Drum Rack`.

#### `create_midi_track_from_drum_pad(song: Song, drum_pad: DrumPad)`

- **Returns:** `None`
- **Args:**
    - `song: Song` -- the current song
    - `drum_pad: DrumPad` -- the drum pad whose device chain to extract
- **Since:** `<11`

Extracts the device chain from the specified Drum Rack pad and places it into a new MIDI track. The
new track contains the device(s) from the pad (e.g. an `OriginalSimpler` loaded with the pad's sample).
Returns `None`.

#### `create_midi_track_with_simpler(song: Song, audio_clip: Clip)`

- **Returns:** `None`
- **Args:**
    - `song: Song` -- the current song
    - `audio_clip: Clip` -- the audio clip to load into Simpler
- **Since:** `<11`

Creates a new MIDI track containing a Simpler instrument (`OriginalSimpler`) loaded with the specified
audio clip. The new track is inserted immediately after the source audio track. Track name follows the
pattern `{index}-{clip_name}`.

#### `is_convertible_to_midi(song: Song, audio_clip: Clip)`

- **Returns:** `bool`
- **Args:**
    - `song: Song` -- the current song
    - `audio_clip: Clip` -- the clip to check
- **Raises:** Error if called with a MIDI clip (not an audio clip).
- **Since:** `<11`

Returns `True` if the given audio clip can be converted to MIDI. Returns `True` even for silent audio
clips. Raises an error if called with a MIDI clip.

#### `move_devices_on_track_to_new_drum_rack_pad(song: Song, track_index: int)`

- **Returns:** `DrumPad` handle when the track has devices; `None` on no-op (no devices). Stub says
  `LomObject`.
- **Args:**
    - `song: Song` -- the current song
    - `track_index: int` -- index of the track whose devices to move
- **Since:** `<11`

Takes all devices from the track at `track_index` and wraps them in a Drum Rack on the C1 (MIDI note 36)
pad. The replacement happens **in-place** on the source track -- no new track is created. Returns a
`DrumPad` handle pointing to the pad that received the devices. `DrumPad` has no `class_name` property.
If the source track has no devices, nothing happens (returns `None`).

#### `sliced_simpler_to_drum_rack(song: Song, simpler: SimplerDevice)`

- **Returns:** `None`
- **Args:**
    - `song: Song` -- the current song
    - `simpler: SimplerDevice` -- the sliced Simpler device to convert
- **Raises:** Error if the Simpler is not in sliced mode.
- **Since:** `<11`

Converts a Simpler device in slice mode (`playback_mode=2`) into a Drum Rack, assigning each slice to
its own drum pad with a Simpler. The replacement happens **in-place** -- the Simpler on the track is
replaced by a `DrumGroupDevice`. No new track is created. Raises an error if the Simpler is not currently
in sliced playback mode.

- **Quirks:** After setting `playback_mode=2`, the property readback confirms `2` immediately, but Live's
  internal slice analysis runs asynchronously. An `async_wait()` (or equivalent delay) is required before
  calling this function -- invoking it while the slice initialization is still in flight crashes Live.

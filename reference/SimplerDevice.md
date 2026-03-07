# SimplerDevice

## SimplerDevice

This class represents an instance of Simpler in Live. A SimplerDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for sample playback, warping, slicing, and voice management.

Simpler has three playback modes: Classic, One-Shot, and Slicing. The available properties
and methods vary depending on the active mode.

### Sources

- **Primary:** `Live/classes/devices/SimplerDevice.py` (stub dump)
- **Secondary:** `MaxForLive/simplerdevice.md`, `MaxForLive/simplerdevice_view.md`
- **Probes:** 2026-02-25 (Live 12.3.5)

### Probe Notes

- **Bridge type:** `"SimplerDevice"`.
- **`class_name`:** `"OriginalSimpler"`. **`class_display_name`:** `"Simpler"`.
- **`type`:** 1 (`INSTRUMENT`).
- **Insert name:** `"Simpler"` (matches `class_display_name`).
- **7 settable properties** round-trip confirmed: `note_pitch_bend_range` (default 48),
  `pad_slicing` (default False), `pitch_bend_range` (default 5), `playback_mode` (default 0,
  range 0–2), `retrigger` (default True), `slicing_playback_mode` (default 0, range 0–2),
  `voices` (default 6, valid: 1,2,3,4,6,8,12,16,24,32).
- **6 read-only properties:** `can_warp_as` (False), `can_warp_double` (False), `can_warp_half`
  (False), `multi_sample_mode` (False), `playing_position` (0.0), `playing_position_enabled`
  (False). All return defaults when no sample is loaded.
- **All 13 properties are listenable.**
- **`sample` child:** Returns `None` when no sample is loaded (confirmed — does not throw).
- **All 6 methods** raise `InternalError` when no sample is loaded. This is expected — they
  require an active sample.
- **`playback_mode`:** 0=Classic, 1=One-Shot, 2=Slicing. Plain `int`, not an enum.
- **`slicing_playback_mode`:** 0=Mono, 1=Poly, 2=Thru. Plain `int`, not an enum.
- **`voices`:** Valid values are 1,2,3,4,6,8,12,16,24,32 (not arbitrary). Invalid values throw.
- **View:** 8 read-only listenable `int` properties. All return `-1` when no sample is loaded.
  `selected_slice` throws `AttributeError` when no sample is loaded and Simpler is not in
  Slicing mode.

### Children

In addition to Device children (`parameters`, `view`), SimplerDevice adds:

| Child    | Returns  | Shape    | Access | Listenable | Available Since | Summary                                 |
| -------- | -------- | -------- | ------ | ---------- | --------------- | --------------------------------------- |
| `sample` | `Sample` | `single` | `get`  | `yes`      | `<11`           | The sample currently loaded in Simpler. |

#### `sample`

- **Returns:** `Sample` or `None`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The sample currently loaded into Simpler. The listener fires when a new sample is loaded
or the sample is replaced. Returns `None` if no sample is loaded.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), SimplerDevice adds:

| Property                   | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                     |
| -------------------------- | ----------- | ----------- | ---------- | --------------- | ----------------------------------------------------------- |
| `can_warp_as`              | `bool`      | —           | `yes`      | `<11`           | Whether `warp_as` is currently available.                   |
| `can_warp_double`          | `bool`      | —           | `yes`      | `<11`           | Whether `warp_double` is currently available.               |
| `can_warp_half`            | `bool`      | —           | `yes`      | `<11`           | Whether `warp_half` is currently available.                 |
| `multi_sample_mode`        | `bool`      | —           | `yes`      | `<11`           | Whether Simpler is in multi-sample mode.                    |
| `note_pitch_bend_range`    | `int`       | `int`       | `yes`      | `11.3`          | The per-note pitch bend range in semitones. Default 48.     |
| `pad_slicing`              | `bool`      | `bool`      | `yes`      | `<11`           | Whether slices can be added by playing unassigned notes.    |
| `pitch_bend_range`         | `int`       | `int`       | `yes`      | `11.3`          | The global pitch bend range in semitones. Default 5.        |
| `playback_mode`            | `int`       | `int`       | `yes`      | `<11`           | 0=Classic, 1=One-Shot, 2=Slicing. Default 0.                |
| `playing_position`         | `float`     | —           | `yes`      | `<11`           | Normalized playback position between start and end markers. |
| `playing_position_enabled` | `bool`      | —           | `yes`      | `<11`           | Whether Simpler is currently playing back the sample.       |
| `retrigger`                | `bool`      | `bool`      | `yes`      | `<11`           | Whether retrigger mode is enabled. Default True.            |
| `slicing_playback_mode`    | `int`       | `int`       | `yes`      | `<11`           | 0=Mono, 1=Poly, 2=Thru. Default 0.                          |
| `voices`                   | `int`       | `int`       | `yes`      | `<11`           | Polyphony voice count. Valid: 1,2,3,4,6,8,12,16,24,32.      |

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
SimplerDevice adds:

| Signature                   | Returns | Available Since | Summary                                                      |
| --------------------------- | ------- | --------------- | ------------------------------------------------------------ |
| `crop()`                    | `None`  | `<11`           | Crop the sample to the region between start and end markers. |
| `guess_playback_length()`   | `float` | `<11`           | Estimate the playback length in beats between the markers.   |
| `reverse()`                 | `None`  | `<11`           | Reverse the loaded sample.                                   |
| `warp_as(beat_time: float)` | `None`  | `<11`           | Warp the active region to fit the given beat length.         |
| `warp_double()`             | `None`  | `<11`           | Double the playback tempo of the active region.              |
| `warp_half()`               | `None`  | `<11`           | Halve the playback tempo of the active region.               |

All methods raise `InternalError` when no sample is loaded.

---

## SimplerDevice.View

Represents the view aspects of a Simpler device. Extends Device.View with sample display
properties for visualizing the waveform, loop region, and slices.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property              | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                      |
| --------------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------------------------------------ |
| `sample_end`          | `int`       | —           | `yes`      | `<11`           | Modulated sample end position in samples. -1 if no sample.   |
| `sample_env_fade_in`  | `int`       | —           | `yes`      | `<11`           | Envelope fade-in time in samples. -1 if no sample.           |
| `sample_env_fade_out` | `int`       | —           | `yes`      | `<11`           | Envelope fade-out time in samples. -1 if no sample.          |
| `sample_loop_end`     | `int`       | —           | `yes`      | `<11`           | Modulated loop end position in samples. -1 if no sample.     |
| `sample_loop_fade`    | `int`       | —           | `yes`      | `<11`           | Modulated loop crossfade length in samples. -1 if no sample. |
| `sample_loop_start`   | `int`       | —           | `yes`      | `<11`           | Modulated loop start position in samples. -1 if no sample.   |
| `sample_start`        | `int`       | —           | `yes`      | `<11`           | Modulated sample start position in samples. -1 if no sample. |
| `selected_slice`      | `int`       | —           | `yes`      | `<11`           | Currently selected slice time. Errors if no sample.          |

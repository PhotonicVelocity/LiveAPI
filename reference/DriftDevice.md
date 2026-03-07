# DriftDevice

## DriftDevice

This class represents a Drift synthesizer device in Live. DriftDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for accessing the modulation matrix, voice settings, and pitch bend range.

Drift's modulation matrix is exposed through a set of index/list property pairs. Each
pair lets you read or change which modulation source or target is selected in a given
slot. The `*_list` properties return the available option names; the `*_index` properties
return or set the currently selected index into that list.

### Sources

- **Primary:** `Live/classes/devices/DriftDevice.py` (stub dump)
- **Secondary:** `MaxForLive/driftdevice.md`
- **Probes:** `.tmp/probe_device_subclasses_moderate.py`, `.tmp/probe_drift_pbr.py`

### Probe Notes

- Bridge type name: `"DriftDevice"`.
- `class_name` = `"Drift"`, `class_display_name` = `"Drift"` (names match).
- Device type = 1 (Instrument).
- All `*_index` properties are **settable** (get+set+listen) — confirmed by probe.
- All `*_list` properties serialize as plain `list[str]` through the bridge (StringVector → list).
- `pitch_bend_range` valid range: 0–12. Setting 13+ throws `"Invalid Pitch Bend Range"`. Settable within range.
- `voice_count_list` = `['4', '8', '16', '24', '32']` (5 entries).
- `voice_mode_list` = `['Poly', 'Mono', 'Stereo', 'Unison']` (4 entries).
- All mod matrix source lists share the same 8 entries: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod',
'Press', 'Slide']`.
- Target lists have 12 entries: `['None', 'Osc 1 Gain', 'Osc 1 Shape', 'Osc 2 Gain', 'Osc 2 Detune',
'Noise Gain', 'LP Frequency', 'LP Resonance', 'HP Frequency', 'LFO Rate', 'Cyc Env Rate', 'Main Volume']`.
- Default `voice_count_index` = 4 (= 32 voices), `voice_mode_index` = 0 (Poly), `pitch_bend_range` = 2.
- Default mod matrix index values: filter_source_1=1, filter_source_2=6, lfo_source=5,
  pitch_source_1=1, pitch_source_2=2, shape_source=7, source_1=5, source_2=4, source_3=6,
  target_1=8, target_2=0, target_3=0.

### Open Questions

None — all questions resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
DriftDevice adds:

| Property                           | Get Returns    | Set Accepts | Listenable | Available Since | Summary                                                 |
| ---------------------------------- | -------------- | ----------- | ---------- | --------------- | ------------------------------------------------------- |
| `mod_matrix_filter_source_1_index` | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for filter frequency mod slot 1.  |
| `mod_matrix_filter_source_1_list`  | `StringVector` | —           | `no`       | `11.3`          | Available source names for filter frequency mod slot 1. |
| `mod_matrix_filter_source_2_index` | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for filter frequency mod slot 2.  |
| `mod_matrix_filter_source_2_list`  | `StringVector` | —           | `no`       | `11.3`          | Available source names for filter frequency mod slot 2. |
| `mod_matrix_lfo_source_index`      | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for LFO amount modulation.        |
| `mod_matrix_lfo_source_list`       | `StringVector` | —           | `no`       | `11.3`          | Available source names for LFO amount modulation.       |
| `mod_matrix_pitch_source_1_index`  | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for pitch mod slot 1.             |
| `mod_matrix_pitch_source_1_list`   | `StringVector` | —           | `no`       | `11.3`          | Available source names for pitch mod slot 1.            |
| `mod_matrix_pitch_source_2_index`  | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for pitch mod slot 2.             |
| `mod_matrix_pitch_source_2_list`   | `StringVector` | —           | `no`       | `11.3`          | Available source names for pitch mod slot 2.            |
| `mod_matrix_shape_source_index`    | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for shape modulation.             |
| `mod_matrix_shape_source_list`     | `StringVector` | —           | `no`       | `11.3`          | Available source names for shape modulation.            |
| `mod_matrix_source_1_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for custom mod slot 1.            |
| `mod_matrix_source_1_list`         | `StringVector` | —           | `no`       | `11.3`          | Available source names for custom mod slot 1.           |
| `mod_matrix_source_2_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for custom mod slot 2.            |
| `mod_matrix_source_2_list`         | `StringVector` | —           | `no`       | `11.3`          | Available source names for custom mod slot 2.           |
| `mod_matrix_source_3_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected source index for custom mod slot 3.            |
| `mod_matrix_source_3_list`         | `StringVector` | —           | `no`       | `11.3`          | Available source names for custom mod slot 3.           |
| `mod_matrix_target_1_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected target index for custom mod slot 1.            |
| `mod_matrix_target_1_list`         | `StringVector` | —           | `no`       | `11.3`          | Available target names for custom mod slot 1.           |
| `mod_matrix_target_2_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected target index for custom mod slot 2.            |
| `mod_matrix_target_2_list`         | `StringVector` | —           | `no`       | `11.3`          | Available target names for custom mod slot 2.           |
| `mod_matrix_target_3_index`        | `int`          | `int`       | `yes`      | `11.3`          | Selected target index for custom mod slot 3.            |
| `mod_matrix_target_3_list`         | `StringVector` | —           | `no`       | `11.3`          | Available target names for custom mod slot 3.           |
| `pitch_bend_range`                 | `int`          | `int`       | `yes`      | `11.3`          | MIDI pitch bend range in semitones (0–12). Settable.    |
| `voice_count_index`                | `int`          | `int`       | `yes`      | `11.3`          | Index of the selected voice count setting.              |
| `voice_count_list`                 | `StringVector` | —           | `no`       | `11.3`          | Available voice count setting names.                    |
| `voice_mode_index`                 | `int`          | `int`       | `yes`      | `11.3`          | Index of the selected voice mode.                       |
| `voice_mode_list`                  | `StringVector` | —           | `no`       | `11.3`          | Available voice mode names.                             |

#### `mod_matrix_filter_source_1_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_filter_source_1_list` for the currently selected modulation
source in filter frequency mod slot 1. Default: 1 (Env 2). Settable.

#### `mod_matrix_filter_source_1_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for filter frequency mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_filter_source_2_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_filter_source_2_list` for the currently selected modulation
source in filter frequency mod slot 2. Default: 6 (Press). Settable.

#### `mod_matrix_filter_source_2_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for filter frequency mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_lfo_source_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_lfo_source_list` for the currently selected modulation source
for the LFO amount. Default: 5 (Mod). Settable.

#### `mod_matrix_lfo_source_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for the LFO amount.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_pitch_source_1_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_pitch_source_1_list` for the currently selected modulation
source in pitch mod slot 1. Default: 1 (Env 2). Settable.

#### `mod_matrix_pitch_source_1_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for pitch mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_pitch_source_2_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_pitch_source_2_list` for the currently selected modulation
source in pitch mod slot 2. Default: 2 (LFO). Settable.

#### `mod_matrix_pitch_source_2_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for pitch mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_shape_source_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_shape_source_list` for the currently selected modulation
source for shape. Default: 7 (Slide). Settable.

#### `mod_matrix_shape_source_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for shape.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_1_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_source_1_list` for the currently selected source in custom
mod slot 1. Default: 5 (Mod). Settable — confirmed by probe.

#### `mod_matrix_source_1_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for custom mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_2_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_source_2_list` for the currently selected source in custom
mod slot 2. Default: 4 (Vel). Settable.

#### `mod_matrix_source_2_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for custom mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_3_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_source_3_list` for the currently selected source in custom
mod slot 3. Default: 6 (Press). Settable.

#### `mod_matrix_source_3_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation source names for custom mod slot 3.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_target_1_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_target_1_list` for the currently selected target in custom
mod slot 1. Default: 8 (HP Frequency). Settable — confirmed by probe.

#### `mod_matrix_target_1_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation target names for custom mod slot 1.
Values: `['None', 'Osc 1 Gain', 'Osc 1 Shape', 'Osc 2 Gain', 'Osc 2 Detune',
'Noise Gain', 'LP Frequency', 'LP Resonance', 'HP Frequency', 'LFO Rate',
'Cyc Env Rate', 'Main Volume']`.

#### `mod_matrix_target_2_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_target_2_list` for the currently selected target in custom
mod slot 2. Default: 0 (None). Settable.

#### `mod_matrix_target_2_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation target names for custom mod slot 2.
Values: same as `mod_matrix_target_1_list`.

#### `mod_matrix_target_3_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `mod_matrix_target_3_list` for the currently selected target in custom
mod slot 3. Default: 0 (None). Settable.

#### `mod_matrix_target_3_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available modulation target names for custom mod slot 3.
Values: same as `mod_matrix_target_1_list`.

#### `pitch_bend_range`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The MIDI pitch bend range in semitones. Valid range: 0–12. Setting values >= 13 throws
`"Invalid Pitch Bend Range"`. Default: 2. Settable within valid range.

#### `voice_count_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `voice_count_list` for the currently selected voice count setting.
Default: 4 (= 32 voices). Settable — confirmed by probe.

#### `voice_count_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available voice count setting names.
Values: `['4', '8', '16', '24', '32']`.

#### `voice_mode_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index into `voice_mode_list` for the currently selected voice mode.
Default: 0 (Poly). Settable — confirmed by probe.

#### `voice_mode_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available voice mode names.
Values: `['Poly', 'Mono', 'Stereo', 'Unison']`.

# HybridReverbDevice

## HybridReverbDevice

This class represents a Hybrid Reverb device in Live. HybridReverbDevice is a subclass
of Device -- it has all the children, properties, and methods of Device plus additional
members for managing the convolution impulse response (IR) selection and time-shaping
parameters.

Hybrid Reverb combines a convolution engine with an algorithmic reverb. The API exposes
properties for browsing and selecting IR files by category, adjusting the IR envelope
(attack, decay, size), and toggling time-shaping.

### Sources

- **Primary:** `Live/classes/devices/HybridReverbDevice.py` (stub dump)
- **Secondary:** `MaxForLive/hybridreverbdevice.md`
- **Probes:** `.tmp/probe_device_subclasses_moderate.py`

### Probe Notes

- Bridge type name: `"HybridReverbDevice"`.
- `class_name` = `"Hybrid"`, `class_display_name` = `"Hybrid Reverb"`.
- Device type = 2 (Audio Effect).
- All 8 properties are **settable** (get+set+listen), contrary to earlier docs that showed "—" for Set.
- `ir_category_list` and `ir_file_list` serialize as plain `list[str]` through the bridge (StringVector → list).
- Changing `ir_category_index` dynamically updates `ir_file_list` (confirmed — file list changed after category switch).
- `ir_file_list` is listenable and fires when the category changes.
- Float precision: `ir_decay_time` shows float32 artifacts (e.g. set 0.3 → readback 0.30000001192092896).
- `ir_category_list` default = `['Early_Reflections', 'Real_Places', 'Chambers_and_Large_Rooms', 'Made_for_Drums',
'Halls', 'Plates', 'Springs', 'Bigger_Spaces', 'Textures', 'User']` (10 categories).

### Open Questions

None — all questions resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
HybridReverbDevice adds:

| Property             | Get Returns    | Set Accepts | Listenable | Available Since | Summary                                                      |
| -------------------- | -------------- | ----------- | ---------- | --------------- | ------------------------------------------------------------ |
| `ir_attack_time`     | `float`        | `float`     | `yes`      | `<11`           | Attack time of the IR amplitude envelope, in seconds.        |
| `ir_category_index`  | `int`          | `int`       | `yes`      | `<11`           | Index of the selected IR category.                           |
| `ir_category_list`   | `StringVector` | —           | `no`       | `<11`           | List of available IR category names.                         |
| `ir_decay_time`      | `float`        | `float`     | `yes`      | `<11`           | Decay time of the IR amplitude envelope, in seconds.         |
| `ir_file_index`      | `int`          | `int`       | `yes`      | `<11`           | Index of the selected IR file within the current category.   |
| `ir_file_list`       | `StringVector` | —           | `yes`      | `<11`           | List of IR file names in the selected category.              |
| `ir_size_factor`     | `float`        | `float`     | `yes`      | `<11`           | Relative size of the IR, 0.0 to 1.0.                         |
| `ir_time_shaping_on` | `bool`         | `bool`      | `yes`      | `<11`           | Whether time-shaping (envelope + size) is applied to the IR. |

#### `ir_attack_time`

- **Get Returns:** `float`
- **Set Accepts:** `float`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The attack time of the amplitude envelope applied to the impulse response, in seconds.
Default: 0.0. Settable.

#### `ir_category_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index of the currently selected impulse response category. Changing this value
selects a different category and updates `ir_file_list` accordingly. Default: 0.
Settable — confirmed by probe.

#### `ir_category_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of available impulse response category names. Read-only.
Default: `['Early_Reflections', 'Real_Places', 'Chambers_and_Large_Rooms', 'Made_for_Drums',
'Halls', 'Plates', 'Springs', 'Bigger_Spaces', 'Textures', 'User']` (10 categories).

#### `ir_decay_time`

- **Get Returns:** `float`
- **Set Accepts:** `float`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The decay time of the amplitude envelope applied to the impulse response, in seconds.
Default: 20.0. Settable. Note: float32 precision artifacts may appear in readback.

#### `ir_file_index`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The index of the currently selected impulse response file within the current category.
Default: 0. Settable — confirmed by probe.

#### `ir_file_list`

- **Get Returns:** `StringVector` (serializes as `list[str]`)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The list of impulse response file names available in the currently selected category.
The listener fires when the category changes, causing the file list to update.
Read-only — the list updates automatically when `ir_category_index` changes.

#### `ir_size_factor`

- **Get Returns:** `float`
- **Set Accepts:** `float`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
The relative size of the impulse response, ranging from 0.0 to 1.0. Only effective when
`ir_time_shaping_on` is enabled. Default: 1.0. Settable.

#### `ir_time_shaping_on`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed`

**Description:**
When enabled (`True`), the selected impulse response is transformed by the amplitude
envelope (attack/decay) and size parameter. When disabled, the raw IR is used.
Default: True. Settable — confirmed by probe.

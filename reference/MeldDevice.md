# MeldDevice

## MeldDevice

This class represents a Meld synthesizer device in Live. MeldDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for selecting the oscillator engine, polyphony mode, voice count, and unison
settings.

### Sources

- **Primary:** `Live/classes/devices/MeldDevice.py` (stub dump)
- **Secondary:** `MaxForLive/melddevice.md`
- **Probes:** `tools/probes/probe_device_subclasses_trivial.py`

### Probe Notes

- Bridge type: `"MeldDevice"`. `class_name`: `"InstrumentMeld"`.
- `selected_engine` returns `bool` through the bridge (not `int`), despite conceptually being
  a 0/1 selector. Setting `1` reads back as `True`, setting `0`/`False` reads back as `False`.
- `mono_poly` returns `int`. Default is 1 (Poly). Settable, round-trips correctly.
- `poly_voices` returns `int`. Default is 5. Settable (set to 2, read back 2), round-trips.
- `unison_voices` returns `int`. Default is 0 (Off). Settable (set to 2, read back 2), round-trips.
- All four properties are listenable and settable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
MeldDevice adds:

| Property          | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                          |
| ----------------- | ----------- | ----------- | ---------- | --------------- | ---------------------------------------------------------------- |
| `mono_poly`       | `int`       | `int`       | `yes`      | `12.0`          | Polyphony mode: 0 = Mono, 1 = Poly.                              |
| `poly_voices`     | `int`       | `int`       | `yes`      | `12.0`          | Polyphony voice count index (0-based).                           |
| `selected_engine` | `bool`      | `bool`      | `yes`      | `12.0`          | Oscillator engine selector: False = Engine A, True = Engine B.   |
| `unison_voices`   | `int`       | `int`       | `yes`      | `12.0`          | Unison voice count index: 0 = Off, 1 = Two, 2 = Three, 3 = Four. |

#### `mono_poly`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Selects the polyphony mode. Values: 0 = Mono, 1 = Poly.

#### `poly_voices`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Selects the polyphony voice count. The index maps to voice counts as follows:
0 = 2, 1 = 3, 2 = 4, 3 = 5, 4 = 6, 5 = 8, 6 = 12.

#### `selected_engine`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Selects which oscillator engine is active. Values: `False` = Engine A, `True` = Engine B.

Note: Despite conceptually being a 0/1 index, the bridge serializes this as `bool`.

#### `unison_voices`

- **Get Returns:** `int`
- **Set Accepts:** `int`
- **Listenable:** `yes`
- **Available Since:** `12.0`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Selects the unison voice count. Values: 0 = Off, 1 = Two, 2 = Three, 3 = Four.

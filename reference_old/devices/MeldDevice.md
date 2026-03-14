# MeldDevice

> `Live.MeldDevice.MeldDevice`

This class represents a Meld synthesizer device in Live. MeldDevice is a subclass of Device -- it has all the
children, properties, and methods of Device plus additional members for selecting the oscillator engine,
polyphony mode, voice count, and unison settings.

??? note "Raw probe notes (temporary)"
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

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), MeldDevice adds:

| Property          | Type   | Settable | Listenable | Summary                                                           |
| ----------------- | ------ | -------- | ---------- | ----------------------------------------------------------------- |
| `mono_poly`       | `int`  | yes      | yes        | Polyphony mode: 0 = Mono, 1 = Poly.                              |
| `poly_voices`     | `int`  | yes      | yes        | Polyphony voice count index (0-based).                            |
| `selected_engine` | `bool` | yes      | yes        | Oscillator engine selector: False = Engine A, True = Engine B.    |
| `unison_voices`   | `int`  | yes      | yes        | Unison voice count index: 0 = Off, 1 = Two, 2 = Three, 3 = Four. |

#### `mono_poly`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the polyphony mode. Values: 0 = Mono, 1 = Poly.

#### `poly_voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the polyphony voice count. The index maps to voice counts as follows:
0 = 2, 1 = 3, 2 = 4, 3 = 5, 4 = 6, 5 = 8, 6 = 12.

#### `selected_engine`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects which oscillator engine is active. Values: `False` = Engine A, `True` = Engine B.

**Quirks:**

- Despite conceptually being a 0/1 index, the bridge serializes this as `bool`.

#### `unison_voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the unison voice count. Values: 0 = Off, 1 = Two, 2 = Three, 3 = Four.

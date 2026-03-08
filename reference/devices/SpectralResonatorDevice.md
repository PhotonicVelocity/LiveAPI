# SpectralResonatorDevice

> `Live.SpectralResonatorDevice.SpectralResonatorDevice`

This class represents a Spectral Resonator device in Live. SpectralResonatorDevice is a
subclass of Device -- it has all the children, properties, and methods of Device plus
additional members for controlling frequency dial mode, MIDI gate, modulation mode,
mono/poly mode, pitch mode, pitch bend range, and polyphony voice count.

Spectral Resonator is a spectral audio effect that tunes incoming audio to pitched
resonances. It can be driven by MIDI for pitch control.

??? note "Raw probe notes (temporary)"
    - Bridge type name: `"SpectralResonatorDevice"`.
    - `class_name` = `"Transmute"` (shares implementation base with Spectral Time -- the stub uses
      `TTransmuteDevicePyHandle`).
    - `class_display_name` = `"Spectral Resonator"`.
    - Device type = 2 (Audio Effect).
    - All 7 index properties are **settable** (get+set+listen).
    - All 5 `*_list` properties serialize as plain `list[str]` through the bridge
      (StringVector -> list).
    - The `*_list` properties are marked listenable in the stub but appear static in practice.
    - `pitch_bend_range` valid range: 0-24 (clamped; setting 48 -> readback 24). Settable.
    - `frequency_dial_mode_list` = `['ModulationHertz', 'ModulationBeat8th']` (internal names,
      not UI labels).
    - `midi_gate_list` = `['Off', 'On']`.
    - `mod_mode_list` = `['None', 'Chorus', 'Wander', 'Granular']`.
    - `mono_poly_list` = `['Mono', 'Poly']`.
    - `pitch_mode_list` = `['Internal', 'MIDI']`.
    - Default values: `frequency_dial_mode` = 0, `midi_gate` = 0, `mod_mode` = 0, `mono_poly` = 0,
      `pitch_mode` = 0, `polyphony` = 2, `pitch_bend_range` = 2.

### Open Questions

None -- all questions resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
SpectralResonatorDevice adds:

| Property                   | Type           | Settable | Listenable | Summary                                                          |
| -------------------------- | -------------- | -------- | ---------- | ---------------------------------------------------------------- |
| `frequency_dial_mode`      | `int`          | `int`    | `yes`      | Freq dial mode: 0 = Hertz, 1 = MIDI note.                        |
| `frequency_dial_mode_list` | `list[str]`    | no       | `yes`      | List of available frequency dial mode names.                     |
| `midi_gate`                | `int`          | `int`    | `yes`      | MIDI gate switch: 0 = Off, 1 = On.                               |
| `midi_gate_list`           | `list[str]`    | no       | `yes`      | List of available MIDI gate options.                             |
| `mod_mode`                 | `int`          | `int`    | `yes`      | Modulation mode: 0 = None, 1 = Chorus, 2 = Wander, 3 = Granular. |
| `mod_mode_list`            | `list[str]`    | no       | `yes`      | List of available modulation mode names.                         |
| `mono_poly`                | `int`          | `int`    | `yes`      | Mono/Poly switch: 0 = Mono, 1 = Poly.                            |
| `mono_poly_list`           | `list[str]`    | no       | `yes`      | List of available mono/poly options.                             |
| `pitch_bend_range`         | `int`          | `int`    | `yes`      | Pitch bend range in semitones (0-24). Settable.                  |
| `pitch_mode`               | `int`          | `int`    | `yes`      | Pitch mode: 0 = Internal, 1 = MIDI.                              |
| `pitch_mode_list`          | `list[str]`    | no       | `yes`      | List of available pitch mode names.                              |
| `polyphony`                | `int`          | `int`    | `yes`      | Polyphony voice count index.                                     |

#### `frequency_dial_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mode of the frequency dial control. Values: 0 = Hertz, 1 = MIDI note values.
Default: 0. Settable -- confirmed by probe.

#### `frequency_dial_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available frequency dial mode names. The stub includes a listener for this
property, suggesting the list can change dynamically.
Values: `['ModulationHertz', 'ModulationBeat8th']` (internal names).

#### `midi_gate`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The state of the MIDI gate switch. Values: 0 = Off, 1 = On.
Default: 0. Settable -- confirmed by probe.

#### `midi_gate_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available MIDI gate options. Values: `['Off', 'On']`.

#### `mod_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The modulation mode. Values: 0 = None, 1 = Chorus, 2 = Wander, 3 = Granular.
Default: 0. Settable -- confirmed by probe.

#### `mod_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available modulation mode names. Values: `['None', 'Chorus', 'Wander', 'Granular']`.

#### `mono_poly`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mono/poly switch state. Values: 0 = Mono, 1 = Poly.
Default: 0. Settable -- confirmed by probe.

#### `mono_poly_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available mono/poly option names. Values: `['Mono', 'Poly']`.

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The pitch bend range in semitones. Valid range: 0-24 (values above 24 are clamped).
Default: 2. Settable -- confirmed by probe.

#### `pitch_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The pitch mode. Values: 0 = Internal, 1 = MIDI.
Default: 0. Settable -- confirmed by probe.

#### `pitch_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available pitch mode names. Values: `['Internal', 'MIDI']`.

#### `polyphony`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The polyphony voice count index. Maps to voice counts as follows:
0 = 2, 1 = 4, 2 = 8, 3 = 16 voices.
Default: 2 (= 8 voices). Settable -- confirmed by probe.

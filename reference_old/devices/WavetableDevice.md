# WavetableDevice

> `Live.WavetableDevice.WavetableDevice`

This class represents a Wavetable synthesizer device in Live. WavetableDevice is a subclass of Device -- it
has all the children, properties, and methods of Device plus additional members for controlling the
oscillators, filter routing, voice settings, unison mode, and the modulation matrix.

Wavetable's modulation matrix is exposed through a set of methods that let you add parameters to the matrix,
query modulation amounts, and set modulation amounts by target and source index. The
`visible_modulation_target_names` property lists the currently visible targets, and
`modulation_matrix_changed` fires a listener when the matrix is modified.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"WavetableDevice"`.
    - **`class_name`:** `"InstrumentVector"`. **`class_display_name`:** `"Wavetable"`.
    - **`type`:** 1 (`INSTRUMENT`).
    - **Insert name:** `"Wavetable"` (matches `class_display_name`).
    - **All 11 int properties** are settable and listenable. Round-trip confirmed.
    - **`filter_routing`:** 0–2 (0=Serial, 1=Parallel, 2=Split). 3+ throws.
    - **`mono_poly`:** 0=Mono, 1=Poly. Default 1.
    - **`oscillator_N_effect_mode`:** 0–3 (0=None, 1=Fm, 2=Classic, 3=Modern). 4+ throws.
    - **`oscillator_N_wavetable_category`:** Index into `oscillator_wavetable_categories`.
      Changing category updates `oscillator_N_wavetables`.
    - **`oscillator_N_wavetable_index`:** Index within current category's wavetable list.
    - **`oscillator_N_wavetables`:** Dynamic `list[str]` — updates on category change.
      Default category 0 ("Basics") has 29 wavetables.
    - **`oscillator_wavetable_categories`:** Static `list[str]` of 12 categories:
      `["Basics", "Collection", "Complex", "Distortion", "Filter", "Formant", "Harmonics",
      "Instrument", "Noise", "Retro", "Vintage", "User"]`.
    - **`poly_voices`:** 0–6 (7 valid values). 7+ throws "Invalid poly voice count".
    - **`unison_mode`:** 0–6 (0=None, 1=Classic, 2=Shimmer, 3=Noise, 4=Phase Sync,
      5=Position Spread, 6=Random Note). 7+ throws.
    - **`unison_voice_count`:** 2–8 (7 valid values). <2 or >8 throws.
    - **`visible_modulation_target_names`:** Read-only `list[str]`. Listenable.
      Default: `["Amp", "Pitch", "Osc 1 Pos", "Osc 1 Warp"]`.
    - **`modulation_matrix_changed`:** Listenable (no readable value, fire-only).
    - **Modulation sources:** 13 sources (indices 0–12). Source 13+ throws "invalid index".
    - **`is_parameter_modulatable(param)`:** Returns `bool`. `Device On` and `Osc 1 On`
      return `False`; `Osc 1 Transp`, `Osc 1 Detune`, `Osc 1 Pos` return `True`.
    - **`add_parameter_to_modulation_matrix(param)`:** Returns `int` (new target index).
    - **`get_modulation_target_parameter_name(target_idx)`:** Returns `str`.
    - **`get_modulation_value(target_idx, source)`:** Returns `float`.
    - **`set_modulation_value(target_idx, source, value)`:** Returns `None`. Round-trip confirmed.

### Children

| Child        | Returns                     | Shape    | Listenable | Summary                                        |
| ------------ | --------------------------- | -------- | ---------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | yes        | Automatable parameters exposed by this device. |
| `view`       | `WavetableDevice.View`      | `single` | no         | View aspects of the device (collapse state).   |

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), WavetableDevice adds:

| Property                          | Type        | Settable | Listenable | Summary                                                       |
| --------------------------------- | ----------- | -------- | ---------- | ------------------------------------------------------------- |
| `filter_routing`                  | `int`       | yes      | yes        | Filter routing mode: 0=Serial, 1=Parallel, 2=Split.          |
| `mono_poly`                       | `int`       | yes      | yes        | Voice mode: 0=Mono, 1=Poly.                                  |
| `oscillator_1_effect_mode`        | `int`       | yes      | yes        | Osc 1 effect mode: 0=None, 1=Fm, 2=Classic, 3=Modern.        |
| `oscillator_1_wavetable_category` | `int`       | yes      | yes        | Oscillator 1 wavetable category index.                        |
| `oscillator_1_wavetable_index`    | `int`       | yes      | yes        | Osc 1 wavetable index within the current category.            |
| `oscillator_1_wavetables`         | `list[str]` | no       | yes        | Wavetable names available for oscillator 1.                   |
| `oscillator_2_effect_mode`        | `int`       | yes      | yes        | Osc 2 effect mode (same values as osc 1).                     |
| `oscillator_2_wavetable_category` | `int`       | yes      | yes        | Oscillator 2 wavetable category index.                        |
| `oscillator_2_wavetable_index`    | `int`       | yes      | yes        | Osc 2 wavetable index within the current category.            |
| `oscillator_2_wavetables`         | `list[str]` | no       | yes        | Wavetable names available for oscillator 2.                   |
| `oscillator_wavetable_categories` | `list[str]` | no       | no         | Names of all available wavetable categories.                  |
| `poly_voices`                     | `int`       | yes      | yes        | Number of polyphonic voices (0–6).                            |
| `unison_mode`                     | `int`       | yes      | yes        | Unison mode (0–6, see values below).                          |
| `unison_voice_count`              | `int`       | yes      | yes        | Number of unison voices (2–8).                                |
| `visible_modulation_target_names` | `list[str]` | no       | yes        | Names of modulation targets visible in the matrix.            |

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot`, `store_chosen_bank`), WavetableDevice
adds:

| Method                                               | Returns | Summary                                                  |
| ---------------------------------------------------- | ------- | -------------------------------------------------------- |
| `add_parameter_to_modulation_matrix(parameter)`      | `int`   | Add a parameter to the modulation matrix.                |
| `get_modulation_target_parameter_name(target_index)` | `str`   | Get the parameter name for a modulation target by index. |
| `get_modulation_value(target_index, source)`         | `float` | Get the modulation amount for a target-source pair.      |
| `is_parameter_modulatable(parameter)`                | `bool`  | Check whether a parameter can be modulated.              |
| `set_modulation_value(target_index, source, value)`  | `None`  | Set the modulation amount for a target-source pair.      |

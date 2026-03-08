# TuningSystem

> `Live.TuningSystem.TuningSystem`

This class represents a tuning system in Live. TuningSystem is a standalone class (not a
Device subclass) that exposes the properties of the currently active tuning system,
including note tunings in cents, the reference pitch, the pseudo octave size, and the
playable note range. It is accessed via `live_set.tuning_system`.

When no custom tuning is active (default 12-TET), `song.tuning_system` returns `None`.
A custom tuning must be loaded from the Browser (Sounds > Tunings) to get a non-None
TuningSystem object.

??? note "Raw probe notes (temporary)"
    - `song.tuning_system` returns `None` when default 12-TET is active (no custom tuning loaded).
    - All 7 properties read successfully when a custom tuning is active.
    - `note_tunings` returns a plain `list[float]` (not a dict wrapping a list as Max docs suggest).
    - `highest_note` and `lowest_note` return `PitchClassAndOctave` instances (C++ value type,
      bridge serializes as `{index_in_octave: int, octave: int}`).
    - `reference_pitch` returns a `ReferencePitch` instance (C++ value type, bridge serializes as
      `{frequency: float, index_in_octave: int, octave: int}`).
    - `name` is writable (set + read-back confirmed).
    - `note_tunings` setter exists but expects a `tuple` (C++ signature: `boost::python::tuple`).
      Sending a `list` fails. Bridge needs decode support to convert `list` -> `tuple`.
    - `highest_note` and `lowest_note` setters exist but expect `NApiHelpers::TPitchClassAndOctave`.
      Bridge needs decode support to construct the C++ type from a dict.
    - `reference_pitch` setter exists but expects `NApiHelpers::TReferencePitch`. Bridge needs
      decode support to construct the C++ type from a dict.
    - `number_of_notes_in_pseudo_octave` and `pseudo_octave_in_cents` are read-only (no setter).

### Open Questions

- Can `note_tunings` be set by passing a Python `tuple` instead of `list`? Needs bridge decode
  support to test. The C++ signature explicitly requires `boost::python::tuple`.
- Can `highest_note`, `lowest_note`, and `reference_pitch` be set by constructing the Python
  wrappers (`PitchClassAndOctave(...)`, `ReferencePitch(...)`)? The C++ types are
  `NApiHelpers::TPitchClassAndOctave` and `NApiHelpers::TReferencePitch`. Bridge needs to
  import and construct these types in `_decode_value`.
- Are the settable properties undo-tracked?
- Listener behavior for all listenable properties is untested.

### Properties

| Property                           | Type                  | Settable              | Listenable | Summary                                                  |
| ---------------------------------- | --------------------- | --------------------- | ---------- | -------------------------------------------------------- |
| `highest_note`                     | `PitchClassAndOctave` | `PitchClassAndOctave` | `yes`      | The highest playable note as index-in-octave and octave. |
| `lowest_note`                      | `PitchClassAndOctave` | `PitchClassAndOctave` | `yes`      | The lowest playable note as index-in-octave and octave.  |
| `name`                             | `str`                 | `str`                 | `yes`      | Name of the currently active tuning system.              |
| `note_tunings`                     | `list[float]`         | `tuple[float, ...]`   | `yes`      | Note tunings in cents for the active tuning system.      |
| `number_of_notes_in_pseudo_octave` | `int`                 | no                    | `no`       | Number of notes in the pseudo octave.                    |
| `pseudo_octave_in_cents`           | `float`               | no                    | `no`       | Size of the pseudo octave in cents.                      |
| `reference_pitch`                  | `ReferencePitch`      | `ReferencePitch`      | `yes`      | The reference pitch of the active tuning system.         |

#### `highest_note`

- **Type:** `PitchClassAndOctave` (get) · `PitchClassAndOctave` (set)
- **Listenable:** `yes`
- **Since:** `12.1`

The highest playable note of the current tuning system. Returns a `PitchClassAndOctave`
instance with `index_in_octave` (int) and `octave` (int) fields. For 19-EDO, the default
value is `{index_in_octave: 15, octave: 6}`.

- **Limitations:** The setter exists (C++ signature accepts `NApiHelpers::TPitchClassAndOctave`) but the
  bridge does not yet construct the C++ type from a dict, so setting fails with a type mismatch error.

#### `lowest_note`

- **Type:** `PitchClassAndOctave` (get) · `PitchClassAndOctave` (set)
- **Listenable:** `yes`
- **Since:** `12.1`

The lowest playable note of the current tuning system. Returns a `PitchClassAndOctave`
instance with `index_in_octave` (int) and `octave` (int) fields. For 19-EDO, the default
value is `{index_in_octave: 2, octave: 0}`.

- **Limitations:** Same setter situation as `highest_note`.

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `12.1`

The name of the currently active tuning system (e.g. `"19-EDO"`, `"Just Intonation"`).
Confirmed writable: set to `"Test Tuning"` and read-back matched, then restored to original.

#### `note_tunings`

- **Type:** `list[float]` (get) · `tuple[float, ...]` (set)
- **Listenable:** `yes`
- **Since:** `12.1`

The note tunings for the active tuning system, specified in cents where 100 cents equals
one semitone in equal temperament. Returns a plain `list[float]` with one entry per note
in the pseudo octave (e.g. 19 entries for 19-EDO, starting at 0.0 and increasing).

- **Limitations:** The setter exists but its C++ signature requires a `boost::python::tuple`, not a Python
  `list`. Sending a list fails with a type mismatch. The bridge needs to convert `list` -> `tuple` in
  `_decode_value` for this property to be settable.

Example value (19-EDO):

```
[0.0, 63.16, 126.32, 189.47, 252.63, 315.79, 378.95, 442.11, 505.26, 568.42,
 631.58, 694.74, 757.89, 821.05, 884.21, 947.37, 1010.53, 1073.68, 1136.84]
```

#### `number_of_notes_in_pseudo_octave`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `12.1`

The number of notes in the pseudo octave for the active tuning system. Returns `19` for
19-EDO. Confirmed read-only: setting raises "property has no setter".

#### `pseudo_octave_in_cents`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.1`

The size of the pseudo octave in cents for the active tuning system. Returns `1200.0` for
19-EDO (standard 2:1 octave ratio). Non-octave tuning systems (e.g. Bohlen-Pierce) would
return a different value. Confirmed read-only: setting raises "property has no setter".

#### `reference_pitch`

- **Type:** `ReferencePitch` (get) · `ReferencePitch` (set)
- **Listenable:** `yes`
- **Since:** `12.1`

The reference pitch of the active tuning system. Returns a `ReferencePitch` instance with
`frequency` (float, Hz), `index_in_octave` (int), and `octave` (int) fields. For 19-EDO
with standard concert pitch, the value is `{frequency: 440.0, index_in_octave: 14, octave: 3}`.

- **Limitations:** The setter exists (C++ signature accepts `NApiHelpers::TReferencePitch`) but the bridge
  does not yet construct the C++ type from a dict, so setting fails with a type mismatch error.

---

## PitchClassAndOctave

> `Live.TuningSystem.PitchClassAndOctave`

A C++ value type (`NApiHelpers::TPitchClassAndOctave`) representing a note position as an
index within the pseudo octave and an octave number. Used by `TuningSystem.highest_note`
and `TuningSystem.lowest_note`. The bridge serializes it as a dict with `_pfl_type`,
`index_in_octave`, and `octave` keys.

??? note "Raw probe notes (temporary)"
    Confirmed as a C++ value type. The bridge reads `index_in_octave` and `octave` attributes.
    Example values from 19-EDO: `{index_in_octave: 15, octave: 6}` (highest),
    `{index_in_octave: 2, octave: 0}` (lowest).

### Properties

| Property          | Type  | Settable | Listenable | Summary                                    |
| ----------------- | ----- | -------- | ---------- | ------------------------------------------ |
| `index_in_octave` | `int` | no       | `no`       | The note's index within the pseudo octave. |
| `octave`          | `int` | no       | `no`       | The octave number.                         |

#### `index_in_octave`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `12.1`

The note's index within the pseudo octave. For 19-EDO, the highest note has
`index_in_octave: 15` and the lowest has `index_in_octave: 2`.

#### `octave`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `12.1`

The octave number for this pitch class position. For 19-EDO, the highest note is in
octave 6 and the lowest in octave 0.

---

## ReferencePitch

> `Live.TuningSystem.ReferencePitch`

A C++ value type (`NApiHelpers::TReferencePitch`) representing the reference pitch of a
tuning system, combining a frequency in Hz with a pitch class position. Used by
`TuningSystem.reference_pitch`. The bridge serializes it as a dict with `_pfl_type`,
`frequency`, `index_in_octave`, and `octave` keys.

??? note "Raw probe notes (temporary)"
    Confirmed as a C++ value type. The bridge reads `frequency`, `index_in_octave`, and `octave`
    attributes. Example value from 19-EDO: `{frequency: 440.0, index_in_octave: 14, octave: 3}`.

### Properties

| Property          | Type    | Settable | Listenable | Summary                                               |
| ----------------- | ------- | -------- | ---------- | ----------------------------------------------------- |
| `frequency`       | `float` | no       | `no`       | The reference frequency in Hz (e.g. 440.0).           |
| `index_in_octave` | `int`   | no       | `no`       | The reference pitch's index within the pseudo octave. |
| `octave`          | `int`   | no       | `no`       | The reference pitch's octave number.                  |

#### `frequency`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.1`

The reference frequency in Hz. For standard concert pitch, this is 440.0 Hz.

#### `index_in_octave`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `12.1`

The reference pitch's index within the pseudo octave. For 19-EDO with A=440, this is 14.

#### `octave`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `12.1`

The octave number of the reference pitch. For 19-EDO with A=440, this is 3.

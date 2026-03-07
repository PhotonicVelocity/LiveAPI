# TuningSystem

## TuningSystem

This class represents a tuning system in Live. TuningSystem is a standalone class (not a
Device subclass) that exposes the properties of the currently active tuning system,
including note tunings in cents, the reference pitch, the pseudo octave size, and the
playable note range. It is accessed via `live_set.tuning_system`.

When no custom tuning is active (default 12-TET), `song.tuning_system` returns `None`.
A custom tuning must be loaded from the Browser (Sounds > Tunings) to get a non-None
TuningSystem object.

### Sources

- **Primary:** `Live/classes/TuningSystem.py` (stub dump)
- **Secondary:** `MaxForLive/tuningsystem.md`
- **Probes:** 2026-02-25, Live 12.3.5, 19-EDO tuning active

### Probe Notes

- `song.tuning_system` returns `None` when default 12-TET is active (no custom tuning loaded).
- All 7 properties read successfully when a custom tuning is active.
- `note_tunings` returns a plain `list[float]` (not a dict wrapping a list as Max docs suggest).
- `highest_note` and `lowest_note` return `PitchClassAndOctave` instances (C++ value type,
  bridge serializes as `{index_in_octave: int, octave: int}`).
- `reference_pitch` returns a `ReferencePitch` instance (C++ value type, bridge serializes as
  `{frequency: float, index_in_octave: int, octave: int}`).
- `name` is writable (set + read-back confirmed).
- `note_tunings` setter exists but expects a `tuple` (C++ signature: `boost::python::tuple`).
  Sending a `list` fails. Bridge needs decode support to convert `list` → `tuple`.
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

| Property                           | Get Returns           | Set Accepts           | Listenable | Available Since | Summary                                                  |
| ---------------------------------- | --------------------- | --------------------- | ---------- | --------------- | -------------------------------------------------------- |
| `highest_note`                     | `PitchClassAndOctave` | `PitchClassAndOctave` | `yes`      | `12.1`          | The highest playable note as index-in-octave and octave. |
| `lowest_note`                      | `PitchClassAndOctave` | `PitchClassAndOctave` | `yes`      | `12.1`          | The lowest playable note as index-in-octave and octave.  |
| `name`                             | `str`                 | `str`                 | `yes`      | `12.1`          | Name of the currently active tuning system.              |
| `note_tunings`                     | `list[float]`         | `tuple[float, ...]`   | `yes`      | `12.1`          | Note tunings in cents for the active tuning system.      |
| `number_of_notes_in_pseudo_octave` | `int`                 | —                     | `no`       | `12.1`          | Number of notes in the pseudo octave.                    |
| `pseudo_octave_in_cents`           | `float`               | —                     | `no`       | `12.1`          | Size of the pseudo octave in cents.                      |
| `reference_pitch`                  | `ReferencePitch`      | `ReferencePitch`      | `yes`      | `12.1`          | The reference pitch of the active tuning system.         |

#### `highest_note`

- **Get Returns:** `PitchClassAndOctave`
- **Set Accepts:** `PitchClassAndOctave` (setter exists, needs bridge decode support)
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The highest playable note of the current tuning system. Returns a `PitchClassAndOctave`
instance with `index_in_octave` (int) and `octave` (int) fields. For 19-EDO, the default
value is `{index_in_octave: 15, octave: 6}`.

The setter exists (C++ signature accepts `NApiHelpers::TPitchClassAndOctave`) but the bridge
does not yet construct the C++ type from a dict, so setting fails with a type mismatch error.

#### `lowest_note`

- **Get Returns:** `PitchClassAndOctave`
- **Set Accepts:** `PitchClassAndOctave` (setter exists, needs bridge decode support)
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The lowest playable note of the current tuning system. Returns a `PitchClassAndOctave`
instance with `index_in_octave` (int) and `octave` (int) fields. For 19-EDO, the default
value is `{index_in_octave: 2, octave: 0}`.

Same setter situation as `highest_note`.

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The name of the currently active tuning system (e.g. `"19-EDO"`, `"Just Intonation"`).
Confirmed writable: set to `"Test Tuning"` and read-back matched, then restored to original.

#### `note_tunings`

- **Get Returns:** `list[float]` — one float per note in the pseudo octave, in cents
- **Set Accepts:** `tuple[float, ...]` (C++ requires `boost::python::tuple`, not `list`)
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The note tunings for the active tuning system, specified in cents where 100 cents equals
one semitone in equal temperament. Returns a plain `list[float]` with one entry per note
in the pseudo octave (e.g. 19 entries for 19-EDO, starting at 0.0 and increasing).

The setter exists but its C++ signature requires a `boost::python::tuple`, not a Python
`list`. Sending a list fails with a type mismatch. The bridge needs to convert `list` →
`tuple` in `_decode_value` for this property to be settable.

Example value (19-EDO):

```
[0.0, 63.16, 126.32, 189.47, 252.63, 315.79, 378.95, 442.11, 505.26, 568.42,
 631.58, 694.74, 757.89, 821.05, 884.21, 947.37, 1010.53, 1073.68, 1136.84]
```

#### `number_of_notes_in_pseudo_octave`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The number of notes in the pseudo octave for the active tuning system. Returns `19` for
19-EDO. Confirmed read-only: setting raises "property has no setter".

#### `pseudo_octave_in_cents`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The size of the pseudo octave in cents for the active tuning system. Returns `1200.0` for
19-EDO (standard 2:1 octave ratio). Non-octave tuning systems (e.g. Bohlen-Pierce) would
return a different value. Confirmed read-only: setting raises "property has no setter".

#### `reference_pitch`

- **Get Returns:** `ReferencePitch`
- **Set Accepts:** `ReferencePitch` (setter exists, needs bridge decode support)
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The reference pitch of the active tuning system. Returns a `ReferencePitch` instance with
`frequency` (float, Hz), `index_in_octave` (int), and `octave` (int) fields. For 19-EDO
with standard concert pitch, the value is `{frequency: 440.0, index_in_octave: 14, octave: 3}`.

The setter exists (C++ signature accepts `NApiHelpers::TReferencePitch`) but the bridge
does not yet construct the C++ type from a dict, so setting fails with a type mismatch error.

---

## PitchClassAndOctave

A C++ value type (`NApiHelpers::TPitchClassAndOctave`) representing a note position as an
index within the pseudo octave and an octave number. Used by `TuningSystem.highest_note`
and `TuningSystem.lowest_note`. The bridge serializes it as a dict with `_pfl_type`,
`index_in_octave`, and `octave` keys.

### Sources

- **Primary:** `Live/classes/TuningSystem.py` (stub dump -- nested class)
- **Probes:** 2026-02-25, Live 12.3.5

### Probe Notes

Confirmed as a C++ value type. The bridge reads `index_in_octave` and `octave` attributes.
Example values from 19-EDO: `{index_in_octave: 15, octave: 6}` (highest),
`{index_in_octave: 2, octave: 0}` (lowest).

### Properties

| Property          | Get Returns | Set Accepts | Listenable | Available Since | Summary                                    |
| ----------------- | ----------- | ----------- | ---------- | --------------- | ------------------------------------------ |
| `index_in_octave` | `int`       | —           | `no`       | `12.1`          | The note's index within the pseudo octave. |
| `octave`          | `int`       | —           | `no`       | `12.1`          | The octave number.                         |

#### `index_in_octave`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The note's index within the pseudo octave. For 19-EDO, the highest note has
`index_in_octave: 15` and the lowest has `index_in_octave: 2`.

#### `octave`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The octave number for this pitch class position. For 19-EDO, the highest note is in
octave 6 and the lowest in octave 0.

---

## ReferencePitch

A C++ value type (`NApiHelpers::TReferencePitch`) representing the reference pitch of a
tuning system, combining a frequency in Hz with a pitch class position. Used by
`TuningSystem.reference_pitch`. The bridge serializes it as a dict with `_pfl_type`,
`frequency`, `index_in_octave`, and `octave` keys.

### Sources

- **Primary:** `Live/classes/TuningSystem.py` (stub dump -- nested class)
- **Probes:** 2026-02-25, Live 12.3.5

### Probe Notes

Confirmed as a C++ value type. The bridge reads `frequency`, `index_in_octave`, and `octave`
attributes. Example value from 19-EDO: `{frequency: 440.0, index_in_octave: 14, octave: 3}`.

### Properties

| Property          | Get Returns | Set Accepts | Listenable | Available Since | Summary                                               |
| ----------------- | ----------- | ----------- | ---------- | --------------- | ----------------------------------------------------- |
| `frequency`       | `float`     | —           | `no`       | `12.1`          | The reference frequency in Hz (e.g. 440.0).           |
| `index_in_octave` | `int`       | —           | `no`       | `12.1`          | The reference pitch's index within the pseudo octave. |
| `octave`          | `int`       | —           | `no`       | `12.1`          | The reference pitch's octave number.                  |

#### `frequency`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The reference frequency in Hz. For standard concert pitch, this is 440.0 Hz.

#### `index_in_octave`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The reference pitch's index within the pseudo octave. For 19-EDO with A=440, this is 14.

#### `octave`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `12.1`
- **Sources:** `stub | probe`
- **Probe Status:** `probed` — 2026-02-25, Live 12.3.5

**Description:**
The octave number of the reference pitch. For 19-EDO with A=440, this is 3.

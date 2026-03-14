# TuningSystem

> `Live.TuningSystem.TuningSystem`

Represents a Tuning System and its properties.

**Live Object:** `yes`

**Access via:**

- `Song.tuning_system`

## Properties

| Property                           | Type                  | Settable | Listenable | Description                                                                      |
| ---------------------------------- | --------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `canonical_parent`                 | `Song`                | `no`     | `no`       | Get the canonical parent of the TuningSystem.                                    |
| `highest_note`                     | `PitchClassAndOctave` | `yes`    | `yes`      | Get/Set the highest note of the current tuning system, where the first entry ... |
| `lowest_note`                      | `PitchClassAndOctave` | `yes`    | `yes`      | Get/Set the lowest note of the current tuning system, where the first entry i... |
| `name`                             | `str`                 | `yes`    | `yes`      | Get/Set the name of the currently active tuning system.                          |
| `note_tunings`                     | `list`                | `yes`    | `yes`      | Get/Set the currently active tuning system's note tunings, specified in Cents... |
| `number_of_notes_in_pseudo_octave` | `int`                 | `no`     | `no`       | Get the number of notes in the pseudo octave.                                    |
| `pseudo_octave_in_cents`           | `float`               | `no`     | `no`       | Get the pseudo octave in cents for the currently active tuning system.           |
| `reference_pitch`                  | `ReferencePitch`      | `yes`    | `yes`      | Get/Set the reference pitch the currently active tuning system.                  |

### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the TuningSystem.

### `highest_note`

- **Type:** `PitchClassAndOctave`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the highest note of the current tuning system, where the first entry is the index within the pseudo octave and the second entry is the octave.

### `lowest_note`

- **Type:** `PitchClassAndOctave`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the lowest note of the current tuning system, where the first entry is the index within the pseudo octave and the second entry is the octave.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the name of the currently active tuning system.

### `note_tunings`

- **Type:** `list`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament.

### `number_of_notes_in_pseudo_octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the number of notes in the pseudo octave.

### `pseudo_octave_in_cents`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Get the pseudo octave in cents for the currently active tuning system.

### `reference_pitch`

- **Type:** `ReferencePitch`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the reference pitch the currently active tuning system.

## PitchClassAndOctave

> `Live.TuningSystem.PitchClassAndOctave`

This class represents a PitchClassAndOctave type.

**Constructor:** `PitchClassAndOctave(index_in_octave: int, octave: int)`

### Properties

| Property          | Type  | Settable | Listenable | Description                                             |
| ----------------- | ----- | -------- | ---------- | ------------------------------------------------------- |
| `index_in_octave` | `int` | `no`     | `no`       | A PitchClassAndOctave's index within the pseudo octave. |
| `octave`          | `int` | `no`     | `no`       | A PitchClassAndOctave's octave.                         |

#### `index_in_octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

A PitchClassAndOctave's index within the pseudo octave.

#### `octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

A PitchClassAndOctave's octave.

## ReferencePitch

> `Live.TuningSystem.ReferencePitch`

This class represents a ReferencePitch type.

**Constructor:** `ReferencePitch(index_in_octave: int, octave: int, frequency: float)`

### Properties

| Property          | Type    | Settable | Listenable | Description                                        |
| ----------------- | ------- | -------- | ---------- | -------------------------------------------------- |
| `frequency`       | `float` | `no`     | `no`       | A ReferencePitch's frequency in Hz.                |
| `index_in_octave` | `int`   | `no`     | `no`       | A ReferencePitch's index within the pseudo octave. |
| `octave`          | `int`   | `no`     | `no`       | A ReferencePitch's octave.                         |

#### `frequency`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

A ReferencePitch's frequency in Hz.

#### `index_in_octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

A ReferencePitch's index within the pseudo octave.

#### `octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

A ReferencePitch's octave.

# TuningSystem (Module)

## TuningSystem (Class)

> `Live.TuningSystem.TuningSystem`

Represents a Tuning System and its properties.

**Live Object:** `yes`

**Access via:**

- `Song.tuning_system`

### Properties

| Property                                                                | Type                  | Supports             |
| ----------------------------------------------------------------------- | --------------------- | -------------------- |
| [`canonical_parent`](#canonical_parent)                                 | `Song`                | `get`                |
| [`highest_note`](#highest_note)                                         | `PitchClassAndOctave` | `get`/`set`/`listen` |
| [`lowest_note`](#lowest_note)                                           | `PitchClassAndOctave` | `get`/`set`/`listen` |
| [`name`](#name)                                                         | `str`                 | `get`/`set`/`listen` |
| [`note_tunings`](#note_tunings)                                         | `list`                | `get`/`set`/`listen` |
| [`number_of_notes_in_pseudo_octave`](#number_of_notes_in_pseudo_octave) | `int`                 | `get`                |
| [`pseudo_octave_in_cents`](#pseudo_octave_in_cents)                     | `float`               | `get`                |
| [`reference_pitch`](#reference_pitch)                                   | `ReferencePitch`      | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `Song`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the TuningSystem.

#### `highest_note`

- **Type:** `PitchClassAndOctave`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the highest note of the current tuning system, where the first entry is the index within the pseudo octave and the second entry is the octave.

#### `lowest_note`

- **Type:** `PitchClassAndOctave`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the lowest note of the current tuning system, where the first entry is the index within the pseudo octave and the second entry is the octave.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the name of the currently active tuning system.

#### `note_tunings`

- **Type:** `list`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament.

#### `number_of_notes_in_pseudo_octave`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the number of notes in the pseudo octave.

#### `pseudo_octave_in_cents`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Get the pseudo octave in cents for the currently active tuning system.

#### `reference_pitch`

- **Type:** `ReferencePitch`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the reference pitch the currently active tuning system.

## PitchClassAndOctave (Type)

> `Live.TuningSystem.PitchClassAndOctave`

This class represents a PitchClassAndOctave type.

**Constructor:** `PitchClassAndOctave(index_in_octave: int, octave: int)`

### Properties

| Property                              | Type  | Supports |
| ------------------------------------- | ----- | -------- |
| [`index_in_octave`](#index_in_octave) | `int` | `get`    |
| [`octave`](#octave)                   | `int` | `get`    |

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

## ReferencePitch (Type)

> `Live.TuningSystem.ReferencePitch`

This class represents a ReferencePitch type.

**Constructor:** `ReferencePitch(index_in_octave: int, octave: int, frequency: float)`

### Properties

| Property                              | Type    | Supports |
| ------------------------------------- | ------- | -------- |
| [`frequency`](#frequency)             | `float` | `get`    |
| [`index_in_octave`](#index_in_octave) | `int`   | `get`    |
| [`octave`](#octave)                   | `int`   | `get`    |

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

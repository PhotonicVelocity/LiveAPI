# DrumPad (Module)

## DrumPad (Class)

> `Live.DrumPad.DrumPad`

This class represents a drum group device pad in Live.

**Live Object:** `yes`

**Access via:**

- `RackDevice.View.selected_drum_pad`

### Properties

| Property                                | Type            | Supports             |
| --------------------------------------- | --------------- | -------------------- |
| [`canonical_parent`](#canonical_parent) | `RackDevice`    | `get`                |
| [`chains`](#chains)                     | `Vector[Chain]` | `get`/`listen`       |
| [`mute`](#mute)                         | `bool`          | `get`/`set`/`listen` |
| [`name`](#name)                         | `str`           | `get`/`listen`       |
| [`note`](#note)                         | `int`           | `get`                |
| [`solo`](#solo)                         | `bool`          | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the drum pad.

#### `chains`

- **Type:** `Vector[Chain]`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of chains in this drum pad.

#### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Mute/unmute the pad.

#### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the drum pad's name. It depends on the contained chains.

#### `note`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the MIDI note of the drum pad.

#### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Solo/unsolo the pad.

### Methods

| Method                                      | Returns |
| ------------------------------------------- | ------- |
| [`delete_all_chains()`](#delete_all_chains) | `None`  |

#### `delete_all_chains()`

- **Returns:** `None`

Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.

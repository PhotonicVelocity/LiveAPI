# DrumPad

> `Live.DrumPad.DrumPad`

This class represents a drum group device pad in Live.

**Live Object:** `yes`

**Access via:**

- `RackDevice.View.selected_drum_pad`

## Properties

| Property           | Type         | Settable | Listenable | Description                                                 |
| ------------------ | ------------ | -------- | ---------- | ----------------------------------------------------------- |
| `canonical_parent` | `RackDevice` | `no`     | `no`       | Get the canonical parent of the drum pad.                   |
| `chains`           | `tuple`      | `no`     | `yes`      | Return const access to the list of chains in this drum pad. |
| `mute`             | `bool`       | `yes`    | `yes`      | Mute/unmute the pad.                                        |
| `name`             | `str`        | `no`     | `yes`      | Return const access to the drum pad's name.                 |
| `note`             | `int`        | `no`     | `no`       | Get the MIDI note of the drum pad.                          |
| `solo`             | `bool`       | `yes`    | `yes`      | Solo/unsolo the pad.                                        |

### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the drum pad.

### `chains`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of chains in this drum pad.

### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Mute/unmute the pad.

### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the drum pad's name. It depends on the contained chains.

### `note`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Get the MIDI note of the drum pad.

### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Solo/unsolo the pad.

## Methods

| Method                | Returns | Description                                    |
| --------------------- | ------- | ---------------------------------------------- |
| `delete_all_chains()` | `None`  | Deletes all chains associated with a drum pad. |

### `delete_all_chains()`

- **Returns:** `None`

Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.

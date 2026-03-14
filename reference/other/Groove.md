# Groove (Module)

## Groove (Class)

> `Live.Groove.Groove`

This class represents a groove in Live.

**Live Object:** `yes`

### Properties

| Property              | Type         | Supports             |
| --------------------- | ------------ | -------------------- |
| `base`                | `Base`       | `get`/`set`          |
| `canonical_parent`    | `GroovePool` | `get`                |
| `name`                | `str`        | `get`/`set`/`listen` |
| `quantization_amount` | `float`      | `get`/`set`/`listen` |
| `random_amount`       | `float`      | `get`/`set`/`listen` |
| `timing_amount`       | `float`      | `get`/`set`/`listen` |
| `velocity_amount`     | `float`      | `get`/`set`/`listen` |

#### `base`

- **Type:** `Base`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set the groove's base grid.

#### `canonical_parent`

- **Type:** `GroovePool`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the groove.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's name

#### `quantization_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's quantization amount.

#### `random_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's random amount.

#### `timing_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's timing amount.

#### `velocity_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's velocity amount.

## Enums

### `Base`

| Value | Name                 |
| ----- | -------------------- |
| `0`   | `gb_four`            |
| `1`   | `gb_eight`           |
| `2`   | `gb_eight_triplet`   |
| `3`   | `gb_sixteen`         |
| `4`   | `gb_sixteen_triplet` |
| `5`   | `gb_thirtytwo`       |
| `6`   | `count`              |

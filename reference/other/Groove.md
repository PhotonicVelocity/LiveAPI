# Groove

> `Live.Groove.Groove`

This class represents a groove in Live.

**Live Object:** `yes`

## Properties

| Property              | Type         | Settable | Listenable | Description                                                   |
| --------------------- | ------------ | -------- | ---------- | ------------------------------------------------------------- |
| `base`                | `Base`       | `yes`    | `no`       | Get/set the groove's base grid.                               |
| `canonical_parent`    | `GroovePool` | `no`     | `no`       | Get the canonical parent of the groove.                       |
| `name`                | `str`        | `yes`    | `yes`      | Read/write/listen access to the groove's name.                |
| `quantization_amount` | `float`      | `yes`    | `yes`      | Read/write/listen access to the groove's quantization amount. |
| `random_amount`       | `float`      | `yes`    | `yes`      | Read/write/listen access to the groove's random amount.       |
| `timing_amount`       | `float`      | `yes`    | `yes`      | Read/write/listen access to the groove's timing amount.       |
| `velocity_amount`     | `float`      | `yes`    | `yes`      | Read/write/listen access to the groove's velocity amount.     |

### `base`

- **Type:** `Base`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set the groove's base grid.

### `canonical_parent`

- **Type:** `GroovePool`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the groove.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's name

### `quantization_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's quantization amount.

### `random_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's random amount.

### `timing_amount`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write/listen access to the groove's timing amount.

### `velocity_amount`

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

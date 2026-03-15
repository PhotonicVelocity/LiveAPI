# Envelope (Module)

## Envelope (Class)

> `Live.Envelope.Envelope`

This class represents an automation or modulation envelope in Live.

**Live Object:** `yes`

**Access via:**

- `Clip.automation_envelope()`
- `Clip.create_automation_envelope()`

### Properties

| Property                                | Type   | Supports |
| --------------------------------------- | ------ | -------- |
| [`canonical_parent`](#canonical_parent) | `Clip` | `get`    |

#### `canonical_parent`

- **Type:** `Clip`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the envelope.

### Methods

| Method                                                                               | Returns               |
| ------------------------------------------------------------------------------------ | --------------------- |
| [`delete_events_in_range()`](#delete_events_in_rangestart_time-float-end_time-float) | `None`                |
| [`events_in_range()`](#events_in_rangestart_time-float-end_time-float)               | `EnvelopeEventVector` |
| [`insert_step()`](#insert_stepstart_time-float-length-float-value-float)             | `None`                |
| [`value_at_time()`](#value_at_timetime-float)                                        | `float`               |

#### `delete_events_in_range(start_time: float, end_time: float)`

- **Returns:** `None`
- **Args:**
  - `start_time: float`
  - `end_time: float`

Deletes the events in the specified time range.

#### `events_in_range(start_time: float, end_time: float)`

- **Returns:** `EnvelopeEventVector`
- **Args:**
  - `start_time: float`
  - `end_time: float`

Returns the events in the specified time range.

#### `insert_step(start_time: float, length: float, value: float)`

- **Returns:** `None`
- **Args:**
  - `start_time: float`
  - `length: float`
  - `value: float`

Given a start time, a step length and a value, creates a step in the envelope.

#### `value_at_time(time: float)`

- **Returns:** `float`
- **Args:**
  - `time: float`

Returns the parameter value at the specified time.

## EnvelopeEvent (Type)

> `Live.Envelope.EnvelopeEvent`

This is a class that represents an envelope event.

**Constructor:** `EnvelopeEvent(time: float, value: float, control_coefficients: EnvelopeEventControlCoefficients)`

### Properties

| Property                                        | Type                               | Supports    |
| ----------------------------------------------- | ---------------------------------- | ----------- |
| [`control_coefficients`](#control_coefficients) | `EnvelopeEventControlCoefficients` | `get`/`set` |
| [`time`](#time)                                 | `float`                            | `get`/`set` |
| [`value`](#value)                               | `float`                            | `get`/`set` |

#### `control_coefficients`

- **Type:** `EnvelopeEventControlCoefficients`
- **Settable:** `yes`
- **Listenable:** `no`

#### `time`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `value`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

## EnvelopeEventControlCoefficients (Type)

> `Live.Envelope.EnvelopeEventControlCoefficients`

This class represents the control coefficients of an envelope event.

**Constructor:** `EnvelopeEventControlCoefficients(x1: float, y1: float, x2: float, y2: float)`

### Properties

| Property    | Type    | Supports    |
| ----------- | ------- | ----------- |
| [`x1`](#x1) | `float` | `get`/`set` |
| [`x2`](#x2) | `float` | `get`/`set` |
| [`y1`](#y1) | `float` | `get`/`set` |
| [`y2`](#y2) | `float` | `get`/`set` |

#### `x1`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `x2`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `y1`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

#### `y2`

- **Type:** `float`
- **Settable:** `yes`
- **Listenable:** `no`

## EnvelopeEventVector (Type)

> `Live.Envelope.EnvelopeEventVector`

A container for holding envelope events.

### Methods

| Method                                    | Returns |
| ----------------------------------------- | ------- |
| [`append()`](#appendvalue-envelopeevent)  | `None`  |
| [`extend()`](#extendvalues-envelopeevent) | `None`  |

#### `append(value: EnvelopeEvent)`

- **Returns:** `None`
- **Args:**
  - `value: EnvelopeEvent`

#### `extend(values: EnvelopeEvent)`

- **Returns:** `None`
- **Args:**
  - `values: EnvelopeEvent`

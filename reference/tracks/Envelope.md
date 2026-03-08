# Envelope

> `Live.Envelope.Envelope`

This class represents an automation or modulation envelope in Live. An envelope contains
breakpoint events that describe how a parameter value changes over time. Envelopes can be
queried for their events, edited by inserting steps or deleting event ranges, and sampled
at arbitrary time positions.

??? note "Raw probe notes (temporary)"
    - `canonical_parent` returns the parent `Clip` handle -- confirmed for session clip envelopes.
    - Time coordinates are in beats (relative to clip start). `insert_step(0.0, 1.0, 0.5)` on a
      4-beat clip created a step from beat 0 to beat 1; `value_at_time(0.5)` returned the inserted
      value `0.5`.
    - `value_at_time` on a fresh envelope (no events) returns the parameter's current value
      (e.g. 0.85 for volume at default).
    - `events_in_range` fails with `ValidationError: Unsupported return type: EnvelopeEvent` --
      EnvelopeEvent is a value object (like MidiNote/WarpMarker), not a handle-based object.
      Returns `[]` successfully when there are no events. Needs bridge-side serialization.
    - `delete_events_in_range` works; after deletion, `events_in_range` returns `[]`.
    - Both `events_in_range` and `delete_events_in_range` reject large `end` values with
      `ValidationError: Range out of bounds.` The max accepted value is approximately `1,576,800`
      beats (~4.5 hours at 120 BPM). `2,147,483,647.0` (max 32-bit int) fails. Values up to
      `1,000,000.0` work reliably.
    - `automation_envelope(param)` accepts a DeviceParameter handle directly. Returns `None` when
      no envelope exists for that parameter, or an Envelope handle when one does.
    - `create_automation_envelope(param)` returns an Envelope handle. Raises
      `InternalError: There is already an envelope for the parameter` if called twice.
    - `automation_envelopes` children list returns Envelope handles via standard `children()` call.
      Empty list when no envelopes exist.
    - `clear_envelope(param)` and `clear_all_envelopes()` both work. `has_envelopes` correctly
      reflects state transitions (False -> True after create, False after clear).
    - Envelope type name in the bridge is `"Envelope"`.

### Open Questions

- ~~Does `insert_step()` overwrite existing events in the step range, or does it merge?~~
  **Resolved:** partial overwrite. The new step overwrites only its range; non-overlapping
  portions of prior steps are preserved. Tested via `value_at_time` on overlapping regions.
- ~~Are the `EnvelopeEvent.control_coefficients` used for curve shaping between breakpoints?
  What do `x1`, `x2`, `y1`, `y2` represent -- Bezier control points?~~
  **Resolved:** Yes, cubic Bezier control points. `(x1, y1)` and `(x2, y2)` define the
  interpolation curve between this event and the next. Default `(0.5, 0.5, 0.5, 0.5)` =
  linear (straight line). Always present (never None). Non-default values only come from
  UI-drawn curves -- `insert_step` has no curve parameter.
- Envelope event values are in the parameter's native internal scale, not the 0-1 linear
  fader range. For volume: `insert_step(value=0.5)` -> event value ~= 0.1995 (dB-scale).
- Each flat step is represented as two events at the same time (discontinuity/jump).
  Boundary events with value 1.0 appear at envelope edges.

### Properties

| Property           | Type     | Settable | Listenable | Summary                                    |
| ------------------ | -------- | -------- | ---------- | ------------------------------------------ |
| `canonical_parent` | `object` | no       | `no`       | The parent object that owns this envelope. |

#### `canonical_parent`

- **Type:** `Clip`
- **Listenable:** `no`
- **Since:** `<11`

Returns the canonical parent of this envelope. For session clip envelopes, this is the parent
`Clip` object. Probing confirmed the returned handle has `type=Clip` and matches the clip OID.

### Methods

| Method                                                   | Returns               | Summary                                         |
| -------------------------------------------------------- | --------------------- | ----------------------------------------------- |
| `delete_events_in_range(start: float, end: float)`       | `None`                | Delete all envelope events within a time range. |
| `events_in_range(start: float, end: float)`              | `EnvelopeEventVector` | Return all envelope events within a time range. |
| `insert_step(start: float, length: float, value: float)` | `None`                | Insert a constant-value step into the envelope. |
| `value_at_time(time: float)`                             | `float`               | Return the parameter value at a specific time.  |

#### `delete_events_in_range(start: float, end: float)`

- **Returns:** `None`
- **Args:**
    - `start: float` -- the start time of the range (beats)
    - `end: float` -- the end time of the range (beats)
- **Raises:** `ValidationError: Range out of bounds.` when `end` exceeds ~1,576,800.
- **Since:** `12.2`

Deletes all envelope events that fall within the specified time range defined by `start`
and `end`. Times are in beats relative to clip start. Probing confirmed deletion works and
subsequent `events_in_range` returns `[]`. The `end` parameter has an upper bound of
approximately 1,576,800 beats; values beyond this (including `2,147,483,647.0`) are rejected.

#### `events_in_range(start: float, end: float)`

- **Returns:** `EnvelopeEventVector` (list of `EnvelopeEvent`)
- **Args:**
    - `start: float` -- the start time of the range (beats)
    - `end: float` -- the end time of the range (beats)
- **Raises:** `ValidationError: Range out of bounds.` when `end` exceeds ~1,576,800.
- **Since:** `12.2`

Returns a vector of `EnvelopeEvent` objects that fall within the specified time range.
Each event has a `time`, `value`, and `control_coefficients` property. Times are in beats
relative to clip start. Values are in the parameter's native internal scale (e.g. dB for
volume). Each flat step creates two events at the same time (a discontinuity). Boundary
events with value 1.0 appear at envelope edges. The `end` parameter has an upper bound of
approximately 1,576,800 beats (~4.5 hours at 120 BPM); values beyond this (including
`2,147,483,647.0`) are rejected with a validation error.

#### `insert_step(start: float, length: float, value: float)`

- **Returns:** `None`
- **Args:**
    - `start: float` -- the start time of the step (beats)
    - `length: float` -- the duration of the step (beats)
    - `value: float` -- the parameter value for the step
- **Since:** `12.2`

Creates a step (flat segment) in the envelope starting at `start`, lasting for `length`,
at the given `value`. Times are in beats relative to clip start. Probing confirmed:
`insert_step(0.0, 1.0, 0.5)` followed by `value_at_time(0.5)` returned `0.5`.

#### `value_at_time(time: float)`

- **Returns:** `float`
- **Args:**
    - `time: float` -- the time position to sample (beats)
- **Since:** `12.2`

Returns the interpolated parameter value of the envelope at the specified time position.
Time is in beats relative to clip start. On a fresh envelope with no events, returns the
parameter's current value (e.g. `0.85` for volume at default). After `insert_step(0.0, 1.0, 0.5)`,
`value_at_time(0.5)` returns `0.5`.

---

## EnvelopeEvent

> `Live.Envelope.EnvelopeEvent`

This class represents a single breakpoint event within an envelope. Each event has a time
position, a value, and control coefficients that define the cubic Bezier curve shape between
this event and the next.

??? note "Raw probe notes (temporary)"
    EnvelopeEvent is a value object (not handle-based), serialized by the bridge following the
    MidiNote/WarpMarker pattern. Probed via `events_in_range` after bridge serialization was added.

    - `control_coefficients` is always present (never None). Default `(0.5, 0.5, 0.5, 0.5)` =
      linear interpolation. Non-default values only come from UI-drawn automation curves.
    - `time` is in beats relative to clip start.
    - `value` is in the parameter's native internal scale (e.g. dB for volume, not 0-1 linear).
    - Each flat step creates two events at the same time (a discontinuity/jump).
    - Boundary events with value 1.0 appear at the start and end of the envelope range.

### Properties

| Property               | Type                               | Settable | Listenable | Summary                                       |
| ---------------------- | ---------------------------------- | -------- | ---------- | --------------------------------------------- |
| `control_coefficients` | `EnvelopeEventControlCoefficients` | no       | `no`       | Curve-shaping coefficients for this event.    |
| `time`                 | `float`                            | no       | `no`       | The time position of this breakpoint (beats). |
| `value`                | `float`                            | no       | `no`       | The parameter value at this breakpoint.       |

#### `control_coefficients`

- **Type:** `EnvelopeEventControlCoefficients`
- **Listenable:** `no`
- **Since:** `12.2`

Cubic Bezier control points defining the interpolation curve between this event and the next.
`(x1, y1)` is the first control point, `(x2, y2)` is the second. Default `(0.5, 0.5, 0.5, 0.5)`
= linear (straight line). Always present (never None). Non-default values only appear from
UI-drawn automation curves -- the `insert_step` API produces flat steps with default coefficients.

#### `time`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

The time position of this breakpoint event in beats relative to clip start. Flat steps
create two events at the same time to represent the value discontinuity (jump).

#### `value`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

The parameter value at this breakpoint, in the parameter's native internal scale. For volume
this is a logarithmic (dB) scale, not 0-1 linear. Boundary events use value 1.0.

---

## EnvelopeEventControlCoefficients

> `Live.Envelope.EnvelopeEventControlCoefficients`

This class represents the cubic Bezier control points of an envelope event, defining the
interpolation curve shape between consecutive breakpoints.

??? note "Raw probe notes (temporary)"
    Probed via `events_in_range` after bridge serialization. All API-created steps produce
    the default `(0.5, 0.5, 0.5, 0.5)` (linear interpolation). The values represent two
    Bezier control points `(x1, y1)` and `(x2, y2)` normalized to the segment between
    consecutive events. Non-default values (curved automation) only appear from UI-drawn
    breakpoints.

### Properties

| Property | Type    | Settable | Listenable | Summary                            |
| -------- | ------- | -------- | ---------- | ---------------------------------- |
| `x1`     | `float` | no       | `no`       | First x-axis control coefficient.  |
| `x2`     | `float` | no       | `no`       | Second x-axis control coefficient. |
| `y1`     | `float` | no       | `no`       | First y-axis control coefficient.  |
| `y2`     | `float` | no       | `no`       | Second y-axis control coefficient. |

#### `x1`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

First Bezier control point x-coordinate. Together with `y1`, defines the departure tangent
from this event toward the next. Default 0.5 = linear interpolation.

#### `x2`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

Second Bezier control point x-coordinate. Together with `y2`, defines the arrival tangent
approaching the next event. Default 0.5 = linear interpolation.

#### `y1`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

First Bezier control point y-coordinate. Together with `x1`, defines the departure tangent
from this event toward the next. Default 0.5 = linear interpolation.

#### `y2`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

Second Bezier control point y-coordinate. Together with `x2`, defines the arrival tangent
approaching the next event. Default 0.5 = linear interpolation.

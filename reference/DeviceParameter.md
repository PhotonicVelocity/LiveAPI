# DeviceParameter

## DeviceParameter

This class represents an automatable parameter within a MIDI or audio device. Each device
exposes a list of parameters that can be read, set, automated, and observed. Parameters
have a value range (`min`/`max`), a display representation, and metadata about whether they
are quantized (boolean/enum) or continuous (float).

To modify a parameter, set its `value` property. Use `begin_gesture()`/`end_gesture()` to
group rapid value changes into a single undo step (e.g., when recording automation from a
physical knob).

### Sources

- **Primary:** `Live/classes/DeviceParameter.py` (stub dump)
- **Secondary:** `MaxForLive/deviceparameter.md`
- **Probes:** `probe_all_devices.py`, `probe_device_parameter.py`

### Probe Notes

- **`value` outside range raises** — setting a value above `max` or below `min` raises
  `InternalError: "Invalid value. Check the parameters range with min/max"`. It does NOT clamp.
- **`display_value` is read-only** — attempting to set it raises a signature mismatch error
  (the API expects float, not str). Despite the stub's "Get/Set" docstring, this property is
  effectively read-only. Use `value` to change the parameter.
- **`default_value` only for continuous** — works on non-quantized params (e.g. returned `1.0`
  for Drift LP Freq). On quantized params, raises `InternalError: "There is no default value
available for this type of parameter"`.
- **`short_value_items` works** — returned `['Off', 'On']` for a boolean parameter (same as
  `value_items` in this case). May differ for params with longer display names.
- **`str_for_value()` works** — `str_for_value(1.0)` returned `'20.0 kHz'` for Drift LP Freq.
- **`automation_state`** confirmed: returns `0` (none) for a parameter with no automation.

### Open Questions

- What `original_name` returns for non-macro parameters (the stub says "the original name,
  unaffected of any renamings" — but Max docs say "the name of a Macro parameter before its
  assignment"). Are these descriptions for different use cases?

### Properties

| Property            | Get Returns     | Set Accepts | Listenable | Available Since | Summary                                                                |
| ------------------- | --------------- | ----------- | ---------- | --------------- | ---------------------------------------------------------------------- |
| `automation_state`  | `int`           | —           | `yes`      | `<11`           | 0=none, 1=active, 2=overridden.                                        |
| `default_value`     | `float`         | —           | `no`       | `<11`           | Default value. Only for non-quantized parameters; raises on quantized. |
| `display_value`     | `str`           | —           | `yes`      | `12.2`          | Value as shown in the GUI (e.g. `"-12 dB"`, `"On"`). Read-only.        |
| `is_enabled`        | `bool`          | —           | `no`       | `<11`           | `False` if macro-mapped or disabled by Max.                            |
| `is_quantized`      | `bool`          | —           | `no`       | `<11`           | `True` for booleans and enums; `False` for continuous float.           |
| `max`               | `float`         | —           | `no`       | `<11`           | Upper bound of the allowed value range.                                |
| `min`               | `float`         | —           | `no`       | `<11`           | Lower bound of the allowed value range.                                |
| `name`              | `str`           | —           | `yes`      | `<11`           | Short parameter name as shown in automation chooser.                   |
| `original_name`     | `str`           | —           | `no`       | `<11`           | Original name before any renaming (e.g. macro assignment).             |
| `short_value_items` | `Sequence[str]` | —           | `no`       | `11.1`          | Short names for quantized values. Only if `is_quantized`.              |
| `state`             | `int`           | —           | `yes`      | `<11`           | 0=enabled, 1=irrelevant, 2=disabled.                                   |
| `value`             | `float`         | `float`     | `yes`      | `<11`           | Internal value between `min` and `max`.                                |
| `value_items`       | `Sequence[str]` | —           | `no`       | `<11`           | Display names for quantized values. Only if `is_quantized`.            |

#### `automation_state`

- **Get Returns:** `int` (`DeviceParameter.AutomationState`)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — returns `0` for param with no automation

**Description:**
The automation state of this parameter:

- `0` = no automation (no automation lane exists or it's empty)
- `1` = automation active (automation is playing back)
- `2` = automation overridden (user has manually moved the parameter, overriding automation)

Use `re_enable_automation()` to clear the override state (transition from 2 back to 1).

#### `default_value`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed`

**Description:**
The default value for this parameter. Only available for non-quantized parameters
(`is_quantized=False`). Accessing this on a quantized parameter raises
`InternalError: "There is no default value available for this type of parameter"`.

#### `display_value`

- **Get Returns:** `str`
- **Set Accepts:** — (read-only)
- **Listenable:** `yes`
- **Available Since:** `12.2`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — set attempt raises signature mismatch (read-only)

**Description:**
The parameter value formatted for display, as shown in the Live GUI. Includes unit suffixes
where applicable (e.g. `"-12.0 dB"`, `"440 Hz"`, `"On"`, `"1/16"`). Read-only despite the
stub's "Get/Set" docstring — attempting to set raises a type error. The Max docs list this
as observable. Use `str_for_value()` to format an arbitrary value without changing the
parameter.

#### `is_enabled`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` when the parameter's value can be modified directly by the user, automation, or MIDI
mapping. `False` when the parameter is macro-controlled, controlled by a `live.remote~`
object, or when Live has disabled it for other reasons. When `False`, setting `value` may
silently fail or raise — needs probing.

#### `is_quantized`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
`True` for boolean toggles and enum/menu parameters. `False` for continuous float parameters
(knobs, sliders). When `True`, use `value_items` to get the display names for each possible
value. Note: some parameters that appear quantized in the UI (e.g., MIDI pitch) actually
report `is_quantized=False` because their internal representation is continuous.

#### `max`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The upper bound of the allowed value range. `value` must be set within `[min, max]`.

#### `min`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The lower bound of the allowed value range. `value` must be set within `[min, max]`.

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The short parameter name as shown in the automation chooser and device parameter list.
For macro parameters, this is the user-assigned name. The listener fires when the name
changes (e.g., when a macro is reassigned).

#### `original_name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The original name of the parameter, unaffected by user renaming. For macro parameters, this
is the name before the macro was assigned to a target parameter. For non-macro parameters,
likely the same as `name`.

#### `short_value_items`

- **Get Returns:** `Sequence[str]`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.1`
- **Sources:** `stub`
- **Probe Status:** `confirmed` — returned `['Off', 'On']` for Device On param

**Description:**
Like `value_items`, but prefers short value names when available. Only valid when
`is_quantized=True` — raises an error otherwise. For simple boolean parameters, returns the
same values as `value_items`. May differ for parameters with longer display names. Not
documented in the Max for Live docs; appears only in the stub.

#### `state`

- **Get Returns:** `int` (`DeviceParameter.ParameterState`)
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The active state of the parameter:

- `0` = enabled — the parameter is active and can be changed.
- `1` = irrelevant — the parameter can be changed but isn't active, so changes won't have
  an audible effect (e.g., a parameter for a disabled feature within the device).
- `2` = disabled — the parameter cannot be changed.

#### `value`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — out-of-range raises, does not clamp

**Description:**
The internal value of the parameter, between `min` and `max`. Setting a value outside this
range raises `InternalError: "Invalid value. Check the parameters range with min/max"` — it
does **not** clamp. For quantized parameters, the value is an integer cast to float (e.g.,
`0.0` for off, `1.0` for on). For continuous parameters, the value is a float in the device's
internal scale (not the display scale). Use `display_value` or `str_for_value()` for the
human-readable representation.

#### `value_items`

- **Get Returns:** `Sequence[str]`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The list of display names for each possible value of a quantized parameter. Indexed by the
parameter's integer value. Only valid when `is_quantized=True` — raises an error otherwise.
For example, a filter type parameter might return `["LP12", "LP24", "BP6", "HP12", ...]`.

### Methods

| Signature                     | Returns | Available Since | Summary                                         |
| ----------------------------- | ------- | --------------- | ----------------------------------------------- |
| `begin_gesture()`             | `None`  | `<11`           | Begin a modification gesture for undo grouping. |
| `end_gesture()`               | `None`  | `<11`           | End a modification gesture.                     |
| `re_enable_automation()`      | `None`  | `<11`           | Clear automation override for this parameter.   |
| `str_for_value(value: float)` | `str`   | `<11`           | Format a value as a display string with units.  |

#### `begin_gesture()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A` (modifies undo behavior of subsequent value changes)
- **Side Effects:** Marks the beginning of a parameter modification group.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Notifies Live that a sequence of `value` modifications should be treated as a single gesture
(one undo step). Call this before rapidly setting `value` multiple times (e.g., when recording
automation from a physical knob or MIDI controller). Must be paired with `end_gesture()`.

#### `end_gesture()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Marks the end of a parameter modification group.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Ends a parameter modification gesture started by `begin_gesture()`. All value changes between
`begin_gesture()` and `end_gesture()` are grouped into a single undo step.

#### `re_enable_automation()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Clears the automation override state for this parameter.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Re-enables automation playback for this parameter after it has been manually overridden.
Transitions `automation_state` from `2` (overridden) back to `1` (active). No effect if
automation is not overridden. This is the per-parameter equivalent of
`Song.re_enable_automation()` which re-enables all overridden parameters.

#### `str_for_value(value: float)`

- **Returns:** `str`
- **Args:**
  - `value: float` — a value in the parameter's `[min, max]` range
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None (display only).
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `confirmed` — e.g. `str_for_value(1.0)` → `'20.0 kHz'` for LP Freq

**Description:**
Returns a string representation of the given value, formatted the same way Live displays it.
The returned string can include unit suffixes like `"dB"`, `"Hz"`, `"%"`, etc. Use this for
display purposes — to format an arbitrary value without actually changing the parameter.

# CuePoint

## CuePoint

This class represents a locator (marker) in Live's Arrangement View. CuePoints are
accessed via `Song.cue_points` and provide a name and a time position in beats. You can
call `jump()` on a CuePoint to move the playback position to that marker.

CuePoint is defined as an inner class of `Song` in the stub (`Song.CuePoint`), but is
documented as a standalone object in the Max for Live reference under
`live_set cue_points N`.

### Sources

- **Primary:** `Live/classes/Song.py` (stub dump -- inner class `Song.CuePoint`)
- **Secondary:** `MaxForLive/cuepoint.md`
- **Probes:** None

### Probe Notes

None yet.

### Open Questions

- Is `time` truly read-only, or can it be set via the Python API? The stub docstring says
  "Get/Listen" (no "Set"), and the Max docs say `read-only`. But it would be worth probing
  to confirm there is no hidden setter.
- What happens when calling `jump()` while recording in the Arrangement -- does it
  interrupt the recording or is the call ignored?
- Can `name` be set to an empty string? If so, how does the marker appear in the
  Arrangement View?
- Does the `cue_points` list on Song update immediately when a marker is created or
  deleted in the UI, or is there a listener delay?

### Properties

| Property | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                   |
| -------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------------- |
| `name`   | `str`       | `str`       | `yes`      | `<11`           | The display name of the locator as shown in the arranger. |
| `time`   | `float`     | —           | `yes`      | `<11`           | Arrangement position of the locator in beats.             |

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The display name of this locator as it appears in the Arrangement View. Read/write. The
listener fires when the name is changed, either via the API or through the Live UI.

#### `time`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The position of the locator in the Arrangement, measured in beats. Read-only according to
both the stub and the Max docs. The listener fires when the marker is moved in the
Arrangement View.

### Methods

| Signature | Returns | Available Since | Summary                                                                   |
| --------- | ------- | --------------- | ------------------------------------------------------------------------- |
| `jump()`  | `None`  | `<11`           | Move the playback position to this locator, quantized if song is playing. |

#### `jump()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Moves the current Arrangement playback position to this locator's time.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Moves the Arrangement playback position to this locator's time. If the Song is currently
playing, the jump is quantized (snapped to the global quantization grid). If the Song is
stopped, the start-playing position is moved directly to the locator's time without
quantization.

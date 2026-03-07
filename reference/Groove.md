# Groove

## Groove

This class represents a groove in Live. A groove applies timing, velocity, and randomization
offsets to MIDI clips. Each groove lives in the groove pool (`Song.groove_pool`) and can be
assigned to individual clips. Grooves control how rigidly or loosely notes align to a grid.

### Sources

- **Primary:** `Live/classes/Groove.py` (stub dump)
- **Secondary:** `MaxForLive/groove.md`
- **Probes:** MS 17 probing (2026-02-22, Live 12.3.5)

### Probe Notes

- All six properties confirmed readable. `name` returns `str` (e.g. `"Swing 16ths 66"`).
- `base` is settable via the Python API. `set("base", 3)` succeeded with no error.
  Readback confirmed the value was stored.
- Amount properties return `float`. Observed values: `timing_amount: 100.0`,
  `quantization_amount: 0.0`, `random_amount: 0.0`, `velocity_amount: 0.0`.
  Range appears to be 0.0–131.0, matching the Live UI percentage slider.
- `timing_amount` setter confirmed: `set("timing_amount", 100.0)` succeeded.
- `Clip.groove` returns a Groove handle when assigned, `None` when no groove is set.
  `Clip.has_groove` correctly reflects the state (`True`/`False`).
  The same handle OID appears in both `clip.get("groove")` and `groove_pool.grooves[0]` —
  they're the same object.
- `Clip.groove` is settable: `clip.set("groove", groove_handle)` works. However, clearing
  (setting to `None`) is **not possible** via the Python API. Exhaustive probing tried:
  `setattr(clip, 'groove', None)` (C++ type mismatch), `delattr(clip, 'groove')` (no deleter),
  null-handle construction via `Live.Groove.Groove()` ("cannot be instantiated from Python"),
  integer 0 / empty string / empty dict (type mismatches), `oid="0"` sentinel (invalid handle),
  clip methods `remove_groove`/`clear_groove`/`reset_groove` (don't exist),
  GroovePool methods `remove_groove`/`clear`/`remove` (don't exist).
  The Live UI can clear the groove via its "None" dropdown option, but this uses an internal
  C++ code path not exposed via the Python API. **Confirmed limitation.** A potential future
  workaround: ship an identity `.agr` file (all amounts 0.0) with the package and load it
  via `Browser.load_item()` as a "null groove" sentinel. Requires Browser access (unprobed).
- Groove type name in the bridge is `"Groove"`.

### Open Questions

- ~~Can `name` be set to an arbitrary string?~~ **Resolved:** Yes. `set("name", "Test Custom Name")`
  succeeded and read back correctly. The name is not locked to the `.agr` file name.
- ~~Does setting `name` rename the groove in the groove pool UI?~~ **Resolved:** Yes, the groove
  pool UI shows the updated name immediately.

### Properties

| Property              | Get Returns | Set Accepts | Listenable | Available Since | Summary                                             |
| --------------------- | ----------- | ----------- | ---------- | --------------- | --------------------------------------------------- |
| `base`                | `int`       | `int`       | `no`       | `<11`           | Base grid for the groove (index-based enum).        |
| `name`                | `str`       | `str`       | `yes`      | `<11`           | Display name of the groove.                         |
| `quantization_amount` | `float`     | `float`     | `yes`      | `<11`           | How much the groove's quantization is applied.      |
| `random_amount`       | `float`     | `float`     | `yes`      | `<11`           | How much random timing variation is applied.        |
| `timing_amount`       | `float`     | `float`     | `yes`      | `<11`           | How much the groove's timing offsets are applied.   |
| `velocity_amount`     | `float`     | `float`     | `yes`      | `<11`           | How much the groove's velocity offsets are applied. |

#### `base`

- **Get Returns:** `int`
- **Set Accepts:** `int`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The base grid that the groove pattern is built on, expressed as an index:
`0` = 1/4, `1` = 1/8, `2` = 1/8T (triplet), `3` = 1/16, `4` = 1/16T (triplet), `5` = 1/32.
Probing confirmed both get and set work. Observed value `3` (= 1/16) for "Swing 16ths 66".

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** `str`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The display name of the groove as shown in the groove pool. Probing returned
`"Swing 16ths 66"` (str). The listener fires when the name changes.

#### `quantization_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Controls how much quantization the groove applies. Higher values push notes closer to the
groove's quantization grid. Range is 0.0–131.0 (matching the UI percentage). Probing returned
`0.0`. The listener fires when this amount changes.

#### `random_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Controls how much random timing variation the groove introduces. Higher values add more
randomness to note positions. Range is 0.0–131.0. Probing returned `0.0`. The listener fires
when this amount changes.

#### `timing_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Controls how much of the groove's timing offsets are applied to notes. At full value, notes
are shifted to match the groove's timing pattern exactly. Range is 0.0–131.0. Probing returned
`100.0`. Both get and set confirmed working. The listener fires when this amount changes.

#### `velocity_amount`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
Controls how much of the groove's velocity offsets are applied to notes. Higher values make
the velocity pattern of the groove more pronounced. Range is 0.0–131.0. Probing returned `0.0`.
The listener fires when this amount changes.

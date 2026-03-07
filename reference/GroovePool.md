# GroovePool

## GroovePool

This class represents the groove pool in Live. The groove pool is a set-level container that
holds all grooves available in the current Live Set. It is accessed via `Song.groove_pool`.
Individual grooves can be assigned to clips to affect their timing, velocity, and
randomization.

### Sources

- **Primary:** `Live/classes/GroovePool.py` (stub dump)
- **Secondary:** `MaxForLive/groovepool.md`
- **Probes:** MS 17 probing (2026-02-22, Live 12.3.5)

### Probe Notes

- `song.groove_pool` returns a `RemoteObject(type=GroovePool)` — accessed via `get` (property,
  not child). Bridge type name is `"GroovePool"`.
- `groove_pool.grooves` returns a list of Groove handles via standard `children()` call.
  Probing returned 1 groove (the "Swing 16ths 66" groove loaded in the test set).
- Groove handle OIDs are stable: `clip.get("groove")` and `groove_pool.grooves[0]` return
  the same OID, confirming identity.
- Grooves are shared objects — all clips referencing the same groove see the same handle.
  Changing a groove's properties (e.g. `timing_amount`) affects all clips that use it.
- The pool holds in-memory copies imported from `.agr` files. Modifying groove properties
  only affects the current Live Set, not the source `.agr` file on disk.
- No direct API to add or remove grooves from the pool. Probed `add`, `create`,
  `add_groove`, `create_groove`, `append`, `insert` on GroovePool and `add_groove`,
  `create_groove`, `load_groove` on Song — none exist. It may be possible to load `.agr`
  files via `Browser.load_item()` (unprobed — Browser is on `Application`, not yet
  accessible through the bridge). Otherwise the pool is only populated through the Live UI.

### Open Questions

- Does the `grooves` listener fire when a groove's internal properties change (e.g. its
  `timing_amount`), or only when grooves are added/removed from the pool? (Not tested.)

### Children

| Child     | Returns            | Shape  | Access | Listenable | Available Since | Summary                                   |
| --------- | ------------------ | ------ | ------ | ---------- | --------------- | ----------------------------------------- |
| `grooves` | `Sequence[Groove]` | `list` | `get`  | `yes`      | `<11`           | All grooves currently in the groove pool. |

#### `grooves`

- **Returns:** `Sequence[Groove]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed`

**Description:**
The list of all grooves in the groove pool, ordered from top to bottom as shown in the groove
pool panel. The listener fires when grooves are added to or removed from the pool. Each
element is a `Groove` object with its own timing, velocity, quantization, and randomization
parameters. Probing confirmed standard `children()` access returns Groove handles.

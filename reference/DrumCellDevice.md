# DrumCellDevice

## DrumCellDevice

This class represents a Drum Cell (Drum Sampler) device in Live. DrumCellDevice is a
subclass of Device -- it has all the children, properties, and methods of Device plus
one additional property for the sample gain level.

A DrumCellDevice appears as the built-in sampler inside each Drum Rack pad cell. It is not
directly insertable — it is automatically created when a sample is loaded into a Drum Rack pad.

### Sources

- **Primary:** `Live/classes/devices/DrumCellDevice.py` (stub dump)
- **Secondary:** `MaxForLive/drumcelldevice.md`
- **Probes:** `tools/probes/probe_device_subclasses_trivial.py`, `tools/probes/probe_drum_cell2.py`

### Probe Notes

- Bridge type: `"DrumCellDevice"` (inferred from `type(obj).__name__` pattern; not directly probed
  because DrumCellDevice requires a sample loaded in a Drum Rack pad, which cannot be done
  programmatically via the current API).
- The stub confirms `gain` has no setter — it is read-only with a listener.
- DrumCellDevice is not insertable via `insert_device`. It appears automatically inside a Drum Rack
  pad chain when a sample is loaded into that pad.
- Empty Drum Rack pads have no chains and no devices.

### Open Questions

- Exact range of `gain` not probed (requires a loaded sample). Presumed 0.0–1.0 based on Max docs.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
DrumCellDevice adds:

| Property | Get Returns | Set Accepts | Listenable | Available Since | Summary                       |
| -------- | ----------- | ----------- | ---------- | --------------- | ----------------------------- |
| `gain`   | `float`     | —           | `yes`      | `12.1`          | The sample gain (normalized). |

#### `gain`

- **Get Returns:** `float`
- **Set Accepts:** — (read-only per stub; no setter method exists)
- **Listenable:** `yes`
- **Available Since:** `12.1`
- **Sources:** `stub | max`
- **Probe Status:** `partially probed` (not runtime-probed due to sample requirement)

**Description:**
The sample gain level as a normalized value (presumably 0.0 to 1.0). The listener fires
when the gain value changes. Read-only — the value reflects the current gain setting in
the Drum Cell UI but cannot be changed programmatically.

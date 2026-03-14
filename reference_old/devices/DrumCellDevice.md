# DrumCellDevice

> `Live.DrumCellDevice.DrumCellDevice`

This class represents a Drum Cell (Drum Sampler) device in Live. DrumCellDevice is a subclass of Device -- it
has all the children, properties, and methods of Device plus one additional property for the sample gain level.

A DrumCellDevice appears as the built-in sampler inside each Drum Rack pad cell. It is not directly
insertable — it is automatically created when a sample is loaded into a Drum Rack pad.

??? note "Raw probe notes (temporary)"
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

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), DrumCellDevice adds:

| Property | Type    | Settable | Listenable | Summary                       |
| -------- | ------- | -------- | ---------- | ----------------------------- |
| `gain`   | `float` | no       | yes        | The sample gain (normalized). |

#### `gain`

- **Type:** `float`
- **Listenable:** yes
- **Since:** `12.1`

The sample gain level as a normalized value (presumably 0.0 to 1.0). The listener fires when the gain value
changes. Read-only — the value reflects the current gain setting in the Drum Cell UI but cannot be changed
programmatically.

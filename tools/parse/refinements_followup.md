# Manual Refinements — Follow-up Backlog

Items to revisit when better evidence becomes available — runtime probes, fresh
captures of M4L-only classes, or corpus updates.

## Needs runtime probe (currently medium-confidence on docstring/M4L only)

These probed_type / arg_type / return_type entries currently rely on M4L docs or
docstring inference, with no corpus usage to corroborate. A probe pass against a
running Live could promote them to `high` (or surface contradictions).

### `PythonLicensingBridge` cluster (M4L-only class, can't reach from Remote Scripts)

- `Live.Licensing.PythonLicensingBridge.base_product_id` → `str`
- `Live.Licensing.PythonLicensingBridge.in_sassafras_mode` → `bool` _(currently low: name pattern only)_
- `Live.Licensing.PythonLicensingBridge.license_must_match_variant` → `bool`
- `Live.Licensing.PythonLicensingBridge.random_number_for_trial_authorization` → `int`
- `Live.Licensing.PythonLicensingBridge.set_has_unsaved_changes` → `bool`
- `Live.Licensing.PythonLicensingBridge.get_startup_dialog` arg_types
- `Live.Licensing.PythonLicensingBridge.process_license_response` arg_types
- `Live.Licensing.PythonLicensingBridge.set_network_timer` arg_types
- `Live.Licensing.get_unlock_dir` → `tuple[str, bool]`

**To probe**: write a small probe that constructs a `PythonLicensingBridge` instance
(if possible from a Control Surface context) and reads each property. The class
appears to be M4L-only — may require a small M4L probe device per the architecture
doc on the behavioral-pipeline branch.

### `ListenerHandle` (internal API, no corpus usage)

- `Live.Listener.ListenerHandle.listener_func` → `Callable`
- `Live.Listener.ListenerHandle.listener_self` → `Any`
- `Live.Listener.ListenerHandle.name` → `str`

**To probe**: register a listener via `add_X_listener(callback)` and inspect the
returned ListenerHandle's properties. Should be reachable from a Control Surface.

### `ControlSurfaceProxy.pad_layout` and `type_name`

- `Live.Application.ControlSurfaceProxy.pad_layout` → `str` (M4L doc: "symbol read-only")
- `Live.Application.ControlSurfaceProxy.type_name` → `str` (no doc, name suggests)

ControlSurfaceProxy is M4L-only (see baseline notes). Same probe context as Licensing.

## Type-correction candidates that need verification

These were mistakes corrected in the research pass — verify them by probe when
possible to upgrade from `high` (currently set to high based on baseline notes that
were themselves probed in MS33).

- `Live.Conversions.move_devices_on_track_to_new_drum_rack_pad` — corrected `Track` →
  `DrumPad | None` based on baseline probe (MS33). A fresh probe against current Live
  would seal it.
- `Live.Song.Song.find_device_position` / `Live.Song.Song.move_device` — corrected
  `Track | Chain` → `LomObject` based on baseline. Probe could pin down whether the
  binding accepts arbitrary `LomObject` or has internal narrowing (only Track / Chain /
  DrumChain / RackDevice etc.).

## Type-fixes left at `medium` — strong-but-not-runtime evidence

These have plausible types from baseline docs / M4L docs but no probe data to lock
them down. Lower priority; revisit if drift surfaces.

- `Live.Track.Track.create_take_lane` → `TakeLane` — baseline lists `LomObject`
  return; LLM said `TakeLane`; P4L wrapper uses `TakeLane`. Likely correct but the
  C++ binding apparently exposes as LomObject. Probe to confirm.
- `Live.Track.Track.insert_device` → `Device` — baseline lists `LomObject` return;
  same situation as create_take_lane.
- `Live.Chain.Chain.insert_device` → `Device` — same.
- `Live.Clip.Clip.duplicate_notes_by_id.destination_time` → `float | None`.

## Resolution shape

When a probe lands on any of these, update the entry's:

- `confidence: high` (if probed value matches the recorded type)
- `source` line citing the probe date and what was observed
- `from:` field in the {from, to} dict, if appropriate (records what the probe-
  observed value was)

Then remove the entry from this file.

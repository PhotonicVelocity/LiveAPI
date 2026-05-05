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

**To probe**: write a small probe that constructs a `PythonLicensingBridge` instance
(if possible from a Control Surface context) and reads each property. The class
appears to be M4L-only — may require a small M4L probe device per the architecture
doc on the behavioral-pipeline branch.

### `ListenerHandle` (internal-only, not reachable from a Control Surface)

- `Live.Listener.ListenerHandle.listener_func` → `Callable`
- `Live.Listener.ListenerHandle.listener_self` → `Any`
- `Live.Listener.ListenerHandle.name` → `str`

There is no public path to obtain a `ListenerHandle` instance from a Control
Surface context: all 367 `add_*_listener` methods return `None`, the class's
`init_doc` says *"This class cannot be instantiated from Python"*, no Live
property exposes a `ListenerVector`, and zero corpus usage exists. The class
appears in the capture's `dir()` walk but instances are private to Live's
internal machinery.

Not actionable until either (a) Live exposes a public accessor, or (b) the
behavioral-probe pipeline can hook into Live's internal listener registry to
intercept handle creation.

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
- `Live.Song.Song.find_device_position` / `Live.Song.Song.move_device` — parser
  resolves the `target` arg to `LomObject` from the C++ signature (no refinement
  needed). Baseline confirms LomObject is correct (accepts any device-container).
  A probe could pin down whether the binding has internal narrowing (only Track /
  Chain / DrumChain / RackDevice, etc.) — would let us tighten the type if so.

## Type-fixes left at `medium` — strong-but-not-runtime evidence

These have plausible types from baseline docs / M4L docs but no probe data to lock
them down. Lower priority; revisit if drift surfaces.

- `Live.Track.Track.create_take_lane` → `TakeLane` — baseline lists `LomObject`
  return; M4L docs say "Creates a take lane for this track"; P4L wrapper uses
  `TakeLane`. Likely correct but the C++ binding apparently exposes as
  `LomObject`. Probe to confirm.
- `Live.Track.Track.insert_device` → `Device` — baseline lists `LomObject` return;
  same situation as create_take_lane.
- `Live.Chain.Chain.insert_device` → `Device` — same.
- `Live.Clip.Clip.duplicate_notes_by_id.destination_time` → `float | None`.

### `map_midi_*_with_feedback_map` — feedback_rule nullability (REMOVED, may re-add)

Three sister functions previously had a `feedback_rule: T -> T | None` widening:

- `Live.MidiMap.map_midi_cc_with_feedback_map` — `CCFeedbackRule | None`
- `Live.MidiMap.map_midi_note_with_feedback_map` — `NoteFeedbackRule | None`
- `Live.MidiMap.map_midi_pitchbend_with_feedback_map` — `PitchBendFeedbackRule | None`

Originally tagged `high` based on an audit that read `feedback_rule = None` at
the top of `_install_mapping` in `_Framework/ControlSurface.py` and
`ableton/v2/control_surface/control_surface.py` as "None passed at runtime."
On re-read, the variable is reassigned to a concrete `*FeedbackRule` in all
reachable paths before any dispatch call — and the immediately-preceding
`feedback_rule.channel = ...` would AttributeError on None. No corpus call site
across all 11 files passes a literal None.

Widenings **removed** rather than downgraded — the stub is now strictly typed
on these args, matching the corpus's actual usage. Re-add `T | None` only after
a runtime probe confirms the binding accepts None — e.g., a small P4L
integration test that calls one of these with `feedback_rule=None` and observes
no exception. (The cc entry has no other refinements and was removed entirely
from `manual_refinements.yaml`; note + pitchbend keep their arg-name renames.)

### `Clip.apply_note_modifications` — strict `MidiNoteVector` arg

This method's C++ signature literally takes `vector<NClipApi::TNoteInfo>`, so
the binding rejects anything that isn't a `MidiNoteVector` instance. The stub
already reflects this (parser resolves the C++ type directly).

The cluster of five `*_notes_by_id` / `add_new_notes` methods that previously
sat in this section was *not* the same shape — those C++ signatures are
`boost::python::api::object` (generic, runtime-checked), and corpus evidence
shows they accept tuples / lists / dict_keys. They've been refined to
`Iterable[T]` and removed from this list.

A future probe could exercise `apply_note_modifications` directly — call it
with a list, a tuple, a generator, and a `MidiNoteVector` to enumerate exactly
which of those raise `InternalError` vs. work. Today the stub is conservative
(strict `MidiNoteVector`) which matches reported behavior.

## Resolution shape

When a probe lands on any of these, update the entry's:

- `confidence: high` (if probed value matches the recorded type)
- `source` line citing the probe date and what was observed
- `from:` field in the {from, to} dict, if appropriate (records what the probe-
  observed value was)

Then remove the entry from this file.

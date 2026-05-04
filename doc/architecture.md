# Architecture: Behavioral Pipeline

> Status: draft. Captures the rethink that follows the project pause. Supersedes parts of `plan.md` and
> `decisions.md` as the implementation lands.

## What this document is

LiveAPI ships two products from one runtime introspection pipeline:

1. **Typed stubs** (`stubs/<version>/Live/`) — for any Remote Script / Max for Live / external-client author
   who wants autocomplete and static analysis.
2. **Browsable reference** (`reference/`, published via MkDocs) — general guidance for Remote Script authors
   and the source-of-truth input for downstream consumers like PythonForLive's typed wrappers.

The static surface (types, settability, listenability, signatures) is solved end-to-end by the existing
`tools/run_pipeline.py`. What stalled — and what this document re-architects — is the **behavioral surface**:
the per-member metadata that explains _how_ a property or method behaves at runtime.

The end goal of the project isn't a schema or a sidecar file. It's a **clear methodology for determining,
recording, and verifying how Live behaves**, applied consistently across every member surfaced in the
reference. The schema is one expression of that methodology; the probe is another; the published reference
is the third. All three exist to make the methodology repeatable, defensible against drift across Live
versions, and honest about its own confidence.

## The developer loop

The architecture is shaped by a specific recurring workflow — every other design choice in this document
flows out of it:

1. **Trigger.** Working in PythonForLive (or another Remote Script project), an oddity surfaces or a
   behavior needs to be confirmed — _"does setting `Clip.warping` while playing pause anything?", "is
   `Song.tempo` actually undo-tracked?", "what raises when I add a warp marker past clip end?"_
2. **Delegate.** The question is handed to Claude along with whatever P4L context made it surface.
3. **Probe.** Claude switches into LiveAPI and uses the probe harness to investigate. Each investigation
   produces or amends a **hypothesis** in the structured sidecar — an invariant, operation rule, side
   effect, etc.
4. **Publish.** Once the hypothesis is verified, the reference markdown is regenerated. The answer is now
   public on the reference site, and any consumer (P4L, other Remote Script authors, future-me) can cite it.
5. **Defend.** When Live ships a new version, the same probe re-runs against the new runtime. If the
   hypothesis still holds, nothing changes. If it doesn't, drift is flagged — the reference docs surface
   the mismatch and somebody (Claude, on request) re-investigates.

This loop has implications that the rest of the document carries:

- **Per-member probe entry point.** Step 3 must run for a single hypothesis on demand, not only as part of
  the per-version pipeline. The probe harness needs an `--only <member>` (or equivalent) mode from Slice 1
  on. Without it, the cold-path workflow is unusable.
- **Hypothesis sidecar is the editable artifact.** Step 3 _is_ "edit the sidecar"; step 4 generates from
  it. There is no separate "now write the docs" step — that decoupling is what burned the previous attempt.
- **Stable, citable URLs.** Step 4 publishes to a known reference path. P4L code, docstrings, and design
  notes link to a specific quirk / invariant / operation rule rather than copying prose. The reference site
  becomes the canonical citation surface.
- **Drift is first-class.** Step 5 is built into the per-version pipeline (Stage 4 below). Verification
  failures produce a report, not a silent skip; the report is the input to the next round of investigation.
- **Cold path and warm path share code.** "Investigate something new" (cold, single hypothesis) and
  "re-verify on a new version" (warm, all hypotheses) hit the same probe code at different entry points
  and produce different reports. The harness designs for both.

## The behavioral surface

Six dimensions per property / method. The first four are "what changes when this is touched"; the last two
are "what's always true and what can't happen."

| Dimension         | What it captures                                                | Automation tier                              |
| ----------------- | --------------------------------------------------------------- | -------------------------------------------- |
| `async_class`     | When does a mutation become readable? `immediate` / `next_tick` | Auto with state setup                        |
| `undo_tracked`    | Does the action enter Live's undo stack?                        | Auto, cheap                                  |
| `side_effects`    | Which other things change when this changes?                    | Auto-with-caveats (state-gated, prefs-gated) |
| `invariants`      | Predicates that always hold over object/collection state        | Auto, post-mutation                          |
| `operation_rules` | Per-method `precondition → outcome` (raises / no-ops / effect)  | Auto with state setup                        |
| `notes`           | Type-level quirks, prose, anything not structurally testable    | Human-only                                   |

These are independent dimensions; each member has its own answer for each. The split between `side_effects`,
`invariants`, and `operation_rules` is driven by the [warp markers case study](#case-study-warp-markers)
below — without it, three different concerns collapse into "side_effects" or "notes" and lose their
verifiability.

## Case study: warp markers

Warp markers are the sharpest test of whether the schema captures what the reference docs need to say. They're
audio-clip-only, controlled by three methods (`add_warp_marker`, `move_warp_marker`, `remove_warp_marker`) plus
a get-only collection (`warp_markers`), and Live enforces a small but interlocking set of rules across them.

### What we know (probed against Live 12.3.5)

1. `warp_markers` is a get-only `WarpMarkerVector`, listenable, audio-clip-only.
2. The last entry is an internal **phantom marker** ~1/32 beat past the last visible marker. The Live UI doesn't
   show it. `move_warp_marker` and `remove_warp_marker` raise when called on its `beat_time`.
3. `WarpMarker.sample_time` is in **seconds** despite the field name (vs. `beat_to_sample_time()` which returns
   samples — collision worth flagging).
4. `WarpMarker(sample_time, beat_time)` constructor is positional-only, with `sample_time` first.
5. All three mutation methods are immediate-visibility, undo-tracked, and fire the `warp_markers` listener.
6. `add_warp_marker(m)` has four conditional outcomes:
   - `m.sample_time` exceeds clip duration → raises `Warp marker sample time is out of range`.
   - A marker exists at `m.beat_time` with a **different** `sample_time` → raises `Segment length out of range`.
   - A marker exists with the **same** `(beat_time, sample_time)` → silent no-op.
   - The resulting segment BPM is outside `[5, 999]` → raises `Segment length out of range`.
7. `move_warp_marker(beat_time, distance)` raises if no marker exists at `beat_time` or if the move would create
   an invalid segment.
8. `remove_warp_marker(beat_time)` raises if no marker exists at `beat_time`.
9. **Slope rule.** For every adjacent pair of markers (including the phantom), the segment's local BPM —
   `(beat_delta / sample_delta_seconds) × 60` — must lie in `[5, 999]`, and both `beat_time` and `sample_time`
   must strictly increase across the pair. The "Segment length out of range" raises in `add_warp_marker` and
   `move_warp_marker` are consequences: Live rejects the operation when it would force any adjacent segment
   into violation. So is the rule that `add` rejects same-`beat_time`/different-`sample_time` (a degenerate
   zero-beat-distance segment, infinite slope).

### What the schema catches and what it misses

| Fact                                          | Captured by                                            |
| --------------------------------------------- | ------------------------------------------------------ |
| 1, 4 (types, signatures)                      | Stubs                                                  |
| 5 (immediate, undo-tracked, listener fan-out) | `async_class`, `undo_tracked`, `side_effects`          |
| 3 (units quirk)                               | `notes`                                                |
| 2 (phantom marker is the last entry)          | **`invariants`** — without it, this is mush in `notes` |
| 9 (slope rule on adjacent segments)           | **`invariants`** — predicate over collection state     |
| 6a / 6b / 6d, 7, 8 (per-method failure modes) | **`operation_rules`** — same reason                    |
| 6c (silent no-op on exact duplicate)          | **`operation_rules`**                                  |

Both missing categories are testable, not just prose, which is what makes them worth promoting from `notes`:

### Invariants

Predicates that hold over object/collection state, independent of which mutation just happened. The probe
verifies them opportunistically — after any mutation in a probe session, snapshot the affected collection and
re-evaluate.

```json
[
  {
    "id": "warp_markers_phantom_last",
    "applies_to": "Live.Clip.Clip.warp_markers",
    "predicate": "len(value) >= 2 and value[-1].beat_time > value[-2].beat_time",
    "description": "The last entry is a phantom marker ~1/32 beat past the last visible marker."
  },
  {
    "id": "warp_markers_slope_in_range",
    "applies_to": "Live.Clip.Clip.warp_markers",
    "predicate": "all(5 <= 60 * (b.beat_time - a.beat_time) / (b.sample_time - a.sample_time) <= 999 for a, b in pairs(value))",
    "description": "Every adjacent segment's derived local BPM is within Live's playable range [5, 999]."
  },
  {
    "id": "warp_markers_strictly_monotonic",
    "applies_to": "Live.Clip.Clip.warp_markers",
    "predicate": "all(b.beat_time > a.beat_time and b.sample_time > a.sample_time for a, b in pairs(value))",
    "description": "Markers strictly increase in both beat_time and sample_time — no zero/negative-length segments."
  }
]
```

### Operation rules

Per-method `(precondition → outcome)` tuples. The probe sets up the precondition, attempts the call, observes
outcome (raise text, no-op, or successful effect), and reports match / mismatch.

```json
{
  "method": "Live.Clip.Clip.add_warp_marker",
  "rules": [
    {
      "id": "exact_duplicate_noop",
      "precondition": "marker exists with matching (beat_time, sample_time)",
      "outcome": "no-op (no exception, no listener fire)"
    },
    {
      "id": "duplicate_beat_diff_sample_raises",
      "precondition": "marker exists at beat_time with different sample_time",
      "outcome": "raises 'Segment length out of range'"
    },
    {
      "id": "bpm_out_of_range_raises",
      "precondition": "resulting segment BPM ∉ [5, 999]",
      "outcome": "raises 'Segment length out of range'"
    },
    {
      "id": "sample_overflow_raises",
      "precondition": "m.sample_time > clip.sample_length / clip.sample_rate",
      "outcome": "raises 'Warp marker sample time is out of range'"
    }
  ]
}
```

Operation rules also drive natural reference content — each rule renders as a Quirks or Raises bullet.

### Invariants and operation rules are linked

The slope rule shows it: `bpm_out_of_range_raises` and `duplicate_beat_diff_sample_raises` (an infinite-slope
segment) and most of the `move_warp_marker` failure modes are all the **same underlying invariant** rejected at
different mutation entry points. Live can't violate the slope rule, so any mutation that would force violation
is rejected.

This is a useful pattern when filling in the schema:

1. Identify the invariant first (one per state-shape rule).
2. Trace each method's rejection cases back to which invariant they protect.
3. Operation rules can then reference an invariant by ID rather than re-stating the predicate, and the probe
   gets a single failure point if the invariant ever changes between Live versions.

The schema doesn't have to enforce this linkage in Slice 4/5 — but writers should be prompted to look for an
invariant before writing N independent operation rules that each duplicate the same predicate inline.

### What the case study implies

- The schema is six dimensions, not four. `invariants` and `operation_rules` are the missing ones; both are
  verifiable, not prose.
- Each new dimension expands what kinds of hypotheses the system can express, which expands what kinds of
  members can be reference-rendered. Warp markers specifically need `invariants` and `operation_rules` to be
  fully captured.
- The slice plan below uses members as units, not dimensions. Warp markers come in as the slice that adds
  invariants and operation rules, not as a final mop-up.

## What the previous attempt got wrong

The original probe approach tried to **discover** all behavioral dimensions exhaustively for every member, with
one probe pass producing authoritative truth. That doesn't terminate, because:

- Many mutations are silently ignored unless preconditions hold (`Song.overdub` requires an armed track;
  `Song.record_mode` is gated by a preference).
- Side-effect graphs depend on session vs arrangement state, on which view is open, on what's selected.
- Async timing depends on the scheduler tick the test ran against.
- The combinatorics across `class × member × precondition` blow up.

Outcome: noisy partial graphs, unclear what was bug vs missing-precondition, and an open-ended exploration
with no defined done-state. The complexity here is what stalled the project.

## Concrete failure modes on `integrate-targeted-probes`

The unmerged branch `integrate-targeted-probes` (tip `a6c878c`) is the previous attempt's stall point. It
produced real probe output (`ProbeResults.json` for ~4 classes, validating the schema shape) but never landed
on main. Reading the branch corroborates the abstract failures above with specifics worth naming — each one
becomes a design rule for the new attempt.

- **Schema thrash mid-build.** The `effect` field on method probes was rewritten across ~20 commits — first
  treated as one side-effect among many, then promoted to a primary measurement, then re-parameterized with
  `effect_obj` for cross-object cases (`b8ba118`, `410fd19`, `0b54259`, `c3e2932`, …). Each rewrite cascaded
  into `probe_method()` changes, parameter renames (`effect` vs `_effect_cls`), and downstream merger updates.
  **Rule:** lock the per-dimension schema before any probe code lands. If the schema needs a change, that's
  its own slice; you don't refactor the probe and the merger and the renderer in flight.

- **Preconditions scattered inline.** "Fire a scene, then probe `Song.back_to_arranger`, then reset playhead"
  lived as procedural setup inside probe scripts. Every new precondition added per-class probe code, and the
  same setup got duplicated across `probe_song.py` and `probe_track.py` with subtle drift.
  **Rule:** preconditions are declarative data, not code. A precondition table keyed by member, consumed by
  a single resolver, separate from the probe driver.

- **Per-class boilerplate not abstracted.** `probe_song.py` and `probe_track.py` total 1,246 LOC for two
  classes. The structural skeleton (set up listeners → discover props → loop properties → loop methods → write
  JSON) is identical between them; the variation is just data — which properties, which methods, which
  preconditions. `_probe_base.py` extracted utility primitives but not the loop itself.
  **Rule:** one probe driver, data tables per class. A class isn't a script; it's a row in a table.

- **Cascading state restoration as a kludge.** `restore_side_effects()` runs up to 3 iterations to chase
  listener-driven cascades, with `is_playing` special-cased to stop first (`f0959f7`). Each new probe
  surfaced a new restoration edge case patched in place.
  **Rule:** state restoration is best-effort. If a probe drifts Live's state, the next probe re-snapshots
  from where things actually are; we don't try to put Live back to pristine. Order probes to minimize
  cross-contamination instead of cleaning up after each one.

- **Decoupled producer and consumer.** `merge_behavioral_data` in `parse_apicapture_results.py` and
  `stamp_behavioral.py` both walk the parsed tree with copy-pasted node-finding logic. The reference
  generator on `claude/generate-reference-docs-4l248` hard-codes shape assumptions about `effect.label`,
  `side_effects[*].prop`, etc. — silent breakage if the probe output schema drifts.
  **Rule:** single stamping function, schema-validated between layers. Probe output is validated against the
  locked schema before merge; merge happens in one place; reference render reads the merged tree, not the raw
  probe output.

### What we'll salvage cleanly

From `_probe_base.py` (~644 LOC) the well-factored primitives survive a redesign without modification:
`fuzzy_eq()`, `json_safe()`, `_seq_key()`, `discover_listenable()`, `discover_snapshot_props()`,
`setup_listeners()` / `teardown_listeners()` (lifecycle only — the closure-mutating callbacks they install
get redesigned), `ptr_set()`, `find_new_index()`. The two-phase generator yield pattern (snapshot → mutate →
yield tick → check state) is sound. The branch is a parts donor for these; everything else gets rebuilt
against the new framing.

### What this means for Slice 1

The probe itself was never the hard part on the previous attempt — the orchestration was. Slice 1's
deliverable is **the contracts**, not the data:

1. The locked hypothesis spec format (one struct, validated). Covers a simple property: action, named
   targets, expected change, prose. No invariants or operation rules yet.
2. The precondition table format. Trivial members may need none, but the table exists from day one so
   later slices extend it instead of inventing it.
3. The single stamping function that validates probe output against the spec format and merges into the
   reference tree.
4. The cold-path `--only <member>` entry point so investigations can run one hypothesis at a time.
5. A reference render path that reads the merged tree, not the raw probe output.

If any of those five pieces feels hand-wavy when Slice 1 starts, stop and resolve before writing probe code.
The previous attempt wrote probe code first and let the contracts emerge; that's what produced the schema
thrash and the dual merging paths.

## The inversion: verify hypotheses, don't discover

The new architecture is **hypothesis-verify**, not **discover**:

1. Humans (or seeded data migrated from the existing curated `doc/live-api/` baseline) record their best guess
   for each member's behavioral dimensions in a structured sidecar.
2. The probe doesn't try to discover those values. It **checks them** against the running Live and reports
   `verified` / `mismatch` / `unprobed-precondition-not-met`.
3. Members not yet hypothesized appear in reference docs as honestly unprobed. They don't block release.
4. When Live ships a new version, the probe re-verifies the hypotheses and flags drift.

This inverts the burden. Humans seed once; automation defends forever. The done-state is well-defined per
member.

## Methodology: hypothesis names targets explicitly

The previous attempt's specific stall point: side-effect probing tried to **discover** what fired by hooking
listeners on everything, mutating, and attributing whatever fired. That produced false positives (passive-tick
noise), state-dependent flapping (a fire only happens when a preference is enabled), and an open-ended cleanup
loop (cascading restoration). The fix is structural: **the probe doesn't sweep, it asks specific questions.**

### The shape of a hypothesis

A hypothesis names exactly:

1. The member being probed (`Live.Song.Track.delete_clip`).
2. The action performed on it (call signature and arguments, or property assignment).
3. The **named targets** whose state or listener firing is asserted on, with the expected change ("becomes
   `null`", "fires within 2 ticks", "raises `Segment length out of range`").
4. The precondition under which the assertion holds, if any (`"track_armed"`,
   `"pref.auto_clip_switch_on_delete = true"`).
5. The prose description that becomes the reference text.

The probe takes the hypothesis, sets up the precondition, performs the action, and **checks just the named
targets**. Anything else that happens in Live during the probe is invisible to the verifier. Either the named
assertions hold or they don't — binary, deterministic, no attribution problem.

### Discovery is human / LLM judgment, not algorithm

The natural follow-up: how does the hypothesis come to know about a target like "playback starts" in the
first place? The answer is iterative refinement during cold-path investigation:

1. Write the hypothesis covering what's expected (`delete_clip` removes the clip, undo-tracked, immediate).
2. Run the probe. It verifies what's named.
3. **Look at Live during the probe** (manually, or via a dedicated investigation tool that snapshots state
   liberally). Notice playback started.
4. Amend the hypothesis to add `"$song.is_playing becomes true within 2 ticks"` as a named target.
5. Re-run. The new assertion now either verifies or fails.
6. Notice it only fires when a certain preference is enabled. Add the precondition. Re-run with both states.

The "smarts" — figuring out what to assert next — live in the human or LLM doing the investigation, not in
the probe driver. The driver verifies what's named; nothing more, nothing less. This is the explicit reversal
of the previous attempt's "broad-listener catch-everything" reflex.

The probe harness can offer an optional **investigation mode** that snapshots widely (every listenable
property on the relevant objects) and shows the diff to the human — but that output is _input to the human's
hypothesis writing_, not a value that gets ingested into the schema. The verified record only ever contains
what was deliberately named.

### Verification gates the driver applies

These are the few gates that are still automatic, because they don't depend on what the hypothesis claims —
they just check that the named claims are robust:

- **Repetition.** Each verification runs N times (default N = 3). All N runs must yield the same result for
  the hypothesis to be `verified`. If they diverge, it's recorded as `intermittent` and surfaced as a quirk
  in the reference rather than a hard fact.
- **Bounded timing window.** Listener-fire assertions specify a tick window (`within_ticks: 2`). The probe
  checks only within that window. Late fires are out of scope, not silently attributed.
- **State tagging.** When the same hypothesis is run under different preconditions and yields different
  outcomes, both rows are kept (`verified` / `armed` and `verified-as-noop` / `unarmed`, for example). The
  reference renders both — no collapsing into a misleading single answer.

### Optional null-control variant

A side-effect hypothesis (target `Y` fires when action `X` runs) _can_ include a paired null control: target
`Y` does **not** fire when action `X` is _not_ run, in the same precondition. When present, this raises
confidence — the fire is causally tied to the action, not coincidental. When absent (e.g., for mutating
methods with no clean no-op variant), the assertion still holds; it just carries lower confidence.

The null control is part of the hypothesis spec, not a probe-driver gate applied universally. The author opts
into it where it adds value; the architecture doesn't force it on every probe.

### Confidence levels

| Level                        | Meaning                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| `verified`                   | All named assertions held across all N runs in the recorded precondition.           |
| `verified-with-null-control` | Same, plus the optional null control held — fire is causally tied to the action.    |
| `state-dependent`            | Same hypothesis verified differently across preconditions. Reference shows the map. |
| `intermittent`               | Repetition unstable. Reference flags it; consumers shouldn't depend on it.          |
| `mismatch`                   | A named assertion failed. Either Live changed, or the hypothesis is wrong.          |
| `unprobed-precondition`      | Precondition couldn't be set up. Hypothesis remains an open question.               |
| `unprobed`                   | Hypothesis is in the sidecar but no probe run has covered it yet.                   |

The reference renders behavior at the confidence level it has. A `verified-with-null-control` side-effect is
a hard bullet; an `intermittent` one is a "fires inconsistently" caveat; an `unprobed` one is "expected, not
yet checked." Consumers see the level and decide.

### What this means for repo shape

A real concern: _"we end up with a huge repo of custom super-detailed scripts probing every member."_ The
mitigation, not avoidance:

- **Per-member detail is irreducible.** Each member that gets reference-rendered has a hypothesis specifying
  named targets, preconditions, prose. There's no algorithmic way around naming what `delete_clip` actually
  does.
- **But the detail is data, not code.** Hypotheses live in a declarative spec format (YAML / JSON), not in
  per-class Python files. One probe driver consumes the spec. New members add a row, not a script.
- **If you find yourself wanting to write per-class Python, that's a signal.** Either the spec format isn't
  expressive enough (extend it, in its own slice) or the member is genuinely a special case (rare; flag it
  explicitly and budget for it). The previous attempt's `probe_song.py` (~726 LOC) and `probe_track.py`
  (~520 LOC) were what happened when that signal got ignored.
- **The hypothesis _is_ the documentation.** Prose lives next to the assertions in the same record. The
  reference render reads the prose for description and the assertions for the structured metadata; nothing
  is duplicated, nothing drifts.

## The two-source merge

Behavioral metadata splits across two homes by editability and consumer:

### `Notes:` in stub docstrings (prose)

```python
@property
def overdub(self) -> bool:
    """Get/Set the global overdub state.

    Notes:
    - Value is not readable until the next tick after setting.
    - Silently ignored when no track is armed.
    """
```

Lives in the `.pyi` because Remote Script authors read these in their editor — that's already where the value
shows up. Prose only. (TBD: edited per-version vs extracted to a cross-version prose sidecar and injected at
codegen time. Defer until we know how often prose actually changes between versions.)

### `behavioral.json` sidecar (hypothesis records)

Each record is a hypothesis: prose description, structured action, named target assertions, optional
preconditions, optional null control. The exact format is locked in Slice 1 — this is illustrative shape,
not a fixed schema:

```yaml
Live.Song.Track.delete_clip:
  description: |
    Deletes the clip at the given slot index in the session view.
    Removal is immediate and undo-tracked. When the "Auto Clip Switch on
    Delete" preference is enabled and the deleted clip was the active one,
    the next clip down begins playback.
  action: { call: delete_clip, args: ["$slot_index"] }
  hypotheses:
    - id: removes_clip
      expects:
        - "$track.clip_slots[$slot_index].clip becomes null"
      undo_tracked: true
      async_class: immediate
    - id: starts_next_clip_with_pref
      precondition: "pref.auto_clip_switch_on_delete = true and clip_was_playing"
      expects:
        - "$song.is_playing becomes true within 2 ticks"
      null_control: "$song.is_playing stays false when delete_clip is not called"
  verified_against: 12.3.6
```

Prose and structured assertions live in the same record. The reference renderer reads the prose for the
description and the assertions for the metadata; nothing is duplicated, nothing drifts. Edited by humans
or LLMs, validated by the probe against the locked spec format, consumed by the reference generator. (TBD:
per-version sidecar vs canonical-with-overrides. Defer until Slice 1 has data.)

## Pipeline shape

```
Stage 1 (existing)         Stage 2 (existing)        Stage 3 (existing + Notes:)
─────────────────          ──────────────────         ─────────────────────────────
APICapture           →     parse + LLM refine    →    generate_stubs.py     →  Live/*.pyi
                                                            ↑
                                                  Notes: blocks (manual)

Stage 4 (new)              Stage 5 (new)
─────────────              ─────────────
behavioral_probe.py  →     generate_reference.py  →  reference/*.md
   ↑      ↑                       ↑
hypothesis  Live runtime          stubs + behavioral.json + Notes:
sidecar
```

`behavioral_probe.py` runs inside Live, reusing APICapture's trigger / hot-reload mechanism. It reads the
hypothesis sidecar, runs each verification, writes a result file. `generate_reference.py` consumes the
resolved tree, the verified sidecar, and the stub `Notes:` blocks to produce the markdown.

## Vertical slice plan

Slices are scoped by **member**, not by dimension. The hypothesis is the unit of work; a hypothesis covers
all the dimensions that apply to its member. Each slice picks a canonical target that exercises something
the previous slices couldn't express, and ships that target end-to-end (schema → probe → merged tree →
rendered reference). When a real cold-path investigation needs a capability the current slice plan doesn't
cover yet, that becomes the next slice's target.

The dimensions don't get built in order; they get built _as the slice's target needs them._

1. **Slice 1 — `Song.tempo` (the contracts). _This is the MVP._** Canonical simple property: settable,
   undo-tracked, immediate, no preconditions, no side-effects worth naming. The probe is trivial; the
   deliverable is the contracts the previous attempt didn't lock down — see ["What this means for Slice
   1"](#what-this-means-for-slice-1) above. Renders one fully-verified property end-to-end. Adds the
   dimensions: `async_class`, `undo_tracked`, `notes`. Lives on a branch until MVP is publishable; merging
   to main flips the canonical site in a single swap-day deploy (see
   [Publishing](#publishing-and-staging)). Slices 2+ are post-MVP expansions, each independently shippable
   against the same plumbing.
2. **Slice 2 — `Song.overdub` (state tagging + preconditions).** A property whose mutation is silently
   ignored under one precondition (no track armed) and effective under another (track armed). Forces the
   precondition table to grow from "trivial" to actually useful, and forces the renderer to display the
   state-tagged outcome map. Same dimensions as Slice 1, with state tagging as a new wrinkle.
3. **Slice 3 — `Track.delete_clip` (side-effects with named targets).** A method whose primary effect is the
   removal of a clip, with a documented side-effect (under preference X, playback may start). Adds the
   `side_effects` dimension with the named-target methodology — including the optional null-control variant
   and the iterative-refinement workflow used to discover the side-effect in the first place. This is the
   slice where the previous attempt's specific stall point is resolved by structural means: no listener
   sweep.
4. **Slice 4 — Warp markers (`invariants` + `operation_rules`).** The case study above, end-to-end. Adds
   the `invariants` dimension (slope rule, monotonicity, phantom marker as last entry) and the
   `operation_rules` dimension (`add_warp_marker`'s four conditional outcomes, `move`/`remove` raises). Adds
   the optional invariant↔operation-rule linkage from the case study so a single predicate isn't duplicated
   across multiple operation rules.
5. **Slice 5+ — Driven by the cold path.** From here, slices are demand-driven. As P4L surfaces questions,
   investigations pick a member, the hypothesis goes into the sidecar, the probe verifies, the reference
   updates. Most members will fit the spec format that exists by Slice 4; ones that don't surface as
   pressure on the spec format itself, and trigger a small extension slice rather than ad-hoc per-class
   code.

`notes` (the prose dimension) is present in every slice from day one — it's part of the hypothesis spec,
not its own slice. The reference generator reads it alongside the structured fields throughout.

After Slice 1 lands and proves the plumbing, the open questions below become concrete decisions instead of
speculation.

## Salvage from `doc/live-api/`

The 41 untracked baseline files are the **seed corpus across all slices** — not a one-time migration to
complete before MVP. Each slice picks a target, draws what's relevant from the baseline (probe notes, open
questions, behavioral observations), turns it into a hypothesis record, and ships. The baseline gets drained
gradually as slices cover its content.

Two anchors:

1. The baseline is _unversioned scratch_. Don't treat it as canon; don't preserve its formatting. Treat it
   as a notebook of prior probing that hasn't yet been turned into structured hypotheses.
2. Once a member's content has been fully absorbed into hypothesis records, its baseline file can be
   deleted — but there's no rush, and partial absorption is fine. A baseline file with three bullets
   migrated and seven still pending stays where it is.

There is also a separate floor to honor: the **existing live `reference/*.md`** files (slim, hand-written,
already publicly served). Anything the new generator emits at a public URL has to be at least as informative
as what's there now, or the public face of the project regresses. See [Publishing and
staging](#publishing-and-staging) for how that floor is preserved during MVP.

## Publishing and staging

The repo is public, but the site is recent and unstarred — no known external citations to defend. That
makes the publishing strategy simple:

**Swap-day.** MVP work lives on a branch (`behavioral-pipeline-architecture` and descendants). The current
site keeps serving the existing slim reference unchanged until MVP is publishable. When it is, a single
merge to main flips the canonical site to the new generator output in one deploy.

The only obligation: **prospective URL stability from Slice 1 forward.** The new generator emits explicit
anchor IDs derived from dotted paths (`#live-song-song-tempo`) so future heading rewords don't break
inbound links. Slug changes between old and new slim-vs-rich layout are accepted as a one-time event with
no redirect plan; this is the cheapest moment to incur it.

If the repo gains visible traction during MVP development (stars, external links discovered), revisit. The
fallback is **side-by-side preview** at a separate path (`/LiveAPI/preview/`) until the new content is
unambiguously better, with redirects on slug changes. More plumbing; only worth it if there's something to
defend.

## Open questions

1. **Sidecar version axis.** _Decided._ MVP ships **12.x only** — one sidecar (`behavioral.12.json`),
   probed against the latest 12.x. The architecture supports **per-major** sidecars
   (`behavioral.<major>.json`) as the post-MVP target; an **11.x backfill** is a planned one-time pass after
   MVP, not its own Slice. Per-minor-with-inheritance is rejected as overhead with no commensurate value.
   Drift detection within a major runs against new minors as Ableton ships them; `verified_against` records
   the latest minor each sidecar was probed against.
2. **`Notes:` editability across versions.** When 12.4 ships, do we copy the 12.3.6 stubs forward and
   re-apply `Notes:` blocks? Or extract `Notes:` to a sidecar and inject at codegen time? Defer; depends on
   how often prose actually changes between versions.
3. **Precondition table format.** Slice 1 introduces the precondition table (declarative, per the
   `integrate-targeted-probes` post-mortem). Slice 2 (`Song.overdub`) is where it first matters — needs to
   express "track armed" as a named precondition. Slice 3 (`Track.delete_clip`) extends it with preferences.
   Open question is the format: pure JSON state spec? JSON with named recipes (`"track_armed"` → setup
   steps)? Tiny Python module per class with named functions? The table starts trivial in Slice 1 and
   pressure-tests the format from Slice 2 on.
4. **Reference generator vs `reference/` legacy.** The existing slim `reference/*.md` files (Properties /
   Methods / Enums tables) — do they get fully regenerated and overwritten, or merged with hand-curated
   content? Defer; depends on whether the generator can match current format quality.
5. **Methods vs properties.** The dimensions were sketched against properties. Methods have analogous but
   not identical behavioral surface (no `async_class` for the call itself, but for return-value visibility
   and listener fan-out). Slice 3 (`Track.delete_clip`) is where this gets resolved.
6. **Predicate DSL for invariants and operation rules.** Slice 4 (warp markers) introduces predicates the
   probe must evaluate. JSON paths + a constrained expression language? Restricted `eval()` with a safe
   namespace? A small Python module per class? Defer; pick when Slice 4 starts.
7. **Investigation-mode tooling.** The methodology calls for an optional wide-snapshot tool that helps the
   human notice unexpected effects during cold-path investigation. Open question: is that a separate CLI
   (`probe --investigate Live.Song.Track.delete_clip`), an APICapture trigger that dumps a wide diff, or
   something the probe driver emits in `--only` mode automatically? Defer until Slice 3 — that's the slice
   where investigation matters most.
8. **Phantom marker as global vs local invariant.** `warp_markers_phantom_last` is specific to one property,
   but the same shape (last entry is internal sentinel) likely recurs elsewhere. Watch for repeats during
   salvage; if there are several, generalize the invariant kind.
9. **Where do incoming questions land?** The developer loop's "trigger" step needs a destination — when
   working in P4L and a question surfaces, where is it captured in LiveAPI before the probe runs? Options:
   `doc/open-questions/<topic>.md` files, `unverified` entries pre-seeded into the sidecar, GitHub issues,
   or just the conversation context with no persistent home. Defer until a few real cold-path investigations
   show what feels natural.
10. **Drift report shape.** When the per-version pipeline starts emitting verification diffs (Slice 1 onward,
    once enough hypotheses exist), what does the human-readable report look like? Per-member status table on
    the reference site? A CI-emitted markdown summary on each Live release PR? Defer until we have real drift
    to look at.
11. **Citability of the published reference.** _Decided._ Prospective only — repo is recent, unstarred, no
    known external citations to defend. The new generator emits **explicit anchor IDs derived from dotted
    paths** (`#live-song-song-tempo`) from Slice 1 onward, so future heading rewords never break inbound
    links. Slug changes between the old slim layout and the new rich layout are a one-time accepted event,
    no redirect plan. Revisit if the repo gains visible traction during MVP development; fallback is the
    side-by-side preview strategy noted in [Publishing](#publishing-and-staging).

## What this supersedes (eventually)

- `plan.md` — the `Notes:` integration sketch is preserved but extended into a four-dimension architecture.
- Parts of `decisions.md` covering the reference format will need an update once the generator drives the
  output rather than human authoring.

Both stay as-is until the new architecture has running code that obsoletes them.

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

- The schema is six dimensions, not four. `invariants` and `operation_rules` are the missing ones, and they're
  both verifiable, not prose.
- The cost is real: each new dimension is its own probe code, its own schema, its own reference render. Slice
  4 (`invariants`) and Slice 5 (`operation_rules`) get added to the slice plan below.
- Warp markers themselves don't get fully reference-rendered until Slice 5 lands. That's acceptable — earlier
  slices ship value for simpler members first.

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

### `behavioral.json` sidecar (structured)

```json
{
  "Live.Song.Song.tempo": {
    "async_class": "immediate",
    "undo_tracked": true,
    "side_effects": [],
    "verified_against": "12.3.6"
  },
  "Live.Song.Song.overdub": {
    "async_class": "next_tick",
    "undo_tracked": false,
    "side_effects": [
      {
        "target": "Live.Song.Song.session_record",
        "precondition": "track_armed"
      }
    ],
    "verified_against": "12.3.6"
  }
}
```

Edited by humans, validated by the probe, consumed by the reference generator. (TBD: per-version sidecar
vs one canonical file with per-version overrides. Defer until Slice 1 has data.)

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

Land one dimension end-to-end before adding the next. Each slice exercises the full pipeline (schema → probe
→ sidecar → reference render) so the plumbing is real, not paper.

1. **Slice 1 — `undo_tracked`.** Cheapest automatable dimension. Probe = mutate, undo, compare. Proves the
   schema, the hypothesis-verify loop, the merge into reference markdown, **and the cold-path
   `--only <member>` entry point** so the developer loop is usable from day one — not just at
   per-version-pipeline scale.
2. **Slice 2 — `async_class`.** Mutate, read immediately, await tick(s), read. Adds tick-driven probing to
   the harness.
3. **Slice 3 — `side_effects`.** Snapshot listenables, mutate, snapshot, diff. Adds the precondition system
   (named good-state setups per class) — this is where state-gated mutations get handled honestly.
4. **Slice 4 — `invariants`.** Predicates over collection/object state, evaluated opportunistically after
   probe-driven mutations. Schema is similar shape to `side_effects`; the new piece is a tiny predicate DSL
   (or restricted Python eval) that humans can read and the probe can run.
5. **Slice 5 — `operation_rules`.** Per-method `(precondition → outcome)` tuples. Reuses the precondition
   harness from Slice 3 plus the predicate plumbing from Slice 4. Most ambitious slice; warp markers become
   fully reference-rendered here.
6. **Stop.** `notes` stays human prose. Reference generator stitches everything together.

After Slice 1 lands and proves the plumbing, the open questions below become concrete decisions instead of
speculation.

## Salvage from `doc/live-api/`

The 41 untracked baseline files are the seed corpus for both `Notes:` blocks and `behavioral.json` hypotheses.
Salvage path:

1. Categorize each "Probe Notes" / "Open Questions" bullet as either prose (→ `Notes:`) or structured (→
   behavioral hypothesis).
2. Once content is migrated, the originals get deleted (they're un-versioned scratch anyway).
3. The new `reference/` markdown is generated from the merge — no hand-edits to it.

## Open questions

1. **Per-version vs canonical sidecar.** Does `behavioral.json` live per-stub-version, or is there one
   canonical file with per-version overrides? Defer until Slice 1 has data.
2. **`Notes:` editability across versions.** When 12.4 ships, do we copy the 12.3.6 stubs forward and
   re-apply `Notes:` blocks? Or extract `Notes:` to a sidecar and inject at codegen time? Defer; depends on
   how often prose actually changes between versions.
3. **State-machine harness for preconditions.** Slice 3 needs a way to declare "before probing
   `Song.overdub`, arm a track." Open question whether that's a Python DSL, a JSON state spec, or hand-coded
   per class.
4. **Reference generator vs `reference/` legacy.** The existing slim `reference/*.md` files (Properties /
   Methods / Enums tables) — do they get fully regenerated and overwritten, or merged with hand-curated
   content? Defer; depends on whether the generator can match current format quality.
5. **Methods vs properties.** The dimensions were sketched against properties. Methods have analogous but not
   identical behavioral surface (no `async_class` for the call itself, but for return-value visibility and
   listener fan-out). Slice 1 should clarify whether methods get the same schema or a parallel one.
6. **Predicate DSL for invariants and operation rules.** Slice 4 introduces predicates the probe must
   evaluate. JSON paths + a constrained expression language? Restricted `eval()` with a safe namespace? A
   small Python module per class? Defer; pick when Slice 4 starts.
7. **Phantom marker as global vs local invariant.** `warp_markers_phantom_last` is specific to one property,
   but the same shape (last entry is internal sentinel) likely recurs elsewhere. Watch for repeats during
   salvage; if there are several, generalize the invariant kind.
8. **Where do incoming questions land?** The developer loop's "trigger" step needs a destination — when
   working in P4L and a question surfaces, where is it captured in LiveAPI before the probe runs? Options:
   `doc/open-questions/<topic>.md` files, `unverified` entries pre-seeded into the sidecar, GitHub issues,
   or just the conversation context with no persistent home. Defer until a few real cold-path investigations
   show what feels natural.
9. **Drift report shape.** When Slice 5 lands and the per-version pipeline starts emitting verification
   diffs, what does the human-readable report look like? Per-member status table on the reference site? A
   CI-emitted markdown summary on each Live release PR? Defer until we have real drift to look at.
10. **Citability of the published reference.** Step 4 of the loop relies on stable URLs. The current MkDocs
    site uses class-name-based slugs; member anchors depend on heading text. Audit whether existing slugs
    are stable enough to cite from P4L source files, or whether members should get explicit anchor IDs
    derived from their dotted path.

## What this supersedes (eventually)

- `plan.md` — the `Notes:` integration sketch is preserved but extended into a four-dimension architecture.
- Parts of `decisions.md` covering the reference format will need an update once the generator drives the
  output rather than human authoring.

Both stay as-is until the new architecture has running code that obsoletes them.

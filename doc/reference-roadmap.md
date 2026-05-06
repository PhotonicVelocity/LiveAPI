# Documentation — Roadmap

> Companion to `reference-design.md` and `reference-design-sketches.md`. The
> design docs describe the destination; this doc describes the path. Each
> phase is independently shippable and produces visible value before the next
> phase starts. Sizing is rough — small / medium / large relative to each
> other, not in hours.

## Phase 0: where we are today

- Capture + parse + refine pipeline producing `LiveTree.refined.json`.
- Stubs generated from the refined tree, including parser-side enum widening,
  NoneType normalization, listener `Callable[[], None]` typing, refinement
  override system.
- Stub docstrings = runtime Boost.Python `__doc__` strings, verbatim.
- No reference site (parked).
- No hypothesis records, no behavioral probing.

The LOM's structural surface is well-covered. The behavioral surface is not
covered at all.

## Phase 1 — Reference v0: render what we already know

**Goal.** Resurface a published reference site, but driven from the refined
tree this time (not AST-parsing the `.pyi` like the old generator did). Pure
mechanical translation of what the parser already knows; no human-authored
content yet.

**What lands.**

- A new `tools/generate/generate_reference.py` that consumes
  `LiveTree.refined.json`. Eliminates the duplicate-parse logic the audit
  flagged.
- Per-class markdown pages with: title, full path, type signatures,
  property/method/enum tables, `Access via` cross-reference list, runtime
  docstring as the description (with a small "auto-generated docstring" tag
  so readers know it's not authored prose), refinement-metadata surfacing
  (`source:` + `confidence:` from the YAML rendered inline).
- MkDocs site rebuilds. GitHub Pages deploy workflow restored.

**What's deliberately not in Phase 1.**

- Authored prose. Every description is the runtime `__doc__`.
- Behavioral assertions. Site renders the static surface only.
- Stub docstring changes — stubs are unchanged from current state.

**Why first.** It's the Phase-2-onward proving ground. Locks in the rendering
pipeline, the cross-reference logic, the directory layout, and the
deployment story. Anything that's hard about Phase 2+ that's actually a
rendering-infrastructure problem surfaces here, before the harder content
work starts.

**Size.** Medium. Mostly a refactor of the parked old generator, plus a swap
of input source. No new methodology.

## Phase 2 — Hypothesis records: schema, authoring, dual rendering

**Goal.** Lock the record format and start hand-authoring prose for the LOM.
Both stubs and the reference start picking up authored content. _No probe
yet — verification comes in Phase 3._ This phase is "the schema and the
plumbing, with humans as the only verifier."

**What lands.**

- Locked record schema (YAML or JSON), validated. Covers description,
  structured hypotheses (with `confidence: unprobed` as the only allowed
  level for now), quirks, verified-against (still version-tagged, just
  empty-handed).
- Storage convention decided. Lean: per-class file in
  `doc/records/<Class>.yaml`, parallel to `tools/parse/manual_refinements.yaml`.
- Validator script run in CI: ensures every record refers to a real symbol
  in the refined tree, schema is well-formed, no duplicate IDs.
- Reference generator extended to read records. Authored description
  replaces runtime docstring when present (with the runtime version
  available in a "see source" admonition or similar).
- Stub generator extended to read records. Authored description replaces or
  augments the runtime `__doc__` in the emitted `.pyi`. The two-rendering
  story from §5 of the design doc starts working end-to-end.
- A handful of records hand-authored as proof: one per slice-plan target
  (`Song.tempo`, `Track.delete_clip`, `Clip.add_warp_marker`) plus a couple
  of randomly-picked simple properties to stress the layout.

**Why second.** The schema lock-in is the single biggest risk for the rest
of the work — the previous attempt's stall point. Doing it before the probe
forces the format to serve the human authoring case first; the probe just
has to verify what's already structured. If the schema feels right to write
by hand, it'll feel right to verify against.

The stub-docstring payoff comes here, not at the end. Hand-authored prose
in stub `.pyi` lands the moment you have records — no probe required.

**Size.** Medium. Schema design is the careful part; the integrations on
both generators are mechanical once it's locked.

## Phase 3 — Probe driver, cold path

**Goal.** Verify hand-authored hypotheses against running Live. The
developer loop ("notice something → propose hypothesis → probe → publish")
becomes real.

**What lands.**

- The probe driver, runs inside Live via APICapture's hot-reload mechanism.
  Single function: take a record + a target member, run the action, check the
  named assertions, return a result with confidence level.
- The precondition table format. Even trivial members may have no preconditions,
  but the table exists from day one so later work extends it instead of
  inventing it.
- Cold-path entry point: `probe.py --only <dotted.path>` runs one member's
  hypotheses, no others. This is also the developer-loop entry point — same
  workflow, same code.
- Stamping function: merges verification results into the records (updates
  `confidence:` and `verified_against:`).
- Reference and stub generators updated to render the verified content
  faithfully — confidence levels surface in both, no collapsing.
- The Phase-2 hand-authored records get probed; the ones that verify
  cleanly become the first verified entries in the docs.

**Why third.** With Phase 2 in place the probe has a clear job: verify what's
already written. No discovery, no schema thrash, no per-class probe scripts.
The driver consumes records and produces verification results — one input
shape, one output shape.

**Size.** Large. The driver itself is the genuinely new code. Precondition
resolution, state setup/teardown, repetition gate, timing window for listener
fires — all the things the previous attempt got wrong are concentrated here.
The lessons from the behavioral arch doc apply directly: lock contracts
first, declarative preconditions, single driver, single stamping function,
state restoration is best-effort.

## Phase 4 — Warm path, drift detection

**Goal.** Run all verified hypotheses against a new Live version. Surface
drift. Make the "hypothesis is forever" claim real.

**What lands.**

- Warm-path entry point: `probe.py` (no `--only`), runs every record's
  hypotheses against the current Live version.
- Drift report: hypotheses that previously verified but now `mismatch`
  surface as a flagged list, ordered by class.
- CI integration: a pipeline workflow runs the warm path on a tagged
  capture, fails (or reports) on new mismatches.
- Reference and stub docstrings render `verified-against: 12.X.Y` so
  readers see staleness explicitly.

**Why fourth.** Builds on Phase 3 with mostly automation. Most of the
infrastructure exists; this phase glues it to the version-bump workflow.

**Size.** Small to medium. Bulk of the work is the report shape + CI
integration; the actual verification logic is the same as Phase 3.

## Phase 5 — Coverage push

**Goal.** Systematically work through the LOM, hand-authoring records and
verifying via cold path.

**What lands.**

- A coverage tracker (probably auto-generated): which members have records,
  which records have verified hypotheses, which are still `unprobed`.
  Renders as a page on the reference site so it's visible to readers.
- Investigation backlog: `refinements_followup.md`-style file listing
  members worth investigating, ordered by impact (Song / Track / Clip
  before edge cases).
- Per-class records, one class at a time, working down a priority list.

**Why last.** This phase isn't a feature; it's iteration on infrastructure
already in place. Could start as soon as Phase 2 lands (you can author
records before probe exists). The coverage push only becomes a coherent
phase once the probe is doing real verification work.

**Size.** Ongoing — there's no defined "done." Reasonable milestones:

- Slice 1 target classes verified (Song, Track, Clip).
- All Live document objects (Song / Track / Clip / ClipSlot / Scene / Device)
  have at least description-level records.
- 50% of public LOM members have authored descriptions.

## Cross-cutting: not assigned to any phase

These are concerns that thread through multiple phases; flagged here so they
don't get rediscovered as surprises later.

- **`__init__` constructor handling.** Bypasses the parser tree (per the
  audit). Reference and stub-docstring injection both inherit the gap.
  Resolve before any class with a non-trivial constructor enters Phase 5
  scope. The fix is upstream of the documentation work — it's a parser/
  generator gap to close in `parse_apicapture_results.py` and
  `generate_stubs.py`.
- **Stable URLs.** Class-page anchors are easy. Per-member anchors are
  easy. Per-assertion sub-anchors (`#warp_markers-slope-rule`) require
  thinking through the URL contract before records get cited from
  external repos. Lock in Phase 2 with the schema.
- **Multi-version side-by-side.** Out of scope per the design doc. If it
  ever comes back, the per-version sidecar story (canonical-with-overrides
  vs full sets per version) needs to be settled — easier to defer than
  guess.

## What the path implies

After Phase 1: published site with auto-generated content, no worse than
the old generator's output, but built on a maintainable foundation.

After Phase 2: hand-authored prose in stubs and reference, no probe needed.
Materially better stub docstrings for any member that's been written up. The
gap between "this is autogen" and "this has a real description" is visible
to readers as explicit metadata.

After Phase 3: verified behavior records for select members. The cold-path
developer loop is real — a question raised in P4L can produce a verified
hypothesis in LiveAPI, and the answer is publicly citable.

After Phase 4: the reference defends itself across Live versions. Drift is
flagged, not silently absorbed.

After Phase 5: depends on how much coverage the maintainer has the bandwidth
for. The infrastructure scales with the writing effort.

The asymmetric distribution is intentional. Phases 1–2 build out the
infrastructure that enables polished docs immediately. Phase 3 is the hard
phase. Phases 4–5 ride on what's been built.

# Documentation — Roadmap

> Companion to `reference-design.md` and `reference-design-sketches.md`. The
> design docs describe the destination; this doc describes the path. Each
> phase is independently shippable and produces visible value before the next
> phase starts. Sizing is rough — small / medium / large relative to each
> other, not in hours.

## Phase 0: where we are today

- Capture + parse + lom-build pipeline producing `stubs/<v>/lom/*.yaml`
  (the curated SOT — algorithmic seed plus sibling `<field>_override:` blocks).
- Stubs generated from `lom/` via `build_stubs_from_yaml.py`, including
  parser-side enum widening, optional widening, listener-triplet folding,
  parametric-container detection, and the override mechanism.
- Stub docstrings = runtime Boost.Python `__doc__` strings, verbatim.
- No reference site (parked).
- No hypothesis records, no behavioral probing.

The LOM's structural surface is well-covered. The behavioral surface is not
covered at all.

## Phase 1 — Reference v0: render what we already know

**Goal.** Resurface a published reference site, but driven from the lom YAML
SOT this time (not AST-parsing the `.pyi` like the old generator did). Pure
mechanical translation of what the parser already knows; no human-authored
content yet.

**What lands.**

- `tools/generate/generate_reference.py` ported from the legacy
  `LiveTree.refined.json` input to read `stubs/<v>/lom/*.yaml` directly.
  Eliminates the duplicate-parse logic the audit flagged.
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

**Stack pivot during execution.** The original plan was MkDocs + Material
(restored from the parked work). After auditing the old generator and looking
at how Blender's Python API docs read, we switched to **Astro Starlight**:
better default visual hierarchy, easier custom Astro components when
behavioral content lands in Phase 2/3, Pagefind search built in. Old MkDocs
work tossed; Starlight project lives at `web/`.

### Step ladder (within Phase 1)

The generator is built up incrementally — each step is its own commit-sized
change, each step's output is independently shippable. Earlier steps consume
just the structural surface from the lom YAML; later steps add detail until
everything in `stubs/<v>/lom/*.yaml` (parser-derived fields plus override
blocks) flows through to the rendered page.

Status as of context reset (mid-Step 2, Blender-styled signatures landed
across class / enum / function headings, main class promoted):

- **Step 1 — Module page skeleton.** ✅ Done. One MDX page per module under
  `web/src/content/docs/modules/`. Page has title, one-line module
  description, and bullet list of class / enum / function names. Generator
  at `tools/generate/generate_reference.py`. Sidebar autogenerates from the
  `modules/` subdirectory.
- **Step 1.5 — Promote names to H3 + syntax-highlight signatures.** ✅ Done.
  Each class / enum / function rendered as Blender-style heading
  (`class Live.Module.Name(Base)` / `enum Live.Module.Name` /
  `def Live.Module.name()`) with span-level coloring (kw / path / name /
  base) and white-bold class name dominating dim-orange path. Custom CSS
  in `web/src/styles/custom.css` covers heading hierarchy + signature spans.
- **Step 1.75 — Main class promotion.** ✅ Done. The class whose name
  matches the module name (the conventional Live.X.X pairing) renders as
  a prominent signature line at the top of the page. Remaining classes
  move under `## Other classes`. When properties / methods land, they
  attach directly under the main class as `## Properties`, `## Methods`,
  etc., making the main-vs-auxiliary structure explicit.
- **Step 2 — Class descriptions.** Pending. Each class heading gets its
  `raw_doc` rendered below as a paragraph. Same for enums and module
  functions when those have raw_doc set.
- **Step 3 — Properties listed.** For each class (starting with the main
  class), render a `## Properties` section with each property name as an
  H3 (signature shape: just the property name in monospace bold). No types
  or descriptions yet.
- **Step 4 — Property types.** Add the `probed_type` to each property's
  heading or as a labeled field below it (`**Type:** float` style).
- **Step 5 — Property settable / listenable.** Annotate with `(get/set,
listenable)` derived from the `settable` flag and the existence of
  `add_X_listener` siblings. Goes inline with the type line.
- **Step 6 — Property descriptions.** Each property's `raw_doc` (which is
  already the cleaned description for properties — no signature header
  to strip, unlike methods) renders as a paragraph below the type metadata.
- **Step 7 — Methods listed.** Same ladder as properties: `## Methods`
  section with method names as H3 headings (signature shape:
  `name(args) -> return`). Use the parser's `description` field rather
  than `raw_doc` so the Boost.Python signature header and `C++ signature:`
  footer don't dump into the doc.
- **Step 8 — Module-level enums.** Currently rendered as headings only.
  Add member tables (`Member | Value` listing) under each enum heading,
  using the enum's `members` field from the refined tree.
- **Step 9 — Module-level functions.** Currently rendered as headings only.
  Add full signature with args + return type, the `description` field as
  prose, and `**Parameters:**` / `**Returns:**` labeled sections.
- **Step 10 — Nested classes.** Classes defined inside other classes
  (e.g., `Clip.View`, `Track.View`, `Song.View`). Render as their own
  section on the parent class's page, with the nested class's properties
  / methods rendered inline.
- **Step 11 — References / Access via.** Cross-reference pass — for each
  class T, list every member elsewhere in the LOM whose type / return
  is T. Implemented as a single tree-walk at generator startup that
  builds a `class_name → [(owner, member, kind)]` map. Renders as a
  collapsible `<details>` at the bottom of each class section, or a
  `## References` section near the page bottom (decide by looking at
  layout density once the data lands).
- **Step 12 — Refinement metadata surfacing.** When a field has a sibling
  `<field>_override:` block in `stubs/<v>/lom/*.yaml`, render the `source:`
  and `confidence:` inline with the member (small italic note under the
  type line, or a callout block — design when the data lands).
- **Step 13 — Inherited members.** For classes with parents in the LOM
  (mostly just `LomObject` for Live document objects, but some richer
  hierarchies exist), show inherited properties / methods in their own
  section with bullet links to the base class's documentation.

After Step 13, every field in `stubs/<v>/lom/*.yaml` (parser-derived
fields plus override blocks) is rendered. Phase 1 is structurally complete.
Phase 2's authored prose / hypothesis records is the next layer of
content, not infrastructure.

### Phase 1 layout decisions (locked during execution)

- **Heading hierarchy.** H1 (page) ~2.25rem, H2 (section dividers) 1.5rem
  with full-width bottom border, H3 (member identifiers) 1rem monospace
  bold. Aggressive scale steps so the hierarchy reads at a glance.
- **Class signatures.** Span-coloring via four CSS classes
  (`cls-kw` / `cls-path` / `cls-name` / `cls-base`). Class name in bright
  white bold dominates the dim-orange path and base.
- **Sidebar.** Flat — single "Modules" group, autogenerated from
  `web/src/content/docs/modules/`, alphabetical. URLs live at
  `/LiveAPI/modules/<name>/`.
- **Right TOC.** Down to H3 (`maxHeadingLevel: 3`) so members show up
  alongside section headers as a navigable index of the page.
- **Main class promotion.** Self-named class (Live.X.X) renders as a
  prominent monospace signature at 1.3rem at the top of the page,
  no left-border accent. Other classes go under `## Other classes`.

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
  `doc/records/<Class>.yaml`, parallel to `stubs/<v>/lom/<Module>.yaml`.
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

**Connection to manual refinements.** The probe driver doesn't just verify
behavioral assertions (side effects, raises, listener fires) — it can also
verify type claims (this property is settable, accepts T, returns T on read).
That means today's `confidence: high` in lom override blocks
(corpus-verified) becomes `confidence: verified` (runtime-probed) once the
probe touches the same member. The refinement system and the hypothesis
system converge on a single confidence ladder; type accuracy and behavioral
accuracy share the same verification mechanism.

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
- Investigation backlog: a markdown file listing members worth investigating,
  ordered by impact (Song / Track / Clip before edge cases).
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
  generator gap to close in `parse_apicapture_results_v2.py`,
  `build_lom_yaml.py`, and `build_stubs_from_yaml.py`.
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

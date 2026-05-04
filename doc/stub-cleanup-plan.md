# Stub Pipeline Cleanup — Implementation Plan

> Working plan for the `stub-pipeline-cleanup` branch. Tracks step-by-step execution. Updated as steps land.
>
> Companion to [decisions.md](decisions.md) (the principles and locked-in decisions) and the
> `behavioral-pipeline-architecture` branch (the separate behavioral-probing work).

## Scope

Pull the LLM-resolve step, audit the parser's `T | None` defaults, demote MaxForLive type claims to docstrings,
keep only the latest 12.x version active, add CI verification of stub usability. See [decisions.md §
Stub Accuracy and Pipeline Posture](decisions.md#stub-accuracy-and-pipeline-posture) for the rationale.

## Sequence

Each step is one focused commit with the previous step's verification as the safety net.

### Step 1 — Add verification CI

Verification before any pipeline change so we have a baseline for what the current stubs do, and a regression
check for everything that follows.

- New `tools/verify/parse_check.py` — walks `stubs/<version>/Live/*.pyi`, runs `ast.parse` on each, exits
  non-zero on any failure. Pure stdlib.
- Pyright invocation against the stubs themselves (`pyright stubs/12.3.6/Live` or a tuned config) to catch
  internal inconsistencies — broken references, undefined symbols, Liskov violations, cyclic imports.
- Pyright `--verifytypes` mode for PEP 561 completeness reporting (tracked as a number, not gated).
- A small `tests/usage/` set of **hand-picked** files exercising typical Remote Script patterns; type-checked
  by pyright. Patterns drawn from `doc/decompiled/AbletonLive12_MIDIRemoteScripts/` — Ableton's own code —
  so each test is a snippet of definitely-working production usage. ~5–10 tests in Step 1 covering the most-
  trafficked surface (Song basics, Track navigation, Clip operations, Device traversal, listener
  registration). Hand-picked deliberately, not auto-extracted (auto-extraction at scale recreates the
  cargo-culted-content problem the LLM removal is solving).
- `.github/workflows/verify-stubs.yml` running on push and PR; triggers on `stubs/**` and `tools/verify/**`
  changes.

Run once locally against `main` stubs before committing to record the baseline. Push only after the baseline
is documented (in this plan, in the verify directory's README, or in the commit message).

**Step 1b — Expand hand-picked usage tests (rolling, driven by cleanup findings).** As later steps surface
gaps (something Ableton's code uses that our stubs don't expose, a parser change that breaks a pattern we
hadn't covered), add a new hand-picked test exercising that pattern. The set grows deliberately, not by
extraction. By the time Step 8 publishes, the suite reflects the surface we know we want to defend.

**Offline audit (any time, not in CI).** Pyright over the entire decompiled corpus (`doc/decompiled/`) using
our stubs as the type source — invocation via `tools/verify/audit_corpus.sh` (TBD). Surfaces missing API
surface, wrong inheritance, type incompatibilities at scale. Noisy because of decompilation artifacts and
internal-module imports; needs a tuned `pyrightconfig.json` filtering to errors that involve `Live.*` types.
Used during Steps 4 and 5 to surface candidate issues before re-running the full pipeline. Not a CI gate —
the hand-picked tests stay the regression bar.

### Step 2 — Strip Stage 2 to parse-only

Reduce the pipeline to capture → parse → generate. Stage 3 reads `LiveTree.parsed.json` directly.

- `run_parse_pipeline.py` runs only `parse_apicapture_results.py`, stops there.
- `extract_unresolved.py`, `callsite_resolve.py`, `apply_refinements.py`, `llm_resolve.py`,
  `llm_resolve_prompt.md`, `llm_hints.md` no longer in the active pipeline.
  - Don't delete files yet — `git rm` in a later step once we're sure nothing is needed back.
  - Update `run_pipeline.py` to skip the `--skip-llm` and related flags.
- Regenerate 12.3.6 stubs from this minimal pipeline. Verification runs. Diff against baseline shows what
  changed.

This is the most aggressive step; expect significant churn in the stubs. Verification tells us whether the
churn is acceptable or whether the parser needs immediate help.

### Step 3 — _(dropped)_ Callsite refinement

Originally planned to re-add `callsite_resolve.py` for arg-name resolution from decompiled Remote
Scripts. **Dropped:** with `, /` (PEP 570) on every callable signature, names are decorative — they show
in autocomplete hints but cannot be used as kwargs. Callsite-resolved names are evidence of how Ableton's
engineers _wrote_ their code, not evidence of what the binding _accepts_; the same accuracy concern that
motivated dropping the LLM applies. The strict posture is: only what we scrape from Live itself (probe
data + parsed C++ signatures + structural inference) feeds the stubs.

### Step 4 — _(dropped)_ `manual_refinements.json`

Originally planned as the hand-curated escape hatch for type fixes the LLM was producing. **Dropped for
now:** in the strict-from-Live posture, the only refinements that should land are corrections to known
wrongness, not "make stubs prettier" entries. If a specific case surfaces during Step 5 (parser audit) or
later that genuinely needs a manual override, we'll add the file then with a strict bar (rationale and
source citation per entry). Keeping it out by default avoids recreating the slippery-slope problem the
LLM removal solved.

### Step 5 — Audit parser `T | None` defaults

The biggest accuracy improvement, and the most potentially-disruptive — affects nearly every signature.

- Audit `parse_apicapture_results.py` for every place it widens to `T | None` defensively.
- Decide per-case: keep (truly nullable per probe data) vs. drop (false-positive defensive widening).
- Regenerate, verify. Sample-check the diff. Likely large but isolated to type annotations.

### Step 6 — Trim version coverage

- Update `release.yml` to only build/publish 12.x.
- Frozen versions (`stubs/11.*`, `stubs/12.0–12.2`) stay as historical artifacts; remove from `mkdocs.yml`
  if/when Pages is re-enabled.
- `release/` directory and `dist/` artifacts for old versions left as-is for forensic record.

### Step 7 — Delete refinement machinery

After Step 6 is stable, `git rm` everything that's no longer in the active pipeline:

- `tools/parse/llm_resolve.py`, `tools/parse/llm_resolve_prompt.md`, `tools/parse/llm_hints.md`,
  `tools/parse/batches/` and any LLM cache/output directories.
- `tools/parse/callsite_resolve.py` (no longer used).
- `tools/parse/extract_unresolved.py` and `tools/parse/apply_refinements.py` (helpers for the dropped
  refinement steps).
- `tools/parse/build_type_skeleton.py` if it was only feeding the LLM prompt.
- Update the [decisions.md](decisions.md) Parse Pipeline section to describe the new minimal pipeline.

### Step 8 — Offline corpus audit tool

`tools/verify/audit_corpus.py` — runs pyright over the full decompiled Ableton Remote Script
corpus using our stubs as the type source, filters out internal-module imports, decompilation
artifacts, and errors that don't mention a class declared in our stubs. Surfaces only places
where the stubs disagree with working production code. Not a CI gate — research tool used to
inform manual refinements and Tier 4 expansion.

### Step 9 — Manual refinements infrastructure

`tools/parse/manual_refinements.yaml` + `tools/parse/apply_manual_refinements.py`. YAML for
human-readability and per-entry comments. Each entry must include a `source` field documenting
why the override is justified. Supports renaming positional args, overriding arg/return types,
and overriding property `probed_type`. Wired into `run_parse_pipeline.py` as Stage 2b.

### Step 10 — Generator fix: enum-arg widening

Boost.Python enum bindings accept either the enum value or the underlying int at runtime — but
the generator emits args typed as the bare enum class. Pyright correctly rejects `int` when the
stub says `MapMode`. Fix: when the resolved arg type is a known enum class, emit `EnumName | int`.
Eliminates Group A of the audit findings entirely (one code change, applies to every enum-typed
parameter across the API).

### Step 11 — Generator fix: NoneType → Any fallback

The generator currently emits `-> None` and `value: None` setters when the property's
`probed_type` is `NoneType`. That happens when the probe observed `None` at probe time but the
property is actually nullable (e.g., `Song.View.selected_chain` is `Chain | None` — the probe
saw None because no chain was selected). Fix: emit `Any` instead of literal `None` for
NoneType-probed cases. Manual refinements then narrow the specific 10 known cases to the right
`T | None`. Honest fallback for any future cases the refinement file doesn't yet cover.

### Step 12 — Targeted manual refinements

Populate `manual_refinements.yaml` with the corrections from Steps 10–11 not handled by the
generator:

- **10 NoneType-property entries** — `Song.View.selected_chain`, `Song.appointed_device`,
  `Clip.groove`, `Browser.hotswap_target`, etc. Override `probed_type` to the right `T | None`.
  Source: probe observed None but the docstring + Live API behavior establishes the underlying
  type.
- **6 feedback-rule entries** — `map_midi_cc_with_feedback_map.feedback_rule` etc. Widen to
  `T | None` where Ableton's `_Framework/ControlSurface.py` passes None at runtime. Source:
  audit finding from corpus.

**argN cosmetic pass deferred** — the user explicitly asked to skip for this phase; will live
on a follow-up branch if pursued.

### Step 13 — Investigate Groups D & E

`BrowserItem.children` override conflict (3 hits) and `DrumPad.parameters` missing (2 hits).
Each needs investigation to know whether it's a stub fix, a parser/probe gap, or noise. Defer
until Step 12 lands; could be either a refinement entry or a follow-up issue.

### Step 14 — Expand Tier 4 with audit-informed tests

Add hand-picked usage tests covering the patterns Step 12 fixed — assigning `Chain` to
`View.selected_chain`, calling `map_midi_cc_with_feedback_map` with `None` for the feedback
rule, calling `map_midi_cc` with `int` for `map_mode`. Future regressions in these areas will
break the test suite.

### Step 15 — Re-publish

When verification passes and the cleaned 12.3.6 (or 12.3.7+) stubs are believed accurate:

- Bump version (PyPI requires a new version string after yank).
- Push to main; release workflow publishes to PyPI.
- Re-enable GitHub Pages with a new index reflecting the rewritten stubs and the existing reference docs.
- Update README banner: remove the "withdrawn" notice or replace with "freshly rebuilt — see release notes".

## Status

| Step                                      | Status                                                |
| ----------------------------------------- | ----------------------------------------------------- |
| 1. Verification CI                        | done — baseline: T1 ✓, T4 ✓, T2 29 errs               |
| 2. Strip pipeline to parse-only           | done — T2 dropped 29 → 3                              |
| 3. ~~Callsite refinement~~                | dropped — same vein as LLM                            |
| 4. ~~`manual_refinements.json`~~          | superseded by Step 9 (yaml-based, narrower scope)     |
| 5. Parser `T \| None` audit               | done — bug at generate_stubs.py:514, ~120 → 3         |
| 6. Trim version coverage                  | done — release.yml scoped to 12.x auto-publish        |
| 7. Delete refinement machinery            | done — 7 files removed, README + decisions updated    |
| 7b. Property-override Liskov fix          | done — T2 dropped 3 → 0 (skip override on probe fail) |
| 8. Offline corpus audit tool              | done — 12,094 raw → 40 candidates                     |
| 9. Manual refinements infrastructure      | done — yaml + apply script + run_parse_pipeline wire  |
| 10. Generator fix: enum-arg widening      | not started                                           |
| 11. Generator fix: NoneType → Any         | not started                                           |
| 12. Targeted refinements (16 entries)     | not started                                           |
| 13. Investigate `BrowserItem` / `DrumPad` | not started                                           |
| 14. Expand Tier 4 with audit findings     | not started                                           |
| 15. Re-publish                            | not started                                           |

`argN` cosmetic pass: deferred. Not part of this branch unless explicitly re-scoped.

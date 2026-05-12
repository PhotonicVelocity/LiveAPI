# Data Flow

How a Live runtime becomes published reference docs and typed stubs. This is
a snapshot of the **current** wiring — what's automated, what's hand-curated,
where the data lives between stages. For *why* each piece exists see
[`decisions.md`](decisions.md) and [`reference-design.md`](reference-design.md).

```
                ┌────────────────────────────────────────────────────────┐
                │   Stage 1 — CAPTURE              (inside Ableton Live) │
                │   driver:  tools/run_pipeline.py                       │
                │   runs:    tools/apicapture/APICapture.py              │
                │            ├─ scripts/CaptureModule.py                 │
                │            ├─ scripts/PropertyProbe.py                 │
                │            └─ scripts/DeviceProbe.py                   │
                └────────────────────────────────────────────────────────┘
                                          │
                          LiveTree.raw.json + LiveClasses.json
                                          ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 2a — PARSE                                     │
                │   driver:  tools/parse/run_parse_pipeline.py           │
                │   runs:    tools/parse/parse_apicapture_results_v2.py  │
                └────────────────────────────────────────────────────────┘
                                          │
                          LiveTree.parsed.v2.json (immutable)
                                          ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 2b — BUILD MARKDOWN SEED                       │
                │   driver:  tools/parse/run_parse_pipeline.py           │
                │   runs:    tools/parse/build_lom_md.py                 │
                └────────────────────────────────────────────────────────┘
                                          │
                          stubs/<v>/reports/seed/*.md
                                          │
   ┌────────────────────────────────┐     │
   │ stubs/<v>/modules/*.md         │  ◀──┘  (resync at intentional checkpoints)
   │ CURATED SOT — seed + sibling   │
   │ <field>_override: blocks       │
   │ (each with source:) + prose    │
   └────────────────┬───────────────┘
                    ▼
              ┌─────┴─────────────────────────────────────────────┐
              ▼                                                   ▼
   ┌──────────────────────────────────┐         ┌──────────────────────────────────┐
   │  Stage 3a — STUBS                │         │  Stage 3b — REFERENCE PAGES      │
   │  tools/generate/                 │         │  tools/generate/                 │
   │    generate_stubs.py             │         │    generate_reference.py         │
   │                                  │         │                                  │
   │  → stubs/<v>/Live/*.pyi          │         │  → web/.../modules/*.mdx         │
   └──────────────────────────────────┘         └──────────────────────────────────┘
                                                              │
                                                              ▼
                                                ┌──────────────────────────────────┐
                                                │  Stage 4 — SITE BUILD            │
                                                │  npm run build (web/)            │
                                                │  Astro / Starlight integration   │
                                                │  → web/dist/ → GitHub Pages      │
                                                └──────────────────────────────────┘
```

`stubs/<v>/modules/*.md` is the **single source of truth** that fans out into
both renderings (stubs and reference). Nothing is hand-maintained twice. Each
module file holds fenced YAML blocks for structured fields plus authored prose
between them — format spec: [`lom-format.md`](lom-format.md).

---

## Stage 1 — Capture (inside Live)

**Tool:** [`tools/apicapture/`](../tools/apicapture/) — a Remote Script that
loads as a Control Surface inside Ableton Live.

**Driver:** [`tools/run_pipeline.py`](../tools/run_pipeline.py) launches Live
with a known `.als` (from [`tools/sets/`](../tools/sets/)) and uses
`/tmp/apicapture_*` trigger files to invoke phases.

**Phases:**

| Phase            | Script                                                              | What it does                                                              |
|------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| capture          | [`CaptureModule.py`](../tools/apicapture/scripts/CaptureModule.py)  | Recursive `dir()` walk of the `Live` module → name/repr/doc/value tree    |
| probe (basic)    | [`PropertyProbe.py`](../tools/apicapture/scripts/PropertyProbe.py)  | Visits live instances, reads each property, records runtime types         |
| probe (full)     | [`DeviceProbe.py`](../tools/apicapture/scripts/DeviceProbe.py)      | Loads every device through the browser to expose device-specific types    |

**Outputs** (under [`stubs/<version>/pipeline/`](../stubs/12.3.6/pipeline/) — gitignored):

- `LiveTree.raw.json` — structural snapshot (the dir-walk tree). Consumed by Stage 2a.
- `LiveClasses.json` — runtime probe data keyed by class repr (property types, settable flags, no-arg getters).
  Currently *not* consumed by the v2 parse pipeline (which is raw_doc-only); kept around as a future input
  for probe-confirmed type widening and for pre-port verification of overrides.

**Hand-curated inputs:** the `.als` set files in
[`tools/sets/`](../tools/sets/) — Live needs *something* loaded for probes to
have instances to walk.

**Not committed:** the raw outputs aren't in git (they're rebuildable from a
running Live). The committed `Live/` directory is the *generated stubs*, not
the raw capture (confusing naming — see Stage 3a).

---

## Stage 2a — Parse (offline)

**Tool:** [`tools/parse/parse_apicapture_results_v2.py`](../tools/parse/parse_apicapture_results_v2.py)
(invoked via [`tools/parse/run_parse_pipeline.py`](../tools/parse/run_parse_pipeline.py)).

**Inputs:** `LiveTree.raw.json` from Stage 1.

Multi-step transform pipeline; each step takes the tree + a shared context dict and returns the transformed tree:

1. fix malformed Boost.Python class names
2. propagate the fixes through `raw_doc` strings
3. resolve inheritance (ancestors + relocate inherited members to defining class)
4. parse enum members from string-encoded forms, retype as `"enum"`
5. parse function docs into structured `signature` / `description` / C++ pairs, build C++→Python type map, resolve into clean args + returns

**Output:** [`stubs/<version>/pipeline/LiveTree.parsed.v2.json`](../stubs/12.3.6/pipeline/) —
the canonical parser output. **Never hand-edited.**

**Hand-curated:** none. Mechanical transform of capture data only.

---

## Stage 2b — Build markdown seed (offline)

**Tool:** [`tools/parse/build_lom_md.py`](../tools/parse/build_lom_md.py)
(also invoked via `run_parse_pipeline.py`). Builds the per-module dict in
memory and serializes via [`md_emit.convert()`](../tools/parse/md_emit.py).

**Inputs:** `LiveTree.parsed.v2.json`.

Converts the parsed tree into one markdown file per top-level Live module,
applying the algorithmic decisions a human shouldn't have to make explicit:

- Type qualification (`Track` → `Live.Track.Track`)
- Optional widening (`T` + `default=None` → `T | None`)
- Enum widening (`E` → `E | int` — Boost.Python emits enums as int subclasses)
- Enum-from-default inference (bare `int` arg with default `Module.Enum.member` → `Enum | int`)
- Listener-triplet folding (`add_*_listener`/`remove_*_listener`/`*_has_listener` collapsed under the property)
- Parametric-container flag (`Live.Base.Vector` → `parametric: true`; renders as `Generic[T]`)
- Container detection (iterables exposing both `append` and `extend` → `container: true`; concrete subclasses
  inherit from `Vector[E]` and synthesize typed mutators at stub-render time)
- Inherited-property cleanup (drop properties identical to an ancestor's declaration so pyright resolves the
  annotation from the inherited declaration; keeps overrides intact)

**Output:** [`stubs/<version>/reports/seed/<Module>.md`](../stubs/12.3.6/reports/seed/) —
the algorithmic baseline. Regenerated freely; not hand-edited.

---

## The modules/ SOT (curated)

**Location:** [`stubs/<version>/modules/<Module>.md`](../stubs/12.3.6/modules/).

Started as a copy of `seed/`. Carries sibling `<field>_override:` blocks where humans
have tightened types, renamed args, or qualified iterable element types. Each override
has a `value:`, an optional `confidence:` (`high` / `medium` / `low` for typed
overrides), and a required `source:` field (corpus def-site, M4L doc citation, raw_doc
text). Format spec: [`lom-format.md`](lom-format.md).

`seed/` regenerates on every Stage 2 run; `modules/` is only resynced at intentional
checkpoints, so a fresh capture won't trample existing overrides. Diffing `seed/`
against `modules/` shows exactly which facts have been hand-touched.

**Drift safety:** type overrides can include a `from:` value that's validated against
the parsed-tree value during port/audit, so a Live-version change that shifts parser
output surfaces as a warning rather than being silently absorbed.

---

## Stage 3 — Two renderings of one SOT

Both consumers read `modules/*.md` and *only* that. They never reach back to raw
capture, M4L docs, or the corpus.

### 3a. Stub generation

**Tool:** [`tools/generate/generate_stubs.py`](../tools/generate/generate_stubs.py).

**Output:** [`stubs/<version>/Live/*.pyi`](../stubs/12.3.6/Live/) — typed
Python stubs published as the `ableton-live-stubs` package via
[`tools/publish/build_package.py`](../tools/publish/build_package.py).

**Hand-curated:** none.

### 3b. Reference page generation

**Tool:** [`tools/generate/generate_reference.py`](../tools/generate/generate_reference.py).

**Output:** [`web/src/content/docs/modules/*.mdx`](../web/src/content/docs/modules/) — one MDX page per top-level Live module (43 today). The current step ladder (modules → classes → properties → property types → settable/listenable → ...) is tracked in [`reference-roadmap.md`](reference-roadmap.md).

**Hand-curated companions** in [`web/`](../web/):

| Path                                  | Purpose                                                        | Maintained by |
|---------------------------------------|----------------------------------------------------------------|----------------|
| `src/content/docs/index.mdx`          | Landing page                                                   | hand           |
| `src/styles/custom.css`               | Heading hierarchy, signature styling, behavior chips           | hand           |
| `astro.config.mjs`                    | Site config (base URL, sidebar, TOC depth, integrations)       | hand           |
| `src/components/`                     | Astro components for confidence badges, behavior, invariants   | hand (sparse — Phase 2 placeholder) |
| `src/content/docs/modules/*.mdx`      | One per module                                                 | **generated, do not edit** |

---

## Stage 4 — Site build

**Tool:** Astro + Starlight (`npm run build` in [`web/`](../web/)). Pulls in
the generated MDX, the hand-curated landing page, the CSS, and the config →
emits a static site under `web/dist/` → published to GitHub Pages at
`/LiveAPI/`.

---

## What's hand-curated vs generated

| Asset                                         | Source            | Drift risk |
|-----------------------------------------------|-------------------|------------|
| `tools/sets/<Set>.als`                         | hand              | low — only needs to exercise the API surface |
| `stubs/<v>/modules/*.md` (override blocks)    | hand (sourced)    | tracked via `from:` drift checks; verified against the corpus in CI |
| `web/src/content/docs/index.mdx`               | hand              | none (static landing page) |
| `web/src/styles/custom.css`, `astro.config.mjs`| hand              | low |
| `stubs/<v>/pipeline/LiveTree.parsed.v2.json`   | generated (Stage 2a) | regenerated from raw on every parse run; gitignored |
| `stubs/<v>/reports/seed/*.md`                 | generated (Stage 2b) | committed; algorithmic baseline for diffing against `modules/` |
| `stubs/<v>/Live/*.pyi`                         | generated (Stage 3a) | committed; published to PyPI |
| `web/src/content/docs/modules/*.mdx`           | generated (Stage 3b) | committed; published to GitHub Pages |

---

## Adjacent things that aren't in the main flow

- [`external/corpus/`](../external/) — Ableton's shipped Remote Scripts, fetched by [`tools/fetch_external/`](../tools/fetch_external/). Used as evidence (`source:` citations) when authoring overrides, and by [`tools/verify/`](../tools/verify/) to assert generated stubs accept the corpus. Not consumed by stub or reference generation directly.
- [`doc/live-api/*.md`](live-api/) — *legacy* hand-authored per-class notes from before the Starlight pivot. Currently untracked / not consumed by anything in the pipeline. Worth deciding whether to retire, fold into overrides as `source:` evidence, or carry forward into Phase 2 hypothesis records.
- **Hypothesis records (Phase 2, not yet implemented).** [`reference-design.md`](reference-design.md) describes a future authoring surface — YAML/JSON behavioral claims that get verified against running Live and rendered alongside the structural skeleton. None of this exists in the pipeline today; the current generator only renders what `modules/*.md` contains.

---

## Open questions for the architecture discussion

- Should hypothesis records (Phase 2) be a *third* input alongside `modules/*.md`, or merge into the module markdown before generation?
- Status of `doc/live-api/`: retire, port forward, or keep as scratchpad?
- Reference and stubs both consume `modules/*.md` directly today. As authored content grows, do we want an intermediate "rendered tree" stage that pre-resolves cross-references, link slugs, etc., so both consumers don't reimplement that logic?

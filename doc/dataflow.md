# Data Flow

How a Live runtime becomes published reference docs and typed stubs. This is a snapshot of the **current** wiring —
what's automated, what's hand-curated, where the data lives between stages. For _why_ each piece exists see
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
                │   runs:    tools/parse/parse_apicapture_results.py     │
                └────────────────────────────────────────────────────────┘
                                          │
                          LiveTree.parsed.json (immutable)
                                          ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 2b — BUILD MARKDOWN SEED                       │
                │   driver:  tools/parse/run_parse_pipeline.py           │
                │   runs:    tools/parse/build_lom_md.py                 │
                └────────────────────────────────────────────────────────┘
                                           │
                                 probe/<v>/seed/*.md
                                           │
   ┌─────────────────────────────────────┐ │
   │ content/<v>/                        │◀┘  (resync at intentional checkpoints)
   │   modules/*.md   ← per-module SOT   │
   │   *.md           ← 4 foundation     │
   │                    pages (flat)     │
   │ CURATED — seed + per-member         │
   │ refinement: blocks (each with       │
   │ confidence + sources) + prose       │
   └─────────────────┬───────────────────┘
                     ▼
              ┌──-───┴────────────────────────────────────────────┐
              ▼                                                   ▼
   ┌──────────────────────────────────┐         ┌──────────────────────────────────┐
   │  Stage 3a — STUBS                │         │  Stage 3b — REFERENCE PAGES      │
   │  tools/generate/                 │         │  tools/generate/                 │
   │    generate_stubs.py             │         │    generate_reference.py         │
   │                                  │         │                                  │
   │  → stubs/<v>/Live/*.pyi          │         │  → web/.../modules/*.mdx         │
   └────────────────┬─────────────────┘         └────────────────┬─────────────────┘
                    ▼                                            ▼
   ┌──────────────────────────────────┐         ┌──────────────────────────────────┐
   │  Stage 4a — STUB PACKAGE BUILD   │         │  Stage 4b — SITE BUILD           │
   │  tools/publish/                  │         │  npm run build (web/)            │
   │    build_package.py              │         │  Astro / Starlight integration   │
   │  → dist/*.whl + sdist → PyPI     │         │  → web/dist/ → GitHub Pages      │
   └──────────────────────────────────┘         └──────────────────────────────────┘
```

`content/<v>/` is the **single source of truth** that fans out into both renderings (stubs and reference). Per-module
markdown lives in `modules/<Module>.md`; the 4 cross-cutting foundation pages sit flat at the version root. Nothing is
hand-maintained twice. Each file holds fenced YAML blocks for structured fields plus authored prose between them —
format spec: [`lom-format.md`](lom-format.md).

---

## Stage 1 — Capture (inside Live)

**Tool:** [`tools/apicapture/`](../tools/apicapture/) — a Remote Script that loads as a Control Surface inside Ableton
Live.

**Driver:** [`tools/run_pipeline.py`](../tools/run_pipeline.py) launches Live with a known `.als` (from
[`tools/sets/`](../tools/sets/)) and uses `/tmp/apicapture_*` trigger files to invoke phases.

**Phases:**

| Phase         | Script                                                             | What it does                                                           |
| ------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| capture       | [`CaptureModule.py`](../tools/apicapture/scripts/CaptureModule.py) | Recursive `dir()` walk of the `Live` module → name/repr/doc/value tree |
| probe (basic) | [`PropertyProbe.py`](../tools/apicapture/scripts/PropertyProbe.py) | Visits live instances, reads each property, records runtime types      |
| probe (full)  | [`DeviceProbe.py`](../tools/apicapture/scripts/DeviceProbe.py)     | Loads every device through the browser to expose device-specific types |

**Outputs** (under [`probe/<version>/pipeline/`](../probe/12.3.6/pipeline/) — gitignored):

- `LiveTree.raw.json` — structural snapshot (the dir-walk tree). Consumed by Stage 2a.
- `LiveClasses.json` — runtime probe data keyed by class repr (property types, settable flags, no-arg getters,
  `constructable`, `iterable`/`container`/`element_type`). Consumed by Stage 2b's `build_lom_md.py` — Stage 2a's parser
  is raw_doc-driven and ignores it.

**Hand-curated inputs:** the `.als` set files in [`tools/sets/`](../tools/sets/) — Live needs _something_ loaded for
probes to have instances to walk.

**Not committed:** the raw outputs aren't in git (they're rebuildable from a running Live).

---

## Stage 2a — Parse (offline)

**Tool:** [`tools/parse/parse_apicapture_results.py`](../tools/parse/parse_apicapture_results.py) (invoked via
[`tools/parse/run_parse_pipeline.py`](../tools/parse/run_parse_pipeline.py)).

**Inputs:** `LiveTree.raw.json` from Stage 1.

Multi-step transform pipeline; each step takes the tree + a shared context dict and returns the transformed tree:

1. fix malformed Boost.Python class names
2. propagate the fixes through `raw_doc` strings
3. resolve inheritance (ancestors + relocate inherited members to defining class)
4. parse enum members from string-encoded forms, retype as `"enum"`
5. parse function docs into structured `signature` / `description` / C++ pairs, build C++→Python type map, resolve into
   clean args + returns

**Output:** [`probe/<version>/pipeline/LiveTree.parsed.json`](../probe/12.3.6/pipeline/) — the canonical parser output.
**Never hand-edited.**

**Hand-curated:** none. Mechanical transform of capture data only.

---

## Stage 2b — Build markdown seed (offline)

**Tool:** [`tools/parse/build_lom_md.py`](../tools/parse/build_lom_md.py) (also invoked via `run_parse_pipeline.py`).
Builds the per-module dict in memory and serializes via [`md_emit.convert()`](../tools/parse/md_emit.py).

**Inputs:** `LiveTree.parsed.json` (structural surface) + `LiveClasses.json` (probe — supplies `constructable`,
`iterable`/`container`/`element_type`, and probed property types).

Converts the parsed tree into one markdown file per top-level Live module, applying the algorithmic decisions a human
shouldn't have to make explicit:

- Type qualification (`Track` → `Live.Track.Track`)
- Optional widening (`T` + `default=None` → `T | None`)
- Enum widening (`E` → `E | int` — Boost.Python emits enums as int subclasses)
- Enum-from-default inference (bare `int` arg with default `Module.Enum.member` → `Enum | int`)
- Listener-triplet folding (`add_*_listener`/`remove_*_listener`/`*_has_listener` collapsed under the property)
- Parametric-container flag (`Live.Base.Vector` → `parametric: true`; renders as `Generic[T]`)
- Container detection (iterables exposing both `append` and `extend` → `container: true`; concrete subclasses inherit
  from `Vector[E]` and synthesize typed mutators at stub-render time)
- Inherited-property cleanup (drop properties identical to an ancestor's declaration so pyright resolves the annotation
  from the inherited declaration; keeps overrides intact)

**Output:** [`probe/<version>/seed/<Module>.md`](../probe/12.3.6/seed/) — the algorithmic baseline. Regenerated freely;
not hand-edited.

---

## The content/ SOT (curated)

**Location:** [`content/<version>/`](../content/12.3.6/). The version root holds two kinds of markdown:

- `content/<v>/modules/<Module>.md` — one file per top-level Live module (43 today). Started as a copy of
  `probe/<v>/seed/`. Each member's fenced YAML can carry a `refinement:` block where humans have tightened a probed
  value (a type, an element_type, an arg name). Each refinement holds the probed-as value (preserved as a diagnostic),
  `confidence` (`high` / `medium` / `low`), and a list of `sources` — bracketed-tag bullets citing the evidence (corpus
  def-site, M4L doc, raw_doc, C++ signature, sister method, probe). See [`lom-format.md`](lom-format.md) §"Refinement"
  for the locked shape.
- `content/<v>/*.md` (flat) — 4 foundation pages (`live-object-model.md`, `listeners.md`, `calling-conventions.md`,
  `remote-scripts.md`). Hand-authored prose for cross-cutting concepts; two of them (`live-object-model`, `listeners`)
  absorb a module's structural content via an `include_module:` directive in their frontmatter, so those modules don't
  render their own per-module page.

Filenames mirror their rendered URL slugs (`live-object-model.md` → `/LiveAPI/live-object-model/`), so the repo layout
is one-to-one with the site URL tree. Format spec: [`lom-format.md`](lom-format.md).

`probe/<v>/seed/` regenerates on every Stage 2 run; `content/<v>/` is only resynced at intentional checkpoints, so a
fresh capture won't trample existing refinements. The diff workflow crosses dirs:
`diff probe/<v>/seed/ content/<v>/modules/` shows exactly which facts have been hand-touched.

---

## Stage 3 — Two renderings of one SOT

Both consumers read `content/<v>/` and _only_ that. They never reach back to raw capture, M4L docs, or the corpus.

### 3a. Stub generation

**Tool:** [`tools/generate/generate_stubs.py`](../tools/generate/generate_stubs.py).

**Output:** [`stubs/<version>/Live/*.pyi`](../stubs/12.3.6/Live/) — typed Python stubs published as the
`ableton-live-stubs` package via [`tools/publish/build_package.py`](../tools/publish/build_package.py).

**Hand-curated:** none.

### 3b. Reference page generation

**Tool:** [`tools/generate/generate_reference.py`](../tools/generate/generate_reference.py).

**Output:** 45 generated MDX pages under [`web/src/content/docs/`](../web/src/content/docs/): 41 per-module pages at
`modules/<Module>.mdx` (LomObject and Listener are absorbed by their foundation pages and skipped here) plus 4
foundation pages flat at the docs root (`live-object-model.mdx`, `listeners.mdx`, `calling-conventions.mdx`,
`remote-scripts.mdx`). The current step ladder (modules → classes → properties → property types → settable/listenable →
...) is tracked in [`reference-roadmap.md`](reference-roadmap.md).

**Hand-curated companions** in [`web/`](../web/):

| Path                             | Purpose                                                      | Maintained by                       |
| -------------------------------- | ------------------------------------------------------------ | ----------------------------------- |
| `src/content/docs/index.mdx`     | Landing page                                                 | hand                                |
| `src/styles/custom.css`          | Heading hierarchy, signature styling, behavior chips         | hand                                |
| `astro.config.mjs`               | Site config (base URL, sidebar, TOC depth, integrations)     | hand                                |
| `src/components/`                | Astro components for confidence badges, behavior, invariants | hand (sparse — Phase 2 placeholder) |
| `src/content/docs/modules/*.mdx` | One per module                                               | **generated, do not edit**          |

---

## Stage 4 — Two distributions of one SOT

Stage 3's two renderings each get their own publish step. Both run on demand, not as part of the per-module generate
flow.

### 4a. Stub package build → PyPI

**Tool:** [`tools/publish/build_package.py`](../tools/publish/build_package.py). Reads `stubs/<v>/Live/*.pyi`, wraps it
as a PEP 561 stub-only package (`Live-stubs/` so `import Live` resolves), and writes a wheel + sdist to `dist/` plus a
zip archive for the GitHub release. The PyPI upload itself is a separate `twine upload dist/*` step.

### 4b. Site build → GitHub Pages

**Tool:** Astro + Starlight (`npm run build` in [`web/`](../web/)). Pulls in the generated MDX, the hand-curated landing
page, the CSS, and the config → emits a static site under `web/dist/` → published to GitHub Pages at `/LiveAPI/`.

---

## What's hand-curated vs generated

| Asset                                           | Source               | Drift risk                                                                   |
| ----------------------------------------------- | -------------------- | ---------------------------------------------------------------------------- |
| `tools/sets/<Set>.als`                          | hand                 | low — only needs to exercise the API surface                                 |
| `content/<v>/modules/*.md` (`refinement:` etc.) | hand (sourced)       | every refinement carries `sources:`; site renders provenance as a footnote   |
| `content/<v>/*.md` (4 foundation pages)         | hand                 | none (cross-cutting prose)                                                   |
| `web/src/content/docs/index.mdx`                | hand                 | none (static landing page)                                                   |
| `web/src/styles/custom.css`, `astro.config.mjs` | hand                 | low                                                                          |
| `probe/<v>/pipeline/LiveTree.parsed.json`       | generated (Stage 2a) | regenerated from raw on every parse run; gitignored                          |
| `probe/<v>/seed/*.md`                           | generated (Stage 2b) | committed; algorithmic baseline for diffing against `modules/`               |
| `stubs/<v>/Live/*.pyi`                          | generated (Stage 3a) | committed; published to PyPI; `regen-check` CI catches drift from SOT        |
| `web/src/content/docs/modules/*.mdx`            | generated (Stage 3b) | committed; published to GitHub Pages; `regen-check` + `web-build-check` gate |

---

## Adjacent things that aren't in the main flow

- [`external/corpus/`](../external/) — Ableton's shipped Remote Scripts, fetched by
  [`tools/fetch_external/`](../tools/fetch_external/). Used as evidence (`source:` citations) when authoring overrides,
  and by [`tools/verify/`](../tools/verify/) to assert generated stubs accept the corpus. Not consumed by stub or
  reference generation directly.
- [`doc/live-api/*.md`](live-api/) — _legacy_ hand-authored per-class notes from before the Starlight pivot. Currently
  untracked / not consumed by anything in the pipeline. Worth deciding whether to retire, fold into overrides as
  `source:` evidence, or carry forward into Phase 2 hypothesis records.
- **Hypothesis records (Phase 2, partial).** [`reference-design.md`](reference-design.md) describes the full authoring
  surface; the schema is locked in [`lom-format.md`](lom-format.md). `refinement:` records ship end-to-end (markdown →
  both generators → rendered footnote). `behavior:` and `quirks:` records have a locked schema but aren't rendered yet
  (planning in [`web-rendering.md`](web-rendering.md) §§2–3). Probe verification (Phase 3 in the roadmap) doesn't exist.

---

## Open questions for the architecture discussion

- Status of `doc/live-api/`: retire, port forward, or keep as scratchpad?
- Reference and stubs both consume `content/<v>/` directly today. As authored content grows, do we want an intermediate
  "rendered tree" stage that pre-resolves cross-references, link slugs, etc., so both consumers don't reimplement that
  logic?

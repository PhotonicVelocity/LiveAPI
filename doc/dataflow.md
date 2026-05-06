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
                │   Stage 2 — PARSE                                      │
                │   driver:  tools/parse/run_parse_pipeline.py           │
                │   runs:    tools/parse/parse_apicapture_results.py     │
                └────────────────────────────────────────────────────────┘
                                          │
                          LiveTree.parsed.json (immutable)
                                          │
   ┌────────────────────────────────┐     │
   │ tools/parse/                   │     │
   │   manual_refinements.yaml      │─────┤
   │ (HAND-CURATED, ~2000 lines)    │     │
   └────────────────────────────────┘     ▼
                ┌────────────────────────────────────────────────────────┐
                │   Stage 3 — REFINE                                     │
                │   driver:  tools/parse/run_parse_pipeline.py           │
                │   runs:    tools/parse/apply_manual_refinements.py     │
                └────────────────────────────────────────────────────────┘
                                          │
                          LiveTree.refined.json (committed)
                                          ▼
              ┌───────────────────────────┴───────────────────────────┐
              ▼                                                       ▼
   ┌──────────────────────────────────┐         ┌──────────────────────────────────┐
   │  Stage 4a — STUBS                │         │  Stage 4b — REFERENCE PAGES      │
   │  tools/generate/generate_stubs.py│         │  tools/generate/                 │
   │                                  │         │    generate_reference.py         │
   │  → stubs/<v>/Live/*.pyi          │         │  → web/.../modules/*.mdx         │
   └──────────────────────────────────┘         └──────────────────────────────────┘
                                                              │
                                                              ▼
                                                ┌──────────────────────────────────┐
                                                │  Stage 5 — SITE BUILD            │
                                                │  npm run build (web/)            │
                                                │  Astro / Starlight integration   │
                                                │  → web/dist/ → GitHub Pages      │
                                                └──────────────────────────────────┘
```

`LiveTree.refined.json` is the **single source of truth** that fans out into
both renderings (stubs and reference). Nothing is hand-maintained twice.

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

**Outputs** (under [`stubs/<version>/Live/`](../stubs/12.3.6/)):

- `LiveTree.raw.json` — structural snapshot (the dir-walk tree)
- `LiveClasses.json` — runtime probe data keyed by class repr (property types, settable flags, no-arg getters)

**Hand-curated inputs:** the `.als` set files in
[`tools/sets/`](../tools/sets/) — Live needs *something* loaded for probes to
have instances to walk.

**Not committed:** the raw outputs aren't in git (they're rebuildable from a
running Live). The committed `Live/` directory is the *generated stubs*, not
the raw capture (confusing naming — see Stage 3a).

---

## Stage 2 — Parse (offline)

**Tool:** [`tools/parse/parse_apicapture_results.py`](../tools/parse/parse_apicapture_results.py)
(invoked via [`tools/parse/run_parse_pipeline.py`](../tools/parse/run_parse_pipeline.py)).

**Inputs:** `LiveTree.raw.json` + `LiveClasses.json` from Stage 1.

Multi-step transform pipeline; each step takes the tree + a shared context dict and returns the transformed tree:

1. fix malformed Boost.Python class names
2. propagate the fixes through `raw_doc` strings
3. resolve inheritance (ancestors + relocate inherited members to defining class)
4. parse enum members from string-encoded forms, retype as `"enum"`
5. parse function docs into structured `signature` / `description` / C++ pairs, build C++→Python type map, resolve into clean args + returns
6. merge `LiveClasses.json` probe data onto matching tree nodes

**Output:** [`stubs/<version>/pipeline/LiveTree.parsed.json`](../stubs/12.3.6/pipeline/) —
the canonical parser output. **Never hand-edited.** Stage 3's drift
detection compares against this exact tree.

**Hand-curated:** none. Mechanical transform of capture data only.

---

## Stage 3 — Refine (offline)

**Tool:** [`tools/parse/apply_manual_refinements.py`](../tools/parse/apply_manual_refinements.py)
(also invoked via `run_parse_pipeline.py`).

**Inputs:** `LiveTree.parsed.json` + the hand-curated overrides file.

The only place in the pipeline where human knowledge enters the tree.
Kept as its own stage so the parsed tree stays immutable — drift detection
on the `from:` field of each refinement compares against fresh-parse output,
not a prior run's apply state.

**Hand-curated input:** [`tools/parse/manual_refinements.yaml`](../tools/parse/manual_refinements.yaml) — ~2000 lines of sourced overrides.

Schema per dotted path: `args:` rename positional args, `arg_types:` /
`return_type:` / `probed_type:` / `element_repr:` override types. Each entry
**requires** a `source:` field (corpus def-site, M4L doc citation, raw_doc
text). Type-changing entries also require a `confidence:` level (`high` /
`medium` / `low`).

**Drift safety:** every type-changing entry can include a `from:` value the
applier validates against the parsed-tree value, so a Live-version change
that shifts parser output surfaces as a warning rather than being silently
absorbed.

**Output:** [`stubs/<version>/pipeline/LiveTree.refined.json`](../stubs/12.3.6/pipeline/LiveTree.refined.json) — the source of truth for everything downstream.

---

## Stage 4 — Two renderings of one tree

Both consumers read `LiveTree.refined.json` and *only* that file. They
never reach back to raw capture, M4L docs, or the corpus.

### 4a. Stub generation

**Tool:** [`tools/generate/generate_stubs.py`](../tools/generate/generate_stubs.py).

**Output:** [`stubs/<version>/Live/*.pyi`](../stubs/12.3.6/Live/) — typed
Python stubs published as the `ableton-live-stubs` package via
[`tools/publish/build_package.py`](../tools/publish/build_package.py).

**Hand-curated:** none.

### 4b. Reference page generation

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

## Stage 5 — Site build

**Tool:** Astro + Starlight (`npm run build` in [`web/`](../web/)). Pulls in
the generated MDX, the hand-curated landing page, the CSS, and the config →
emits a static site under `web/dist/` → published to GitHub Pages at
`/LiveAPI/`.

---

## What's hand-curated vs generated

| Asset                                         | Source            | Drift risk |
|-----------------------------------------------|-------------------|------------|
| `tools/sets/<Set>.als`                         | hand              | low — only needs to exercise the API surface |
| `tools/parse/manual_refinements.yaml`          | hand (sourced)    | tracked via `from:` drift checks; verified against the corpus in CI |
| `web/src/content/docs/index.mdx`               | hand              | none (static landing page) |
| `web/src/styles/custom.css`, `astro.config.mjs`| hand              | low |
| `stubs/<v>/pipeline/LiveTree.parsed.json`      | generated (Stage 2)  | regenerated from raw on every parse run |
| `stubs/<v>/pipeline/LiveTree.refined.json`     | generated (Stage 3)  | committed; rebuilt when refinements or capture change |
| `stubs/<v>/Live/*.pyi`                         | generated (Stage 4a) | committed; published to PyPI |
| `web/src/content/docs/modules/*.mdx`           | generated (Stage 4b) | committed; published to GitHub Pages |

---

## Adjacent things that aren't in the main flow

- [`external/corpus/`](../external/) — Ableton's shipped Remote Scripts, fetched by [`tools/fetch_external/`](../tools/fetch_external/). Used as evidence (`source:` citations) when authoring refinements, and by [`tools/verify/`](../tools/verify/) to assert refined stubs accept the corpus. Not consumed by stub or reference generation directly.
- [`doc/live-api/*.md`](live-api/) — *legacy* hand-authored per-class notes from before the Starlight pivot. Currently untracked / not consumed by anything in the pipeline. Worth deciding whether to retire, fold into refinements as `source:` evidence, or carry forward into Phase 2 hypothesis records.
- **Hypothesis records (Phase 2, not yet implemented).** [`reference-design.md`](reference-design.md) describes a future authoring surface — YAML/JSON behavioral claims that get verified against running Live and rendered alongside the structural skeleton. None of this exists in the pipeline today; the current generator only renders what `LiveTree.refined.json` contains.

---

## Open questions for the architecture discussion

- Should hypothesis records (Phase 2) be a *third* input alongside `LiveTree.refined.json`, or merge into the refined tree before generation?
- Is `manual_refinements.yaml` the right home for prose (descriptions, quirks, examples) too, or does that surface deserve its own authored format?
- Status of `doc/live-api/`: retire, port forward, or keep as scratchpad?
- Reference and stubs both consume `LiveTree.refined.json` directly today. As authored content grows, do we want an intermediate "rendered tree" stage that pre-resolves cross-references, link slugs, etc., so both consumers don't reimplement that logic?

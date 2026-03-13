# Decisions

Architectural and formatting decisions for the LiveAPI project. Updated as decisions are made.

## Terminology

- **Live Object Model (LOM)** — the object hierarchy exposed by Live's Python runtime. Not Max-specific; the same model
  is accessed by Remote Scripts, Max for Live, and external clients like LiveRelay. Prefer "LOM" or "Live Object Model"
  over "Live Python API" when referring to the object structure.

## Project Structure

- **`reference/`** is the product. Everything else exists to produce and maintain it.
- **`tools/`** holds all introspection, probing, and parsing tooling. Keeping it in this repo (not a separate one) to
  avoid cross-repo coordination overhead.
  - **`tools/apicapture/`** — APICapture Control Surface (runs inside Live, captures raw tree + probes properties).
  - **`tools/parse/`** — parsing and stub generation pipeline (see [Parse Pipeline](#parse-pipeline) below).
  - **`tools/other/`** — legacy/utility scripts not yet integrated into the main pipeline.
  - **`tools/install.py`** — installs APICapture to Live's Remote Scripts folder.
  - **`tools/justfile`** — shortcuts for install/build/reload workflow.
  - **`tools/sets/`** — Ableton Live sets used with APICapture for probing.
- **`build/`** — per-version build artifacts. Each version directory (e.g. `build/12.3.6/`) contains the full pipeline
  output: raw capture, probe results, parsed tree, refinements, resolved tree, and generated stubs.
- **`MaxForLive/`** — API docs parsed from Max for Live HTML documentation. Used as cross-reference for type refinement.
- **`doc/`** — project-level documentation (this file, contributing guide, pipeline plans).
- **`web/`** removed — replaced by MkDocs + GitHub Pages.

## Parse Pipeline

The pipeline transforms raw API captures into typed Python stubs through four stages:

```
                          APICapture (inside Live)
                                   │
                          LiveTree.raw.json + LiveClasses.json
                                   │
                    ┌──────────────┴──────────────┐
                    │  parse_apicapture_results.py │  Stage 1: Parse & enrich
                    └──────────────┬──────────────┘
                          LiveTree.parsed.json
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                     │
     extract_unresolved.py   resolve_unresolved.py      │
              │                    │                     │
        unresolved.json      refinements.json           │
              │                    │                     │
              └────────────────────┘                     │
                                   │                     │
                    ┌──────────────┴──────────────┐      │
                    │    apply_refinements.py      │  Stage 2: Refine
                    └──────────────┬──────────────┘
                          LiveTree.resolved.json
                                   │
                    ┌──────────────┴──────────────┐
                    │      generate_stubs.py       │  Stage 3: Generate
                    └──────────────┬──────────────┘
                             Live/*.pyi
```

**Stage 1 — Parse** (`parse_apicapture_results.py`): Reads `LiveTree.raw.json` + `LiveClasses.json`, applies
inheritance resolution, doc parsing, signature parsing, probe data merging. Outputs `LiveTree.parsed.json`.

**Stage 2 — Refine**: Three scripts work together:

- `extract_unresolved.py` — scans parsed tree for `object`-typed args, `argN`-named params, `object` returns, and null
  property types. Outputs `unresolved.json`.
- `resolve_unresolved.py` — produces `refinements.json` from hand-curated overrides (sourced from Notes.md, MaxForLive
  docs, and decompiled remote scripts). 201/201 items resolved.
- `apply_refinements.py` — applies `refinements.json` to `LiveTree.parsed.json`, producing `LiveTree.resolved.json`
  with all arg names, arg types, return types, and property types baked in.

**Stage 3 — Generate** (`generate_stubs.py`): Reads `LiveTree.resolved.json` and emits `.pyi` stub files. The generator
has no refinement logic — it renders the tree as-is. Each namespace module becomes a package directory; classes, enums,
functions, and properties are rendered according to their node type with proper `TYPE_CHECKING` imports.

All scripts live in `tools/parse/` and accept a version argument (e.g. `python tools/parse/generate_stubs.py 12.3.6`).

## Reference Format

### Page structure

Each reference file documents one LOM class:

1. **Title** — class name as H1 (`# Song`), with full path in a blockquote (`> Live.Song.Song`).
2. **Description** — what this represents in Live, when you'd interact with it.
3. **Raw probe notes (temporary)** — collapsed admonition for unprocessed findings. These are transitional; as tooling
   matures, raw notes move to probe scripts/data files and are removed from the reference.
4. **Children** — summary table + per-child detail sections.
5. **Properties** — summary table + per-property detail sections.
6. **Methods** — summary table + per-method detail sections.
7. **Enums** — value tables for enum types defined by this class.
8. **Open Questions** — unresolved behavior that needs probing.

### Member detail sections

Each child, property, or method gets:

- **Metadata** — type, listenable, since version. Kept minimal.
- **Description** — what it does, including distilled probe findings.
- **Quirks** (optional) — non-obvious behavior, gotchas.
- **Limitations** (optional) — constraints on when/where it works.

### What's NOT in the reference

- **Sources / Probe Status per member** — contributor metadata, not user-facing. Track in contributing guide or coverage
  file.
- **Raw probe dumps in member sections** — findings should be distilled into descriptions/quirks/limitations. Raw notes
  stay at the class level (collapsed) only as a transitional measure.
- **Undo-tracked / Async visibility / Applicable to** — removed from per-member metadata. Too verbose and mostly
  `Unknown`. Document in description or quirks when it matters.

### Summary tables

Kept narrow for scannability:

- **Children:** Child, Returns, Shape, Listenable, Summary
- **Properties:** Property, Type, Settable, Listenable, Summary
- **Methods:** Method, Returns, Summary

### Format template

`_Format.md` will move from `reference/` to the contributing guide so MkDocs doesn't render it as a page.

## Navigation

Organized by LOM hierarchy (not flat alphabetical):

```
Live Set (Song)
├── Tracks
│   ├── Track
│   ├── MixerDevice
│   ├── ClipSlot
│   └── Clip
├── Scenes
├── Devices
│   ├── Device / DeviceParameter
│   ├── RackDevice / Chain
│   ├── DrumPad / DrumChain
│   └── Subclasses (Simpler, Drift, Wavetable, etc.)
├── Browser
├── Application
└── Other (Groove, TuningSystem, Conversions, etc.)
```

This mirrors how people think about Live's structure and matches the parent-child relationships in the LOM.

## Publishing

- **MkDocs + Material theme** — renders `reference/` as a searchable site with sidebar navigation.
- **GitHub Pages** — deployed via GitHub Actions on push to main.
- **Markdown stays the source of truth** — GitHub browsing still works alongside the site.

## Tooling Direction (future)

- Probing and parsing should eventually generate reference content automatically.
- Raw probe notes in the reference are temporary — the goal is a clean pipeline:
  `stubs + M4L docs + probe results → parser → reference markdown`.
- Whether probes use the APICapture Control Surface or LiveRelay is TBD.
- **LLM-assisted resolution** — `unresolved.json` includes full context (descriptions, signatures, C++ signatures) for
  each item. A future `--llm` mode on `resolve_unresolved.py` could propose refinements for review, useful as the API
  evolves across Live versions.
- **M4L probe device** — some LOM types (e.g. `ControlSurfaceProxy`) are only reachable from the Max for Live process,
  not from a control surface script. APICapture runs in the control surface process, so it sees actual
  `ControlSurface` objects rather than proxies. A small M4L device could probe these M4L-only types by reading
  properties and writing results to a JSON file for the main pipeline to merge. Low priority since
  `ControlSurfaceProxy` is currently the only known case, and it was resolved via decompiled source.

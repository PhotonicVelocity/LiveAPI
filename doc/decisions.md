# Decisions

Architectural and formatting decisions for the LiveAPI project. Updated as decisions are made.

## Terminology

- **Live Object Model (LOM)** — the object hierarchy exposed by Live's Python runtime. Not Max-specific; the same model
  is accessed by Remote Scripts, Max for Live, and any RPC bridges that wrap the runtime. Prefer "LOM" or "Live Object
  Model" over "Live Python API" when referring to the object structure.

## Project Structure

- **`reference/`** is the product. Everything else exists to produce and maintain it.
- **`tools/`** holds all introspection, probing, and parsing tooling. Keeping it in this repo (not a separate one) to
  avoid cross-repo coordination overhead.
  - **`tools/apicapture/`** — APICapture Control Surface (runs inside Live, captures raw tree + probes properties).
  - **`tools/parse/`** — parsing and stub generation pipeline (see [Parse Pipeline](#parse-pipeline) below).
  - **`tools/other/`** — legacy/utility scripts not yet integrated into the main pipeline.
  - **`tools/install.py`** — installs APICapture to Live's Remote Scripts folder.
  - **`tools/sets/`** — Ableton Live sets used with APICapture for probing.
- **`stubs/`** — per-version generated stubs. Each version directory (e.g. `stubs/12.3.6/`) contains `Live/` (tracked
  final output) and `pipeline/` (gitignored intermediates: raw capture, parsed tree, refinements, etc.).
- **`MaxForLive/`** — API docs parsed from Max for Live HTML documentation. Used as cross-reference for type refinement.
- **`doc/`** — project-level documentation (this file, contributing guide, pipeline plans).
- **`web/`** removed — replaced by MkDocs + GitHub Pages.

## Stub Accuracy and Pipeline Posture

**Principle.** Stubs exist to give Remote Script developers type checking and autocomplete. Accuracy beats
prettiness — a stub that misleads is worse than one that looks generic. The Live API binding is messy
(Boost.Python positional-only, runtime type coercion, internal C++ crashes on bad input); the stubs should
reflect what the binding actually does, not what its prose documentation suggests.

### What's already correct

The current stubs emit **PEP 570 positional-only markers (`, /`)** on every callable method with args.
Pyright and mypy reject kwarg calls (`zoom_view(direction=1, ...)`) at type-check time. Names in the
signature serve as readable labels for autocomplete hints, hover docs, and pyright error messages — but
cannot be used as kwargs in checked code. This is the right answer to "how do we keep readable names
without letting users type them as kwargs"; it stays.

### Failure modes to avoid

- **Types looser than the binding accepts.** Pyright accepts a Python `list`; the underlying Boost.Python
  binding requires the specific `TVector` type and crashes with `InternalError`. Concrete example today:
  `Clip.add_new_notes(notes: Iterable[MidiNoteSpecification] | None, /)` — sister method
  `apply_note_modifications` is documented as failing exactly this way at runtime. This is the
  highest-impact misleading class because `, /` doesn't help — pyright still accepts a wrong-type call.
- **Pervasive `T | None` parser defaults.** Today's parser widens every positional arg to `T | None`.
  Pyright accepts `None`; the runtime usually crashes. Visible across most stub files; not introduced by
  the LLM — this is a parser default. Affects every method, every property setter; the broadest
  misleading surface in the codebase.
- **Name semantics that don't describe the parameter accurately.** Lower-stakes than the above (`, /`
  prevents kwarg calls, so pyright won't accept `f(wrong_name=...)`) but still affects hover hints and IDE
  inlay-hint readability. A name from a source that misjudges intent — e.g., a doc that names the M4L
  proxy parameter rather than the underlying binding's conceptual parameter — misleads readers about what
  the arg means even when they can't call it as a kwarg.

### Decisions

1. **Version coverage: latest 12.x only.** Drop active maintenance of earlier versions. The repo tracks
   only the current `stubs/12.x.y/` directory; older versions (`stubs/11.*`, `stubs/12.0–12.2`) have been
   removed. Anyone needing older-version stubs can rebuild from a tagged commit (the apicapture pipeline
   still supports 11.x via `tools/sets/Set 11 Project/`).

2. **Refinement strictness — only what we can scrape from Live itself.** All signature content comes from
   sources that observe the binding directly. With `, /` (PEP 570) on every callable, kwarg-callability is
   already prevented by the type checker; names are decorative labels for autocomplete and hover. That
   removes the loudest misleading-stubs failure mode but doesn't license loose sourcing — names that
   don't accurately describe the parameter still mislead readers about meaning.
   - Arg **names**: from the parsed C++ signature embedded in the raw docstring (when non-generic) or
     structural inference. Otherwise `argN`. **No external doc lookups** — not callsite analysis on
     decompiled Remote Scripts, not MaxForLive docs, not LLM resolution. Each is evidence of how someone
     _used_ the API, not evidence of how the binding is _defined_.
   - Arg **types**: from probe data (type observed at runtime) or parsed C++ signature only. Otherwise
     `Any`. Prose docstrings and M4L type claims are not acceptable type sources.
   - Return **types** and property **types**: same rule — what we observed from Live, otherwise `Any`.
   - Generic-looking but truthful beats pretty but wrong.

3. **MaxForLive docs: docstring-only.** M4L describes a related-but-distinct API. Its content flows into
   `.pyi` docstrings as informational prose ("Max for Live names this parameter `direction`") and never
   into signatures. The LLM-resolve pipeline used M4L docs to drive both names and types into
   signatures; that path is the misleading-stubs risk we're correcting.

4. **LLM-resolve and callsite-resolve both removed.** Both relied on external evidence about how someone
   uses the API rather than what Live itself reports — the LLM via M4L docs and prose docstrings,
   `callsite_resolve.py` via decompiled Ableton Remote Scripts. Same accuracy concern, same drop. The
   pipeline becomes the minimal capture → parse → generate. If a specific case surfaces during the
   parser audit (decision #5) or later that genuinely needs a hand-stamped override, a
   `manual_refinements.json` may be added with a strict bar (rationale and source citation per entry);
   not added by default.

5. **Parser defaults audit (same branch as LLM removal).** `parse_apicapture_results.py` currently emits
   `T | None` on every positional arg as a defensive default. This is the broadest misleading surface in
   the codebase, and removing the LLM does not fix it. The cleanup branch (`stub-pipeline-cleanup`)
   audits every parser-introduced widening and emits the captured type without unwarranted `| None`
   decoration.

6. **Stub usability tests in CI.** `ast.parse()` on every emitted `.pyi` (syntax validity) and `pyright`
   against the stubs themselves (internal consistency) are wired into CI on the cleanup branch. Both gate
   any change that would alter the stubs.

### What this changes operationally

- The Parse Pipeline section below describes the active minimal pipeline on `main` after the cleanup.
- `MaxForLive/` stays in the repo as input — the new pipeline reads it for prose content that flows into
  stub docstrings only. Its names, types, and shape claims do not reach signatures.
- `external/corpus/` (gitignored) keeps its role as the corpus for
  Tier 4 usage tests but no longer participates in stub generation.

## Parse Pipeline

The pipeline transforms raw API captures into typed Python stubs through three stages:

```
                          APICapture (inside Live)
                                   │
                          LiveTree.raw.json + LiveClasses.json
                                   │
                    ┌──────────────┴──────────────┐
                    │  parse_apicapture_results.py │  Stage 2: Parse
                    └──────────────┬──────────────┘
                          LiveTree.parsed.json
                                   │
                    ┌──────────────┴──────────────┐
                    │      generate_stubs.py       │  Stage 3: Generate
                    └──────────────┬──────────────┘
                             Live/*.pyi
```

**Stage 1 — Capture + Probe** (inside Live, via APICapture Control Surface). Produces `LiveTree.raw.json`
(structural tree from `dir()` walking) and `LiveClasses.json` (runtime property probe results).

**Stage 2 — Parse** (`parse_apicapture_results.py`): Reads the raw capture and probe outputs and produces
`LiveTree.parsed.json`. Applies class-name fixes, inheritance resolution, member relocation, enum parsing,
function-doc parsing, signature parsing, type resolution, and probe data merging. This is the only refinement
step the pipeline performs — there is no LLM resolution, no callsite analysis, no hand-stamped overrides.
Only what we scrape from Live itself reaches the stubs (see [Stub Accuracy and Pipeline
Posture](#stub-accuracy-and-pipeline-posture) above).

**Stage 3 — Generate** (`generate_stubs.py`): Reads `LiveTree.parsed.json` and emits `.pyi` stub files.
Renders the tree as-is; each namespace module becomes a flat `.pyi` file under the `Live/` package,
mirroring the real C extension module layout (`Live.Song` is a flat module, not a package).

All scripts live in `tools/` and accept a version argument
(e.g. `python tools/parse/parse_apicapture_results.py 12.3.6`). The orchestrators are
`tools/run_pipeline.py` (full Stage 1 + 2 + 3) and `tools/parse/run_parse_pipeline.py` (Stage 2 only).

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

## Tooling Direction

- Probing and parsing should eventually generate reference content automatically.
- Raw probe notes in the reference are temporary — the goal is a clean pipeline:
  `stubs + M4L docs + probe results → parser → reference markdown`.
- Probes run via the APICapture Control Surface (see `tools/apicapture/`).
- **M4L probe device** — some LOM types (e.g. `ControlSurfaceProxy`) are only reachable from the Max for Live process,
  not from a control surface script. APICapture runs in the control surface process, so it sees actual
  `ControlSurface` objects rather than proxies. A small M4L device could probe these M4L-only types by reading
  properties and writing results to a JSON file for the main pipeline to merge. Low priority since
  `ControlSurfaceProxy` is currently the only known case, and it was resolved via decompiled source.

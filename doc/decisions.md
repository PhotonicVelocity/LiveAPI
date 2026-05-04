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
  `apply_note_modifications` is documented as failing exactly this way (P4L work confirms). This is the
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

1. **Version coverage: latest 12.x only.** Drop active maintenance of earlier versions. Existing
   `stubs/11.*` and `stubs/12.0–12.2` directories remain as frozen historical artifacts but no longer
   participate in regeneration. Anyone needing older-version stubs can rebuild from a tagged commit.

2. **Refinement strictness — signatures carry verified types; names are descriptive labels.** With `, /`
   in place, kwarg-callability is not the bar for arg names. The bar shifts:
   - Arg **names**: emit any informative descriptor sourced from callsite analysis, parsed C++ signature
     (when non-generic), MaxForLive docs, or hand-stamped manual overrides. Otherwise `argN`. The name is
     a readable label; `, /` already prevents kwarg use.
   - Arg **types**: must reflect what the underlying binding actually accepts. Sources: probe data (the
     type observed at runtime), parsed C++ signature, hand-stamped manual overrides. Otherwise `Any`.
     Prose docstrings and M4L type claims are **not** acceptable type sources — they describe a
     related-but-distinct API.
   - Return **types** and property **types**: same rule — verified sources only, otherwise `Any`.
   - Generic-looking but truthful beats pretty but wrong.

3. **MaxForLive docs: split role.** Names from M4L docs are acceptable in signatures (paired with `, /`
   they're descriptive labels, not callable kwargs). Types and shape claims from M4L are demoted to
   docstrings only. The current LLM-resolve pipeline used M4L docs to drive both names and types into
   signatures; the type-side of that is the misleading-stubs risk we're correcting.

4. **LLM-resolve removed.** With kwarg-callability solved structurally by `, /`, the LLM's main output
   (arg names, ~61% of its fixes) is lower-stakes — but a deterministic name lookup using the same
   sources (M4L docs, callsite, parsed C++ signature) does the same job without an API key, batched calls,
   nondeterminism, or per-version cost. For the LLM's type-resolution work (~39% of its fixes), prose-
   inferred types are exactly the wrong source given the strictness rule above. Replaced by
   `manual_refinements.json` for hand-curated overrides plus the existing `callsite_resolve.py`. The
   pipeline becomes capture → parse → resolve (callsite + probe + manual) → generate.

5. **Parser defaults audit (same branch as LLM removal).** `parse_apicapture_results.py` currently emits
   `T | None` on every positional arg as a defensive default. This is the broadest misleading surface in
   the codebase, and removing the LLM does not fix it. The cleanup branch (`stub-pipeline-cleanup`)
   audits every parser-introduced widening and emits the captured type without unwarranted `| None`
   decoration.

6. **Stub usability tests in CI.** `ast.parse()` on every emitted `.pyi` (syntax validity) and `pyright`
   against the stubs themselves (internal consistency) are wired into CI on the cleanup branch. Both gate
   any change that would alter the stubs.

### What this changes operationally

- The Parse Pipeline section below describes the **current** pipeline (LLM-resolve still in place). It
  will be revised when the cleanup branch lands. Until then, the description is accurate to `main` only.
- `tools/parse/llm_resolve.py`, `tools/parse/llm_resolve_prompt.md`, and the LLM-prompt-related parts of
  `tools/parse/llm_hints.md` are slated for deletion. The deterministic-hint content of `llm_hints.md`
  migrates to `manual_refinements.json`.
- `MaxForLive/` stays in the repo as input. The new pipeline reads it for: (a) arg names that make their
  way into signatures (paired with `, /`, decision #3); (b) prose content that flows into stub docstrings.
  Its type/shape claims are not consumed.
- `extract_unresolved.py` stays. Its output becomes the queue of "things still needing a hand-stamped
  answer" — consumed when populating `manual_refinements.json` rather than by the LLM.

## Parse Pipeline

> _Note: this section describes the pipeline on `main` today. It will be rewritten when the
> `stub-pipeline-cleanup` branch lands per the Stub Accuracy decisions above._

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
     extract_unresolved.py    llm_resolve.py            │
              │                    │                     │
        unresolved.json    refinements.llm.json         │
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
- `llm_resolve.py` — produces `refinements.llm.json` using Claude to resolve unresolved items. Sends items along with a
  type skeleton, MaxForLive docs, and curated reference docs as context. Supports batch processing via `--prepare` /
  `--merge` or direct API calls. System prompt is in `llm_resolve_prompt.md`.
- `apply_refinements.py` — applies `refinements.llm.json` to `LiveTree.parsed.json`, producing `LiveTree.resolved.json`
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

## Tooling Direction

- Probing and parsing should eventually generate reference content automatically.
- Raw probe notes in the reference are temporary — the goal is a clean pipeline:
  `stubs + M4L docs + probe results → parser → reference markdown`.
- Whether probes use the APICapture Control Surface or LiveRelay is TBD.
- **M4L probe device** — some LOM types (e.g. `ControlSurfaceProxy`) are only reachable from the Max for Live process,
  not from a control surface script. APICapture runs in the control surface process, so it sees actual
  `ControlSurface` objects rather than proxies. A small M4L device could probe these M4L-only types by reading
  properties and writing results to a JSON file for the main pipeline to merge. Low priority since
  `ControlSurfaceProxy` is currently the only known case, and it was resolved via decompiled source.

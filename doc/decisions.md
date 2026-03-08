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
- **`build/`** and **`MaxForLive/`** are source material — inputs to the reference docs, not end-user deliverables.
- **`web/`** removed — replaced by MkDocs + GitHub Pages.
- **`set/`** moved to `tools/set/` — used by introspection tooling.

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
- Whether probes use the MakeDoc Control Surface or LiveRelay is TBD.

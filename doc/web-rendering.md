# Web rendering of LOM annotations

Planning doc for how each annotation type in `content/<v>/modules/<Module>.md` flows to the rendered Starlight site.
The goal: for every record type the spec defines, lock down what the **markdown source** looks like and what the
**rendered page** does with it, before we write the code. Parser/adapter internals stay out of this doc.

> **Status.** Iteration scratch. Each section below has a "Source" example, a "Renders as" sketch, a "Status" line
> noting whether code exists, and an "Open" list of decisions still to make. Iterate freely — nothing here is locked.

## Vocabulary

The rendered site uses a small set of building blocks. New record types should compose from these rather than invent
new visual primitives.

- **Chip** — small colored pill on a heading or value, conveying status (`core`, `deprecated`, `synthesized`,
  `confidence: high`, etc.). Already used for the foundation-page sidebar badge and the confidence row inside override
  tooltips.
- **Footnote** — a superscript marker (`*`, `†`, numbered) attached to a value or heading; hover/focus reveals a
  structured tooltip with rows of data (confidence, probed value, evidence bullets, prose). One primitive — what GFM
  spells `[^id]` and what `override_marker_html()` already produces are the same visual thing. Three source forms all
  flow into the same marker-and-tooltip rendering:
  1. **Unreferenced record on a member** — `behavior:` / `quirks:` / `refinement:` / `deprecated:` entry with no
     inline `[^id]` referrer. Marker auto-attaches to the member heading (or to the refined field in the signature).
  2. **Inline reference** — `[^id]` in the member's prose body, resolved against the record with that `id:` on the
     same member. Marker placed at the `[^id]` site instead of on the heading.
  3. **Inline anonymous footnote** — `^[short body]` (Pandoc-style inline footnote) in the prose body, with the body
     text becoming the entire tooltip content. No record needed; for parenthetical asides too small to deserve a
     structured `behavior:` entry. Marker placed at the `^[...]` site.
- **Callout** — block-level admonition (`note`, `caution`, `tip`) embedded in the member's body. For prose-shaped
  content too long for a tooltip — long form quirks, multi-paragraph behavior write-ups, deprecation notes with
  migration steps.

## Annotation types

### 1. `refinement:` — type / name / element_type overrides

**Source** (member fenced YAML):

```yaml
type: Live.Base.Vector[Live.Device.Device]
refinement:
  type:
    probed: Live.Base.Vector[Live.LomObject.LomObject]
    confidence: high
    sources:
      - "[C++ signature] binding declares element type as LomObject."
      - "[corpus] Push2/device_navigation.py indexes chain.devices[i] as Device."
```

**Renders as:** footnote (marker + tooltip) attached to the refined value in the signature. Tooltip body: confidence
chip, probed-as row, evidence bullets with tag chips (`[corpus]`, `[C++ signature]`, ...).

**Status:** ✅ wired. `override_marker_html()` in `generate_reference.py:134` produces the marker + tooltip; CSS classes
`.override-marker`, `.override-marker-tooltip`, `.ot-confidence-*`, `.ot-tag-*` already styled. Treat this as the
reference implementation for the footnote primitive — other record types (behavior, quirks) reuse the same plumbing.

**Open:**

- One marker per refined field (current: separate marker on `type` vs `element_type`) vs one marker per record
  (consolidated). Current granularity feels right — confirm.

### 2. `behavior:` — runtime assertions

**Source:**

```yaml
behavior:
  - id: excludes-mixer
    assertion: "The vector excludes the chain's mixer_device."
    confidence: high
    verified_against: "12.3.6"
    sources:
      - "[probe] iterating chain.devices on a populated rack never yields mixer_device."
```

**Renders as:** footnote (same primitive as refinement). Placement depends on whether the record is referenced
inline:

- **With inline `[^id]` in prose** — marker placed at that phrase, tooltip body shows the assertion + sources.
- **Without inline `[^id]`** — marker auto-attaches to the member heading. Multiple unreferenced records → multiple
  markers on the heading.

Tooltip body for behavior:

- Assertion (headline)
- Confidence chip
- `verified_against:` row (with staleness chip when older than current `<v>`)
- Sources bullets with `[tag]` chips (reuse refinement source rendering)

**Status:** ❌ not rendered. Plumbing reuses `override_marker_html()` structure.

**Open:**

- Long-form assertions (multi-sentence, paragraph-shaped) may overflow a tooltip. Threshold for promoting to a
  callout in the body? Probably "if the source markdown has multiple paragraphs."

### 3. `quirks:` — gotchas

**Source:**

```yaml
quirks:
  - id: tempo-clamp
    assertion: "Setting tempo outside [20.0, 999.0] silently clamps to the nearest bound."
    sources:
      - "[probe] song.tempo = 1500 → reads back 999.0."
```

**Renders as:** footnote, same as behavior. Same marker placement rules (inline `[^id]` → at phrase; otherwise → on
heading). Visual distinction is a colour/icon on the marker glyph itself (e.g. blue for behavior, amber for quirk) —
single render path, two skins.

**Status:** ❌ not rendered. Same plumbing as behavior.

**Open:**

- Should quirks ever escalate to a body-level callout for prominence? Probably no — by spec they're "gotchas worth
  flagging," tooltip is enough.

### 4. Inline footnote sources (`[^id]` and `^[body]`)

**Source** (prose body of a member). Two forms:

```markdown
Devices contained in the chain. The vector excludes the chain's `mixer_device`[^excludes-mixer] — that lives on a
separate property.

Setting `tempo` outside the supported range^[Clamps to [20.0, 999.0]; observed via probe.] silently clamps.
```

- `[^excludes-mixer]` is a **reference** to a structured record (`behavior:` / `quirks:` / `refinement:`) defined in
  the member's frontmatter. The renderer looks up the id and uses that record's tooltip body.
- `^[Clamps to ...]` is an **anonymous inline footnote**. The bracketed body is the entire tooltip content; no record
  to look up. For parenthetical asides too small to deserve a full structured entry.

**Renders as:** *not* a separate render type — both forms produce the same marker+tooltip primitive used elsewhere.
The id-resolved form populates the tooltip from the structured record; the anonymous form populates it from the
inline body text.

**Status:** ❌ not wired end-to-end. The renderer needs a generator-side rewrite pass over member prose that:

1. Scans for both `[^id]` and `^[body]` occurrences.
2. For `[^id]`: looks up the matching record on the member, renders the marker with that record's tooltip body,
   suppresses the record from the auto-attached-to-heading list.
3. For `^[body]`: renders a marker whose tooltip body is the inline text (treat as a minimal record:
   `{ assertion: body }` — no confidence, no sources, no id).

**Open:**

- Default GFM/remark handling of `[^id]` will render as a numbered bottom-of-page footnote if we don't intercept —
  rewrite must happen at MDX-emit time (in `generate_reference.py`), not site-build time.
- Pandoc's `^[body]` inline syntax isn't standard CommonMark/GFM. Either we intercept it ourselves in the generator
  (preferred — same rewrite pass as `[^id]`) or pick a different sigil that won't collide with anything in the prose.
- Behavior when an `[^id]` doesn't resolve — leave as broken marker, drop with a warning, or error at generate time?

### 5. `raw_doc` vs authored prose

The body text under a member always renders the same way — readers don't see a visual distinction between authored
prose and runtime docstring. A footnote marker appended to the end of the body is the source signal: hover/focus
reveals the provenance.

**Source — two real states:**

```yaml
##### devices

raw_doc: "Return const access to all available Devices that are present in the chains"
```

```yaml
##### devices

raw_doc: "Return const access to all available Devices that are present in the chains"
```

> Devices contained in the chain, in chain-order. Excludes the chain's `mixer_device`.

State 1 (raw_doc only, no body prose): the body renders the `raw_doc` text verbatim. Footnote tooltip reads
"From Live's runtime docstring."

State 2 (raw_doc + authored body): the body renders the authored prose. Footnote tooltip shows the raw_doc text
verbatim under a "Runtime docstring" label so readers can compare authored vs source.

Reader-side: the body always reads as prose; the marker is the truth-in-labeling.

**Renders as:** the same footnote primitive used elsewhere, with a `ⓘ` glyph (distinct from the `*` glyph used by
refinement/annotation markers so the reader can tell "source-of-body footnote" apart from "annotation footnote" at
a glance). Marker is appended at the end of the rendered body (not on the heading) so the affordance sits next to
the prose it annotates.

**Status:** ✅ wired. `source_footnote_html()` in `generate_reference.py` produces the marker; CSS classes
`.source-marker`, `.source-marker-tooltip`, `.sm-label`, `.sm-raw`, `.sm-note` are styled in `custom.css`. Hover
positioning shared with refinement markers via `web/src/scripts/tooltip-positioner.js` — both clamp to the article
bounds and floor on the visible bottom of all sticky top bars.

**Resolved opens:**

- "No investigation yet" state (no raw_doc, no body) → no marker (absence speaks for itself).
- Marker glyph → `ⓘ` (small info-circle), visually distinct from the `*` used by refinement/annotation footnotes.

### 6. `deprecated:` — member-level flag

**Source:**

```yaml
deprecated: true
```

or:

```yaml
deprecated:
  since: "12.0.0"
  replacement: "Track.new_method"
  note: "The legacy form returned an int; the replacement returns Live.Foo.Bar."
```

**Renders as:** TBD. Candidates:

- **A — Strikethrough + chip.** Member heading rendered with strikethrough and a "deprecated" chip; tooltip carries
  the `since` / `replacement` / `note`.
- **B — Admonition.** Starlight `<Aside type="caution">` at the top of the member body.

**Status:** ❌ not rendered.

**Open:**

- The boolean form (`deprecated: true`) and the structured form both need to work — fall back to "deprecated" with no
  detail when the boolean form is used.

### 7. `_synthesized:` and `_synthesis_note:`

**Source:**

```yaml
_synthesized: true
_synthesis_note: "Listener triplet inferred from raw_doc mention; not directly probed."
```

**Renders as:** TBD. Small "synthesized" chip on the member heading; hover reveals the `_synthesis_note`.

**Status:** ❌ not rendered.

**Open:**

- Whether synthesized members should be visually de-emphasized (greyed) or just chipped.

## Decision priorities

Roughly in increasing order of complexity / risk:

1. **`_synthesized:` chip.** Trivial once the chip vocabulary is locked.
2. **`deprecated:` rendering.** Binary or structured; pick A vs B.
3. ~~**`raw_doc` / body matrix.**~~ ✅ Shipped (§5). Body always renders as prose; ⓘ footnote at end carries source.
4. **`behavior:` + `quirks:` footnote rendering.** Together — same data shape, same primitive as refinement, two
   skins for visual distinction. Generalize `override_marker_html()` into a record-agnostic footnote renderer.
5. **Inline `[^id]` resolution.** Depends on (4). Generator-side rewrite of `[^id]` in member prose into the footnote
   marker, with the corresponding record suppressed from heading auto-attachment.

## Open meta-questions

- Generalize `override_marker_html()` into a record-agnostic `footnote_html(record, kind)` that handles all five
  record types (refinement / behavior / quirk / deprecated / synthesized) — yes, this is the natural shape now that
  we've collapsed marker and footnote into one primitive. The only per-kind variation is tooltip body content and
  marker skin (glyph + color).
- CSS organization — today the override-marker styles live in `web/src/styles/custom.css`. With the unified primitive,
  base classes (`.footnote-marker`, `.footnote-tooltip`) plus per-kind modifiers (`.footnote-marker--behavior`,
  `--quirk`, `--deprecated`, ...). Stylesheet split if `custom.css` gets unwieldy; flat for now.

# LOM module format

Per-module markdown schema for the Live Object Model. One file per top-level Live module, under
`stubs/<v>/modules/<Module>.md`. The format is the **authoring midpoint** in a two-stage transformation pipeline; humans
edit only this midpoint, and two downstream generators project it into the shipped artifacts.

> **Status.** Live. The probe pipeline emits markdown directly, and both generators read `stubs/<v>/modules/<Module>.md`
> as their only input. The legacy YAML format has been retired.

## Pipeline

```
LiveTree.raw.json     LiveClasses.json    ← Live probe outputs
       │                    │               (pure data, machine-derived,
       │                    │                no human content)
       └─────────┬──────────┘
                 │  (probe re-runs on every Live install / version bump)
                 ▼
        merge into existing markdown  ◀──┐
                 │                       │ updates probe-derived fields,
                 ▼                       │ preserves human content, flags
stubs/<v>/modules/<Module>.md            │ drift between the two
        │                                │
        │  SOURCE OF TRUTH ──────────────┘
        │  (structured data from probe
        │   + human prose
        │   + annotation records)
        │
        ├─→ stubs/<v>/Live/<Module>.pyi          ← typed Python stubs
        │   (terse projection — types, signatures, `__doc__`)
        │
        └─→ web/src/content/docs/modules/...mdx  ← reference site
            (rich projection — prose, footnotes, refinements, behavior)
```

The markdown files are the **source of truth** for both downstream artifacts. Humans edit only the markdown; the probe
never overwrites human content. On each re-probe:

- Probe-derived fields (`raw_doc`, `type`, `ancestors`, `args`, `returns`, etc.) get refreshed from the new JSON.
- Human content (description prose under each heading, `refinement` / `behavior` / `quirks` records) is preserved
  verbatim.
- Drift is surfaced as an audit signal — e.g., if a `refinement.probed` field no longer matches what the probe sees, the
  rationale was attached to a value that no longer exists in this Live version, so a human needs to revisit. Similarly
  when raw_doc text changes, authored prose may need a review; the diff flags it.

The probe produces two complementary JSON artifacts:

- **`LiveTree.raw.json`** — the tree shape: every module's nested children walked via `dir()` and the Boost.Python
  introspection surface. Carries `name`, `type`, `id`, `repr`, `raw_doc`, `bases`, `init_doc`, and `children` arrays at
  each node.
- **`LiveClasses.json`** — the flat class index: qualified class names → property tables with probed types, getter
  signatures, constructability flags. Resolves type information the tree walk can't see at the node level (Boost.Python
  doesn't expose property types directly; the class index captures them separately).

Both feed the parser that produces / updates the markdown midpoint.

The midpoint is doing two distinct jobs:

1. **Storage of structured data** in a form humans can read and edit — same data the probe JSON carries (kinds, types,
   signatures, ancestors, raw_doc), reshaped into per-module files with the structural recursion visible as markdown
   heading depth.
2. **A canvas for human-authored content** that sits next to the data it annotates — module prose, class descriptions,
   member descriptions, and structured annotation records (refinement, behavior, quirks) that the probe can't generate.

Both downstream generators select the subset they need:

| Field on the midpoint                            | Stub `.pyi`               | Reference site                    |
| ------------------------------------------------ | ------------------------- | --------------------------------- |
| `kind`, `path`, `ancestors`, structural identity | ✓                         | ✓                                 |
| `type`, `args`, `returns` (resolved values)      | ✓                         | ✓                                 |
| `raw_doc` (verbatim runtime text)                | as `__doc__`              | as footnote / fallback prose      |
| Authored body prose                              | merged into `__doc__`     | primary description               |
| `refinement` (probed value + sources)            | uses `value` only         | marker + tooltip                  |
| `behavior` / `quirks` records                    | summary line in `__doc__` | full marker + tooltip + collector |

## File shape

One file per Live module: `stubs/<v>/modules/Chain.md`, `stubs/<v>/modules/Track.md`, etc.

Top of file: YAML frontmatter carrying module identity. Body paragraphs before any heading are the module-level
description prose.

### Heading hierarchy

| Heading                                                  | Marks                                            |
| -------------------------------------------------------- | ------------------------------------------------ |
| `## Classes`, `## Enums`, `## Functions`, `## Constants` | Module-level kind groupings (top-level sections) |
| `### EntryName`                                          | One class / enum / function / constant entry     |
| `#### Properties`, `#### Methods`                        | Sub-groupings inside a class                     |
| `##### member_name`                                      | One property or method                           |

Kind-group headings (H2 at module level, H4 inside a class) exist for _human readability_ of the source. The parser's
authoritative discriminator is the `kind:` field inside each entry's fenced YAML. If a member sits under `#### Methods`
but its YAML says `kind: property`, the YAML wins (and the parser warns).

### Nested classes / enums / constants hoist to the top level

Anything declared inside a class — a nested class (Live's structural pattern for `Song.View`, `Application.View`,
`Clip.View`, etc.), a nested enum (`Application.View.NavDirection`), or class-level constants (`Application.Variants`
has `BETA`, `INTRO`, …) — renders at the module file's top level under the appropriate `## Classes` / `## Enums` /
`## Constants` section, sibling of the parent class. The heading uses the simple name; the structural nesting is
recorded in the entry's `parent:` field:

```yaml
kind: class
path: Live.Chain.Chain.View
parent: Chain
```

The parser groups by `parent:` when computing nested relationships. The renderer composes the qualified display name
(`Chain.View`) and the slug (`chainview`) from `parent + name`. Source markdown stays flat and easy to navigate — a
deeply nested member is always one level of indentation away.

## Anatomy of a class entry

````markdown
### Chain

```yaml
kind: class
path: Live.Chain.Chain
ancestors:
  - Live.Track.DeviceContainer
  - Live.LomObject.LomObject
  - Boost.Python.instance
constructable: false
raw_doc: "This class represents a group device chain in Live."
```

Authored class description prose. Multiple paragraphs OK. Markdown formatting works as expected.

#### Properties

##### devices

```yaml
kind: property
type: Live.Base.Vector[Live.Device.Device]
settable: false
listenable: true
raw_doc: "Return const access to all available Devices that are present in the chains"
refinement:
  type:
    probed: Live.Base.Vector[Live.LomObject.LomObject]
    confidence: high
    sources:
      - "[C++ signature] binding declares the element type as LomObject."
      - "[corpus] Push2/device_navigation.py indexes chain.devices[i] as Device."
behavior:
  - id: excludes-mixer
    assertion: "The vector excludes the chain's mixer_device."
    confidence: verified
    verified_against: 12.3.6
    sources:
      - "[probe] iterated devices and compared against chain.mixer_device."
```

Devices contained in the chain, in chain-order. The vector excludes the chain's `mixer_device`[^excludes-mixer] — that
lives on a separate property.

#### Methods

##### delete_device

```yaml
kind: method
args:
  - name: index
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - '[docstring] "Remove a device identified by its index from the chain".'
      type:
        probed: object
        confidence: high
        sources:
          - "[C++ signature] void delete_device(TChainPyHandle, int)."
returns:
  type: None
raw_doc: "Remove a device identified by its index from the chain."
```

Remove the device at the given index from the chain.
````

## Member frontmatter

Each `##### member_name` H5 (or H3 for top-level enum / function / constant) is followed by a fenced YAML block carrying
the member's **structured data**. Same syntactic role the file's top frontmatter plays for the document — just scoped to
one member.

The convention: read the fenced YAML block immediately after the heading; the markdown paragraph(s) below it (until the
next heading) are the member's authored description.

### Property fields

```yaml
kind: property
type: <Python type annotation> # resolved value (overrides applied)
element_type: <Python type> # optional, resolved element type for Vector-like types
settable: <bool>
listenable: <bool> # or false / omitted
raw_doc: <Live's runtime docstring>
refinement: { ... } # optional, see "Refinement" below
behavior: [...] # optional
quirks: [...] # optional
deprecated: { ... } # optional, see "Member-level metadata"
_synthesized: <bool> # optional, see "Member-level metadata"
_synthesis_note: <prose> # optional
```

### Method / function fields

```yaml
kind: method # or `function` for module-level
signature: <Boost.Python signature string> # probe artifact, preserved verbatim
cpp_signature: <C++ signature> # probe artifact, preserved verbatim
args:
  - name: <arg name> # resolved (after rename)
    type: <Python type> # resolved (after retype)
    optional: <bool> # if has default
    default: <literal> # if has default
    refinement: { name: { ... }, type: { ... } } # optional
returns:
  type: <Python type>
  element_type: <Python type> # optional, when return is Vector-like
  refinement: { type: { ... }, element_type: { ... } } # optional
raw_doc: <Live's runtime docstring>
behavior: [...] # optional
quirks: [...] # optional
deprecated: { ... } # optional
```

### Class fields

```yaml
kind: class
path: <fully qualified Live.Module.Name>
parent: <ContainingClassName> # only if nested
ancestors: [...] # MRO from probe
constructable: <bool>
init_doc:
  <Live's __init__ docstring> # probe artifact; typically the
  # "Raises an exception" boilerplate
  # for non-constructable classes
raw_doc: <Live's runtime docstring>
```

### Enum / constant fields

```yaml
kind: enum
parent: <ContainingClassName> # only if nested in a class
members: { <name>: <int>, ... }
raw_doc: <Live's runtime docstring>
```

```yaml
kind: constant
parent: <ContainingClassName> # only if nested in a class
type: <Python type>
value: <literal>
raw_doc: <Live's runtime docstring>
```

## Annotation records

Annotation records sit inside member frontmatter as named keys. Three kinds today:

- `refinement` — type / name overrides (the override layer from the old YAML, restructured). Singular per member-scope.
- `behavior` — list of behavioral assertions about runtime behavior the type system can't capture. Each carries its own
  confidence and evidence. Phase 2 content.
- `quirks` — list of gotchas / edge cases worth flagging. Phase 2 content.

All three share the same body shape: a structured record with confidence, optional version verified against, and a list
of sources tagged with bracketed evidence-type prefixes.

### Refinement

`refinement:` blocks are **always nested by what's being refined**. The same shape applies at every scope (property,
method arg, method return) — the only difference is which sub-keys are valid at each scope. A `refinement:` block holds
one or more sub-blocks; each sub-block describes the refinement of one field (`type`, `name`, `element_type`, etc.) with
its own probed value, confidence, and sources.

Valid sub-keys per scope:

| Scope         | Valid refinement sub-keys      |
| ------------- | ------------------------------ |
| Property      | `type`, `element_type`         |
| Method arg    | `name`, `type`, `element_type` |
| Method return | `type`, `element_type`         |

Each sub-block has the same shape:

```yaml
<sub-key>:
  probed: <original value the probe captured> # optional — omit when there's nothing to compare against
  confidence: high | medium | low # required for typed refinements; omitted for name renames
  sources:
    - "[<tag>] <evidence>"
```

`probed:` is **only present when the probe captured a value the refinement is narrowing-away-from**. Some cases:

- **Refining `type:` on a property/return.** Always carries `probed:` — the probe captured a wider or wrong type that's
  being narrowed (e.g., `Chain.devices: Vector[LomObject]` → `Vector[Device]` has `probed: Vector[LomObject]`).
- **Refining `name:` on a method arg.** Carries `probed:` to document the rename source (`arg2 → index`,
  `probed: arg2`). Informational rather than a correction signal — the rename adds clarity over Boost.Python's
  auto-generated `argN`, it doesn't fix wrongness.
- **Refining `element_type:` on a concrete-vector property.** Often omits `probed:` because the probe sees the concrete
  container class (`UnavailableFeatureVector`) but no element type — `element_type` is purely added information, not
  refined-away-from anything.

Example — property with a type refinement:

```yaml
type: Live.Base.Vector[Live.Device.Device]
refinement:
  type:
    probed: Live.Base.Vector[Live.LomObject.LomObject]
    confidence: high
    sources:
      - "[C++ signature] binding declares the element type as LomObject."
```

Example — method arg with both a name rename and a type narrow:

```yaml
- name: index
  type: int
  refinement:
    name:
      probed: arg2
      sources:
        - '[docstring] "Remove a device identified by its index from the chain".'
    type:
      probed: object
      confidence: high
      sources:
        - "[C++ signature] void delete_device(TChainPyHandle, int)."
```

Example — property with an element_type refinement on a Vector-bearing return:

```yaml
type: Live.Application.UnavailableFeatureVector
element_type: Live.Application.UnavailableFeature
refinement:
  element_type:
    confidence: high
    sources:
      - "[probe] property's probed_type is UnavailableFeatureVector; element type is the UnavailableFeature enum."
      - "[corpus] checks of the form `Live.Application.UnavailableFeature.X not in
        get_application().unavailable_features`."
```

### Behavior

```yaml
behavior:
  - id:
      <optional-kebab-case-id> # set if the assertion is
      # referenced inline from prose
    assertion: "<statement of runtime behavior>"
    confidence: verified | state-dependent | intermittent | unprobed
    verified_against: <Live version, e.g. 12.3.6>
    sources:
      - "[<tag>] <evidence>"
```

The `assertion:` is a one-sentence factual claim — the renderer shows it as the headline of the footnote tooltip. The
`verified_against:` field tracks drift: if the probe re-runs against a newer Live version and the assertion still holds,
this updates; if not, the record stays at its old version and an audit signal fires.

### Quirks

```yaml
quirks:
  - id: <optional-kebab-case-id>
    summary: "<short statement of the gotcha>"
    severity: edge-case | invariant | undocumented
    sources:
      - "[<tag>] <evidence>"
```

## Member-level metadata

A few additional fields can sit alongside the main structural fields on any member entry. These are bookkeeping markers
consumed by the generators — not annotations, not authored prose.

### `deprecated:`

Marks the member as deprecated. The renderer surfaces it via the `[deprecated]` chip + a collapsed "Deprecated" section
at the bottom of the class block.

```yaml
deprecated: true               # bare flag — no replacement guidance available
# OR
deprecated:
  replaced_by: <method_name>   # name of the replacement method on the same class
                               # (renders as a clickable chip on the rendered page)
```

Used in `Clip.yaml` on methods like `get_notes` (deprecated; replaced by `get_notes_extended`) and on
`Browser.legacy_libraries` (bare flag — no replacement, just abandoned).

### `_synthesized:` and `_synthesis_note:`

Flags a member as not declared in Live's runtime but added to the YAML to express a conceptual model. Used on
`LomObject.canonical_parent` — Live declares `canonical_parent` per-subclass with narrowed return types but never on the
`LomObject` base; we synthesize the universal declaration on the base for renderer convenience.

```yaml
_synthesized: true
_synthesis_note: |
  <prose explaining why the member exists in the YAML without a runtime declaration>
```

The renderer doesn't surface the `_` -prefixed fields to readers — they're internal markers that the lom-merge step
preserves across probe runs (the probe never overwrites a synthesized entry).

## Footnote references in prose

Annotation records with an `id:` can be referenced inline from the markdown body using GFM's standard `[^id]` syntax:

```markdown
Devices contained in the chain, in chain-order. The vector excludes the chain's `mixer_device`[^excludes-mixer] — that
lives on a separate property.
```

The renderer resolves `[^excludes-mixer]` against the member's `behavior` / `quirks` / `refinement` records by `id`,
producing a superscript marker that hovers/clicks to reveal the record body. Records without an `id:` still render as a
member-level footnote (chip on the heading); the `id:` is purely opt-in for inline placement at a specific phrase in
prose.

Note that `[^id]` references are initially scoped to the **member's** records — the parser only resolves IDs against
records on the same member. Cross-member footnotes (a quirk on `Track.delete_clip` referenced from `Clip` prose, for
example) are out of scope for v1 but a likely future expansion; promoting to class-scoped or module-scoped IDs would
require uniqueness guarantees at the corresponding scope.

## Evidence-type tags

Each item in a `sources:` list starts with a bracketed evidence-type tag identifying where the evidence comes from. The
renderer parses the leading `[tag]` and produces a styled chip on the bullet so readers can scan provenance.

| Tag               | When to use                                                                       |
| ----------------- | --------------------------------------------------------------------------------- |
| `[corpus]`        | Evidence from Ableton-shipped Remote Scripts (`external/corpus/...` paths).       |
| `[docstring]`     | Evidence from the field's own `raw_doc`. Quoted text from raw_doc → use this tag. |
| `[M4L]`           | Evidence from Max for Live documentation (`external/max-for-live-docs/...`).      |
| `[C++ signature]` | Evidence from the C++ binding signature (cpp_signature field).                    |
| `[sister method]` | Comparison to a similar/related method or property on the same or related class.  |
| `[probe]`         | Runtime introspection observation — probe data, element_repr observations.        |
| `[schema]`        | Applied per a documented YAML schema convention (e.g., the enum-arg convention).  |
| `[inference]`     | Reasoned conclusion from established facts — no direct citation. See note below.  |

The `[inference]` tag covers claims that follow from how Python, Boost.Python, or the LOM's runtime semantics work in
general — things that don't anchor to a specific corpus / docstring / M4L / signature site. It's structurally the
weakest evidence kind (there's nothing concrete to cite), so prefer pairing with stronger sources when available, and
keep `confidence: high` for inference-only annotations rare.

Many `[inference]` claims today are unverified system-level invariants — facts about how the LOM works in aggregate that
nobody's bothered to formally probe yet. Examples: "Boost.Python proxies are GC'd by Python independently of C++
ownership," "every observable property exposes the same add/remove/has listener triplet," "setting a property and
reading it back returns the same value." Each is a candidate for a **higher-level probe** — a one-time investigation
documenting its scope, methodology, and findings, that per-member annotations then cite by reference. The promotion path
is `[inference]` → `[probe]` claim by claim, as these system-level investigations land. Once written, a single
higher-level probe can replace `[inference]` sources on dozens of members at once.

## Raw docstring vs authored prose

Both layers coexist for every entry that has a Live runtime `__doc__`:

- **`raw_doc:` field in the entry's frontmatter** — verbatim runtime string the probe captured. Hand-edited never;
  updated only by the probe on Live version bumps.
- **Markdown body below the YAML block** — authored prose, optional.

Renderer logic:

| State        | Primary content             | Footnote                                                |
| ------------ | --------------------------- | ------------------------------------------------------- |
| Body present | Body (authored prose)       | `[runtime docstring]` footnote with the raw_doc content |
| Body empty   | `raw_doc` rendered verbatim | Chip flags "raw runtime docstring; not yet authored"    |
| Neither      | Skeleton placeholder        | Chip flags "no investigation yet"                       |

This gives the docs an explicit "investigated" gradient: skeleton → raw_doc shown verbatim → raw_doc plus authored prose
→ authored prose with verified behavior records.

## Parser contract

```python
def parse_module_md(path: Path) -> dict:
    """Read a module's class-markdown file → in-memory module dict.

    Returns a dict matching the in-memory shape the generators consume:
    {
      "module": str,
      "raw_doc": str | None,
      "description": str,                   # body before any H2
      "classes": [ <class_dict>, ... ],     # top-level + hoisted nested
      "enums":   [ <enum_dict>, ... ],
      "functions": [ ... ],
      "constants": [ ... ],
    }

    Each class dict carries its own properties / methods / nested
    children. Nested classes are resolved from the flat list via
    each child's `parent:` field.
    """
```

Output shape is what the two generators consume.

## Open questions

- **Inline footnote placement scope** — currently `[^id]` references resolve against the containing **member's** records
  only. Useful to allow scope-up to the class? Probably not — IDs would need uniqueness across the whole class.
- **`raw_doc:` field placement at class level** — currently in the class's fenced YAML block (`raw_doc:` field). Equally
  workable in the file's top frontmatter. Class-fenced wins for consistency with member-level placement; the file
  frontmatter stays for module-level identity only.

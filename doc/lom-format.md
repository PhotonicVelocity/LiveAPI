# LOM YAML format

Per-module YAML schema for the Live Object Model. One file per top-level
Live module.

Two locations, same schema:

- **`stubs/<v>/lom/<Module>.yaml`** — the curated SOT. Parser-derived
  fields plus sibling `<field>_override:` blocks for hand-tightened
  types/names.
- **`stubs/<v>/reports/seed/<Module>.yaml`** — the algorithmic baseline
  emitted by `tools/parse/build_lom_yaml.py` on every parse run. No
  overrides; useful for diffing against `lom/` to see which facts have
  been hand-touched.

This is the format both stub generation (`tools/generate/generate_stubs.py`)
and reference page generation will consume.

## Conventions

- **Members are grouped by kind into named lists**, not a flat list with
  a `kind:` discriminator: `primary_class:`, `classes:`, `enums:`,
  `functions:`, `constants:` at the module level; `properties:`,
  `methods:`, `classes:`, `enums:`, `constants:` inside a class.
- **Order within each list drives rendered output order.**
- **`primary_class:`** is a one-element list carrying the module's
  primary class (the one whose name matches the module's). Other classes
  in the module live under `classes:`.
- **Parser-derived fields stay flat scalars** — the 80% case (no
  override) is one line per fact.
- **Overrides live in a sibling `<field>_override:` block** carrying:
  - `value:` — required, the override value
  - `confidence:` — `high` / `medium` / `low`. Required for typed/structural
    facts (`type`, `args`, `returns`, `element_type`); omitted for
    name-only renames where the rename is positional-decorative under
    PEP 570 (`, /`).
  - `source:` — required: corpus def-site, M4L doc citation, raw_doc text.
  - `from:` — optional: the parser-derived value the override expects to
    find. Validated during port/audit; mismatch is a drift warning.
- **Inherited properties are dropped.** When an ancestor class declares
  the same `name`/`type`/`settable`/`listenable` shape (and neither side
  has overrides), the property is omitted from the subclass — pyright
  resolves the annotation from the inherited declaration. Type-overridden
  properties stay put.

## Module top level

```yaml
module: Song
description: |              # hand-authored prose (markdown). Renders as the
  Top-level Live set: tracks, transport, scenes, history. The Song is the
  root of the LOM document tree.

primary_class:
- name: Song
  ...

classes:
- name: BeatTime
  ...

enums:
- name: ...

functions:
- name: ...

constants:
- name: ...
```

A module may omit any group when empty. The `description:` field is the
hand-authored module-level prose; the reference generator uses it as the
intro paragraph below the page H1 and as the `<meta>` description tag.
Live's runtime exposes no module-level docstrings, so this field is
always hand-authored. When absent, the reference renders a visible
`_No module description._` placeholder so the gap is editorially obvious.

## Class — primary

Real source: `Live.Song.Song`.

```yaml
- name: Song
  path: Live.Song.Song           # parser — fully qualified
  raw_doc: This class represents a Live set.
  ancestors:                     # parser — Boost.Python boilerplate stripped
  - Live.LomObject.LomObject
  init_doc: |-                   # parser — raw __init__ docstring
    Raises an exception
    This class cannot be instantiated from Python
  constructable: false           # parser — has zero-arg __init__?

  properties:
  - name: tempo
    ...
  methods:
  - name: create_audio_track
    ...
  classes:                       # nested classes (View, etc.)
  - name: View
    ...
  enums:
  - name: ...
```

`init_doc:` is rarely useful — preserved verbatim but the renderer can
suppress the boilerplate "cannot be instantiated" form.

## Property — basic

Real source: `Live.Song.Song.arrangement_overdub`.

```yaml
- name: arrangement_overdub
  raw_doc: Get/Set the global arrangement overdub state.
  type: bool                                       # parser
  settable: true                                   # parser
  listenable:                                      # parser — listener triplet folded under the property
  - add_arrangement_overdub_listener               #          (key omitted entirely when not listenable)
  - remove_arrangement_overdub_listener
  - arrangement_overdub_has_listener
```

Override example (`Live.Song.Song.appointed_device`):

```yaml
- name: appointed_device
  raw_doc: Read, write, and listen access to the appointed Device
  type: None                                       # parser saw None at probe time
  type_override:
    value: Live.Device.Device | None               # hand — corpus-verified
    confidence: high
    source: |
      Docstring: "Read, write, and listen access to the appointed Device."
      Corpus-verified — pushbase / ableton.v2 / ableton.v3 all read and
      assign Device values here.
  settable: true
  listenable:
  - add_appointed_device_listener
  - remove_appointed_device_listener
  - appointed_device_has_listener
```

## Iterable container classes

Iterability is encoded by two flags:

- **`iterable: true`** — the class is iterable (has `__iter__`). Set when
  the runtime class supports the iterator protocol.
- **`container: true`** — the class is a *container* (has `append` and
  `extend` bound by the parser, in addition to iteration). Distinguishes
  vector-style classes from plain iterators. The stub generator inherits
  the iterator protocol from `Vector[E]` for containers and uses
  `Iterable[E]` for plain iterators.
- **`parametric: true`** — only on `Live.Base.Vector`. The class is the
  generic base; the renderer emits `class Vector(Generic[T])` plus a
  module-scope `T = TypeVar('T', covariant=True)`. Concrete container
  subclasses inherit from `Vector[E]` rather than redeclaring members.
- **`element_type:`** — the concrete element type for non-parametric
  iterables. Used by the renderer for `Iterable[E]` / `Vector[E]` bases
  and for synthesizing typed `append`/`extend` on container subclasses.

Examples:

```yaml
# Generic base — the only class with `parametric: true`.
- name: Vector
  path: Live.Base.Vector
  raw_doc: A simple read only container for returning objects from Live.
  ancestors: []
  iterable: true
  parametric: true               # → class Vector(Generic[T])

# Concrete container — inherits Vector[float], gets typed append/extend synthesized.
- name: FloatVector
  path: Live.Base.FloatVector
  iterable: true
  container: true
  element_type: float            # → class FloatVector(Vector[float])

# Plain iterator (no append/extend in the runtime).
- name: BrowserItemIterator
  path: Live.Browser.BrowserItemIterator
  iterable: true                 # no `container:` flag → renders as Iterable[E]
  element_type_override:         # parser didn't observe element type; hand-supplied.
    value: Live.Browser.BrowserItem
    confidence: high
    source: |
      raw_doc confirms; corpus Push2/browser_list.py:63 isinstance check
      against this class.
```

`append` and `extend` are not stored in the YAML for any iterable —
they're synthesized at stub-render time (typed to the element for
container subclasses; the abstract `Vector` base stays read-only at the
type level).

## Method

Real source: `Live.Track.Track.create_audio_clip`. Parser splits the
verbatim Boost.Python doc into three derived fields: a Python signature
line, a C++ signature line, and the cleaned description text.

```yaml
- name: create_audio_clip
  raw_doc: |-
    Creates an audio clip referencing the file at the given path...
  signature: 'create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :'
  cpp_signature: TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)
  args:
  - name: self
    type: Live.Track.Track
  - name: arg2                   # parser
    name_override:               # hand — no confidence on name renames
      value: file_path
      source: |
        Arg names verified against corpus / M4L docs:
          - arg2 -> file_path  [M4L docs]: external/max-for-live-docs/9.0/track.md
    type: str
  - name: arg3
    name_override:
      value: position
      source: |
        ...
    type: float
  returns:
    type: Live.Clip.Clip
```

Per-arg overrides nest inside the arg dict, mirroring the top-level
convention. `name_override:` typically omits `confidence:` (positional-
only under PEP 570 means name accuracy affects hover hints, not type
checking); typed `*_override:` blocks always carry it.

## Enum

Real source: `Live.Clip.GridQuantization`. Members are an ordered map
of name → integer value.

```yaml
- name: GridQuantization
  raw_doc: |-
    The grid quantization used by Clip.quantize and Clip.quantize_pitch.
  members:
    g_no_grid: 0
    g_thirtysecond: 1
    g_sixteenth: 2
    g_eighth: 3
    g_quarter: 4
    g_half: 5
    g_bar: 6
    g_2_bars: 7
    g_4_bars: 8
    g_8_bars: 9
```

## Module-level function

Real source: `Live.Conversions.audio_to_midi_clip`. Same shape as a
class method, just nested at the module level instead of inside a class.

```yaml
- name: audio_to_midi_clip
  raw_doc: |-
    Creates a MIDI clip in a new MIDI track with the notes extracted from
    the given audio_clip...
  args:
  - name: song
    type: Live.Song.Song
  - name: audio_clip
    type: Live.Clip.Clip
  - name: audio_to_midi_type
    type: Live.Conversions.AudioToMidiType | int
  returns:
    type: None
```

## Module-level constant

Real source: `Live.Application.BETA`.

```yaml
- name: BETA
  type: str
  value: Beta
```

For the algorithmic transforms `build_lom_yaml.py` applies when emitting
the seed (type qualification, optional widening, listener folding,
parametric-container detection, inherited-property cleanup, etc.), see
[`dataflow.md` — Stage 2b](dataflow.md#stage-2b--build-yaml-seed-offline).
They produce the shapes documented above.

---

## Deferred

- **Hypothesis attachment.** Format will be added to this spec once the
  verification stage lands.
- **`description:` field.** Hand-authored prose (markdown) parallel to
  `raw_doc:`. Not currently emitted; reserved for the reference page
  generator's authored-content phase.
- **Confidence vocabulary expansion.** Today's `high` / `medium` / `low`
  was inherited from the legacy refinement file. The
  `reference-design.md` draft mentions `verified` / `state-dependent` /
  `intermittent` / `mismatch` / `unprobed` for hypothesis records. To be
  reconciled when verification lands.

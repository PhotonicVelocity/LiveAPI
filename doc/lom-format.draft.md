# LOM YAML format — examples to edit

Draft of the per-module YAML shape (`doc/lom/<Module>.yaml`). Examples
are seeded from real entries in `LiveTree.refined.json`. Iterate until
the shape feels right; this isn't a spec yet.

## Conventions used in these examples

- **Order in YAML drives rendered page order.** First class in `members:`
  is the primary class (no `primary:` flag needed).
- **`kind:`** on every member discriminates `class` / `property` /
  `method` / `enum` / `constant` / `function`. Parser knows it; humans
  don't have to infer.
- **Parser-derived fields stay flat scalars** so the 80% case (no override)
  stays terse and one-line-per-fact.
- **Overrides live in a sibling block** `<field>_override:` with
  `value` / `confidence` / `source`. Visually distinct, easy to grep for.
- **`description:`** holds hand-authored prose (markdown). When the parser
  has a `raw_doc`, it's preserved verbatim under `raw_doc:`; the human
  rewrites into `description:` and the renderer prefers it.

---

## 1. Module top level — `Song.yaml`

```yaml
module: Song
raw_doc: null                # parser
description: |               # hand (optional; rendered before members)
  Top-level Live set: transport, scenes, tracks, history.

members:
  - kind: class
    name: Song               # primary class (first class entry)
    # ... see §2
  - kind: class
    name: BeatTime
    # ... see §6
  - kind: class
    name: CuePoint
  - kind: class
    name: SmptTime
```

A module with module-level enums or functions extends the same `members:`
list (see §7, §8, §9).

---

## 2. Class — primary

Real source: `Live.Song.Song`.

```yaml
- kind: class
  name: Song
  raw_doc: "This class represents a Live set."        # parser
  description: |                                      # hand
    The Song is the root of the Live Object Model — every track, scene,
    clip, and device hangs off it. Persistent for the lifetime of the
    Live process.
  ancestors:                                          # parser
    - LomObject
  init_doc: "Raises an exception\nThis class cannot be instantiated from Python\n"  # parser
  constructable: false                                # parser

  members:
    - kind: property
      name: tempo
      # ... see §3
    - kind: property
      name: cue_points
      # ... see §4
    - kind: method
      name: create_audio_track
      # ... see §5
```

`ancestors:` strips Boost.Python boilerplate (`<class 'Boost.Python.instance'>`)
to the meaningful base only. `init_doc:` is rarely useful — preserved
verbatim but the renderer can suppress the boilerplate "cannot be
instantiated" form.

---

## 3. Property — basic

Real source: `Live.Song.Song.tempo`. Shows the three things every
property carries: probed type, settable flag, and listenability (derived
from sibling `add_*_listener`/`remove_*_listener`/`*_has_listener`
methods that the parser will fold into this node).

```yaml
- kind: property
  name: tempo
  raw_doc: "Get/Set the global project tempo."        # parser
  probed_type: float                                  # parser
  settable: true                                      # parser
  listenable: true                                    # parser (derived from listener triplet)
  description: |                                      # hand
    Tempo in BPM. Range matches Live's UI: 20.0 – 999.0. Writes outside
    the range silently clamp.
  description_override:                               # hand — example of a typed override
    confidence: medium
    source: "raw_doc + manual UI inspection in Live 12.3.6"
```

Override examples (only one of these would normally be present per field):

```yaml
  probed_type: int                                    # parser said int
  probed_type_override:                               # hand
    value: float
    confidence: high
    source: "corpus: BarBeat.py:42 — assigns float to song.tempo"
```

---

## 4. Property — collection

Real source: `Live.Song.Song.cue_points`. Has `probed_repr` (the runtime
class) and `element_repr` (the element type when the runtime is a
Vector-like).

```yaml
- kind: property
  name: cue_points
  raw_doc: "Const access to a list of all cue points of the Live Song."
  probed_type: Vector
  probed_repr: "<class 'Base.Vector'>"     # parser — disambiguates Vector subclasses
  element_repr: "<class 'Song.CuePoint'>"  # parser — element type
  settable: false
  listenable: true
  description: |
    Cue points on the master timeline, ordered by their `time` field.
    Iteration order is stable; mutation reorders.
```

Renderer typically displays this as `Vector[CuePoint]` (synthesized from
`probed_type` + `element_repr`).

---

## 5. Method

Real source: `Live.Song.Song.create_audio_track`. Shows args + returns +
the parser's three-form signature (Python, C++, cleaned description).

```yaml
- kind: method
  name: create_audio_track
  raw_doc: |                                          # parser — verbatim Boost.Python output
    create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :
        Create a new audio track at the optional given index ...
        C++ signature :
            TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])
  signature: "create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :"        # parser
  cpp_signature: "TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])"  # parser
  description: |                                      # parser-cleaned (raw_doc minus signature/footer)
    Create a new audio track at the optional given index and return it.
    If the index is -1, the new track is added at the end. ...
  args:                                               # parser (`self` dropped — not useful in docs)
    - name: index
      type: "int | None"
      optional: true
      default: "None"
  returns:
    type: Track
```

Override example (renaming a positional arg whose parser-emitted name is generic):

```yaml
  args:
    - name: arg1                                      # parser
      arg1_override:                                  # hand
        name: index
        confidence: high
        source: "corpus: SetSong.py:88 — `song.create_audio_track(index=...)`"
      type: "int | None"
      optional: true
      default: "None"
```

(Open question: rename overrides on positional args want a different shape — see open questions at bottom.)

---

## 6. Class — auxiliary variants

```yaml
# Constructable helper class — Live.Song.BeatTime
- kind: class
  name: BeatTime
  raw_doc: "Represents a Time, splitted into Bars, Beats, SubDivision and Ticks."
  ancestors: []                  # parser strips Boost.Python.instance → empty list
  constructable: true            # parser (has zero-arg __init__)
  init_doc: |
    __init__( (object)arg1) -> None :
        C++ signature :
            void __init__(_object*)

# Iterable container — Live.Base.Vector
- kind: class
  name: Vector
  raw_doc: "A simple read only container for returning objects from Live."
  ancestors: []
  iterable: true                 # parser
  element_repr: "<class 'LomObject.LomObject'>"   # parser

# Exception class — Live.Base.LimitationError
# (One node in the tree; parser emits `kind: type` today — folding into class.)
- kind: exception
  name: LimitationError
  raw_doc: null
  ancestors:
    - Exception
```

---

## 7. Enum

Real source: `Live.Clip.ClipLaunchQuantization`. Members are an
ordered map of name → integer value.

```yaml
- kind: enum
  name: ClipLaunchQuantization
  raw_doc: null
  description: |                 # hand
    Launch quantization for clip start. Values match Live's launch box
    dropdown order top-to-bottom.
  members:
    q_global: 0
    q_none: 1
    q_8_bars: 2
    q_4_bars: 3
    q_2_bars: 4
    q_bar: 5
    q_half: 6
    q_half_triplet: 7
    q_quarter: 8
    q_quarter_triplet: 9
    q_eighth: 10
    q_eighth_triplet: 11
    q_sixteenth: 12
    q_sixteenth_triplet: 13
    q_thirtysecond: 14
```

---

## 8. Module-level function

Real source: `Live.Conversions.audio_to_midi_clip`. Same shape as a
class method, just nested at the module level instead of inside a class.

```yaml
- kind: function
  name: audio_to_midi_clip
  description: |
    Creates a MIDI clip in a new MIDI track with the notes extracted from
    the given audio_clip. ...
  args:
    - name: song
      type: Song
    - name: audio_clip
      type: Clip
    - name: audio_to_midi_type
      type: "AudioToMidiType | int"
  returns:
    type: None
```

---

## 9. Module-level constant

Real source: a handful of `str`-typed module attributes, e.g., `BETA`.

```yaml
- kind: constant
  name: BETA
  type: str
  value: "Beta"
```

---

## 10. Hypothesis attachment (sketch — to nail down)

Hypotheses hang off the member they describe (property or method). Shape
is just a placeholder — the verification stage isn't built yet, but
showing where they live in the YAML helps think about the schema.

```yaml
- kind: property
  name: appointed_device
  probed_type: "Device | None"
  settable: true
  listenable: true
  hypotheses:
    - id: appointed-device-fires-on-set
      claim: "Setting appointed_device fires the appointed_device listener."
      confidence: unprobed
      precondition: "A device exists on at least one track."
      expected: "Listener fires once with no args."
      source: ""                 # filled in once verified
    - id: appointed-device-survives-undo
      claim: "appointed_device survives an undo of an unrelated edit."
      confidence: state-dependent
      notes: |
        Verified twice — held under tempo undo, lost under track-add undo.
        Worth re-verifying with explicit undo-stack inspection.
```

---

## Open questions for the schema

1. **Override shape on list-valued fields.** `args:` is a list; renaming
   `arg1` → `index` in a sibling override block is awkward. Options:
   inline `name_override:` per arg item, separate top-level `args_override:`
   keyed by position, or a different override syntax for collections.

2. **`raw_doc` retention.** Worth keeping verbatim once a `description:`
   exists? Useful for drift detection (parser changes Boost.Python format,
   we want to know) but adds bulk. Could move `raw_doc:` to the seed-only
   side and keep `description:` in the SOT.

3. **Where do listeners actually go?** Today the tree has `add_*_listener`
   etc. as full method nodes. The renderer drops them. For YAML, fold
   them into the property's `listenable: true` flag entirely (drop method
   nodes) or keep them visible and let the renderer collapse them?

4. **`kind: type` (the lone `LimitationError`).** Treat as a class
   variant (`kind: class, exception: true`) or a separate `kind: exception`?
   Only one node in this category today.

5. **`ref: true` nodes.** 384 nodes carry this — inherited members the
   parser relocated to their defining class. In YAML, do we render them
   as full nodes at the inherited site, or just a back-pointer
   (`inherited_from: LomObject`)?

6. **Confidence vocabulary.** Today's `manual_refinements.yaml` uses
   `high` / `medium` / `low`. The reference-design draft mentions
   `verified` / `state-dependent` / `intermittent` / `mismatch` /
   `unprobed`. Reconcile to one ladder, or two (refinement-confidence vs
   hypothesis-confidence)?

7. **Source-citation format.** Free-text today (`"corpus: foo.py:42"`,
   `"M4L docs: ..."`). Worth structuring (`{type: corpus, file: foo.py,
   line: 42}`) for tooling, or stay free-text for ergonomics?

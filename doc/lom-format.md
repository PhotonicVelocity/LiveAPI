# LOM YAML format

Per-module YAML schema for the Live Object Model. One file per top-level
Live module (`doc/lom/<Module>.yaml` once the SOT moves there; for now
emitted to `stubs/<v>/reports/seed/<Module>.yaml` by Stage 2 of the
pipeline — see [`dataflow.md`](dataflow.md)).

This is the format both stub generation (4a) and reference page
generation (4b) consume. Examples below are real entries from the
hand-curated `stubs/<v>/lom/<Module>.yaml` files (the SOT — algorithmic
seed plus sibling `<field>_override:` blocks).

## Conventions

- **Order in YAML drives rendered page order.** First class in `members:`
  is the primary class — no flag needed.
- **`kind:`** on every member discriminates `class` / `property` /
  `method` / `enum` / `constant` / `function`. The schema is shape-driven;
  `kind:` is an explicit discriminator so consumers don't have to infer.
- **Parser-derived fields stay flat scalars** — the 80% case (no
  override) is one line per fact.
- **Overrides live in a sibling `<field>_override:` block** carrying:
  - `value:` — always required, the override value
  - `confidence:` — required for typed/structural facts (`type`, `args`,
    `returns`); omitted for prose
  - `source:` — required for typed/structural facts; omitted for prose
- **`description:`** is hand-authored prose (markdown). The
  parser-cleaned text (raw_doc with signature/footer stripped) lives in
  `raw_doc:`. The renderer prefers `description:` when both exist;
  `raw_doc:` may also surface as a tooltip / expandable.
- **Class variants are derived, not flagged.** "It's an exception" is
  encoded by `Exception` in `ancestors:`, not a special `kind:`.

## Module top level

```yaml
module: Song
raw_doc: null                # parser
description: |               # hand (optional; rendered before members)
  Top-level Live set: transport, scenes, tracks, history.

members:
  - kind: class
    name: Song               # primary class (first class entry)
  - kind: class
    name: BeatTime
  - kind: class
    name: CuePoint
  - kind: class
    name: SmptTime
```

A module with module-level enums, functions, or constants extends the
same `members:` list (see Enum / Module function / Module constant
sections below).

## Class — primary

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
    - kind: property
      name: cue_points
    - kind: method
      name: create_audio_track
```

`ancestors:` strips Boost.Python boilerplate (`Boost.Python.instance`)
to the meaningful base only. `init_doc:` is rarely useful — preserved
verbatim but the renderer can suppress the boilerplate "cannot be
instantiated" form.

## Property — basic

Real source: `Live.Song.Song.tempo`.

```yaml
- kind: property
  name: tempo
  raw_doc: "Get/Set the global project tempo."        # parser
  type: float                                         # parser
  settable: true                                      # parser
  listenable:                                         # parser — listener triplet folded in;
    - add_tempo_listener                              #          key omitted entirely when not listenable
    - remove_tempo_listener
    - tempo_has_listener
  description: |                                      # hand
    Tempo in BPM. Live clamps writes to 20.0 – 999.0 silently.
```

Override example:

```yaml
  type: int                                           # parser said int
  type_override:                                      # hand — typed fact override
    value: float
    confidence: high
    source: "corpus: BarBeat.py:42 — assigns float to song.tempo"
```

Prose override (no `confidence:` / `source:`):

```yaml
  description_override:
    value: |
      Tempo in BPM. Range matches Live's UI: 20.0 – 999.0; out-of-range
      writes silently clamp.
```

## Property — collection

Real source: `Live.Song.Song.cue_points`. `repr:` and `element_repr:`
appear when the runtime class needs disambiguation (Vector subclass) or
when the runtime is iterable.

```yaml
- kind: property
  name: cue_points
  raw_doc: "Const access to a list of all cue points of the Live Song."
  type: Vector
  repr: "<class 'Base.Vector'>"            # parser — disambiguates Vector subclasses
  element_repr: "<class 'Song.CuePoint'>"  # parser — element type
  settable: false
  listenable:
    - add_cue_points_listener
    - remove_cue_points_listener
    - cue_points_has_listener
  description: |
    Cue points on the master timeline, ordered by their `time` field.
```

The renderer typically displays this as `Vector[CuePoint]` (synthesized
from `type:` + `element_repr:`).

> **Open:** clean up parser output so `repr:` / `element_repr:` come
> through as `Base.Vector` / `Song.CuePoint` instead of the
> `<class '...'>` literals. Override remains the escape hatch.

## Method

Real source: `Live.Song.Song.create_audio_track`. Parser splits the
verbatim Boost.Python doc into three derived fields: a Python signature
line, a C++ signature line, and the cleaned description text. The
verbatim form does not survive into YAML.

```yaml
- kind: method
  name: create_audio_track
  raw_doc: |                                          # parser — cleaned (signature + cpp_sig stripped)
    Create a new audio track at the optional given index and return it.
    If the index is -1, the new track is added at the end. ...
  signature: "create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :"        # parser
  cpp_signature: "TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])"  # parser
  description: |                                      # hand
    Create a new audio track. Index `-1` appends; out-of-range raises
    `LimitationError`. Omitted index inserts after the last selected item.
  args:                                               # parser (`self` dropped — not useful in docs)
    - name: index
      type: "int | None"
      optional: true
      default: "None"
  returns:
    type: Track
```

Per-arg overrides nest inside the arg dict, mirroring the top-level
convention:

```yaml
  args:
    - name: arg1                                      # parser
      name_override:                                  # hand
        value: index
        confidence: high
        source: "corpus: SetSong.py:88 — `song.create_audio_track(index=...)`"
      type: "int"                                     # parser
      type_override:                                  # hand
        value: "int | None"
        confidence: high
        source: "raw_doc: 'optional given index' + sister method create_midi_track accepts None"
      optional: true
      default: "None"
```

## Class — auxiliary variants

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
# (Renderer detects `Exception` in ancestors and adjusts treatment.)
- kind: class
  name: LimitationError
  raw_doc: null
  ancestors:
    - Exception
```

## Enum

Real source: `Live.Clip.ClipLaunchQuantization`. Members are an ordered
map of name → integer value.

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

## Module-level function

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

## Module-level constant

Real source: a handful of `str`-typed module attributes, e.g., `BETA`.

```yaml
- kind: constant
  name: BETA
  type: str
  value: "Beta"
```

## Hypothesis attachment

Deferred. Format will be added to this spec once the verification stage
lands.

---

## Deferred

- **Confidence vocabulary.** The legacy `manual_refinements.yaml` (now ported into `lom/`) used
  `high` / `medium` / `low`; the design draft mentions `verified` /
  `state-dependent` / `intermittent` / `mismatch` / `unprobed`. To
  reconcile when hypothesis verification lands.
- **Source-citation format.** Free text for now. Tighten later if
  tooling needs structured fields.
- **Cleaner `repr:` / `element_repr:` strings.** Parser improvement —
  emit `Base.Vector` instead of `<class 'Base.Vector'>`.

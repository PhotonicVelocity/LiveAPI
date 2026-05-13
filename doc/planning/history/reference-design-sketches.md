# Documentation — Worked Sketches (historical)

> **Status.** Archived. These sketches predate the lom-format spec —
> the record format they propose (top-level `"Live.X.X.member":` keys
> with `hypotheses` / `action` / `expects` / `operation_rules` /
> `invariants` fields) didn't survive into the shipped schema. The
> actual format embeds member-scoped `refinement:` / `behavior:` /
> `quirks:` records inside each member's fenced YAML block in
> `content/<v>/modules/<Module>.md`; see [`doc/lom-format.md`](../../lom-format.md).
>
> Kept here as context for the design conversation that led to the
> current format. New worked examples — sketched in the actual
> shipped format — would be a separate doc.

> Companion to `reference-design.md`. Walks through concrete examples of what a
> member record looks like, what its stub docstring renders to, and what its
> reference-page section renders to. Format details are illustrative — locking
> them in is Slice 1's deliverable, not this doc's.

The three examples are picked to span the slice plan's complexity ladder:

1. **`Song.tempo`** — simple settable property, no preconditions, no side
   effects worth naming. Slice 1 territory.
2. **`Track.delete_clip`** — method with preconditions and a state-gated side
   effect. Slice 2–3 territory.
3. **`Clip.add_warp_marker`** — method with invariants and operation rules.
   Slice 4 territory (the warp-markers case study).

Plus a sketch of the class-page-level layout for `Clip`.

---

## Example 1: `Song.tempo`

### The member record

```yaml
"Live.Song.Song.tempo":
  kind: property
  description: |
    The song-level tempo in beats per minute. Drives all clip playback,
    metronome, and timeline navigation that don't have a per-clip override.
  hypotheses:
    - id: settable_immediate
      action: { set: tempo, value: 128.0 }
      expects:
        - "$song.tempo becomes 128.0"
      async_class: immediate
      undo_tracked: true
      verified_against: 12.3.6
      confidence: verified
  quirks: []
  notes: []
```

### Stub docstring rendering

```python
@property
def tempo(self) -> float:
    """The song-level tempo in beats per minute. Drives all clip playback,
    metronome, and timeline navigation that don't have a per-clip override.

    Settable, immediate visibility, undo-tracked.

    See also: https://photonicvelocity.github.io/LiveAPI/Song/#tempo
    """
    ...

@tempo.setter
def tempo(self, value: float) -> None: ...
```

The stub picks: the description prose, a one-line behavioral summary collapsed
from the structured assertions, and the reference link.

### Reference page section

```markdown
### `tempo`

- **Type:** `float` (get) / `float` (set)
- **Listenable:** yes
- **Verified against:** Live 12.3.6

The song-level tempo in beats per minute. Drives all clip playback, metronome,
and timeline navigation that don't have a per-clip override.

#### Behavior

| Aspect       | Value                            | Confidence |
| ------------ | -------------------------------- | ---------- |
| Visibility   | Immediate (readable next access) | `verified` |
| Undo-tracked | Yes                              | `verified` |
| Side effects | None named                       | `verified` |
```

The reference picks: the description, a structured behavior table, and the
verification metadata. No prose summary collapse — the table _is_ the rendering.

---

## Example 2: `Track.delete_clip`

A method with a real precondition table and a state-gated side effect.

### The member record

```yaml
"Live.Track.Track.delete_clip":
  kind: method
  description: |
    Deletes the clip at the given session-view slot index. Removal is immediate
    and undo-tracked. When the "Auto Clip Switch on Delete" preference is enabled
    and the deleted clip was the active one, the next clip down begins playback.
  hypotheses:
    - id: removes_clip
      action: { call: delete_clip, args: ["$slot_index"] }
      expects:
        - "$track.clip_slots[$slot_index].clip becomes null"
      async_class: immediate
      undo_tracked: true
      verified_against: 12.3.6
      confidence: verified

    - id: starts_next_clip_with_pref
      precondition: "pref.auto_clip_switch_on_delete = true and clip_was_playing"
      action: { call: delete_clip, args: ["$active_slot_index"] }
      expects:
        - "$song.is_playing becomes true within 2 ticks"
      null_control: "$song.is_playing stays false when delete_clip is not called"
      verified_against: 12.3.6
      confidence: verified-with-null-control

    - id: noop_without_pref
      precondition: "pref.auto_clip_switch_on_delete = false and clip_was_playing"
      action: { call: delete_clip, args: ["$active_slot_index"] }
      expects:
        - "$song.is_playing stays unchanged"
      verified_against: 12.3.6
      confidence: verified

  quirks:
    - "The slot index is into the session view, not the arrangement."
```

### Stub docstring rendering

```python
def delete_clip(self, slot_index: int, /) -> None:
    """Delete the clip at the given session-view slot index.

    Removal is immediate and undo-tracked. When the 'Auto Clip Switch on
    Delete' preference is enabled and the deleted clip was the active one,
    the next clip down begins playback.

    Notes:
    - Slot index is into the session view, not the arrangement.
    - Side effect (auto-clip-switch) is preference-gated.

    See also: https://photonicvelocity.github.io/LiveAPI/tracks/Track/#delete_clip
    """
    ...
```

The stub picks: description, the most important quirk and a one-line summary
of the state-gated side effect, the reference link. The full per-precondition
breakdown stays in the reference.

### Reference page section

```markdown
### `delete_clip(slot_index: int) -> None`

- **Verified against:** Live 12.3.6

Deletes the clip at the given session-view slot index. Removal is immediate
and undo-tracked. When the "Auto Clip Switch on Delete" preference is enabled
and the deleted clip was the active one, the next clip down begins playback.

#### Behavior

| Aspect       | Value            | Confidence |
| ------------ | ---------------- | ---------- |
| Visibility   | Immediate        | `verified` |
| Undo-tracked | Yes              | `verified` |
| Raises       | (no raise modes) | `verified` |

#### Side effects

When `pref.auto_clip_switch_on_delete = true` and the deleted clip was
playing, deleting it triggers playback of the next clip down:

- `$song.is_playing` becomes `true` within 2 ticks.
- `verified-with-null-control` (Live 12.3.6): null control confirmed —
  `$song.is_playing` stays `false` when `delete_clip` is not called under
  the same precondition.

When the preference is `false`, no side effect: `$song.is_playing` stays
unchanged.

#### Quirks

- The slot index is into the session view, not the arrangement.
```

The reference splits the structured assertions by precondition, surfaces the
null-control evidence (raising confidence), and renders the quirk inline.

---

## Example 3: `Clip.add_warp_marker`

The warp-markers case study — invariants, operation rules, and the slope rule
that ties them together.

### The member record

```yaml
"Live.Clip.Clip.add_warp_marker":
  kind: method
  description: |
    Adds a warp marker at the position specified by the given `WarpMarker`
    instance. Warp markers anchor sample-time to beat-time within the clip's
    audio; the segments between adjacent markers determine local playback BPM.
  hypotheses:
    - id: appends_when_valid
      action: { call: add_warp_marker, args: ["$valid_marker"] }
      expects:
        - "$clip.warp_markers contains $valid_marker"
      async_class: immediate
      undo_tracked: true
      verified_against: 12.3.6
      confidence: verified

    - id: noop_on_exact_duplicate
      precondition: "$clip.warp_markers contains m with same (beat_time, sample_time)"
      action: { call: add_warp_marker, args: ["$m"] }
      expects:
        - "$clip.warp_markers length unchanged"
        - "$clip.warp_markers listener does not fire"
      verified_against: 12.3.6
      confidence: verified

  operation_rules:
    - id: sample_overflow_raises
      precondition: "marker.sample_time > clip.sample_length / clip.sample_rate"
      outcome: "raises 'Warp marker sample time is out of range'"
      protects: warp_markers_strictly_monotonic
      confidence: verified

    - id: duplicate_beat_diff_sample_raises
      precondition: "marker exists at marker.beat_time with different sample_time"
      outcome: "raises 'Segment length out of range'"
      protects: warp_markers_strictly_monotonic
      confidence: verified

    - id: bpm_out_of_range_raises
      precondition: "resulting segment local BPM ∉ [5, 999]"
      outcome: "raises 'Segment length out of range'"
      protects: warp_markers_slope_in_range
      confidence: verified

  quirks:
    - "Marker comparison is by exact (beat_time, sample_time) tuple."
```

(`invariants` referenced by `protects:` are recorded once at the
`Clip.warp_markers` collection level; `add_warp_marker`, `move_warp_marker`,
`remove_warp_marker` all reference the same invariant set.)

### Stub docstring rendering

```python
def add_warp_marker(self, marker: WarpMarker, /) -> None:
    """Add a warp marker at the position specified by the given WarpMarker.

    Warp markers anchor sample-time to beat-time within the clip's audio; the
    segments between adjacent markers determine local playback BPM.

    Raises:
    - 'Warp marker sample time is out of range' — if marker.sample_time exceeds
      the clip's audio length.
    - 'Segment length out of range' — if the marker would create an invalid
      segment (out-of-range BPM, or duplicate beat_time with different
      sample_time).

    Notes:
    - Exact-duplicate markers (same beat_time and sample_time) are silent
      no-ops, no listener fire.

    See also: https://photonicvelocity.github.io/LiveAPI/tracks/Clip/#add_warp_marker
    """
    ...
```

The stub picks: description, a `Raises:` block from the operation rules
(grouped by raised text where possible), the most important `Notes:` quirk,
the reference link.

### Reference page section

```markdown
### `add_warp_marker(marker: WarpMarker) -> None`

- **Verified against:** Live 12.3.6

Adds a warp marker at the position specified by the given `WarpMarker` instance.
Warp markers anchor sample-time to beat-time within the clip's audio; the
segments between adjacent markers determine local playback BPM.

#### Behavior

| Aspect       | Value                                         | Confidence |
| ------------ | --------------------------------------------- | ---------- |
| Visibility   | Immediate                                     | `verified` |
| Undo-tracked | Yes                                           | `verified` |
| Listener     | Fires `Clip.warp_markers` listener on success | `verified` |

#### Operation rules

| Precondition                                              | Outcome                                          | Protects                                                              |
| --------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------- |
| `marker.sample_time > clip duration`                      | Raises `Warp marker sample time is out of range` | [`warp_markers_strictly_monotonic`](#warp_markers-strictly-monotonic) |
| Marker exists at `marker.beat_time` with different sample | Raises `Segment length out of range`             | [`warp_markers_strictly_monotonic`](#warp_markers-strictly-monotonic) |
| Marker exists with exact `(beat_time, sample_time)` match | Silent no-op (no listener fire)                  | —                                                                     |
| Resulting segment local BPM ∉ `[5, 999]`                  | Raises `Segment length out of range`             | [`warp_markers_slope_in_range`](#warp_markers-slope-in-range)         |

All raise modes verified against Live 12.3.6.

#### Quirks

- Marker comparison is by exact `(beat_time, sample_time)` tuple.
```

The `protects:` links jump to the invariant definition on the
`Clip.warp_markers` page, where the predicate is stated once and shared across
the three mutation methods.

---

## Example 4: A class page sketch (`Clip`)

Top of `reference/tracks/Clip.md`:

```markdown
# Clip

> `Live.Clip.Clip`

A clip is a unit of MIDI or audio content that plays back in a track. Audio
clips have warp markers and a sample reference; MIDI clips have a note grid.
Most clip operations are scoped to one of the two types — touching MIDI-only
fields on an audio clip raises, and vice versa.

- **Verified against:** Live 12.3.6
- **Live document object:** yes (one instance per slot)

## Access via

`Clip` instances are reachable from:

- `Track.clip_slots[N].clip` — session-view clips
- `Track.arrangement_clips[N]` — arrangement-view clips
- `Song.View.detail_clip` — the currently-detailed clip
- `Song.View.highlighted_clip_slot.clip` — currently selected clip

## Properties

| Property        | Type               | Supports           | Summary                                          |
| --------------- | ------------------ | ------------------ | ------------------------------------------------ |
| `name`          | `str`              | get / set / listen | User-editable clip name.                         |
| `is_audio_clip` | `bool`             | get                | True for audio clips, False for MIDI.            |
| `length`        | `float`            | get / listen       | Clip length in beats.                            |
| `warp_markers`  | `WarpMarkerVector` | get / listen       | Warp markers (audio-only). See invariants below. |
| ...             |                    |                    |                                                  |

[per-property detail sections render below]

## Methods

| Method                       | Returns | Summary                                 |
| ---------------------------- | ------- | --------------------------------------- |
| `add_warp_marker(marker)`    | `None`  | Add a warp marker. See operation rules. |
| `move_warp_marker(beat, dt)` | `None`  | Move a marker. See operation rules.     |
| `remove_warp_marker(beat)`   | `None`  | Remove a marker. See operation rules.   |
| ...                          |         |                                         |

[per-method detail sections render below]

## Invariants

These predicates always hold over `Clip` state. The mutation methods that
could violate them (`add_warp_marker`, `move_warp_marker`, …) reject
invalid inputs to preserve them.

### `warp_markers_strictly_monotonic`

`Clip.warp_markers` strictly increases in both `beat_time` and `sample_time`
across adjacent markers — no zero/negative-length segments.

Predicate: `all(b.beat_time > a.beat_time and b.sample_time > a.sample_time for a, b in pairs(value))`

Verified against Live 12.3.6.

Protected by: [`add_warp_marker.duplicate_beat_diff_sample_raises`](#add_warp_marker),
[`add_warp_marker.sample_overflow_raises`](#add_warp_marker), …

### `warp_markers_slope_in_range`

For every adjacent pair of markers, the segment's local BPM —
`(beat_delta / sample_delta_seconds) × 60` — must lie in `[5, 999]`.

Predicate: `all(5 <= 60 * (b.beat_time - a.beat_time) / (b.sample_time - a.sample_time) <= 999 for a, b in pairs(value))`

Verified against Live 12.3.6.

Protected by: [`add_warp_marker.bpm_out_of_range_raises`](#add_warp_marker),
[`move_warp_marker.bpm_out_of_range_raises`](#move_warp_marker)

## Quirks

- `WarpMarker.sample_time` is in **seconds** despite the field name. The
  `beat_to_sample_time()` method returns _samples_ (the sample-frame count) —
  collision worth flagging.
- Warp markers include an internal phantom marker as the last entry (~1/32
  beat past the last visible marker). Live's UI doesn't show it; mutation
  methods raise when called on its `beat_time`.

## Open questions

- Does `add_warp_marker` raise if the clip is currently being recorded into?
  Not yet investigated.
```

The class page hosts cross-cutting concerns — invariants that span multiple
methods, class-scoped quirks, the access-via cross-reference list — and the
per-member detail sections render below.

---

## What's not in these sketches

- **Examples (code snippets).** Out of scope for v1; the record format leaves
  room.
- **Image/diagram rendering.** Behavior diagrams (e.g. timing windows for
  async events) deferred.
- **Live-version-pinned URLs.** The above sketches use the unpinned reference
  URL; the URL design (do we serve only the latest, or do we keep a frozen
  per-version reference?) is a deferred decision.
- **Hypothesis ID format and stable URLs at the assertion level.** Sketches
  show fragment anchors at member granularity; the per-assertion stability
  story (`#add_warp_marker-bpm-out-of-range`) is real but not detailed here.

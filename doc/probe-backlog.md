# Probe backlog

Behavioral claims worth verifying once Phase 3's probe driver lands.
Each entry: the claim as currently written, where it appears in
authored prose, and what a probe would actually check.

Format is deliberately minimal — these aren't full hypothesis records
yet (those land in Phase 2 with the locked schema). This is the
"things that should become hypothesis records" pre-list, so claims
that survived authoring don't get lost between writing them and
having a place to verify them.

## How entries get here

When authoring prose (module descriptions, class descriptions, future
member descriptions), if a claim is reasonable but not formally
verified — i.e., it would survive an editor's "are you sure?" but not
a runtime probe — log it here rather than scrubbing it from the prose.
The prose still ships; the claim still gets verified later.

When Phase 2 lands and the hypothesis record schema is locked, entries
here get promoted to records (one per claim, attached to the relevant
class / member). When Phase 3 lands, the records get probed. Entries
graduate off this list as records are written.

## Open

### `LomObject` — `_live_ptr` as identity

- **Claim** (LomObject module description, Identity paragraph): "`_live_ptr`
  is the raw pointer-to-C++ — ground truth for whether two references
  point at the same Live object. Two proxies with different `id(...)`
  but matching `_live_ptr` are the same Live object."
- **What's known**: type is `int`; declared on `LomObject`, inherited
  everywhere; not settable.
- **What's unverified**: whether `_live_ptr` is actually a memory
  address vs an opaque handle ID, and — crucially — whether the
  identity equivalence holds (same `_live_ptr` ↔ same underlying Live
  object) or whether the C++ side ever reuses the integer for a
  different object after destruction.
- **Probe sketch**: obtain two proxies for the same track via different
  paths (`song.tracks[0]` vs `song.view.selected_track` when track 0
  is selected); compare `id(proxy)` and `_live_ptr`. Repeat after
  deleting and re-creating a track at the same index; check whether
  `_live_ptr` is reused.

### `LomObject` — invalidation failure mode

- **Claim** (LomObject module description, Proxies-can-outlive paragraph):
  "When the C++ side destroys the object — track deleted, clip removed,
  Set closed — any Python proxy still referencing it is invalidated.
  Subsequent attribute access typically raises."
- **What's known**: real-world Live API users observe failures; "typically"
  hedges it.
- **What's unverified**: the exact failure mode. `RuntimeError`?
  `AttributeError`? Silent stale read? Different per attribute kind
  (own properties vs inherited vs `_live_ptr` itself)?
- **Probe sketch**: hold a proxy to a track; delete the track via
  `song.delete_track`; attempt `track.name`, `track.devices`,
  `track._live_ptr`, `track.canonical_parent`. Record exception types
  and messages. Repeat for clip-in-slot, scene, device, parameter.

### `LomObject` — `canonical_parent` chain termination

- **Claim** (LomObject module description, canonical_parent paragraph):
  "Most LOM classes expose it; following the chain ends at a root
  (typically `Live.Application.Application` or the document)."
- **What's known**: `canonical_parent` appears on most LomObject
  subclasses; it returns a `LomObject`.
- **What's unverified**: where the chain actually terminates. `None`?
  `Application`? `Live.Song.Song`? Different per starting class?
- **Probe sketch**: from each top-level LOM root reachable from
  `Application` (`song`, `tracks[*]`, `scenes[*]`, ...), walk
  `canonical_parent` until it returns `None` or repeats; log the
  terminator class for each starting class.

## Graduated (links to records)

_None yet — Phase 2 record schema not locked._

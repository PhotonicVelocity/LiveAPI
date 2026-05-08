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

### Listeners — `add_*_listener` return value

- **Claim** (Listener foundation page, Subscribing section): "Register
  a callback with `add_<prop>_listener(callback)`."
- **What's known**: LiveRelay's bridge (`bridge.py:1250`) calls the
  method but discards any return value, so the bridge's behavior is
  agnostic.
- **What's unverified**: the runtime-level return value. `None`?
  `ListenerHandle`? Something else? Worth knowing because the prose
  on this page documents `ListenerHandle` as a bookkeeping class but
  doesn't claim it's the return value.
- **Probe sketch**: subscribe a no-op callback to
  `song.transport.tempo`; capture the return; report `type(...)` and
  `repr(...)`. Repeat across a few representative listenable
  properties (signal-only, value-bearing, on different LOM classes).

### Listeners — callback firing thread

- **Claim** (Listener foundation page, Threading section): "Callback
  invocation fires synchronously when Live decides the property has
  changed, presumed (but unverified) to also run on Live's main
  thread."
- **What's known**: LiveRelay docs confirm listener *attachment* runs
  on Live's main thread. Firing thread is presumed but not documented.
- **What's unverified**: whether callbacks fire on the main thread,
  the audio thread, a message-pump thread, or context-dependent.
  Material for callers contemplating thread-affine work in handlers.
- **Probe sketch**: subscribe a callback that records
  `threading.current_thread().name`; trigger property changes for a
  representative set (transport state, clip notes, song selection);
  log thread names.

### Listeners — same callback added twice

- **Claim** (Listener foundation page, Subscribing section): "Removal
  matches by object identity — the same function reference must be
  passed to both `add` and `remove`."
- **What's known**: LiveRelay's bridge doesn't prevent double-add on
  its side; the runtime behavior is opaque.
- **What's unverified**: when the same callback identity is added
  twice, does Live fire it twice (separate registrations), once
  (idempotent), or raise? Affects whether callers need to wrap their
  own dedupe.
- **Probe sketch**: register a callback that increments a counter;
  call `add_..._listener(callback)` twice; trigger the property
  change once; assert the counter equals 1 vs 2.

### Vector containers — safety of `append` / `extend`

- **Claim** (Base.Vector class description, "Bound mutators"
  paragraph): "Whether calling `append` / `extend` directly on a
  LOM-returned vector produces consistent state (listener fires, UI
  updates, persistence) is **unverified**."
- **What's known**: Boost.Python binds `append(value: T)` /
  `extend(values: Iterable[T])` on every container class (the
  parametric `Vector` base and every concrete `XVector`). Live's
  own runtime docstring describes `Vector` as "read only." The LOM
  provides dedicated state-change methods on the tracked objects
  (`Track.create_audio_clip`, `Song.delete_track`, ...).
- **What's unverified**: whether calling these mutators directly on
  a LOM-returned vector (e.g. `track.arrangement_clips.append(clip)`)
  succeeds, fails silently, or corrupts state; whether listener
  triplets fire on the property; whether the change persists on
  Set save / undo.
- **Probe sketch**: pick a representative LOM-returned vector
  property (e.g. `track.arrangement_clips`, `song.scenes`); register
  a listener on the property; call `vector.append(...)` with a
  freshly-constructed element; record (a) any exception, (b)
  whether the listener fired, (c) whether subsequent reads of the
  property reflect the new element, (d) whether the change survives
  `song.save_song()` + reload. Repeat across a couple of containers
  with different element types.

## Graduated (links to records)

_None yet — Phase 2 record schema not locked._

---
title: Live Object Model
include_module: LomObject
sidebar_badge: core
_note: |
  Foundation page for the LOM. Every LOM class signature on every
  other module page renders a clickable `LomObject` badge linking
  here (see `lom_badge_html` in `tools/generate/generate_reference.py`).
  Hoisted above the alphabetical Modules group in the sidebar (see
  `web/astro.config.mjs`). The class itself (`Live.LomObject.LomObject`)
  is appended below this prose via the `include_module:` directive.
---

The Live Object Model (LOM) is the tree of objects that comprises
Live's runtime API — Sets, tracks, clips, devices, parameters, scenes,
views — exposed with **properties** to read state, **methods** to
drive behavior, and **parent / child relations** that form a
navigable hierarchy. Every object reachable through this tree is a
`LomObject`.

The class itself is structurally minimal — it carries no public
methods and one universal property (`_live_ptr`, the C++ identity
field) — but the **identity, lifetime, and construction model**
documented here applies uniformly to every concrete LOM class
(`Song`, `Track`, `Clip`, `Device`, ...). The `LomObject` badge
next to a class signature elsewhere on the site marks that class
as bound by these rules.

## Reaching LOM objects

Instances arrive by walking down from
`Live.Application.Application` — `get_application()` is the root
entry point, `get_application().get_document()` lands on the current
Set, and from there every reachable object hangs off properties and
collections (`song.tracks[0]`, `track.clip_slots[2].clip`,
`device.parameters[1]`, ...). Python can't construct LOM objects
directly — every concrete LOM class is non-constructable. References
arrive via traversal, not allocation.

Most LOM classes also expose `canonical_parent`, which walks the
same tree the other way — following the chain up ends at a root
(typically `Application` or the document). The result is itself a
`LomObject`, so the rules below apply equally.

## How LOM objects work under the hood

Each `LomObject` is a Boost.Python proxy holding a pointer to a C++
object owned by Live's runtime. The Python object is a view into
that C++ object, not an independent value. Most surprising aspects
of LOM behavior fall out of this single fact:

**Lifetime is C++-side.** Live owns the underlying C++ object — its
lifetime tracks Set / Live application state, not Python references.
Python GCs the proxy normally; GC'ing the proxy doesn't destroy the
underlying object, and conversely the underlying object can be
destroyed (track deleted, Set closed) while a proxy still exists.

**Proxies can outlive their C++ object.** When the C++ side destroys
the object — track deleted, clip removed, Set closed — any Python
proxy still referencing it is invalidated. Subsequent attribute
access typically raises. No Python-side contract prevents this; C++
lifetime wins.

**Identity is the C++ pointer.** `_live_ptr` (declared here,
inherited everywhere) is the raw pointer-to-C++ — ground truth for
whether two references point at the same Live object. Two proxies
with different `id(...)` but matching `_live_ptr` are the same
Live object.

## Collections

LOM properties that return a list of objects use one of two
container patterns:

- **Parametric `Vector[T]`** — a single `Live.Base.Vector` class
  reused for collections of LomObjects. `Vector[Track]`,
  `Vector[Clip]`, `Vector[Scene]`, ... all return the same Python
  class; the element type varies per call site.
- **Concrete `XVector`** — distinct named classes for collections
  of non-LomObject elements (primitives, Boost.Python value
  classes): `IntVector`, `RoutingChannelVector`, `MidiNoteVector`,
  `WarpMarkerVector`, ...

Both behave identically at the Python level — read-only, iterable,
indexable. See [`Live.Base.Vector`](/LiveAPI/modules/base/#vector)
for the specific rule and one observed exception.

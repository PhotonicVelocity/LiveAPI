# Decisions

Long-form rationale for decisions that load-bearing tooling cites by anchor. Other architectural and
formatting concerns live in their proximate `README.md` (root, `tools/`, `tools/verify/`, etc.).

## Terminology

- **Live Object Model (LOM)** — the object hierarchy exposed by Live's Python runtime. Not Max-specific; the same model
  is accessed by Remote Scripts, Max for Live, and any RPC bridges that wrap the runtime. Prefer "LOM" or "Live Object
  Model" over "Live Python API" when referring to the object structure.

## Stub Accuracy and Pipeline Posture

**Principle.** Stubs exist to give Remote Script developers type checking and autocomplete. Accuracy beats
prettiness — a stub that misleads is worse than one that looks generic. The Live API binding is messy
(Boost.Python positional-only, runtime type coercion, internal C++ crashes on bad input); the stubs should
reflect what the binding actually does, not what its prose documentation suggests.

### What's already correct

The current stubs emit **PEP 570 positional-only markers (`, /`)** on every callable method with args.
Pyright and mypy reject kwarg calls (`zoom_view(direction=1, ...)`) at type-check time. Names in the
signature serve as readable labels for autocomplete hints, hover docs, and pyright error messages — but
cannot be used as kwargs in checked code. This is the right answer to "how do we keep readable names
without letting users type them as kwargs"; it stays.

### Failure modes to avoid

- **Types looser than the binding accepts.** Pyright accepts a Python `list`; the underlying Boost.Python
  binding requires the specific `TVector` type and crashes with `InternalError`. Concrete example today:
  `Clip.add_new_notes(notes: Iterable[MidiNoteSpecification] | None, /)` — sister method
  `apply_note_modifications` is documented as failing exactly this way at runtime. This is the
  highest-impact misleading class because `, /` doesn't help — pyright still accepts a wrong-type call.
- **`T | None` widening on args that don't accept None.** A defensive parser default that emits
  `T | None` on every positional arg accepts `None` at the type level, but the runtime usually crashes.
  Affects every method and every property setter if left in — the broadest misleading surface available.
- **Name semantics that don't describe the parameter accurately.** Lower-stakes than the above (`, /`
  prevents kwarg calls, so pyright won't accept `f(wrong_name=...)`) but still affects hover hints and IDE
  inlay-hint readability. A name from a source that misjudges intent — e.g., a doc that names the M4L
  proxy parameter rather than the underlying binding's conceptual parameter — misleads readers about what
  the arg means even when they can't call it as a kwarg.

### Decisions

1. **Version coverage: latest 12.x only.** Drop active maintenance of earlier versions. The repo tracks
   only the current `stubs/12.x.y/` directory; older versions (`stubs/11.*`, `stubs/12.0–12.2`) have been
   removed. Anyone needing older-version stubs can rebuild from a tagged commit (the apicapture pipeline
   still supports 11.x via `tools/sets/Set 11 Project/`).

2. **Refinement strictness — only what we can scrape from Live itself, plus hand-curated overrides with
   evidence.** All signature content comes from sources that observe the binding directly. With `, /`
   (PEP 570) on every callable, kwarg-callability is already prevented by the type checker; names are
   decorative labels for autocomplete and hover. That removes the loudest misleading-stubs failure mode
   but doesn't license loose sourcing — names that don't accurately describe the parameter still
   mislead readers about meaning.
   - Arg **names**: from the parsed C++ signature embedded in the raw docstring (when non-generic) or
     structural inference. Otherwise `argN`. No name lookups against external sources (decompiled Remote
     Scripts, M4L docs) — those are evidence of how the API was _used_, not how the binding is _defined_.
   - Arg **types**: from the parsed C++ signature only. Otherwise `Any`. Prose docstrings and M4L type
     claims are not acceptable type sources.
   - Return **types** and property **types**: same rule — what was observed from Live, otherwise `Any`.
   - Generic-looking but truthful beats pretty but wrong.

   **Manual refinements** live as sibling `<field>_override:` blocks next to the parser-derived value in
   `stubs/<v>/modules/*.md` (inside the fenced YAML block for each member). They are the one sanctioned
   override path, used only to correct known
   wrongness — a probed type that's loose where the binding is strict, a missing element-type on a
   `Vector`, a return type the parser couldn't infer. Every override carries a `source:` field with
   concrete evidence (corpus def-site, M4L doc citation, raw_doc text). Refinements never invent
   narrowings the binding doesn't actually accept.

3. **MaxForLive docs: docstring-only.** M4L describes a related-but-distinct API. Its content flows into
   `.pyi` docstrings as informational prose ("Max for Live names this parameter `direction`") and never
   into signatures. M4L type claims and parameter names describe the M4L proxy, not the underlying
   binding; using them in signatures would mislead.

4. **External-evidence sources stay out of signatures.** Decompiled Remote Script callsites and M4L docs
   are evidence of how the API was _used_, not how the binding is _defined_. The pipeline is the
   minimal capture → parse → generate, plus the manual-refinements override step (decision #2) gated by
   per-entry sourced evidence.

5. **Verification gates.** Four CI tiers run on every push (see
   [`tools/verify/README.md`](../tools/verify/README.md)): `ast.parse` (syntax), pyright self-check on
   the stubs (internal consistency), pyright `--verifytypes` (PEP 561 completeness, tracking-only), and
   pyright on hand-picked usage patterns from Ableton-shipped Remote Scripts (Tier 4 — hard gate).

## Reference Site Rendering

### `canonical_parent` rendered as inherited from `LomObject`

The reference site shows `canonical_parent` inside an "Inherited from `LomObject`" box on every LOM-tree
class, even though the runtime declares it per-class via Boost's `bases<>` registration (each class has
its own declaration with a narrowed return type — `DriftDevice.canonical_parent → Track`,
`Device.canonical_parent → Track | RackDevice | Chain`, etc.).

The probe data is faithful: every declaring class keeps its own entry in `LiveClasses.json` and in the
parsed YAML. The fiction is in the generator. `tools/generate/generate_reference.py:resolve_lom_universal`
walks the MRO from the leaf up, picks the closest declaration, hides every other declaration in the
ancestor chain, and pins the chosen one inside the `LomObject` inherited-box.

**Why this is the right lie.** The runtime semantics are universal — every LOM-tree node has a
`canonical_parent` — and Boost just happens to register it per-class to express narrowed return types.
Rendering the truth would mean either a redundant entry on every class's own properties list, or 30
ancestor boxes each repeating "this class also redeclares canonical_parent." Both are technically
truthful and conceptually misleading. Pinning to `LomObject` matches how readers actually think about
the property.

The lie is render-time only. The YAML and the parsed JSON keep every declaration intact, so anything
downstream of the YAML (stubs, type checking, override authoring) sees the binding as it actually is.

# Documentation — Design

> Focus is **structure** — what the docs contain, how the content is
> organized, and how stubs and the reference relate. Implementation details
> (pipeline stages, slice plans, lessons-learned, build framework) live
> elsewhere; this doc decides shape first. Companion: `reference-roadmap.md`
> for the path; `web-rendering.md` for the rendering primitives.

## 1. Where we are vs. where we're going

**Current state.** Stubs are solid: types accurate, listenability and
settability captured, refinements correct what the parser can't infer. What's
not solid is the prose — every docstring in the stubs comes verbatim from
Live's runtime Boost.Python `__doc__`. They're lowercase, run-on, fragmentary;
they describe what Boost.Python emits, not what the binding actually _does_.

**Where we're going.** Comprehensive documentation backed by **behavioral
probing (hypothesis testing)**. The same probed-and-verified knowledge feeds
two artifacts:

1. **Richer stub docstrings.** Polished prose from probed hypotheses replaces
   or augments the runtime-relayed text, so editor hover/autocomplete shows
   useful descriptions without leaving the IDE.
2. **A browsable reference.** Per-class pages with full structured
   rendering — types, behavioral assertions, quirks, cross-references.

Stubs and reference are **two renderings of one knowledge base.** Nothing is
hand-maintained twice; nothing drifts between them.

## 2. The methodology in one paragraph

Humans (or LLMs) write **hypotheses** about what each member does — named
targets, expected outcomes, optional preconditions. The probe **verifies** the
named claims against running Live; it doesn't sweep or discover. Each
hypothesis ends up at one of a few confidence levels (`verified`, `state-
dependent`, `intermittent`, `mismatch`, `unprobed`). The reference renders at
the confidence level it has — never overclaiming. When Live ships a new
version, hypotheses re-verify; drift surfaces as `mismatch`.

The full methodology — including the previous attempt's discovery-mode failure
modes and the dimensions of the behavioral surface — is captured on the
[behavioral-pipeline-architecture branch's architecture
doc](https://github.com/PhotonicVelocity/LiveAPI/blob/behavioral-pipeline-architecture/doc/architecture.md).
This doc treats that methodology as given and focuses on the documentation
structure that sits above it.

## 3. The unit of documentation: a member record

Each documented member (property, method, enum, sometimes class) has one
record. The record is the source of truth for both stubs and reference; both
artifacts render subsets of the same content.

A record carries:

- **Identity** — dotted path, kind (property / method / enum), the parser-
  derived type signature.
- **Description** — human-authored prose. One sentence answers "what does this
  do." Additional sentences expand. Both artifacts use this text.
- **Behavioral assertions** — structured hypothesis records with named targets,
  preconditions, expected outcomes, and confidence levels. Reference renders
  in full; stub docstring renders a short summary.
- **Quirks / gotchas** — short callouts for things that surprise: units
  mismatches, terminology overloads, cases the type system can't capture.
  Reference renders inline; stub docstring renders the most important ones as
  a `Notes:` section.
- **Refinement metadata** — when an override narrows a type, the rationale
  (`source:` and `confidence:` from the `<field>_override:` block in
  `content/<v>/modules/*.md`) surfaces in the reference so readers see _why_ a type
  was narrowed. Invisible from the stub itself.
- **Verified-against** — the Live version the assertions were last verified
  against. Surfaces drift across version bumps.

## 4. The unit of organization: a class page

Members are grouped by their owning class. One LOM class → one reference page;
one stub `.pyi` module hosts one or more classes worth of members.

A class page carries:

- **Class identity** — name, dotted path, base classes, whether it's a Live
  document object (one runtime instance) or a value type (constructable).
- **Description** — class-level prose. What is this thing? When does someone
  touch it? Same authored-prose story as a member's description.
- **Access via** — generated cross-reference list of where this class shows up
  as a property type or method return. The inverse of what the stubs encode.
- **Members** — properties, methods, enums, in fixed order. Each member's
  record renders here.
- **Quirks** — class-scoped gotchas that don't belong on any single member.
- **Open questions** — known investigation items not yet hypothesized. Visible
  evidence that the docs are honest about their gaps.

## 5. How the two artifacts share the content

Both stubs and reference draw from the same records. Each artifact picks the
subset that fits its medium:

| Field on the record   | Stub docstring                        | Reference page                                                  |
| --------------------- | ------------------------------------- | --------------------------------------------------------------- |
| Description (prose)   | Replaces / augments runtime `__doc__` | Renders as the description text                                 |
| Refinement (`type` / `name` / `element_type`) | Uses the refined `value` only | Refined value plus `*` footnote with confidence + sources       |
| Behavioral assertions | Short summary as `Notes:` block       | Footnote on the asserted phrase or member (id + tooltip)        |
| Quirks                | One-line callout(s) in `Notes:`       | Footnote with the quirk text (same primitive as behavior)       |
| Cross-references      | Link to reference page                | Rendered as "Access via" / type links                           |

> **Implementation status.** The refinement row and the cross-reference row are
> shipped. Behavioral / quirks footnotes have a locked schema but no rendering
> yet (see `web-rendering.md`). The stubs side of "authored description
> replaces / augments runtime `__doc__`" is **not yet wired** — stubs today
> emit raw `__doc__` only; lifting authored prose into the `.pyi` is the
> missing half of Phase 2.

The stub is the editor-time view: terse, scoped to what's useful at the call
site. The reference is the deep-dive view: full structured assertions, links to
related members, the full investigation trail.

## 6. Honesty about confidence

Both artifacts surface what they don't know. The reference is more verbose
about it; the stub is more compressed. In both:

- A `verified` assertion renders as a hard fact.
- An `intermittent` or `state-dependent` assertion renders as a caveat — "fires
  inconsistently," "behavior depends on whether track is armed."
- An `unprobed` assertion renders as an open question — visible to the reader,
  not pretending the gap doesn't exist.
- A member whose body text is the runtime `__doc__` (no authored prose yet)
  carries an `ⓘ` source footnote labelling it "From Live's runtime
  docstring." A member with authored prose carries the same footnote, but
  the tooltip shows the original `raw_doc` for comparison. A member with
  neither carries no marker — absence is the signal.

Confidence levels never get collapsed for the convenience of cleaner-looking
output. If two preconditions yield two outcomes, both render. If a probe is
flaky across runs, the doc says so. The point of the methodology is that the
docs accurately reflect the state of knowledge — collapsing for prettiness
defeats it.

## 7. Stable URLs and citation

Reference pages are linked from elsewhere — Remote Script projects citing a
quirk, design notes citing an invariant, the stub docstring linking to the
deep dive. URLs need to be **stable per member**, not just per class:

- A class page lives at a known relative path.
- Each member has a fragment anchor (`#warp_markers`, `#delete_clip`).
- Each behavioral assertion within a member has a sub-anchor
  (`#warp_markers-slope-rule`, `#delete_clip-fires-on-armed-track`).

Once a URL is published it doesn't move. Renames go through a redirect; deleted
members leave a tombstone for one Live version cycle.

## 8. Prose style: telegraphic

Authored prose throughout the LOM reference (module descriptions,
class/member descriptions, hypothesis records, behavioral notes) is
written telegraphically: drop articles, second-person pronouns,
copulas, and other connective filler that doesn't load-bear meaning.

Why: reference docs are scanned, not read. Each paragraph is competing
for the reader's attention with the surrounding signature, type table,
and metadata; padding loses to skimming. Telegraphic prose also reads
as authoritative — closer to the runtime's terse `__doc__` strings —
which matches the role this content plays in the artifact.

Practical rules:

- No "you". "Obtain instances by walking down from `Application`," not
  "you obtain instances by walking down from `Application`."
- Drop "the" / "a" where the noun is unambiguous. "C++ side owns
  lifetime," not "the C++ side owns the lifetime."
- Prefer noun phrases as section leads to full sentences when stating a
  fact. "**Lifetime is C++-side.**" then explanatory body.
- Keep verbs. Telegraphic prose drops articles and pronouns, not the
  predicate — "Object holds C++ pointer" reads as a stub, not an
  authoritative claim.
- Imperative voice is fine in instructions; declarative voice is fine
  in descriptions. Both stay terse.

Counter-rule: if dropping a word makes a sentence ambiguous or
introduces a garden-path reading, keep the word. Telegraphic ≠ cryptic.

## 9. Out of scope (v1)

- **Code examples.** The record format leaves room; rendering deferred.
- **Multi-version side-by-side.** Docs build for the latest tracked Live
  version only; older accessible via tagged commit.
- **Cross-version diff.** Useful but separate.
- **Search-result tuning.** Default site-framework search is acceptable.

## 10. Open structural questions

This doc deliberately doesn't decide:

- **Stub docstring rendering style.** Replace runtime `__doc__` outright, or
  prepend authored prose with the runtime text below, or keep `__doc__` and
  append a `Notes:` section. Pick by writing a few examples and reading them.
  (Reference side is decided — `ⓘ` footnote labels the source, body always
  renders as prose; see web-rendering.md §5.)
- **Class-level vs member-level scope of authored content.** Some quirks span
  multiple members (warp-marker slope rule applies across `add` / `move` /
  `remove`); should the prose live once at the class level and be referenced,
  or duplicate-for-locality at each member? Cross-member `[^id]` resolution
  is out of scope for v1 (see lom-format.md "Footnote references in prose")
  but this is the resolution path if we lift it.

**Resolved since draft:**

- ~~**Sidecar storage format.**~~ Decided: records embed inside each member's
  fenced YAML block in `content/<v>/modules/<Module>.md`. See lom-format.md.
- ~~**Reference page layout details.**~~ Locked during Phase 1 — see
  reference-roadmap.md "Phase 1 layout decisions."
- ~~**Constructor (`__init__`) coverage.**~~ `build_lom_md.py` synthesizes
  an `__init__` from `init_doc` for constructable classes (or `(self) -> None`
  when none parses); both generators render it. Authored constructor prose
  uses the same member-level pathway as any other method.

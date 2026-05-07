# Documentation — Design

> Status: draft. Focus is **structure** — what the docs contain, how the
> content is organized, and how stubs and the reference relate. Implementation
> details (pipeline stages, slice plans, lessons-learned, build framework) live
> elsewhere; this doc decides shape first.

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
  `stubs/<v>/lom/*.yaml`) surfaces in the reference so readers see _why_ a type
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

| Field on the record   | Stub docstring                        | Reference page                        |
| --------------------- | ------------------------------------- | ------------------------------------- |
| Description (prose)   | Replaces / augments runtime `__doc__` | Renders as the description text       |
| Behavioral assertions | Short summary as `Notes:` block       | Full structured rendering             |
| Quirks                | One-line callout(s) in `Notes:`       | Inline callout boxes                  |
| Refinement metadata   | Invisible                             | Rendered with `source:` citation      |
| Cross-references      | Link to reference page                | Rendered as "Access via" / type links |

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
- Members with no record at all render with their parser-derived type signature
  only and a placeholder description ("not yet investigated"). Honest about
  the lack of investigation.

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

## 8. Out of scope (v1)

- **Code examples.** The record format leaves room; rendering deferred.
- **Multi-version side-by-side.** Docs build for the latest tracked Live
  version only; older accessible via tagged commit.
- **Cross-version diff.** Useful but separate.
- **Search-result tuning.** Default site-framework search is acceptable.

## 9. Open structural questions

This doc deliberately doesn't decide:

- **Sidecar storage format.** Per-member files vs single shared file vs
  embedded as additional override-style fields in `stubs/<v>/lom/*.yaml`.
  Affects authoring ergonomics and merge-conflict surface.
- **Stub docstring rendering style.** Replace runtime `__doc__` outright, or
  prepend authored prose with the runtime text below, or keep `__doc__` and
  append a `Notes:` section. Pick by writing a few examples and reading them.
- **Reference page layout details.** Section order, table column widths,
  how `Access via` is collapsed vs. always-shown. Best decided by trying
  layouts on a real class.
- **Class-level vs member-level scope of authored content.** Some quirks span
  multiple members (warp-marker slope rule applies across `add` / `move` /
  `remove`); should the prose live once at the class level and be referenced,
  or duplicate-for-locality at each member?
- **Constructor (`__init__`) coverage.** `build_lom_yaml.py` now synthesizes
  an `__init__` method from `init_doc` for constructable classes (or
  `(self) -> None` when none is present), so this is wired into the lom
  YAML and the stubs. Reference rendering of authored constructor prose
  remains an open layout question.

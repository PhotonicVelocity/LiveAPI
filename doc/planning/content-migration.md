# Content migration — old hand-authored prose + probe results → SOT

Working doc for migrating historical LOM documentation into the `content/<v>/modules/*.md` SOT. The footnote / record
infrastructure is now ready; this is the content-authoring pass that fills it in.

## Sources

**Source A — `doc/live-api/` (41 .md files, ~15k lines, on-disk only — gitignored).** Old hand-authored reference docs
from sister project (PythonForLive). Highly structured per-member template defined in `doc/live-api/_Format.md`. Every
module has a file. Each per-property / per-method entry follows the same shape:

```markdown
#### `tempo`

- **Get Returns:** `float`
- **Set Accepts:** `float`
  - **Undo-tracked:** `yes`
  - **Async visibility:** `immediate (probed on MIDI track)`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max | probe`
- **Probe Status:** `probed (Live 12.3.5)`

**Description:** Song tempo in BPM, range `60.0` to `999.0`. Setting is confirmed undo-tracked in current probes.
```

Module preambles also carry **Sources**, **Probe Notes**, and **Open Questions** sections — the prose summary, the
ad-hoc findings, and the known gaps.

**Source B — `targeted-probing-*` branches.** Branches: `targeted-probing-clip`, `-clipslot`, `-scene`, `-song`,
`-tracks`, `-liverelay`, `integrate-targeted-probes`. The mineable content lives in:

- **`tools/apicapture/scripts/probes/probe_*.py`** — probe scripts for Clip, ClipSlot, Scene, Song, Track. Each script
  is ~300–800 lines, generator-based, runnable inside Live. Two veins of recoverable signal:
  1. **`NOTES: dict[str, str]`** at the top of each script — behavioral observations recorded as inline strings keyed by
     `<Class>.<member>` (e.g. `"ClipSlot.fire": "With quantization, the effect is on is_triggered."`).
  2. **Script body** — encodes test data (settable property values), skipped-member rationales, cross-module listener
     setups, async-vs-immediate assumptions. Comments often carry behavioral context.
- **`doc/probe-backlog.md`** — running list of behaviors worth probing later; mostly forward-looking, but some entries
  are observation-shaped and worth lifting.

The branches do _not_ carry saved probe outputs — running the scripts is the only way to regenerate JSON. Re-running is
out of scope for this migration; we mine the prose in the scripts.

The branches also have an older `reference/` directory (different format, predates `doc/live-api/`). Skip —
`doc/live-api/` supersedes it.

**Source coverage matrix:**

| Module    | doc/live-api/ | Probe script | Notes                                                |
| --------- | ------------- | ------------ | ---------------------------------------------------- |
| Song      | ✅ 107K       | ✅           |                                                      |
| Track     | ✅            | ✅           |                                                      |
| Clip      | ✅ 89K        | ✅           | Warp-marker case study                               |
| ClipSlot  | ✅ 20K        | ✅           |                                                      |
| Scene     | ✅            | ✅           |                                                      |
| All other | ✅            | ❌           | 36 other modules; `doc/live-api/` is the only source |

## What we're migrating

Per the user's framing: **dump everything we know into the authored `description:` field on each member.** Don't
pre-structure yet — claims that will eventually want their own YAML fields (async-visibility, undo-tracked,
applicable-to, …) live in prose for now. We restructure once we have a full picture of what's worth structuring.

**Every behavioral claim gets a footnote.** Use:

- `behavior:` records on the member, with `[^id]` references in the prose at each claim site.
- `confidence: medium` for hand-authored / informally probed claims (we can't say `high` without re-running the probe;
  we're not `unprobed` either because someone wrote this down after observing it).
- `sources: ["[informal probe] <where the observation came from>"]` using `[informal probe]` evidence tag (we're adding
  this tag to the evidence-tag vocabulary).

**Pure prose without behavioral claims** (e.g. "Song tempo in BPM, range 60.0 to 999.0") goes into the `description:`
field as-is. No footnote needed — it's descriptive, not asserted.

**Quirks** (a "gotcha" kind of claim) use `quirks:` records with the same shape as `behavior:`.

**Inline footnote authoring pattern:**

```markdown
Song tempo in beats per minute. Range `[60.0, 999.0]`. Setting is undo-tracked[^undo-tracked] and visible
immediately[^visibility] without a tick wait.
```

```yaml
behavior:
  - id: undo-tracked
    assertion: Setting `tempo` is undo-tracked.
    confidence: medium
    sources:
      - "[informal probe] observed in doc/live-api/Song.md probe notes (Live 12.3.5)."
  - id: visibility
    assertion: Tempo writes are immediately visible on the next read.
    confidence: medium
    sources:
      - "[informal probe] observed on MIDI track (Live 12.3.5)."
```

## Spec adjustment

Add `[informal probe]` to the evidence-tag vocabulary in `lom-format.md` §"Evidence-type tags". Explicitly weaker than
`[probe]` — records observations from the older PythonForLive reference docs and the abandoned targeted-probing scripts,
not formal probe-driver runs. Cleaner to extend the vocab than to overload `[probe]`.

## Pilot

Pick **one module** to validate the approach end-to-end, then dispatch agents for the rest.

**Pilot candidates** (modules with the richest source data — both Source A and Source B):

| Module   | doc/live-api/ size | Probing branch | Notes                                 |
| -------- | ------------------ | -------------- | ------------------------------------- |
| Song     | 107K               | -song          | Largest. Highest-impact for users.    |
| Clip     | 89K                | -clip          | Warp-marker case study target.        |
| Track    | medium             | -tracks        | Core LOM class.                       |
| ClipSlot | 20K                | -clipslot      | Smaller, gentler validation.          |
| Scene    | smaller            | -scene         | Smallest of the targeted-probing set. |

**Recommendation: ClipSlot.** Mid-sized (large enough to exercise the pattern across multiple members and at least one
class-level quirk; small enough to land in one sitting). Has a dedicated targeted-probing branch.

## Pilot workflow

1. **Surface the source.** Read `doc/live-api/ClipSlot.md` (local on-disk) AND check out the `targeted-probing-clipslot`
   branch's version into a temp file for comparison. The branch version is the source of truth where it exists.
2. **Walk member-by-member.** For each property / method in the source:
   - Lift the **Description** prose into `content/12.3.6/modules/ClipSlot.md` as the member's authored description
     (markdown body below the fenced YAML block).
   - Walk the metadata flags (Undo-tracked, Async visibility, Listenable, Applicable to, Available Since). Each one
     that's specific (not "unknown" / "unprobed") becomes a `behavior:` record with an `[^id]` reference in the prose
     where the claim lands.
   - Walk the module's **Probe Notes** and **Open Questions** for class-level claims; those become class-level
     `behavior:` / `quirks:` records.
3. **Validate.** Run `tools/verify/run.sh` — validator must be clean.
4. **Visual check.** Regenerate and look at the rendered page; markers should land where expected, tooltips should read
   correctly.
5. **Author review.** User reviews the pilot before we batch.

## Batch (post-pilot)

Once the pilot pattern is approved, dispatch one agent per remaining module. Each agent's prompt template:

> **Task.** Migrate the authored content for `<Module>` from `doc/live-api/<Module>.md` (and the
> `targeted-probing-<module>` branch version, if one exists) into `content/12.3.6/modules/<Module>.md`. Don't touch the
> existing fenced YAML structure or refinement blocks — only add authored `description:` prose and `behavior:` /
> `quirks:` records with `[^id]` inline references.
>
> **Source preference.** `doc/live-api/<Module>.md` (local on disk) is the primary source. If the module also has a
> `tools/apicapture/scripts/probes/probe_<module>.py` on the `targeted-probing-*` branches, mine its `NOTES` dict and
> script comments as a secondary signal.
>
> **Conventions.** See `doc/planning/content-migration.md` for the full pattern. Confidence: `medium`. Sources:
> `[informal probe]` tag, citing where the observation came from (e.g. "doc/live-api/Song.md probe notes" or "probe
> script NOTES dict on targeted-probing-song").
>
> **Acceptance.** `tools/verify/run.sh` must pass after your edits. Regenerate the MDX
> (`python tools/generate/generate_reference.py 12.3.6 --output web/src/content/docs/`); local `astro build` must
> succeed.
>
> **Out of scope.** Don't restructure the YAML schema. Don't add refinement records — those are typed/probed
> corrections, not behavioral notes. Don't invent claims; only migrate what's in the source.

Modules to delegate (38 — excludes pilot ClipSlot + foundation modules LomObject + Listener which are absorbed by their
foundation pages):

```
Application Base Browser CcControlDevice Chain ChainMixerDevice Clip
CompressorDevice Conversions Device DeviceIO DeviceParameter
DriftDevice DrumCellDevice DrumChain DrumPad Envelope Eq8Device
Groove GroovePool HybridReverbDevice Licensing LooperDevice
MaxDevice MeldDevice MidiMap MixerDevice PluginDevice RackDevice
RoarDevice Sample Scene ShifterDevice SimplerDevice Song
SpectralResonatorDevice TakeLane Track TuningSystem WavetableDevice
```

Batch in groups (e.g. 5–8 agents at a time) so we can spot-check pattern drift between batches.

## Open

- **Probe scripts on the branches** — keep them as historical reference, or fold their logic into the future Phase-3
  probe driver? Decided later; not blocking content migration.
- **Probe-summary.md** — port to a `doc/probe-categories.md` or fold into `web-rendering.md`? Probably a follow-up doc;
  not blocking.
- **`Available Since:` version tags** — Source A records these. They're useful but don't fit the current `behavior:`
  schema. Defer (could become a `since:` member-level field later).

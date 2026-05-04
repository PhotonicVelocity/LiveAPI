# Stub Verification

Three-tier verification of generated `.pyi` stubs. Run locally via `tools/verify/run.sh`; runs in CI on every
push and PR via `.github/workflows/verify-stubs.yml`.

## Tiers

### Tier 1 — `ast.parse` (`tools/verify/parse_check.py`)

Walks every `.pyi` under `stubs/<version>/Live/` and runs `ast.parse` on it. Catches malformed Python emitted
by the generator. Pure stdlib.

**Gate.** Hard fail if any file fails to parse.

### Tier 2 — Pyright internal consistency (`pyright stubs/<version>/Live`)

Treats the stubs as source code and runs pyright on them. Catches:

- References to types not imported / defined.
- Cyclic forward-references.
- Liskov violations on subclass method overrides.
- Property setter/getter type disagreements.
- Module-level expressions that don't type-check.

Does **not** catch types that are syntactically valid but semantically wrong (e.g.,
`Iterable[MidiNoteSpecification]` claimed when the binding requires `MidiNoteVector`). That's a separate
class of accuracy issue, addressed by Steps 4–5 of [stub-cleanup-plan.md](../../doc/stub-cleanup-plan.md).

**Tracking only during cleanup.** The current `main` baseline has **29 errors across 9 files** (most are
incompatible-method-override on Vector subclasses for routing types). The cleanup steps are expected to drive
this down. Running with `--strict` (or in CI's eventual gated mode) requires zero errors.

### Tier 4 — Usage tests (`pyright tests/usage/`)

Hand-picked usage patterns drawn from real Ableton-shipped Remote Scripts in
`doc/decompiled/AbletonLive12_MIDIRemoteScripts/` (gitignored — patterns copied into the test files
verbatim with attribution comments). Each pattern is something Ableton's own engineers wrote and shipped, so
it is by definition working production usage. If our stubs reject any of these patterns, the stubs are wrong
about something Ableton's code already does.

Patterns are deliberately curated, not auto-extracted (auto-extraction at scale recreates the
cargo-culted-content problem the LLM removal is solving). Expand the set when later cleanup steps surface
new gaps.

**Gate.** Hard fail on any pyright error.

### Tier 3 — Pyright `--verifytypes` (deferred)

PEP 561 completeness scoring. Reports the percentage of public symbols with known types (`Any` counts as
known). Requires the stubs to be installable as a `Live-stubs` package, which adds setup cost. Deferred
until after the LLM removal and parser audit so the score reflects the cleaned pipeline.

## Baseline (recorded against `main`, captured during Step 1 of stub-cleanup-plan)

```
Tier 1 (ast.parse):        44 stub files, all parse                          PASS
Tier 4 (usage tests):       6 usage files, 0 errors                          PASS
Tier 2 (stubs internal):   29 errors across 9 files                          tracking
  Base.pyi:        8 errors
  Track.pyi:       4 errors
  Clip.pyi:        4 errors
  Application.pyi: 4 errors
  Listener.pyi:    2 errors
  Envelope.pyi:    2 errors
  Device.pyi:      2 errors
  Browser.pyi:     2 errors
  DrumChain.pyi:   1 error
```

The 29 Tier-2 errors are the bar to drive down through the cleanup. Most look to be Liskov violations on
auto-generated Vector subclass overrides — addressed by either fixing the generator's override emission or
by the parser-defaults audit (Step 5).

## Adding a usage test

1. Find a working pattern in `doc/decompiled/AbletonLive12_MIDIRemoteScripts/<some-script>/`.
2. Copy it into a new file in `tests/usage/`, with a top-of-file comment citing the source script and line
   numbers.
3. Trim to the smallest snippet that demonstrates the pattern; remove unrelated logic.
4. Add explicit type annotations on parameters so the test pins down the expected stub shape.
5. Run `tools/verify/run.sh` locally — the new test should pyright-clean.

If the new test fails against current stubs, that's a real finding — either the stubs are missing something,
have the wrong type, or the pattern was misread. Investigate before adjusting either side.

## Commands

```bash
# Full local verification (matches CI):
tools/verify/run.sh

# Specific Live version:
tools/verify/run.sh --version 12.3.6

# Treat Tier 2 as a gate too (will fail until cleanup lands):
tools/verify/run.sh --strict

# Just the syntax check:
python3 tools/verify/parse_check.py 12.3.6

# Just the usage tests:
pyright tests/usage/

# Just the stubs internal consistency:
pyright stubs/12.3.6/Live
```

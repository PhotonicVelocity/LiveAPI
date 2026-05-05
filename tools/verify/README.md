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
`Iterable[MidiNoteSpecification]` claimed when the binding requires `MidiNoteVector`). That class of
accuracy issue is addressed by hand-curated `manual_refinements.yaml` overrides with per-entry sourced
rationale.

**Tracking only.** Currently zero errors (post-cleanup baseline). `--strict` mode promotes Tier 2 to a
hard gate; without it Tier 2 stays informational so CI can surface regressions without blocking unrelated
work.

### Tier 3 — Pyright `--verifytypes` (deferred)

PEP 561 completeness scoring. Reports the percentage of public symbols with known types (`Any` counts as
known). Requires the stubs to be installable as a `Live-stubs` package, which adds setup cost. Currently
deferred — the cleaned pipeline is in place, so this is now actionable when we want a coverage number;
just not yet wired into CI.

### Tier 4 — Usage tests (`pyright tests/usage/`)

Hand-picked usage patterns drawn from real Ableton-shipped Remote Scripts at
[gluon/AbletonLive12_MIDIRemoteScripts](https://github.com/gluon/AbletonLive12_MIDIRemoteScripts), pinned to
commit `810ef77` (single source of truth: `CORPUS_PIN` in
[`tools/fetch/corpus.py`](../fetch/corpus.py); validated by `tools/fetch/check_pin.py`). Run
`tools/fetch/bootstrap.sh` to clone the corpus to `doc/decompiled/` (gitignored). Test files cite the
upstream URL with line anchors so references stay stable across local clones. Each pattern is something
Ableton's own engineers wrote and shipped, so it is by definition working production usage. If our stubs
reject any of these patterns, the stubs are wrong about something Ableton's code already does.

Patterns are deliberately curated, not auto-extracted (auto-extraction at scale recreates the
cargo-culted-content problem of the dropped LLM-resolve flow). Expand the set when refinement work or
new captures surface gaps.

**Gate.** Hard fail on any pyright error.

## Current baseline

```
Tier 1 (ast.parse):       44 stub files, all parse           PASS
Tier 2 (stubs internal):  0 errors                           tracking (now clean)
Tier 4 (usage tests):      8 usage files, 0 errors           PASS
```

All three active tiers green on the post-cleanup baseline (Tier 3 deferred). CI surfaces regressions;
`--strict` promotes Tier 2 to a hard gate.

## Adding a usage test

1. Find a working pattern in the
   [gluon/AbletonLive12_MIDIRemoteScripts](https://github.com/gluon/AbletonLive12_MIDIRemoteScripts) corpus
   (cloned at `doc/decompiled/AbletonLive12_MIDIRemoteScripts/` via `tools/fetch/bootstrap.sh`).
2. Copy it into a new file in `tests/usage/`, with a top-of-file comment and inline references citing the
   **upstream URL** with line anchors, pinned to the active `CORPUS_PIN`. Format:
   ```
   https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/<CORPUS_PIN>/<path>#L<start>-L<end>
   ```
3. Trim to the smallest snippet that demonstrates the pattern; remove unrelated logic.
4. Add explicit type annotations on parameters so the test pins down the expected stub shape.
5. Run `tools/verify/run.sh` locally — the new test should pyright-clean (and `check_pin.py` should pass,
   confirming the new file's URLs match `CORPUS_PIN`).

If the new test fails against current stubs, that's a real finding — either the stubs are missing something,
have the wrong type, or the pattern was misread. Investigate before adjusting either side.

When the corpus pin is bumped (a new Live version's decompiled scripts land):
1. Update `CORPUS_PIN` in `tools/fetch/corpus.py`.
2. `tools/fetch/bootstrap.sh --force` to re-fetch.
3. `sed -i '' "s/810ef77/<new>/g" tests/usage/*.py tools/verify/README.md` (or the equivalent rename pass).
4. Run `tools/verify/run.sh` — `check_pin.py` validates the sweep was complete; Tier 4 catches any patterns
   that no longer apply.

## Offline corpus audit (not in CI)

`tools/verify/audit_corpus.py` runs pyright over the full decompiled Ableton Remote Script corpus
(`doc/decompiled/AbletonLive12_MIDIRemoteScripts/`) using our stubs as the type source. Surfaces places
where the stubs disagree with working production code. Filters out internal-module imports, decompilation
artifacts, and errors that don't mention a class declared in our stubs. Not a CI gate — research tool.

```bash
python3 tools/verify/audit_corpus.py             # grouped summary (default)
python3 tools/verify/audit_corpus.py --raw       # ungrouped, full message text
python3 tools/verify/audit_corpus.py --top 30    # top 30 grouped shapes
python3 tools/verify/audit_corpus.py --all-noise # disable Live-class restriction
```

### Suppressing investigated-and-declined findings

`tools/verify/audit_ignores.yaml` records audit findings we've investigated and decided not to fix. Each
entry includes a `rationale` and `investigated` date so future re-investigation can decide whether the
entry is still valid. Match shape:

```yaml
ignores:
  - id: <stable-identifier>
    investigated: <YYYY-MM-DD>
    match:
      file_contains: <substring> # optional
      message_contains: <substring> # optional; at least one matcher required
    rationale: |
      Why this finding is corpus-side noise / Ableton-side pattern / out-of-scope —
      not a real stub bug to fix.
```

The audit script applies these after the standard filters and surfaces a per-id breakdown so it's clear
how many findings each ignore is suppressing. **Real stub bugs are fixed, not ignored** — only add an
entry once you've confirmed the finding is corpus-side or out-of-scope.

## Commands

```bash
# Full local verification (matches CI):
tools/verify/run.sh

# Specific Live version:
tools/verify/run.sh --version 12.3.6

# Treat Tier 2 as a gate too:
tools/verify/run.sh --strict

# Just the syntax check:
python3 tools/verify/parse_check.py 12.3.6

# Just the usage tests:
pyright tests/usage/

# Just the stubs internal consistency:
pyright stubs/12.3.6/Live
```

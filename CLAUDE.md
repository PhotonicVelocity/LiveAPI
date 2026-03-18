# AGENTS

This file captures standing repo-level instructions for work in `LiveAPI`.

## What This Project Is

LiveAPI is a comprehensive reference for the Ableton Live Object Model (LOM) — the object hierarchy exposed by Live's
Python runtime. It documents classes, properties, methods, enums, and behavioral notes that Ableton doesn't publicly
document. The reference is the primary deliverable; everything else (tooling, build output, Max for Live docs) exists to
produce and maintain it.

## Priorities

1. Follow explicit user instructions for the current task.
2. Preserve existing work; never discard unrelated changes.
3. The reference docs are the product — keep them clean, accurate, and well-structured.

## Context Compaction

After every context compaction (when the conversation summary replaces earlier messages), re-read this CLAUDE.md file
before continuing work. The summary may lose repo-specific constraints that are captured here.

## Formatting

- Wrap lines at 120 characters in all files (code, docs, markdown).
- After editing any markdown file, run `prettier --prose-wrap preserve --write <file>` to normalize formatting.

## Git Safety

- Do not run destructive git commands unless explicitly requested.
- Do not amend commits unless explicitly requested.
- If unexpected modifications appear, stop and ask before proceeding.

## Targeted Probing

The targeted probe phase (`tools/apicapture/scripts/probes/`) formalizes the ad-hoc exploratory probing previously done
in `PythonForLive/.tmp/`. Each probe script runs inside Live via the APICapture trigger system and produces structured,
deterministic results in `stubs/<version>/pipeline/ProbeResults.json`.

The goal is to systematically document Live API behavioral metadata — undo tracking, async visibility, side effects,
argument ranges, error conditions — that isn't available from introspection alone. Results should be reproducible and
machine-parseable so downstream tooling (stub generation, reference docs) can consume them directly.

Probes should avoid edge cases in their baseline measurements (e.g. use middle indices for create/duplicate to avoid
end-of-list selection quirks). Quirky behaviors discovered during probing should be noted for later targeted tests that
specifically document those edge cases.

Probes run against Live's built-in Demo Set, which provides a rich environment (tracks with devices, clips with
automation, chains, MIDI content). A JSON dump of the demo set's structure is available at
`~/dev/ableton-api/PythonForLive/tests/integration/fixtures/demo_song_export.json` — use it to find specific objects
by index when writing probes (e.g. which track has a rack device, which clip slot has a clip).

```bash
echo scripts/probes/song_props.py > /tmp/apicapture_targeted_probe   # trigger a targeted probe
cat /tmp/apicapture_targeted_probe_done                               # read output path when done
```

## APICapture Hot Reload

The APICapture Control Surface runs from a **copy** in `~/Music/Ableton/User Library/Remote Scripts/APICapture/`, not
from the source tree. After editing files in `tools/apicapture/scripts/`, you must reinstall before hot reload will pick
up changes:

```bash
python tools/install.py                  # copy updated source to Remote Scripts
touch /tmp/apicapture_capture            # trigger raw capture (CaptureModule)
touch /tmp/apicapture_probe              # trigger basic probe (PropertyProbe only)
touch /tmp/apicapture_full_probe         # trigger full probe (PropertyProbe + DeviceProbe)
touch /tmp/apicapture_run                # trigger full pipeline (capture + full probe)
echo verbose > /tmp/apicapture_probe     # include instance data in probe output
```

Scripts in `scripts/` are reloaded via `importlib.reload()` on every trigger, so code changes take effect immediately
after reinstalling. Changes to `APICapture.py` or `__init__.py` require a full Live restart.

## Dev Server

```bash
# Start (background, no terminal hold):
nohup ./tools/other/serve.sh > /tmp/mkdocs.log 2>&1 &

# Stop:
kill $(lsof -ti:8123)
```

Serves at http://localhost:8123/LiveAPI/

## Governing Docs

- **Decisions** — `doc/decisions.md`: terminology, project structure, parse pipeline, reference format, navigation,
  publishing, tooling direction.
- **Reference format** — `doc/contributing.md`: page structure template and format principles.

## Project Structure

- `reference/` — curated per-class LOM reference docs (the product)
  - `index.md` — landing page for the MkDocs site
  - `tracks/` — Track, Clip, ClipSlot, Envelope, MixerDevice, TakeLane
  - `devices/` — all device classes (base + subclasses)
  - `other/` — Conversions, Groove, GroovePool, TuningSystem
- `stubs/` — per-version generated stubs (`<version>/Live/`) with pipeline intermediates in `<version>/pipeline/`
- `MaxForLive/` — API docs parsed from Max for Live HTML documentation
- `tools/` — APICapture and build tooling
  - `apicapture/` — APICapture Control Surface (runs inside Live, captures API metadata)
  - `parse/` — parsing and stub generation pipeline (see `doc/decisions.md` for full diagram)
  - `other/` — legacy/utility scripts (serve.sh, watch.py, v1 StubGenerator)
  - `install.py` — installs APICapture to Remote Scripts folder
  - `sets/` — Ableton Live sets used with APICapture for probing
- `doc/` — project-level documentation (decisions, contributing)

## Reference Format

Each reference file documents one LOM class following this structure:

1. `# ClassName` — page title
2. `> Live.Namespace.ClassName` — full LOM path
3. Description
4. Raw probe notes (temporary, collapsed) — will be removed as tooling matures
5. Children — summary table + per-child details
6. Properties — summary table + per-property details
7. Methods — summary table + per-method details
8. Enums — value tables
9. Open Questions

Per-member sections use: Type, Listenable, Since, Description, Quirks (optional), Limitations (optional).

Do NOT include Sources, Probe Status, Undo-tracked, Async visibility, or Applicable to in member metadata — these are
either contributor-only or too verbose. Document in description or quirks when relevant.

## Terminology

- **LOM (Live Object Model)** — the object hierarchy. Not Max-specific; same model accessed by Remote Scripts, Max for
  Live, and LiveRelay.
- **Namespace** — the Python module containing a class (e.g., `Live.Song` is the namespace, `Song` is the class).
- Prefer "LOM" over "Live Python API" when referring to the object structure.

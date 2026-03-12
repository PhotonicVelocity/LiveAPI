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
nohup ./tools/serve.sh > /tmp/mkdocs.log 2>&1 &

# Stop:
kill $(lsof -ti:8123)
```

Serves at http://localhost:8123/LiveAPI/

## Governing Docs

- **Decisions** — `doc/decisions.md`: terminology, project structure, reference format, navigation, publishing, tooling
  direction.
- **Reference format** — `doc/contributing.md`: page structure template and format principles.

## Project Structure

- `reference/` — curated per-class LOM reference docs (the product)
  - `index.md` — landing page for the MkDocs site
  - `tracks/` — Track, Clip, ClipSlot, Envelope, MixerDevice, TakeLane
  - `devices/` — all device classes (base + subclasses)
  - `other/` — Conversions, Groove, GroovePool, TuningSystem
- `build/` — auto-generated API stubs and XML dumps per Live version (11.0–12.3.5)
- `MaxForLive/` — API docs parsed from Max for Live HTML documentation
- `tools/` — APICapture and build tooling
  - `apicapture/` — APICapture Control Surface (runs inside Live, captures API metadata)
  - `install.py` — installs APICapture to Remote Scripts folder
  - `watch.py` — tails Ableton's log file for debugging
  - `justfile` — shortcuts for install/build/reload workflow
  - `set/` — Ableton Live set used with APICapture
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

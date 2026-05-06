# AGENTS

This file captures standing repo-level instructions for work in `LiveAPI`.

## What This Project Is

LiveAPI documents the Ableton Live Object Model (LOM) — the object hierarchy exposed by Live's Python runtime. It ships
two products from one introspection pipeline:

1. **Typed Python stubs** (`stubs/<version>/Live/`) — `.pyi` modules for autocomplete + static type checking, published
   as a PEP 561 stub-only package.
2. **Reference docs** (`reference/`) — per-class HTML documentation, generated from the stubs and published via
   MkDocs at [photonicvelocity.github.io/LiveAPI](https://photonicvelocity.github.io/LiveAPI/).

Tooling, captured externals, and posture decisions all exist to keep both products accurate and verifiable.

## Priorities

1. Follow explicit user instructions for the current task.
2. Preserve existing work; never discard unrelated changes.
3. Stubs and reference are the products — keep them accurate, sourced, and verifiable.

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
nohup ./tools/other/serve.sh > /tmp/mkdocs.log 2>&1 &

# Stop:
kill $(lsof -ti:8123)
```

Serves at http://localhost:8123/LiveAPI/

## Governing Docs

- **Decisions** — `doc/decisions.md`: terminology and the "Stub Accuracy and Pipeline Posture" rationale
  cited from the parse / generate / verify tooling.
- **Tools README** — `tools/README.md`: full pipeline (capture → parse → generate).
- **Verify README** — `tools/verify/README.md`: the four-tier verification gates.

## Project Structure

- `stubs/` — per-version generated stubs. `<version>/Live/` is tracked output; `<version>/pipeline/` holds gitignored
  intermediates (raw capture, parsed tree, refinements).
- `reference/` — per-class reference markdown, generated from stubs by `tools/generate/generate_reference.py`. Topology:
  flat top-level pages (Song, Application, Browser, …) plus subdirs `tracks/`, `devices/`, `other/`.
- `tools/` — capture + parse + generate + verify + publish pipeline.
  - `apicapture/` — APICapture Control Surface (runs inside Live; produces raw tree + probe data).
  - `parse/` — parser, manual refinements, and the apply step that produces `LiveTree.parsed.json`.
  - `generate/` — stub generator and reference-markdown generator.
  - `verify/` — four-tier verification suite (`run.sh`, `parse_check.py`, `audit_corpus.py`, `audit_ignores.yaml`).
  - `publish/` — wheel builder + PyPI release glue.
  - `fetch_external/` — bootstrap for `external/` (corpus pin, M4L docs, release notes).
  - `sets/` — Ableton Live sets used as fixtures by the probe.
  - `other/` — small dev utilities (`serve.sh`, `watch.py`, `swap_live.py`, `quit_live.py`).
  - `install.py` — installs APICapture to Live's Remote Scripts folder.
  - `run_pipeline.py` — full Stage 1 + 2 + 3 orchestrator.
- `external/` — gitignored, populated by `tools/fetch_external/bootstrap.sh`:
  - `corpus/` — decompiled Ableton Remote Scripts (Tier 4 usage tests + offline audit; pinned via `CORPUS_PIN`).
  - `max-for-live-docs/` — parsed Max for Live HTML reference (docstring source only).
  - `release-notes/` — Live release notes for cross-referencing version-introduction.
- `tests/usage/` — hand-curated Tier 4 usage patterns drawn from the corpus.
- `doc/` — `decisions.md` (terminology + the "Stub Accuracy and Pipeline Posture" rationale cited from tooling).

## Terminology

- **LOM (Live Object Model)** — the object hierarchy. Not Max-specific; the same runtime is accessed by Remote Scripts,
  Max for Live, and any RPC bridge wrapping it.
- **Namespace** — the Python module containing a class (e.g., `Live.Song` is the namespace, `Song` is the class).
- Prefer "LOM" or "Live Object Model" over "Live Python API" when referring to the object structure.

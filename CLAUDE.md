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

## Formatting

- Wrap lines at 120 characters in all files (code, docs, markdown).
- After editing any markdown file, run `prettier --prose-wrap preserve --write <file>` to normalize formatting.

## Git Safety

- Do not run destructive git commands unless explicitly requested.
- Do not amend commits unless explicitly requested.
- If unexpected modifications appear, stop and ask before proceeding.

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
- `tools/` — introspection and build tooling
  - `introspection/` — MakeDoc Control Surface (runs inside Live, dumps API surfaces)
  - `install.py` — installs the introspection script to Remote Scripts folder
  - `watch.py` — tails Ableton's log file for debugging
  - `justfile` — shortcuts for install/build/reload workflow
  - `set/` — Ableton Live set used with introspection tooling
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

# LiveAPI

Comprehensive reference for the Ableton Live Python API — classes, properties, methods, enums, and behavioral notes
that Ableton doesn't publicly document.

## Purpose

Ableton does not publish documentation for the Python API embedded in Live. The best available sources are auto-generated
stubs (incomplete types, no behavioral notes), Max for Live docs (partial coverage, not always current), and tribal
knowledge scattered across forums and source code. LiveAPI synthesizes all of these — plus direct runtime probing — into
a single accurate, browsable reference.

## Audience

Anyone working with Live's Python API:

- Remote Script / Control Surface authors
- Max for Live developers
- [LiveRelay](https://github.com/PhotonicVelocity/LiveRelay) and
  [PythonForLive](https://github.com/PhotonicVelocity/PythonForLive) contributors and users
- [AbletonOSC](https://github.com/ideoforms/AbletonOSC) contributors
- Anyone building tools that interact with Live programmatically

## Project Structure

### `reference/` — The Product

Curated per-class reference docs. Each file covers one Live API class with its properties, methods, children, enums, and
behavioral notes. This is the primary deliverable of the project — everything else exists to produce and maintain it.

See [reference/README.md](reference/README.md) for coverage status, format guidelines, and contributing instructions.

Published as a searchable site via GitHub Pages (MkDocs + Material theme).

### `build/` — Generated Output

Per-version output from the introspection pipeline. Each version directory (e.g., `build/12.3.6/`) contains:

- `Live.xml` — raw API dump (classes, methods, properties, docstrings)
- `probe_results.json` — runtime metadata (types, settability, listeners, enums)
- `Live/` — typed Python stubs

### `MaxForLive/` — Parsed Max for Live Docs

API documentation extracted from Max for Live's HTML docs. Another source for cross-referencing when writing reference
docs. Richer descriptions than stubs but does not cover the full API.

### `tools/` — Introspection and Build Tooling

Two-phase pipeline for generating typed stubs from Live's API:

**Phase 1: Capture** (runs inside Live)

`tools/introspection/` is a MIDI Remote Script that introspects the `Live` module at runtime and writes raw data files.
Install with `python tools/install.py`, then start Live.

- `DocumentationGenerator` — walks `Live` module via `dir()` / `inspect` → `Live.xml`
- `ProbeGenerator` — walks the live object tree for runtime types → `probe_results.json`

**Phase 2: Generate stubs** (runs outside Live)

```
python tools/generate_stubs.py build/<version>
```

Reads `Live.xml` and `probe_results.json`, produces typed Python stubs in `build/<version>/Live/`.

### Sources and Synthesis

The reference docs are built from three sources:

1. **Generated stubs** (`build/`) — complete class/method/property inventory with runtime types
2. **Max for Live docs** (`MaxForLive/`) — richer descriptions and gotcha coverage, but partial API coverage
3. **Direct probing** — runtime verification of behavior that neither source clarifies

Each reference file records its probe status (`unprobed`, `partial`, or `verified`) so coverage gaps are visible.

## Related Projects

- [LiveRelay](https://github.com/PhotonicVelocity/LiveRelay) — Remote Script that exposes the Live API over RPC
- [PythonForLive](https://github.com/PhotonicVelocity/PythonForLive) — Typed Python client for LiveRelay

## Credits

Introspection tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

## Disclaimer

This is unofficial documentation for the Ableton Live API. These files are provided as-is, without any warranty. Do not
contact Ableton with questions about this project.

# LiveAPI

Comprehensive reference for the Ableton Live Python API — classes, properties, methods, enums, and behavioral notes
that Ableton doesn't publicly document.

## Overview

Ableton does not publish documentation for the Python API embedded in Live. LiveAPI fills that gap with:

- **Curated reference docs** — per-class documentation with properties, methods, enums, and behavioral notes
- **Typed Python stubs** — use in your Control Surface or Remote Script for autocomplete and type checking

## Reference Docs

The [`reference/`](reference/) directory contains per-class documentation for the Live Object Model, generated from
the stubs by [`tools/generate/generate_reference.py`](tools/generate/generate_reference.py). Each file covers one
class with summary tables, detailed member descriptions, quirks, and open questions.

Published as a searchable site via GitHub Pages (MkDocs + Material theme).

## Using the Stubs

Pre-built stubs for the latest tracked Live version live at [`stubs/12.3.6/Live/`](stubs/12.3.6/Live/) — typed
modules you can use for autocomplete and static analysis.

To use in a Control Surface project, add the stubs directory to your type checker's stub path
(e.g., `"stubPath": "stubs/12.3.6"` in pyrightconfig.json). The stubs include a `py.typed` marker for PEP 561
compatibility.

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import Live
    from Live.Song import Song

def on_tempo_changed(song: Song) -> None:
    app: Live.Application.Application = Live.Application.get_application()
    print(f"Live {app.get_major_version()}: tempo is now {song.tempo}")
```

## Project Structure

```
stubs/         Typed .pyi modules for the latest tracked Live version
reference/    Per-class API docs generated from the stubs (mkdocs-published)
tools/         APICapture + parse + generate pipeline (see tools/README.md)
```

## First-time Setup

Two external sources need to be on disk before the pipeline + verify suite work:
the decompiled Remote Scripts corpus (used by Tier 4 usage tests + the offline
audit) and the Max for Live LOM docs (cited by `manual_refinements.yaml`).

```bash
tools/fetch/bootstrap.sh           # corpus + M4L 9.0
tools/fetch/bootstrap.sh --all     # also M4L 8.0 (legacy) + release notes
```

Both targets are gitignored. The corpus is pinned to a specific commit in
[`tools/fetch/corpus.py`](tools/fetch/corpus.py) (`CORPUS_PIN`); `tools/fetch/check_pin.py`
validates that every reference (test docstrings, README) matches.

## Sources

The pipeline draws from four sources, in roughly increasing order of authority:

1. **Runtime introspection** (APICapture) — class/method/property inventory captured by `dir()` walking and
   property probing inside Live. The base structure of every stub.
2. **Max for Live docs** ([`doc/max-for-live-docs/`](doc/max-for-live-docs/)) — richer descriptions and parameter
   names; partial API coverage.
3. **Decompiled Remote Scripts** (corpus) — Ableton's own shipped Python code provides ground truth for
   parameter names and call shapes. Auto-cloned to `doc/decompiled/`.
4. **`tools/parse/manual_refinements.yaml`** — hand-curated overrides with a per-entry `source:` field documenting
   the rationale (corpus def-site, M4L doc citation, raw_doc, etc.). Enforced by the apply step.

Each reference file records its probe status (`unprobed`, `partial`, or `verified`) so coverage gaps are visible.

## Related Projects

- [LiveRelay](https://github.com/PhotonicVelocity/LiveRelay) — Remote Script that exposes the Live API over RPC
- [PythonForLive](https://github.com/PhotonicVelocity/PythonForLive) — Typed Python client for LiveRelay

## Credits

APICapture tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

## Disclaimer

This is unofficial documentation for the Ableton Live API. These files are provided as-is, without any warranty. Do not
contact Ableton with questions about this project.

# LiveAPI

Comprehensive reference for the Ableton Live Python API — classes, properties, methods, enums, and behavioral notes
that Ableton doesn't publicly document.

## Overview

Ableton does not publish documentation for the Python API embedded in Live. LiveAPI fills that gap with:

- **Curated reference docs** — per-class documentation with properties, methods, enums, and behavioral notes
- **Typed Python stubs** — use in your Control Surface or Remote Script for autocomplete and type checking

## Reference Docs

The [`reference/`](reference/) directory contains per-class documentation for the Live Object Model. Each file covers
one class with summary tables, detailed member descriptions, quirks, and open questions.

Published as a searchable site via GitHub Pages (MkDocs + Material theme).

## Using the Stubs

Pre-built stubs for each Live version are available in [`build/`](build/). Each version directory contains a `Live/`
package with typed modules you can use for autocomplete and static analysis.

To use in a Control Surface project, add the relevant `build/<version>/Live/` directory to your type checker's search
path. The stubs include a `py.typed` marker for PEP 561 compatibility.

## Project Structure

```
reference/     Curated per-class API docs (the primary product)
build/         Generated stubs and capture data per Live version
MaxForLive/    API docs parsed from Max for Live HTML documentation
tools/         APICapture and stub generation pipeline (see tools/README.md)
```

## Sources

The reference docs are built from three sources:

1. **Generated stubs** — complete class/method/property inventory from runtime introspection
2. **Max for Live docs** — richer descriptions and gotcha coverage, partial API coverage
3. **Direct probing** — runtime verification of behavior that neither source clarifies

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

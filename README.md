# LiveAPI

Comprehensive reference for the Ableton Live Python API — classes, properties, methods, enums, and behavioral notes
that Ableton doesn't publicly document.

## What's Here

- **`reference/`** — Curated per-class reference docs synthesized from stubs, Max for Live docs, and direct probing.
  See [reference/README.md](reference/README.md) for coverage and contributing guidelines.
- **`build/`** — Generated API stubs and XML dumps per Live version (11.0 through 12.3.5).
- **`MaxForLive/`** — API docs parsed from Max for Live HTML documentation.
- **`src/`** — Introspection tooling (runs as a Control Surface inside Live to dump API surfaces).

## Audience

Anyone working with Live's Python API:

- Remote Script / Control Surface authors
- Max for Live developers
- [LiveRelay](https://github.com/PhotonicVelocity/LiveRelay) and [PythonForLive](https://github.com/PhotonicVelocity/PythonForLive) users
- [AbletonOSC](https://github.com/ideoforms/AbletonOSC) contributors
- Anyone building tools that interact with Live programmatically

## Credits

Introspection tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

## Disclaimer

This is unofficial documentation for the Ableton Live API. These files are provided as-is, without any warranty. Do not
contact Ableton with questions about this project.

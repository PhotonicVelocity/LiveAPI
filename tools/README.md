# Introspection and Stub Generation

Two-phase pipeline for capturing Live API metadata and generating typed Python stubs.

## Phase 1: Capture (runs inside Live)

`introspection/` is a MIDI Remote Script (Control Surface) that introspects the `Live` module at runtime and writes raw
data files to `build/<version>/`.

### Install

```
python tools/install.py
```

This copies the introspection package into Ableton's MIDI Remote Scripts directory with the output path configured to
`build/`. After installing, start Live and select **MakeDoc** as a Control Surface in Preferences → Link, Tempo & MIDI.

### What It Captures

- `DocumentationGenerator` — walks the `Live` module via `dir()` / `inspect` → `Live.xml` (classes, methods,
  properties, docstrings)

### Hot Reload

After the initial capture, MakeDoc polls for a trigger file. To re-run capture without restarting Live:

```
touch /tmp/makedoc_reload
```

The generator modules are reloaded via `importlib.reload()`, so code changes to `DocumentationGenerator` or `Generator`
take effect immediately.

## Phase 2: Generate Stubs (runs outside Live)

```
python tools/generate_stubs.py build/<version>
```

Reads `Live.xml` from the build directory and produces typed Python stubs in `build/<version>/Live/`. The stubs include:

- Per-class modules in `Live/<ClassName>.py`
- Monolithic `Live/__init__.py` with all classes
- Enum classes with typed values
- Listener method stubs (`add_*_listener`, `remove_*_listener`, `*_has_listener`)
- `py.typed` marker for PEP 561

### Options

```
python tools/generate_stubs.py build/12.3.6              # version inferred from directory name
python tools/generate_stubs.py build/12.3.6 --version 12.3.6  # version specified explicitly
```

## Pipeline Structure

```
tools/
├── install.py              Install the capture script into Live's Remote Scripts
├── generate_stubs.py       CLI for offline stub generation
├── introspection/          The MIDI Remote Script package
│   ├── __init__.py         Control Surface entry point
│   ├── MakeDoc.py          Capture orchestrator + hot reload
│   ├── generators/
│   │   ├── Generator.py        Base class (module walking, file I/O)
│   │   ├── DocumentationGenerator.py   XML output
│   │   └── StubGenerator.py    Python stub output (used by generate_stubs.py)
│   └── helpers/
│       └── app.py          Version number extraction
├── justfile                Task runner shortcuts
├── serve.sh                Local docs preview server
└── watch.py                File watcher for development
```

## Credits

Introspection tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

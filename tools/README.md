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

`CaptureGenerator` walks the `Live` module recursively via `dir()` and `inspect`, producing `Live.json` — a flat list of
every discoverable API element with its qualified name and docstring (if any).

**Output format** (`Live.json`):

```json
{
  "version": "12.3.6",
  "python_version": "3.11.6",
  "elements": [
    { "kind": "Module", "name": "Live.Application" },
    {
      "kind": "Class",
      "name": "Live.Application.Application",
      "doc": "This class represents..."
    },
    {
      "kind": "Property",
      "name": "Live.Application.Application.browser",
      "doc": "Returns..."
    },
    {
      "kind": "Method",
      "name": "Live.Application.Application.get_document()",
      "doc": "get_document(..."
    }
  ]
}
```

**Element kinds:**

| Kind       | Count (12.3.6) | Description                                                             |
| ---------- | -------------- | ----------------------------------------------------------------------- |
| `Module`   | 44             | Top-level modules under `Live` (e.g., `Live.Song`, `Live.Track`)        |
| `Class`    | 147            | Classes and sub-classes (e.g., `Live.Song.Song`, `Live.Song.Song.View`) |
| `Method`   | 1796           | Instance methods, including listener add/remove/has methods             |
| `Property` | 929            | Properties exposed by classes                                           |
| `Built-In` | 33             | Module-level static functions                                           |

**Boost.Python quirks:** Live's C++ bindings (Boost.Python) sometimes concatenate the docstring onto `__name__`. The
capture handles this by detecting the overlap and splitting at CamelCase boundaries to recover the real class name.

### Hot Reload

After the initial capture, MakeDoc polls for a trigger file. To re-run capture without restarting Live:

```
touch /tmp/makedoc_reload
```

The generator modules are reloaded via `importlib.reload()`, so code changes to `CaptureGenerator` or `Generator` take
effect immediately.

## Phase 2: Generate Stubs (runs outside Live)

```
python tools/generate_stubs.py build/<version>
```

Reads `Live.json` from the build directory and produces typed Python stubs in `build/<version>/Live/`. The stubs include:

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
│   │   ├── Generator.py            Base class (module walking, file I/O)
│   │   ├── CaptureGenerator.py     JSON capture output
│   │   └── StubGenerator.py        Python stub output (used by generate_stubs.py)
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

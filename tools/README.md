# Introspection and Stub Generation

Three-phase pipeline for capturing Live API metadata and generating typed Python stubs.

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

`CaptureGenerator` walks the `Live` module recursively via `dir()` and `inspect`, producing `Live.json` — a structured
list of every discoverable API element. Boost.Python docstrings are parsed into structured fields (args with types and
defaults, return types, descriptions, C++ signatures). Enum classes are detected automatically.

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
      "kind": "Class",
      "name": "Live.Song.Quantization",
      "enum": true,
      "enum_values": { "q_2_bars": 1, "q_4_bars": 2, "q_8_bars": 3 }
    },
    {
      "kind": "Property",
      "name": "Live.Application.Application.browser",
      "doc": "Returns the application's browser."
    },
    {
      "kind": "Method",
      "name": "Live.Song.Song.continue_playing()",
      "returns": "None",
      "doc": "Continue playing the song from the current position.",
      "cpp_signature": "void continue_playing(TPyHandle<ASong>)"
    },
    {
      "kind": "Method",
      "name": "Live.Song.Song.get_beats_loop_start()",
      "args": [{ "name": "quarters", "type": "float" }],
      "returns": "BeatTime",
      "cpp_signature": "..."
    },
    {
      "kind": "Built-In",
      "name": "Live.Application.get_application()",
      "returns": "Application",
      "doc": "Returns the current Live application instance."
    }
  ]
}
```

**Element kinds:**

| Kind       | Count (12.3.6) | Description                                                      |
| ---------- | -------------- | ---------------------------------------------------------------- |
| `Module`   | 44             | Top-level modules under `Live` (e.g., `Live.Song`, `Live.Track`) |
| `Class`    | 147            | Classes and sub-classes, including 43 auto-detected enums        |
| `Method`   | 1753           | Instance methods, including listener add/remove/has methods      |
| `Property` | 929            | Properties exposed by classes                                    |
| `Built-In` | 33             | Module-level static functions                                    |

**Structured fields** (on Method and Built-In elements):

| Field           | Description                                                           |
| --------------- | --------------------------------------------------------------------- |
| `args`          | List of `{name, type, default?}` dicts (self is stripped for Methods) |
| `returns`       | Return type string                                                    |
| `doc`           | Human-readable description                                            |
| `cpp_signature` | Raw C++ signature from Boost.Python                                   |

**Boost.Python quirks:** Live's C++ bindings sometimes concatenate docstrings onto `__name__` or corrupt return types by
appending class docs. The capture handles both cases by detecting overlaps and splitting at CamelCase boundaries.

### Hot Reload

After the initial capture, MakeDoc polls for a trigger file. To re-run capture without restarting Live:

```
touch /tmp/makedoc_reload
```

The generator modules are reloaded via `importlib.reload()`, so code changes to `CaptureGenerator` or `Generator` take
effect immediately.

## Phase 2: Probe (runs inside Live)

`ProbeGenerator` reads live object properties to determine runtime types, settability, and listener support. It uses
`Live.json` from Phase 1 as its input — iterating over captured classes and properties, navigating the Live Object Model
to reach an instance of each class, then reading each property value to record its `type()`.

### How It Works

The probe needs a live instance of each class to read properties from. It navigates the object tree starting from a
fresh empty Live set:

- **Root objects** — `Application`, `Song`, `Song.View` are directly accessible
- **Collection traversal** — `Song.tracks[0]` → `Track`, `Track.clip_slots[0]` → `ClipSlot`, etc.
- **Nested navigation** — `Track.mixer_device` → `MixerDevice`, `MixerDevice.volume` → `DeviceParameter`
- **Unreachable classes** — classes that require specific session state (e.g., a loaded Wavetable device, a clip with
  automation) are skipped and logged

### What It Probes

For each reachable class, the probe records:

- **Property types** — `type(getattr(obj, prop_name)).__name__` for each property
- **Vector element types** — for sequence properties, probes `value[0]` to get the element type
- **Settability** — checks `prop.fset is not None` on the descriptor (no mutation, purely read-only)
- **Listeners** — which properties support `add_*_listener` (detected by checking for the method)
- **Enum detection** — confirms enum classes identified in Phase 1

### Output Format (`probe_results.json`)

```json
{
  "Song.Song": {
    "properties": {
      "tempo": {
        "runtime_type": "float",
        "settable": true
      },
      "tracks": {
        "runtime_type": "Vector",
        "runtime_element_type": "Track"
      },
      "is_playing": {
        "runtime_type": "bool",
        "settable": false
      }
    },
    "listeners": ["tempo", "is_playing", "tracks", "current_song_time"]
  },
  "Song.Quantization": {
    "likely_enum": true,
    "enum_values": { "q_2_bars": 1, "q_4_bars": 2, "q_8_bars": 3 }
  }
}
```

### Running

The probe runs as a separate pass after capture, triggered the same way:

```
touch /tmp/makedoc_probe
```

It requires a Live session with a document open (at least one track, one clip slot). The probe is read-only — it does
not modify the Live session, create clips, or change any state. Properties that raise on read are logged and skipped.
DeprecationWarnings are suppressed during probing so deprecated properties are still captured for older Live version
compatibility.

## Phase 3: Generate Stubs (runs outside Live)

```
python tools/generate_stubs.py build/<version>
```

Reads `Live.json` and (optionally) `probe_results.json` from the build directory and produces typed Python stubs in
`build/<version>/Live/`. The stubs include:

- Per-class modules in `Live/classes/<ClassName>.py`
- Monolithic `Live/__init__.py` with all classes
- Typed method signatures with args, defaults, and return types
- Listener callbacks typed as `Callable`
- Enum classes with named int values
- Listener method stubs from probe data (`add_*_listener`, `remove_*_listener`, `*_has_listener`)
- Property return types and setters from probe data (when `probe_results.json` is available)
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
│   │   ├── CaptureGenerator.py     Phase 1: JSON capture output
│   │   ├── ProbeGenerator.py       Phase 2: runtime property type probing
│   │   └── StubGenerator.py        Phase 3: Python stub output (used by generate_stubs.py)
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

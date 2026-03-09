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
Nothing runs automatically on startup — MakeDoc just starts its tick loop and waits for trigger files.

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

To run or re-run capture without restarting Live:

```
touch /tmp/makedoc_reload
```

The generator modules are reloaded via `importlib.reload()`, so code changes to `CaptureGenerator` or `Generator` take
effect immediately.

## Phase 2: Probe (runs inside Live)

`PropertyProbe` reads live object properties to determine runtime types, settability, and listener support. It uses
`Live.json` from Phase 1 as its input — iterating over captured classes and properties, navigating the Live Object Model
to reach an instance of each class, then reading each property value to record its `type()`.

### How It Works

The probe needs a live instance of each class to read properties from. Object collection happens in three phases within
`_collect_live_objects()`:

1. **Natural walk** — traverses the object tree from Application/Song downward, registering every reachable instance in
   a fresh empty Live set. First registration wins so that richer instances (e.g., audio track over MIDI track) take
   priority. Examples:
   - **Root objects** — `Application`, `Song`, `Song.View` are directly accessible
   - **Collection traversal** — `Song.tracks[0]` → `Track`, `Track.clip_slots[0]` → `ClipSlot`, etc.
   - **Nested navigation** — `Track.mixer_device` → `MixerDevice`, `MixerDevice.volume` → `DeviceParameter`

2. **Construction** — instantiates standalone value types that exist independently of any Live document.
   `CCFeedbackRule()`, `NoteFeedbackRule()`, `PitchBendFeedbackRule()`, `Base.Timer()` can all be constructed directly
   from the `Live` module. Construction runs before scaffolding so that anything obtainable without mutating the set is
   registered first.

3. **Scaffolding** — creates temporary Live objects (clips, MIDI notes, automation envelopes, etc.) to reach classes
   that don't exist in a fresh empty set. Each `_ensure_*` method follows the pattern: check if already registered →
   create the object → register it → append a cleanup callable to `self._cleanup`. Cleanup runs in LIFO order after
   probing completes.

**Alt-instance probing** — when different instances of the same class expose different subsets of properties (e.g.,
master track mixer has `crossfader`/`cue_volume`/`song_tempo` while regular track mixer has `crossfade_assign`),
alternative instances are registered with `_register_alt()`. The probe tries the primary instance first, then falls back
to alts for any property that raises on the primary.

Classes that require specific session state (e.g., a loaded Wavetable device, a Drum Rack with chains) remain
unreachable from a fresh empty set and are reported with `runtime_type: null`.

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

It requires a Live session with a document open (at least one track, one clip slot). The probe may create temporary
objects (clips, MIDI notes, automation envelopes, audio clips, take lanes) to reach classes that don't exist in an empty
set — these are cleaned up automatically when probing finishes. Use a fresh empty set to avoid any risk to real project
data. Properties that raise on read are skipped and reported with `runtime_type: null`. DeprecationWarnings are
suppressed during probing so deprecated properties are still captured for older Live version compatibility.

### Step 4: Device Probe

`DevicePropertyProbe` extends the probe by loading every built-in device from the browser one at a time and probing
device-specific classes that aren't reachable from a fresh empty set (e.g., `Compressor2Device`, `Eq8Device`,
`WavetableDevice`).

**Why a separate step?** `browser.load_item()` is asynchronous — devices aren't initialized until the next
`schedule_message` tick after loading. The device probe is therefore a tick-driven state machine rather than a
synchronous pass:

```
INIT → LOAD → WAIT → PROBE → LOAD → ... → CLEANUP → DONE
```

Each tick advances one state transition. MakeDoc's tick loop drives the probe, calling `tick()` once per cycle until it
returns `False`.

**What it probes per device:**

- The device class itself (e.g., `Compressor2Device.Compressor2Device`)
- The device's `.view` (e.g., `Compressor2Device.Compressor2Device.View`)
- Chains (Rack devices) → `Chain.Chain`, `ChainMixerDevice.ChainMixerDevice`
- Drum pads (Drum Rack) → `DrumPad.DrumPad`, `DrumChain.DrumChain`
- Sample (SimplerDevice) → `Sample.Sample`
- Device I/O routing → `DeviceIO.DeviceIO`

PluginDevice (third-party VST/AU) is skipped. Device classes already probed by an earlier device are also skipped —
deduplication is by Python class name, not browser item name.

**Trigger:**

```
touch /tmp/makedoc_probe_devices
```

Results are merged into the same `probe_results.json` used by the synchronous probe (steps 1-3).

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

## Running the Full Pipeline

`run_pipeline.py` orchestrates all four phases end-to-end. It triggers each in-Live phase via tmp files and polls for
completion markers before moving on.

```
python tools/run_pipeline.py                  # auto-detect version from latest build dir
python tools/run_pipeline.py --version 12.3.6
python tools/run_pipeline.py --skip-capture   # skip phase 1 (reuse existing Live.json)
```

Or via the justfile:

```
cd tools && just pipeline
cd tools && just pipeline --skip-capture
```

Each in-Live phase writes a completion marker (`/tmp/makedoc_*_done`) when finished:

| Phase        | Trigger                      | Marker                           |
| ------------ | ---------------------------- | -------------------------------- |
| Capture      | `/tmp/makedoc_reload`        | `/tmp/makedoc_capture_done`      |
| Probe        | `/tmp/makedoc_probe`         | `/tmp/makedoc_probe_done`        |
| Device probe | `/tmp/makedoc_probe_devices` | `/tmp/makedoc_device_probe_done` |

## Pipeline Structure

```
tools/
├── run_pipeline.py         Run all phases end-to-end (trigger + poll + generate)
├── install.py              Install the capture script into Live's Remote Scripts
├── generate_stubs.py       CLI for offline stub generation
├── introspection/          The MIDI Remote Script package
│   ├── __init__.py         Control Surface entry point
│   ├── MakeDoc.py          Tick loop orchestrator + trigger file polling
│   ├── generators/
│   │   ├── Generator.py            Base class (module walking, file I/O)
│   │   ├── CaptureGenerator.py     Phase 1: JSON capture output
│   │   ├── PropertyProbe.py        Phase 2 steps 1-3: synchronous property probing
│   │   ├── DevicePropertyProbe.py  Phase 2 step 4: tick-driven device probing
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

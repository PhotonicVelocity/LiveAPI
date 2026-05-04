# APICapture Pipeline

Three-stage pipeline for capturing Live API metadata and generating typed Python stubs.

```
Stage 1: Capture + Probe  (inside Live)                 → LiveTree.raw.json + LiveClasses.json
- Captures structural tree via dir() and raw docstrings, settability via fset (LiveTree.raw.json)
- Probes runtime types in a saved set, then loads devices for additional discovery (LiveClasses.json)
Stage 2: Parse & Refine   (external + decompiled + LLM) → LiveTree.resolved.json
- Parses raw capture into structured tree, merges probe results, extracts unresolved items (LiveTree.parsed.json)
- Deterministic name resolution from decompiled Remote Scripts + usage hints (refinements.callsite.json)
- LLM-guided refinement of unresolved items using tree structure, docstrings, usage hints, and M4L docs (refinements.llm.json)
Stage 3: Generate         (external)                    → stubs/<version>/Live/*.pyi
- Renders resolved tree into .pyi stubs with typed signatures, properties, enums, and listener callbacks
```

## Stage 1: Capture + Probe (runs inside Live)

`apicapture/` is a MIDI Remote Script (Control Surface) that introspects the `Live` module at runtime. It produces two
output files in `stubs/<version>/pipeline/`:

- **`LiveTree.raw.json`** — structural tree from recursive `dir()` walking, with raw Boost.Python docstrings
- **`LiveClasses.json`** — runtime property probe results (types, settability, listeners)

### Install

```
python tools/install.py
```

This copies the `apicapture` package into Ableton's MIDI Remote Scripts directory with the output path configured to
`stubs/`. After installing, start Live and select **APICapture** as a Control Surface in Preferences → Link, Tempo &
MIDI. Nothing runs automatically on startup — APICapture starts its tick loop and waits for trigger files.

### Triggers

All phases are triggered externally via files in `/tmp/`. APICapture polls for these once per tick and removes them on
consumption.

| Trigger                                | What it does                                          |
| -------------------------------------- | ----------------------------------------------------- |
| `touch /tmp/apicapture_capture`        | Raw capture — `dir()` tree dump → `LiveTree.raw.json` |
| `touch /tmp/apicapture_probe`          | Basic probe — PropertyProbe only (no device loading)  |
| `touch /tmp/apicapture_full_probe`     | Full probe — PropertyProbe + DeviceProbe              |
| `touch /tmp/apicapture_run`            | Full pipeline — capture + full probe                  |
| `echo verbose > /tmp/apicapture_probe` | Include instance data in probe output (for debugging) |

Completion markers (`/tmp/apicapture_capture_done`, `/tmp/apicapture_probe_done`) are written when each phase finishes.
They contain the build directory path so external scripts can auto-detect the version.

### Hot Reload

Scripts in `apicapture/scripts/` (CaptureModule, PropertyProbe, DeviceProbe) are reloaded via `importlib.reload()` on
every trigger, so code changes take effect immediately after reinstalling. Changes to `APICapture.py` or `__init__.py`
require a full Live restart.

### Raw Capture (`LiveTree.raw.json`)

CaptureModule walks the `Live` module recursively via `dir()`, producing a tree where each node has:

```json
{
  "name": "Song",
  "type": "class",
  "id": 140234567890,
  "repr": "<class 'Song.Song'>",
  "raw_doc": "...",
  "children": [...]
}
```

Node types include `module`, `class`, `function`, `builtin_function_or_method`, `method_descriptor`, `property`,
`getset_descriptor`, and `int` (for enum values).

**Boost.Python quirks:** Live's C++ bindings sometimes concatenate docstrings onto `__name__` (e.g.
`"StartupDialogServes as..."`) or corrupt return types by appending class docs. These are fixed in Stage 2 (parse).

### Property Probe (`LiveClasses.json`)

PropertyProbe reads live object properties to determine runtime types, settability, and listener support. It requires a
**saved set** (`sets/`) containing pre-created objects: MIDI clips with notes, automation envelopes, audio clip with warp
markers, cue points, a groove, a tuning system, a take lane, and a group track.

For each reachable class, the probe records:

- **Property types** — `type(getattr(obj, prop_name)).__name__`
- **Vector element types** — probes `value[0]` to get element type for sequence properties
- **Settability** — checks `prop.fset is not None` on the descriptor
- **Getters** — getter methods (`get_*`) used internally to reach types that aren't accessible via properties (e.g.
  `get_document` for Song, `get_all_notes_extended` for MidiNote)
- **Constructable** — whether the class can be instantiated directly (e.g. `CCFeedbackRule()`, `Base.Timer()`)

Output format:

```json
{
  "<class 'Song.Song'>": {
    "path": "Live.Song.Song",
    "complete": true,
    "constructable": false,
    "properties": {
      "tempo": { "probed": true, "type": "float" },
      "tracks": { "probed": true, "type": "list", "element_type": "Track" }
    },
    "getters": ["current_song_time", "appointed_device"]
  }
}
```

### Device Probe

DeviceProbe extends the property probe by loading every built-in device from the browser onto track 0 of the set. This
makes device-specific classes discoverable by the normal PropertyProbe loop — classes like `CompressorDevice`,
`Eq8Device`, `WavetableDevice`, and their sub-objects (chains, drum pads, samples, device I/O) that aren't reachable
from the saved set alone.

`browser.load_item()` is asynchronous — devices aren't initialized until the next `schedule_message` tick. The device
probe is therefore a tick-driven state machine:

```
LOAD → WAIT → PROBE → LOAD → ... → CLEANUP → DONE
```

Device discovery walks the browser to collect loadable items:

- **Bare devices** from `browser.instruments`, `browser.audio_effects`, `browser.midi_effects`
- **Rack presets** (`.adg`) from Rack device folders — needed to discover `Chain`/`ChainMixerDevice`
- **Drum Rack preset** from `browser.drums` — for `DrumPad`/`DrumChain`
- **Audio sample** from `browser.samples` — for `SimplerDevice` in slice mode
- **Plugin** from `browser.plugins` — first available VST/AU for `PluginDevice`

Each cycle loads one item, waits a tick for it to initialize, then discovers it — checking its type, registering it as
an instance in the probe index, and running the probe loop on the newly registered class. Classes already probed by an
earlier device are skipped. Each device is deleted after probing. Results are merged into the same `LiveClasses.json`.

### Python Compatibility

All capture modules use `from __future__ import annotations` so that modern type hint syntax works on Live 11's Python
3.7.3 runtime without raising `TypeError` at import time.

## Stage 2: Parse (runs outside Live)

The pipeline is intentionally minimal — see [doc/decisions.md "Stub Accuracy and Pipeline
Posture"](../doc/decisions.md#stub-accuracy-and-pipeline-posture) for the rationale. One script turns the raw capture
into a structured tree:

```bash
python tools/parse/parse_apicapture_results.py 12.3.6
# or, equivalently:
python tools/parse/run_parse_pipeline.py 12.3.6
```

Output: `stubs/12.3.6/pipeline/LiveTree.parsed.json`.

### parse_apicapture_results.py

Reads `LiveTree.raw.json` + `LiveClasses.json` from the pipeline directory and produces `LiveTree.parsed.json` — a
normalized, enriched tree ready for stub generation.

Transforms applied:

- **Class name fix** — splits Boost.Python's concatenated name+doc strings (e.g. `"StartupDialogServes as..."` →
  name `"StartupDialog"`, doc `"Serves as..."`)
- **Doc rewriting** — propagates class name fixes into `raw_doc` fields throughout the tree
- **Inheritance resolution** — expands base classes into ancestor chains
- **Member relocation** — moves inherited members to the class that actually defines them
- **Enum parsing** — converts string-encoded enums into structured members
- **Function doc parsing** — extracts structured `signature`, `description`, and `cpp_signature` from raw docstrings
- **Signature parsing** — splits Python/C++ signatures into matched args/returns
- **Type resolution** — resolves raw signature parts into clean structured args/returns using a C++ → Python type map
- **Probe merge** — folds `LiveClasses.json` runtime types, settability, and listeners into the tree nodes

This is the only refinement step the pipeline performs. There is no LLM resolution, no callsite analysis, no
hand-stamped overrides — only what we scrape from Live itself reaches the stubs.

## Stage 3: Generate Stubs (runs outside Live)

```
python tools/generate/generate_stubs.py 12.3.6
```

Reads `LiveTree.resolved.json` and emits `.pyi` stub files in `stubs/<version>/Live/`. The generator has no refinement
logic — it renders the tree as-is.

Output layout:

- `Live/__init__.py` — imports all namespace modules
- `Live/<Module>/<Module>.pyi` — main class (when the module has a namesake class)
- `Live/<Module>/__init__.py` — helper classes, enums, functions
- `Live/py.typed` — PEP 561 marker for type checking

Features:

- Typed method signatures with args, defaults, and return types
- `@property` with setter when `settable=true`
- `__init__` parsing from `init_doc` for constructable classes
- `TYPE_CHECKING` imports for forward references
- Enum classes with named int values
- Listener callbacks typed as `Callable`

## Directory Structure

```
tools/
├── apicapture/              The MIDI Remote Script package (Stage 0)
│   ├── __init__.py          Control Surface entry point
│   ├── APICapture.py        Tick loop orchestrator + trigger file polling
│   ├── scripts/
│   │   ├── CaptureModule.py   Raw dir() tree capture
│   │   ├── PropertyProbe.py   Synchronous property probing
│   │   └── DeviceProbe.py     Tick-driven device probing
│   └── helpers/
│       └── app.py           Version number extraction
├── parse/                   Stages 2–3: parsing, refinement, generation
│   ├── parse_apicapture_results.py   Stage 2: parse raw capture → parsed tree
│   ├── extract_unresolved.py         Stage 2: find unresolved types/names
│   ├── callsite_resolve.py           Stage 2: deterministic name resolution from decompiled scripts
│   ├── build_type_skeleton.py        Stage 2: compact API skeleton for LLM context
│   ├── llm_resolve.py               Stage 2: LLM-assisted resolution
│   ├── llm_resolve_prompt.md         System prompt for LLM resolution
│   ├── apply_refinements.py          Stage 2: apply refinements → resolved tree
│   └── generate_stubs.py            Stage 3: generate .pyi stubs
├── install.py               Install APICapture to Live's Remote Scripts
├── sets/                    Ableton Live sets used for probing
└── other/                   Legacy/utility scripts
```

## Credits

APICapture tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

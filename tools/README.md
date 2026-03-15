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

## Stage 2: Parse & Refine (runs outside Live)

Five scripts turn raw capture data into a fully resolved tree. Full pipeline for 12.3.6:

```bash
# 1. Parse raw capture into structured tree
python tools/parse/parse_apicapture_results.py 12.3.6

# 2. Extract unresolved items from parsed tree
python tools/parse/extract_unresolved.py 12.3.6

# 3. Deterministic name resolution from decompiled Remote Scripts
python tools/parse/callsite_resolve.py 12.3.6 --pretty -o stubs/12.3.6/pipeline/refinements.callsite.json

# 4. Apply callsite refinements → intermediate tree
python tools/parse/apply_refinements.py 12.3.6 \
  --refinements stubs/12.3.6/pipeline/refinements.callsite.json \
  --output stubs/12.3.6/pipeline/LiveTree.callsite_resolved.json

# 5. Re-extract remaining unresolved items from the callsite-resolved tree
python tools/parse/extract_unresolved.py 12.3.6 \
  --input stubs/12.3.6/pipeline/LiveTree.callsite_resolved.json \
  --output stubs/12.3.6/pipeline/unresolved.remaining.json

# 6. LLM-assisted resolution of remaining items
set -a && source .env && set +a && python tools/parse/llm_resolve.py 12.3.6 \
  --input stubs/12.3.6/pipeline/unresolved.remaining.json    # option A: direct API call
python tools/parse/llm_resolve.py 12.3.6 \
  --input stubs/12.3.6/pipeline/unresolved.remaining.json \
  --prepare                                                  # option B: write batch files
python tools/parse/llm_resolve.py 12.3.6 --merge             #           then merge results

# 7. Apply LLM refinements to produce the final resolved tree
python tools/parse/apply_refinements.py 12.3.6 \
  --input stubs/12.3.6/pipeline/LiveTree.callsite_resolved.json \
  --refinements stubs/12.3.6/pipeline/refinements.llm.json \
  --output stubs/12.3.6/pipeline/LiveTree.resolved.json
```

### parse_apicapture_results.py

Reads `LiveTree.raw.json` + `LiveClasses.json` from the pipeline directory and produces `LiveTree.parsed.json` — a
normalized, enriched tree ready for refinement.

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

### extract_unresolved.py

Scans `LiveTree.parsed.json` for items that need refinement:

- Function args typed `object` (unresolved types)
- Function args named `arg1`, `arg2`, etc. (unnamed parameters)
- Function returns typed `object`
- Properties with null `probed_type`

Outputs `unresolved.json` keyed by path, with full context for each item (kind, signature, description, C++ signature).
The structure mirrors `refinements.llm.json` so the LLM can add resolved fields directly.

### callsite_resolve.py

Deterministic resolution by analysing decompiled Ableton Remote Scripts
([gluon/AbletonLive12_MIDIRemoteScripts](https://github.com/gluon/AbletonLive12_MIDIRemoteScripts)). The repo is
auto-cloned on first run into `doc/decompiled/` (shallow clone, ~50 MB, gitignored).

Searches 1200+ decompiled `.py` files for:

1. **Function definitions** — `def func_name(self, param1, param2)` gives parameter names directly. When multiple
   definitions exist, names are voted on per position.
2. **Call sites** — `obj.func_name(value)` gives variable names callers use, collected as hints for the LLM phase.
3. **Type usage context** — code snippets showing how members with unresolved types are used in practice.

For methods with common names (`append`, `extend`, etc.), the parent object at the call site is compared against the
class name to avoid cross-class contamination.

Outputs JSON with three sections:

- `refinements` — high-confidence names from definition analysis (applied directly)
- `call_site_hints` — per-arg vote tallies from call sites (context for LLM phase)
- `type_hints` — usage context snippets for items needing type resolution

### build_type_skeleton.py

Builds a compact text skeleton of the full API from `LiveTree.parsed.json` — all modules, classes, enums (with values),
and properties (with probed types). Functions are omitted since they're already present on the unresolved items. Used as
LLM context for type resolution; can also be run standalone to inspect the tree structure.

### llm_resolve.py

Produces `refinements.llm.json` using Claude to resolve remaining unresolved items. Sends unresolved items along with
the type skeleton, call-site hints, MaxForLive docs, and curated per-class reference docs (`reference/`) as context. The
system prompt is in `llm_resolve_prompt.md`.

Three modes:

- **`--prepare`** — splits items into batches grouped by module, writes batch files to
  `stubs/<version>/pipeline/batches/` for processing via the Agent tool (no API key needed)
- **`--merge`** — merges batch result files into a single `refinements.llm.json`
- **(default)** — calls the Anthropic API directly (requires `ANTHROPIC_API_KEY`)

### apply_refinements.py

Applies `refinements.llm.json` to `LiveTree.parsed.json`, producing `LiveTree.resolved.json` with all arg names, arg
types, return types, and property types baked in. The resolved tree is the final input to stub generation.

## Stage 3: Generate Stubs (runs outside Live)

```
python tools/parse/generate_stubs.py 12.3.6
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

# APICapture Pipeline

Three-stage pipeline for capturing Live API metadata and generating typed Python stubs.

```
Stage 1: Capture + Probe  (inside Live)        → LiveTree.raw.json + LiveClasses.json
- Captures structural tree via dir() and raw docstrings, settability via fset (LiveTree.raw.json)
- Probes runtime types in a saved set, then loads devices for additional discovery (LiveClasses.json)
Stage 2: Parse + markdown seed (external)      → LiveTree.parsed.json + probe/<v>/seed/*.md
- Parses raw capture into a structured tree (LiveTree.parsed.json)
- Builds the per-module markdown seed under probe/<v>/seed/, applying algorithmic
  decisions (type qualification, optional widening, enum widening, listener-triplet folding,
  parametric-container detection)
Stage 3: Generate         (external)           → stubs/<version>/Live/*.pyi
- Reads content/<v>/modules/*.md (the curated SOT — seed + sibling <field>_override: blocks)
  and emits .pyi stubs. The override mechanism is the seam through which manual refinements
  reach the rendered output.
```

## Stage 1: Capture + Probe (runs inside Live)

`apicapture/` is a MIDI Remote Script (Control Surface) that introspects the `Live` module at runtime. It produces two
output files in `probe/<version>/pipeline/`:

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

Submodules (`Live.Application`, `Live.Licensing`, `Live.Song`, etc.) are also indexed and probed — the module instance
is the seed and any top-level `get_*()` functions are called as no-arg getters. Output entries for modules carry
`is_module: true` and live alongside class entries in the same dict, keyed by `<module 'Foo'>`.

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
  },
  "<module 'Licensing'>": {
    "path": "/Live/Licensing",
    "is_module": true,
    "complete": true,
    "properties": {},
    "getters": {
      "get_unlock_dir": {
        "probed": true,
        "type": "tuple",
        "element_reprs": ["<class 'str'>", "<class 'bool'>"]
      }
    }
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

All capture modules use `from __future__ import annotations` so that modern type hint syntax works on
older Live runtimes (e.g. Live 11's Python 3.7.3) without raising `TypeError` at import time. Active
publishing tracks Live 12.x only, but the apicapture pipeline still runs against 11.x via
`tools/sets/Set 11 Project/`.

## Stage 2: Parse + markdown seed (runs outside Live)

The pipeline is intentionally minimal — see [doc/decisions.md "Stub Accuracy and Pipeline
Posture"](../doc/decisions.md#stub-accuracy-and-pipeline-posture) for the rationale. Two scripts: parse the raw capture
into a structured tree, then build a per-module markdown seed that captures every algorithmic decision before any human
override.

```bash
python tools/parse/run_parse_pipeline.py 12.3.6
# Equivalent to:
#   python tools/parse/parse_apicapture_results.py 12.3.6
#   python tools/parse/build_lom_md.py 12.3.6
```

Output: `probe/12.3.6/pipeline/LiveTree.parsed.json` (parsed tree) and
`probe/12.3.6/seed/<Module>.md` (per-module markdown seed — the algorithmic baseline for each module).

The curated SOT lives in `content/12.3.6/modules/<Module>.md`. It started as a copy of `seed/` and now carries
sibling `<field>_override:` blocks (inside the fenced YAML for each member) where humans have tightened types, renamed
args, or qualified iterable element types. `seed/` regenerates freely on each Stage 2 run; `modules/` is only resynced
from `seed/` at intentional checkpoints (no automatic flow). Diff `seed/` against `modules/` to see exactly which facts
have been hand-touched.

### parse_apicapture_results.py

Reads `LiveTree.raw.json` from the pipeline directory and produces `LiveTree.parsed.json` — a normalized,
enriched tree. Probe data (`LiveClasses.json`) is currently not consumed by v2; the parser is raw_doc-driven.

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

### build_lom_md.py

Reads `LiveTree.parsed.json` and emits one markdown file per top-level Live module under `probe/<v>/seed/`.
Internally it builds a per-module dict and serializes via `md_emit.convert()` — the same emitter used at intentional
sync points to refresh the curated SOT. Algorithmic decisions live here — anything a human shouldn't have to make
explicit:

- Type qualification (`Track` → `Live.Track.Track`)
- Optional widening (`T` + `default=None` → `T | None`)
- Enum widening (`E` → `E | int` — Boost.Python emits enums as int subclasses)
- Enum-from-default inference (bare `int` arg with default `Module.Enum.member` → `Enum | int`)
- Listener-triplet folding (`add_*_listener`/`remove_*_listener`/`*_has_listener` collapsed under the property)
- Parametric-container detection (Generic[T] for the abstract `Live.Base.Vector`)

Format spec: [doc/lom-format.md](../doc/lom-format.md). The override pattern (`<field>_override:` siblings inside each
member's fenced YAML) is what the curated `modules/` layer adds on top of the seed.

## Stage 3: Generate Stubs (runs outside Live)

```
python tools/generate/generate_stubs.py 12.3.6
```

Reads `content/<v>/modules/*.md` and emits `.pyi` stub files in `stubs/<version>/Live/`. The generator is mechanical —
it picks `<field>_override.value` when present, else falls back to the parser-derived field. No type inference,
no narrowing decisions. Renders what the markdown says.

Output layout (flat, mirroring the real `Live` C extension module):

- `Live/__init__.pyi` — imports all submodules
- `Live/<Module>.pyi` — one file per submodule, containing main class + helper classes/enums/functions
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
├── parse/                   Stage 2: parser + LOM markdown seed builder
│   ├── parse_apicapture_results.py   Parse raw capture → LiveTree.parsed.json
│   ├── build_lom_md.py                  Build per-module markdown seed → probe/<v>/seed/*.md
│   ├── md_emit.py                       Markdown emitter (used by build_lom_md and one-off conversion)
│   ├── parse_module_md.py               Markdown parser + legacy-shape adapter (consumed by generators)
│   └── run_parse_pipeline.py            Orchestrator (parse + build)
├── generate/                Stage 3: stub + reference generation
│   ├── generate_stubs.py         Read content/<v>/modules/*.md → emit .pyi
│   └── generate_reference.py     Read content/<v>/modules/*.md → emit Starlight MDX
├── verify/                  Verification — pyright audit + corpus consistency checks
│   ├── run.sh                        Orchestrator (Tiers 1-4)
│   ├── parse_check.py                Tier 1: ast.parse over every .pyi
│   ├── audit_corpus.py               Offline pyright audit over external/corpus
│   ├── audit_ignores.yaml            Investigated-and-declined audit findings
│   ├── audit_pyrightconfig.json      Pyright config used by audit_corpus.py
│   └── README.md                     Tier definitions and how to run locally
├── fetch_external/          External-source bootstrap (outputs to external/, gitignored)
│   ├── corpus.py                     Clone gluon corpus at CORPUS_PIN → external/corpus/
│   ├── m4l_docs.py                   Scrape Max for Live LOM docs → external/max-for-live-docs/
│   ├── release_notes.py              Scrape Live release notes → external/release-notes/
│   ├── check_pin.py                  Validate pin references match corpus.py
│   └── bootstrap.sh                  First-time setup orchestrator
├── publish/                 PyPI release tooling
│   └── build_package.py              Build the ableton-live-stubs wheel + sdist
├── run_pipeline.py          Full Stage 1 + 2 + 3 orchestrator (capture → parse → generate)
├── install.py               Install APICapture to Live's Remote Scripts
├── sets/                    Ableton Live sets used for probing
└── other/                   Misc utilities (quit_live, swap_live, watch)
```

## Credits

APICapture tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

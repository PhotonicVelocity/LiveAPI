# Tooling

Three-stage pipeline for capturing Live API metadata and rendering it as typed Python stubs + the Starlight reference
site.

```
Stage 1: Capture + Probe  (inside Live)   → LiveTree.raw.json + LiveClasses.json
- Captures structural tree via dir() and raw docstrings, settability via fset (LiveTree.raw.json)
- Probes runtime types in a saved set, then loads devices for additional discovery (LiveClasses.json)
Stage 2: Parse + markdown seed (offline)  → LiveTree.parsed.json + probe/<v>/seed/*.md
- Parses raw capture into a structured tree (LiveTree.parsed.json)
- Builds the per-module markdown seed under probe/<v>/seed/, applying algorithmic
  decisions (type qualification, optional widening, enum widening, listener-triplet folding,
  parametric-container detection)
Stage 3: Generate         (offline)       → stubs/<v>/Live/*.pyi + web/src/content/docs/**/*.mdx
- Reads content/<v>/modules/*.md (the curated SOT — algorithmic seed plus per-member
  `refinement:` blocks with confidence + sources).
- generate_stubs.py emits the typed .pyi package.
- generate_reference.py emits the Starlight MDX pages.
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
`probe/<version>/pipeline/`. After installing, start Live and select **APICapture** as a Control Surface in Preferences
→ Link, Tempo & MIDI. Nothing runs automatically on startup — APICapture starts its tick loop and waits for trigger
files.

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
**saved set** (`sets/`) containing pre-created objects: MIDI clips with notes, automation envelopes, audio clip with
warp markers, cue points, a groove, a tuning system, a take lane, and a group track.

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

All capture modules use `from __future__ import annotations` so that modern type hint syntax works on older Live
runtimes (e.g. Live 11's Python 3.7.3) without raising `TypeError` at import time. Active publishing tracks Live 12.x
only, but the apicapture pipeline still runs against 11.x via `tools/sets/Set 11 Project/`.

## Stage 2: Parse + markdown seed (runs outside Live)

The pipeline is intentionally minimal — see
[doc/decisions.md "Stub Accuracy and Pipeline Posture"](../doc/decisions.md#stub-accuracy-and-pipeline-posture) for the
rationale. Two scripts: parse the raw capture into a structured tree, then build a per-module markdown seed that
captures every algorithmic decision before any human override.

```bash
python tools/parse/run_parse_pipeline.py 12.3.6
# Equivalent to:
#   python tools/parse/parse_apicapture_results.py 12.3.6
#   python tools/parse/build_lom_md.py 12.3.6
```

Output: `probe/12.3.6/pipeline/LiveTree.parsed.json` (parsed tree) and `probe/12.3.6/seed/<Module>.md` (per-module
markdown seed — the algorithmic baseline for each module).

The curated SOT lives in `content/12.3.6/modules/<Module>.md` (plus the foundation pages flat at `content/12.3.6/`). It
started as a copy of `seed/` and now carries per-member `refinement:` blocks where humans have tightened a probed value
(a type, an element type, an arg name) with `confidence` + cited `sources`. Format spec:
[`doc/lom-format.md`](../doc/lom-format.md). `seed/` regenerates freely on each Stage 2 run; `content/` is only resynced
from `seed/` at intentional checkpoints (no automatic flow). `diff probe/<v>/seed/ content/<v>/modules/` shows exactly
which facts have been hand-touched.

### parse_apicapture_results.py

Reads `LiveTree.raw.json` from the pipeline directory and produces `LiveTree.parsed.json` — a normalized, enriched tree.
Probe data (`LiveClasses.json`) is folded in by `build_lom_md.py` in the next step; this script is purely
raw_doc-driven.

Transforms applied:

- **Class name fix** — splits Boost.Python's concatenated name+doc strings (e.g. `"StartupDialogServes as..."` → name
  `"StartupDialog"`, doc `"Serves as..."`)
- **Doc rewriting** — propagates class name fixes into `raw_doc` fields throughout the tree
- **Inheritance resolution** — expands base classes into ancestor chains
- **Member relocation** — moves inherited members to the class that actually defines them
- **Enum parsing** — converts string-encoded enums into structured members
- **Function doc parsing** — extracts structured `signature`, `description`, and `cpp_signature` from raw docstrings
- **Signature parsing** — splits Python/C++ signatures into matched args/returns
- **Type resolution** — resolves raw signature parts into clean structured args/returns using a C++ → Python type map

### build_lom_md.py

Reads `LiveTree.parsed.json` and emits one markdown file per top-level Live module under `probe/<v>/seed/`. Internally
it builds a per-module dict and serializes via `md_emit.convert()` — the same emitter used at intentional sync points to
refresh the curated SOT. Algorithmic decisions live here — anything a human shouldn't have to make explicit:

- Type qualification (`Track` → `Live.Track.Track`)
- Optional widening (`T` + `default=None` → `T | None`)
- Enum widening (`E` → `E | int` — Boost.Python emits enums as int subclasses)
- Enum-from-default inference (bare `int` arg with default `Module.Enum.member` → `Enum | int`)
- Listener-triplet folding (`add_*_listener`/`remove_*_listener`/`*_has_listener` collapsed under the property)
- Parametric-container detection (Generic[T] for the abstract `Live.Base.Vector`)

Format spec: [doc/lom-format.md](../doc/lom-format.md). The `refinement:` block inside each member's fenced YAML is what
the curated `content/<v>/modules/` layer adds on top of the seed.

## Stage 3: Generate stubs + reference (runs outside Live)

Two generators, one input. Both read `content/<v>/modules/*.md` directly (via `parse_module_md` + the small
`regraft_hoisted` helper that nests hoisted children under their parent class). When a member has a `refinement:` block,
the resolved value lives at the top level of the member's YAML and the `refinement.<key>.probed` / `confidence` /
`sources` carry the diagnostic; both generators read the resolved value directly and surface the refinement metadata
where appropriate.

### generate_stubs.py

```
python tools/generate/generate_stubs.py 12.3.6
```

Reads `content/<v>/modules/*.md` and emits `.pyi` stub files in `stubs/<v>/Live/`. The generator is mechanical: no type
inference, no narrowing decisions. Renders what the markdown says.

Output layout (flat, mirroring the real `Live` C extension module):

- `Live/__init__.pyi` — imports all submodules
- `Live/<Module>.pyi` — one file per submodule, containing main class + helper classes/enums/functions
- `Live/py.typed` — PEP 561 marker for type checking

Features:

- Typed method signatures with args, defaults, and return types (`self` injected at args-render time)
- `@property` with setter when `settable=true`
- `__init__` parsing from `init_doc` for constructable classes
- `TYPE_CHECKING` imports for forward references
- Enum classes with named int values
- Listener triplet expansion (from `listenable: true` shorthand) at render time
- `Callable`-typed listener registration methods

### generate_reference.py

```
python tools/generate/generate_reference.py 12.3.6
```

Reads `content/<v>/modules/*.md` (per-module) and `content/<v>/*.md` (flat foundation pages) and emits Starlight MDX
under `web/src/content/docs/`. Renders:

- One MDX per per-module class group (41 today); LomObject and Listener are absorbed by their foundation pages.
- Four foundation MDX pages (`live-object-model.mdx`, `listeners.mdx`, `calling-conventions.mdx`, `remote-scripts.mdx`).
- Per-class signatures with linkified types, properties + methods tables, inherited members box, "Returned by"
  cross-references, refinement footnote markers (`*`) with tooltip (confidence chip + probed-as + tagged evidence
  bullets), and source-of-body footnote markers (`ⓘ`) revealing the runtime docstring on hover.

Both generators consume the same dict shape that `parse_module_md` produces — no intermediate "legacy" adapter (see
`doc/dataflow.md` for the full Stage 1 → Stage 4 flow).

## Workflow + CI gates

The repo treats `content/<v>/modules/*.md` (plus the foundation pages) as the source of truth and the `.pyi` stubs +
`.mdx` reference pages as **committed-but-regenerated** artifacts. Whenever you change something upstream of those
artifacts, regenerate locally and commit the regenerated outputs in the same commit as the change that caused them.

```bash
# 1. Make your change to the SOT or a generator.
#    Examples: edit content/12.3.6/modules/Track.md, or edit
#              tools/generate/generate_stubs.py.

# 2. Regenerate the downstream artifacts.
python tools/generate/generate_stubs.py 12.3.6
python tools/generate/generate_reference.py 12.3.6

# 3. Stage the change AND the regenerated outputs together.
git add content/ tools/ stubs/12.3.6/Live/ web/src/content/docs/
git commit -m "..."
git push
```

If you forget step 2, CI catches it. **`regen-check`** runs both generators on the committed SOT and `git diff`s the
result against the committed `stubs/<v>/Live/` and `web/src/content/docs/`. Any drift fails the workflow with the exact
`diff --stat` so you can see what's out of sync.

### CI workflows in effect

| Workflow          | Triggers on                                                                 | What it checks                                                                                                                      |
| ----------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `regen-check`     | Pushes / PRs touching `content/`, `tools/parse                              | generate/`, `stubs/`, `web/src/content/docs/`                                                                                       | Regenerated outputs match committed outputs (no drift) |
| `web-build-check` | Every push to main and every PR                                             | Astro build succeeds — catches MDX parse errors before merge                                                                        |
| `verify-stubs`    | Pushes / PRs touching `stubs/`, `content/`, `tools/verify/`, `tests/usage/` | `validate_content.py` (SOT schema + inline footnote links) + Tier 1 (ast.parse) + Tier 2 (pyright, tracking) + Tier 4 (usage tests) |
| `deploy-site`     | Push to main touching `web/`                                                | Rebuilds + deploys the GitHub Pages site                                                                                            |
| `release`         | Push to main touching `stubs/12.*/Live/`                                    | Builds and publishes the PyPI wheel for the changed Live version                                                                    |

`web-build-check` is the **required status check** for branch protection. PRs can't be merged via the UI until it
passes. The other workflows fail visibly but don't block merge — they're tracking signals.

### Branch protections in effect on `main`

- **Force-push blocked** — including for admins. Catches accidents like `git push --force` on the wrong branch.
- **Deletion blocked** — main can't be deleted.
- **`web-build-check` must pass for PR merges** — admins can override via the "merge without waiting for requirements"
  button, but the override is a deliberate click.

Direct pushes to main by admins still work; CI runs after the push and fails visibly on drift / build / verify problems,
but doesn't auto-revert. If you push a bad commit directly, push a fix or revert it yourself. The site won't redeploy
because `deploy-site`'s build job uses the same `npm run build` that `web-build-check` runs — a build that's broken on
main won't reach Pages either.

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
│   ├── parse_module_md.py               Markdown parser + regraft_hoisted helper (consumed by generators)
│   └── run_parse_pipeline.py            Orchestrator (parse + build)
├── generate/                Stage 3: stub + reference generation
│   ├── generate_stubs.py         Read content/<v>/modules/*.md → emit .pyi
│   └── generate_reference.py     Read content/<v>/modules/*.md → emit Starlight MDX
├── verify/                  Verification — content schema + pyright audit + corpus consistency
│   ├── run.sh                        Orchestrator (content + Tiers 1-4)
│   ├── validate_content.py           Content schema + inline-footnote link integrity
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

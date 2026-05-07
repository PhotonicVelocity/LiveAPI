# LiveAPI

Comprehensive reference for the Ableton Live Python API — classes, properties, methods, enums, and behavioral notes
that Ableton doesn't publicly document.

This branch ships the **typed Python stubs**. A browsable HTML reference site (the second planned product) is in
work on the [`reference-doc-generator-wip`](https://github.com/PhotonicVelocity/LiveAPI/tree/reference-doc-generator-wip)
branch — generator architecture is being reworked to consume the parsed/refined tree directly instead of
re-parsing the stubs, and is not currently published.

## Typed Python Stubs

**Who it's for.** Anyone writing Python that talks to Live's runtime API and wants autocomplete + static type
checking — most commonly Control Surface / Remote Script developers, but also tooling that wraps the API (RPC
bridges, code generators, test harnesses).

Pre-built `.pyi` modules for the latest tracked Live version live at [`stubs/12.3.6/Live/`](stubs/12.3.6/Live/) —
typed inventory of every reachable class, property, method, and enum.

### Setup

**Published — recommended.** Install via pip; pyright and mypy auto-discover the stubs (PEP 561 stub-only package
convention). No config needed.

```bash
pip install ableton-live-stubs
```

Each release pins a specific Live version.

**From this repo — bleeding-edge or contributing.** Point the type checker's stub path at the version directory:

```jsonc
// pyrightconfig.json
{
  "stubPath": "path/to/LiveAPI/stubs/12.3.6",
}
```

The package includes a `py.typed` marker so any PEP 561-aware tool picks it up.

### Usage

```python
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import Live
    from Live.Song import Song

def on_tempo_changed(song: Song) -> None:
    app: Live.Application.Application = Live.Application.get_application()
    print(f"Live {app.get_major_version()}: tempo is now {song.tempo}")
```

### Limitations & caveats

The stubs are best-effort. Live's Python API is a Boost.Python binding with no published reference, so the pipeline
draws from runtime introspection plus a handful of cross-referenced sources (Max for Live docs, decompiled Remote
Scripts). Some of that has slack in it — read the stubs as "Ableton's most likely intent" rather than a contract.

#### Posture decisions

- **Names are decorative.** All callables emit PEP 570 positional-only markers (`, /`), so type-checkers won't
  accept kwarg calls (`song.create_scene(index=0)` fails). Names show in autocomplete + hover but never as kwargs.
- **Types are conservative.** Args without a pinned-down type stay as `object` rather than getting a guess. A
  wrong-but-pretty type that lets pyright accept a runtime-crashing call is worse than a vague-but-honest one —
  especially for Boost.Python's native-Vector args.
- **Refinements over reality, not prettiness.** Hand-curated overrides live as sibling `<field>_override:` blocks
  next to the parser-derived value in [`stubs/<v>/lom/*.yaml`](stubs/12.3.6/lom/). They are only used to correct known
  wrongness (every override carries a `source:` field with concrete evidence) and never invent narrowings the binding
  doesn't actually accept.
- **Docstrings are runtime-relayed, not authored.** All docstring text comes from Live's runtime Boost.Python
  `__doc__` strings — captured during the `dir()` walk and emitted into the stub mostly verbatim (the parser strips
  the auto-generated signature header and `C++ signature :` footer for functions, but doesn't rewrite the prose).
  They have Boost-style quirks (lowercase prose, run-on sentences, occasional stray formatting) and don't reflect
  refinements (a re-typed arg's docstring still describes whatever Live's runtime says). A cleanup pass to polish
  them is on the roadmap.

#### Validation

Every change to the stubs runs through four CI gates ([`.github/workflows/verify-stubs.yml`](.github/workflows/verify-stubs.yml)):

- **Tier 1 — `ast.parse`.** All 44 `.pyi` files parse as valid Python. Hard gate.
- **Tier 2 — pyright self-check.** Stubs internally consistent (no broken references, no Liskov violations on
  overrides, no cyclic imports). Currently 0 errors. Tracking-only by default; promotable to a hard gate via
  `--strict`.
- **Tier 3 — pyright `--verifytypes`.** PEP 561 type completeness score. Currently 99.9% (2728 public symbols,
  2725 known, 3 unknown). Tracking-only — surfaced in the CI job summary, promotable to hard gate via `--strict`
  (100% required).
- **Tier 4 — usage tests.** Hand-picked patterns from Ableton's own shipped Remote Scripts (pinned to a specific
  commit of [gluon/AbletonLive12_MIDIRemoteScripts](https://github.com/gluon/AbletonLive12_MIDIRemoteScripts)) — the
  stubs must accept what Ableton's engineers wrote and shipped. Hard gate.

In addition, an offline corpus audit ([`tools/verify/audit_corpus.py`](tools/verify/audit_corpus.py)) runs pyright
over the entire decompiled corpus against the stubs to surface places where the stubs disagree with working
production code. Not a CI gate; used during refinement work.

#### Known weak spots

The stubs ship with a small set of items typed on weaker evidence:

| Area                                                                          | Current type                                                           | Why it's weak                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Live.Licensing.PythonLicensingBridge.*` (5 properties + 3 method signatures) | Inferred from `raw_doc` and naming patterns.                           | The class is M4L-only and can't be instantiated from a Control Surface — unreachable to the probe. Needs an M4L probe device.                                                                                       |
| `Live.Listener.ListenerHandle.{listener_func, listener_self, name}`           | Inferred from `raw_doc`.                                               | The class is internal — every `add_*_listener` returns `None` (367 of them), the class can't be instantiated from Python, and no Live property exposes a `ListenerVector`. Not actionable without an internal hook. |
| `Live.Application.ControlSurfaceProxy.{pad_layout, type_name}`                | M4L docs say `pad_layout` is a string; `type_name` inferred from name. | M4L-only class, same situation as Licensing.                                                                                                                                                                        |
| `map_midi_*_with_feedback_map` `feedback_rule` arg                            | Strictly typed (no `\| None`).                                         | The corpus never passes literal `None`, but the binding _might_ accept it. Currently strict; would be widened if a probe confirms it.                                                                               |
| `Live.MidiMap.PitchBendFeedbackRule.value_pair_map`                           | `tuple[tuple, ...]` — outer concrete, inner unparameterized.           | Sister `cc_value_map` / `vel_map` are `tuple[int, ...]`; pitch-bend value pairs likely `tuple[int, int]`, but no corpus literal and no M4L doc confirms the inner shape. Refining without evidence is forbidden.    |

#### `class Track(DeviceContainer):` — a Boost.Python quirk

Track and Chain show as inheriting from a `DeviceContainer` class that you'll never see referenced in any
Live runtime code, the M4L docs, or Ableton's own decompiled Remote Scripts. The class technically exists
— Live's Python truly registers it as a base of Track and Chain, and `isinstance(some_track,
Live.Track.DeviceContainer)` returns True at runtime — but it's a Boost.Python implementation artifact
rather than a real LOM type.

Mechanically: Live's C++ source binds Track and Chain through Boost.Python's `class_<TTrack,
bases<TDeviceContainer>>("Track")` form. Boost honors `bases<>` by registering DeviceContainer as a real
Python superclass (`__bases__`, `__mro__`, `isinstance()` all work), but it binds the actual methods on
each concrete subclass independently — so `dir(DeviceContainer)` returns essentially nothing while
`dir(Track)` and `dir(Chain)` each show the full shared interface (`devices`, `name`, `mute`,
`insert_device`, etc.). The shared C++ implementation gets two independent Python descriptors with
different docstrings — Track's say "Track", Chain's say "Chain", and a few of Chain's are even slightly
wrong (e.g. `Chain.color`'s docstring describes the color *index* even though the property is the RGB
color).

We render the `(DeviceContainer)` base because it's a runtime fact — pyright needs the inheritance to
type-check `isinstance` patterns honestly. But it's not how anyone actually uses the API; Ableton's
Push2 corpus, when it wants to "is this a thing with devices?", explicitly checks `isinstance(c,
(Live.Track.Track, Live.Chain.Chain))` rather than against the common base.

## First-time setup (contributors)

Two external sources need to be on disk before the pipeline + verify suite work: the decompiled Remote Scripts
corpus (used by Tier 4 usage tests + the offline audit) and the Max for Live LOM docs (cited by
`<field>_override.source` blocks in `stubs/<v>/lom/*.yaml`).

```bash
tools/fetch_external/bootstrap.sh           # corpus + M4L 9.0
tools/fetch_external/bootstrap.sh --all     # also M4L 8.0 (legacy) + release notes
```

Both targets are gitignored. The corpus is pinned to a specific commit in
[`tools/fetch_external/corpus.py`](tools/fetch_external/corpus.py) (`CORPUS_PIN`); `tools/fetch_external/check_pin.py`
validates that every reference (test docstrings, README) matches.

See [`tools/README.md`](tools/README.md) for the full pipeline (capture → parse → generate).

## Project structure

```
stubs/         Typed .pyi modules for the latest tracked Live version
reference/     Per-class API docs generated from the stubs (mkdocs-published)
tools/         APICapture + parse + generate pipeline (see tools/README.md)
external/      Auto-fetched sources (corpus, M4L docs, release notes) — gitignored
```

## Sources

The pipeline draws from four sources, in roughly increasing order of authority:

1. **Runtime introspection** (APICapture) — class/method/property inventory captured by `dir()` walking and
   property probing inside Live. The base structure of every stub.
2. **Max for Live docs** ([`external/max-for-live-docs/`](external/max-for-live-docs/)) — richer descriptions and parameter
   names; partial API coverage.
3. **Decompiled Remote Scripts** (corpus) — Ableton's own shipped Python code provides ground truth for
   parameter names and call shapes. Cloned to `external/corpus/`.
4. **`stubs/<v>/lom/*.yaml` overrides** — hand-curated `<field>_override:` blocks sitting next to each
   parser-derived value, with a per-override `source:` field documenting the rationale (corpus def-site, M4L doc
   citation, raw_doc, etc.). Consumed mechanically by `generate_stubs.py`.

## Credits

APICapture tooling forked from [isfopo/LiveAPI_MakeDoc](https://github.com/isfopo/LiveAPI_MakeDoc) (itself a fork of
[NSUSpray/LiveAPI_MakeDoc](https://github.com/NSUSpray/LiveAPI_MakeDoc)). Stub generation based on
[cylab/AbletonLive-API-Stub](https://github.com/cylab/AbletonLive-API-Stub).

## Disclaimer

This is unofficial documentation for the Ableton Live API. These files are provided as-is, without any warranty. Do not
contact Ableton with questions about this project.

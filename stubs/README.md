# Stubs

Typed Python stubs for the Ableton Live API.

```
12.3.6/
├── Live/        # tracked .pyi modules — the published output
└── pipeline/    # gitignored intermediates from the generation pipeline
```

Currently shipping a single Live version (12.3.6); older versions can be rebuilt
from a tagged commit if needed.

## How These Are Generated

See [`tools/README.md`](../tools/README.md) for the full pipeline. In short:

1. **APICapture** (inside Live) — captures the raw API tree and probes runtime types
2. **`run_parse_pipeline.py`** (external) — parses + applies hand-curated refinements from `manual_refinements.yaml`
3. **`generate_stubs.py`** (external) — emits `.pyi` files from the parsed tree

## Usage

Add `stubs/12.3.6/Live/` to your type checker's search path for autocomplete and
static analysis. The stubs include a `py.typed` marker for PEP 561 compatibility.

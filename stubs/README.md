# Stubs

Typed Python stubs for the Ableton Live API, organized by Live version.

Each version directory contains:

- `Live/` — typed `.pyi` stub modules (the tracked output)
- `pipeline/` — gitignored intermediates from the generation pipeline

## How These Are Generated

See `tools/README.md` for the full four-stage pipeline. In short:

1. APICapture (inside Live) captures the raw API tree and probes runtime types
2. `parse_apicapture_results.py` normalizes and enriches the tree
3. `llm_resolve.py` resolves unresolved types and parameter names
4. `generate_stubs.py` emits `.pyi` files from the resolved tree

## Usage

Add the relevant `stubs/<version>/Live/` directory to your type checker's search path for autocomplete and static
analysis. The stubs include a `py.typed` marker for PEP 561 compatibility.

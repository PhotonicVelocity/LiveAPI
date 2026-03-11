# Build Output

Auto-generated API stubs and capture data, organized by Live version.

Each version directory contains:

- `Live.json` — captured API metadata (classes, methods, properties, docstrings)
- `Live/` — typed Python stub modules generated from the capture

## How These Are Generated

The APICapture Control Surface in `tools/apicapture/` runs inside Ableton Live and dumps the API surface for the running
version. See `tools/install.py` to install the script, then select it as a Control Surface in Live's preferences.

## Purpose

These are source material for writing the curated reference docs in `reference/`. They provide a complete inventory of
classes, methods, and properties but have sparse docstrings and weak types — the reference docs fill those gaps with
descriptions and behavioral notes from Max for Live docs and direct probing.

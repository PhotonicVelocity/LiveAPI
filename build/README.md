# Build Output

Auto-generated API stubs and XML dumps, organized by Live version (11.0 through 12.3.5).

Each version directory contains:

- `Live/` — Python stub modules for every Live API class
- `Live.xml` — XML dump of the full API surface

## How These Are Generated

The introspection Control Surface in `tools/introspection/` runs inside Ableton Live and dumps the API surface for the
running version. See `tools/install.py` to install the script, then select it as a Control Surface in Live's preferences.

## Purpose

These are source material for writing the curated reference docs in `reference/`. They provide a complete inventory of
classes, methods, and properties but have sparse docstrings and weak types — the reference docs fill those gaps with
descriptions and behavioral notes from Max for Live docs and direct probing.

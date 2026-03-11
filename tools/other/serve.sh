#!/usr/bin/env bash
# Kill any existing mkdocs server on port 8123 and restart
set -e
lsof -ti:8123 | xargs kill 2>/dev/null || true
cd "$(dirname "$0")/.."
~/.local/bin/mkdocs serve -a localhost:8123

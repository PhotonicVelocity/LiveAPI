#!/usr/bin/env bash
# First-time setup — fetch all external sources the project depends on.
#
# Run once after cloning the repo. Skips work if dirs already exist; pass
# --force to re-fetch from scratch.
#
# Usage:
#   tools/fetch_external/bootstrap.sh           # fetch corpus + M4L 9.0 docs
#   tools/fetch_external/bootstrap.sh --all     # also fetch M4L 8.0 (legacy) + release notes
#   tools/fetch_external/bootstrap.sh --force   # re-fetch everything fresh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

ALL=0
FORCE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --all)   ALL=1; shift ;;
    --force) FORCE=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

force_flag=""
[[ "$FORCE" == "1" ]] && force_flag="--force"

echo "=== Decompiled Remote Scripts corpus ==="
python3 tools/fetch_external/corpus.py $force_flag
echo

echo "=== Max for Live docs (9.0) ==="
if [[ "$FORCE" == "1" ]] || [[ ! -d external/max-for-live-docs/9.0 ]]; then
  python3 tools/fetch_external/m4l_docs.py
else
  echo "Already present at external/max-for-live-docs/9.0/ (pass --force to refetch)"
fi
echo

if [[ "$ALL" == "1" ]]; then
  echo "=== Max for Live docs (8.0 legacy) ==="
  if [[ "$FORCE" == "1" ]] || [[ ! -d external/max-for-live-docs/8.0 ]]; then
    python3 tools/fetch_external/m4l_docs.py --legacy
  else
    echo "Already present (pass --force to refetch)"
  fi
  echo

  echo "=== Live release notes ==="
  if [[ "$FORCE" == "1" ]] || [[ ! -d external/release-notes ]] || [[ -z "$(ls -A external/release-notes 2>/dev/null)" ]]; then
    python3 tools/fetch_external/release_notes.py
  else
    echo "Already present at external/release-notes/ (pass --force to refetch)"
  fi
  echo
fi

echo "Bootstrap complete."

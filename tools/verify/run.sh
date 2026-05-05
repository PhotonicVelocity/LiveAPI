#!/usr/bin/env bash
# Local verification orchestrator. Mirrors what CI runs.
#
# Tier 1 (ast.parse) and Tier 4 (usage tests) are hard gates; Tier 2 (stubs internal
# consistency) is tracking-only during cleanup — see tools/verify/README.md.
#
# Usage:
#   tools/verify/run.sh
#   tools/verify/run.sh --version 12.3.6
#   tools/verify/run.sh --strict      # also fail on Tier 2 errors

set -uo pipefail

VERSION="12.3.6"
STRICT=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --version) VERSION="$2"; shift 2 ;;
    --strict)  STRICT=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

OVERALL=0

echo "=== Corpus pin consistency ==="
python3 tools/fetch/check_pin.py || OVERALL=1
echo

echo "=== Tier 1: ast.parse on stubs/$VERSION/Live ==="
python3 tools/verify/parse_check.py "$VERSION" || OVERALL=1
echo

echo "=== Tier 4: usage tests against stubs/$VERSION ==="
pyright tests/usage/ || OVERALL=1
echo

echo "=== Tier 2 (tracking): stubs internal consistency ==="
TIER2_OUT=$(pyright "stubs/$VERSION/Live" 2>&1) || true
echo "$TIER2_OUT"
TIER2_TAIL=$(echo "$TIER2_OUT" | tail -1)
if [[ "$STRICT" == "1" ]] && [[ "$TIER2_TAIL" != *"0 errors"* ]]; then
  OVERALL=1
fi
echo

if [[ "$OVERALL" -eq 0 ]]; then
  echo "verify: PASS"
else
  echo "verify: FAIL"
fi
exit $OVERALL

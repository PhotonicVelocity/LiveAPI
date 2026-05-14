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

# Prefer the local venv if present — parse_module_md needs pyyaml which
# isn't always in the system python.
if [[ -x "$REPO_ROOT/.venv/bin/python" ]]; then
  PY="$REPO_ROOT/.venv/bin/python"
else
  PY="python3"
fi

OVERALL=0

echo "=== Corpus pin consistency ==="
$PY tools/fetch_external/check_pin.py || OVERALL=1
echo

echo "=== Content schema + link integrity (content/$VERSION/) ==="
$PY tools/verify/validate_content.py "$VERSION" || OVERALL=1
echo

echo "=== Tier 1: ast.parse on stubs/$VERSION/Live ==="
$PY tools/verify/parse_check.py "$VERSION" || OVERALL=1
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

echo "=== Tier 3 (tracking): pyright --verifytypes (PEP 561 completeness) ==="
# Pyright's verifytypes resolves the package via Python's sys.path; pointing
# PYTHONPATH at stubs/$VERSION/ makes it find Live/ as a regular package
# (with __init__.pyi + py.typed) without needing to build/install a wheel.
TIER3_OUT=$(PYTHONPATH="stubs/$VERSION" pyright --verifytypes Live --ignoreexternal 2>&1) || true
TIER3_SCORE=$(echo "$TIER3_OUT" | grep -E "^Type completeness score:" | head -1)
echo "$TIER3_SCORE"
echo
TIER3_KNOWN=$(echo "$TIER3_OUT" | grep -E "^\s*With known type:" | head -1 | awk '{print $4}')
TIER3_AMBIG=$(echo "$TIER3_OUT" | grep -E "^\s*With ambiguous type:" | head -1 | awk '{print $4}')
TIER3_UNKNOWN=$(echo "$TIER3_OUT" | grep -E "^\s*With unknown type:" | head -1 | awk '{print $4}')
TIER3_TOTAL=$(echo "$TIER3_OUT" | grep -E "^Symbols exported by" | head -1 | awk '{print $NF}')
echo "Symbols: ${TIER3_TOTAL:-?} total — known ${TIER3_KNOWN:-?}, ambiguous ${TIER3_AMBIG:-?}, unknown ${TIER3_UNKNOWN:-?}"
if [[ "$STRICT" == "1" ]] && [[ "$TIER3_SCORE" != *"100%"* ]]; then
  OVERALL=1
fi
echo

if [[ "$OVERALL" -eq 0 ]]; then
  echo "verify: PASS"
else
  echo "verify: FAIL"
fi
exit $OVERALL

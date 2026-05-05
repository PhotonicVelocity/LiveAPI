#!/usr/bin/env python3
"""Validate that every reference to the corpus pin matches CORPUS_PIN.

The pin (a short git SHA from gluon/AbletonLive12_MIDIRemoteScripts) appears in:
  - tools/fetch_external/corpus.py (the source of truth)
  - tests/usage/*.py (URL anchors back to upstream)
  - tools/verify/README.md (documentation)

This check greps for any short-SHA-shaped references in those files and
asserts they all equal CORPUS_PIN. Run by tools/verify/run.sh.

Bumping the pin is then a CORPUS_PIN edit in corpus.py + a sed across the
URL references. Mismatches surface immediately.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Files that legitimately reference the pin.
PIN_REF_PATHS = [
    REPO_ROOT / "tools" / "fetch_external" / "corpus.py",
    REPO_ROOT / "tools" / "verify" / "README.md",
    *(REPO_ROOT / "tests" / "usage").glob("*.py"),
]

# A short SHA appearing inside the gluon corpus URL or as a literal pin.
URL_PIN_RE = re.compile(
    r"github\.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/([0-9a-f]{7,40})/"
)
LITERAL_PIN_RE = re.compile(r'CORPUS_PIN\s*=\s*"([0-9a-f]{7,40})"')
COMMIT_PHRASE_RE = re.compile(r"commit `([0-9a-f]{7,40})`")


def _expected_pin() -> str:
    """Read CORPUS_PIN from corpus.py — the source of truth."""
    text = (REPO_ROOT / "tools" / "fetch_external" / "corpus.py").read_text()
    m = LITERAL_PIN_RE.search(text)
    if not m:
        print("error: CORPUS_PIN not found in tools/fetch_external/corpus.py", file=sys.stderr)
        sys.exit(2)
    return m.group(1)


def main() -> int:
    expected = _expected_pin()
    print(f"Expected pin (from corpus.py): {expected}")

    mismatches: list[tuple[Path, int, str]] = []
    for path in PIN_REF_PATHS:
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text().splitlines(), start=1):
            for match_re in (URL_PIN_RE, COMMIT_PHRASE_RE):
                for m in match_re.finditer(line):
                    sha = m.group(1)
                    if not expected.startswith(sha) and not sha.startswith(expected):
                        try:
                            rel = path.relative_to(REPO_ROOT)
                        except ValueError:
                            rel = path
                        mismatches.append((rel, lineno, sha))

    if mismatches:
        print(f"\n{len(mismatches)} pin mismatch(es):", file=sys.stderr)
        for rel, lineno, sha in mismatches:
            print(f"  {rel}:{lineno}: found {sha!r}, expected {expected!r}", file=sys.stderr)
        return 1

    print("All pin references match.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

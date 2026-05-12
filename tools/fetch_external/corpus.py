#!/usr/bin/env python3
"""Clone the decompiled Ableton Remote Scripts corpus at the pinned commit.

The corpus is the source of truth for "how Ableton's own engineers use the API."
It feeds:
  - tests/usage/* (Tier 4 verification — patterns drawn from real call sites)
  - tools/verify/audit_corpus.py (offline corpus audit against our stubs)
  - stubs/<v>/modules/*.md (per-override source citations on _override blocks)

The pin is updated rarely. When bumping:
  1. Update CORPUS_PIN below.
  2. Update tests/usage/* docstrings + tools/verify/README.md to use the new SHA.
  3. Run tools/fetch_external/check_pin.py to confirm everywhere matches.
  4. Re-clone (rm -rf external/corpus && this script).
  5. Run tools/verify/run.sh — fix any new findings before committing the bump.

Usage:
    python tools/fetch_external/corpus.py           # clone if absent, fetch + checkout pin if present
    python tools/fetch_external/corpus.py --force   # delete existing dir and re-clone fresh
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

CORPUS_PIN = "810ef77"
CORPUS_REPO = "https://github.com/gluon/AbletonLive12_MIDIRemoteScripts.git"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXTERNAL_DIR = REPO_ROOT / "external"
CORPUS_PATH = EXTERNAL_DIR / "corpus"


def _run(cmd: list[str], cwd: Path | None = None) -> None:
    """Run a subprocess; print the command and abort on failure."""
    print(f"  $ {' '.join(cmd)}" + (f"  (in {cwd})" if cwd else ""))
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"failed: {' '.join(cmd)}", file=sys.stderr)
        sys.exit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true",
                        help="Delete existing corpus dir and re-clone")
    args = parser.parse_args()

    EXTERNAL_DIR.mkdir(parents=True, exist_ok=True)

    if args.force and CORPUS_PATH.exists():
        print(f"Removing {CORPUS_PATH}")
        shutil.rmtree(CORPUS_PATH)

    if not CORPUS_PATH.exists():
        print(f"Cloning {CORPUS_REPO} → {CORPUS_PATH}")
        _run(["git", "clone", "--quiet", CORPUS_REPO, str(CORPUS_PATH)])
    else:
        print(f"Corpus already at {CORPUS_PATH}; fetching")
        _run(["git", "fetch", "--quiet", "origin"], cwd=CORPUS_PATH)

    print(f"Checking out {CORPUS_PIN}")
    _run(["git", "checkout", "--quiet", CORPUS_PIN], cwd=CORPUS_PATH)

    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                          cwd=CORPUS_PATH, capture_output=True, text=True).stdout.strip()
    print(f"Corpus at {head}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

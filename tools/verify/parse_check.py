#!/usr/bin/env python3
"""Tier-1 verification: every .pyi file under stubs/<version>/Live/ ast-parses.

Usage:
    python tools/verify/parse_check.py                  # check stubs/12.3.6/Live
    python tools/verify/parse_check.py 12.3.6           # explicit version
    python tools/verify/parse_check.py --path PATH      # explicit directory

Exits non-zero if any file fails to parse.
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", nargs="?", default="12.3.6")
    parser.add_argument("--path", help="Override stubs directory (default: stubs/<version>/Live)")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    target = Path(args.path) if args.path else repo_root / "stubs" / args.version / "Live"
    if not target.is_dir():
        print(f"error: not a directory: {target}", file=sys.stderr)
        return 2

    files = sorted(target.rglob("*.pyi"))
    if not files:
        print(f"error: no .pyi files under {target}", file=sys.stderr)
        return 2

    failed: list[tuple[Path, SyntaxError]] = []
    for path in files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as e:
            failed.append((path, e))

    if failed:
        print(f"FAIL: {len(failed)} of {len(files)} stub files do not parse", file=sys.stderr)
        for path, err in failed:
            rel = path.relative_to(repo_root) if path.is_relative_to(repo_root) else path
            print(f"  {rel}:{err.lineno}: {err.msg}", file=sys.stderr)
        return 1

    print(f"OK: {len(files)} stub files parse")
    return 0


if __name__ == "__main__":
    sys.exit(main())

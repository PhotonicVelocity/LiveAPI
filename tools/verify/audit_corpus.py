#!/usr/bin/env python3
"""Offline corpus audit: pyright over the decompiled Ableton Remote Scripts using our stubs.

Surfaces places where our `Live/*.pyi` stubs and Ableton's own production code disagree.
Each diagnostic is something Ableton actually wrote — so a stub-side error here means our
stubs are claiming something different from what working production code does.

Filters out two large noise classes the corpus is full of:
  - Imports of Ableton-internal modules (`_Framework`, `ableton.v2`, `pushbase`, …) for which
    no stubs exist — every Remote Script imports these and we can't help it.
  - Decompilation artifacts: name-mangled attribute accesses like `_Class__attr` that the
    decompiler reconstructed from bytecode but no source-level type checker can resolve.

What's left is Live-related signal: missing API surface, wrong inheritance, type
incompatibilities at scale. Output is grouped and counted; not a CI gate. Run by hand
during cleanup or before publish.

Usage:
    python tools/verify/audit_corpus.py
    python tools/verify/audit_corpus.py --raw      # show every diagnostic, ungrouped
    python tools/verify/audit_corpus.py --top 30   # show the 30 most-common groups
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG = REPO_ROOT / "tools" / "verify" / "audit_pyrightconfig.json"
IGNORES = REPO_ROOT / "tools" / "verify" / "audit_ignores.yaml"

# Imports of these modules / packages are out-of-scope; we have no stubs for them.
INTERNAL_PREFIXES = (
    "_Framework",
    "_APC",
    "_Generic",
    "_Mono_Framework",
    "ableton",
    "pushbase",
    "novation",
    "consts",
    "Live.X",   # not real; defensive — but typos in corpus do happen
)

# Name-mangled attribute accesses (`_ClassName__attr`) come from the decompiler's
# reconstruction; they aren't valid in source-level Python and pyright can't resolve them.
MANGLED_NAME_RE = re.compile(r"_[A-Z][A-Za-z0-9_]*__")

# Pure-decompilation-noise message patterns (pyright complaining about reconstructed
# bytecode that no source-level type checker could ever validate).
DECOMPILATION_NOISE_PATTERNS = (
    "Statements must be separated by newlines or semicolons",
    "Expression value is unused",
    "could not be determined because it refers to itself",
    "Argument to class must be a base class",
    "Module is not callable",
)


def _live_class_names() -> set[str]:
    """Return the set of class names declared in our stubs/12.3.6/Live/*.pyi."""
    stubs_dir = REPO_ROOT / "stubs" / "12.3.6" / "Live"
    names: set[str] = set()
    class_re = re.compile(r"^\s*class\s+([A-Z][A-Za-z0-9_]*)")
    for pyi in stubs_dir.glob("*.pyi"):
        for line in pyi.read_text(encoding="utf-8").splitlines():
            m = class_re.match(line)
            if m:
                names.add(m.group(1))
    return names


def _mentions_live_class(message: str, live_classes: set[str]) -> bool:
    """True if the diagnostic message names a class declared in our stubs."""
    for cls in live_classes:
        # Match as a quoted token to avoid spurious substring matches (e.g., "List" in "ListenerHandle").
        if f'"{cls}"' in message or f'"{cls}.' in message or f' {cls} ' in message:
            return True
    return False


def _load_ignores() -> list[dict]:
    """Parse audit_ignores.yaml. Returns [] when missing or empty."""
    if not IGNORES.exists():
        return []
    try:
        import yaml  # noqa: PLC0415  (optional dependency for ignore support)
    except ImportError:
        print(
            f"warning: PyYAML not available — ignore list at {IGNORES.relative_to(REPO_ROOT)} "
            "will not be applied. Install with `pip install pyyaml`.",
            file=sys.stderr,
        )
        return []
    data = yaml.safe_load(IGNORES.read_text()) or {}
    return data.get("ignores") or []


def _matches_ignore(file: str, message: str, entry: dict) -> bool:
    match = entry.get("match") or {}
    if not match:
        return False
    if "file_contains" in match and match["file_contains"] not in file:
        return False
    if "message_contains" in match and match["message_contains"] not in message:
        return False
    return True


def _is_internal_import(message: str) -> bool:
    """Drop pyright errors about imports of Ableton-internal modules."""
    if "Import" not in message and "could not be resolved" not in message:
        return False
    for prefix in INTERNAL_PREFIXES:
        if f'"{prefix}' in message or f"'{prefix}" in message:
            return True
    return False


def _is_mangled_attr(message: str) -> bool:
    """Drop attribute-access errors against name-mangled members."""
    return ("attribute" in message.lower()) and bool(MANGLED_NAME_RE.search(message))


def _normalize_message(message: str) -> str:
    """Collapse instance-specific text so we can group by error shape."""
    msg = re.sub(r'"[^"]+"', '"X"', message)  # collapse quoted strings
    msg = re.sub(r"\bline \d+", "line N", msg)
    return msg.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", action="store_true", help="Print every diagnostic, ungrouped")
    parser.add_argument("--top", type=int, default=20, help="How many groups to show in summary mode")
    parser.add_argument(
        "--all-noise",
        action="store_true",
        help="Show all diagnostics that survive the basic filters (no Live-class restriction)",
    )
    args = parser.parse_args()

    live_classes = _live_class_names()
    ignores = _load_ignores()

    print(f"Running pyright with --project {CONFIG.relative_to(REPO_ROOT)} ...", file=sys.stderr)
    result = subprocess.run(
        ["pyright", "--project", str(CONFIG), "--outputjson"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if not result.stdout:
        print("pyright produced no output:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        return 2

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"failed to parse pyright JSON output: {e}", file=sys.stderr)
        return 2

    diags = data.get("generalDiagnostics", [])
    total = len(diags)

    kept: list[dict] = []
    dropped_internal = 0
    dropped_mangled = 0
    dropped_decomp = 0
    dropped_no_live = 0
    dropped_ignored = 0
    ignored_by_id: dict[str, int] = {}
    for d in diags:
        msg = d.get("message", "")
        if _is_internal_import(msg):
            dropped_internal += 1
            continue
        if _is_mangled_attr(msg):
            dropped_mangled += 1
            continue
        if any(p in msg for p in DECOMPILATION_NOISE_PATTERNS):
            dropped_decomp += 1
            continue
        if not args.all_noise and not _mentions_live_class(msg, live_classes):
            dropped_no_live += 1
            continue
        # Ignore-list match (after Live-class filter so the count reflects real-signal noise)
        file = d.get("file", "")
        matched_id = next((e.get("id", "?") for e in ignores if _matches_ignore(file, msg, e)), None)
        if matched_id is not None:
            dropped_ignored += 1
            ignored_by_id[matched_id] = ignored_by_id.get(matched_id, 0) + 1
            continue
        kept.append(d)

    print(
        f"diagnostics: {total} total · "
        f"{dropped_internal} internal-imports · "
        f"{dropped_mangled} mangled-attrs · "
        f"{dropped_decomp} decompilation-noise · "
        f"{dropped_no_live} no-Live-class · "
        f"{dropped_ignored} ignored · "
        f"{len(kept)} kept",
        file=sys.stderr,
    )
    if ignored_by_id:
        print("ignored breakdown:", file=sys.stderr)
        for ig_id, count in sorted(ignored_by_id.items()):
            print(f"  {count:4d}  {ig_id}", file=sys.stderr)

    if args.raw:
        for d in kept:
            file = d.get("file", "")
            try:
                rel = Path(file).resolve().relative_to(REPO_ROOT)
            except ValueError:
                rel = Path(file)
            line = d.get("range", {}).get("start", {}).get("line", 0) + 1
            sev = d.get("severity", "?")
            print(f"  {rel}:{line} [{sev}] {d.get('message', '')}")
        return 0

    # Group by normalized message
    grouped: Counter[str] = Counter()
    examples: dict[str, list[str]] = {}
    for d in kept:
        norm = _normalize_message(d.get("message", ""))
        grouped[norm] += 1
        if norm not in examples:
            file = d.get("file", "")
            try:
                rel = Path(file).resolve().relative_to(REPO_ROOT)
            except ValueError:
                rel = Path(file)
            line = d.get("range", {}).get("start", {}).get("line", 0) + 1
            examples[norm] = [f"{rel}:{line}"]
        elif len(examples[norm]) < 3:
            file = d.get("file", "")
            try:
                rel = Path(file).resolve().relative_to(REPO_ROOT)
            except ValueError:
                rel = Path(file)
            line = d.get("range", {}).get("start", {}).get("line", 0) + 1
            examples[norm].append(f"{rel}:{line}")

    print(f"\nTop {args.top} grouped diagnostics:\n")
    for norm, count in grouped.most_common(args.top):
        print(f"[{count}] {norm}")
        for ex in examples[norm]:
            print(f"      e.g. {ex}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())

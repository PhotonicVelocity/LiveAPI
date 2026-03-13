"""Resolve argument names by analysing definitions and call sites in decompiled Remote Scripts.

Searches a local clone of gluon/AbletonLive12_MIDIRemoteScripts for:

1. **Function definitions** — ``def func_name(self, param1, param2)`` gives us parameter names
   directly. When multiple definitions exist, names are voted on per position.

2. **Call sites** — ``obj.func_name(value)`` gives us the variable names callers use. These are
   collected as hints for the LLM resolution phase, not treated as resolved names.

For methods with common names (append, extend, etc.), the parent object at the call site is
compared against the class name to avoid cross-class contamination.

Input:
    stubs/<version>/pipeline/unresolved.json
        Items with args that have ``needs_name: true``.

Output (stdout, or --output file):
    JSON with two sections:
    - ``refinements`` — high-confidence names from definition analysis (refinements format)
    - ``call_site_hints`` — per-arg vote tallies from call sites (context for LLM phase)

Reference data:
    doc/decompiled/AbletonLive12_MIDIRemoteScripts/
        Auto-cloned on first run if missing (shallow clone, ~50 MB).

Usage:
    python tools/parse/callsite_resolve.py 12.3.6
    python tools/parse/callsite_resolve.py 12.3.6 --pretty -o pipeline/refinements.callsite.json
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from os.path import dirname
from pathlib import Path

REPO_ROOT = Path(dirname(dirname(dirname(__file__))))
DECOMPILED_DIR = REPO_ROOT / "doc" / "decompiled" / "AbletonLive12_MIDIRemoteScripts"

# Patterns we skip when extracting names — these are not meaningful identifiers
_SKIP_NAMES = {"self", "None", "True", "False"}
# Minimum length for extracted names — single-char vars like i, j, k are loop artifacts
_MIN_NAME_LEN = 2

# Function names common enough to cause cross-class vote contamination.
# For these, we require the call-site parent to match the class name.
_AMBIGUOUS_NAMES = {"append", "extend", "remove", "insert", "pop", "clear", "count", "index", "copy", "sort"}


def _extract_arg_name(node: ast.expr) -> str | None:
    """Extract a human-readable name from a call-site argument expression.

    Returns a snake_case name suitable for a parameter, or None if the
    expression is too complex to yield a useful name.
    """
    # Simple variable: channel, cc_no, midi_map_handle
    if isinstance(node, ast.Name):
        name = node.id
        if name in _SKIP_NAMES or name.startswith("_") or len(name) < _MIN_NAME_LEN:
            return None
        # Skip ALL_CAPS constants — they're specific to the caller, not the API
        if name.isupper():
            return None
        return name

    # Attribute access: self.channel, self._channel
    # Skip chained calls like self.song().signature_denominator — the attribute describes
    # the return value, not the parameter.
    if isinstance(node, ast.Attribute):
        if isinstance(node.value, ast.Call):
            return None
        attr = node.attr
        if attr.startswith("_") or len(attr) < _MIN_NAME_LEN:
            return None
        if attr.isupper():
            return None
        return attr

    # Method call: self.handle(), self.script_handle()
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        method = node.func.attr
        if method.startswith("_") or len(method) < _MIN_NAME_LEN:
            return None
        return method

    # Subscript: BUTTONS[i] — skip, too specific
    # Constant: 0, 15, "string" — skip
    # BinOp, UnaryOp, etc. — skip
    return None


def _extract_parent_name(node: ast.expr) -> str | None:
    """Extract the parent object name from a method call target.

    For ``obj.method()``, returns the variable/attribute name of ``obj``.
    Used to disambiguate common method names like append/extend.
    """
    if not isinstance(node, ast.Attribute):
        return None
    value = node.value
    if isinstance(value, ast.Name):
        return value.id.lower()
    if isinstance(value, ast.Attribute):
        return value.attr.lstrip("_").lower()
    # self.thing().method() — use the method name as parent hint
    if isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute):
        return value.func.attr.lstrip("_").lower()
    return None


def _find_py_files(directory: Path) -> list[Path]:
    """Recursively find all .py files."""
    return list(directory.rglob("*.py"))


def _parse_file(path: Path) -> ast.Module | None:
    """Parse a Python file, returning None on failure."""
    try:
        source = path.read_text(encoding="utf-8", errors="replace")
        return ast.parse(source, filename=str(path))
    except (SyntaxError, ValueError):
        return None


def _build_search_patterns(unresolved: dict) -> dict[str, list[str]]:
    """Build a mapping from function name to list of unresolved paths that use it."""
    patterns: dict[str, list[str]] = {}
    for path, entry in unresolved.items():
        if "args" not in entry:
            continue
        has_name_needed = any(arg.get("needs_name") for arg in entry["args"].values())
        if not has_name_needed:
            continue

        parts = path.split(".")
        func_name = parts[-1]
        if func_name not in patterns:
            patterns[func_name] = []
        patterns[func_name].append(path)
    return patterns


def _is_method(path: str) -> bool:
    """Determine if a path represents an instance method (has self as arg1)."""
    parts = path.split(".")
    # Module-level functions: Live.MidiMap.forward_midi_cc (3 parts)
    # Instance methods: Live.Clip.Clip.quantize (4+ parts)
    if len(parts) >= 4:
        return True
    return False


def _class_name_from_path(path: str) -> str:
    """Extract the class name from a LOM path, lowercased for fuzzy matching.

    Live.Clip.MidiNoteVector.append -> 'midinotevector'
    Live.Song.Song.jump_by -> 'song'
    """
    parts = path.split(".")
    if len(parts) >= 4:
        return parts[-2].lower()
    return ""


def _parent_matches_class(parent: str | None, class_name: str) -> bool:
    """Check if a call-site parent name plausibly refers to the target class.

    Uses substring matching: parent 'midi_note_vector' matches class 'midinotevector',
    parent 'notes' matches class 'midinotevector' (partial).
    """
    if not parent or not class_name:
        return False
    # Normalize: strip underscores for comparison
    parent_norm = parent.replace("_", "")
    return parent_norm in class_name or class_name in parent_norm


# ---------------------------------------------------------------------------
# Definition collector — high-confidence source of arg names
# ---------------------------------------------------------------------------


class DefCollector(ast.NodeVisitor):
    """AST visitor that collects parameter names from function definitions."""

    def __init__(self, target_funcs: set[str]):
        self.target_funcs = target_funcs
        # func_name -> list of param name lists (one per definition found)
        self.hits: dict[str, list[list[str]]] = {f: [] for f in target_funcs}

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if node.name in self.target_funcs:
            # Collect non-self parameter names
            params = []
            for arg in node.args.args:
                name = arg.arg
                if name == "self":
                    continue
                params.append(name)
            if params:
                self.hits[node.name].append(params)
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef


def _collect_def_sites(py_files: list[Path], target_funcs: set[str]) -> dict[str, list[list[str]]]:
    """Scan all Python files for function definitions matching target names."""
    merged: dict[str, list[list[str]]] = {f: [] for f in target_funcs}
    for path in py_files:
        tree = _parse_file(path)
        if tree is None:
            continue
        collector = DefCollector(target_funcs)
        collector.visit(tree)
        for func, hits in collector.hits.items():
            merged[func].extend(hits)
    return merged


# ---------------------------------------------------------------------------
# Call-site collector — lower-confidence, used as hints
# ---------------------------------------------------------------------------


class CallSiteCollector(ast.NodeVisitor):
    """AST visitor that collects argument names and parent context from call sites."""

    def __init__(self, target_funcs: set[str]):
        self.target_funcs = target_funcs
        # func_name -> list of (parent_name, [arg_names])
        self.hits: dict[str, list[tuple[str | None, list[str | None]]]] = {f: [] for f in target_funcs}

    def visit_Call(self, node: ast.Call) -> None:
        func_name = self._get_func_name(node.func)
        if func_name and func_name in self.target_funcs:
            parent = _extract_parent_name(node.func)
            arg_names: list[str | None] = []
            for arg in node.args:
                arg_names.append(_extract_arg_name(arg))
            self.hits[func_name].append((parent, arg_names))
        self.generic_visit(node)

    def _get_func_name(self, node: ast.expr) -> str | None:
        """Extract the function name from a call target."""
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        return None


def _collect_call_sites(
    py_files: list[Path], target_funcs: set[str]
) -> dict[str, list[tuple[str | None, list[str | None]]]]:
    """Scan all Python files for calls to target functions."""
    merged: dict[str, list[tuple[str | None, list[str | None]]]] = {f: [] for f in target_funcs}
    for path in py_files:
        tree = _parse_file(path)
        if tree is None:
            continue
        collector = CallSiteCollector(target_funcs)
        collector.visit(tree)
        for func, hits in collector.hits.items():
            merged[func].extend(hits)
    return merged


# ---------------------------------------------------------------------------
# Resolution from definitions
# ---------------------------------------------------------------------------


def _resolve_from_defs(
    unresolved: dict,
    def_sites: dict[str, list[list[str]]],
    patterns: dict[str, list[str]],
) -> dict[str, dict]:
    """Produce refinements from function definition analysis.

    For each unresolved function, find definitions with matching names, vote on
    parameter names per position, and emit refinements.
    """
    refinements: dict[str, dict] = {}

    for func_name, paths in patterns.items():
        defs = def_sites.get(func_name, [])
        if not defs:
            continue

        for path in paths:
            entry = unresolved[path]
            args = entry["args"]
            is_meth = _is_method(path)

            needs_name_args = {k: v for k, v in args.items() if v.get("needs_name")}
            if not needs_name_args:
                continue

            arg_refinement: dict[str, dict] = {}

            for arg_key in sorted(needs_name_args.keys()):
                m = re.match(r"arg(\d+)", arg_key)
                if not m:
                    continue
                arg_num = int(m.group(1))

                if is_meth:
                    # arg2 in unresolved = position 0 in def (self excluded)
                    def_idx = arg_num - 2
                else:
                    def_idx = arg_num - 1

                if def_idx < 0:
                    continue

                # Vote across all definitions
                name_votes: Counter[str] = Counter()
                total_defs = 0
                for def_params in defs:
                    if def_idx < len(def_params):
                        total_defs += 1
                        param = def_params[def_idx]
                        if param not in _SKIP_NAMES and not param.startswith("_") and len(param) >= _MIN_NAME_LEN:
                            name_votes[param] += 1

                if not name_votes:
                    continue

                best_name, best_count = name_votes.most_common(1)[0]

                arg_refinement[arg_key] = {
                    "name": best_name,
                    "name_reason": f"Definition analysis: {best_count}/{total_defs} defs use '{best_name}'",
                    "_votes": dict(name_votes),
                    "_total_defs": total_defs,
                }

            if arg_refinement:
                refinements[path] = {"args": arg_refinement}

    return refinements


# ---------------------------------------------------------------------------
# Call-site hints (context for LLM phase)
# ---------------------------------------------------------------------------


def _build_call_site_hints(
    unresolved: dict,
    call_sites: dict[str, list[tuple[str | None, list[str | None]]]],
    patterns: dict[str, list[str]],
    already_resolved: dict[str, dict],
) -> dict[str, dict]:
    """Collect unique call-site value names as hints for the LLM phase.

    Skips args already resolved by definition analysis.
    For ambiguous names (append, extend, ...), filters call sites by parent match.
    """
    hints: dict[str, dict] = {}

    for func_name, paths in patterns.items():
        all_sites = call_sites.get(func_name, [])
        if not all_sites:
            continue

        is_ambiguous = func_name in _AMBIGUOUS_NAMES

        for path in paths:
            entry = unresolved[path]
            args = entry["args"]
            is_meth = _is_method(path)
            class_name = _class_name_from_path(path)

            needs_name_args = {k: v for k, v in args.items() if v.get("needs_name")}
            if not needs_name_args:
                continue

            # Skip args already resolved by defs
            resolved_args = set()
            if path in already_resolved:
                resolved_args = set(already_resolved[path].get("args", {}).keys())

            # Filter sites by parent match for ambiguous names
            if is_ambiguous:
                sites = [(p, a) for p, a in all_sites if _parent_matches_class(p, class_name)]
            else:
                sites = all_sites

            if not sites:
                continue

            arg_hints: dict[str, dict] = {}

            for arg_key in sorted(needs_name_args.keys()):
                if arg_key in resolved_args:
                    continue

                m = re.match(r"arg(\d+)", arg_key)
                if not m:
                    continue
                arg_num = int(m.group(1))

                if is_meth:
                    site_idx = arg_num - 2
                else:
                    site_idx = arg_num - 1

                if site_idx < 0:
                    continue

                name_votes: Counter[str] = Counter()
                total_sites = 0
                for _parent, site_args in sites:
                    if site_idx < len(site_args):
                        total_sites += 1
                        name = site_args[site_idx]
                        if name:
                            name_votes[name] += 1

                if not name_votes:
                    continue

                # Collect unique names sorted by frequency
                sorted_names = [name for name, _count in name_votes.most_common()]
                arg_hints[arg_key] = {
                    "call_site_names": sorted_names,
                    "_votes": dict(name_votes),
                    "_total_sites": total_sites,
                }

            if arg_hints:
                hints[path] = {"args": arg_hints}

    return hints


# ---------------------------------------------------------------------------
# Repo cloning and orchestration
# ---------------------------------------------------------------------------

_DECOMPILED_REPO = "https://github.com/gluon/AbletonLive12_MIDIRemoteScripts.git"


def _clone_decompiled_scripts() -> None:
    """Shallow-clone the decompiled Remote Scripts repo into doc/decompiled/."""
    import subprocess

    print(f"Cloning {_DECOMPILED_REPO} into {DECOMPILED_DIR}...", file=sys.stderr)
    DECOMPILED_DIR.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "clone", "--depth", "1", _DECOMPILED_REPO, str(DECOMPILED_DIR)],
        check=True,
    )
    print("Clone complete.", file=sys.stderr)


def resolve(version: str) -> dict:
    """Run call-site resolution for the given stub version."""
    stubs_dir = REPO_ROOT / "stubs" / version
    unresolved_path = stubs_dir / "pipeline" / "unresolved.json"

    if not unresolved_path.exists():
        print(f"Error: {unresolved_path} not found", file=sys.stderr)
        sys.exit(1)

    if not DECOMPILED_DIR.exists():
        _clone_decompiled_scripts()

    with open(unresolved_path) as f:
        data = json.load(f)
    unresolved = data["items"]

    # Build search patterns
    patterns = _build_search_patterns(unresolved)
    target_funcs = set(patterns.keys())

    print(f"Searching for {len(target_funcs)} function names across decompiled scripts...", file=sys.stderr)

    # Find and parse all .py files
    py_files = _find_py_files(DECOMPILED_DIR)
    print(f"Scanning {len(py_files)} Python files...", file=sys.stderr)

    # Phase 1: Collect definitions (high confidence)
    def_sites = _collect_def_sites(py_files, target_funcs)
    defs_with_hits = sum(1 for defs in def_sites.values() if defs)
    total_defs = sum(len(defs) for defs in def_sites.values())
    print(f"Found {total_defs} definitions across {defs_with_hits}/{len(target_funcs)} functions", file=sys.stderr)

    # Phase 2: Collect call sites (hints)
    call_sites = _collect_call_sites(py_files, target_funcs)
    total_calls = sum(len(sites) for sites in call_sites.values())
    calls_with_hits = sum(1 for sites in call_sites.values() if sites)
    print(f"Found {total_calls} call sites across {calls_with_hits}/{len(target_funcs)} functions", file=sys.stderr)

    # Resolve from definitions
    refinements = _resolve_from_defs(unresolved, def_sites, patterns)

    # Build call-site hints for remaining args
    call_site_hints = _build_call_site_hints(unresolved, call_sites, patterns, refinements)

    # Summary
    resolved_args = sum(len(r["args"]) for r in refinements.values())
    hint_args = sum(len(h["args"]) for h in call_site_hints.values())
    total_needed = sum(
        sum(1 for a in entry["args"].values() if a.get("needs_name"))
        for entry in unresolved.values()
        if "args" in entry
    )
    print(f"\nResolved {resolved_args}/{total_needed} arg names from definitions", file=sys.stderr)
    print(f"Collected call-site hints for {hint_args} additional args", file=sys.stderr)

    return {"version": version, "refinements": refinements, "call_site_hints": call_site_hints}


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve arg names from decompiled definitions and call sites")
    parser.add_argument("version", help="Stub version (e.g. 12.3.6)")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()

    result = resolve(args.version)

    indent = 2 if args.pretty else None
    output = json.dumps(result, indent=indent)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
            f.write("\n")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()

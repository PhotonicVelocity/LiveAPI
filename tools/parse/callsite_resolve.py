"""Resolve argument names by analysing call sites in decompiled Remote Scripts.

Searches a local clone of gluon/AbletonLive12_MIDIRemoteScripts for actual
invocations of unresolved Live API functions. For each function with unnamed
args (arg1, arg2, …), finds call sites across 1200+ decompiled .py files,
extracts the variable names passed at each positional arg, votes across all
call sites, and picks the most common name per position.

Input:
    stubs/<version>/pipeline/unresolved.json
        Items with args that have ``needs_name: true``.

Output (stdout, or --output file):
    JSON in refinements format — same structure as refinements.llm.json,
    with ``name``, ``name_reason``, ``_votes``, and ``_total_sites`` per arg.

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
from os.path import dirname, join
from pathlib import Path

REPO_ROOT = Path(dirname(dirname(dirname(__file__))))
DECOMPILED_DIR = REPO_ROOT / "doc" / "decompiled" / "AbletonLive12_MIDIRemoteScripts"

# Patterns we skip when extracting names — these are not meaningful identifiers
_SKIP_NAMES = {"self", "None", "True", "False"}
# Minimum length for extracted names — single-char vars like i, j, k are loop artifacts
_MIN_NAME_LEN = 2


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

    # Attribute access: self.handle() is handled by Call below,
    # but self.channel or self._channel
    if isinstance(node, ast.Attribute):
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
    """Build a mapping from function name to list of unresolved paths that use it.

    For module-level functions like Live.MidiMap.forward_midi_cc, we search for
    both 'forward_midi_cc(' and 'Live.MidiMap.forward_midi_cc('.

    For instance methods like Live.Clip.Clip.quantize, we search for '.quantize('.
    """
    patterns: dict[str, list[str]] = {}
    for path, entry in unresolved.items():
        if "args" not in entry:
            continue
        # Only items with needs_name args
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
    # Module-level functions: Live.Application.encrypt_challenge2 (3 parts)
    # Instance methods: Live.Clip.Clip.quantize (4+ parts)
    # But also: Live.Base.log (3 parts, module-level)
    # And: Live.Application.ControlSurfaceProxy.send_midi (4 parts, instance method)
    # Heuristic: if there are 4+ parts, it's likely an instance method
    # For 3 parts, check if the second part looks like a class (starts with uppercase)
    if len(parts) >= 4:
        return True
    if len(parts) == 3:
        # Module-level functions in Live.MidiMap, Live.Application, Live.Base
        return False
    return False


class CallSiteCollector(ast.NodeVisitor):
    """AST visitor that collects argument names from call sites."""

    def __init__(self, target_funcs: set[str]):
        self.target_funcs = target_funcs
        # func_name -> list of (arg_position, extracted_name)
        self.hits: dict[str, list[list[str | None]]] = {f: [] for f in target_funcs}

    def visit_Call(self, node: ast.Call) -> None:
        func_name = self._get_func_name(node.func)
        if func_name and func_name in self.target_funcs:
            arg_names: list[str | None] = []
            for arg in node.args:
                arg_names.append(_extract_arg_name(arg))
            self.hits[func_name].append(arg_names)
        self.generic_visit(node)

    def _get_func_name(self, node: ast.expr) -> str | None:
        """Extract the function name from a call target."""
        # Simple name: forward_midi_cc(...)
        if isinstance(node, ast.Name):
            return node.id
        # Attribute: Live.MidiMap.forward_midi_cc(...) or self.quantize(...)
        if isinstance(node, ast.Attribute):
            return node.attr
        return None


def _collect_call_sites(py_files: list[Path], target_funcs: set[str]) -> dict[str, list[list[str | None]]]:
    """Scan all Python files for calls to target functions."""
    merged: dict[str, list[list[str | None]]] = {f: [] for f in target_funcs}
    for path in py_files:
        tree = _parse_file(path)
        if tree is None:
            continue
        collector = CallSiteCollector(target_funcs)
        collector.visit(tree)
        for func, hits in collector.hits.items():
            merged[func].extend(hits)
    return merged


def _resolve_from_call_sites(
    unresolved: dict,
    call_sites: dict[str, list[list[str | None]]],
    patterns: dict[str, list[str]],
    min_confidence: int = 1,
) -> dict[str, dict]:
    """Produce refinements from call-site analysis.

    For each unresolved item, look at collected call sites for its function name,
    align arg positions, vote on names, and emit refinements for high-confidence matches.
    """
    refinements: dict[str, dict] = {}

    for func_name, paths in patterns.items():
        sites = call_sites.get(func_name, [])
        if not sites:
            continue

        for path in paths:
            entry = unresolved[path]
            args = entry["args"]
            is_meth = _is_method(path)

            # Build arg keys in order (arg1, arg2, ... or named args)
            needs_name_args = {k: v for k, v in args.items() if v.get("needs_name")}
            if not needs_name_args:
                continue

            # Map arg keys to their expected position in call sites
            # For instance methods, the unresolved args start at arg2 (arg1=self)
            # and call sites don't include self, so call-site index 0 = arg2
            # For module-level functions, arg1 maps to call-site index 0
            arg_refinement: dict[str, dict] = {}

            for arg_key in sorted(needs_name_args.keys()):
                # Extract the numeric position from argN
                m = re.match(r"arg(\d+)", arg_key)
                if not m:
                    continue
                arg_num = int(m.group(1))

                if is_meth:
                    # arg2 in unresolved = position 0 in call site (self excluded)
                    site_idx = arg_num - 2
                else:
                    # arg1 in unresolved = position 0 in call site
                    site_idx = arg_num - 1

                if site_idx < 0:
                    continue

                # Collect names from all call sites at this position
                name_votes: Counter[str] = Counter()
                total_sites = 0
                for site_args in sites:
                    if site_idx < len(site_args):
                        total_sites += 1
                        name = site_args[site_idx]
                        if name:
                            name_votes[name] += 1

                if not name_votes:
                    continue

                # Pick the most common name
                best_name, best_count = name_votes.most_common(1)[0]
                if best_count < min_confidence:
                    continue

                arg_refinement[arg_key] = {
                    "name": best_name,
                    "name_reason": f"Call-site analysis: {best_count}/{total_sites} sites use '{best_name}'",
                    "_votes": dict(name_votes),
                    "_total_sites": total_sites,
                }

            if arg_refinement:
                refinements[path] = {"args": arg_refinement}

    return refinements


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

    # Collect call sites
    call_sites = _collect_call_sites(py_files, target_funcs)

    # Count total hits
    total_hits = sum(len(sites) for sites in call_sites.values())
    funcs_with_hits = sum(1 for sites in call_sites.values() if sites)
    print(f"Found {total_hits} call sites across {funcs_with_hits}/{len(target_funcs)} functions", file=sys.stderr)

    # Resolve
    refinements = _resolve_from_call_sites(unresolved, call_sites, patterns)

    # Summary
    resolved_args = sum(len(r["args"]) for r in refinements.values())
    total_needed = sum(
        sum(1 for a in entry["args"].values() if a.get("needs_name"))
        for entry in unresolved.values()
        if "args" in entry
    )
    print(f"\nResolved {resolved_args}/{total_needed} arg names across {len(refinements)} functions", file=sys.stderr)

    return {"version": version, "refinements": refinements}


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve arg names from decompiled call sites")
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

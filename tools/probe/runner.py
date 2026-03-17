"""Probe runner — connects to LiveRelay, discovers and runs probe modules, writes ProbeResults.json."""

from __future__ import annotations

import argparse
import importlib
import json
import pkgutil
import sys
import time
from pathlib import Path
from typing import Any

# Ensure repo root is on sys.path so `tools.probe.*` imports work when run as a script
_repo_root = str(Path(__file__).resolve().parent.parent.parent)
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

try:
    from pythonforlive.client import LiveClient
except ImportError:
    print(
        "Probe scripts require the PythonForLive client.\n" "Install with: pip install -e ../PythonForLive",
        file=sys.stderr,
    )
    sys.exit(1)

from tools.probe.base import ProbeContext


def discover_probe_modules() -> dict[str, Any]:
    """Discover all probe modules in tools/probe/probes/ and return {class_name: module}."""
    import tools.probe.probes as probes_pkg

    modules: dict[str, Any] = {}
    for importer, name, ispkg in pkgutil.iter_modules(probes_pkg.__path__):
        if name.startswith("_"):
            continue
        mod = importlib.import_module(f"tools.probe.probes.{name}")
        # Module name is the class name in snake_case; convert to PascalCase for display
        class_name = getattr(mod, "CLASS_NAME", name.replace("_", " ").title().replace(" ", ""))
        modules[class_name] = mod
    return modules


def get_probe_functions(module: Any, categories: list[str] | None) -> list[tuple[str, Any]]:
    """Get probe functions from a module, optionally filtered by category.

    Probe functions are named probe_<category>(ctx) — e.g. probe_undo, probe_async, probe_range, probe_error.
    """
    funcs = []
    for name in sorted(dir(module)):
        if not name.startswith("probe_"):
            continue
        category = name[len("probe_") :]
        if categories and category not in categories:
            continue
        fn = getattr(module, name)
        if callable(fn):
            funcs.append((category, fn))
    return funcs


def run_probes(
    ctx: ProbeContext,
    classes: list[str] | None = None,
    categories: list[str] | None = None,
) -> dict[str, Any]:
    """Discover and run probe functions, return structured results."""
    modules = discover_probe_modules()

    if classes:
        # Filter to requested classes
        filtered = {}
        for cls_name in classes:
            if cls_name in modules:
                filtered[cls_name] = modules[cls_name]
            else:
                print(f"  Warning: no probe module for {cls_name}", file=sys.stderr)
        modules = filtered

    if not modules:
        print("No probe modules found.", file=sys.stderr)
        return {}

    for cls_name, mod in sorted(modules.items()):
        funcs = get_probe_functions(mod, categories)
        if not funcs:
            continue

        print(f"\n{'=' * 60}")
        print(f"  {cls_name}")
        print(f"{'=' * 60}")

        for category, fn in funcs:
            print(f"\n--- {category} ---")
            try:
                fn(ctx)
            except Exception as e:
                print(f"  ERROR in probe_{category}: {e}", file=sys.stderr)

    return ctx.to_dict()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Live API behavioral probes via LiveRelay")
    parser.add_argument("version", help="Live version being probed (e.g. 12.3.6)")
    parser.add_argument("--classes", help="Comma-separated class names to probe (default: all)")
    parser.add_argument("--categories", help="Comma-separated categories: undo,async,range,error (default: all)")
    parser.add_argument("--output", help="Output path for ProbeResults.json (default: stubs/<version>/pipeline/)")
    parser.add_argument("--socket", default="/tmp/liverelay.sock", help="LiveRelay socket path")
    args = parser.parse_args()

    classes = [c.strip() for c in args.classes.split(",")] if args.classes else None
    categories = [c.strip() for c in args.categories.split(",")] if args.categories else None

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(f"stubs/{args.version}/pipeline/ProbeResults.json")

    # Connect to LiveRelay
    print(f"Connecting to LiveRelay at {args.socket}...")
    client = LiveClient(args.socket)
    print("Connected.\n")

    ctx = ProbeContext(client)

    start = time.time()
    results = run_probes(ctx, classes=classes, categories=categories)
    elapsed = time.time() - start

    # Add metadata
    output = {
        "version": args.version,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "elapsed_seconds": round(elapsed, 1),
        "classes": results.get("classes", {}),
    }

    # Write results
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, default=str) + "\n")

    # Summary
    total_props = sum(len(c.get("properties", {})) for c in output["classes"].values())
    total_methods = sum(len(c.get("methods", {})) for c in output["classes"].values())
    print(f"\n{'=' * 60}")
    print(f"  Done in {elapsed:.1f}s — {total_props} properties, {total_methods} methods")
    print(f"  Written to {output_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

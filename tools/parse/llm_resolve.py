"""LLM-assisted resolution of unresolved types and arg names.

Reads unresolved.json and MaxForLive documentation, sends them to Claude,
and produces refinements.llm.json — with no hardcoded domain knowledge.

Usage:
    # Prepare batch files for Agent tool (no API key needed):
    python tools/parse/llm_resolve.py 12.3.6 --prepare

    # Then feed each batch to a subagent. Results go in stubs/{version}/pipeline/batches/.
    # Merge results:
    python tools/parse/llm_resolve.py 12.3.6 --merge

    # Or call the API directly (requires ANTHROPIC_API_KEY):
    python tools/parse/llm_resolve.py 12.3.6

The system prompt lives in llm_resolve_prompt.md alongside this script.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from os.path import dirname, exists, join
from pathlib import Path


def _load_system_prompt() -> str:
    """Load the system prompt from llm_resolve_prompt.md."""
    prompt_path = join(dirname(__file__), "llm_resolve_prompt.md")
    with open(prompt_path) as f:
        return f.read().strip()


def _build_type_skeleton(tree: dict) -> dict | None:
    """Build a types-only skeleton of the parsed tree for LLM context.

    Includes modules, classes, enums (with values), and properties (with probed types).
    Omits functions — those are already on the unresolved items themselves.
    """
    FUNCTION_TYPES = {"function", "builtin_function_or_method", "method", "method_descriptor"}

    def _strip(node: dict) -> dict | None:
        t = node.get("type")
        if t in ("module", "class"):
            out: dict = {"name": node["name"], "type": t}
            if node.get("constructable"):
                out["constructable"] = True
            children = [_strip(c) for c in node.get("children", []) if isinstance(c, dict)]
            children = [c for c in children if c is not None]
            if children:
                out["children"] = children
            return out
        if t == "enum":
            out = {"name": node["name"], "type": "enum"}
            values = [c.get("name") for c in node.get("children", [])
                      if isinstance(c, dict) and c.get("type") == "int"]
            if values:
                out["values"] = values
            return out
        if t == "property":
            out = {"name": node["name"]}
            if node.get("probed_type"):
                out["probed_type"] = node["probed_type"]
            return out
        if t == "str":
            return {"name": node["name"], "type": "str", "value": node.get("value")}
        if t == "type":
            return {"name": node["name"], "type": "exception"}
        if t in FUNCTION_TYPES:
            return None
        return None

    return _strip(tree)


def _build_user_prompt(items: list[dict], m4l_docs: dict[str, str],
                       type_skeleton: dict | None = None) -> str:
    """Build the user prompt with unresolved items, type skeleton, and MaxForLive docs."""
    parts = []

    parts.append("## Unresolved Items\n")
    parts.append("```json")
    parts.append(json.dumps(items, indent=2))
    parts.append("```\n")

    if type_skeleton:
        parts.append("## API Type Skeleton\n")
        parts.append("This is the complete type hierarchy of the Live API — all modules, classes, enums, "
                     "and properties. Use it to identify valid type names and understand class relationships.\n")
        parts.append("```json")
        parts.append(json.dumps(type_skeleton, indent=2))
        parts.append("```\n")

    # Split into M4L docs and reference docs
    m4l_only = {k: v for k, v in m4l_docs.items() if not k.startswith("reference/")}
    ref_only = {k: v for k, v in m4l_docs.items() if k.startswith("reference/")}

    if m4l_only:
        parts.append("## MaxForLive Documentation\n")
        parts.append("These are the official Ableton MaxForLive docs for the Live Object Model. "
                     "Use them to find parameter names, types, and descriptions.\n")
        for filename, content in sorted(m4l_only.items()):
            parts.append(f"### {filename}\n")
            parts.append(content)
            parts.append("")

    if ref_only:
        parts.append("## Reference Documentation\n")
        parts.append("These are curated API reference docs with probed function signatures, "
                     "parameter names, and types. When these docs show explicit parameter names "
                     "in function signatures (e.g. `load_item(item)`, `insert_step(start, length, value)`), "
                     "use those names directly.\n")
        for filename, content in sorted(ref_only.items()):
            parts.append(f"### {filename}\n")
            parts.append(content)
            parts.append("")

    return "\n".join(parts)


def _load_m4l_docs(m4l_dir: str) -> dict[str, str]:
    """Load all MaxForLive markdown files and reference docs."""
    docs = {}
    for path in sorted(glob.glob(join(m4l_dir, "*.md"))):
        filename = os.path.basename(path)
        with open(path) as f:
            docs[filename] = f.read()

    # Also load reference docs (curated per-class docs with probed parameter names)
    ref_dir = join(os.path.dirname(m4l_dir), "reference")
    if os.path.isdir(ref_dir):
        for path in sorted(glob.glob(join(ref_dir, "**", "*.md"), recursive=True)):
            relpath = os.path.relpath(path, ref_dir)
            key = f"reference/{relpath}"
            with open(path) as f:
                docs[key] = f.read()
    return docs


def _relevant_m4l_docs(items: list[dict], all_docs: dict[str, str]) -> dict[str, str]:
    """Filter M4L/reference docs to only those relevant to the given items."""
    # Collect module and class names from items
    names = set()
    for item in items:
        parts = item["path"].split(".")
        if len(parts) > 1:
            names.add(parts[1].lower())  # module
        if len(parts) > 2:
            names.add(parts[2].lower())  # class

    relevant = {}
    for fn, content in all_docs.items():
        # For reference docs like "reference/tracks/Envelope.md", use the filename stem
        basename = os.path.basename(fn)
        stem = basename.replace(".md", "").lower()
        if any(n in stem or stem in n for n in names):
            relevant[fn] = content
    return relevant


def _batch_items(items: list[dict], batch_size: int = 70) -> list[list[dict]]:
    """Split unresolved items into batches grouped by module."""
    from collections import OrderedDict
    by_module: dict[str, list[dict]] = OrderedDict()
    for item in items:
        parts = item["path"].split(".")
        module = parts[1] if len(parts) > 1 else "unknown"
        by_module.setdefault(module, []).append(item)

    batches: list[list[dict]] = []
    current: list[dict] = []
    for module_items in by_module.values():
        if len(current) + len(module_items) > batch_size and current:
            batches.append(current)
            current = []
        current.extend(module_items)
    if current:
        batches.append(current)

    return batches


def _call_llm(system: str, user: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Call the Anthropic API and return the response text."""
    import anthropic

    client = anthropic.Anthropic()
    message = client.messages.create(
        model=model,
        max_tokens=16384,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return message.content[0].text


def _parse_response(text: str) -> dict:
    """Extract JSON from the LLM response, handling markdown fences."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)
    return json.loads(text)


def _load_type_skeleton(version: str) -> dict | None:
    """Load the parsed tree and build a types-only skeleton."""
    parsed_path = join("stubs", version, "pipeline", "LiveTree.parsed.json")
    if not exists(parsed_path):
        return None
    with open(parsed_path) as f:
        data = json.load(f)
    tree = data.get("tree", data)
    return _build_type_skeleton(tree)


def prepare(version: str, input_path: str, m4l_dir: str) -> str:
    """Write batch files to disk for use with the Agent tool.

    Returns the batch directory path.
    """
    with open(input_path) as f:
        unresolved = json.load(f)

    all_docs = _load_m4l_docs(m4l_dir)
    type_skeleton = _load_type_skeleton(version)
    items = unresolved["unresolved"]
    batches = _batch_items(items)

    batch_dir = join("stubs", version, "pipeline", "batches")
    Path(batch_dir).mkdir(parents=True, exist_ok=True)

    system_prompt = _load_system_prompt()
    with open(join(batch_dir, "system_prompt.md"), "w") as f:
        f.write(system_prompt)

    for i, batch in enumerate(batches, 1):
        modules = sorted(set(item["path"].split(".")[1] for item in batch))
        relevant_docs = _relevant_m4l_docs(batch, all_docs)

        # Write items
        with open(join(batch_dir, f"batch{i}_items.json"), "w") as f:
            json.dump(batch, f, indent=2)

        # Write full prompt (system + user combined for easy copy-paste)
        user_prompt = _build_user_prompt(batch, relevant_docs, type_skeleton)
        with open(join(batch_dir, f"batch{i}_prompt.md"), "w") as f:
            f.write(user_prompt)

        print(f"Batch {i}: {len(batch)} items, modules: {', '.join(modules)}, "
              f"M4L docs: {len(relevant_docs)}")

    print(f"\nWrote {len(batches)} batches to {batch_dir}/")
    print(f"System prompt: {batch_dir}/system_prompt.md")
    print(f"\nTo run with Agent tool, feed each batch{i}_prompt.md as the user message")
    print(f"with system_prompt.md as context. Save results as batch{{N}}_result.json.")
    return batch_dir


def merge(version: str, batch_dir: str, output_path: str) -> dict:
    """Merge batch result files into a single refinements.llm.json."""
    merged: dict[str, dict] = {}

    result_files = sorted(glob.glob(join(batch_dir, "batch*_result.json")))
    if not result_files:
        print(f"No batch result files found in {batch_dir}/")
        sys.exit(1)

    for path in result_files:
        with open(path) as f:
            data = json.load(f)
        refs = data.get("refinements", data)  # Handle both wrapped and unwrapped
        if isinstance(refs, dict) and "refinements" not in refs:
            # Already the refinements dict
            batch_refs = refs
        else:
            batch_refs = refs.get("refinements", refs)
        merged.update(batch_refs)
        print(f"  {os.path.basename(path)}: {len(batch_refs)} refinements")

    result = {"version": version, "refinements": merged}
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nMerged {len(merged)} total refinements to {output_path}")
    return result


def summarize(generated: dict) -> None:
    """Print a summary of the generated refinements."""
    refs = generated.get("refinements", {})

    name_fixes = 0
    type_fixes = 0
    return_fixes = 0
    probed_types = 0

    for entry in refs.values():
        if "probed_type" in entry:
            probed_types += 1
        if "returns" in entry:
            return_fixes += 1
        for arg_val in entry.get("args", {}).values():
            if isinstance(arg_val, dict):
                if "name" in arg_val:
                    name_fixes += 1
                if "type" in arg_val:
                    type_fixes += 1

    print(f"\nSummary: {len(refs)} paths")
    print(f"  arg names resolved: {name_fixes}")
    print(f"  arg types resolved: {type_fixes}")
    print(f"  return types resolved: {return_fixes}")
    print(f"  property types resolved: {probed_types}")


def main():
    parser = argparse.ArgumentParser(description="LLM-assisted resolution of unresolved types/names")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to unresolved.json")
    parser.add_argument("--output", help="Path to output refinements.llm.json")
    parser.add_argument("--m4l-dir", help="Path to MaxForLive docs directory", default="MaxForLive")
    parser.add_argument("--model", help="Claude model to use", default="claude-sonnet-4-20250514")
    parser.add_argument("--prepare", action="store_true",
                        help="Write batch files for Agent tool, don't call API")
    parser.add_argument("--merge", action="store_true",
                        help="Merge batch result files into refinements.llm.json")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")
    args = parser.parse_args()

    pipeline = join("stubs", args.version, "pipeline")
    input_path = args.input or join(pipeline, "unresolved.json")
    output_path = args.output or join(pipeline, "refinements.llm.json")
    batch_dir = join(pipeline, "batches")

    if args.prepare:
        prepare(args.version, input_path, args.m4l_dir)
        return

    if args.merge:
        result = merge(args.version, batch_dir, output_path)
        summarize(result)
        return

    # Direct API mode
    with open(input_path) as f:
        unresolved = json.load(f)

    m4l_docs = _load_m4l_docs(args.m4l_dir)
    type_skeleton = _load_type_skeleton(args.version)
    items = unresolved["unresolved"]
    print(f"Loaded {len(items)} unresolved items, {len(m4l_docs)} MaxForLive docs"
          f"{', type skeleton loaded' if type_skeleton else ''}")

    system_prompt = _load_system_prompt()
    user_prompt = _build_user_prompt(items, m4l_docs, type_skeleton)

    if args.dry_run:
        print(f"\n--- System prompt ({len(system_prompt)} chars) ---")
        print(system_prompt)
        print(f"\n--- User prompt ({len(user_prompt)} chars) ---")
        print(user_prompt[:2000])
        print(f"... ({len(user_prompt)} chars total)")
        return

    print(f"Calling {args.model}...")
    response_text = _call_llm(system_prompt, user_prompt, model=args.model)

    result = _parse_response(response_text)
    result["version"] = unresolved.get("version", "")

    n = len(result.get("refinements", {}))
    print(f"LLM produced {n} refinements")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote to {output_path}")
    summarize(result)


if __name__ == "__main__":
    main()

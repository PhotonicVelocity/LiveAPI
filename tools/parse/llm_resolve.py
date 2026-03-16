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
import subprocess
import sys
from os.path import dirname, exists, join
from pathlib import Path


def _load_system_prompt() -> str:
    """Load the system prompt from llm_resolve_prompt.md."""
    prompt_path = join(dirname(__file__), "llm_resolve_prompt.md")
    with open(prompt_path) as f:
        return f.read().strip()


def _build_type_skeleton(tree: dict) -> str | None:
    """Build a types-only skeleton of the parsed tree for LLM context."""
    import sys
    parse_dir = dirname(__file__)
    if parse_dir not in sys.path:
        sys.path.insert(0, parse_dir)
    from build_type_skeleton import build_skeleton
    return build_skeleton(tree)


def _build_user_prompt(items: dict[str, dict], m4l_docs: dict[str, str],
                       type_skeleton: str | None = None,
                       callsite_data: dict | None = None) -> str:
    """Build the user prompt with unresolved items, type skeleton, callsite hints, and MaxForLive docs."""
    parts = []

    # Manual hints — domain knowledge that can't be inferred from code
    hints_path = join(dirname(__file__), "llm_hints.md")
    if exists(hints_path):
        with open(hints_path) as f:
            hints = f.read().strip()
        if hints:
            parts.append(hints)
            parts.append("\n")

    parts.append("## Unresolved Items\n")
    parts.append("```json")
    parts.append(json.dumps(items, indent=2))
    parts.append("```\n")

    # Inject callsite hints for items in this batch
    if callsite_data:
        call_hints = callsite_data.get("call_site_hints", {})
        type_hints = callsite_data.get("type_hints", {})

        # Filter to items in this batch
        batch_call_hints = {k: v for k, v in call_hints.items() if k in items}
        batch_type_hints = {k: v for k, v in type_hints.items() if k in items}

        if batch_call_hints or batch_type_hints:
            parts.append("## Decompiled Remote Scripts Evidence\n")
            parts.append("These hints were extracted from Ableton's decompiled Remote Scripts "
                         "(1200+ Python files that call the Live API). Use them as additional "
                         "evidence when resolving names and types.\n")

        if batch_call_hints:
            parts.append("### Call-Site Arg Name Hints\n")
            parts.append("Variable names observed at call sites for each arg position, "
                         "sorted by frequency. These are the names callers used when passing "
                         "values — suggestive but not definitive.\n")
            parts.append("```json")
            parts.append(json.dumps(batch_call_hints, indent=2))
            parts.append("```\n")

        if batch_type_hints:
            parts.append("### Type Usage Context\n")
            parts.append("Code snippets showing how members with unresolved types are used "
                         "in practice. Use these to infer types from usage patterns "
                         "(e.g. compared to strings → str, iterated → sequence, etc.).\n")
            parts.append("```json")
            parts.append(json.dumps(batch_type_hints, indent=2))
            parts.append("```\n")

    if type_skeleton:
        parts.append("## API Type Skeleton\n")
        parts.append("This is the complete type hierarchy of the Live API — all modules, classes, enums "
                     "(with values), and properties (with types where known). Use it to identify valid type "
                     "names and understand class/module relationships.\n")
        parts.append("Format: containers end with `:` and have indented children, properties use "
                     "`name -> Type`, enums use `Name = val1, val2, ...`, string constants use "
                     "`name = 'value'`, exceptions use `!Name`.\n")
        parts.append("```")
        parts.append(type_skeleton)
        parts.append("```\n")

    if m4l_docs:
        parts.append("## MaxForLive Documentation\n")
        parts.append("These are the official Ableton MaxForLive docs for the Live Object Model. "
                     "Use them to find parameter names, types, and descriptions.\n")
        for filename, content in sorted(m4l_docs.items()):
            parts.append(f"### {filename}\n")
            parts.append(_indent_headers(content, 3))
            parts.append("")

    return "\n".join(parts)


def _load_m4l_docs(m4l_dir: str) -> dict[str, str]:
    """Load all MaxForLive markdown files."""
    docs = {}
    for path in sorted(glob.glob(join(m4l_dir, "*.md"))):
        filename = os.path.basename(path)
        with open(path) as f:
            docs[filename] = f.read()
    return docs


def _relevant_m4l_docs(paths: list[str], all_docs: dict[str, str]) -> dict[str, str]:
    """Filter M4L docs to relevant files, then extract only sections for unresolved items.

    Keeps the file preamble (everything before the first ### header) for context,
    plus only the ### sections whose name matches an unresolved function/property.
    """
    # Collect module/class names for file-level matching
    module_names = set()
    # Collect function/property names for section-level filtering
    func_names = set()
    for path in paths:
        parts = path.split(".")
        if len(parts) > 1:
            module_names.add(parts[1].lower())
        if len(parts) > 2:
            module_names.add(parts[2].lower())
        if len(parts) >= 4:
            func_names.add(parts[-1])

    relevant = {}
    for fn, content in all_docs.items():
        basename = os.path.basename(fn)
        stem = basename.replace(".md", "").lower()
        if not any(n in stem or stem in n for n in module_names):
            continue

        # Extract preamble + relevant sections
        filtered = _extract_sections(content, func_names)
        if filtered:
            relevant[fn] = filtered
    return relevant


def _indent_headers(text: str, levels: int) -> str:
    """Increase all markdown header levels by the given amount."""
    prefix = "#" * levels
    lines = text.split("\n")
    return "\n".join(prefix + line if line.startswith("#") else line for line in lines)


def _extract_sections(doc: str, names: set[str]) -> str | None:
    """Extract preamble and matching ### sections from a markdown doc.

    Returns None if no sections matched (preamble alone isn't useful).
    """
    lines = doc.split("\n")
    preamble: list[str] = []
    sections: list[str] = []
    in_relevant = False
    in_preamble = True

    for line in lines:
        if line.startswith("### "):
            in_preamble = False
            # Extract section name: "### func_name ..." or "### `func_name`"
            header_parts = line[4:].split()
            name = header_parts[0].strip("`") if header_parts else ""
            in_relevant = name in names

        if in_preamble:
            preamble.append(line)
        elif in_relevant:
            sections.append(line)

    if not sections:
        return None
    return "\n".join(preamble + sections).strip()


def _batch_items(items: dict[str, dict], batch_size: int = 70) -> list[dict[str, dict]]:
    """Split unresolved items dict into balanced batches grouped by module.

    First groups items by module (keeping related paths together), then distributes
    module groups across batches as evenly as possible.
    """
    from math import ceil

    by_module: list[dict[str, dict]] = []
    current_module: str | None = None
    current_group: dict[str, dict] = {}
    for path, entry in items.items():
        parts = path.split(".")
        module = parts[1] if len(parts) > 1 else "unknown"
        if module != current_module and current_group:
            by_module.append(current_group)
            current_group = {}
        current_module = module
        current_group[path] = entry
    if current_group:
        by_module.append(current_group)

    total = sum(len(g) for g in by_module)
    num_batches = max(1, ceil(total / batch_size))
    target = ceil(total / num_batches)

    batches: list[dict[str, dict]] = []
    current: dict[str, dict] = {}
    for group in by_module:
        if len(current) + len(group) > target and current:
            batches.append(current)
            current = {}
        current.update(group)
    if current:
        batches.append(current)

    return batches


def _call_llm(system: str, user: str, model: str = "claude-sonnet-4-20250514",
              max_retries: int = 3) -> str:
    """Call the Anthropic API and return the response text. Retries on rate limits."""
    import time
    import anthropic  # type: ignore[import-not-found]

    client = anthropic.Anthropic()
    for attempt in range(max_retries + 1):
        try:
            message = client.messages.create(
                model=model,
                max_tokens=16384,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            return message.content[0].text
        except anthropic.RateLimitError as e:
            if attempt == max_retries:
                raise
            # Parse retry-after header if available, otherwise wait 60s
            retry_after = getattr(e.response, "headers", {}).get("retry-after")
            wait = int(retry_after) if retry_after else 60
            print(f"  Rate limited, waiting {wait}s (attempt {attempt + 1}/{max_retries})...")
            time.sleep(wait)
    raise RuntimeError("unreachable")


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


def _fix_malformed_refinements(refinements: dict, items: dict[str, dict]) -> int:
    """Fix common LLM malformations in refinement output.

    Catches two patterns:
    1. type/type_reason at the root level instead of under args
    2. type/type_reason as siblings of arg entries inside args dict instead of inside an arg entry

    Returns the number of entries fixed.
    """
    VALID_KEYS = {"args", "returns", "probed_type", "probed_type_reason", "element_repr", "element_repr_reason"}
    fixed = 0
    for path, entry in list(refinements.items()):
        # Fix 1: type/type_reason at root level
        bad_keys = set(entry.keys()) - VALID_KEYS
        if bad_keys:
            unresolved = items.get(path, {})
            object_args = [
                aname for aname, aval in unresolved.get("args", {}).items()
                if aval.get("current_type") == "object"
            ]

            if object_args and "type" in entry:
                arg_name = object_args[0]
                arg_entry = {"type": entry.pop("type")}
                if "type_reason" in entry:
                    arg_entry["type_reason"] = entry.pop("type_reason")
                entry.setdefault("args", {})[arg_name] = arg_entry
                fixed += 1
                print(f"  Fixed malformed entry: {path} (moved type from root to args.{arg_name})")
            else:
                print(f"  Warning: unexpected keys {bad_keys} in {path}, could not auto-fix")

        # Fix 2: type/type_reason as siblings of arg entries inside args dict
        # e.g. {"args": {"arg2": {"name": "notes"}, "type": "list[X]", "type_reason": "..."}}
        args_dict = entry.get("args", {})
        if "type" in args_dict and isinstance(args_dict["type"], str):
            # Find the actual arg entry (the one that's a dict, not a string)
            arg_entries = {k: v for k, v in args_dict.items() if isinstance(v, dict)}
            if len(arg_entries) == 1:
                arg_name = next(iter(arg_entries))
                arg_entries[arg_name]["type"] = args_dict.pop("type")
                if "type_reason" in args_dict:
                    arg_entries[arg_name]["type_reason"] = args_dict.pop("type_reason")
                fixed += 1
                print(f"  Fixed malformed entry: {path} (moved type from args to args.{arg_name})")

    return fixed


def _load_type_skeleton(version: str) -> str | None:
    """Load the parsed tree and build a types-only skeleton."""
    parsed_path = join("stubs", version, "pipeline", "LiveTree.parsed.json")
    if not exists(parsed_path):
        return None
    with open(parsed_path) as f:
        data = json.load(f)
    tree = data.get("tree", data)
    return _build_type_skeleton(tree)


def _load_callsite_data(callsite_path: str | None) -> dict | None:
    """Load callsite hints file if provided and it exists."""
    if not callsite_path or not exists(callsite_path):
        return None
    with open(callsite_path) as f:
        return json.load(f)


def prepare(version: str, input_path: str, m4l_dir: str,
            callsite_path: str | None = None) -> str:
    """Write batch files to disk for use with the Agent tool.

    Returns the batch directory path.
    """
    with open(input_path) as f:
        unresolved = json.load(f)

    all_docs = _load_m4l_docs(m4l_dir)
    type_skeleton = _load_type_skeleton(version)
    callsite_data = _load_callsite_data(callsite_path)
    items = unresolved["items"]
    batches = _batch_items(items)

    batch_dir = join("stubs", version, "pipeline", "batches")
    Path(batch_dir).mkdir(parents=True, exist_ok=True)

    system_prompt = _load_system_prompt()
    with open(join(batch_dir, "system_prompt.md"), "w") as f:
        f.write(system_prompt)

    for i, batch in enumerate(batches, 1):
        modules = sorted(set(path.split(".")[1] for path in batch))
        relevant_docs = _relevant_m4l_docs(list(batch.keys()), all_docs)

        # Write items
        with open(join(batch_dir, f"batch{i}_items.json"), "w") as f:
            json.dump(batch, f, indent=2)

        # Write full prompt (system + user combined for easy copy-paste)
        user_prompt = _build_user_prompt(batch, relevant_docs, type_skeleton, callsite_data)
        with open(join(batch_dir, f"batch{i}_prompt.md"), "w") as f:
            f.write(user_prompt)

        print(f"Batch {i}: {len(batch)} paths, modules: {', '.join(modules)}, "
              f"M4L docs: {len(relevant_docs)}")

    print(f"\nWrote {len(batches)} batches to {batch_dir}/")
    print(f"System prompt: {batch_dir}/system_prompt.md")
    print(f"\nTo run with Agent tool, feed each batch{{N}}_prompt.md as the user message")
    print(f"with system_prompt.md as context. Save results as batch{{N}}_result.json.")
    return batch_dir


def merge(version: str, batch_dir: str, output_path: str,
          unresolved_path: str | None = None) -> dict:
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

    # Fix malformed entries if we have the unresolved items for cross-reference
    if unresolved_path and exists(unresolved_path):
        with open(unresolved_path) as f:
            items = json.load(f).get("items", {})
        _fix_malformed_refinements(merged, items)

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
    element_types = 0

    for entry in refs.values():
        if "probed_type" in entry:
            probed_types += 1
        if "element_repr" in entry:
            element_types += 1
        if "returns" in entry:
            return_fixes += 1
        for arg_val in entry.get("args", {}).values():
            if isinstance(arg_val, dict):
                if "name" in arg_val:
                    name_fixes += 1
                if "type" in arg_val:
                    type_fixes += 1

    total = name_fixes + type_fixes + return_fixes + probed_types + element_types
    print(f"\nSummary: {len(refs)} paths")
    print(f"  arg names resolved: {name_fixes}")
    print(f"  arg types resolved: {type_fixes}")
    print(f"  return types resolved: {return_fixes}")
    print(f"  property types resolved: {probed_types}")
    print(f"  element types resolved: {element_types}")
    print(f"  total fixes: {total}")


def main():
    parser = argparse.ArgumentParser(description="LLM-assisted resolution of unresolved types/names")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to unresolved.json")
    parser.add_argument("--output", help="Path to output refinements.llm.json")
    parser.add_argument("--m4l-dir", help="Path to MaxForLive docs directory (auto-detected from version)")
    parser.add_argument("--model", help="Claude model to use", default="claude-sonnet-4-20250514")
    parser.add_argument("--callsite-hints",
                        help="Path to refinements.callsite.json for call-site and type hints")
    parser.add_argument("--prepare", action="store_true",
                        help="Write batch files for Agent tool, don't call API")
    parser.add_argument("--merge", action="store_true",
                        help="Merge batch result files into refinements.llm.json")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")
    args = parser.parse_args()

    # Auto-detect M4L docs directory from Live version, fetch if missing
    if not args.m4l_dir:
        major, minor = (int(x) for x in args.version.split(".")[:2])
        if major >= 12 and minor >= 2:
            args.m4l_dir = "doc/max-for-live-docs/9.0"
        else:
            args.m4l_dir = "doc/max-for-live-docs/8.0"

    if not exists(args.m4l_dir):
        print(f"M4L docs not found at {args.m4l_dir}, fetching...")
        fetch_script = join(dirname(__file__), "..", "other", "fetch_m4l_docs.py")
        cmd = [sys.executable, fetch_script, "-o", args.m4l_dir]
        if args.m4l_dir.endswith("8.0"):
            cmd.append("--legacy")
        subprocess.run(cmd, check=True)
        print()

    pipeline = join("stubs", args.version, "pipeline")
    # Prefer unresolved.remaining.json (post-callsite) over unresolved.json
    default_input = join(pipeline, "unresolved.remaining.json")
    if not exists(default_input):
        default_input = join(pipeline, "unresolved.json")
    input_path = args.input or default_input
    output_path = args.output or join(pipeline, "refinements.llm.json")
    batch_dir = join(pipeline, "batches")
    callsite_path = args.callsite_hints or join(pipeline, "refinements.callsite.json")

    if args.prepare:
        prepare(args.version, input_path, args.m4l_dir, callsite_path)
        return

    if args.merge:
        result = merge(args.version, batch_dir, output_path, unresolved_path=input_path)
        summarize(result)
        return

    # Direct API mode — automatically batches to stay within context limits
    with open(input_path) as f:
        unresolved = json.load(f)

    all_docs = _load_m4l_docs(args.m4l_dir)
    type_skeleton = _load_type_skeleton(args.version)
    callsite_data = _load_callsite_data(callsite_path)
    items = unresolved["items"]
    batches = _batch_items(items)
    print(f"Loaded {len(items)} paths in {len(batches)} batches, "
          f"{len(all_docs)} MaxForLive docs"
          f"{', type skeleton loaded' if type_skeleton else ''}"
          f"{', callsite hints loaded' if callsite_data else ''}")

    system_prompt = _load_system_prompt()

    if args.dry_run:
        # Show first batch as a preview
        batch = batches[0]
        relevant_docs = _relevant_m4l_docs(list(batch.keys()), all_docs)
        user_prompt = _build_user_prompt(batch, relevant_docs, type_skeleton, callsite_data)
        print(f"\n--- System prompt ({len(system_prompt)} chars) ---")
        print(system_prompt)
        print(f"\n--- User prompt for batch 1/{len(batches)} ({len(user_prompt)} chars) ---")
        print(user_prompt[:2000])
        print(f"... ({len(user_prompt)} chars total)")
        return

    merged: dict[str, dict] = {}
    for i, batch in enumerate(batches, 1):
        modules = sorted(set(path.split(".")[1] for path in batch))
        relevant_docs = _relevant_m4l_docs(list(batch.keys()), all_docs)
        user_prompt = _build_user_prompt(batch, relevant_docs, type_skeleton, callsite_data)

        print(f"\nBatch {i}/{len(batches)}: {len(batch)} paths, "
              f"modules: {', '.join(modules)}, docs: {len(relevant_docs)}")
        print(f"  Calling {args.model}...")
        response_text = _call_llm(system_prompt, user_prompt, model=args.model)

        batch_result = _parse_response(response_text)
        batch_refs = batch_result.get("refinements", batch_result)
        merged.update(batch_refs)
        print(f"  Got {len(batch_refs)} refinements")

    result = {"version": unresolved.get("version", ""), "refinements": merged}
    n_fixed = _fix_malformed_refinements(merged, items)
    print(f"\nTotal: {len(merged)} refinements from {len(batches)} batches"
          f"{f' ({n_fixed} fixed)' if n_fixed else ''}")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote to {output_path}")
    summarize(result)


if __name__ == "__main__":
    main()

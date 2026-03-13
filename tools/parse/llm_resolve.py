"""LLM-assisted resolution of unresolved types and arg names.

Reads unresolved.json and MaxForLive documentation, sends them to Claude,
and produces refinements.json — with no hardcoded domain knowledge.

Usage:
    # Prepare batch files for Agent tool (no API key needed):
    python tools/parse/llm_resolve.py 12.3.6 --prepare

    # Then feed each batch to a subagent. Results go in build/{version}/batches/.
    # Merge results:
    python tools/parse/llm_resolve.py 12.3.6 --merge

    # Or call the API directly (requires ANTHROPIC_API_KEY):
    python tools/parse/llm_resolve.py 12.3.6

    # Validate output against ground truth:
    python tools/parse/llm_resolve.py 12.3.6 --validate

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


def _build_user_prompt(items: list[dict], m4l_docs: dict[str, str]) -> str:
    """Build the user prompt with unresolved items and MaxForLive docs."""
    parts = []

    parts.append("## Unresolved Items\n")
    parts.append("```json")
    parts.append(json.dumps(items, indent=2))
    parts.append("```\n")

    parts.append("## MaxForLive Documentation\n")
    parts.append("These are the official Ableton MaxForLive docs for the Live Object Model. "
                 "Use them to find parameter names, types, and descriptions.\n")
    for filename, content in sorted(m4l_docs.items()):
        parts.append(f"### {filename}\n")
        parts.append(content)
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


def _relevant_m4l_docs(items: list[dict], all_docs: dict[str, str]) -> dict[str, str]:
    """Filter M4L docs to only those relevant to the given items."""
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
        stem = fn.replace(".md", "").lower()
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


def prepare(version: str, input_path: str, m4l_dir: str) -> str:
    """Write batch files to disk for use with the Agent tool.

    Returns the batch directory path.
    """
    with open(input_path) as f:
        unresolved = json.load(f)

    all_docs = _load_m4l_docs(m4l_dir)
    items = unresolved["unresolved"]
    batches = _batch_items(items)

    batch_dir = join("build", version, "batches")
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
        user_prompt = _build_user_prompt(batch, relevant_docs)
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


def validate(generated: dict, reference_path: str) -> dict:
    """Compare generated refinements against existing refinements.json."""
    with open(reference_path) as f:
        reference = json.load(f).get("refinements", {})

    gen_refs = generated.get("refinements", {})
    all_keys = sorted(set(list(reference.keys()) + list(gen_refs.keys())))

    matches = 0
    mismatches = 0
    missing = 0
    extra = 0
    extra_types = 0
    name_diffs = 0
    type_diffs = 0
    structural = 0

    for key in all_keys:
        ref = reference.get(key)
        gen = gen_refs.get(key)

        if ref and not gen:
            missing += 1
            print(f"  MISSING: {key}")
            print(f"    expected: {json.dumps(ref)}")
        elif gen and not ref:
            extra += 1
            print(f"  EXTRA: {key}")
            print(f"    generated: {json.dumps(gen)}")
        elif ref != gen:
            mismatches += 1
            if ref and gen:
                ref_args = ref.get("args", {})
                gen_args = gen.get("args", {})
                for arg_key in set(list(ref_args.keys()) + list(gen_args.keys())):
                    ra = ref_args.get(arg_key, {})
                    ga = gen_args.get(arg_key, {})
                    if "type" in ga and "type" not in ra:
                        extra_types += 1
                    if ra.get("name") != ga.get("name") and ("name" in ra or "name" in ga):
                        name_diffs += 1
                    if ra.get("type") != ga.get("type") and "type" in ra and "type" in ga:
                        type_diffs += 1
                if "return_type" in gen or "property_type" in gen:
                    structural += 1

            print(f"  MISMATCH: {key}")
            print(f"    expected:  {json.dumps(ref)}")
            print(f"    generated: {json.dumps(gen)}")
        else:
            matches += 1

    total = len(all_keys)
    print(f"\nValidation: {matches}/{total} exact matches, "
          f"{mismatches} mismatches, {missing} missing, {extra} extra")
    if extra_types:
        print(f"  Extra types added: {extra_types}")
    if name_diffs:
        print(f"  Name disagreements: {name_diffs}")
    if type_diffs:
        print(f"  Type disagreements: {type_diffs}")
    if structural:
        print(f"  Structural issues: {structural}")

    return {"matches": matches, "total": total, "mismatches": mismatches,
            "missing": missing, "extra": extra}


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
    parser.add_argument("--validate", action="store_true",
                        help="Compare output against existing refinements.json")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")
    args = parser.parse_args()

    input_path = args.input or join("build", args.version, "unresolved.json")
    output_path = args.output or join("build", args.version, "refinements.llm.json")
    batch_dir = join("build", args.version, "batches")

    if args.prepare:
        prepare(args.version, input_path, args.m4l_dir)
        return

    if args.merge:
        result = merge(args.version, batch_dir, output_path)
        if args.validate:
            ref_path = join("build", args.version, "refinements.json")
            if exists(ref_path):
                validate(result, ref_path)
        return

    # Direct API mode
    with open(input_path) as f:
        unresolved = json.load(f)

    m4l_docs = _load_m4l_docs(args.m4l_dir)
    items = unresolved["unresolved"]
    print(f"Loaded {len(items)} unresolved items, {len(m4l_docs)} MaxForLive docs")

    system_prompt = _load_system_prompt()
    user_prompt = _build_user_prompt(items, m4l_docs)

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

    if args.validate:
        ref_path = join("build", args.version, "refinements.json")
        if exists(ref_path):
            validate(result, ref_path)


if __name__ == "__main__":
    main()

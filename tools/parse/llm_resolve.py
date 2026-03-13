"""LLM-assisted resolution of unresolved types and arg names.

Reads unresolved.json and MaxForLive documentation, sends them to Claude via the Agent tool
(subagent), and produces refinements.json — with no hardcoded domain knowledge.

Usage:
    python tools/parse/llm_resolve.py 12.3.6
    python tools/parse/llm_resolve.py 12.3.6 --dry-run        # print prompt, don't call LLM
    python tools/parse/llm_resolve.py 12.3.6 --validate       # compare output against existing refinements.json

When run directly, requires ANTHROPIC_API_KEY environment variable. The script is also designed
to have its prompt extracted and used with the Claude Code Agent tool for key-less execution.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from os.path import exists, join


_SYSTEM_PROMPT = """\
You are an expert on Ableton Live's Python API (the Live Object Model / LOM). You are resolving \
unresolved types and parameter names in the API's type stubs.

You will receive:
1. A JSON list of unresolved items from the parsed API tree
2. The full MaxForLive documentation (markdown files documenting the same API from Ableton's perspective)

Each unresolved item has a `kind` field:
- `arg_type`: An argument typed `object` that needs a more specific type
- `arg_name`: An argument named `arg1`, `arg2`, etc. that needs a meaningful name
- `return_type`: A return typed `object` that needs a more specific type
- `property_type`: A property with unknown runtime type

## Output Format

Respond with ONLY a JSON object in this exact format:
```json
{
  "refinements": {
    "Live.Module.Class.method": {
      "args": {
        "arg2": {
          "name": "new_name"
        }
      }
    },
    "Live.Module.Class.other_method": {
      "args": {
        "arg2": {
          "type": "SpecificType"
        }
      }
    },
    "Live.Module.Class.getter": {
      "returns": {
        "type": "ReturnType"
      }
    },
    "Live.Module.Class.prop": {
      "probed_type": "PropertyType"
    }
  }
}
```

## Critical Rules

### For `arg_name` items (the most common — ~164 items):
- Provide ONLY `"name"` with a meaningful parameter name. Do NOT include `"type"`.
- The type is already correct — these items only need a name fix.
- The current names are `arg1`, `arg2`, `arg3`, etc. — rename them to something descriptive.
- Key the args dict by the CURRENT arg name (e.g. `"arg2"`, not the new name).

### For `arg_type` items (~18 items):
- Provide ONLY `"type"` with the correct Python type. Do NOT include `"name"`.
- The arg name may already be meaningful — these items only need a type fix.
- Exception: if the arg also has a generic `argN` name, you may include both `"name"` and `"type"`.

### For `return_type` items (~2 items):
- Provide `"returns": {"type": "..."}` on the path entry (NOT `"return_type"`).

### For `property_type` items (~17 items):
- Provide `"probed_type": "..."` on the path entry (NOT `"property_type"`).

### General:
- Use Python type names: `str`, `bool`, `int`, `float`, `Callable`, `Any`, `list[X]`, `tuple[X, ...]`.
- For LOM class references, use the class name only (e.g. `ClipSlot` not `Live.ClipSlot.ClipSlot`).
- Combine multiple unresolved items on the same path into a single entry.
- If you cannot determine the correct resolution for an item, omit it entirely (do not guess).

## Naming Conventions

Use these conventions when choosing arg names:
- Vector `append`/`extend` methods: use `value` for the element argument (arg2).
- Index-based operations (delete_track, delete_scene, etc.): use `index`.
- Fire button state methods: use `state`.
- Clip note methods (add_new_notes, set_notes, etc.): use `notes` or `note_ids` as appropriate.
- Methods taking a DeviceParameter: use `parameter`.
- Methods taking a BrowserItem: use `item`.
- Amount/offset methods (jump_by, scrub_by, move_playing_pos): use `amount`.
- Boolean enable/disable args: use `enabled`.
- View identifier args (focus_view, show_view, hide_view, etc.): use `identifier`.
- View navigation args: `direction`, `identifier`, `animate`.

## Context Clues

Use ALL available context to determine the correct resolution:
- The `signature` field shows the Boost.Python signature with C++ argument types.
- The `cpp_signature` field shows the underlying C++ types:
  - `TString` = `str`
  - `TPyHandle<X>` = the X class object
  - `bool` = `bool`
  - `int` / `long` = `int`
  - `double` / `float` = `float`
- The `description` field describes what the function does.
- The MaxForLive docs may document the same function with explicit parameter names and types.
- Class context: `_live_ptr` properties are typically `int`.
- Pattern matching: if similar methods on sibling classes have known types, apply the same pattern.

## MidiMap Module Functions

Pay special attention to MidiMap functions — they follow specific parameter naming patterns:
- First arg is always `midi_map_handle`
- `map_midi_cc` / `map_midi_cc_with_feedback_map`: handle, parameter, midi_channel, cc_no, ...
- `map_midi_note` / `map_midi_note_with_feedback_map`: handle, parameter, midi_channel, note_number, ...
- `map_midi_pitchbend` / `map_midi_pitchbend_with_feedback_map`: handle, parameter, midi_channel, ...
- `forward_midi_cc`: handle, midi_channel, controller_number, controller_value
- `forward_midi_note`: handle, midi_channel, note_number, note_velocity
- `forward_midi_pitchbend`: handle, midi_channel, pitchbend_value
- `send_feedback_for_parameter`: handle, parameter

Respond with ONLY the JSON object, no other text."""


def _build_prompt(unresolved: dict, m4l_docs: dict[str, str]) -> str:
    """Build the user prompt with unresolved items and MaxForLive docs."""
    parts = []

    parts.append("## Unresolved Items\n")
    parts.append("```json")
    parts.append(json.dumps(unresolved["unresolved"], indent=2))
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


def _validate(generated: dict, reference_path: str) -> dict:
    """Compare generated refinements against existing refinements.json.

    Returns a dict with summary stats and detailed mismatches.
    """
    with open(reference_path) as f:
        reference = json.load(f).get("refinements", {})

    gen_refs = generated.get("refinements", {})
    all_keys = sorted(set(list(reference.keys()) + list(gen_refs.keys())))

    matches = 0
    mismatches = 0
    missing = 0
    extra = 0
    extra_types = 0  # LLM added type when only name was needed
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
            # Categorize
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
                # Check structural (wrong key names)
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


def _batch_items(items: list[dict], batch_size: int = 70) -> list[list[dict]]:
    """Split unresolved items into batches grouped by module."""
    # Group by module (first component after Live.)
    from collections import OrderedDict
    by_module: dict[str, list[dict]] = OrderedDict()
    for item in items:
        path = item["path"]
        parts = path.split(".")
        module = parts[1] if len(parts) > 1 else "unknown"
        by_module.setdefault(module, []).append(item)

    # Pack modules into batches
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


def get_system_prompt() -> str:
    """Return the system prompt for external callers (e.g. Agent tool)."""
    return _SYSTEM_PROMPT


def build_batch_prompt(items: list[dict], m4l_docs: dict[str, str]) -> str:
    """Build a prompt for a batch of items. Public for use with Agent tool."""
    batch_data = {"unresolved": items}
    return _build_prompt(batch_data, m4l_docs)


def main():
    parser = argparse.ArgumentParser(description="LLM-assisted resolution of unresolved types/names")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to unresolved.json")
    parser.add_argument("--output", help="Path to output refinements.json")
    parser.add_argument("--m4l-dir", help="Path to MaxForLive docs directory", default="MaxForLive")
    parser.add_argument("--model", help="Claude model to use", default="claude-sonnet-4-20250514")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling API")
    parser.add_argument("--validate", action="store_true",
                        help="Compare output against existing refinements.json")
    args = parser.parse_args()

    input_path = args.input or join("build", args.version, "unresolved.json")
    output_path = args.output or join("build", args.version, "refinements.llm.json")

    with open(input_path) as f:
        unresolved = json.load(f)

    m4l_docs = _load_m4l_docs(args.m4l_dir)
    print(f"Loaded {len(unresolved['unresolved'])} unresolved items, {len(m4l_docs)} MaxForLive docs")

    user_prompt = _build_prompt(unresolved, m4l_docs)

    if args.dry_run:
        print(f"\n--- System prompt ({len(_SYSTEM_PROMPT)} chars) ---")
        print(_SYSTEM_PROMPT)
        print(f"\n--- User prompt ({len(user_prompt)} chars) ---")
        print(user_prompt[:2000])
        print(f"... ({len(user_prompt)} chars total)")
        return

    print(f"Calling {args.model}...")
    response_text = _call_llm(_SYSTEM_PROMPT, user_prompt, model=args.model)

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
            _validate(result, ref_path)
        else:
            print(f"No reference refinements.json at {ref_path} to validate against")


if __name__ == "__main__":
    main()

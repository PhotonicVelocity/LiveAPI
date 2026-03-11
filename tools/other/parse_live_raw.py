"""
Parse and normalize LiveTree.raw.json into LiveTree.parsed.json.

Current transforms:
- Fix Boost.Python class name/doc concatenation when class names contain spaces.

Usage:
    python tools/parse_live_raw.py build/12.3.6
    python tools/parse_live_raw.py build/12.3.6/LiveTree.raw.json
    python tools/parse_live_raw.py build/12.3.6/LiveTree.raw.json --output /tmp/LiveTree.parsed.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def split_joined_class_name(name: str) -> tuple[str, str] | None:
    """Split a malformed class name into (class_name, doc_fragment).

    Rule:
    - If a class name contains spaces, find the nearest capital letter before the
      first space and split there.
    - Example:
      "StartupDialogServes as ... " -> ("StartupDialog", "Serves as ...")
    """
    if " " not in name:
        return None

    first_space = name.find(" ")
    split_idx: int | None = None
    for i in range(first_space - 1, 0, -1):
        if name[i].isupper():
            split_idx = i
            break

    if split_idx is None:
        # Fallback: split at first space if no internal capital was found.
        split_idx = first_space

    class_name = name[:split_idx].strip()
    doc_fragment = name[split_idx:].strip()
    if not class_name or not doc_fragment:
        return None
    return class_name, doc_fragment


def rewrite_class_repr(repr_value: str, old_name: str, new_name: str) -> str:
    """Rewrite class repr leaf name: <class 'Pkg.Old'> -> <class 'Pkg.New'>."""
    marker = f".{old_name}'>"
    if marker in repr_value:
        return repr_value.replace(marker, f".{new_name}'>")
    return repr_value


def _replace_text(text: str, replacements: dict[str, str]) -> str:
    """Apply a set of literal replacements to one string."""
    updated = text
    for old, new in replacements.items():
        updated = updated.replace(old, new)
    return updated


def _rewrite_raw_docs(node: Any, replacements: dict[str, str]) -> Any:
    """Apply token replacements to all raw_doc fields in the tree."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "raw_doc" and isinstance(v, str):
                out[k] = _replace_text(v, replacements)
            else:
                out[k] = _rewrite_raw_docs(v, replacements)
        return out
    if isinstance(node, list):
        return [_rewrite_raw_docs(v, replacements) for v in node]
    return node


def _trim_blank_edges(lines: list[str]) -> list[str]:
    """Trim only leading/trailing blank lines, preserving internal spacing."""
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def _clean_description(lines: list[str]) -> str | None:
    """Trim excess whitespace from description lines while preserving paragraphs."""
    trimmed = _trim_blank_edges(lines)
    if not trimmed:
        return None

    cleaned: list[str] = []
    prev_blank = False
    for line in trimmed:
        stripped = line.strip()
        if not stripped:
            if cleaned and not prev_blank:
                cleaned.append("")
            prev_blank = True
            continue

        # Collapse repeated spaces/tabs inside a line.
        normalized = " ".join(stripped.split())
        cleaned.append(normalized)
        prev_blank = False

    if not cleaned:
        return None

    return "\n".join(cleaned)


def _parse_function_raw_doc(raw_doc: str) -> dict[str, str | None] | None:
    """Extract signature/description/cpp_signature from a function raw_doc.

    Parsing rules:
    - Split on newlines, then trim leading/trailing blank lines.
    - signature: first line containing '->'
    - description: all lines between signature and 'C++ signature :'
      (or until end if C++ marker is absent), with only outer blank lines trimmed.
    - cpp_signature: first non-empty line after 'C++ signature :', else None.
    """
    lines = _trim_blank_edges(raw_doc.split("\n"))
    if not lines:
        return None

    sig_idx: int | None = None
    for i, line in enumerate(lines):
        if "->" in line:
            sig_idx = i
            break
    if sig_idx is None:
        return None

    signature = lines[sig_idx].strip()

    cpp_idx: int | None = None
    for i in range(sig_idx + 1, len(lines)):
        if lines[i].strip() == "C++ signature :":
            cpp_idx = i
            break

    if cpp_idx is None:
        description = _clean_description(lines[sig_idx + 1 :])
        return {
            "signature": signature,
            "description": description,
            "cpp_signature": None,
        }

    description = _clean_description(lines[sig_idx + 1 : cpp_idx])

    cpp_signature: str | None = None
    for line in lines[cpp_idx + 1 :]:
        if line.strip():
            cpp_signature = line.strip()
            break

    return {
        "signature": signature,
        "description": description,
        "cpp_signature": cpp_signature,
    }


def _annotate_function_docs(node: Any) -> tuple[Any, int]:
    """Parse function raw_doc blocks into structured fields."""
    parsed_count = 0
    function_like_types = {
        "function",
        "builtin_function_or_method",
        "method",
        "method_descriptor",
    }

    if isinstance(node, dict):
        node_type = node.get("type")
        raw_doc = node.get("raw_doc")
        if node_type in function_like_types and isinstance(raw_doc, str):
            parsed = _parse_function_raw_doc(raw_doc)
            if parsed is not None:
                node.update(parsed)
                parsed_count += 1

        for key, value in list(node.items()):
            normalized, child_count = _annotate_function_docs(value)
            node[key] = normalized
            parsed_count += child_count
        return node, parsed_count

    if isinstance(node, list):
        out = []
        for item in node:
            normalized, child_count = _annotate_function_docs(item)
            out.append(normalized)
            parsed_count += child_count
        return out, parsed_count

    return node, 0


def normalize_tree(node: Any, replacements: dict[str, str]) -> tuple[Any, int]:
    """Normalize malformed class names and dependent strings in-place shape."""
    fixed = 0

    if isinstance(node, dict):
        is_class = node.get("type") == "class"
        class_name = node.get("name")
        if is_class and isinstance(class_name, str):
            split = split_joined_class_name(class_name)
            if split is not None:
                new_name, doc_fragment = split
                old_name = class_name

                node["name"] = new_name

                existing_doc = node.get("raw_doc")
                if isinstance(existing_doc, str) and existing_doc.strip():
                    node["raw_doc"] = f"{doc_fragment} {existing_doc}".strip()
                else:
                    node["raw_doc"] = doc_fragment

                repr_value = node.get("repr")
                if isinstance(repr_value, str):
                    node["repr"] = rewrite_class_repr(repr_value, old_name, new_name)

                replacements[old_name] = new_name

                fixed += 1

        for key, value in list(node.items()):
            normalized, child_fixed = normalize_tree(value, replacements)
            node[key] = normalized
            fixed += child_fixed
        return node, fixed

    if isinstance(node, list):
        out = []
        for item in node:
            normalized, child_fixed = normalize_tree(item, replacements)
            out.append(normalized)
            fixed += child_fixed
        return out, fixed

    return node, 0


def parse_live_raw(data: dict[str, Any]) -> tuple[dict[str, Any], int, int]:
    """Apply all parsing/normalization passes.

    Returns (parsed_data, malformed_class_fixes, parsed_function_docs).
    """
    replacements: dict[str, str] = {}
    parsed, fixed = normalize_tree(data, replacements)
    if replacements:
        parsed = _rewrite_raw_docs(parsed, replacements)
    parsed, parsed_docs = _annotate_function_docs(parsed)
    return parsed, fixed, parsed_docs


def resolve_paths(input_arg: str, output_arg: str | None) -> tuple[Path, Path]:
    """Resolve input/output paths for either a build dir or a LiveTree.raw.json file."""
    input_path = Path(input_arg).expanduser().resolve()

    if input_path.is_dir():
        raw_path = input_path / "LiveTree.raw.json"
        out_path = Path(output_arg).expanduser().resolve() if output_arg else input_path / "LiveTree.parsed.json"
    else:
        raw_path = input_path
        out_path = (
            Path(output_arg).expanduser().resolve()
            if output_arg
            else raw_path.with_name("LiveTree.parsed.json")
        )

    return raw_path, out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse and normalize LiveTree.raw.json")
    parser.add_argument(
        "input",
        help="Path to build directory containing LiveTree.raw.json, or path to LiveTree.raw.json",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output path for parsed JSON (default: alongside input as LiveTree.parsed.json)",
    )
    args = parser.parse_args()

    raw_path, out_path = resolve_paths(args.input, args.output)
    if not raw_path.exists():
        raise SystemExit(f"Input file not found: {raw_path}")

    with open(raw_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    parsed, fixed_count, parsed_doc_count = parse_live_raw(data)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(
        f"Wrote parsed JSON: {out_path} "
        f"(fixed {fixed_count} malformed class name(s), parsed {parsed_doc_count} function raw_doc(s))"
    )


if __name__ == "__main__":
    main()

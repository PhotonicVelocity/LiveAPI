"""
Post-process Live.json to add cpp_type fields to method args.

Parses the cpp_signature for each method/built-in and maps positional C++ arg
types back onto the args list extracted from the Boost.Python docstring.

Usage:
    python tools/enrich_cpp_types.py build/12.3.6/Live.json
"""

import json
import re
import sys


def parse_cpp_args(cpp_sig: str) -> list[dict]:
    """Extract C++ arg types and optionality from a cpp_signature string.

    Returns a list of dicts with keys: cpp_type, optional.

    Examples:
        "void add_listener(TPyHandle<ASong>,boost::python::api::object)"
        -> [{"cpp_type": "TPyHandle<ASong>", "optional": False},
            {"cpp_type": "boost::python::api::object", "optional": False}]

        "TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])"
        -> [{"cpp_type": "TPyHandle<ASong>", "optional": False},
            {"cpp_type": "boost::python::api::object", "optional": True}]
    """
    # Extract the args portion between the outermost parens after the function name
    match = re.search(r"\w+\((.+)\)\s*$", cpp_sig)
    if not match:
        return []

    args_str = match.group(1)

    # Track which character positions are inside [...] brackets (optional args)
    in_optional = False
    optional_mask: list[bool] = []
    for ch in args_str:
        if ch == "[":
            in_optional = True
        elif ch == "]":
            in_optional = False
        optional_mask.append(in_optional)

    # Remove brackets for parsing
    args_str_clean = args_str.replace("[", "").replace("]", "")

    # Split on commas, respecting template angle brackets.
    # Track original position to determine optionality.
    args: list[str] = []
    arg_optional: list[bool] = []
    depth = 0
    current = ""
    orig_pos = 0  # position in original args_str (with brackets)
    clean_pos = 0  # position in cleaned string
    current_is_optional = False

    for ch in args_str:
        if ch in "[]":
            orig_pos += 1
            continue
        if ch == "<":
            depth += 1
            current += ch
        elif ch == ">":
            depth -= 1
            current += ch
        elif ch == "," and depth == 0:
            current = current.strip()
            if current:
                args.append(current)
                arg_optional.append(current_is_optional)
            current = ""
            current_is_optional = optional_mask[orig_pos]
        else:
            if not current.strip():
                # First non-whitespace char of this arg — check optionality
                if ch.strip():
                    current_is_optional = optional_mask[orig_pos]
            current += ch
        orig_pos += 1

    current = current.strip()
    if current:
        args.append(current)
        arg_optional.append(current_is_optional)

    # Clean each arg: strip default values and build result
    result: list[dict] = []
    for i, arg in enumerate(args):
        arg = re.sub(r"=\S*$", "", arg).strip()
        result.append({"cpp_type": arg, "optional": arg_optional[i]})

    return result


def is_self_type(cpp_type: str) -> bool:
    """Check if a C++ type is a self/handle type (first arg, not exposed to Python)."""
    return cpp_type.startswith("TPyHandle<") or cpp_type.startswith("TPyViewData<")


def enrich(data: dict) -> int:
    """Add cpp_type and optional to args in-place. Returns count of enriched args."""
    count = 0
    for el in data["elements"]:
        cpp_sig = el.get("cpp_signature")
        args = el.get("args")
        if not cpp_sig or not args:
            continue

        cpp_args = parse_cpp_args(cpp_sig)
        if not cpp_args:
            continue

        # Skip the self/handle arg (first C++ arg)
        if cpp_args and is_self_type(cpp_args[0]["cpp_type"]):
            cpp_args = cpp_args[1:]

        # Map remaining C++ types onto Python args
        for i, arg in enumerate(args):
            if i < len(cpp_args):
                arg["cpp_type"] = cpp_args[i]["cpp_type"]
                if cpp_args[i]["optional"]:
                    arg["optional"] = True
                count += 1

    return count


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <Live.json>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    count = enrich(data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Enriched {count} args with cpp_type in {path}")


if __name__ == "__main__":
    main()

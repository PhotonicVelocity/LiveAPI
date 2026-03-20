"""
Parse and enrich APICapture results into a single normalized tree.

Takes the raw capture outputs (LiveTree.raw.json and LiveClasses.json) and runs a pipeline of transform steps to
produce LiveTree.parsed.json — a cleaned-up tree with probe data merged in.

Pipeline steps:
1. fix_malformed_class_names — split Boost.Python's concatenated class name/doc strings
2. rewrite_raw_docs — propagate class name fixes into raw_doc text throughout the tree
3a. resolve_inheritance — expand bases into full ancestor chains on class nodes
3b. relocate_inherited_members — move inherited members to their true defining class
4. parse_enums — parse string-encoded enum names/values into structured members, retype as "enum"
5a. parse_function_docs — extract signature, description, and C++ signature from function docstrings
5b. parse_signatures — split Python and C++ signatures into matched args and return types
5c. build_type_map — build C++ → Python type mapping from signature pairs (stored in ctx, no tree changes)
5d. resolve_signatures — resolve raw signature parts into clean structured args and returns
6. merge_probe_data — merge runtime probe results (LiveClasses.json) onto matching tree nodes

Usage:
    python tools/parse/parse_apicapture_results.py 12.3.6
    python tools/parse/parse_apicapture_results.py 12.3
    python tools/parse/parse_apicapture_results.py 12.3.6 --output /tmp/LiveTree.parsed.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

# Type alias for pipeline steps. Each step receives the tree and a shared context dict, and returns the transformed
# tree. Steps communicate via ctx (e.g. storing replacements, probe data, stats counters).
TreeNode = dict[str, Any] | list[Any] | Any
PipelineStep = Any  # Callable[[TreeNode, dict[str, Any]], TreeNode] — can't express cleanly without typing_extensions


# ------------------------------------------------------------------------------- #
# Helpers
# ------------------------------------------------------------------------------- #

_REPR_NAME_RE = re.compile(r"<class '(?:\w+\.)?(\w+)'>")


def _ancestor_names(ancestors: list[str]) -> list[str]:
    """Extract class names from repr-format ancestor strings.

    E.g. ["<class 'Device'>", "<class 'LomObject'>"] -> ["Device", "LomObject"]
    """
    names = []
    for a in ancestors:
        m = _REPR_NAME_RE.match(a)
        if m:
            names.append(m.group(1))
    return names


class ClassContext:
    """Tracks the current class context during tree walks."""

    __slots__ = ("name", "path", "ancestors", "child_classes", "siblings")

    def __init__(
        self,
        name: str | None = None,
        path: str | None = None,
        ancestors: list[str] | None = None,
        child_classes: frozenset[str] | None = None,
        siblings: frozenset[str] | None = None,
    ):
        self.name = name
        self.path = path
        self.ancestors = ancestors or []
        self.child_classes = child_classes or frozenset()
        self.siblings = siblings or frozenset()


_NO_CLASS = ClassContext()


def _walk_tree(
    node: TreeNode,
    visitor: Any,
    ctx: dict[str, Any],
    parent: ClassContext = _NO_CLASS,
) -> TreeNode:
    """Depth-first tree walk that calls visitor(node, ctx, parent) on every dict node.

    The visitor may mutate the node in place. Non-dict nodes are passed through unchanged.
    parent is a ClassContext with name, path (dot-separated nesting), and ancestors (name strings).
    Properly scoped so nested classes don't corrupt the context for sibling nodes.
    """
    if isinstance(node, dict):
        visitor(node, ctx, parent)
        current = parent
        node_type = node.get("type")
        if node_type in ("class", "module"):
            # Collect child class names so children can see their siblings via parent.child_classes
            child_classes: frozenset[str] = frozenset(
                c["name"]
                for c in node.get("children", [])
                if isinstance(c, dict) and c.get("type") in ("class", "enum") and not c.get("ref") and c.get("name")
            )
            if node_type == "class":
                name = node.get("name")
                path = f"{parent.path}.{name}" if parent.path else name
                current = ClassContext(
                    name, path, _ancestor_names(node.get("ancestors", [])), child_classes, parent.child_classes
                )
            else:
                # Module: propagate child_classes so nested classes get siblings, but don't create a class context
                current = ClassContext(child_classes=child_classes)
        for key, value in list(node.items()):
            node[key] = _walk_tree(value, visitor, ctx, current)
        return node
    if isinstance(node, list):
        return [_walk_tree(item, visitor, ctx, parent) for item in node]
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
        cleaned.append(" ".join(stripped.split()))
        prev_blank = False

    return "\n".join(cleaned) if cleaned else None


# ------------------------------------------------------------------------------- #
# Step 1: fix_malformed_class_names
# ------------------------------------------------------------------------------- #


def _split_joined_class_name(name: str) -> tuple[str, str] | None:
    """Split a malformed class name into (class_name, doc_fragment).

    Boost.Python sometimes concatenates the class name with its docstring when the class name contains spaces.
    We find the nearest capital letter before the first space and split there.

    Example: "StartupDialogServes as ..." -> ("StartupDialog", "Serves as ...")
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
        split_idx = first_space

    class_name = name[:split_idx].strip()
    doc_fragment = name[split_idx:].strip()
    if not class_name or not doc_fragment:
        return None
    return class_name, doc_fragment


def _visit_fix_class_names(node: dict[str, Any], ctx: dict[str, Any], _parent: ClassContext) -> None:
    """Visitor: fix malformed class names, stash replacements in ctx."""
    if node.get("type") != "class":
        return
    class_name = node.get("name")
    if not isinstance(class_name, str):
        return

    split = _split_joined_class_name(class_name)
    if split is None:
        return

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
        marker = f".{old_name}'>"
        if marker in repr_value:
            node["repr"] = repr_value.replace(marker, f".{new_name}'>")

    ctx.setdefault("replacements", {})[old_name] = new_name
    ctx["stats"]["malformed_class_names"] = ctx["stats"].get("malformed_class_names", 0) + 1


def fix_malformed_class_names(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Split Boost.Python's concatenated class name/doc strings."""
    return _walk_tree(tree, _visit_fix_class_names, ctx)


# ------------------------------------------------------------------------------- #
# Step 2: rewrite_raw_docs
# ------------------------------------------------------------------------------- #


def _visit_rewrite_raw_docs(node: dict[str, Any], ctx: dict[str, Any], _parent: ClassContext) -> None:
    """Visitor: apply class name replacements to raw_doc fields."""
    replacements = ctx.get("replacements", {})
    if not replacements:
        return
    raw_doc = node.get("raw_doc")
    if not isinstance(raw_doc, str):
        return
    for old, new in replacements.items():
        raw_doc = raw_doc.replace(old, new)
    node["raw_doc"] = raw_doc


def rewrite_raw_docs(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Propagate class name fixes into raw_doc text throughout the tree."""
    if not ctx.get("replacements"):
        return tree
    return _walk_tree(tree, _visit_rewrite_raw_docs, ctx)


# ------------------------------------------------------------------------------- #
# Step 3: resolve_inheritance
# ------------------------------------------------------------------------------- #


def resolve_inheritance(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Collect bases from class nodes and expand into full ancestor chains.

    Keyed by repr to avoid name collisions (e.g. multiple classes named "View").
    Bases in the raw capture are stored as reprs (e.g. "<class 'Device.View'>").

    Pass 1: walk the tree to build a repr → bases mapping.
    Pass 2: for each class with bases, compute the full ancestor chain and store it on the node.
    """
    # Pass 1: collect direct bases for every class, keyed by repr
    class_bases: dict[str, list[str]] = {}

    def _collect_bases(node: TreeNode) -> None:
        if isinstance(node, dict):
            if node.get("type") in ("class", "enum", "type") and not node.get("ref"):
                bases = node.get("bases")
                r = node.get("repr")
                if bases and r:
                    class_bases[r] = bases
            for value in node.values():
                _collect_bases(value)
        elif isinstance(node, list):
            for item in node:
                _collect_bases(item)

    _collect_bases(tree)

    # Build full ancestor chains (walk bases transitively)
    def _get_ancestors(r: str, seen: set[str] | None = None) -> list[str]:
        if seen is None:
            seen = set()
        if r in seen:
            return []
        seen.add(r)
        bases = class_bases.get(r, [])
        ancestors = list(bases)
        for base in bases:
            ancestors.extend(_get_ancestors(base, seen))
        return ancestors

    ancestor_map: dict[str, list[str]] = {}
    for r in class_bases:
        chain = _get_ancestors(r)
        if chain:
            ancestor_map[r] = chain

    # Pass 2: replace bases with full ancestor chain on class nodes, keeping children last
    def _stamp_ancestors(node: TreeNode) -> None:
        if isinstance(node, dict):
            if node.get("type") in ("class", "enum", "type"):
                r = node.get("repr")
                node.pop("bases", None)
                saved_children = node.pop("children", None)
                if r and r in ancestor_map:
                    node["ancestors"] = ancestor_map[r]
                if saved_children is not None:
                    node["children"] = saved_children
            for value in node.values():
                _stamp_ancestors(value)
        elif isinstance(node, list):
            for item in node:
                _stamp_ancestors(item)

    _stamp_ancestors(tree)

    ctx["stats"]["classes_with_ancestors"] = len(ancestor_map)
    return tree


# ------------------------------------------------------------------------------- #
# Step 3b: relocate_inherited_members
# ------------------------------------------------------------------------------- #


def relocate_inherited_members(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Move inherited members to their true defining class based on ancestry.

    When CaptureModule walks classes, the first class encountered gets the full definition
    and all subsequent classes with the same member get a ref. This doesn't respect inheritance —
    e.g. Device.View might end up as a ref pointing to CcControlDevice.View.

    This step fixes that by finding, for each shared member id, the class highest in the
    hierarchy (the one that's an ancestor of all others) and moving the full definition there.
    """
    # Pass 1: collect member id → [(class_repr, class_ancestors, member_node, parent_children_list)]
    member_locations: dict[int, list[tuple[str, list[str], dict, list]]] = {}

    def _collect(node: TreeNode) -> None:
        if isinstance(node, dict):
            if node.get("type") == "class" and node.get("children"):
                class_repr = node.get("repr", "")
                class_ancestors = node.get("ancestors", [])
                children = node["children"]
                for child in children:
                    if isinstance(child, dict) and "id" in child:
                        mid = child["id"]
                        member_locations.setdefault(mid, []).append(
                            (class_repr, class_ancestors, child, children)
                        )
            for value in node.values():
                _collect(value)
        elif isinstance(node, list):
            for item in node:
                _collect(item)

    _collect(tree)

    # Pass 2: for each member shared across multiple classes, find the true owner
    relocated = 0
    for mid, locations in member_locations.items():
        if len(locations) < 2:
            continue

        # Find the original (non-ref) definition
        original_idx = None
        for i, (cr, _, node, _) in enumerate(locations):
            if not node.get("ref"):
                original_idx = i
                break
        if original_idx is None:
            continue

        # Find the true owner: the class whose repr appears in the ancestors of all other classes
        true_owner_idx = None
        for i, (cr, _, node, _) in enumerate(locations):
            others_descend = all(
                cr in locations[j][1]  # cr in other's ancestors
                for j in range(len(locations))
                if j != i
            )
            if others_descend:
                true_owner_idx = i
                break

        if true_owner_idx is None or true_owner_idx == original_idx:
            continue

        # Swap: move full definition to true owner, make original a ref
        _, _, orig_node, orig_children = locations[original_idx]
        _, _, owner_node, owner_children = locations[true_owner_idx]

        # Build the full definition for the true owner's slot
        full_def = {k: v for k, v in orig_node.items() if k != "ref"}
        # Build a ref for the original's slot
        ref_node = {"name": orig_node["name"], "type": orig_node["type"], "id": mid, "ref": True}
        if "repr" in orig_node:
            ref_node["repr"] = orig_node["repr"]

        # Replace in-place in the children lists
        for i, child in enumerate(orig_children):
            if child is orig_node:
                orig_children[i] = ref_node
                break
        for i, child in enumerate(owner_children):
            if child is owner_node:
                owner_children[i] = full_def
                break

        relocated += 1

    ctx["stats"]["relocated_members"] = relocated
    return tree


# ------------------------------------------------------------------------------- #
# Step 4: parse_enums
# ------------------------------------------------------------------------------- #

# Matches entries like "0: Module.Enum.member_name" in the string-encoded values dict.
_ENUM_VALUE_RE = re.compile(r"(-?\d+)\s*:\s*\S+\.(\w+)")


def _parse_enum_values(values_str: str) -> dict[str, int] | None:
    """Parse the string-encoded values dict into {member_name: int_value}.

    Input format: "{0: Module.Enum.up, 1: Module.Enum.down, ...}"
    Output: {"up": 0, "down": 1, ...}
    """
    matches = _ENUM_VALUE_RE.findall(values_str)
    if not matches:
        return None
    return {name: int(val) for val, name in matches}


def _visit_parse_enums(node: dict[str, Any], ctx: dict[str, Any], _parent: ClassContext) -> None:
    """Visitor: parse type nodes with valid names/values into enum nodes."""
    if node.get("type") != "type":
        return
    values_str = node.get("values")
    if not isinstance(values_str, str) or values_str == "None":
        return

    members = _parse_enum_values(values_str)
    if members is None:
        return

    node["type"] = "enum"
    node["members"] = members
    del node["names"]
    del node["values"]
    ctx["stats"]["parsed_enums"] = ctx["stats"].get("parsed_enums", 0) + 1


def parse_enums(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Parse string-encoded enum names/values into structured members, retype as 'enum'."""
    return _walk_tree(tree, _visit_parse_enums, ctx)


# ------------------------------------------------------------------------------- #
# Step 5a: parse_function_docs
# ------------------------------------------------------------------------------- #

_FUNCTION_TYPES = {"function", "builtin_function_or_method", "method", "method_descriptor"}


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
        return {
            "signature": signature,
            "description": _clean_description(lines[sig_idx + 1 :]),
            "cpp_signature": None,
        }

    cpp_signature: str | None = None
    for line in lines[cpp_idx + 1 :]:
        if line.strip():
            cpp_signature = line.strip()
            break

    return {
        "signature": signature,
        "description": _clean_description(lines[sig_idx + 1 : cpp_idx]),
        "cpp_signature": cpp_signature,
    }


def _visit_parse_function_docs(node: dict[str, Any], ctx: dict[str, Any], _parent: ClassContext) -> None:
    """Visitor: parse function docstrings into structured fields."""
    if node.get("type") not in _FUNCTION_TYPES:
        return
    raw_doc = node.get("raw_doc")
    if not isinstance(raw_doc, str):
        return
    parsed = _parse_function_raw_doc(raw_doc)
    if parsed is not None:
        node.update(parsed)
        ctx["stats"]["parsed_function_docs"] = ctx["stats"].get("parsed_function_docs", 0) + 1


def parse_function_docs(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Extract signature, description, and C++ signature from function docstrings."""
    return _walk_tree(tree, _visit_parse_function_docs, ctx)


# ------------------------------------------------------------------------------- #
# Step 5b: parse_signatures
# ------------------------------------------------------------------------------- #


def _split_sig_args(arg_str: str) -> list[tuple[str, int]]:
    """Split a signature's argument string into (arg_text, bracket_depth) tuples.

    Tracks bracket nesting so optional args carry their depth.
    Example: "(Application)arg1, (Text)text [, (int)buttons=OK [, (bool)markup=False]]"
    → [("(Application)arg1", 0), ("(Text)text", 0), ("(int)buttons=OK", 1), ("(bool)markup=False", 2)]
    """
    arg_str = arg_str.strip()
    if not arg_str:
        return []

    args: list[tuple[str, int]] = []
    current: list[str] = []
    depth = 0
    arg_depth = 0  # depth when this arg started

    for ch in arg_str:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch == ",":
            arg = "".join(current).strip()
            if arg:
                args.append((arg, arg_depth))
            current = []
            arg_depth = depth  # next arg starts at current depth
        else:
            if not current:
                arg_depth = depth  # record depth at start of arg text
            current.append(ch)

    last = "".join(current).strip()
    if last:
        args.append((last, arg_depth))

    return args


def _extract_py_sig_parts(signature: str) -> tuple[list[tuple[str, int]], str] | None:
    """Extract argument (text, depth) tuples and return type from a Python signature.

    Input:  "name( (Type)arg1, (Type)arg2 [, (Type)arg3=default]) -> ReturnType :"
    Output: ([("(Type)arg1", 0), ("(Type)arg2", 0), ("(Type)arg3=default", 1)], "ReturnType")
    """
    # Split on " -> " to get args and return
    arrow_idx = signature.find(" -> ")
    if arrow_idx == -1:
        return None

    left = signature[:arrow_idx]
    returns = signature[arrow_idx + 4 :].rstrip(" :").strip()

    # Extract the content between the outermost parens after the function name
    paren_start = left.find("(")
    if paren_start == -1:
        return [], returns

    # Find the matching close paren (last one)
    paren_end = left.rfind(")")
    if paren_end == -1:
        return None

    # The full left side is: "func_name( (Type)arg1, ...)"
    # Extract the inner content between the outermost parens
    inner = left[paren_start + 1 : paren_end].strip()

    args = _split_sig_args(inner)
    return args, returns


def _extract_cpp_sig_parts(cpp_signature: str) -> tuple[list[tuple[str, int]], str] | None:
    """Extract argument (text, depth) tuples and return type from a C++ signature.

    Input:  "int show_message(TPyHandle<ASongApp>,TText [,int=OK [,bool=False]])"
    Output: ([("TPyHandle<ASongApp>", 0), ("TText", 0), ("int=OK", 1), ("bool=False", 2)], "int")

    C++ return type is everything before the function name. The function name is the last identifier before "(".
    """
    # Find the outermost arg parens. We need to find "(" that isn't inside "<...>"
    # Strategy: find the first "(" that isn't preceded by an unmatched "<"
    paren_start = None
    angle_depth = 0
    for i, ch in enumerate(cpp_signature):
        if ch == "<":
            angle_depth += 1
        elif ch == ">":
            angle_depth -= 1
        elif ch == "(" and angle_depth == 0:
            paren_start = i
            break

    if paren_start is None:
        return None

    # Return type + function name is everything before the paren
    prefix = cpp_signature[:paren_start].strip()

    # Find matching close paren from the end
    paren_end = cpp_signature.rfind(")")
    if paren_end == -1:
        return None

    args_inner = cpp_signature[paren_start + 1 : paren_end].strip()

    # Split return type from function name: return type is everything before the last whitespace-separated token
    # E.g. "std::__1::vector<...> available_main_views" → return="std::__1::vector<...>", name="available_main_views"
    # Find the last space that isn't inside angle brackets
    last_space = None
    angle_depth = 0
    for i, ch in enumerate(prefix):
        if ch == "<":
            angle_depth += 1
        elif ch == ">":
            angle_depth -= 1
        elif ch == " " and angle_depth == 0:
            last_space = i

    if last_space is not None:
        returns = prefix[:last_space].strip()
    else:
        returns = ""

    # Split args on commas, respecting angle brackets and square brackets
    args = _split_cpp_args(args_inner) if args_inner else []
    return args, returns


def _split_cpp_args(args_str: str) -> list[tuple[str, int]]:
    """Split C++ args on commas, respecting <> nesting. Tracks [] bracket depth."""
    args: list[tuple[str, int]] = []
    current: list[str] = []
    angle_depth = 0
    bracket_depth = 0
    arg_depth = 0  # depth when this arg started

    for ch in args_str:
        if ch == "[":
            bracket_depth += 1
        elif ch == "]":
            bracket_depth -= 1
        elif ch == "<":
            angle_depth += 1
            current.append(ch)
        elif ch == ">":
            angle_depth -= 1
            current.append(ch)
        elif ch == "," and angle_depth == 0:
            arg = "".join(current).strip()
            if arg:
                args.append((arg, arg_depth))
            current = []
            arg_depth = bracket_depth  # next arg starts at current depth
        else:
            if not current:
                arg_depth = bracket_depth
            current.append(ch)

    last = "".join(current).strip()
    if last:
        args.append((last, arg_depth))

    return args


_VECTOR_PREFIX = "std::__1::vector<"


def _extract_vector_element_type(cpp_self: str) -> str | None:
    """Extract the element type from a C++ vector self arg.

    Input:  "std::__1::vector<TControlDescription, std::__1::allocator<TControlDescription>> {lvalue}"
    Output: "TControlDescription"
    """
    cleaned = re.sub(r"\s*\{lvalue\}", "", cpp_self).strip()
    if not cleaned.startswith(_VECTOR_PREFIX):
        return None
    inner = cleaned[len(_VECTOR_PREFIX) :]
    # Find the first comma at angle depth 0 — everything before it is the element type
    depth = 0
    for i, ch in enumerate(inner):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif ch == "," and depth == 0:
            return inner[:i].strip()
    return None


def _visit_parse_signatures(node: dict[str, Any], ctx: dict[str, Any], parent: ClassContext) -> None:
    """Visitor: parse Python and C++ signatures into matched args and returns."""
    if node.get("type") not in _FUNCTION_TYPES:
        return
    signature = node.get("signature")
    if not isinstance(signature, str):
        return

    py_parts = _extract_py_sig_parts(signature)
    if py_parts is None:
        return

    py_args, py_returns = py_parts

    cpp_signature = node.get("cpp_signature")
    cpp_parts = _extract_cpp_sig_parts(cpp_signature) if isinstance(cpp_signature, str) else None
    cpp_args, cpp_returns = cpp_parts if cpp_parts else ([], None)

    # Zip args together, padding the shorter list. Use bracket depth from Python sig (primary), fall back to C++.
    max_len = max(len(py_args), len(cpp_args))
    args: list[dict[str, Any]] = []
    for i in range(max_len):
        py_text, py_depth = py_args[i] if i < len(py_args) else (None, 0)
        cpp_text, cpp_depth = cpp_args[i] if i < len(cpp_args) else (None, 0)
        depth = py_depth if py_text is not None else cpp_depth
        args.append({"python": py_text, "cpp": cpp_text, "optional": depth})

    node["args"] = args
    node["returns"] = {"python": py_returns, "cpp": cpp_returns}
    ctx["stats"]["parsed_signatures"] = ctx["stats"].get("parsed_signatures", 0) + 1

    # Vector element type extraction: if the first C++ arg is a std::vector, extract the element type
    # and replace boost::python::api::object in subsequent C++ args with it.
    vector_element_cpp: str | None = None
    if cpp_args:
        first_cpp = cpp_args[0][0] if cpp_args[0] else None
        if first_cpp:
            vector_element_cpp = _extract_vector_element_type(first_cpp)
    if vector_element_cpp:
        for a in args[1:]:
            cpp_text = a.get("cpp")
            if cpp_text and re.sub(r"\s*\{lvalue\}", "", cpp_text).strip() == "boost::python::api::object":
                a["cpp"] = vector_element_cpp

    # Collect py↔cpp type pairs for the type map
    type_pairs = ctx.setdefault("type_pairs", [])
    for a in args:
        py_raw, cpp_raw = a.get("python"), a.get("cpp")
        if py_raw and cpp_raw:
            py_type = re.match(r"\((\w+)\)", py_raw)
            cpp_clean = re.sub(r"\s*=.*$", "", cpp_raw)
            cpp_clean = re.sub(r"\s*\{lvalue\}", "", cpp_clean).strip()
            if py_type and cpp_clean:
                type_pairs.append(("arg", py_type.group(1), cpp_clean, parent.path))
    if py_returns and cpp_returns:
        type_pairs.append(("return", py_returns, cpp_returns, parent.path))

    # Emit vector element type pair: map C++ element type → sibling Python class.
    # Strip namespace prefix, then strip leading "T", and check against siblings.
    if vector_element_cpp:
        cpp_core = _unwrap_cpp_type(vector_element_cpp)
        candidate = cpp_core.rsplit("::", 1)[-1]
        if candidate.startswith("T"):
            candidate = candidate[1:]
        if candidate in parent.siblings:
            type_pairs.append(("element", candidate, vector_element_cpp, parent.path))


def parse_signatures(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Split Python and C++ signatures into matched args and return types."""
    return _walk_tree(tree, _visit_parse_signatures, ctx)


# ------------------------------------------------------------------------------- #
# Step 5c: build_type_map
# ------------------------------------------------------------------------------- #

# Known C++ → Python primitive mappings that don't need signature evidence.
_CPP_PRIMITIVES: dict[str, str] = {
    "int": "int",
    "unsigned int": "int",
    "unsigned long long": "int",
    "long": "int",
    "float": "float",
    "double": "float",
    "bool": "bool",
    "void": "None",
    "TString": "str",
    "std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>": "str",
    "boost::python::api::object": "object",
    "boost::python::tuple": "tuple",
    "boost::python::list": "list",
    "boost::python::dict": "dict",
}


def _unwrap_cpp_type(cpp_type: str) -> str:
    """Strip TWeakPtr<> and TPyHandle<> wrappers to get the core C++ type."""
    t = cpp_type.strip()
    while t.startswith("TWeakPtr<") and t.endswith(">"):
        t = t[len("TWeakPtr<") : -1]
    while t.startswith("TPyHandle<") and t.endswith(">"):
        t = t[len("TPyHandle<") : -1]
    return t


def _find_class_name_collisions(tree: TreeNode) -> set[str]:
    """Find class names that refer to multiple distinct classes in the tree.

    Walks the tree and collects class name → set of reprs. Names with 2+ distinct reprs
    are truly ambiguous (e.g. "View" is Device.View, Clip.View, etc.).
    """
    name_reprs: dict[str, set[str]] = {}

    def _collect(node: TreeNode) -> None:
        if isinstance(node, dict):
            if node.get("type") == "class" and not node.get("ref"):
                name = node.get("name")
                r = node.get("repr")
                if name and r:
                    name_reprs.setdefault(name, set()).add(r)
            for value in node.values():
                _collect(value)
        elif isinstance(node, list):
            for item in node:
                _collect(item)

    _collect(tree)
    return {name for name, reprs in name_reprs.items() if len(reprs) > 1}


def build_type_map(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Build a C++ → Python type mapping from collected signature pairs.

    Stored in ctx["cpp_to_py"] for use by later steps. Does not modify the tree.
    When a Python type name is ambiguous (same name refers to genuinely different classes,
    e.g. "View" exists as Device.View, Clip.View, etc.), it's qualified with its parent path.
    """
    cpp_to_py: dict[str, str] = dict(_CPP_PRIMITIVES)

    # Only qualify types where the same name refers to genuinely different classes in the tree
    ambiguous = _find_class_name_collisions(tree)

    for _, py_type, cpp_type, parent_path in ctx.get("type_pairs", []):
        if py_type == "object":
            continue
        # Qualify ambiguous types using the parent class path
        if py_type in ambiguous and parent_path:
            # If the path already ends with the type name (self arg), use the path as-is
            if parent_path.endswith(f".{py_type}") or parent_path == py_type:
                qualified = parent_path
            else:
                qualified = f"{parent_path}.{py_type}"
        else:
            qualified = py_type
        if cpp_type not in cpp_to_py:
            cpp_to_py[cpp_type] = qualified
        core = _unwrap_cpp_type(cpp_type)
        if core != cpp_type and core not in cpp_to_py:
            cpp_to_py[core] = qualified

    ctx["cpp_to_py"] = cpp_to_py
    ctx["stats"]["type_map_entries"] = len(cpp_to_py)
    return tree


# ------------------------------------------------------------------------------- #
# Step 5d: resolve_signatures
# ------------------------------------------------------------------------------- #

# Regex to parse Python arg text: "(Type)name" or "(Type)name=default"
_PY_ARG_RE = re.compile(r"^\((\w+)\)(\w+)(?:=(.+))?$")


_PASCAL_RE = re.compile(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")


def _pascal_to_snake(name: str) -> str:
    """Convert PascalCase arg names to snake_case. Leaves already-lowercase names unchanged."""
    return _PASCAL_RE.sub("_", name).lower()


def _resolve_type(py_type: str, cpp_raw: str | None, cpp_to_py: dict[str, str]) -> str:
    """Resolve a Python type, using the C++ type map for 'object' types."""
    if py_type != "object" or not cpp_raw:
        return py_type
    cpp_clean = re.sub(r"\s*=.*$", "", cpp_raw)
    cpp_clean = re.sub(r"\s*\{lvalue\}", "", cpp_clean).strip()
    # Direct lookup
    if cpp_clean in cpp_to_py:
        return cpp_to_py[cpp_clean]
    # Try unwrapping handles
    core = _unwrap_cpp_type(cpp_clean)
    if core in cpp_to_py:
        return cpp_to_py[core]
    return py_type


def _resolve_arg(raw: dict[str, Any], cpp_to_py: dict[str, str]) -> dict[str, Any]:
    """Convert a raw arg dict into a clean structured arg."""
    py_text = raw.get("python")
    cpp_text = raw.get("cpp")
    optional = raw.get("optional", 0) > 0

    if not py_text:
        # C++-only arg (rare mismatch) — best effort
        return {"name": None, "type": None, "optional": optional, "default": None}

    m = _PY_ARG_RE.match(py_text)
    if not m:
        # Unparseable — keep raw text as name, no type
        return {"name": py_text, "type": None, "optional": optional, "default": None}

    py_type, name, default = m.group(1), m.group(2), m.group(3)
    name = _pascal_to_snake(name)
    resolved_type = _resolve_type(py_type, cpp_text, cpp_to_py)

    return {"name": name, "type": resolved_type, "optional": optional, "default": default}


def _resolve_returns(raw: dict[str, Any], cpp_to_py: dict[str, str]) -> dict[str, str | None]:
    """Convert raw returns dict into a clean return type."""
    py_type = raw.get("python")
    cpp_type = raw.get("cpp")
    if not py_type:
        return {"type": None}
    resolved = _resolve_type(py_type, cpp_type, cpp_to_py)
    return {"type": resolved}


def _visit_resolve_signatures(node: dict[str, Any], ctx: dict[str, Any], parent: ClassContext) -> None:
    """Visitor: resolve raw signature parts into clean structured args and returns.

    Also applies well-known arg name patterns: arg1→self for instance methods,
    listener callback naming, and Vector append/extend naming.
    """
    if node.get("type") not in _FUNCTION_TYPES:
        return
    raw_args = node.get("args")
    raw_returns = node.get("returns")
    if not isinstance(raw_args, list) or not isinstance(raw_returns, dict):
        return

    cpp_to_py = ctx.get("cpp_to_py", {})
    name = node.get("name", "")
    args = [_resolve_arg(a, cpp_to_py) for a in raw_args]

    # Rename arg1 to self when its type matches the parent class or an ancestor
    if args and parent.name and args[0].get("name") == "arg1":
        arg1_type = args[0].get("type")
        if arg1_type == parent.name or arg1_type in parent.ancestors:
            args[0]["name"] = "self"

    # Listener methods: last arg is Callable
    is_listener = name.endswith("_listener") and ("add_" in name or "remove_" in name or "has_" in name)
    if is_listener and len(args) >= 2:
        args[-1]["type"] = "Callable"
        args[-1]["name"] = "callback"

    # Vector methods: append(value), extend(values)
    if parent.name and parent.name.endswith("Vector"):
        if name == "append" and len(args) == 2 and args[1].get("name", "").startswith("arg"):
            args[1]["name"] = "value"
        elif name == "extend" and len(args) == 2:
            if args[1].get("name", "").startswith("arg"):
                args[1]["name"] = "values"
            # extend takes an iterable of elements, not a single element
            elem_type = args[1].get("type")
            if elem_type and elem_type != "object":
                args[1]["type"] = f"Iterable[{elem_type}]"

    node["args"] = args
    node["returns"] = _resolve_returns(raw_returns, cpp_to_py)

    # Track object resolutions
    resolved = sum(1 for a in args if a["type"] and a["type"] != "object")
    unresolved = sum(1 for a in args if a["type"] == "object")
    ctx["stats"]["resolved_args"] = ctx["stats"].get("resolved_args", 0) + resolved
    ctx["stats"]["unresolved_object_args"] = ctx["stats"].get("unresolved_object_args", 0) + unresolved


def resolve_signatures(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Resolve raw signature parts into clean structured args and returns."""
    return _walk_tree(tree, _visit_resolve_signatures, ctx)


# ------------------------------------------------------------------------------- #
# Step 6: merge_probe_data
# ------------------------------------------------------------------------------- #


def merge_probe_data(tree: TreeNode, ctx: dict[str, Any]) -> TreeNode:
    """Merge runtime probe results (LiveClasses.json) onto matching tree nodes.

    Matches class nodes by repr. Stamps property types, element_repr, constructable,
    and cross-checks getter return types against resolved signatures.
    Skips gracefully if no probe data is available in ctx.
    """
    probe: dict[str, Any] = ctx.get("probe_data", {})
    if not probe:
        return tree

    merged_props = 0
    merged_element = 0
    getter_upgrades = 0
    getter_mismatches: list[str] = []

    def _merge(node: TreeNode) -> None:
        nonlocal merged_props, merged_element, getter_upgrades
        if isinstance(node, dict):
            if node.get("type") == "class" and not node.get("ref"):
                r = node.get("repr")
                entry = probe.get(r) if r else None
                if entry:
                    _merge_class(node, entry)
            for value in node.values():
                _merge(value)
        elif isinstance(node, list):
            for item in node:
                _merge(item)

    _PRIMITIVE_REPRS = {f"<class '{t}'>" for t in ("int", "float", "str", "bool")}

    def _resolve_element_reprs(reprs: list[str]) -> str | None:
        """Resolve a list of element reprs to a single element_repr.

        - Single repr → use it directly.
        - All known Live API classes → LomObject.
        - All same primitive → use it.
        - Mixed or unknown → object.
        """
        if not reprs:
            return None
        # Filter out NoneType — empty slots aren't informative
        meaningful = [r for r in reprs if r != "<class 'NoneType'>"]
        if not meaningful:
            return None
        if len(meaningful) == 1:
            # Single type — validate it's known
            r = meaningful[0]
            if r in probe or r in _PRIMITIVE_REPRS:
                return r
            return repr(object)
        # Multiple types — check if all are known Live API classes
        if all(r in probe for r in meaningful):
            return "<class 'LomObject.LomObject'>"
        # Mixed or unknown
        return repr(object)

    def _merge_class(node: dict, entry: dict) -> None:
        nonlocal merged_props, merged_element, getter_upgrades

        children = node.get("children", [])
        children_by_name: dict[str, dict] = {}
        for child in children:
            if isinstance(child, dict) and "name" in child:
                children_by_name[child["name"]] = child

        # Properties: stamp probed_type, probed_repr, and element_type/element_repr
        props = entry.get("properties", {})
        for prop_name, prop_info in props.items():
            if not prop_info.get("probed"):
                continue
            child = children_by_name.get(prop_name)
            if child and child.get("type") == "property":
                probed_type = prop_info.get("type")
                if probed_type:
                    child["probed_type"] = probed_type
                probed_repr = prop_info.get("repr")
                if probed_repr:
                    child["probed_repr"] = probed_repr
                # Resolve element type for iterable properties.
                # For vector classes, iterability is on the class entry in repr_index.
                # For tuple properties, element_reprs may be on prop_info directly.
                class_entry = probe.get(probed_repr) if probed_repr else None
                is_iterable = (class_entry and class_entry.get("iterable")) or prop_info.get("element_reprs")
                if is_iterable:
                    elem_reprs = prop_info.get("element_reprs")
                    if not elem_reprs and class_entry:
                        # Fall back to the class entry (only if it has a single
                        # element type — generic containers like Base.Vector have
                        # many and shouldn't be used as fallback)
                        class_reprs = class_entry.get("element_reprs")
                        if class_reprs and len(class_reprs) == 1:
                            elem_reprs = class_reprs
                    if elem_reprs:
                        resolved = _resolve_element_reprs(elem_reprs)
                        if resolved:
                            child["element_repr"] = resolved
                merged_props += 1

        # _live_ptr is always an int (internal C++ pointer handle on every LOM object)
        live_ptr = children_by_name.get("_live_ptr")
        if live_ptr and live_ptr.get("type") == "property" and not live_ptr.get("probed_type"):
            live_ptr["probed_type"] = "int"
            merged_props += 1

        # Constructable: stamp onto class node
        if entry.get("constructable"):
            saved_children = node.pop("children", None)
            node["constructable"] = True
            if saved_children is not None:
                node["children"] = saved_children

        # Getters: cross-check return types, upgrade object → probed type
        getters = entry.get("getters", {})
        for getter_name, getter_info in getters.items():
            if not getter_info.get("probed"):
                continue
            child = children_by_name.get(getter_name)
            if not child or child.get("type") not in _FUNCTION_TYPES:
                continue
            returns = child.get("returns")
            if not isinstance(returns, dict):
                continue
            tree_type = returns.get("type")
            probed_type = getter_info.get("type")
            if not probed_type:
                continue
            if tree_type == "object" and probed_type != "object":
                returns["type"] = probed_type
                getter_upgrades += 1
            elif tree_type and tree_type != "object" and probed_type != tree_type:
                getter_mismatches.append(f"{node.get('name')}.{getter_name}: tree={tree_type}, probe={probed_type}")

        # iterable + element_reprs: stamp onto class node
        # Probe-based: the probe stamped iterable on the class entry
        # Heuristic: classes with append/extend are iterable even if never probed
        is_iterable = entry.get("iterable") or any(
            children_by_name.get(fn, {}).get("type") in _FUNCTION_TYPES for fn in ("append", "extend")
        )
        if is_iterable:
            saved_children = node.pop("children", None)
            node["iterable"] = True
            if saved_children is not None:
                node["children"] = saved_children
        elem_reprs = entry.get("element_reprs")
        if elem_reprs:
            element_repr = _resolve_element_reprs(elem_reprs)
            if element_repr:
                saved_children = node.pop("children", None)
                node["element_repr"] = element_repr
                if saved_children is not None:
                    node["children"] = saved_children
                merged_element += 1

                # Resolve remaining object args on append/extend using element_repr
                m = re.match(r"<class '(?:[\w.]+\.)?(\w+)'>", element_repr)
                if m:
                    element_type = m.group(1)
                    for fn_name in ("append", "extend"):
                        fn = children_by_name.get(fn_name)
                        if not fn or fn.get("type") not in _FUNCTION_TYPES:
                            continue
                        for p in fn.get("args", []):
                            if p.get("type") == "object":
                                if fn_name == "extend":
                                    p["type"] = f"Iterable[{element_type}]"
                                else:
                                    p["type"] = element_type

    _merge(tree)

    if getter_mismatches:
        ctx["getter_mismatches"] = getter_mismatches
    ctx["stats"]["merged_properties"] = merged_props
    ctx["stats"]["merged_element_types"] = merged_element
    ctx["stats"]["getter_return_upgrades"] = getter_upgrades
    ctx["stats"]["getter_return_mismatches"] = len(getter_mismatches)
    return tree



# ------------------------------------------------------------------------------- #
# Pipeline
# ------------------------------------------------------------------------------- #

STEPS: list[PipelineStep] = [
    fix_malformed_class_names,
    rewrite_raw_docs,
    resolve_inheritance,
    relocate_inherited_members,
    parse_enums,
    parse_function_docs,
    parse_signatures,
    build_type_map,
    resolve_signatures,
    merge_probe_data,
]


def run_pipeline(tree: TreeNode, ctx: dict[str, Any] | None = None) -> tuple[TreeNode, dict[str, Any]]:
    """Run all pipeline steps in order. Returns (transformed_tree, ctx)."""
    if ctx is None:
        ctx = {}
    ctx.setdefault("stats", {})

    for step in STEPS:
        tree = step(tree, ctx)

    return tree, ctx


# ------------------------------------------------------------------------------- #
# CLI
# ------------------------------------------------------------------------------- #


STUBS_DIR = Path(__file__).resolve().parent.parent.parent / "stubs"


def resolve_pipeline_dir(version: str) -> Path:
    """Resolve a version string to a pipeline directory.

    Accepts exact versions (12.3.6) or partial (12.3 → 12.3.0). If the exact path doesn't exist, appends .0 as a
    fallback for minor-only versions. Returns the pipeline/ subdirectory where intermediates live.
    """
    ver_dir = STUBS_DIR / version
    if ver_dir.is_dir():
        return ver_dir / "pipeline"

    # Try appending .0 for partial versions like "12.3" → "12.3.0"
    fallback = STUBS_DIR / f"{version}.0"
    if fallback.is_dir():
        return fallback / "pipeline"

    # List available versions for a helpful error
    available = sorted(p.name for p in STUBS_DIR.iterdir() if p.is_dir()) if STUBS_DIR.is_dir() else []
    msg = f"No stubs directory found for version '{version}'"
    if available:
        msg += f"\nAvailable: {', '.join(available)}"
    raise SystemExit(msg)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse and enrich APICapture results")
    parser.add_argument("version", help="Live version (e.g. 12.3.6 or 12.3)")
    parser.add_argument("--output", "-o", help="Output path (default: LiveTree.parsed.json in pipeline dir)")
    args = parser.parse_args()

    pipeline_dir = resolve_pipeline_dir(args.version)
    raw_path = pipeline_dir / "LiveTree.raw.json"
    out_path = Path(args.output).expanduser().resolve() if args.output else pipeline_dir / "LiveTree.parsed.json"

    if not raw_path.exists():
        raise SystemExit(f"Input file not found: {raw_path}")

    with open(raw_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ctx: dict[str, Any] = {}
    probe_path = pipeline_dir / "LiveClasses.json"
    if probe_path.exists():
        with open(probe_path, "r", encoding="utf-8") as f:
            ctx["probe_data"] = json.load(f)

    parsed, ctx = run_pipeline(data, ctx)
    stats = ctx.get("stats", {})

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)
        f.write("\n")

    parts = [f"Wrote {out_path}"]
    if stats:
        parts.append("(" + ", ".join(f"{v} {k.replace('_', ' ')}" for k, v in stats.items()) + ")")
    print(" ".join(parts))


if __name__ == "__main__":
    main()

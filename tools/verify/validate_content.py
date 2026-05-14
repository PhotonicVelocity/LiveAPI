#!/usr/bin/env python3
"""Validate `content/<v>/modules/*.md` + foundation pages against the
schema defined in doc/lom-format.md. Catches authoring mistakes before
the generators run.

Two tiers:

  T1 — link integrity:
    - Every `[^id]` reference in member prose resolves to a real
      `behavior:` or `quirks:` record with matching id on the same
      member.
    - No two records on the same member share an `id:`.

  T2 — schema well-formedness:
    - `refinement:` blocks use only valid sub-keys for their scope
      (property: type/element_type; method arg: name/type/element_type;
      etc.).
    - `behavior:` / `quirks:` records have a non-empty `assertion:`.
    - `confidence:` if present is one of the spec-defined values
      (high/medium/low — hand-confidence — or verified/state-dependent/
      intermittent/unprobed — probe-confidence).
    - `sources:` if present is a string or list-of-strings.
    - `verified_against:` if present is a string.
    - `deprecated:` is a bool or a dict (no shape enforcement yet).

Exits 0 when the SOT is clean. Exits 1 on any T1 or T2 error. Prints a
human-readable report grouped by file.

Usage:
    python tools/verify/validate_content.py [VERSION]
    python tools/verify/validate_content.py --input <content-dir>

Defaults: VERSION=12.3.6, --input=content/<version>/.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

VALID_REFINEMENT_KEYS_BY_SCOPE = {
    "property": {"type", "element_type"},
    "method_arg": {"name", "type", "element_type"},
    "method_return": {"type", "element_type"},
    "class": {"type", "element_type"},
}

VALID_CONFIDENCE_VALUES = {
    # Hand-assessed (used until probe driver lands)
    "high",
    "medium",
    "low",
    # Probe-verified (written by the Phase 3 probe driver)
    "verified",
    "state-dependent",
    "intermittent",
    "unprobed",
}

INLINE_REF_RE = re.compile(r"\[\^([A-Za-z0-9][A-Za-z0-9_-]*)\]")


class Finding:
    """A single validation finding."""

    __slots__ = ("level", "path", "where", "message")

    def __init__(self, level: str, path: Path, where: str, message: str) -> None:
        self.level = level  # "error" or "warning"
        self.path = path
        self.where = where  # member path / location label
        self.message = message

    def __str__(self) -> str:
        return f"  [{self.level}] {self.where}: {self.message}"


def _records_with_ids(member: dict, kind: str) -> list[tuple[int, str | None, dict]]:
    """Return [(index, id, record), ...] for behavior/quirks records on a member."""
    out: list[tuple[int, str | None, dict]] = []
    for i, rec in enumerate(member.get(kind) or []):
        if isinstance(rec, dict):
            out.append((i, rec.get("id"), rec))
    return out


def _validate_record(
    record: dict, where: str, kind: str, path: Path, findings: list[Finding]
) -> None:
    """Schema checks for a single behavior/quirk record."""
    assertion = record.get("assertion")
    if not isinstance(assertion, str) or not assertion.strip():
        findings.append(
            Finding("error", path, where, f"{kind} record missing non-empty `assertion:` field")
        )
    confidence = record.get("confidence")
    if confidence is not None:
        if not isinstance(confidence, str) or confidence not in VALID_CONFIDENCE_VALUES:
            findings.append(
                Finding(
                    "error", path, where,
                    f"{kind} record `confidence: {confidence!r}` — must be one of "
                    f"{sorted(VALID_CONFIDENCE_VALUES)}",
                )
            )
    sources = record.get("sources")
    if sources is not None and not isinstance(sources, (str, list)):
        findings.append(
            Finding("error", path, where, f"{kind} record `sources:` must be string or list of strings")
        )
    elif isinstance(sources, list) and not all(isinstance(s, str) for s in sources):
        findings.append(
            Finding("error", path, where, f"{kind} record `sources:` list items must all be strings")
        )
    verified_against = record.get("verified_against")
    if verified_against is not None and not isinstance(verified_against, str):
        findings.append(
            Finding(
                "error", path, where,
                f"{kind} record `verified_against: {verified_against!r}` must be a string",
            )
        )


def _validate_refinement(
    refinement: dict, where: str, scope: str, path: Path, findings: list[Finding]
) -> None:
    """Schema checks for a refinement block."""
    valid_keys = VALID_REFINEMENT_KEYS_BY_SCOPE.get(scope, set())
    for key, block in refinement.items():
        if key not in valid_keys:
            findings.append(
                Finding(
                    "error", path, where,
                    f"refinement.{key} — not valid at {scope} scope "
                    f"(allowed: {sorted(valid_keys)})",
                )
            )
            continue
        if not isinstance(block, dict):
            findings.append(
                Finding("error", path, where, f"refinement.{key} must be a mapping")
            )
            continue
        # Inner block: probed (optional), confidence, sources
        confidence = block.get("confidence")
        if confidence is not None and (
            not isinstance(confidence, str) or confidence not in VALID_CONFIDENCE_VALUES
        ):
            findings.append(
                Finding(
                    "error", path, where,
                    f"refinement.{key}.confidence: {confidence!r} — must be one of "
                    f"{sorted(VALID_CONFIDENCE_VALUES)}",
                )
            )
        sources = block.get("sources")
        if sources is not None and not isinstance(sources, (str, list)):
            findings.append(
                Finding(
                    "error", path, where,
                    f"refinement.{key}.sources must be string or list of strings",
                )
            )


def _validate_deprecated(
    deprecated: object, where: str, path: Path, findings: list[Finding]
) -> None:
    if not isinstance(deprecated, (bool, dict)):
        findings.append(
            Finding(
                "error", path, where,
                f"deprecated: {deprecated!r} — must be a boolean or a mapping",
            )
        )


def _validate_member(
    member: dict, where: str, scope: str, path: Path, findings: list[Finding]
) -> None:
    """Run T1 + T2 checks for a single member node."""
    # T2: schema
    if "refinement" in member:
        refinement = member.get("refinement")
        if not isinstance(refinement, dict):
            findings.append(
                Finding("error", path, where, "refinement: must be a mapping")
            )
        else:
            _validate_refinement(refinement, where, scope, path, findings)

    if "deprecated" in member:
        _validate_deprecated(member["deprecated"], where, path, findings)

    behavior_records = _records_with_ids(member, "behavior")
    for i, _id, rec in behavior_records:
        _validate_record(rec, f"{where}.behavior[{i}]", "behavior", path, findings)
    quirk_records = _records_with_ids(member, "quirks")
    for i, _id, rec in quirk_records:
        _validate_record(rec, f"{where}.quirks[{i}]", "quirk", path, findings)

    # T1: id uniqueness within the member
    id_locations: dict[str, list[str]] = defaultdict(list)
    for i, rec_id, _ in behavior_records:
        if rec_id is not None:
            id_locations[rec_id].append(f"behavior[{i}]")
    for i, rec_id, _ in quirk_records:
        if rec_id is not None:
            id_locations[rec_id].append(f"quirks[{i}]")
    for rec_id, locs in id_locations.items():
        if len(locs) > 1:
            findings.append(
                Finding(
                    "error", path, where,
                    f"duplicate record id `{rec_id}` on member: {' + '.join(locs)}",
                )
            )

    # T1: every [^id] in description resolves to a record id on this member
    desc = member.get("description")
    if isinstance(desc, str):
        known_ids = set(id_locations.keys())
        for m in INLINE_REF_RE.finditer(desc):
            ref_id = m.group(1)
            if ref_id not in known_ids:
                findings.append(
                    Finding(
                        "error", path, where,
                        f"inline `[^{ref_id}]` doesn't resolve to a record id on this member",
                    )
                )


def _validate_args(
    args: list, where: str, path: Path, findings: list[Finding]
) -> None:
    for i, arg in enumerate(args or []):
        if not isinstance(arg, dict):
            continue
        arg_where = f"{where}.args[{i}]"
        # Args use refinement at method_arg scope.
        if "refinement" in arg:
            refinement = arg.get("refinement")
            if isinstance(refinement, dict):
                _validate_refinement(refinement, arg_where, "method_arg", path, findings)
            else:
                findings.append(
                    Finding("error", path, arg_where, "refinement: must be a mapping")
                )


def _validate_returns(
    returns: dict, where: str, path: Path, findings: list[Finding]
) -> None:
    if "refinement" in returns:
        refinement = returns.get("refinement")
        if isinstance(refinement, dict):
            _validate_refinement(refinement, f"{where}.returns", "method_return", path, findings)
        else:
            findings.append(
                Finding("error", path, f"{where}.returns", "refinement: must be a mapping")
            )


def _validate_class(cls: dict, where: str, path: Path, findings: list[Finding]) -> None:
    _validate_member(cls, where, "class", path, findings)
    for prop in cls.get("properties") or []:
        if isinstance(prop, dict):
            name = prop.get("name", "<anonymous>")
            _validate_member(prop, f"{where}.{name}", "property", path, findings)
    for method in cls.get("methods") or []:
        if isinstance(method, dict):
            name = method.get("name", "<anonymous>")
            m_where = f"{where}.{name}"
            _validate_member(method, m_where, "method_arg", path, findings)
            _validate_args(method.get("args") or [], m_where, path, findings)
            returns = method.get("returns") or {}
            if isinstance(returns, dict) and returns:
                _validate_returns(returns, m_where, path, findings)


def _validate_module(module: dict, path: Path, findings: list[Finding]) -> None:
    module_name = module.get("module", path.stem)
    for cls in module.get("classes") or []:
        if isinstance(cls, dict):
            name = cls.get("name", "<anonymous>")
            _validate_class(cls, f"{module_name}.{name}", path, findings)
    for fn in module.get("functions") or []:
        if isinstance(fn, dict):
            name = fn.get("name", "<anonymous>")
            f_where = f"{module_name}.{name}"
            _validate_member(fn, f_where, "method_arg", path, findings)
            _validate_args(fn.get("args") or [], f_where, path, findings)
            returns = fn.get("returns") or {}
            if isinstance(returns, dict) and returns:
                _validate_returns(returns, f_where, path, findings)
    for enum in module.get("enums") or []:
        if isinstance(enum, dict):
            name = enum.get("name", "<anonymous>")
            _validate_member(enum, f"{module_name}.{name}", "class", path, findings)
    for const in module.get("constants") or []:
        if isinstance(const, dict):
            name = const.get("name", "<anonymous>")
            _validate_member(const, f"{module_name}.{name}", "class", path, findings)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", nargs="?", default="12.3.6",
                        help="Live version (default: 12.3.6)")
    parser.add_argument(
        "--input",
        help="Content dir to validate (default: content/<version>/)",
    )
    args = parser.parse_args()

    content_dir = (
        Path(args.input)
        if args.input
        else REPO_ROOT / "content" / args.version / "modules"
    )
    if not content_dir.is_dir():
        print(f"error: modules dir not found at {content_dir}", file=sys.stderr)
        return 2

    parse_dir = str(REPO_ROOT / "tools" / "parse")
    if parse_dir not in sys.path:
        sys.path.insert(0, parse_dir)
    from parse_module_md import parse_module_md

    findings_by_file: dict[Path, list[Finding]] = {}
    # Validate per-module markdown only. Foundation pages
    # (content/<v>/*.md) use a different schema and aren't covered here.
    files = sorted(content_dir.glob("*.md"))
    if not files:
        print(f"warning: no .md files under {content_dir}", file=sys.stderr)
        return 0

    for path in files:
        try:
            module = parse_module_md(path)
        except Exception as exc:  # noqa: BLE001
            findings_by_file[path] = [
                Finding("error", path, "<parse>", f"parse failed: {exc}")
            ]
            continue
        findings: list[Finding] = []
        _validate_module(module, path, findings)
        if findings:
            findings_by_file[path] = findings

    error_count = sum(
        1 for fs in findings_by_file.values() for f in fs if f.level == "error"
    )
    warning_count = sum(
        1 for fs in findings_by_file.values() for f in fs if f.level == "warning"
    )

    if findings_by_file:
        for path in sorted(findings_by_file):
            try:
                rel = path.relative_to(REPO_ROOT)
            except ValueError:
                rel = path
            print(f"\n{rel}")
            for f in findings_by_file[path]:
                print(f)
        print(
            f"\n{error_count} error(s), {warning_count} warning(s) across "
            f"{len(findings_by_file)} file(s)."
        )
    else:
        print(f"OK — {len(files)} content file(s) validated.")

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())

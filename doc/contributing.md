# Reference Format Guide

> How to write and maintain reference docs in `reference/`.

## Page Structure

```markdown
# ClassName

> `Live.Namespace.ClassName`

General class description — what this represents in Live, when you'd interact with it.

??? note "Raw probe notes (temporary)"
    Unprocessed probe findings that haven't been distilled into member descriptions yet.
    These will be moved to probe scripts/data files as the tooling matures.

## Children

| Child | Returns | Shape | Listenable | Summary |
| ----- | ------- | ----- | ---------- | ------- |
| ...   | ...     | ...   | ...        | ...     |

### `child_name`

- **Returns:** `Type`
- **Shape:** `single` | `list`
- **Listenable:** `yes` | `no`
- **Since:** `<11` | `11.0` | `12.0` | etc.

Description of the child, including any quirks.

## Properties

| Property | Type | Settable | Listenable | Summary |
| -------- | ---- | -------- | ---------- | ------- |
| ...      | ...  | ...      | ...        | ...     |

### `property_name`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes` | `no`
- **Since:** `<11` | `11.0` | `12.0` | etc.

Description of what this property represents.

**Quirks:**
- Setting to `None` raises `InternalError` (C++ type mismatch).
- Value snaps to nearest palette color.

**Limitations:**
- Read-only on group tracks.
- Only meaningful when `some_flag` is `True`.

## Methods

| Method | Returns | Summary |
| ------ | ------- | ------- |
| ...    | ...     | ...     |

### `method_name(arg1, arg2)`

- **Returns:** `Type`
- **Args:**
  - `arg1: type` — description
  - `arg2: type = default` — description
- **Raises:** `ErrorType` when condition.
- **Since:** `<11` | `11.0` | `12.0` | etc.

Description of what this method does.

**Quirks:**
- Ignores the object it's called on; always acts on the selected scene.

**Limitations:**
- Only works on MIDI tracks.
- Raises if the slot is non-empty.

## Enums

### `EnumName`

| Value | Name | Description |
| ----- | ---- | ----------- |
| `0`   | ...  | ...         |
| `1`   | ...  | ...         |

## Open Questions

- Unresolved behavior to probe later.
```

## Format Principles

- **Page title** is the class name (`# Song`), with full path in a blockquote (`> Live.Song.Song`).
- **Summary tables** at the top of each section for quick scanning. Keep them narrow — details go in the per-member sections.
- **Descriptions** are the primary content. Probe findings should be distilled into descriptions, quirks, and limitations
  — not kept as raw notes. The reference is the final product, not a probe log.
  - **Quirks** — non-obvious behavior, gotchas, things that don't work as you'd expect.
  - **Limitations** — constraints on when/where a member works (track type, state requirements, etc.).
- **Raw probe notes** are temporary. During the transition, keep them in a collapsed `??? note "Raw probe notes (temporary)"`
  admonition at the class level. As tooling matures, these move to probe scripts/data files and are removed from the
  reference entirely.
- **Enums** get their own section with a value table when a class defines enum types.
- **Open Questions** stays at the bottom — signals what's unknown and needs probing.
- **Sources / Probe Status** metadata is omitted from the reference. Track coverage in the contributing guide.

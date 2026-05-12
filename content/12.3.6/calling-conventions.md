---
title: Calling conventions
slug: calling-conventions
sidebar_badge: core
_note: |
  Foundation page describing the positional-only calling model that
  applies across every callable in the LOM. Linked from the
  `Parameters` section label on every method / function reference
  page. Hoisted above the alphabetical Modules group in the sidebar
  (see `web/astro.config.mjs`).
---

Every method and function in the LOM takes **positional arguments
only** — no kwargs.

Signatures show parameter names (`view_name`, `direction`,
`bank_index`, ...) for readability — autocomplete labels, hover
hints, pyright error messages. The names are not callable as
kwargs:

```python
# correct — positional
app.view.is_view_visible("Browser")
app.view.is_view_visible("Browser", False)

# error — kwargs not accepted
app.view.is_view_visible(view_name="Browser")
app.view.is_view_visible("Browser", main_window_only=False)
```

Live's Python bindings use Boost.Python with positional-only
parameter binding. Kwarg calls raise `TypeError` at runtime, or
in some cases crash the C++ side with `InternalError` before the
Python exception machinery sees them.

## Type-checker enforcement

The generated `.pyi` stubs include PEP 570 `/` markers on every
callable. Pyright and mypy reject kwarg calls at type-check time
before they reach the runtime — surface the error at the editor
layer, not at the bridge:

```python
# error: Expected 1 positional argument
app.view.is_view_visible(view_name="Browser")  # type: ignore[call-arg]
```

The reference pages drop the `/` from rendered signatures for
readability, but it's present in the `.pyi` files distributed with
the stubs package.

## Why the names matter

Names label the slot, not the call:

- Hover hints and IDE tooltips display each parameter's name
  alongside its type annotation
- Autocomplete shows positional-arg labels as the cursor moves
  through the call
- Pyright errors quote the parameter name when types don't match
  — `Argument of type "int" cannot be assigned to parameter
  "view_name" of type "str"`

Treat the names as documentation, not call-site syntax.

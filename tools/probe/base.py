"""ProbeContext — wraps LiveClient with helpers for systematic behavioral probing.

Extracted from PythonForLive/.tmp/probe_undo_async.py. Provides reusable primitives
for probing undo tracking, async visibility, value ranges, and error behavior.
"""

from __future__ import annotations

from typing import Any, Callable

try:
    from pythonforlive.client import LiveClient
except ImportError:
    raise ImportError(
        "Probe scripts require the PythonForLive client.\n"
        "Install with: pip install -e ../PythonForLive"
    )


def fuzzy_eq(a: Any, b: Any) -> bool:
    """Compare values with tolerance for float precision and color snapping."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 0.01
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01
    return a == b


class ProbeResult:
    """A single probe finding for one member."""

    def __init__(self, cls: str, member: str, kind: str) -> None:
        self.cls = cls
        self.member = member
        self.kind = kind  # "property" or "method"
        self.data: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def __repr__(self) -> str:
        return f"ProbeResult({self.cls}.{self.member} {self.data})"


class ProbeContext:
    """Wraps a LiveClient connection with probe helpers and result accumulation."""

    def __init__(self, client: LiveClient) -> None:
        self.client = client
        self._results: list[ProbeResult] = []
        # Pre-resolve song OID for undo operations
        song = client.request("resolve", {"root": "song", "path": []})
        self.song_oid: str = song["oid"]

    @property
    def results(self) -> list[ProbeResult]:
        return list(self._results)

    def _record(self, cls: str, member: str, kind: str) -> ProbeResult:
        result = ProbeResult(cls, member, kind)
        self._results.append(result)
        return result

    def resolve_child(self, oid: str, child_name: str) -> str | None:
        """Resolve a single child object and return its OID."""
        payload = self.client.request("children", {"oid": oid, "child_name": child_name})
        if isinstance(payload, dict):
            if "oid" in payload:
                return payload["oid"]
            if "item" in payload and isinstance(payload["item"], dict):
                return payload["item"].get("oid")
            if "items" in payload and payload["items"]:
                return payload["items"][0].get("oid")
        return None

    def resolve_children(self, oid: str, child_name: str) -> list[dict[str, Any]]:
        """Resolve a list child and return the items."""
        payload = self.client.request("children", {"oid": oid, "child_name": child_name})
        if isinstance(payload, dict) and "items" in payload:
            return payload["items"]
        return []

    def get(self, oid: str, prop: str) -> Any:
        """Get a property value."""
        return self.client.request("get", {"oid": oid, "prop": prop})

    def set(self, oid: str, prop: str, value: Any) -> Any:
        """Set a property value."""
        return self.client.request("set", {"oid": oid, "prop": prop, "value": value})

    def call(self, oid: str, method: str, args: list[Any] | None = None) -> Any:
        """Call a method on an object."""
        return self.client.request("call", {"oid": oid, "method": method, "args": args or []})

    def wait(self) -> None:
        """Wait for bridge drain — guarantees the next call runs on a new tick."""
        self.client.async_wait()

    # ── Undo/Async probe ────────────────────────────────────────────────────

    def probe_property_undo_async(
        self,
        obj_oid: str,
        cls: str,
        prop: str,
        test_value: Any,
        *,
        compare: Callable[[Any, Any], bool] | None = None,
        restore_value: Any = None,
        is_color: bool = False,
    ) -> ProbeResult:
        """Probe a settable property for undo tracking and async visibility.

        Methodology:
          1. Read original value
          2. Set test value inside an undo group
          3. Immediate readback → async visibility
          4. Wait, then undo
          5. Readback after undo → undo tracking
          6. Restore if undo didn't revert
        """
        eq = compare or fuzzy_eq
        result = self._record(cls, prop, "property")

        try:
            orig = self.get(obj_oid, prop)

            # For booleans, always use the opposite of the current value
            if isinstance(orig, bool):
                test_value = not orig

            if eq(orig, test_value):
                result.set("async_visibility", "skip")
                result.set("undo_tracked", "skip")
                result.set("notes", f"test_value matches original ({orig!r})")
                self._log(cls, prop, "property", result)
                return result

            # Set inside undo group
            self.call(self.song_oid, "begin_undo_step")
            self.set(obj_oid, prop, test_value)

            # Immediate readback
            immediate = self.get(obj_oid, prop)

            self.call(self.song_oid, "end_undo_step")

            if eq(immediate, test_value):
                result.set("async_visibility", "immediate")
            elif eq(immediate, orig):
                result.set("async_visibility", "next_tick")
            elif is_color and immediate != orig:
                result.set("async_visibility", "immediate")
            else:
                result.set("async_visibility", f"unexpected:{immediate!r}")

            # Wait for undo stack
            self.wait()

            # Undo
            self.call(self.song_oid, "undo")
            self.wait()

            # Check undo
            after_undo = self.get(obj_oid, prop)
            if eq(after_undo, orig):
                result.set("undo_tracked", True)
            elif eq(after_undo, test_value) or (is_color and after_undo != orig):
                result.set("undo_tracked", False)
            else:
                result.set("undo_tracked", f"unexpected:{after_undo!r}")

            # Redo to neutralize our undo (keeps the undo stack clean for the next probe),
            # then always manually restore to original regardless of undo outcome.
            self.call(self.song_oid, "redo")
            self.wait()
            rv = restore_value if restore_value is not None else orig
            if not eq(self.get(obj_oid, prop), rv):
                self.set(obj_oid, prop, rv)
                self.wait()

        except Exception as e:
            result.set("async_visibility", "error")
            result.set("undo_tracked", "error")
            result.set("error", str(e)[:200])

        self._log(cls, prop, "property", result)
        return result

    def probe_method_undo(
        self,
        cls: str,
        method_name: str,
        call_oid: str,
        args: list[Any],
        *,
        check_fn: Callable[[], bool] | None = None,
        cleanup_fn: Callable[[], None] | None = None,
    ) -> ProbeResult:
        """Probe a method for undo tracking.

        Args:
            check_fn: Returns True if the method's effect is still present.
            cleanup_fn: Called after probe to restore state.
        """
        result = self._record(cls, method_name, "method")

        try:
            self.call(call_oid, method_name, args)

            # Check immediately (before wait) for async visibility
            immediate = check_fn() if check_fn else None

            self.wait()

            after_wait = check_fn() if check_fn else None

            if check_fn is not None:
                if immediate:
                    result.set("async_visibility", "immediate")
                elif after_wait:
                    result.set("async_visibility", "next_tick")
                else:
                    result.set("async_visibility", f"unclear:immediate={immediate},after_wait={after_wait}")

            self.call(self.song_oid, "undo")
            self.wait()

            after_undo = check_fn() if check_fn else None

            if check_fn is not None:
                if after_wait and not after_undo:
                    result.set("undo_tracked", True)
                elif after_wait and after_undo:
                    result.set("undo_tracked", False)
                else:
                    result.set("undo_tracked", f"unclear:before={after_wait},after={after_undo}")
            else:
                result.set("undo_tracked", "unknown")

        except Exception as e:
            result.set("undo_tracked", "error")
            result.set("error", str(e)[:200])

        # After undo: if undo-tracked, the effect is already gone — no cleanup needed.
        # If NOT undo-tracked, undo popped a previous entry — redo to restore it,
        # then run cleanup to remove our method's effect.
        undo_result = result.data.get("undo_tracked")
        if undo_result is True:
            # Effect already undone. Redo stack has our method — clear it with
            # an empty undo group so nothing can accidentally redo it.
            self.call(self.song_oid, "begin_undo_step")
            self.call(self.song_oid, "end_undo_step")
            self.wait()
        else:
            # Undo hit a previous entry — redo to restore it
            self.call(self.song_oid, "redo")
            self.wait()
            # Run cleanup to remove our method's effect, wrapped in undo group
            # that we immediately undo so the stack stays clean
            if cleanup_fn:
                try:
                    self.call(self.song_oid, "begin_undo_step")
                    cleanup_fn()
                    self.call(self.song_oid, "end_undo_step")
                    self.wait()
                    self.call(self.song_oid, "undo")
                    self.wait()
                except Exception:
                    pass

        self._log(cls, method_name, "method", result)
        return result

    # ── Value range probe ───────────────────────────────────────────────────

    def probe_value_range(
        self,
        obj_oid: str,
        cls: str,
        prop: str,
        test_values: list[Any],
    ) -> ProbeResult:
        """Probe a property with a series of values, recording which succeed and which raise.

        Returns a result with 'accepted' (values that stuck) and 'rejected' (values that raised).
        Restores original value after probing.
        """
        result = self._record(cls, prop, "property")
        accepted: list[Any] = []
        rejected: list[dict[str, Any]] = []

        try:
            orig = self.get(obj_oid, prop)

            for val in test_values:
                try:
                    self.set(obj_oid, prop, val)
                    readback = self.get(obj_oid, prop)
                    accepted.append({"value": val, "readback": readback})
                except Exception as e:
                    rejected.append({"value": val, "error": str(e)[:200]})

            # Restore
            try:
                self.set(obj_oid, prop, orig)
            except Exception:
                pass

        except Exception as e:
            result.set("error", str(e)[:200])

        result.set("value_range", {"accepted": accepted, "rejected": rejected})
        self._log(cls, prop, "property", result)
        return result

    # ── Error behavior probe ────────────────────────────────────────────────

    def probe_error(
        self,
        obj_oid: str,
        cls: str,
        prop: str,
        bad_values: list[Any],
    ) -> ProbeResult:
        """Probe a property with values expected to cause errors, recording the error messages."""
        result = self._record(cls, prop, "property")
        errors: list[dict[str, str]] = []

        for val in bad_values:
            try:
                self.set(obj_oid, prop, val)
                errors.append({"value": repr(val), "error": "no error (unexpected)"})
            except Exception as e:
                errors.append({"value": repr(val), "error": str(e)[:200]})

        result.set("error_behavior", errors)
        self._log(cls, prop, "property", result)
        return result

    # ── Logging ─────────────────────────────────────────────────────────────

    def _log(self, cls: str, member: str, kind: str, result: ProbeResult) -> None:
        tag = "prop" if kind == "property" else "meth"
        parts = []
        for k, v in result.data.items():
            if k == "notes":
                continue
            parts.append(f"{k}={v}")
        notes = result.data.get("notes", "")
        detail = ", ".join(parts)
        suffix = f"  ({notes})" if notes else ""
        print(f"  [{tag}] {cls}.{member}: {detail}{suffix}")

    # ── Serialization ───────────────────────────────────────────────────────

    def to_dict(self) -> dict[str, Any]:
        """Serialize all results into the ProbeResults.json format."""
        classes: dict[str, dict[str, dict[str, Any]]] = {}

        for r in self._results:
            if r.cls not in classes:
                classes[r.cls] = {"properties": {}, "methods": {}}
            section = "properties" if r.kind == "property" else "methods"
            classes[r.cls][section][r.member] = r.data

        return {"classes": classes}

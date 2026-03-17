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

    def release(self) -> None:
        """Release the bridge — sleeps past the drain window so the next RPC runs on a new tick."""
        self.client.async_wait()

    def wait_for_next_tick(self) -> None:
        """Wait for the next tick by sending a ping."""
        self.client.request("ping", {})

    # ── Listener infrastructure ──────────────────────────────────────────────

    def subscribe_all(self, targets: dict[str, tuple[str, list[str]]]) -> dict[str, Any]:
        """Bulk-subscribe to listenable properties and snapshot initial values.

        Args:
            targets: {label: (oid, [prop_names])} — label is used for logging
                     and event grouping (e.g. "Song", "Song.View").

        Returns:
            Initial snapshot: {label: {prop: value}} for all readable properties.
        """
        self._sub_ids: list[str] = []
        self._sub_map: dict[str, tuple[str, str]] = {}  # sub_id → (label, prop)
        snapshot: dict[str, dict[str, Any]] = {}

        for label, (oid, props) in targets.items():
            # Bulk subscribe
            items = [{"oid": oid, "prop": p} for p in props]
            result = self.client.request("listen_bulk", {"items": items})
            for key, sub_info in result.items():
                sub_id = sub_info["sub_id"]
                prop = key.split(":", 1)[1]  # "o_1:tempo" → "tempo"
                self._sub_ids.append(sub_id)
                self._sub_map[sub_id] = (label, prop)

            # Get initial values
            values = self.client.request("get_many", {"oid": oid, "props": props})
            snapshot[label] = values

            print(f"  Subscribed to {len(result)}/{len(props)} properties on {label}")

        # Drain any stale events from subscription setup
        self.release()
        self.client.poll(timeout=0.0)
        self.client.drain_events()

        return snapshot

    def unsubscribe_all(self) -> None:
        """Unsubscribe all listeners registered via subscribe_all."""
        for sub_id in getattr(self, "_sub_ids", []):
            try:
                self.client.request("unlisten", {"sub_id": sub_id})
            except Exception:
                pass
        self._sub_ids = []
        self._sub_map = {}

    def collect_fired_listeners(self) -> list[dict[str, Any]]:
        """Collect all listener events that have fired.

        Polls the socket briefly to read any events flushed by the bridge.
        """
        self.client.poll(timeout=0.0)
        raw = self.client.drain_events()

        result = []
        for e in raw:
            if e.get("type") != "event":
                continue
            sub_id = e.get("sub_id", "")
            label, prop = self._sub_map.get(sub_id, ("?", "?"))
            result.append({"label": label, "prop": prop, "value": e.get("value")})
        return result

    def discard_events(self) -> None:
        """Read and discard any pending events from the socket."""
        self.client.poll(timeout=0.0)
        self.client.drain_events()

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
    ) -> ProbeResult:
        """Probe a settable property for undo tracking, async visibility, and side effects.

        Methodology:
          1. Ping to sync with bridge (flushes pending events). Drain stale events.
          2. Read original value.
          3. Start undo group, set test value, end undo group.
          4. Get property value → if changed, async_visibility = "immediate".
          5. Release bridge and ping to sync with next tick.
          6. If async wasn't immediate, get again → "next_tick" or "no_change".
          7. Collect fired listeners for side effects (they should all have fired by now).
          8. Undo, check readback → undo tracking. Wait a tick before get if async isn't immediate.
          9. Redo + restore if undo didn't work (e.g. because it popped a previous entry)
          10. release
        """
        eq = compare or fuzzy_eq
        result = self._record(cls, prop, "property")
        has_listeners = bool(getattr(self, "_sub_map", {}))

        try:
            # 1. Ping to sync with bridge. Drain stale events.
            self.wait_for_next_tick()
            if has_listeners:
                self.discard_events()

            # 2. Read original value.
            orig = self.get(obj_oid, prop)
            if isinstance(orig, bool):
                test_value = not orig
            if eq(orig, test_value):
                result.set("async_visibility", "skip")
                result.set("undo_tracked", "skip")
                result.set("notes", f"test_value matches original ({orig!r})")
                self._log(cls, prop, "property", result)
                return result

            # 3. Start undo group, set test value, end undo group.
            self.call(self.song_oid, "begin_undo_step")
            self.set(obj_oid, prop, test_value)
            self.call(self.song_oid, "end_undo_step")

            # 4. Get property value → async visibility.
            readback = self.get(obj_oid, prop)
            is_immediate = eq(readback, test_value)

            # 5. Release bridge and ping to sync with next tick.
            self.release()
            self.wait_for_next_tick()

            # 6. If async wasn't immediate, get again to confirm next_tick.
            if is_immediate:
                result.set("async_visibility", "immediate")
            else:
                readback_next = self.get(obj_oid, prop)
                if eq(readback_next, test_value):
                    result.set("async_visibility", "next_tick")
                else:
                    result.set("async_visibility", "no_change")

            # 7. Collect fired listeners for side effects.
            if has_listeners:
                fired = self.collect_fired_listeners()
                side_effects = [
                    {"label": e["label"], "prop": e["prop"]}
                    for e in fired
                    if not (e["label"] == cls and e["prop"] == prop)
                ]
                if side_effects:
                    result.set("side_effects", side_effects)

            # 8. Undo, check readback → undo tracking.
            self.call(self.song_oid, "undo")
            if is_immediate:
                after_undo = self.get(obj_oid, prop)
            else:
                self.release()
                self.wait_for_next_tick()
                after_undo = self.get(obj_oid, prop)
            result.set("undo_tracked", eq(after_undo, orig))

            # 9. Cleanup + release.
            undo_worked = eq(after_undo, orig)
            if not undo_worked:
                # Undo popped a previous entry — redo to restore it, then fix our property.
                self.call(self.song_oid, "redo")
                if not is_immediate:
                    self.release()
                    self.wait_for_next_tick()
                rv = restore_value if restore_value is not None else orig
                if not eq(self.get(obj_oid, prop), rv):
                    self.set(obj_oid, prop, rv)
                    
            # 10. Release
            self.release()

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
        """Probe a method for undo tracking, async visibility, and side effects.

        Methodology:
          1. Ping to sync with bridge. Drain stale events.
          2. Record pre-state via check_fn.
          3. Start undo group, call method, end undo group.
          4. Check effect immediately via check_fn → if changed, async = "immediate".
          5. Release + ping to sync with next tick.
          6. If effect wasn't immediate, check again → "next_tick" or "no_effect".
          7. Collect fired listeners for side effects.
          8. Undo, check via check_fn → undo tracking. Wait a tick if async wasn't immediate.
          9. Redo + cleanup if undo didn't work (e.g. because it popped a previous entry).
          10. Release.

        Args:
            check_fn: Returns True if the method's effect is present.
            cleanup_fn: Called after probe to restore state if undo didn't work.
        """
        result = self._record(cls, method_name, "method")
        has_listeners = bool(getattr(self, "_sub_map", {}))

        try:
            # 1. Ping to sync with bridge. Drain stale events.
            self.wait_for_next_tick()
            if has_listeners:
                self.discard_events()

            # 2. Record pre-state.
            before = check_fn() if check_fn else None

            # 3. Start undo group, call method, end undo group.
            self.call(self.song_oid, "begin_undo_step")
            self.call(call_oid, method_name, args)
            self.call(self.song_oid, "end_undo_step")

            # 4. Check effect immediately.
            is_immediate = False
            if check_fn is not None:
                after = check_fn()
                is_immediate = after and not before if before is not None else after

            # 5. Release + ping to sync with next tick.
            self.release()
            self.wait_for_next_tick()

            # 6. If effect wasn't immediate, check again.
            if check_fn is not None:
                if is_immediate:
                    result.set("async_visibility", "immediate")
                else:
                    after_tick = check_fn()
                    effect_present = after_tick and not before if before is not None else after_tick
                    if effect_present:
                        result.set("async_visibility", "next_tick")
                    else:
                        result.set("async_visibility", "no_effect")

            # 7. Collect fired listeners for side effects.
            if has_listeners:
                fired = self.collect_fired_listeners()
                if fired:
                    result.set("side_effects", [
                        {"label": e["label"], "prop": e["prop"]}
                        for e in fired
                    ])

            # 8. Undo, check via check_fn → undo tracking.
            self.call(self.song_oid, "undo")
            if not is_immediate:
                self.release()
                self.wait_for_next_tick()

            if check_fn is not None:
                after_undo = check_fn()
                if before is not None:
                    # Effect should be gone after undo if tracked
                    undo_reverted = not after_undo if before is False else after_undo == before
                else:
                    undo_reverted = not after_undo
                result.set("undo_tracked", undo_reverted)
            else:
                result.set("undo_tracked", "unknown")

        except Exception as e:
            result.set("undo_tracked", "error")
            result.set("error", str(e)[:200])

        # 9. Redo + cleanup if undo didn't work.
        undo_result = result.data.get("undo_tracked")
        if undo_result is not True:
            # Undo hit a previous entry — redo to restore it.
            self.call(self.song_oid, "redo")
            if not is_immediate:
                self.release()
                self.wait_for_next_tick()
            # Run cleanup to remove our method's effect.
            if cleanup_fn:
                try:
                    self.call(self.song_oid, "begin_undo_step")
                    cleanup_fn()
                    self.call(self.song_oid, "end_undo_step")
                    self.call(self.song_oid, "undo")
                except Exception:
                    pass

        # 10. Release.
        self.release()

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

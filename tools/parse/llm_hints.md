# Manual Hints for LLM Resolution

These are facts about the Live API that cannot be inferred from the type skeleton, decompiled code,
or MaxForLive docs. Use them to guide your resolutions.

- Song and Application are root objects that have no parent. Their `canonical_parent` is always None.
- Browser.hotswap_target points to the Device that will be hotswapped.

"""Smoke test for the targeted probe trigger. Runs across two ticks."""


def run(song, log):
    log(f"[test_trigger] tick 1: tempo={song.tempo}")
    yield
    log(f"[test_trigger] tick 2: tracks={len(song.tracks)}, scenes={len(song.scenes)}")

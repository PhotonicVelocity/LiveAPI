"""Smoke test for the targeted probe trigger. Logs tempo and track count."""


def run(song, log):
    log(f"[test_trigger] tempo={song.tempo}")
    log(f"[test_trigger] tracks={len(song.tracks)}")
    log(f"[test_trigger] scenes={len(song.scenes)}")
    log("[test_trigger] OK")

"""Second smoke test — verify different scripts can run without restarting Live."""


def run(song, log):
    log(f"[test_trigger2] tick 1: tempo={song.tempo}, loop={song.loop}")
    yield
    log(f"[test_trigger2] tick 2: metronome={song.metronome}, overdub={song.overdub}")

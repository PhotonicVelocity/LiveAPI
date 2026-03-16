from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .WavetableDevice import WavetableDevice


class EffectMode:
    none: int = 0
    frequency_modulation: int = 1
    sync_and_pulse_width: int = 2
    warp_and_fold: int = 3

class FilterRouting:
    serial: int = 0
    parallel: int = 1
    split: int = 2

class ModulationSource:
    amp_envelope: int = 0
    envelope_2: int = 1
    envelope_3: int = 2
    lfo_1: int = 3
    lfo_2: int = 4
    midi_velocity: int = 5
    midi_note: int = 6
    midi_pitch_bend: int = 7
    midi_channel_pressure: int = 8
    midi_mod_wheel: int = 9
    midi_random: int = 10

class UnisonMode:
    none: int = 0
    classic: int = 1
    slow_shimmer: int = 2
    fast_shimmer: int = 3
    phase_sync: int = 4
    position_spread: int = 5
    random_note: int = 6

class VoiceCount:
    two: int = 0
    three: int = 1
    four: int = 2
    five: int = 3
    six: int = 4
    seven: int = 5
    eight: int = 6

class Voicing:
    mono: int = 0
    poly: int = 1

__all__ = ['WavetableDevice', 'EffectMode', 'FilterRouting', 'ModulationSource', 'UnisonMode', 'VoiceCount', 'Voicing']

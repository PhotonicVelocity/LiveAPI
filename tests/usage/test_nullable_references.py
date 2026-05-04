"""Nullable-reference properties: assigning real values and checking for None.

These patterns broke in earlier stub generations where the probe-observed-None on
properties like Song.View.selected_chain produced `value: None` setters that rejected
real assignments. The Step 12 manual refinements + Step 11 generator fix corrected
each of these to `T | None`. Pattern citations point to Push2 / pushbase usage in
the decompiled corpus where these assignments and checks appear.

References:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Push2/track_selection.py#L95
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/pushbase/selection.py#L54
"""

from __future__ import annotations

from Live.Browser import Browser, BrowserItem
from Live.Chain import Chain
from Live.Clip import Clip
from Live.Device import Device
from Live.DeviceParameter import DeviceParameter
from Live.Groove import Groove
from Live.Scene import Scene
from Live.Song import Song


def assign_selected_chain(song: Song, chain: Chain | None) -> None:
    # Push2/track_selection.py:95 pattern: assign Chain to View.selected_chain.
    song.view.selected_chain = chain


def read_appointed_device(song: Song) -> Device | None:
    return song.appointed_device


def read_clip_groove(clip: Clip) -> Groove | None:
    return clip.groove


def read_scene_color(scene: Scene) -> int | None:
    return scene.color_index


def assign_scene_color(scene: Scene, color: int | None) -> None:
    # Scene.color_index docstring: "Can be None for no color."
    scene.color_index = color


def read_detail_clip(song: Song) -> Clip | None:
    return song.view.detail_clip


def read_selected_parameter(song: Song) -> DeviceParameter | None:
    return song.view.selected_parameter


def read_browser_item_children(browser_item: BrowserItem) -> object:
    return browser_item.children


def hotswap_to_device(browser: Browser, device: Device | None) -> Device | None:
    # Browser.hotswap_target is Device | None per probe (MS33 in doc/live-api/Browser.md):
    # during active hotswap it returns the Device being swapped, not a BrowserItem.
    # Settable: assigning a Device handle activates hotswap; None deactivates.
    browser.hotswap_target = device
    return browser.hotswap_target

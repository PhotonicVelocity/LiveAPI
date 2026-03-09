"""Fetch Ableton Live release notes and write them to doc/release-notes/.

Scrapes the release notes page with BeautifulSoup, preserving the full
hierarchy: version → section → category → items.

Usage:
    python tools/fetch_release_notes.py              # fetch Live 11 + 12
    python tools/fetch_release_notes.py --version 12 # fetch Live 12 only

Requires: pip install beautifulsoup4
"""

import argparse
import os
import re
import sys
from urllib.request import urlopen

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    print("Missing dependency: pip install beautifulsoup4", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
OUT_DIR = os.path.join(REPO_ROOT, "doc", "release-notes")

URLS = {
    "11": "https://www.ableton.com/en/release-notes/live-11/",
    "12": "https://www.ableton.com/en/release-notes/live-12/",
}


def parse_release_notes(html: str) -> list[dict]:
    """Parse release notes HTML into structured version dicts."""
    soup = BeautifulSoup(html, "html.parser")
    versions = []

    for block in soup.select("div.release-notes"):
        # Version header is the h2 directly in the block
        h2 = block.find("h2")
        if not h2:
            continue
        ver_text = h2.get_text(strip=True)
        ver_match = re.search(r"(\d+\.\d+(?:\.\d+)?(?:b\d+)?)", ver_text)
        if not ver_match:
            continue

        version_info: dict = {
            "version": ver_match.group(1),
            "date": "",
            "lines": [],
        }
        versions.append(version_info)

        # Content is inside div.release_note_text
        content_div = block.select_one("div.release_note_text")
        if not content_div:
            continue

        # Heading hierarchy varies across versions. Ableton's CMS uses:
        #   h1 = major new feature (e.g. "Stem Separation") — only in big releases
        #   h2 = section (e.g. "New Features and Improvements", "Auto Pan-Tremolo Updates")
        #   h3 = category (e.g. "Arrangement View", "Browser")
        #   h4 = subcategory (rare)
        # For smaller releases, h3 may be used for sections that are h2 elsewhere.
        for child in content_div.children:
            if not isinstance(child, Tag):
                continue

            tag = child.name
            text = child.get_text(" ", strip=True)

            # Date can appear in <p>, <h4>, or other tags — grab it before type dispatch
            if not version_info["date"]:
                date_match = re.match(
                    r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?"
                    r"|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
                    r"\s+\d{1,2},?\s+\d{4}",
                    text,
                )
                if date_match:
                    version_info["date"] = text
                    continue

            if tag == "p":
                if text:
                    version_info["lines"].append(("paragraph", text))

            elif tag == "h1":
                # Major new feature header (e.g. "Stem Separation", "Splice Integration")
                version_info["lines"].append(("feature", text.rstrip(":")))

            elif tag == "h2":
                # h2 can be either a structural section ("New Features and Improvements",
                # "Bugfixes") or a feature description ("Auto Pan-Tremolo Updates",
                # "Bounce Group Tracks"). Distinguish by known section names.
                clean = text.rstrip(":")
                if clean.lower() in (
                    "new features and improvements",
                    "bugfixes",
                    "known issues",
                    "deprecations",
                ):
                    version_info["lines"].append(("section", clean))
                else:
                    version_info["lines"].append(("feature", clean))

            elif tag == "h3":
                clean = text.rstrip(":")
                if clean.lower() in (
                    "new features and improvements",
                    "bugfixes",
                    "known issues",
                    "deprecations",
                ):
                    version_info["lines"].append(("section", clean))
                else:
                    version_info["lines"].append(("category", clean))

            elif tag == "h4":
                version_info["lines"].append(("subcategory", text.rstrip(":")))

            elif tag == "ul":
                for li in child.find_all("li", recursive=False):
                    item_text = li.get_text(" ", strip=True)
                    if item_text:
                        version_info["lines"].append(("item", item_text))

            elif tag == "ol":
                for i, li in enumerate(child.find_all("li", recursive=False), 1):
                    item_text = li.get_text(" ", strip=True)
                    if item_text:
                        version_info["lines"].append(("ordered_item", f"{i}. {item_text}"))

    return versions


def versions_to_markdown(versions: list[dict], major: str) -> str:
    """Convert parsed versions to markdown with full hierarchy."""
    lines = [f"# Ableton Live {major} Release Notes", ""]

    for ver in versions:
        version = ver["version"]
        date = ver["date"]
        if date:
            lines.append(f"## {version} ({date})")
        else:
            lines.append(f"## {version}")
        lines.append("")

        prev_kind = ""
        for kind, text in ver["lines"]:
            # Add blank line before headers if previous was an item
            if kind in ("feature", "section", "category", "subcategory") and prev_kind in ("item", "ordered_item"):
                lines.append("")

            if kind == "feature":
                lines.append(f"### {text}")
                lines.append("")
            elif kind == "section":
                lines.append(f"### {text}")
                lines.append("")
            elif kind == "category":
                lines.append(f"**{text}**")
                lines.append("")
            elif kind == "subcategory":
                lines.append(f"_{text}_")
                lines.append("")
            elif kind == "item":
                lines.append(f"- {text}")
            elif kind == "ordered_item":
                lines.append(text)
            elif kind == "paragraph":
                lines.append(text)
                lines.append("")

            prev_kind = kind

        # Ensure trailing newline after last items
        if ver["lines"] and ver["lines"][-1][0] == "item":
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Ableton Live release notes")
    parser.add_argument("--version", choices=["11", "12"], help="Fetch only this major version")
    args = parser.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)

    targets = {args.version: URLS[args.version]} if args.version else URLS

    for major, url in sorted(targets.items()):
        print(f"Fetching {url}...")
        with urlopen(url) as resp:
            html = resp.read().decode("utf-8")

        versions = parse_release_notes(html)
        if not versions:
            print(f"  No versions found for Live {major} — page structure may have changed", file=sys.stderr)
            continue

        md = versions_to_markdown(versions, major)
        out_path = os.path.join(OUT_DIR, f"live-{major}.md")
        with open(out_path, "w") as f:
            f.write(md)
        print(f"  Wrote {len(versions)} versions to {out_path}")


if __name__ == "__main__":
    main()

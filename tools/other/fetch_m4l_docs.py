"""Fetch Max for Live LOM documentation from docs.cycling74.com.

Scrapes the Live Object Model reference pages and saves them as markdown files
matching the format expected by llm_resolve.py.

Supports two modes:
  - Current (Max 9+): per-class pages at /apiref/lom/<class>/
  - Legacy (Max 8):   single page with all classes inline

Usage:
    python tools/other/fetch_m4l_docs.py                          # current docs → doc/max-for-live-docs/<version>/
    python tools/other/fetch_m4l_docs.py -o doc/max-for-live-docs/9.1
    python tools/other/fetch_m4l_docs.py --legacy                 # Max 8 legacy docs → doc/max-for-live-docs/8.0/

Requires: pip install beautifulsoup4
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup, Tag, NavigableString

BASE_URL = "https://docs.cycling74.com/apiref/lom"
LEGACY_URL = "https://docs.cycling74.com/legacy/max8/vignettes/live_object_model"
USER_AGENT = "LiveAPI-DocFetcher/1.0"
DELAY = 0.5  # seconds between requests


def fetch_page(url: str) -> str:
    """Fetch a URL and return the HTML content."""
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


# ---------------------------------------------------------------------------
# HTML → Markdown conversion using BeautifulSoup
# ---------------------------------------------------------------------------

def _tag_to_md(tag: Tag, *, inline: bool = False) -> str:
    """Recursively convert a bs4 Tag to markdown."""
    parts: list[str] = []

    for child in tag.children:
        if isinstance(child, NavigableString):
            text = str(child)
            if not inline:
                text = re.sub(r"\s+", " ", text)
            parts.append(text)
        elif isinstance(child, Tag):
            if child.name == "svg":
                continue
            if child.name == "a" and "anchorLink" in " ".join(child.get("class", [])):
                continue
            if child.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(child.name[1])
                text = _tag_to_md(child, inline=True).strip()
                # Collapse runs of whitespace (from inline element boundaries)
                text = re.sub(r"\s+", " ", text)
                parts.append(f"\n\n{'#' * level} {text}")
            elif child.name == "p":
                inner = _tag_to_md(child, inline=True).strip()
                if inner:
                    parts.append(f"\n\n{inner}")
            elif child.name == "br":
                parts.append("  \n")
            elif child.name == "pre":
                code_tag = child.find("code")
                code_text = code_tag.get_text() if code_tag else child.get_text()
                parts.append(f"\n\n```\n{code_text.strip()}\n```")
            elif child.name == "code":
                parts.append(f"`{child.get_text()}`")
            elif child.name == "a":
                href = child.get("href", "")
                text = child.get_text(strip=True)
                if href and ("/apiref/lom/" in href or "/lom/" in href):
                    parts.append(f"[{text}]({href})")
                else:
                    parts.append(text)
            elif child.name in ("ul", "ol"):
                for li in child.find_all("li", recursive=False):
                    li_text = _tag_to_md(li, inline=True).strip()
                    parts.append(f"\n- {li_text}")
                parts.append("\n")
            elif child.name in ("strong", "b"):
                parts.append(f"**{child.get_text()}**")
            elif child.name in ("em", "i"):
                parts.append(f"*{child.get_text()}*")
            else:
                parts.append(_tag_to_md(child, inline=inline))

    result = "".join(parts)
    return result


def _clean_markdown(md: str) -> str:
    """Normalize markdown output."""
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"(\w)(read-only|observe)", r"\1 \2", md)
    md = md.replace("read-onlyobserve", "read-only observe")
    # Strip trailing whitespace from each line (except intentional br "  \n")
    lines = md.split("\n")
    lines = [line.rstrip() for line in lines]
    return "\n".join(lines).strip() + "\n"


# ---------------------------------------------------------------------------
# Current docs (Max 9+): one page per class
# ---------------------------------------------------------------------------

def _article_to_md(html: str) -> str:
    """Extract <article> from a v9 page and convert to markdown."""
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if not article:
        return ""
    return _clean_markdown(_tag_to_md(article))


def extract_class_pages(html: str) -> list[tuple[str, str]]:
    """Extract (slug, title) pairs from the __NEXT_DATA__ TOC."""
    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if match:
        data = json.loads(match.group(1))
        toc = data.get("props", {}).get("pageProps", {}).get("toc", [])
        pages = []
        for entry in toc:
            path = entry.get("path", "")
            title = entry.get("title", "")
            if path.startswith("/apiref/lom/") and path != "/apiref/lom":
                slug = path.rstrip("/").rsplit("/", 1)[-1]
                pages.append((slug, title))
        return pages

    # Fallback: parse links from HTML
    pages = []
    for m in re.finditer(r'href="(/apiref/lom/([a-z_]+)/)"[^>]*>([^<]+)<', html, re.I):
        _, slug, title = m.groups()
        pages.append((slug, title.strip()))
    return sorted(set(pages))


def fetch_current(output_dir: Path) -> None:
    """Fetch all LOM class pages from the current (Max 9+) docs."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching LOM index from {BASE_URL}/ ...")
    index_html = fetch_page(f"{BASE_URL}/")

    version_match = re.search(r"Ableton Live version ([\d.]+)", index_html)
    if version_match:
        print(f"  Documentation version: Live {version_match.group(1)}")

    pages = extract_class_pages(index_html)
    print(f"  Found {len(pages)} class pages\n")

    for i, (slug, title) in enumerate(pages, 1):
        url = f"{BASE_URL}/{slug}/"
        out_file = output_dir / f"{slug}.md"

        print(f"  [{i}/{len(pages)}] {title} → {out_file.name}", end="", flush=True)

        try:
            html = fetch_page(url)
            md = _article_to_md(html)
            out_file.write_text(md)
            print(f"  ({len(md)} chars)")
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)

        if i < len(pages):
            time.sleep(DELAY)

    # Save the index page
    index_md = _article_to_md(index_html)
    (output_dir / "lom.md").write_text(index_md)
    print(f"\n  Index → lom.md ({len(index_md)} chars)")

    print(f"\nDone. {len(pages)} pages saved to {output_dir}/")


# ---------------------------------------------------------------------------
# Legacy docs (Max 8): single page, split by <h2> class sections
# ---------------------------------------------------------------------------

def _slug_from_title(title: str) -> str:
    """Convert a class title to a filename slug (e.g., 'Application.View' → 'application_view')."""
    return title.lower().replace(".", "_")


def _legacy_member_to_md(member_div: Tag) -> str:
    """Convert a legacy member entry (child/property/function) to markdown.

    Input HTML structure:
        <h5 class="liveapi_child_name">name</h5>
        <div class="type"><span class="heading">Type</span><span class="value">int</span></div>
        <div class="access"><span class="heading">Access</span><span class="value">get, observe</span></div>
        <h6>Description</h6>
        <p class="description">...</p>
        <div class="parameters"><span class="heading">Parameter</span><span class="value">...</span></div>
        <div class="return"><span class="heading">Returns</span><span class="value">...</span></div>

    Output: ### name int read-only observe\n\nDescription text
    """
    name_tag = member_div.find("h5")
    if not name_tag:
        return ""
    name = name_tag.get_text(strip=True)

    # Extract type
    type_div = member_div.find("div", class_="type") if isinstance(member_div, Tag) else None
    type_text = ""
    if type_div:
        val = type_div.find("span", class_="value")
        if val:
            # Handle links inside type (e.g., <a>Application.View</a>)
            type_text = val.get_text(strip=True)

    # Extract access → convert to read-only / observe notation
    access_div = member_div.find("div", class_="access") if isinstance(member_div, Tag) else None
    access_text = ""
    if access_div:
        val = access_div.find("span", class_="value")
        if val:
            raw = val.get_text(strip=True)
            parts = [p.strip() for p in raw.split(",")]
            access_parts = []
            if "set" not in parts:
                access_parts.append("read-only")
            if "observe" in parts:
                access_parts.append("observe")
            access_text = " ".join(access_parts)

    # Build ### header
    header_parts = [name]
    if type_text:
        header_parts.append(type_text)
    if access_text:
        header_parts.append(access_text)
    lines = [f"### {' '.join(header_parts)}"]

    # Extract description
    desc_tag = member_div.find("p", class_="description")
    if desc_tag:
        desc = _tag_to_md(desc_tag, inline=True).strip()
        if desc:
            lines.append(f"\n{desc}")

    # Extract parameters (for functions)
    param_div = member_div.find("div", class_="parameters")
    if param_div:
        val = param_div.find("span", class_="value")
        if val:
            param_text = val.get_text(strip=True)
            if param_text:
                lines.append(f"\nParameter: `{param_text}`")

    # Extract return value
    return_div = member_div.find("div", class_="return")
    if return_div:
        val = return_div.find("span", class_="value")
        if val:
            ret_text = val.get_text(strip=True)
            if ret_text:
                lines.append(f"\nReturns: {ret_text}")

    return "\n".join(lines)


def _parse_legacy_class(section_soup: Tag) -> str:
    """Convert a legacy <h2> class section to markdown matching the v9 format."""
    lines: list[str] = []

    # Class name from h2
    h2 = section_soup.find("h2")
    if h2:
        lines.append(f"# {h2.get_text(strip=True)}")

    # Intro paragraph — first <p class="description"> that's a direct child
    intro_p = section_soup.find("p", class_="description", recursive=False)
    if intro_p:
        intro = _tag_to_md(intro_p, inline=True).strip()
        if intro:
            lines.append(f"\n{intro}")

    # Find the details div
    details = section_soup.find("div", class_="liveapi_object_details")
    if not details:
        return _clean_markdown("\n".join(lines))

    # Canonical paths
    for h4 in details.find_all("h4"):
        if "canonical" in h4.get_text().lower():
            path_h6 = h4.find_next_sibling("h6", class_="path")
            if path_h6:
                if not any("## Canonical Path" in l for l in lines):
                    lines.append("\n## Canonical Path")
                path_text = path_h6.get_text(strip=True)
                lines.append(f"\n```\n{path_text}\n```")

    # Process Children / Properties / Functions sections
    MEMBER_GROUPS = {
        "Children": "liveapi_child_group",
        "Properties": "liveapi_property_group",
        "Functions": "liveapi_function_group",
    }

    for h4 in details.find_all("h4"):
        section_name = h4.get_text(strip=True)
        group_class = MEMBER_GROUPS.get(section_name)
        if not group_class:
            continue

        lines.append(f"\n## {section_name}")

        # Find all member group divs after this h4
        sibling = h4.find_next_sibling()
        while sibling:
            if sibling.name == "h4":
                break
            if isinstance(sibling, Tag) and group_class in (sibling.get("class") or []):
                md = _legacy_member_to_md(sibling)
                if md:
                    lines.append(f"\n{md}")
            sibling = sibling.find_next_sibling()

    return _clean_markdown("\n".join(lines))


def fetch_legacy(output_dir: Path) -> None:
    """Fetch the legacy single-page LOM doc and split into per-class files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching legacy LOM page from {LEGACY_URL} ...")
    html = fetch_page(LEGACY_URL)
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup

    version_match = re.search(r"Ableton Live version ([\d.]+)", str(article))
    if version_match:
        print(f"  Documentation version: Live {version_match.group(1)}")

    # Find all class sections by their h2 anchors
    class_headings = article.find_all("h2", id=re.compile(r"^live_obj_anchor_"))

    count = 0
    for h2 in class_headings:
        title = re.sub(r"^live_obj_anchor_", "", h2.get("id", ""))
        slug = _slug_from_title(title)

        # Collect h2 + all siblings until the next h2
        section_parts = [str(h2)]
        sibling = h2.find_next_sibling()
        while sibling:
            if sibling.name == "h2":
                break
            section_parts.append(str(sibling))
            sibling = sibling.find_next_sibling()

        section_soup = BeautifulSoup("".join(section_parts), "html.parser")
        md = _parse_legacy_class(section_soup)

        out_file = output_dir / f"{slug}.md"
        out_file.write_text(md)
        count += 1

        print(f"  {title} → {slug}.md ({len(md)} chars)")

    # Save intro as lom.md
    intro_parts = []
    for child in article.children:
        if isinstance(child, Tag) and child.name == "h2" and child.get("id", "").startswith("live_obj_anchor_"):
            break
        intro_parts.append(str(child))
    intro_md = _clean_markdown(_tag_to_md(BeautifulSoup("".join(intro_parts), "html.parser")))
    (output_dir / "lom.md").write_text(intro_md)
    print(f"\n  Index → lom.md ({len(intro_md)} chars)")

    print(f"\nDone. {count} classes saved to {output_dir}/")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Max for Live LOM docs from docs.cycling74.com")
    parser.add_argument("-o", "--output", type=Path, help="Output directory")
    parser.add_argument("--legacy", action="store_true", help="Fetch Max 8 legacy docs (single-page format)")
    args = parser.parse_args()

    if args.legacy:
        output_dir = args.output or Path("doc/max-for-live-docs/8.0")
        fetch_legacy(output_dir)
    else:
        if args.output:
            output_dir = args.output
        else:
            print("Detecting documentation version...")
            index_html = fetch_page(f"{BASE_URL}/")
            version_match = re.search(r"Max (\d+)", index_html)
            folder_name = version_match.group(1) + ".0" if version_match else "latest"
            output_dir = Path("doc/max-for-live-docs") / folder_name
        fetch_current(output_dir)


if __name__ == "__main__":
    main()

"""Build a distributable stub package for a given Live version.

Creates a PEP 561 stub-only package that type checkers auto-discover when installed.
The package installs as `Live-stubs/` so `import Live` resolves to the stubs.

Outputs:
  - A wheel (.whl) and sdist (.tar.gz) in dist/
  - A zip archive in dist/ for GitHub release

Usage:
    python tools/publish/build_package.py 12.3.6
    python tools/publish/build_package.py 12.3.6 --post 1
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

PYPROJECT_TEMPLATE = """\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "ableton-live-stubs"
version = "{version}"
description = "PEP 561 type stubs for Ableton Live's Python API"
readme = "README.md"
license = "MIT"
requires-python = ">=3.10"
keywords = ["ableton", "live", "stubs", "typing"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Typing :: Stubs Only",
]

[project.urls]
Homepage = "https://github.com/PhotonicVelocity/LiveAPI"

[tool.hatch.build.targets.wheel]
packages = ["Live-stubs"]
"""

README_TEMPLATE = """\
# ableton-live-stubs

PEP 561 type stubs for Ableton Live {live_version}'s Python API.

## Installation

```
pip install ableton-live-stubs=={version}
```

## Usage

Once installed, type checkers (pyright, mypy) automatically discover the `Live` module stubs.
No configuration needed.

```python
from Live.Application import Application
from Live.Song import Song
```

## Manual setup (without pip)

Download the zip from the
[GitHub release](https://github.com/PhotonicVelocity/LiveAPI/releases/tag/v{live_version})
and add the extracted `Live/` directory to your type checker's search path:

```json
// pyrightconfig.json
{{
  "extraPaths": ["path/to/Live-stubs"]
}}
```

## Source

Generated from runtime introspection of Ableton Live {live_version}.
See [LiveAPI](https://github.com/PhotonicVelocity/LiveAPI) for details.
"""


def build_package(live_version: str, post: int | None = None) -> None:
    stubs_src = REPO_ROOT / "stubs" / live_version / "Live"
    if not stubs_src.is_dir():
        print(f"Error: {stubs_src} does not exist", file=sys.stderr)
        sys.exit(1)

    version = f"{live_version}.post{post}" if post else live_version

    dist_dir = REPO_ROOT / "dist"
    dist_dir.mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        build_dir = Path(tmp)

        # Copy stubs as Live-stubs/ (PEP 561 naming)
        stubs_dest = build_dir / "Live-stubs"
        shutil.copytree(stubs_src, stubs_dest)

        # Write pyproject.toml
        (build_dir / "pyproject.toml").write_text(PYPROJECT_TEMPLATE.format(version=version))

        # Write README
        (build_dir / "README.md").write_text(
            README_TEMPLATE.format(version=version, live_version=live_version)
        )

        # Build wheel + sdist
        print(f"Building ableton-live-stubs {version} ...")
        subprocess.run(
            [sys.executable, "-m", "build", "--outdir", str(dist_dir)],
            cwd=build_dir,
            check=True,
        )

    # Create zip for GitHub release (outside dist/ so PyPI upload doesn't pick it up)
    release_dir = REPO_ROOT / "release"
    release_dir.mkdir(parents=True, exist_ok=True)
    zip_name = f"ableton-live-stubs-{version}"
    zip_path = release_dir / zip_name
    shutil.make_archive(str(zip_path), "zip", stubs_src.parent, "Live")
    print(f"\nGitHub release zip: {zip_path}.zip")

    print(f"\nBuilt in {dist_dir}/:")
    for f in sorted(dist_dir.iterdir()):
        if f.is_file():
            print(f"  {f.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build stub package for a Live version")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--post", type=int, default=None, help="Post-release number (e.g. 1 → 12.3.6.post1)")
    args = parser.parse_args()
    build_package(args.version, args.post)


if __name__ == "__main__":
    main()

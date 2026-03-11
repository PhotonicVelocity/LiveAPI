"""
Generate typed Python stubs from captured Live API data.

Usage:
    python tools/generate_stubs.py build/12.3.6

Reads Live.json (and optionally probe_results.json) from the given directory
and generates stub files in <dir>/Live/.
"""

import argparse
import os
import sys

# Add repo root to path so we can import the generator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "apicapture"))

from generators.StubGenerator import StubGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate typed Python stubs from Live API capture data")
    parser.add_argument("build_dir", help="Directory containing Live.json (e.g., build/12.3.6)")
    parser.add_argument("--version", help="Live version string (default: inferred from directory name)")
    args = parser.parse_args()

    build_dir = os.path.abspath(args.build_dir)
    if not os.path.isdir(build_dir):
        print(f"Error: {build_dir} is not a directory")
        sys.exit(1)

    json_file = os.path.join(build_dir, "Live.json")
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found")
        sys.exit(1)

    version = args.version or os.path.basename(build_dir)

    generator = StubGenerator(build_dir, version=version)
    generator.generate()
    print(f"Stubs generated in {os.path.join(build_dir, 'Live')}/")


if __name__ == "__main__":
    main()

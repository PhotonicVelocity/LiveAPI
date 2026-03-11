"""
Install the APICapture Remote Script into Ableton Live's User Library.

Copies the apicapture package into the Remote Scripts folder and patches
the output folder placeholder so generated files land in build/<version>/.

This script only works for Live 11+ (User Library based).

Flags:
  --user_lib_dir  Path to User Library (if non-standard)
  --user          Override detected username
  --name          Name of the installed Remote Script folder (default: APICapture)
"""

import codecs
import os
import shutil
import getpass
import argparse
import platform

USERLIBWIN = "C:\\Users\\{user}\\Documents\\Ableton\\User Library"
USERLIBMAC = "/Users/{user}/Music/Ableton/User Library"

parser = argparse.ArgumentParser(description="Install remote script")
parser.add_argument("--user_lib_dir", required=False)
parser.add_argument("--user", required=False)
parser.add_argument("--name", required=False)

args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
src_dir = os.path.join(script_dir, "apicapture")

user = args.user or getpass.getuser()

user_scripts_path = os.path.join(
    args.user_lib_dir
    or (USERLIBWIN if platform.system() == "Windows" else USERLIBMAC).format(user=user),
    "Remote Scripts",
)

user_script_dir = os.path.join(
    user_scripts_path, args.name or "APICapture"
)

if os.path.isdir(user_script_dir):
    shutil.rmtree(user_script_dir)

shutil.copytree(src_dir, user_script_dir)

outdir = os.path.join(repo_root, "build")

with codecs.open(os.path.join(user_script_dir, "__init__.py"), "r", "utf-8") as f:
    content = f.read()

with codecs.open(os.path.join(user_script_dir, "__init__.py"), "w", "utf-8") as f:
    content = content.replace("%%%OUTPUTFOLDER%%%", outdir)
    f.write(content)

print(
    f"""
    Installed to: {user_script_dir}
    Output folder: {outdir}

    Restart Ableton to activate.
    """
)

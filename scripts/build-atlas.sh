#!/usr/bin/env bash
# Regenerate the Compliance Atlas reading-view HTML from README.md.
# Requires: pandoc, python3.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
python3 scripts/build_atlas.py README.md dist/atlas.html

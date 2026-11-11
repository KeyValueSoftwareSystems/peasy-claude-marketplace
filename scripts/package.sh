#!/usr/bin/env bash
# Builds installable plugin files into dist/:  dist/<name>.plugin
# Upload them in Claude (Customize → Plugins), or attach them to a GitHub release.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for p in plugins/*/; do
  name=$(basename "$p")
  rm -f "dist/$name.plugin"
  (cd "$p" && zip -qr "../../dist/$name.plugin" . -x '*.DS_Store')
  echo "dist/$name.plugin"
done

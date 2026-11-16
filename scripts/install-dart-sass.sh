#!/usr/bin/env bash
# Install Dart Sass and print the directory to prepend to PATH.
#
# Hugo's dartsass transpiler talks to the compiler over the embedded
# protocol. The plain `sass` npm package is pure JS and cannot do that
# ("sass --embedded is unavailable in pure JS mode"), so install
# `sass-embedded`, which bundles the standalone Dart Sass binary.
set -euo pipefail

npm install --global sass-embedded \
  --registry="${NPM_REGISTRY:-https://registry.npmmirror.com}" \
  --no-audit --no-fund >/dev/null

find "$(npm root -g)" -type d -path '*/dart-sass' | head -n 1
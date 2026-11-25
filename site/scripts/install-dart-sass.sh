#!/usr/bin/env bash
# Install Dart Sass and print the directory to prepend to PATH.
#
# Hugo's dartsass transpiler executes a `sass` binary. The pure-JS `sass`
# npm package cannot serve it, and the sass-embedded platform package can
# end up nested under node_modules on CI. Installing sass-embedded
# globally is the reliable path (same approach as the previous theme).
set -euo pipefail

npm install --global sass-embedded@1.77.8 \
  --registry="${NPM_REGISTRY:-https://registry.npmmirror.com}" \
  --no-audit --no-fund >/dev/null

find "$(npm root -g)" -type d -path '*/dart-sass' | head -n 1
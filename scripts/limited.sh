#!/usr/bin/env bash
# Run a command with its own memory limit, in its own systemd scope, so that a runaway test only kills itself.
# Without this, the kernel can kill the whole editor with every session in it (2026-11-07: a probe took 107 GB).
#   scripts/limited.sh [-m 32G] <command> ...
set -euo pipefail
max=32G
if [ "${1:-}" = "-m" ]; then max="$2"; shift 2; fi
exec systemd-run --user --scope --quiet -p "MemoryMax=$max" -p MemorySwapMax=0 -- "$@"

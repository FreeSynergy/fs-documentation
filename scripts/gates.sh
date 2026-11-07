#!/usr/bin/env bash
# All gates before a tag, as one command with a real exit code.
#   scripts/gates.sh <repo root> && git push ... && git tag ...
# Run it on a fresh clone. Do not rely on `set -e` in a tool call: the shell wrapper runs commands inside an
# `&&` list, where bash ignores it. Inside this script it works.
set -euo pipefail
root="$(cd "$1" && pwd)"
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
rules="$here/check_rust_rules.py"
cd "$root"
export CARGO_BUILD_JOBS="${CARGO_BUILD_JOBS:-4}"
export TMPDIR="${TMPDIR_GATES:-/srv/FreeSynergy/.scratch}"
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "gates FAILED: uncommitted changes in $root" >&2
  exit 1
fi
fmt_args=()
for manifest in crates/*/Cargo.toml; do
  [ -f "$manifest" ] || continue
  fmt_args+=(-p "$(sed -n 's/^name = "\(.*\)"/\1/p' "$manifest" | head -1)")
done
cargo fmt --check "${fmt_args[@]}"
"$here/limited.sh" cargo clippy --workspace --all-targets --all-features -- -D warnings
"$here/limited.sh" cargo test --workspace --all-features
python3 -I "$rules" "$root"
echo "gates ok: $root at $(git rev-parse --short HEAD)"

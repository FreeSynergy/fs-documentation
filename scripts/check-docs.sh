#!/usr/bin/env bash
# All documentation checks of the CI step "Check component documentation standard", run locally.
#   scripts/check-docs.sh
# Exit code is non-zero if any check fails. Fix stale indexes with the generators (without --check).
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
fail=0
run() {
  echo "== $*"
  python3 "scripts/$1" "${@:2}" >/dev/null || { echo "FAILED: $*" >&2; python3 "scripts/$1" "${@:2}" | tail -15; fail=1; }
}
run check_components.py --lang en
run gen_component_indexes.py --lang en --check
run check_components.py --lang de
run gen_component_indexes.py --lang de --check
run gen_frontend_indexes.py --check
[ "$fail" -eq 0 ] && echo "check-docs ok" || echo "check-docs FAILED" >&2
exit "$fail"

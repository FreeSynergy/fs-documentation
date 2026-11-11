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
# Same as the CI steps "Publish the decision records" and "Build MkDocs site" (strict).
MKDOCS="$(command -v mkdocs || true)"
[ -z "$MKDOCS" ] && [ -x /srv/FreeSynergy/.scratch/venv-mkdocs/bin/mkdocs ] && MKDOCS=/srv/FreeSynergy/.scratch/venv-mkdocs/bin/mkdocs
if [ -n "$MKDOCS" ]; then
  echo "== gen_decisions.py + mkdocs build --strict"
  python3 scripts/gen_decisions.py >/dev/null || { echo "FAILED: gen_decisions.py" >&2; fail=1; }
  site="$(mktemp -d)"
  "$MKDOCS" build --strict -q -d "$site" >"$site.log" 2>&1 || { echo "FAILED: mkdocs build --strict" >&2; grep -E "WARNING|ERROR|Aborted" "$site.log" | head -15; fail=1; }
  rm -rf "$site" "$site.log"
else
  echo "SKIPPED: mkdocs build --strict (mkdocs not installed; CI runs it: pip install -r requirements.txt)" >&2
fi
[ "$fail" -eq 0 ] && echo "check-docs ok" || echo "check-docs FAILED" >&2
exit "$fail"

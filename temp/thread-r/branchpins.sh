#!/usr/bin/env bash
# branchpins.sh <repo> <branch>: move FreeSynergy dependency pins of a branch to v0.0.1 (deps only), push
set -euo pipefail
r=$1; b=$2; wt=/srv/FreeSynergy/.scratch/tr/wtb-$r-${b//\//_}
cd /srv/FreeSynergy/$r; git fetch -q
git worktree add -q --detach "$wt" origin/$b; cd "$wt"
python3 /srv/FreeSynergy/.scratch/tr/reset.py "$PWD" --deps-only >/dev/null
if git diff --quiet; then echo "nochange $r $b"; else
git commit -qam "Dependencies on v0.0.1 (version reset, ADR 0064); branch conversion only, not built

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git push -q origin HEAD:refs/heads/$b; echo "OK $r $b"; fi
cd /srv/FreeSynergy/$r; git worktree remove --force "$wt"

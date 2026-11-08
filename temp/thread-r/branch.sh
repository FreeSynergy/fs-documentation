#!/usr/bin/env bash
# branch.sh <repo> <branch>: one conversion commit on the branch, pushed, no merge, no tag
set -euo pipefail
r=$1; b=$2; wt=/srv/FreeSynergy/.scratch/tr/wt-$r-${b//\//_}
cd /srv/FreeSynergy/$r
git worktree add -q --detach "$wt" origin/$b
cd "$wt"
files=$(grep -rIl "fs-store\|fs_store" . --exclude-dir=target --exclude-dir=.git --exclude-dir=.claude || true)
[ -n "$files" ] && echo "$files" | xargs sed -i -E \
 -e 's#FreeSynergy/fs-store(\.git)?"?, tag = "v[0-9.]+"#FreeSynergy/fs-objects", tag = "v0.5.0"#g' \
 -e 's#FreeSynergy/fs-store#FreeSynergy/fs-objects#g' -e 's/fs-store/fs-objects/g; s/fs_store/fs_objects/g'
for d in $(find . -name 'fs-store*' -not -path './.git/*' -not -path '*/target/*' | sort -r); do git mv "$d" "$(dirname $d)/$(basename $d | sed s/fs-store/fs-objects/)"; done
git add -A
git commit -qm "Switch fs-store to fs-objects (ADR 0060); branch conversion only, not built

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git push -q origin HEAD:refs/heads/$b
cd /srv/FreeSynergy/$r; git worktree remove --force "$wt"
echo "OK $r $b"

#!/usr/bin/env bash
# finish.sh <repo> : commit fixes, gates, push, tag from Cargo.toml version, record
set -euo pipefail
r=$1; cd /srv/FreeSynergy/$r
git add -u; git diff --cached --quiet || git commit -qm "fix: adapt to fs-objects API

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
bash /srv/FreeSynergy/.scratch/t5-gates/gates.sh "$PWD"
v=v$(sed -n '0,/^version = "\(.*\)"/s//\1/p' Cargo.toml | head -1)
git push -q origin main; git tag "$v"; git push -q origin "$v"
echo "$r $v" >> /srv/FreeSynergy/.scratch/tr/tags.txt; echo "DONE $r $v"

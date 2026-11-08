#!/usr/bin/env bash
# reset.sh <repo> : stage step for one repo (commit, push main, fresh-clone gates, tag v0.0.1)
set -euo pipefail
r=$1; T=/srv/FreeSynergy/.scratch/tr; cd /srv/FreeSynergy/$r
git checkout -q main; git pull -q --rebase
python3 $T/reset.py "$PWD"
cargo fmt --all 2>/dev/null || true
cargo build -q --workspace --all-targets --all-features 2>&1 | tail -3
git add -u; git diff --cached --quiet || git commit -qm "version 0.0.1: reset of the version numbers, dependencies on v0.0.1

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git pull -q --rebase; git push -q origin main
fc=$T/fc-$r; rm -rf $fc; git clone -q git@github.com:FreeSynergy/$r.git $fc
bash /srv/FreeSynergy/.scratch/t5-gates/gates.sh $fc > $T/$r.reset.log 2>&1 || { echo "GATES FAILED $r (log $T/$r.reset.log)"; exit 1; }
rm -rf $fc
git tag v0.0.1; git push -q origin v0.0.1; echo "TAGGED $r v0.0.1"

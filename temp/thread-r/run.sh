#!/usr/bin/env bash
# run.sh <repo>: pull, convert, fmt, minor bump, commit, gates, push, tag, record tag
set -euo pipefail
T=/srv/FreeSynergy/.scratch/tr; r=$1; cd /srv/FreeSynergy/$r
git pull -q --ff-only
files=$(grep -rIl "fs-store\|fs_store\|FreeSynergy/fs-" . --exclude-dir=target --exclude-dir=.git --exclude-dir=.claude --exclude=Cargo.lock || true)
exprs=(-e 's#FreeSynergy/fs-store", tag = "v[0-9.]+"#FreeSynergy/fs-objects", tag = "v0.5.0"#g')
while read -r n t; do exprs+=(-e "s#(FreeSynergy/$n\", tag = \")v[0-9.]+#\1$t#g"); done < $T/tags.txt
exprs+=(-e 's/fs-store/fs-objects/g; s/fs_store/fs_objects/g')
[ -n "$files" ] && echo "$files" | xargs sed -i -E "${exprs[@]}"
last=$(git tag --sort=-v:refname | head -1); IFS=. read -r a b c <<<"${last#v}"
new="$a.$((b+1)).0"
grep -q "^version = \"${last#v}\"" Cargo.toml && sed -i "0,/^version = \"${last#v}\"/s//version = \"$new\"/" Cargo.toml || echo "WARN: version line not found, tag $new only"
cargo fmt --all
cargo update -q -p fs-objects 2>/dev/null || true
git add -u; git commit -qm "Switch to fs-objects (ADR 0060); version $new

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
bash /srv/FreeSynergy/.scratch/t5-gates/gates.sh "$PWD"
git push -q origin main; git tag "v$new"; git push -q origin "v$new"
echo "$r v$new" >> $T/tags.txt; echo "DONE $r v$new"

#!/usr/bin/env python3
"""Generic restructuring: move/rename files by regex rules, keep every link intact.

Replaces one-off move scripts (`_archive/move_*.py`). Link arithmetic follows
`migrate_links.py` (exact, no guessing) but works per file, so a rule may rename
files, insert directories (e.g. a version level) or merge trees.

RULES
    One rule:  REGEX => REPLACEMENT
    REGEX is matched with re.fullmatch against the repo-relative POSIX path of
    every file under --scope. First matching rule wins. REPLACEMENT uses Python
    group syntax (\\1, \\g<name>) and lookups {TABLE:GROUP}: the value of named
    group GROUP is looked up in TABLE (from --table NAME=FILE.tsv, two columns
    key<TAB>value); missing keys use --default NAME=VALUE or abort.

    Rules come from --rule (repeatable) and/or --rules FILE (one per line,
    `#` comments, blank lines ignored).

WHAT IT DOES
    1. Builds the file map old -> new, aborts on collisions.
    2. Rewrites relative Markdown links in every .md under --links-in (default
       docs): links from moved files and links to moved files/dirs. A directory
       link follows the directory's index.md (or where its index.md would go).
       Links to missing files are mapped by the rules too (--links-only does just
       this). Code fences, external links and pure anchors are left alone.
    3. --nav FILE: rewrites docs-relative paths (mkdocs.yml nav) via the map.
    4. --sync-state FILE: re-keys doc_sync state (keys relative to docs/<lang>/).
    5. With --apply: writes, `git mv` (retries while index.lock is held) (plain move for untracked files), removes
       empty directories. Without --apply: dry run, prints a summary.

EXAMPLES
    # masks/<p>/x.md -> frontends/<p>/<version>/x.md, index.md stays on program level
    python3 scripts/move.py --scope docs/en --scope docs/de \\
      --rules scripts/rules/masks_to_frontends.rules \\
      --table version=temp/frontend-versions.tsv --default version=latest \\
      --nav mkdocs.yml --sync-state temp/sync_state.json            # dry run
    ... --apply

    # rename a single folder everywhere
    python3 scripts/move.py --scope docs \\
      --rule 'docs/(en|de)/data/geodaten/(.*)=>docs/\\1/data/geodata/\\2' --apply

If a run is interrupted while moving, repeat it with --moves-only (links, nav and
state were already rewritten before the first move).

Afterwards: `mkdocs build` as verification (CONVENTIONS §9).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\n]+?)(\))")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
LOOKUP_RE = re.compile(r"\{(\w+):(\w+)\}")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


# ---------------------------------------------------------------- rules ----
def load_rules(args):
    raw = list(args.rule or [])
    for f in args.rules or []:
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                raw.append(line)
    rules = []
    for r in raw:
        if "=>" not in r:
            sys.exit(f"rule needs 'REGEX => REPLACEMENT': {r}")
        pat, rep = (s.strip() for s in r.split("=>", 1))
        rules.append((re.compile(pat), rep))
    if not rules:
        sys.exit("no rules given (--rule / --rules)")
    return rules


def load_tables(args):
    tables, defaults = {}, {}
    for spec in args.table or []:
        name, path = spec.split("=", 1)
        t = {}
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                k, _, v = line.partition("\t")
                t[k.strip()] = v.strip()
        tables[name] = t
    for spec in args.default or []:
        name, val = spec.split("=", 1)
        defaults[name] = val
    return tables, defaults


def apply_rules(path, rules, tables, defaults, missing):
    for pat, rep in rules:
        m = pat.fullmatch(path)
        if not m:
            continue

        def lookup(lm):
            table, group = lm.group(1), lm.group(2)
            key = m.group(group)
            val = tables.get(table, {}).get(key)
            if val is None:
                if table not in defaults:
                    sys.exit(f"no value for {table}[{key}] ({path}) and no --default")
                missing.setdefault(table, set()).add(key)
                val = defaults[table]
            return val.replace("\\", "\\\\")

        return m.expand(LOOKUP_RE.sub(lookup, rep))
    return path


# ------------------------------------------------------------- mapping ----
def rel(p):
    return Path(os.path.relpath(p, ROOT)).as_posix()


def build_map(args, rules, tables, defaults):
    missing = {}
    fmap = {}
    for scope in args.scope:
        for dirpath, dirs, names in os.walk(ROOT / scope):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for n in names:
                old = rel(os.path.join(dirpath, n))
                new = apply_rules(old, rules, tables, defaults, missing)
                if new != old:
                    fmap[old] = os.path.normpath(new)
    # collisions
    seen = {}
    for old, new in fmap.items():
        if new in seen:
            sys.exit(f"collision: {seen[new]} and {old} -> {new}")
        seen[new] = old
        if (ROOT / new).exists() and new not in fmap:
            sys.exit(f"collision: target exists and is not moved: {new}")
    return fmap, missing, rules, tables, defaults


def dir_target(d, fmap, rules, tables, defaults):
    """Where does directory d go? Follows its (real or hypothetical) index.md."""
    idx = f"{d}/index.md"
    if idx in fmap:
        return os.path.dirname(fmap[idx])
    new = apply_rules(idx, rules, tables, defaults, {})
    return os.path.dirname(new) if new != idx else d


# --------------------------------------------------------------- links ----
def map_target(t, fmap, ctx):
    if t in fmap:
        return fmap[t]
    if (ROOT / t).is_dir() or not os.path.splitext(t)[1]:
        return dir_target(t, fmap, *ctx)
    if not (ROOT / t).exists():
        # target missing (not written yet, or moved earlier): map it by the rules anyway
        return os.path.normpath(apply_rules(t, *ctx, {}))
    return t


def rewrite_links(path, fmap, ctx):
    text = (ROOT / path).read_text(encoding="utf-8")
    old_dir = os.path.dirname(path)
    new_dir = os.path.dirname(fmap.get(path, path))
    changes = []

    def repl(m):
        head, inner, tail = m.groups()
        pm = re.match(r"^(\S+)(\s+.*)?$", inner)
        if not pm:
            return m.group(0)
        link, title = pm.group(1), pm.group(2) or ""
        if link.startswith("#") or SCHEME_RE.match(link) or link.startswith("/"):
            return m.group(0)
        anchor = ""
        if "#" in link:
            link, a = link.split("#", 1)
            anchor = "#" + a
        trailing = link.endswith("/")
        t_old = os.path.normpath(os.path.join(old_dir, link)) if link else old_dir
        t_new = map_target(t_old, fmap, ctx)
        if t_new == t_old and new_dir == old_dir:
            return m.group(0)
        new_link = os.path.relpath(t_new, new_dir).replace(os.sep, "/")
        if new_link == ".":
            new_link = "./"
        if trailing and not new_link.endswith("/"):
            new_link += "/"
        new_inner = new_link + anchor + title
        if new_inner == inner:
            return m.group(0)
        changes.append((inner, new_inner))
        return head + new_inner + tail

    out, fence = [], False
    for line in text.splitlines(keepends=True):
        if FENCE_RE.match(line):
            fence = not fence
            out.append(line)
            continue
        out.append(line if fence else LINK_RE.sub(repl, line))
    return "".join(out), changes


def rewrite_nav(navfile, fmap, docs_dir):
    text = (ROOT / navfile).read_text(encoding="utf-8")
    pre = docs_dir.rstrip("/") + "/"
    short = {o[len(pre):]: n[len(pre):] for o, n in fmap.items()
             if o.startswith(pre) and n.startswith(pre)}
    dirs = {}
    for o, n in short.items():
        if o.endswith("/index.md"):
            dirs[o[:-len("index.md")]] = n[:-len("index.md")]
    count = 0

    def repl(m):
        nonlocal count
        tok = m.group(0)
        new = short.get(tok) or dirs.get(tok)
        if new:
            count += 1
            return new
        return tok

    out = re.sub(r"[\w.\-/]+(?:\.md|/)", repl, text)
    return out, count


def rekey_state(statefile, fmap, docs_dir):
    data = json.loads((ROOT / statefile).read_text(encoding="utf-8"))
    entries = data.get("entries", {})
    pre = docs_dir.rstrip("/") + "/"
    keymap = {}
    for o, n in fmap.items():
        if o.startswith(pre) and n.startswith(pre):
            o_parts, n_parts = o[len(pre):].split("/", 1), n[len(pre):].split("/", 1)
            if len(o_parts) == 2 and len(n_parts) == 2:
                keymap[o_parts[1]] = n_parts[1]
    moved = 0
    for o, n in keymap.items():
        if o in entries and n not in entries:
            entries[n] = entries.pop(o)
            entries[n].setdefault("history", []).append(
                {"at": "move.py", "event": f"renamed from {o}"})
            moved += 1
    return data, moved


def git_mv(o, n, tries=10):
    """git mv with retries: another process (e.g. a background job) may hold index.lock."""
    for i in range(tries):
        r = subprocess.run(["git", "-C", str(ROOT), "mv", o, n], capture_output=True, text=True)
        if r.returncode == 0:
            return
        if "index.lock" not in r.stderr or i == tries - 1:
            sys.exit(f"git mv {o} {n} failed: {r.stderr.strip()}\n"
                     "resume with the same command plus --moves-only")
        time.sleep(1 + i)


# ---------------------------------------------------------------- main ----
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", action="append", required=True,
                    help="tree whose files the rules apply to (repeatable)")
    ap.add_argument("--rule", action="append")
    ap.add_argument("--rules", action="append", help="rules file")
    ap.add_argument("--table", action="append", metavar="NAME=FILE.tsv")
    ap.add_argument("--default", action="append", metavar="NAME=VALUE")
    ap.add_argument("--links-in", default="docs", help="tree whose links are rewritten")
    ap.add_argument("--docs-dir", default="docs", help="mkdocs docs_dir (for --nav/--sync-state)")
    ap.add_argument("--nav", action="append", help="file with docs-relative paths (mkdocs.yml)")
    ap.add_argument("--sync-state", help="doc_sync state JSON to re-key")
    ap.add_argument("--list", action="store_true", help="print every move")
    ap.add_argument("--missing-out", help="write missing table keys to this file")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--links-only", action="store_true",
                    help="move nothing; only repoint links whose targets match the rules "
                         "(after someone else moved files, or for links to missing files)")
    ap.add_argument("--moves-only", action="store_true",
                    help="only move files (resume an interrupted run; links/nav/state already done)")
    args = ap.parse_args()

    rules = load_rules(args)
    tables, defaults = load_tables(args)
    fmap, missing, *_ = build_map(args, rules, tables, defaults)
    if args.links_only:
        fmap = {}
    ctx = (rules, tables, defaults)

    print(f"files to move: {len(fmap)}")
    for o, n in (sorted(fmap.items()) if args.list else sorted(fmap.items())[:10]):
        print(f"  {o}\n    -> {n}")
    if not args.list and len(fmap) > 10:
        print(f"  … ({len(fmap) - 10} more, --list shows all)")
    for table, keys in missing.items():
        print(f"default used for {table}: {len(keys)} keys")
        if args.missing_out:
            Path(args.missing_out).write_text("\n".join(sorted(keys)) + "\n", encoding="utf-8")

    if args.moves_only:
        args.nav, args.sync_state, args.links_in = None, None, None
    # links
    link_files, link_total, rewrites = 0, 0, {}
    for dirpath, dirs, names in (os.walk(ROOT / args.links_in) if args.links_in else []):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for n in names:
            if n.endswith(".md"):
                p = rel(os.path.join(dirpath, n))
                out, ch = rewrite_links(p, fmap, ctx)
                if ch:
                    rewrites[p] = out
                    link_files += 1
                    link_total += len(ch)
    print(f"links rewritten: {link_total} in {link_files} files")

    navs = {}
    for nf in args.nav or []:
        out, c = rewrite_nav(nf, fmap, args.docs_dir)
        navs[nf] = out
        print(f"nav paths rewritten in {nf}: {c}")

    state = None
    if args.sync_state:
        state, c = rekey_state(args.sync_state, fmap, args.docs_dir)
        print(f"sync-state keys renamed: {c}")

    if not args.apply:
        print("dry run — nothing written (use --apply)")
        return 0

    for p, out in rewrites.items():
        (ROOT / p).write_text(out, encoding="utf-8")
    for nf, out in navs.items():
        (ROOT / nf).write_text(out, encoding="utf-8")
    if state is not None:
        (ROOT / args.sync_state).write_text(
            json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tracked = set(subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True,
                                 text=True, check=True).stdout.splitlines())
    for o, n in sorted(fmap.items()):
        (ROOT / n).parent.mkdir(parents=True, exist_ok=True)
        if o in tracked:
            git_mv(o, n)
        else:
            shutil.move(str(ROOT / o), str(ROOT / n))
    # remove empty source directories
    for o in sorted({os.path.dirname(o) for o in fmap}, key=len, reverse=True):
        d = ROOT / o
        while d != ROOT and d.is_dir() and not any(d.iterdir()):
            d.rmdir()
            d = d.parent
    print("applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

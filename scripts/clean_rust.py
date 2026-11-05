#!/usr/bin/env python3
"""Clean Rust build output across all FreeSynergy repos (ADR 0041).

Finds every `target/` directory below ROOT (default /srv/FreeSynergy) — only directories that sit
next to a Cargo.toml — and removes:
  * incremental caches (`target/*/incremental`)            always
  * debug builds (`target/debug`)        if older than --days (default 3) or if --all
  * everything (`target/`)               with --all
Reports sizes before/after. Dry run by default; --apply deletes.

    python3 scripts/clean_rust.py                 # show what would be removed
    python3 scripts/clean_rust.py --apply         # clean incremental + old debug builds
    python3 scripts/clean_rust.py --apply --all   # remove all target/ dirs
    python3 scripts/clean_rust.py --max-gb 10 --apply   # also clean everything if total > 10 GB
"""
import argparse, os, shutil, sys, time
from pathlib import Path

def size(p):
    total = 0
    for dp, _, fs in os.walk(p):
        for f in fs:
            try: total += os.lstat(os.path.join(dp, f)).st_size
            except OSError: pass
    return total

def gb(n): return f"{n/1e9:.2f} GB"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="/srv/FreeSynergy")
    ap.add_argument("--days", type=float, default=3)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--max-gb", type=float)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    targets = [p for p in Path(a.root).rglob("target")
               if p.is_dir() and (p.parent / "Cargo.toml").exists() and ".git" not in p.parts]
    total = sum(size(t) for t in targets)
    print(f"target dirs: {len(targets)}, total {gb(total)}")
    force_all = a.all or (a.max_gb is not None and total > a.max_gb * 1e9)
    victims = []
    for t in targets:
        if force_all:
            victims.append(t); continue
        victims += [p for p in t.glob("*/incremental") if p.is_dir()]
        dbg = t / "debug"
        if dbg.is_dir() and time.time() - dbg.stat().st_mtime > a.days * 86400:
            victims.append(dbg)
    freed = 0
    for v in victims:
        s = size(v); freed += s
        print(f"  {'remove' if a.apply else 'would remove'} {v} ({gb(s)})")
        if a.apply: shutil.rmtree(v, ignore_errors=True)
    print(f"{'freed' if a.apply else 'would free'}: {gb(freed)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

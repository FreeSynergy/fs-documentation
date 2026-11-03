#!/usr/bin/env python3
"""Einmal-Migration: components/<typgruppe>/<komponente>/ ->
components/<band>/<typgruppe>/<komponente>/  (ADr 0001 und 0004).

Nutzt die Zuordnung aus scripts/gen_component_indexes.py (ASSIGNMENT).
Bewegt mit `git mv`, damit der Umzug als Rename erkennbar ist. Erzeugte
Kategorie-Indexdateien am alten Platz werden geloescht (der Generator schreibt
sie an neuer Stelle neu).

Reihenfolge: erst dieser Lauf, dann scripts/fix_links.py, dann
scripts/gen_component_indexes.py, dann mkdocs build.

Aufruf:
    python3 scripts/_archive/move_component_bands.py --dry-run
    python3 scripts/_archive/move_component_bands.py
"""
import argparse
import os
import subprocess
import sys

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPTS)
import gen_component_indexes as gen  # noqa: E402

ROOT = gen.ROOT
COMPONENTS = gen.COMPONENTS


def git(*a, dry=False):
    if dry:
        print("  git " + " ".join(a))
        return
    subprocess.run(["git", *a], check=True, cwd=ROOT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    moved = skipped = 0
    for band, groups in gen.ASSIGNMENT.items():
        for cat, names in groups.items():
            for name in names:
                if name == "base":
                    src, dst = COMPONENTS / "basics" / "base.md", \
                               COMPONENTS / band / cat / "base.md"
                else:
                    src, dst = COMPONENTS / cat / name, COMPONENTS / band / cat / name
                if dst.exists():
                    skipped += 1
                    continue
                if not src.exists():
                    print(f"  ! fehlt: {src.relative_to(ROOT)}")
                    continue
                rel_src = str(src.relative_to(ROOT))
                rel_dst = str(dst.relative_to(ROOT))
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                git("mv", "-f", rel_src, rel_dst, dry=args.dry_run)
                moved += 1

    # erzeugte Kategorie-Indexseiten am alten Platz (Generator schreibt sie neu)
    for cat in gen.CATEGORY_ORDER:
        old = COMPONENTS / cat / "index.md"
        if old.is_file():
            git("rm", "-q", str(old.relative_to(ROOT)), dry=args.dry_run)

    print(f"verschoben: {moved}, bereits am neuen Platz: {skipped}")
    if not args.dry_run:
        for cat in gen.CATEGORY_ORDER:
            d = COMPONENTS / cat
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

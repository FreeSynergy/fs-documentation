#!/usr/bin/env python3
"""Einmal-Migration: docs/<sprache>/programs/**/skins -> masks (ADR 0007).

Verschiebt alle skins/-Verzeichnisse unter docs/de und docs/en per git mv und
setzt danach die internen Links mit scripts/fix_links.py --force neu.

Aufruf:
    python3 scripts/_archive/move_skins_to_masks.py --dry-run
    python3 scripts/_archive/move_skins_to_masks.py
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dirs = sorted(
        p for lang in ("de", "en")
        for p in (ROOT / "docs" / lang).rglob("skins")
        if p.is_dir()
    )
    print("skins-Verzeichnisse gefunden:", len(dirs))

    for d in dirs:
        target = d.with_name("masks")
        cmd = ["git", "-C", str(ROOT), "mv", str(d.relative_to(ROOT)),
               str(target.relative_to(ROOT))]
        if args.dry_run:
            print(" ".join(cmd))
            continue
        subprocess.run(cmd, check=True)

    if args.dry_run:
        return 0

    subprocess.run([sys.executable, str(ROOT / "scripts" / "fix_links.py"),
                    "--force"], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

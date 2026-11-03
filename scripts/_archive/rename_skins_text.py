#!/usr/bin/env python3
"""Einmal-Migration (ADR 0007): Pfadtexte und Links skins -> masks in docs/.

fix_links.py loest ueber die Namens-Registry auf; nach dem git mv gibt es dort
kein `skins` mehr, also bleiben die skins-Links unaufgeloest. Dieses Skript setzt
deshalb ausschliesslich das Pfadstueck `skins` -> `masks`, und zwar nur dort, wo
es eindeutig ein Pfad ist:

  - in Link-Zielen:  (../wiki/skins/...)  [text](skins/index.md)
  - in Backticks:    `apps/<kategorie>/skins/<programm>/`
  - in Pfad-Zeilen:  programs/apps/wiki/skins/mediawiki/api.md

Prosa („Skin-Dokumentation“, „Skins“) bleibt unveraendert — die heißt weiterhin so,
bis sie spaeter sprachlich folgt.

Aufruf:
    python3 scripts/_archive/rename_skins_text.py --dry-run
    python3 scripts/_archive/rename_skins_text.py
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

# Pfad-Stueck `skins` mit / oder ) oder Backtick oder Zeilenende danach.
PATTERNS = [
    (re.compile(r"(?P<pre>(?:\.\./)+[\w./-]*?)skins(/|\))"), r"\g<pre>masks\g<2>"),
    (re.compile(r"(?P<pre>[\w./<>-]*?/)skins(/|\)|\b)"), r"\g<pre>masks\g<2>"),
    (re.compile(r"\(skins/"), "(masks/"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = files = 0
    for path in sorted(DOCS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new = text
        for pat, rep in PATTERNS:
            new = pat.sub(rep, new)
        if new != text:
            files += 1
            n = sum(1 for a, b in zip(text.splitlines(), new.splitlines()) if a != b)
            changed += n
            print(" ", path.relative_to(ROOT), n, "Zeilen")
            if not args.dry_run:
                path.write_text(new, encoding="utf-8")
    print("Dateien:", files, "| Zeilen:", changed)
    return 0


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Setzt relative Markdown-Links nach einem Umzug von Verzeichnissen korrekt neu.

Reihenfolge: ZUERST dieses Skript laufen lassen (linkt um, Dateien liegen noch alt),
DANN `git mv` ausfuehren. Das Skript geht davon aus, dass die Dateien auf der Platte
noch an ihrer ALTEN Position liegen.

Ein Umzug wird als `ALT=NEU` angegeben (Pfade relativ zum Repo-Stamm), mehrfach moeglich.

    python3 scripts/migrate_links.py --dry-run \
        --move docs/de/gestures=docs/de/interactions/gestures \
        --move docs/de/animations=docs/de/interactions/animations

Ohne --dry-run wird geschrieben. --check prueft (CI): exit 1, wenn es noch zu
setzende Links gaebe (nutzt denselben Lauf wie der Umzug, dry).

Annahmen: Markdown-Links `](pfad)`; keine Links in code fences; keine Spaces in Pfaden.
Externe/absolute/mailto-Links und reine Anker (`#...`) bleiben unberuehrt.
"""
import argparse
import os
import re
import sys
from pathlib import PurePosixPath

ROOT = PurePosixPath(os.path.dirname(os.path.abspath(__file__))).parent  # repo root
LINK_RE = re.compile(r'(!?\[[^\]]*\]\()([^)\n]+?)(\))')


def parse_moves(specs):
    moves = []
    for s in specs:
        if "=" not in s:
            sys.exit(f"--move erwartet ALT=NEU, bekam: {s}")
        old, new = s.split("=", 1)
        moves.append((normalize(str(ROOT / old)), normalize(str(ROOT / new))))
    return moves


def normalize(p):
    return os.path.normpath(p)


def parts(p):
    return PurePosixPath(p).parts


def forward(p, moves):
    """Alte absolute Lage -> neue absolute Lage (Prefix-Tausch, Pfadteile-genau)."""
    pp = parts(p)
    for old, new in moves:
        op = parts(old)
        if pp[:len(op)] == op:
            rest = pp[len(op):]
            return normalize(os.path.join(new, *rest)) if rest else new
    return p


def is_external_or_anchor(target):
    if not target:
        return True
    if target.startswith("#"):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):  # http:, mailto:, ...
        return True
    return False  # '/' (abs ab docs-root) wird separat behandelt


def rewrite_file(path, moves, dry, docs_root):
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    old_file = path
    old_dir = os.path.dirname(old_file)
    new_dir = os.path.dirname(forward(old_file, moves))
    changes = []

    def repl(m):
        head, inner, tail = m.group(1), m.group(2), m.group(3)
        # Pfad + optionaler Titel: 'pfad "Titel"'
        pm = re.match(r"^(\S+)(\s+.*)?$", inner)
        if not pm:
            return m.group(0)
        link, title = pm.group(1), (pm.group(2) or "")
        if is_external_or_anchor(link):
            return m.group(0)
        anchor = ""
        if "#" in link:
            link, a = link.split("#", 1)
            anchor = "#" + a
        trailing = link.endswith("/")
        if link.startswith("/"):  # absolut ab docs-root
            cand = normalize(os.path.join(docs_root, link.lstrip("/")))
            target_new = forward(cand, moves)
            if target_new == cand:
                return m.group(0)
            new_link = "/" + os.path.relpath(target_new, docs_root).replace(os.sep, "/")
        else:
            # Ziel relativ zur ALTEN Dateiposition (Dateien liegen noch alt auf Platte)
            target_old = normalize(os.path.join(old_dir, link)) if link else old_dir
            target_new = forward(target_old, moves)
            if target_new == target_old and new_dir == old_dir:
                return m.group(0)  # nichts bewegt
            new_link = os.path.relpath(target_new, new_dir).replace(os.sep, "/")
            if new_link == ".":
                new_link = "./"
        if trailing and not new_link.endswith("/"):
            new_link += "/"
        new_inner = new_link + anchor + title
        if new_inner != inner:
            changes.append((inner, new_inner))
            return head + new_inner + tail
        return m.group(0)

    out = LINK_RE.sub(repl, text)
    if changes and not dry:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)
    return changes


def main():
    ap = argparse.ArgumentParser(description="Relative Links nach Umzug neu setzen")
    ap.add_argument("--move", action="append", required=True, metavar="ALT=NEU")
    ap.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts schreiben")
    ap.add_argument("--check", action="store_true", help="exit 1 wenn etwas zu aendern waere")
    ap.add_argument("--docs", default="docs", help="Wurzel der Markdown-Dateien")
    args = ap.parse_args()

    moves = parse_moves(args.move)
    docs_root = normalize(str(ROOT / args.docs))
    total = 0
    files = 0
    for dirpath, _, names in os.walk(docs_root):
        for n in names:
            if not n.endswith(".md"):
                continue
            fp = normalize(os.path.join(dirpath, n))
            ch = rewrite_file(fp, moves, args.dry_run or args.check, docs_root)
            if ch:
                files += 1
                total += len(ch)
                if args.dry_run or args.check:
                    rel = os.path.relpath(fp, ROOT)
                    for o, nw in ch:
                        print(f"  {rel}: {o}  ->  {nw}")
    mode = "CHECK" if args.check else ("DRY" if args.dry_run else "SCHREIB")
    print(f"[{mode}] {files} Dateien, {total} Links angepasst")
    if args.check and total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

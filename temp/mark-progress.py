#!/usr/bin/env python3
"""Mark files as translated in temp/translation-progress.md.

Usage: python3 temp/mark-progress.py <de-rel-path> [<de-rel-path> ...]
Paths are given relative to docs/de/ (as stored in the table).
"""
import os
import sys

OUT = "/srv/FreeSynergy/fs-documentation/temp/translation-progress.md"


def main():
    wanted = {p.strip().removeprefix("docs/de/") for p in sys.argv[1:]}
    if not wanted:
        print("no paths given")
        return 1
    with open(OUT, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    hit = set()
    for i, line in enumerate(lines):
        if not line.startswith("|") or line.startswith("| App") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[1] in wanted:
            cells[-1] = "[x] übersetzt"
            lines[i] = "| " + " | ".join(cells) + " |"
            hit.add(cells[1])
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    missing = wanted - hit
    print(f"marked {len(hit)}")
    for m in sorted(missing):
        print("  NOT IN TABLE:", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())

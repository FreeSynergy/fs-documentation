#!/usr/bin/env python3
import sys


def build(path, de_path, cells):
    """cells: list of rows; each row is either str (full inner text) or (c1, c2)."""
    de = open(de_path, encoding="utf-8").read().split("\n")
    dw = [len(l) for l in de if l[:1] in ("\u250c", "\u2502", "\u251c", "\u2514")]
    # segment widths from first rule line containing box drawings ┬
    rule = [l for l in de if l[:1] == "\u251c" and "\u252c" in l]
    lines = []
    ri = 0
    segs = None
    if rule:
        r = rule[0]
        segs = []
        cur = 0
        for ch in r[1:-1]:
            if ch in ("\u252c", "\u2534"):
                segs.append(cur)
                cur = 0
            else:
                cur += 1
        segs.append(cur)
    W = dw[0]
    for k, c in enumerate(cells):
        w = dw[k] if k < len(dw) else W
        if isinstance(c, tuple):
            assert segs and len(c) == len(segs), (segs, c)
            s = "\u2502"
            for i, t in enumerate(c):
                t = t[: segs[i]]
                s += t + " " * (segs[i] - len(t)) + "\u2502"
            s = s.rstrip()
            if len(s) < w:
                s += " " * (w - len(s))
            lines.append(s)
        else:
            c = c[: w - 2]
            lines.append("\u2502" + c + " " * (w - 2 - len(c)) + "\u2502")
    return lines


if __name__ == "__main__":
    de, en, cells = sys.argv[1], sys.argv[2], sys.argv[3:]
    rows = []
    for c in cells:
        if "|" in c:
            rows.append(tuple(c.split("|")))
        else:
            rows.append(c)
    out = build(en, de, rows)
    for l in out:
        print(len(l), l)

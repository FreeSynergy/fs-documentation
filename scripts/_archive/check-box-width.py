#!/usr/bin/env python3
"""Compare (default) or normalise (--fix) the ASCII-box widths of DE vs EN files.

The EN box is normalised to the dominant box width of the DE file by adding or
removing spaces just before the closing box character of each line.
"""
import sys

BOX = ("\u250c", "\u2502", "\u251c", "\u2514")
CLOSE = {
    "\u2502": ("\u2502",),
    "\u251c": ("\u2524", "\u251c"),
    "\u2514": ("\u2518",),
    "\u250c": ("\u2510",),
}


def is_box(line):
    return line[:1] in BOX


def target_widths(path):
    ws = [len(l) for l in open(path, encoding="utf-8").read().split("\n") if is_box(l.rstrip("\n"))]
    if not ws:
        return None, []
    dom = max(set(ws), key=ws.count)
    return dom, ws


def close_index(line):
    for ch in reversed(line):
        if ch in ("\u2502", "\u2524", "\u2518", "\u251c", "\u2510", "\u252c", "\u2534"):
            return line.rindex(ch)
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fix = "--fix" in sys.argv
    de, en = args[0], args[1]
    dom, dw = target_widths(de)
    if dom is None:
        print("no box in DE")
        return
    if not fix:
        ew = [len(l) for l in open(en, encoding="utf-8").read().split("\n") if is_box(l)]
        print("DE widths:", dw, "dominant:", dom)
        print("EN widths:", ew, "OK" if all(w == dom for w in ew) else "OFF")
        return
    lines = open(en, encoding="utf-8").read().split("\n")
    changed = 0
    for i, line in enumerate(lines):
        if not is_box(line) or len(line) == dom:
            continue
        ci = close_index(line)
        if ci is None:
            continue
        diff = dom - len(line)
        lines[i] = line[:ci] + " " * diff + line[ci:]
        changed += 1
    open(en, "w", encoding="utf-8").write("\n".join(lines))
    print(f"normalised {changed} lines to width {dom}")


if __name__ == "__main__":
    main()

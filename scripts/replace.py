#!/usr/bin/env python3
"""Generic text replacement by regex rules, with dry run and per-rule report.

Companion to `move.py`: move.py moves files and fixes links, replace.py fixes the
words around them (headings, path texts in prose, link labels).

RULES
    One rule:  REGEX => REPLACEMENT        (Python re, \\1 / \\g<name> in REPLACEMENT)
    From --rule (repeatable) and/or --rules FILE (one per line, `#` comments).
    Rules run in order; each sees the result of the previous one.
    An empty REPLACEMENT is allowed (`REGEX =>`) and deletes the match.

OPTIONS
    --scope DIR         tree to process (repeatable)
    --glob PATTERN      file name pattern (default *.md, repeatable)
    --skip-code         leave fenced code blocks and `inline code` untouched
    --apply             write (default: dry run)
    --show N            sample changes per rule in the dry run (default 3)

EXAMPLE
    python3 scripts/replace.py --scope docs/en \\
        --rules scripts/rules/masks_to_frontends_text.rules          # dry run
    ... --apply
"""
import argparse
import fnmatch
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_RE = re.compile(r"(`[^`\n]*`)")


def load_rules(args):
    raw = list(args.rule or [])
    for f in args.rules or []:
        for line in Path(f).read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if s and not s.startswith("#"):
                raw.append(s)
    rules = []
    for r in raw:
        if "=>" not in r:
            sys.exit(f"rule needs 'REGEX => REPLACEMENT': {r}")
        pat, rep = r.split("=>", 1)
        rules.append((re.compile(pat.strip()), rep.strip(), r))
    if not rules:
        sys.exit("no rules given (--rule / --rules)")
    return rules


def sub_text(text, rules, counts, samples, path, skip_code, show):
    def apply(segment):
        for pat, rep, key in rules:
            def r(m, key=key, rep=rep):
                new = m.expand(rep)
                counts[key] += 1
                if len(samples[key]) < show:
                    samples[key].append(f"{path}: {m.group(0)!r} -> {new!r}")
                return new
            segment = pat.sub(r, segment)
        return segment

    if not skip_code:
        return apply(text)
    out, fence = [], False
    for line in text.splitlines(keepends=True):
        if FENCE_RE.match(line):
            fence = not fence
            out.append(line)
        elif fence:
            out.append(line)
        else:
            parts = INLINE_RE.split(line)
            out.append("".join(p if i % 2 else apply(p) for i, p in enumerate(parts)))
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", action="append", required=True)
    ap.add_argument("--glob", action="append")
    ap.add_argument("--rule", action="append")
    ap.add_argument("--rules", action="append")
    ap.add_argument("--skip-code", action="store_true")
    ap.add_argument("--show", type=int, default=3)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    rules = load_rules(args)
    globs = args.glob or ["*.md"]
    counts, samples = Counter(), defaultdict(list)
    changed = {}
    for scope in args.scope:
        base = ROOT / scope
        walk = [(str(base.parent), [], [base.name])] if base.is_file() else os.walk(base)
        for dirpath, dirs, names in walk:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for n in names:
                if not any(fnmatch.fnmatch(n, g) for g in globs):
                    continue
                p = Path(dirpath) / n
                rp = p.relative_to(ROOT).as_posix()
                text = p.read_text(encoding="utf-8")
                new = sub_text(text, rules, counts, samples, rp, args.skip_code, args.show)
                if new != text:
                    changed[p] = new

    for _, _, key in rules:
        print(f"[{counts[key]:5d}] {key}")
        for s in samples[key]:
            print(f"          {s}")
    print(f"files changed: {len(changed)}")
    if not args.apply:
        print("dry run — nothing written (use --apply)")
        return 0
    for p, new in changed.items():
        p.write_text(new, encoding="utf-8")
    print("applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

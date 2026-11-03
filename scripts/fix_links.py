#!/usr/bin/env python3
"""Setzt interne Markdown-Links anhand einer Namens-Registry neu.

Idee: der docs/-Baum wird einmal als Liste aller Link-Ziele aufgenommen. Ein Ziel
ist eine Markdown-Datei (`de/components/primitives/fields/text-input/usage.md`)
oder ein Ordner (`de/components/primitives/fields/text-input`). Im Text sitzt ein
Link, dessen Schluessel (`../textarea/`, `../../basics/base.md`,
`components/data/list-view/`) gegen diese Registry aufgeloest wird.

Aufloesung pro Link:
1. Link zeigt schon auf ein存在的 Ziel, das zum Schluessel passt -> nichts tun.
2. Schluessel (letzte Pfadteile, `.md` und fuehrendes/folgendes `/` optional)
   gegen die Registry: Suffix-Treffer. Bevorzugt gleiche Sprachwurzel (de/en) —
   ueber Sprachbaeume hinweg wird nicht verlinkt (CONVENTIONS.md Abschnitt 4) —
   und gleicher Zweig (components/interactions/data/programs) wie die Datei.
   Eindeutig -> Link neu setzen. Mehrdeutig -> Hinweis, es wird nichts geraten.

Der Stil bleibt erhalten: endet der Link auf `/`, bleibt es ein Ordner-Link; endet
er auf `.md`, bleibt es eine Datei-Link. `(../base/)`-Links auf eine Datei ohne
eigenen Ordner werden zu `(../base.md)` — mkdocs kennt den Ordner nicht.

Der Lauf ist unabhaengig von Tiefen-Arithmetik: erst `git mv`, dann
`fix_links.py --force`, dann `scripts/gen_component_indexes.py`, dann
`mkdocs build` als Verifikation. --force prueft jeden Link, auch wenn sein Ziel
noch existiert (nach einem Umzug koennen Links gueltig, aber falsch sein).

Aufruf:
    python3 scripts/fix_links.py --force --dry-run      # anzeigen
    python3 scripts/fix_links.py --force                # schreiben
    python3 scripts/fix_links.py --force --check        # exit 1 wenn zu aendern
    python3 scripts/fix_links.py --only docs/de         # nur Teilbaum
"""
import argparse
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\n]+?)(\))")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INDEX = "/index.md"


def norm(p):
    return p.replace(os.sep, "/")


def registry_of(docs_root):
    """(files, dirs, by_name) — alles Pfade relativ zu docs_root.

    by_name: letzter Pfadteil -> [(art, pfad)] mit art in {"file", "dir"}.
    Eine Datei `x/index.md` zusaetzlich unter dem Ordnernamen von `x`."""
    files, dirs = set(), set()
    for dirpath, _subdirs, names in os.walk(docs_root):
        rel_dir = norm(os.path.relpath(dirpath, docs_root))
        if rel_dir != ".":
            dirs.add(rel_dir)
        for n in names:
            if n.endswith(".md"):
                files.add(norm(os.path.join(rel_dir, n)) if rel_dir != "." else n)
    by_name = defaultdict(set)
    for f in files:
        stem = f.rsplit("/", 1)[-1][:-3]
        by_name[stem].add(("file", f))
        if stem == "index":
            d = f[: -len(INDEX)]
            by_name[d.rsplit("/", 1)[-1]].add(("dir", d))
    for d in dirs:
        by_name[d.rsplit("/", 1)[-1]].add(("dir", d))
    return files, dirs, {k: sorted(v) for k, v in by_name.items()}


def lang_of(rel):
    return rel.split("/", 1)[0]


def branch_of(rel):
    parts = rel.split("/")
    return parts[1] if len(parts) > 2 else ""


def key_variants(link):
    """moegliche Schluessel aus dem Linktext, laengster zuerst"""
    clean = link.split("#")[0].strip()
    clean = clean.strip("/").strip(".").strip("/")
    if clean.endswith(".md"):
        clean = clean[:-3]
    if not clean:
        return []
    parts = [p for p in clean.split("/") if p]
    variants = ["/".join(parts[i:]) for i in range(len(parts))]
    # Datei-Links nicht bis auf den nackten Dateinamen (`description`, `usage`, …)
    # herunterbrechen — der ist in diesem Repo ueberall gleich und nur mehrdeutig.
    if link.split("#")[0].endswith(".md") and len(parts) > 1:
        variants = [v for v in variants if len(v.split("/")) >= 2]
    return variants


def matches(kind, path, key):
    """key (ohne .md, ohne fuehrendes/folgendes `/`) als Pfad-Teilfolge von path.

    Teilfolge, nicht striktes Suffix: beim Band-Umzug kommt genau eine Ebene neu
    dazu (`components/data/...` -> `components/widgets/data/...`). Die Teile des
    Schluessels bleiben in Reihenfolge erhalten. Mehrdeutigkeiten meldet resolve()."""
    p = path.split("/")
    k = key.split("/")
    if not k:
        return False
    i = 0
    for j, part in enumerate(p):
        want = k[i]
        last = (i == len(k) - 1)
        if part == want or (last and kind == "file" and part == want + ".md"):
            i += 1
            if i == len(k):
                return True
    return False


def ups_of(link):
    """Anzahl fuehrender ../ in einem Linktext (relative Distanz des Autors)."""
    return len([p for p in link.split("/") if p == ".."])


def resolve(link, by_name, ctx, ups_orig=0):
    """-> ((art, pfad) | None, grund); ctx = (sprache, zweig, ordner der Datei)"""
    variants = key_variants(link)
    if not variants:
        return None, "kein Pfad"
    for key in variants:
        last = key.rsplit("/", 1)[-1]
        pool = by_name.get(last, [])
        if not pool:
            continue
        hits = [(k, p) for k, p in pool if lang_of(p) == ctx[0] and matches(k, p, key)]
        if not hits:
            continue

        def score(item):
            _k, p = item
            s = 0
            if ctx[1] and branch_of(p) == ctx[1]:
                s += 2
            # relative Distanz des Autors beibehalten: ein ../../data/ meint
            # hoechstwahrscheinlich dasselbe Niveau, nicht vier Ebenen hoeher
            s -= abs(ups_orig - ups_of(os.path.relpath(p, ctx[2]).replace(os.sep, "/")))
            return s

        hits.sort(key=score, reverse=True)
        best = score(hits[0])
        top = [h for h in hits if score(h) == best]
        if len(top) == 1:
            return top[0], "ok"
        return None, "mehrdeutig: " + ", ".join(sorted(p for _k, p in top)[:5])
    return None, "kein Treffer"


def new_link(kind, target, from_dir, want_dir, files):
    """Ziel -> Linktext im bisherigen Stil (Ordner- oder Datei-Link)."""
    if kind == "dir":
        if want_dir:
            return norm(os.path.relpath(target, from_dir)) + "/"
        if target + INDEX in files:
            return norm(os.path.relpath(target + INDEX, from_dir))
        return norm(os.path.relpath(target, from_dir)) + "/"
    return norm(os.path.relpath(target, from_dir))


def rewrite(path, docs_root, files, dirs, by_name, dry, force=False):
    rel_file = norm(os.path.relpath(path, docs_root))
    from_dir = os.path.dirname(rel_file)
    ctx = (lang_of(rel_file), branch_of(rel_file), from_dir)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    changes, unresolved = [], []

    def repl(m):
        head, inner, tail = m.group(1), m.group(2), m.group(3)
        pm = re.match(r"^(\S+)(\s+.*)?$", inner)
        if not pm:
            return m.group(0)
        link, title = pm.group(1), (pm.group(2) or "")
        if (not link or link.startswith("#")
                or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link)
                or link.startswith("/")):
            return m.group(0)

        bare = link.split("#")[0]
        probe = norm(os.path.normpath(os.path.join(from_dir, bare))) if bare else "."
        probe = probe.lstrip("./") or "."
        reachable = probe in files or probe in dirs or (probe + INDEX) in files
        if reachable and not force:
            return m.group(0)

        anchor = ""
        if "#" in link:
            link, a = link.split("#", 1)
            anchor = "#" + a
        want_dir = link.endswith("/")

        hit, why = resolve(link, by_name, ctx, ups_orig=ups_of(link))
        if hit is None:
            if not reachable:
                unresolved.append(f"{rel_file}: {link} ({why})")
            return m.group(0)

        # Ziel bereits richtig erreicht und Stil passend -> nichts tun
        kind, target = hit
        if reachable and probe_ok(probe, kind, target, files):
            return m.group(0)

        out = new_link(kind, target, from_dir, want_dir, files)
        if out + anchor + title != inner:
            changes.append((inner, out + anchor + title))
            return head + out + anchor + tail
        return m.group(0)

    lines, fenced, out_lines = text.split("\n"), False, []
    for line in lines:
        if FENCE_RE.match(line):
            fenced = not fenced
            out_lines.append(line)
            continue
        out_lines.append(line if fenced else LINK_RE.sub(repl, line))
    new_text = "\n".join(out_lines)

    if changes and not dry:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_text)
    return changes, unresolved


def probe_ok(probe, kind, target, files):
    if kind == "dir":
        return probe == target
    return probe == target or probe + "/index.md" == target


def main():
    ap = argparse.ArgumentParser(description="Interne Links per Namens-Registry neu setzen")
    ap.add_argument("--docs", default="docs", help="Wurzel der Markdown-Dateien")
    ap.add_argument("--dry-run", action="store_true", help="nur anzeigen")
    ap.add_argument("--check", action="store_true", help="exit 1 wenn etwas zu aendern waere")
    ap.add_argument("--force", action="store_true",
                    help="jeden Link pruefen, auch wenn sein Ziel noch existiert")
    ap.add_argument("--only", help="nur Dateien unter diesem Pfad (relativ zum Repo)")
    ap.add_argument("--show-unresolved", action="store_true",
                    help="nicht aufloesbare Links listen")
    args = ap.parse_args()

    docs_root = os.path.join(ROOT, args.docs)
    files, dirs, by_name = registry_of(docs_root)

    dry = args.dry_run or args.check
    only = norm(args.only) if args.only else None
    touched = total = 0
    unresolved = []
    for dirpath, _dirs, names in os.walk(docs_root):
        for n in names:
            if not n.endswith(".md"):
                continue
            fp = os.path.join(dirpath, n)
            rel_repo = norm(os.path.relpath(fp, ROOT))
            if only and not rel_repo.startswith(only):
                continue
            ch, un = rewrite(fp, docs_root, files, dirs, by_name, dry, force=args.force)
            unresolved.extend(un)
            if ch:
                touched += 1
                total += len(ch)
                if dry:
                    for o, nw in ch:
                        print(f"  {rel_repo}: {o}  ->  {nw}")
    mode = "CHECK" if args.check else ("DRY" if dry else "SCHREIB")
    print(f"[{mode}] {touched} Dateien, {total} Links angepasst")
    if unresolved:
        print(f"NICHT aufgeloest ({len(unresolved)}) — nur wenn gewuenscht anzeigen: --show-unresolved")
        if args.show_unresolved:
            for u in unresolved:
                print(f"  ? {u}")
    return 1 if (args.check and total) else 0


if __name__ == "__main__":
    raise SystemExit(main())

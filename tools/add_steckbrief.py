#!/usr/bin/env python3
"""Fuegt in jede `description.md` eine Steckbrief-Tabelle ein (Konzept Abschnitt 7,
Maske aus basics/base.md), wenn noch keine vorhanden ist.

Die Werte werden moeglichst aus den vorhandenen Dateien abgeleitet:
Kategorie = Ordner, Varianten/Typen = Tabellen im Abschnitt Varianten,
Rolle = `role`-Zeile in attributes.md, Verwandt = Links auf andere Komponenten,
Zusaetzliche Zustaende, Gesten und Animationen = Fachwoerter in appearance.md und
attributes.md, Elternteil = bekannte Vererbung (PARENTS).

Zusaetzlich erhaelt jede `description.md` einen Abschnitt `Siehe auch` (Pflichtabschnitt),
falls er fehlt.

Aufruf:
    python3 tools/add_steckbrief.py            # Dry-Run
    python3 tools/add_steckbrief.py --apply    # schreiben
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "de"
COMPONENTS = DOCS / "components"

# Bekannte echte Vererbung (Elternklasse muss als Ordner existieren)
PARENTS = {
    "audio": ["media-player"],
    "video": ["media-player"],
    "context-menu": ["menu"],
    "search-field": ["text-input"],
    "mention-input": ["text-input"],
    "tags-input": ["text-input"],
    "combobox": ["select"],
    "slider": ["number-input"],
    "rich-text-editor": ["textarea"],
}

STATE_WORDS = ["selected", "checked", "expanded", "collapsed", "open", "closed", "empty",
               "unread", "pinned", "completed", "dragging", "partial", "invalid", "filled"]
# Mehrdeutige Namen: als Animationsname gemeint, aber meist als Bauteil genannt
ANIM_IGNORE = {"progress", "skeleton", "highlight"}
BASE_STATES = ["default", "hover", "active", "focus", "disabled", "loading", "error"]
CELL_SPLIT = re.compile(r"(?<!\\)\|")
LINK_RE = re.compile(r"\]\(([^)\s#]+)(#[^)]*)?\)")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def words(text, vocab):
    found = []
    for w in vocab:
        if re.search(rf"(?<![a-z-]){re.escape(w)}(?![a-z-])", text):
            found.append(w)
    return found


def all_sections(text):
    """{ueberschrift (klein, ohne ##): [zeilen]}"""
    out, head, body = {}, None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if head is not None:
                out.setdefault(head, []).extend(body)
            head, body = line[3:].strip().lower(), []
        elif head is not None:
            body.append(line)
    if head is not None:
        out.setdefault(head, []).extend(body)
    return out


def section_body(text, name):
    """Zeilen des Abschnitts `## name` (oder None, wenn es den Abschnitt nicht gibt)."""
    return all_sections(text).get(name.lower())


def first_cells(body):
    """Erste Zelle jeder Tabellenzeile eines Abschnitts, sauber formatiert."""
    out, seen_header = [], False
    for line in body:
        s = line.strip()
        if not s.startswith("|"):
            continue
        if SEP_RE.match(s):
            seen_header = True
            continue
        if not seen_header:
            continue
        cell = CELL_SPLIT.split(s[1:].rstrip("|").strip())[0].strip()
        cell = cell.strip("*").strip("`").strip()
        if cell and cell.lower() not in ("attribut", "variante", "typ", "zustand", "größe", "grösse"):
            out.append(cell)
    return out


def role_of(attributes_text):
    m = re.search(r"\|\s*`role`\s*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|", attributes_text)
    if not m:
        return None
    value = m.group(1)
    m2 = re.search(r"(`[^`]+`)", value)
    return m2.group(1) if m2 else None


def related_of(comp, files_text):
    names = []
    for text in files_text:
        for target, _ in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            clean = target.rstrip("/").split("#")[0]
            if not clean:
                continue
            resolved = (comp / clean).resolve()
            rel = resolved.relative_to(COMPONENTS) if str(resolved).startswith(str(COMPONENTS)) else None
            if rel and len(rel.parts) == 2 and rel.parts[1] not in ("index.md", "base.md", "base", comp.name):
                if rel.parts[1] not in names:
                    names.append(rel.parts[1])
    return names


def build_row(comp, cat, name):
    desc = (comp / "description.md").read_text(encoding="utf-8")
    attrs_text = (comp / "attributes.md").read_text(encoding="utf-8") if (comp / "attributes.md").is_file() else ""
    app_text = (comp / "appearance.md").read_text(encoding="utf-8") if (comp / "appearance.md").is_file() else ""
    usage_text = (comp / "usage.md").read_text(encoding="utf-8") if (comp / "usage.md").is_file() else ""

    variants = []
    for sec in ("Varianten", "Typen", "Varianten (`variant`)", "Typen (`type`)"):
        body = section_body(desc, sec) or section_body(app_text, sec)
        if body:
            variants = first_cells(body)
            if variants:
                break
    variant_text = ", ".join(f"`{v}`" for v in variants[:8]) if variants else "keine"

    states = [s for s in words(app_text + "\n" + attrs_text, STATE_WORDS) if s not in BASE_STATES]
    state_text = ", ".join(f"`{s}`" for s in states[:6]) if states else "-"

    gesture_names = sorted(p.name for p in (DOCS / "gestures").glob("*") if p.is_dir())
    anim_names = sorted(p.parent.name for p in (DOCS / "animations").glob("*/*/description.md")
                        if p.parent.name not in ANIM_IGNORE)
    gest = words(desc + "\n" + usage_text + "\n" + app_text + "\n" + attrs_text, gesture_names)
    anim = [a for a in words(app_text + "\n" + desc, anim_names) if a not in gest]
    gest_text = ", ".join(f"`{g}`" for g in gest[:5]) if gest else "-"
    anim_text = ", ".join(f"`{a}`" for a in anim[:5]) if anim else "-"

    parents = ["base"] + [p for p in PARENTS.get(name, []) if (COMPONENTS / cat / p).is_dir()
                          or any((COMPONENTS / c / p).is_dir() for c in ("media", "navigation", "fields"))]
    role = role_of(attrs_text)
    related = related_of(comp, (desc, attrs_text, app_text, usage_text))

    rows = [
        ("Kategorie", f"`{cat}`"),
        ("Erbt von", ", ".join(f"`{p}`" for p in parents)),
        ("Varianten", variant_text),
        ("Zustände", state_text),
        ("Gesten", gest_text),
        ("Animationen", anim_text),
        ("Verwandt", ", ".join(f"`{r}`" for r in related[:6]) if related else "-"),
    ]
    if role:
        rows.append(("Rolle", role))
    rows.append(("Status", "dokumentiert"))
    return ["| Feld | Wert |", "|------|------|"] + [f"| **{k}** | {v} |" for k, v in rows]


def steckbrief_span(lines):
    """(anfang, ende_exklusiv) der Steckbrief-Tabelle vor der ersten `## `-Ueberschrift,
    oder None."""
    start = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            break
        if line.strip().startswith("|"):
            if start is None:
                start = i
            end = i + 1
        elif start is not None and line.strip():
            break
    return (start, end) if start is not None else None


def normalize_blank_lines(text):
    """Setzt genau eine Leerzeile zwischen die Markdown-Blöcke (Überschriften, Tabellen,
    Listen, Absätze, Hinweise, Codeblöcke bleiben heil)."""
    blocks, cur, fence = [], [], False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            if cur and not fence:
                blocks.append(cur)
                cur = []
            cur.append(line)
            fence = not fence
            if fence:
                continue
            blocks.append(cur)
            cur = []
            continue
        if fence or not s:
            if not fence:
                if cur:
                    blocks.append(cur)
                    cur = []
                continue
            cur.append(line)
            continue
        starts_block = (s.startswith("#") or s.startswith("!!!") or s.startswith("???")
                        or s.startswith("|") or s[:1] in "-*+" and len(s) > 1 and s[1] == " "
                        or re.match(r"^\d+\.\s", s))
        if starts_block and cur:
            same_table = cur[-1].strip().startswith("|") and s.startswith("|")
            same_list = bool(re.match(r"^([-*+]|\d+\.)\s", cur[-1].strip())) and bool(re.match(r"^([-*+]|\d+\.)\s", s))
            admonition = bool(re.match(r"^(!!!|\?\?\?)", cur[-1].strip())) and line.startswith("    ")
            if not (same_table or same_list or admonition):
                blocks.append(cur)
                cur = []
        cur.append(line)
    if cur:
        blocks.append(cur)
    return "\n\n".join("\n".join(b) for b in blocks).rstrip() + "\n"


def has_steckbrief(lines):
    """Steckbrief = Markdown-Tabelle vor der ersten Ueberschrift `## `."""
    for line in lines:
        if line.startswith("## "):
            return False
        if line.strip().startswith("|"):
            return True
    return False


def cat_of(comp, name):
    for d in COMPONENTS.glob(f"*/{name}"):
        return d.parent.name
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--replace", action="store_true", help="vorhandene Steckbrief-Tabelle neu erzeugen")
    ap.add_argument("--blank-lines", action="store_true",
                    help="nur Leerzeilen zwischen Markdown-Blöcken normalisieren")
    args = ap.parse_args()

    if args.blank_lines:
        n = 0
        for md in sorted(COMPONENTS.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            new = normalize_blank_lines(text)
            if new != text:
                n += 1
                if args.apply:
                    md.write_text(new, encoding="utf-8")
        print(f"{'ANGEWENDET' if args.apply else 'DRY-RUN'}: Dateien mit Leerzeilen-Kur {n}")
        return 0

    added = replaced = seealso = 0
    for comp in sorted(d for d in COMPONENTS.glob("*/*") if d.is_dir()):
        cat, name = comp.parent.name, comp.name
        desc = comp / "description.md"
        if not desc.is_file():
            continue
        lines = desc.read_text(encoding="utf-8").splitlines()
        span = steckbrief_span(lines)
        if span and args.replace:
            lines = lines[:span[0]] + lines[span[1]:]
            span = None
        if span is None:
            while lines and not lines[0].strip():
                lines.pop(0)
            row = build_row(comp, cat, name)
            pos = 1
            while pos < len(lines) and lines[pos].strip() == "":
                pos += 1
            lines = lines[:pos] + [""] + row + [""] + lines[pos:]
            lines = [l for i, l in enumerate(lines) if not (l == "" and i and lines[i - 1] == "")]
            if args.apply:
                desc.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            added += 1
            print(f"  {'Steckbrief neu' if args.replace else 'Steckbrief'}: {cat}/{name}")

        text = desc.read_text(encoding="utf-8") if args.apply else "\n".join(lines) + "\n"
        if not any(l.strip() == "## Siehe auch" for l in text.splitlines()):
            related = related_of(comp, (text,))
            block = ["", "## Siehe auch", ""]
            for r in related[:4]:
                c = cat_of(comp, r)
                if c:
                    block.append(f"- [{r}](../../{c}/{r}/)")
            block.append(f"- [{cat} – Übersicht](../index.md)")
            block.append("- [Basiskomponente](../../basics/base/)")
            out = text.rstrip().splitlines() + block
            if args.apply:
                desc.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
            seealso += 1
            print(f"  Siehe auch: {cat}/{name}")
        if args.replace:
            replaced += 1

    print(f"\n{'ANGEWENDET' if args.apply else 'DRY-RUN'}: Steckbriefe {added}, "
          f"Siehe-auch-Abschnitte {seealso}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Prueft den Komponentenbestand gegen den Standard aus
docs/de/components/basics/base.md und docs/de/components/konzept-und-plan.md.

Geprueft werden:
1. Pflichtdateien           description.md, appearance.md, attributes.md, usage.md
2. Steckbrief               Pflichtfelder in description.md, Kategorie stimmt mit dem Ordner
3. Pflichtabschnitte        und ihre Reihenfolge pro Datei
4. Tabellen                 Zeilen mit anderer Zellenzahl als die Kopfzeile (Render-Verlust)
5. Links                    interne Links, die ins Leere laufen
6. Basisklasse              Attribute, die in >= 60 % der Komponenten stehen, aber nicht in base.md
7. Doppelstuecke            Attribut-Aehnlichkeit (Jaccard) ueber 0,6
8. mkdocs.yml               Komponenten, die in der Navigation fehlen

Fehler (exit 1) sind: fehlende Dateien, fehlender Steckbrief, fehlende Pflichtabschnitte,
kaputte Links, Tabellen-Schreibfehler. Absichtslos Benanntes und Doppelstuecke sind
Hinweise. Mit --strict werden auch Hinweise zu Fehlern.

Aufruf:
    python3 tools/check_components.py
    python3 tools/check_components.py --strict
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
COMPONENTS = DOCS / "de" / "components"

REQUIRED_FILES = ["description.md", "appearance.md", "attributes.md", "usage.md"]
STECKBRIEF = ["Kategorie", "Erbt von", "Varianten", "Zustände", "Gesten", "Animationen", "Verwandt", "Status"]
OPTIONAL_STECKBRIEF = ["Rolle"]
SECTIONS = {
    "description.md": ["Beschreibung", "Verwendungszweck", "Varianten", "Features",
                       "Abgrenzung", "Best Practices", "Siehe auch"],
    "appearance.md": ["Grundlayout", "Varianten", "Größen", "Farben und Zustände",
                      "Hover- und Fokus-Effekte", "Reaktiv"],
    "attributes.md": ["Geerbt von"],
}
# Abschnitte, deren Fehlen ein Fehler ist (Rest: Hinweis)
HARD_SECTIONS = {
    "description.md": ["Beschreibung", "Verwendungszweck", "Siehe auch"],
    "appearance.md": ["Grundlayout"],
    "attributes.md": ["Geerbt von"],
}
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def cells_of(line):
    """Zellen einer Markdown-Tabelle; `\\|` innerhalb einer Zelle ist kein Trennzeichen."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in CELL_SPLIT.split(s)]
LINK_RE = re.compile(r"\]\(([^)\s#]+)(#[^)]*)?\)")
SKIP_DIRS = {"basics"}  # base.md ist selbst die Elternklasse


def sections_of(text):
    """[(ueberschrift_ohne_##, [zeilen])] in Reihenfolge."""
    out, head, body = [], None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if head is not None:
                out.append((head, body))
            head, body = line[3:].strip(), []
        else:
            body.append(line)
    if head is not None:
        out.append((head, body))
    return out


def steckbrief(text):
    """Felder der Steckbrief-Tabelle: die erste Markdown-Tabelle vor der ersten
    Ueberschrift `## `."""
    fields, rows = {}, []
    for line in text.splitlines():
        if line.startswith("## "):
            break
        s = line.strip()
        if s.startswith("|") and not SEP_RE.match(s):
            cells = cells_of(s)
            if len(cells) >= 2:
                rows.append(cells)
    for cells in rows[1:]:
        key = cells[0].strip("*").strip()
        fields[key] = cells[1] if len(cells) > 1 else ""
    return fields


def table_problems(text):
    """Zeilen, deren Zellenzahl von der Kopfzeile abweicht."""
    problems, lines = [], text.splitlines()
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip()):
            ncol = len(cells_of(s))
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                row = lines[j].strip()
                if not SEP_RE.match(row):
                    n = len(cells_of(row))
                    if n != ncol:
                        problems.append((j + 1, ncol, n, row[:60]))
                j += 1
            i = j
        else:
            i += 1
    return problems


def attr_names(text):
    out = set()
    for _head, body in sections_of(text):
        for line in body:
            s = line.strip()
            if s.startswith("|") and not SEP_RE.match(s):
                first = s.strip("|").split("|")[0].strip()
                if first.startswith("`") and first.endswith("`") and len(first) > 2:
                    out.add(first[1:-1])
    return out


def check_links(comp, text, errors):
    for target, _frag in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        clean = target.split("#")[0]
        if not clean:
            continue
        resolved = (DOCS / clean.lstrip("/")) if clean.startswith("/") else (comp / clean)
        resolved = resolved.resolve()
        if not resolved.exists() and not (resolved.parent.is_dir() and resolved.with_suffix(".md").exists()):
            errors.append(f"{comp.relative_to(ROOT)}: Link ins Leere -> {target}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="Hinweise ebenfalls als Fehler werten")
    args = ap.parse_args()

    errors, notes = [], []
    comps = sorted(d for d in COMPONENTS.glob("*/*") if d.is_dir())
    counts = {}
    all_attrs = {}
    nav_text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    base_attrs = set()
    base_file = COMPONENTS / "basics" / "base.md"
    if base_file.is_file():
        base_attrs = attr_names(base_file.read_text(encoding="utf-8"))

    for comp in comps:
        cat, name = comp.parent.name, comp.name
        counts.setdefault(cat, []).append(name)

        for f in REQUIRED_FILES:
            if not (comp / f).is_file():
                errors.append(f"{comp.relative_to(ROOT)}: {f} fehlt")

        desc = comp / "description.md"
        if desc.is_file():
            text = desc.read_text(encoding="utf-8")
            fields = steckbrief(text)
            if not fields:
                errors.append(f"{comp.relative_to(ROOT)}/description.md: Steckbrief-Tabelle fehlt")
            else:
                missing = [k for k in STECKBRIEF if k not in fields]
                if missing:
                    errors.append(f"{comp.relative_to(ROOT)}/description.md: Steckbrief-Felder fehlen: "
                                  + ", ".join(missing))
                if fields.get("Kategorie", "").strip("`* ") != cat:
                    errors.append(f"{comp.relative_to(ROOT)}: Steckbrief-Kategorie "
                                  f"'{fields.get('Kategorie','')}' != Ordner '{cat}'")
                if "Status" in fields and "dokumentiert" not in fields["Status"]:
                    notes.append(f"{comp.relative_to(ROOT)}: Status = {fields['Status']}")
            secs = [h for h, _ in sections_of(text)]
            for s in HARD_SECTIONS["description.md"]:
                if s not in secs:
                    errors.append(f"{comp.relative_to(ROOT)}/description.md: Abschnitt '{s}' fehlt")
            for s in SECTIONS["description.md"]:
                if s not in secs:
                    notes.append(f"{comp.relative_to(ROOT)}/description.md: Abschnitt '{s}' fehlt")

        for f in ("appearance.md", "attributes.md"):
            path = comp / f
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            secs = [h for h, _ in sections_of(text)]
            for s in HARD_SECTIONS[f]:
                if s not in secs:
                    errors.append(f"{comp.relative_to(ROOT)}/{f}: Abschnitt '{s}' fehlt")
            for s in SECTIONS[f]:
                if s not in secs:
                    notes.append(f"{comp.relative_to(ROOT)}/{f}: Abschnitt '{s}' fehlt")

        for f in REQUIRED_FILES:
            path = comp / f
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for line, want, got, _ in table_problems(text):
                errors.append(f"{comp.relative_to(ROOT)}/{f}:{line}: {got} Zellen, Kopfzeile hat {want}")
            check_links(comp, text, errors)

        attrs = comp / "attributes.md"
        if attrs.is_file():
            all_attrs[name] = attr_names(attrs.read_text(encoding="utf-8"))

        if f"de/components/{cat}/{name}/" not in nav_text and f"de/components/{cat}/{name}" not in nav_text:
            notes.append(f"{comp.relative_to(ROOT)}: nicht in mkdocs.yml (nav)")

    # Basisklasse: Attribute, die fast alle listen, aber nicht in base.md stehen
    n = len(all_attrs)
    common = []
    for attr in {a for s in all_attrs.values() for a in s}:
        hit = sum(1 for s in all_attrs.values() if attr in s)
        if hit >= 0.6 * n and attr not in base_attrs:
            common.append((hit, attr))
    for hit, attr in sorted(common, reverse=True):
        notes.append(f"Attribut `{attr}` steht in {hit}/{n} Komponenten, aber nicht in basics/base.md")

    # Doppelstuecke
    names = sorted(all_attrs)
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            x, y = all_attrs[a], all_attrs[b]
            if not x or not y:
                continue
            j = len(x & y) / len(x | y)
            if j >= 0.6:
                pairs.append((round(j, 2), a, b))
    for j, a, b in sorted(pairs, reverse=True):
        notes.append(f"Doppelstuecke: {a} und {b} Aehnlichkeit {j}")

    print("Kategorien:")
    for cat in sorted(counts):
        print(f"  {cat:12s} {len(counts[cat]):3d}  {', '.join(sorted(counts[cat]))}")
    print(f"\nKomponenten gesamt: {sum(len(v) for v in counts.values())}")

    if errors:
        print(f"\nFEHLER ({len(errors)}):")
        for e in errors:
            print(f"  ! {e}")
    if notes:
        print(f"\nHINWEISE ({len(notes)}):")
        for nn in notes:
            print(f"  - {nn}")

    failed = bool(errors) or (args.strict and bool(notes))
    print("\nERGEBNIS:", "nicht bestanden" if failed else "bestanden")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

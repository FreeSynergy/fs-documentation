#!/usr/bin/env python3
"""Prueft den Komponentenbestand gegen den Standard aus
docs/<lang>/components/primitives/basics/base.md und conventions/CONVENTIONS.md.

Layout: components/<band>/<typgruppe>/<komponente>/ (Bänder nach ADR 0004).

Geprueft werden:
1. Band-Zuordnung           jede Komponente liegt im von CONVENTIONS.md §3 vorgegebenen Band
2. Pflichtdateien           description.md, appearance.md, attributes.md, usage.md
3. Steckbrief               Pflichtfelder in description.md, Kategorie stimmt mit dem Ordner
4. Pflichtabschnitte        und ihre Reihenfolge pro Datei
5. Tabellen                 Zeilen mit anderer Zellenzahl als die Kopfzeile (Render-Verlust)
6. Links                    interne Links, die ins Leere laufen
7. Basisklasse              Attribute, die in >= 60 % der Komponenten stehen, aber nicht in base.md
8. Doppelstuecke            Attribut-Aehnlichkeit (Jaccard) ueber 0,6
9. mkdocs.yml               Komponenten, die in der Navigation fehlen

Fehler (exit 1) sind: falsches Band, fehlende Dateien, fehlender Steckbrief, fehlende
Pflichtabschnitte, kaputte Links, Tabellen-Schreibfehler. Absichtslos Benanntes und
Doppelstuecke sind Hinweise. Mit --strict werden auch Hinweise zu Fehlern.

Aufruf:
    python3 scripts/check_components.py            # --lang en (Standard)
    python3 scripts/check_components.py --lang de
    python3 scripts/check_components.py --strict
"""
import argparse
import re
import sys
from pathlib import Path

import gen_component_indexes as gen

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
COMPONENTS = DOCS / "en" / "components"  # per --lang umgesetzt
LANG = "en"

REQUIRED_FILES = ["description.md", "appearance.md", "attributes.md", "usage.md"]
# Steckbrief-Felder und Abschnittsnamen pro Sprache (en = Hauptsprache, ADR 0011).
LANG_RULES = {
    "de": {
        "steckbrief": ["Kategorie", "Erbt von", "Varianten", "Zustände", "Gesten",
                       "Animationen", "Verwandt", "Status"],
        "category": "Kategorie", "status": "Status", "documented": "dokumentiert",
        # Steckbrief-Felder, die einen Wert brauchen (`-` gilt als leer).
        "filled": ["Varianten", "Zustände", "Gesten", "Animationen", "Verwandt"],
        "sections": {
            "description.md": ["Beschreibung", "Verwendungszweck", "Varianten", "Features",
                               "Abgrenzung", "Best Practices", "Siehe auch"],
            "appearance.md": ["Grundlayout", "Varianten", "Größen", "Farben und Zustände",
                              "Hover- und Fokus-Effekte", "Reaktiv"],
            "attributes.md": ["Geerbt von"],
        },
        "hard": {
            "description.md": ["Beschreibung", "Verwendungszweck", "Siehe auch"],
            "appearance.md": ["Grundlayout"],
            "attributes.md": ["Geerbt von"],
        },
    },
    "en": {
        "steckbrief": ["Category", "Inherits from", "Variants", "States", "Gestures",
                       "Animations", "Related", "Status"],
        "category": "Category", "status": "Status", "documented": "documented",
        "filled": ["Variants", "States", "Gestures", "Animations", "Related"],
        "sections": {
            "description.md": ["Description", "Purpose", "Variants", "Features",
                               "Distinction", "Best Practices", "See also"],
            "appearance.md": ["Base layout", "Variants", "Sizes", "Colours and states",
                              "Hover and focus effects", "Responsive"],
            "attributes.md": ["Inherited from"],
        },
        "hard": {
            "description.md": ["Description", "Purpose", "See also"],
            "appearance.md": ["Base layout"],
            "attributes.md": ["Inherited from"],
        },
    },
}
RULES = LANG_RULES[LANG]
# Paare, deren Aehnlichkeit geprueft und bewusst akzeptiert wurde
# (combobox = zusaetzlich Freitext und Vorschlaege, select = nur vorhandene Optionen).
ACCEPTED_PAIRS = {("combobox", "select")}
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
    global COMPONENTS, LANG, RULES
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="Hinweise ebenfalls als Fehler werten")
    ap.add_argument("--lang", choices=["en", "de"], default="en",
                    help="Sprachbaum (Standard: en)")
    args = ap.parse_args()
    LANG = args.lang
    COMPONENTS = DOCS / LANG / "components"
    RULES = LANG_RULES[LANG]
    gen.set_lang(LANG)

    errors, notes = [], []
    comps = sorted(d for d in COMPONENTS.glob("*/*/*") if d.is_dir())
    counts = {}
    all_attrs = {}
    nav_text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    base_attrs = set()
    base_file = COMPONENTS / "primitives" / "basics" / "base.md"
    if base_file.is_file():
        base_attrs = attr_names(base_file.read_text(encoding="utf-8"))

    want_band = {}
    for band, groups in gen.ASSIGNMENT.items():
        for cat, names in groups.items():
            for name in names:
                want_band[f"{cat}/{name}"] = band

    for comp in comps:
        band, cat, name = comp.parent.parent.name, comp.parent.name, comp.name
        counts.setdefault(f"{band}/{cat}", []).append(name)

        expected = want_band.get(f"{cat}/{name}")
        if expected is None:
            errors.append(f"{comp.relative_to(ROOT)}: in CONVENTIONS.md §3 nicht zugeordnet")
        elif expected != band:
            errors.append(f"{comp.relative_to(ROOT)}: falsches Band, erwartet {expected}/")

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
                missing = [k for k in RULES["steckbrief"] if k not in fields]
                if missing:
                    errors.append(f"{comp.relative_to(ROOT)}/description.md: Steckbrief-Felder fehlen: "
                                  + ", ".join(missing))
                if fields.get(RULES["category"], "").strip("`* ") != cat:
                    errors.append(f"{comp.relative_to(ROOT)}: Steckbrief-Kategorie "
                                  f"'{fields.get(RULES['category'], '')}' != Ordner '{cat}'")
                if "Status" in fields and RULES["documented"] not in fields["Status"]:
                    notes.append(f"{comp.relative_to(ROOT)}: Status = {fields['Status']}")
                for key in RULES["filled"]:
                    if fields.get(key, "").strip(" `-") in ("", "\u2013"):
                        notes.append(f"{comp.relative_to(ROOT)}/description.md: "
                                     f"Steckbrief-Feld '{key}' ist leer")
            secs = [h for h, _ in sections_of(text)]
            for s in RULES["hard"]["description.md"]:
                if s not in secs:
                    errors.append(f"{comp.relative_to(ROOT)}/description.md: Abschnitt '{s}' fehlt")
            for s in RULES["sections"]["description.md"]:
                if s not in secs:
                    notes.append(f"{comp.relative_to(ROOT)}/description.md: Abschnitt '{s}' fehlt")

        for f in ("appearance.md", "attributes.md"):
            path = comp / f
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            secs = [h for h, _ in sections_of(text)]
            for s in RULES["hard"][f]:
                if s not in secs:
                    errors.append(f"{comp.relative_to(ROOT)}/{f}: Abschnitt '{s}' fehlt")
            for s in RULES["sections"][f]:
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

        if f"{LANG}/components/{band}/{cat}/{name}/" not in nav_text \
                and f"{LANG}/components/{band}/{cat}/{name}" not in nav_text:
            notes.append(f"{comp.relative_to(ROOT)}: nicht in mkdocs.yml (nav)")

    # Basisklasse: Attribute, die fast alle listen, aber nicht in base.md stehen
    n = len(all_attrs)
    common = []
    for attr in {a for s in all_attrs.values() for a in s}:
        hit = sum(1 for s in all_attrs.values() if attr in s)
        if hit >= 0.6 * n and attr not in base_attrs:
            common.append((hit, attr))
    for hit, attr in sorted(common, reverse=True):
        notes.append(f"Attribut `{attr}` steht in {hit}/{n} Komponenten, "
                     "aber nicht in primitives/basics/base.md")

    # Doppelstuecke
    names = sorted(all_attrs)
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            x, y = all_attrs[a], all_attrs[b]
            if not x or not y:
                continue
            j = len(x & y) / len(x | y)
            if j >= 0.6 and (a, b) not in ACCEPTED_PAIRS:
                pairs.append((round(j, 2), a, b))
    for j, a, b in sorted(pairs, reverse=True):
        notes.append(f"Doppelstuecke: {a} und {b} Aehnlichkeit {j}")

    print("Bänder / Typgruppen:")
    for cat in sorted(counts):
        print(f"  {cat:26s} {len(counts[cat]):3d}  {', '.join(sorted(counts[cat]))}")
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

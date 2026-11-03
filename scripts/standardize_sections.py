#!/usr/bin/env python3
"""Vereinheitlicht die Abschnittsnamen und ihre Reihenfolge in den Komponenten-Dateien
(Konzept Abschnitt 7). Gleichnamiges wird zusammengefuehrt, komponentenspezifische
Abschnitte bleiben erhalten und stehen nach den Standardabschnitten.

Zusaetzlich: Abschnitte "Beispiele" / "Usage Beispiele" in description.md wandern in
usage.md (Beschluss 2: usage.md enthaelt Anwendung, Szenarien und Beispiele).

Aufruf:
    python3 tools/standardize_sections.py            # Dry-Run
    python3 tools/standardize_sections.py --apply    # schreiben
"""
import argparse
import re
import sys
from pathlib import Path

COMPONENTS = Path(__file__).resolve().parent.parent / "docs" / "de" / "components"

ALIASES = {
    "description.md": {
        "Verwendung": "Verwendungszweck",
        "Einsatzzweck": "Verwendungszweck",
        "Varianten (`source`)": "Varianten",
        "Varianten (`variant`)": "Varianten",
        "Arten von Buttons": "Varianten",
        "Typen": "Varianten",
        "Beschreibung / Übersicht": "Beschreibung",
    },
    "appearance.md": {
        "Layout": "Grundlayout",
        "Layout-Varianten": "Varianten",
        "Layout-Variationen": "Varianten",
        "Form-Varianten": "Varianten",
        "Form-Varianten (CSS)": "Varianten",
        "Format-Varianten": "Varianten",
        "Inhalt-Varianten": "Varianten",
        "Icon-Varianten": "Varianten",
        "Button-Varianten": "Varianten",
        "Spalten-Varianten": "Varianten",
        "Größe-Varianten": "Größen",
        "Größen-Varianten": "Größen",
        "Farb-Varianten": "Farben und Zustände",
        "Farb-Varianten (CSS Variables)": "Farben und Zustände",
        "Farb-Varianten (Initials)": "Farben und Zustände",
        "Farben & Styling": "Farben und Zustände",
        "Farbpalette": "Farben und Zustände",
        "Hover-Effekte": "Hover- und Fokus-Effekte",
        "Responsive Verhalten": "Reaktiv",
        "Responsive": "Reaktiv",
        "Interaktivität": "Reaktiv",
    },
    "attributes.md": {
        "Verhaltens-Attribute": "Verhalten",
        "Interaktive Attribute": "Verhalten",
        "Auslösung und Andockung": "Verhalten",
        "Auslösung": "Verhalten",
        "Display-Attribute": "Darstellung",
        "Styling-Attribute": "Darstellung",
        "Layout-Attribute": "Darstellung",
        "Größe-Attribute": "Darstellung",
        "Positionierung": "Darstellung",
        "Event-Attribute": "Events",
        "Keyboard-Shortcuts": "Events",
        "Accessibility (Barrierefreiheit)": "Barrierefreiheit",
        "Responsive Attribute": "Darstellung",
        "Animation-Attribute": "Darstellung",
    },
}
ORDER = {
    "description.md": ["Beschreibung", "Verwendungszweck", "Varianten", "Features",
                       "Abgrenzung", "Best Practices"],
    "appearance.md": ["Grundlayout", "Varianten", "Größen", "Farben und Zustände",
                      "Hover- und Fokus-Effekte", "Reaktiv"],
    "attributes.md": ["Hauptattribute", "Verhalten", "Darstellung", "Events",
                      "Barrierefreiheit"],
}
LAST = {"description.md": "Siehe auch", "appearance.md": None, "attributes.md": "Geerbt von"}
EXAMPLE_SECTIONS = {"Beispiele", "Usage Beispiele", "Interaktive Beispiele"}
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


def split(text):
    """(preamble-zeilen, [(head, body)])"""
    lines = text.splitlines()
    pre, head, body, out = [], None, [], []
    for line in lines:
        if line.startswith("## "):
            if head is not None:
                out.append((head, body))
            else:
                pre = body
            head, body = line[3:].strip(), []
        else:
            body.append(line)
    if head is not None:
        out.append((head, body))
    return pre, out


def join(pre, sections):
    blocks = ["\n".join(pre)]
    for head, body in sections:
        blocks.append("## " + head + "\n" + "\n".join(body))
    return "\n\n".join(b.rstrip() for b in blocks).rstrip() + "\n"


def fix_attribute_tables(text):
    """Tabellen mit den Kopfspalten `Attribut | Typ | Beschreibung`, deren Zeilen
    zusaetzlich einen Vorgabewert tragen, bekommen eine Default-Spalte; Zeilen ohne
    Vorgabewert werden mit `-` aufgefuellt. Ohne diese Korrektur fallen die Zellen beim
    Rendern weg."""
    lines = text.splitlines()
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if (s.startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip())
                and cells_of(s) == ["Attribut", "Typ", "Beschreibung"]):
            j = i + 2
            rows = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(j)
                j += 1
            wide = [k for k in rows if len(cells_of(lines[k])) == 4
                    and cells_of(lines[k])[2] not in ("", "-")]
            if wide and all(len(cells_of(lines[k])) in (3, 4) for k in rows):
                out.append("| Attribut | Typ | Default | Beschreibung |")
                out.append("|----------|-----|---------|--------------|")
                for k in rows:
                    cells = cells_of(lines[k])
                    if len(cells) == 3:
                        cells = [cells[0], cells[1], "-", cells[2]]
                    out.append("| " + " | ".join(cells[:4]) + " |")
                i = j
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out).rstrip() + "\n"


def standardize(fname, text):
    aliases, order = ALIASES[fname], ORDER[fname]
    pre, sections = split(text)
    merged, order_seen, moved = {}, [], []
    for head, body in sections:
        target = aliases.get(head, head)
        if fname == "description.md" and target in EXAMPLE_SECTIONS:
            moved.append((target, body))
            continue
        if target not in merged:
            merged[target] = list(body)
            order_seen.append(target)
        else:
            kept = [l for l in merged[target] if l.strip()]
            added = [l for l in body if l.strip()]
            merged[target] = kept + [""] + added
    wanted = [s for s in order if s in merged]
    rest = [s for s in order_seen if s not in wanted]
    last = LAST[fname]
    if last and last in merged:
        rest = [s for s in rest if s != last] + [last]
    out = [(s, merged[s]) for s in wanted + rest]
    return join(pre, out), moved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    changed = moved = 0
    for comp in sorted(d for d in COMPONENTS.glob("*/*") if d.is_dir()):
        for fname in ALIASES:
            path = comp / fname
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            new, moves = standardize(fname, fix_attribute_tables(text))
            if not moves and new == text:
                continue
            changed += 1
            if args.apply:
                path.write_text(new, encoding="utf-8")
            for title, body in moves:
                usage = comp / "usage.md"
                extra = "\n".join(body).strip()
                if not extra:
                    continue
                base = usage.read_text(encoding="utf-8").rstrip() if usage.is_file() \
                    else f"# {comp.name} - Verwendung"
                if "## Beispiele" not in base:
                    base += "\n\n## Beispiele\n\n" + extra + "\n"
                if args.apply:
                    usage.write_text(base, encoding="utf-8")
                moved += 1
                print(f"  Beispiele -> usage.md: {comp.parent.name}/{comp.name}")
            if new != text:
                print(f"  Abschnitte: {comp.parent.name}/{comp.name}/{fname}")
    print(f"\n{'ANGEWENDET' if args.apply else 'DRY-RUN'}: Dateien {changed}, "
          f"Beispiel-Abschnitte verschoben {moved}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Erzeugt die Uebersichtsseiten der Komponenten aus den Steckbriefen:

- docs/de/components/index.md                     (Kategorien, Zahlen)
- docs/de/components/<kategorie>/index.md         (Elemente der Kategorie)
- mkdocs.yml                                      (Nav-Abschnitt zwischen Markern)

Die Zahlen stimmen damit immer mit dem Bestand ueberein (Konzept Abschnitt 8).
Einleitungsabsaetze sind im Skript hinterlegt, damit sie bei jedem Lauf gleich bleiben.

Aufruf:
    python3 tools/gen_component_indexes.py             # schreiben
    python3 tools/gen_component_indexes.py --check     # Pruefen (CI), exit 1 bei Abweichung
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "de"
COMPONENTS = DOCS / "components"
MKDOCS = ROOT / "mkdocs.yml"

CATEGORY_INTRO = {
    "basics": "Grundlagen, von denen alle anderen Komponenten ausgehen: die Basisklasse "
              "mit ihren geerbten Attributen, Zuständen und Tokens sowie die kleinsten "
              "Bausteine.",
    "actions": "Action-Elemente lösen eine einzelne Handlung aus oder bündeln "
               "zusammengehörige Handlungen. Sie verändern Daten oder Zustände, aber "
               "nicht die Adresse.",
    "navigation": "Elemente, die den Weg durch das Programm zeigen oder umschalten: "
                  "Menüs, Leisten, Reiter, Seitenleisten und Pfadangaben.",
    "containers": "Boxen und Flächen, die anderen Inhalt aufnehmen: Karten, Panels, "
                  "aufklappbare Gruppen, geteilte Ansichten und Assistenten.",
    "overlays": "Elemente, die über anderem Inhalt erscheinen und eigenen Fokus "
                "bekommen. Sie haben eine eigene Lebensdauer und schließen mit `Esc` "
                "oder Klick außerhalb.",
    "feedback": "Elemente, die den Zustand einer Anwendung sichtbar machen: Meldungen, "
                "Fortschritt, Ladezustände und Kennzeichnungen.",
    "fields": "Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) hält "
              "dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.",
    "data": "Elemente, die Daten darstellen: Listen, Tabellen, Raster, Bäume, Zeitachsen "
            "und Diagramme. Sie bearbeiten Werte, sondern zeigen sie — zum Ändern kommen "
            "die [Felder](../fields/) zum Einsatz.",
    "media": "Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die "
             "Elternklasse von `audio` und `video`.",
    "special": "Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, "
               "Einbettungen, Karten und Ansichten, die es bei generischen "
               "Bibliotheken nicht gibt.",
}
CATEGORY_LABEL = {
    "basics": "Grundlagen", "actions": "Aktionen", "navigation": "Navigation",
    "containers": "Container", "overlays": "Overlays", "feedback": "Rückmeldung",
    "fields": "Felder", "data": "Daten", "media": "Medien", "special": "Spezielle Elemente",
}
CATEGORY_ORDER = ["basics", "actions", "navigation", "containers", "overlays", "feedback",
                  "fields", "data", "media", "special"]
CELL_SPLIT = re.compile(r"(?<!\\)\|")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def cells_of(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in CELL_SPLIT.split(s)]


def steckbrief(text):
    """Felder der Steckbrief-Tabelle (erste Tabelle vor der ersten `## `-Ueberschrift)."""
    fields = {}
    for line in text.splitlines():
        if line.startswith("## "):
            break
        s = line.strip()
        if not s.startswith("|") or SEP_RE.match(s):
            continue
        cells = cells_of(s)
        if len(cells) >= 2:
            fields[cells[0].strip("*").strip()] = cells[1]
    return fields


def kurz(text):
    """Erster Satz aus dem Abschnitt Beschreibung."""
    on, out = False, []
    for line in text.splitlines():
        if line.startswith("## "):
            if on:
                break
            on = line[3:].strip().lower() == "beschreibung"
        elif on and line.strip():
            out.append(line.strip())
    sentence = " ".join(out)
    m = re.match(r"^(.*?[.!?])(\s|$)", sentence)
    return (m.group(1) if m else sentence[:120]).strip()


def collect():
    data = {}
    for comp in sorted(d for d in COMPONENTS.glob("*/*") if d.is_dir()):
        desc = comp / "description.md"
        if not desc.is_file():
            continue
        text = desc.read_text(encoding="utf-8")
        fields = steckbrief(text)
        cat = comp.parent.name
        data.setdefault(cat, []).append({
            "name": comp.name,
            "fields": fields,
            "kurz": kurz(text),
            "has_usage": (comp / "usage.md").is_file(),
        })
    return data


def category_page(cat, items):
    lines = [f"# {cat} ({CATEGORY_LABEL[cat]})", "", CATEGORY_INTRO[cat], "",
             "## Elemente", ""]
    for it in items:
        lines.append(f"- [**{it['name']}**](./{it['name']}/) – {it['kurz']}")
    lines += ["", "## Steckbriefe", "",
              "| Komponente | Erbt von | Varianten | Rolle | Status |",
              "|------------|----------|-----------|-------|--------|"]
    for it in items:
        f = it["fields"]
        lines.append("| [{0}](./{0}/) | {1} | {2} | {3} | {4} |".format(
            it["name"], f.get("Erbt von", "-"), f.get("Varianten", "-"),
            f.get("Rolle", "-"), f.get("Status", "-")))
    lines += ["", "## Siehe auch", "", "- [Komponenten-Übersicht](../index.md)",
              "- [Basiskomponente](../basics/base/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def components_page(data):
    total = sum(len(v) for v in data.values())
    lines = ["# UI-Komponenten & Elemente", "",
             "Diese Dokumentation beschreibt die UI-Elemente, die in FreeSynergy-Programmen",
             "verwendet werden.", "", "## Grundlagen", "",
             "Alle Komponenten erben von der **Basisklasse** "
             "[base](basics/base.md): geerbte Attribute, Größen-Raster, Zustände,",
             "Barrierefreiheit, Dateisatz und Namenskonvention. Eine Komponentendatei",
             "listet nur ihre **eigenen** Attribute.", "",
             f"## Kategorien ({len(data)}) — {total} Komponenten", ""]
    for cat in CATEGORY_ORDER:
        if cat not in data:
            continue
        lines.append(f"### [{cat}](./{cat}/) — {CATEGORY_LABEL[cat]} ({len(data[cat])})")
        lines.append("")
        lines.append(CATEGORY_INTRO[cat])
        lines.append("")
        lines.append(", ".join(f"[{it['name']}](./{cat}/{it['name']}/)" for it in data[cat]))
        lines.append("")
    lines += ["## Was ist hier dokumentiert?", "",
              "Jede Komponente hat einen festen Dateisatz:", "",
              "- **description.md** – Steckbrief, Beschreibung, Verwendungszweck, Varianten, Abgrenzung",
              "- **appearance.md** – Aussehen: Layout, Größen, Farben, Zustände, Reaktiv",
              "- **attributes.md** – nur **eigene** Attribute + Verweis auf `basics/base.md`",
              "- **usage.md** – Anwendung, Szenarien und Beispiele", "",
              "Die Listen und Zahlen auf dieser Seite erzeugt `tools/gen_component_indexes.py`."
              " `tools/check_components.py` prüft den Standard.", "", "## Siehe auch", "",
              "- [Konzept und Plan](konzept-und-plan.md) – Standardisierung, Kategorien, Merges",
              "- [Gesten](../gestures/) und [Animationen](../animations/)",
              "- [Standardisierte Daten](../data/)", "- [Apps](../apps/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def nav_block(data):
    """Volstaendiger Nav-Abschnitt: jede Kategorie mit ihrem index.md und jede
    Komponente mit ihrem Dateisatz, damit keine Seite ohne Navigationspfad ist."""
    lines = ["  - de/components/:", "      - de/components/index.md"]
    for cat in CATEGORY_ORDER:
        if cat not in data:
            continue
        lines.append(f"      - de/components/{cat}/:")
        lines.append(f"          - de/components/{cat}/index.md")
        for it in data[cat]:
            base = f"de/components/{cat}/{it['name']}"
            lines.append(f"          - {it['name']}:")
            for part in ("description.md", "appearance.md", "attributes.md", "usage.md"):
                if (COMPONENTS / cat / it["name"] / part).is_file():
                    lines.append(f"              - {base}/{part}")
    return "\n".join(lines)


def patch_mkdocs(data, write):
    text = MKDOCS.read_text(encoding="utf-8")
    block = nav_block(data)
    begin, end = "# BEGIN components nav", "# END components nav"
    if begin in text and end in text:
        head, rest = text.split(begin, 1)
        _old, tail = rest.split(end, 1)
        new = f"{head}{begin}\n{block}\n{end}{tail}"
    else:
        marker = re.search(r"  - de/components/:\n(?:      - .*\n)+", text)
        if not marker:
            print("mkdocs.yml: kein components-Abschnitt gefunden")
            return False
        new = text[:marker.start()] + f"{begin}\n{block}\n{end}\n" + text[marker.end():]
    if new == text:
        return True
    if write:
        MKDOCS.write_text(new, encoding="utf-8")
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nichts schreiben, exit 1 bei Abweichung")
    args = ap.parse_args()

    data = collect()
    stale = []
    targets = {COMPONENTS / "index.md": components_page(data)}
    for cat, items in data.items():
        targets[COMPONENTS / cat / "index.md"] = category_page(cat, items)
    for path, content in targets.items():
        current = path.read_text(encoding="utf-8") if path.is_file() else ""
        if current != content:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    # patch_mkdocs liefert True, wenn der Nav-Block bereits aktuell ist
    if not patch_mkdocs(data, not args.check):
        stale.append("mkdocs.yml")

    total = sum(len(v) for v in data.values())
    if args.check and stale:
        print("Veraltet (Bitte tools/gen_component_indexes.py ausführen):")
        for s in stale:
            print(f"  - {s}")
        return 1
    print(f"{len(data)} Kategorien, {total} Komponenten, "
          f"{'geprüfte' if args.check else 'geschriebene'} Dateien: {len(targets)} + mkdocs.yml")
    return 0


if __name__ == "__main__":
    sys.exit(main())

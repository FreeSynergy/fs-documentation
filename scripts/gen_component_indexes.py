#!/usr/bin/env python3
"""Erzeugt die Uebersichtsseiten der Komponenten aus den Steckbriefen.

Layout (Beschluss 0001 und 0004): components/ traegt drei Bander (= Ebenen),
in jedem Band die Typgruppen, in der Typgruppe die Komponente:

    components/<band>/<typgruppe>/<komponente>/

- docs/de/components/index.md                      (Baender, Typgruppen, Zahlen)
- docs/de/components/<band>/index.md               (Typgruppen des Bands)
- docs/de/components/<band>/<typgruppe>/index.md   (Elemente der Typgruppe)
- mkdocs.yml                                       (Nav-Abschnitt zwischen Markern)

Die Zuordnung Komponente -> Band steht in ASSIGNMENT und ist die Maschine-Lesung
von conventions/CONVENTIONS.md Abschnitt 3. Sie ist verbindlich: fehlt eine
Komponente in der Liste oder steht eine auf der Platte, die nicht gelistet ist,
bricht das Skript mit Hinweis ab (statt still eine Luecke zu erzeugen).

Die Zahlen stimmen damit immer mit dem Bestand ueberein (Konzept Abschnitt 8).
Einleitungsabsaetze sind im Skript hinterlegt, damit sie bei jedem Lauf gleich bleiben.

Aufforderung:
    python3 scripts/gen_component_indexes.py             # schreiben
    python3 scripts/gen_component_indexes.py --check     # Pruefen (CI), exit 1 bei Abweichung
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "de"
COMPONENTS = DOCS / "components"
MKDOCS = ROOT / "mkdocs.yml"

BANDS = ["primitives", "widgets", "workbenches"]
BAND_LABEL = {
    "primitives": "Grundbausteine",
    "widgets": "Bausteine mit bekanntem Inhalt",
    "workbenches": "Offene Arbeitsflaechen",
}
BAND_INTRO = {
    "primitives": "Nicht weiter zerlegbar: ein Wert, eine Geste, ein Zustand. "
                  "Kein Band enthält Inhalte, die es erst zur Laufzeit bekommt.",
    "widgets": "Kennt seine Inhalte beim Bauen: bindet ein bekanntes Datenmodell, "
               "hat endliche Kinder und eigenen Zustand.",
    "workbenches": "Erhält seinen Inhalt erst zur Laufzeit: offene Fläche, die selbst "
                   "primitives und widgets aufnehmen darf.",
}
BAND_TEST = {
    "primitives": "nicht weiter zerlegbar",
    "widgets": "kennt seine Inhalte beim Bauen",
    "workbenches": "erhält Inhalte erst zur Laufzeit",
}

# Zuordnung aus conventions/CONVENTIONS.md Abschnitt 3 (ADr 0004).
ASSIGNMENT = {
    "primitives": {
        "basics": ["base", "kbd", "label", "link", "separator"],
        "actions": ["button", "button-group", "floating-action-button"],
        "feedback": ["alert", "badge", "empty-state", "progress", "skeleton", "spinner",
                     "toast"],
        "fields": ["checkbox", "color-input", "combobox", "date-input", "field",
                   "input-group", "mention-input", "number-input", "otp-input",
                   "radio-group", "rating", "search-field", "select",
                   "slider", "switch", "tags-input", "text-input", "textarea"],
        "media": ["icon", "image"],
    },
    "widgets": {
        "containers": ["accordion", "card", "panel", "scroll-area", "split-view",
                       "wizard"],
        "navigation": ["bottom-navigation", "breadcrumb", "command", "language-switcher",
                       "menu", "pagination", "radial-menu", "sidebar", "tabs", "toolbar"],
        "overlays": ["alert-dialog", "context-menu", "drawer", "hover-card", "modal",
                     "popover", "tooltip"],
        "data": ["avatar", "calendar-view", "chart", "description-list", "grid-view",
                 "list-view", "repeater", "table", "table-of-contents", "timeline",
                 "tree-view"],
        "fields": ["date-picker", "emoji-picker", "file-upload", "range-calendar",
                   "time-picker"],
        "media": ["audio", "video", "media-player", "carousel", "gallery"],
        "special": ["map-view"],
    },
    "workbenches": {
        "special": ["code-editor", "dashboard", "embed", "whiteboard"],
        "fields": ["rich-text-editor"],
    },
}

# base.md ist die Basisklasse: keine eigenen Dateien, eigener Pfad im Band basics.
BASE_ENTRY = ("primitives", "basics", "base")

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
            "die Felder zum Einsatz.",
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
# Reihenfolge der Typgruppen pro Band (Gruppen ohne Eintrag fallen weg).
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


def inventory():
    """Bestand von der Platte, gegen ASSIGNMENT geprueft.

    Liefert {band: {typgruppe: [ {name, fields, kurz, has_usage} ]}}.
    Bei Abweichung zwischen Platte und ASSIGNMENT wird abgebrochen.
    """
    on_disk = {}
    for band in BANDS:
        for cat in COMPONENTS.glob(f"{band}/*/"):
            if not cat.is_dir():
                continue
            for comp in sorted(d for d in cat.iterdir() if d.is_dir()):
                on_disk.setdefault(band, {}).setdefault(cat.name, []).append(comp.name)

    want = {band: {cat: sorted(names) for cat, names in groups.items()}
            for band, groups in ASSIGNMENT.items()}
    have = {band: {cat: sorted(names) for cat, names in groups.items()}
            for band, groups in on_disk.items()}

    problems = []
    for band, groups in want.items():
        for cat, names in groups.items():
            got = have.get(band, {}).get(cat, [])
            for name in names:
                if name == "base":
                    if not (COMPONENTS / band / cat / "base.md").is_file():
                        problems.append(f"{band}/{cat}/base.md fehlt auf der Platte")
                elif name not in got:
                    problems.append(f"{band}/{cat}/{name} fehlt auf der Platte")
    for band, groups in have.items():
        for cat, names in groups.items():
            for name in names:
                if name not in want.get(band, {}).get(cat, []):
                    problems.append(f"{band}/{cat}/{name} steht nicht in ASSIGNMENT "
                                    f"(conventions/CONVENTIONS.md Abschnitt 3)")
    if problems:
        print("Bestand passt nicht zur Zuordnung:")
        for p in problems:
            print(f"  ! {p}")
        raise SystemExit(1)

    data = {}
    for band, groups in ASSIGNMENT.items():
        for cat, names in groups.items():
            items = []
            for name in names:
                if name == "base":
                    continue
                comp = COMPONENTS / band / cat / name
                desc = comp / "description.md"
                if not desc.is_file():
                    continue
                text = desc.read_text(encoding="utf-8")
                items.append({
                    "name": name,
                    "fields": steckbrief(text),
                    "kurz": kurz(text),
                    "has_usage": (comp / "usage.md").is_file(),
                })
            if items:
                data.setdefault(band, {})[cat] = items
    return data


def ordered_cats(band, data):
    return [c for c in CATEGORY_ORDER if c in data.get(band, {})]


def base_link(band, cat):
    """Relativer Link auf die Basisklasse aus components/<band>/<cat>/index.md."""
    if (band, cat) == ("primitives", "basics"):
        return "./base.md"
    if band == "primitives":
        return "../basics/base.md"
    return "../../primitives/basics/base.md"


def band_page(band, data):
    total = sum(len(v) for v in data[band].values())
    lines = [f"# {band} – {BAND_LABEL[band]}", "",
             f"{BAND_INTRO[band]} Testfrage: *{BAND_TEST[band]}*.", "",
             f"## Typgruppen ({len(data[band])}) — {total} Komponenten", ""]
    for cat in ordered_cats(band, data):
        items = data[band][cat]
        lines.append(f"### [{cat}](./{cat}/) — {CATEGORY_LABEL[cat]} ({len(items)})")
        lines.append("")
        lines.append(CATEGORY_INTRO[cat])
        lines.append("")
        lines.append(", ".join(f"[{it['name']}](./{cat}/{it['name']}/)" for it in items))
        lines.append("")
    lines += ["## Siehe auch", "",
              "- [Komponenten-Übersicht](../index.md)"]
    if band == "primitives":
        lines += ["- [Basisklasse](./basics/base.md)"]
    else:
        lines += ["- [Basisklasse](../primitives/basics/base.md)"]
    for other in BANDS:
        if other != band:
            lines.append(f"- [{other}](../{other}/) – {BAND_LABEL[other]}")
    lines += ["- [Gesten](../../interactions/gestures/) und "
              "[Animationen](../../interactions/animations/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def category_page(band, cat, items):
    lines = [f"# {cat} ({CATEGORY_LABEL[cat]})", "",
             f"Band [{band}](../) – {BAND_TEST[band]}.", "", CATEGORY_INTRO[cat], "",
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
    lines += ["", "## Siehe auch", "",
              f"- [Komponenten-Übersicht](../../index.md)",
              f"- [Band {band}](../)"]
    if (band, cat) != BASE_ENTRY[:2]:
        lines.append(f"- [Basiskomponente]({base_link(band, cat)})")
    if cat == "data":
        lines.append("- [Felder](../../primitives/fields/) zum Ändern")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def components_page(data):
    total = sum(len(items) for groups in data.values() for items in groups.values())
    cats = sorted({c for groups in data.values() for c in groups})
    lines = ["# UI-Komponenten & Elemente", "",
             "Diese Dokumentation beschreibt die UI-Elemente, die in FreeSynergy-Programmen",
             "verwendet werden. Sie sind nach Ebene sortiert: `primitives` → `widgets` →",
             "`workbenches` (Beschlüsse 0001 und 0004); die Typgruppen (basics, fields, …)",
             "bleiben innerhalb der Bänder erhalten.", "", "## Grundlagen", "",
             "Alle Komponenten erben von der **Basisklasse** "
             "[base](primitives/basics/base.md): geerbte Attribute, Größen-Raster, Zustände,",
             "Barrierefreiheit, Dateisatz und Namenskonvention. Eine Komponentendatei",
             "listet nur ihre **eigenen** Attribute.", "",
             f"## Bänder ({len(BANDS)}) — {total} Komponenten, {len(cats)} Typgruppen", ""]
    for band in BANDS:
        n = sum(len(v) for v in data.get(band, {}).values())
        lines.append(f"### [{band}](./{band}/) — {BAND_LABEL[band]} ({n})")
        lines.append("")
        lines.append(BAND_INTRO[band])
        lines.append("")
        for cat in ordered_cats(band, data):
            items = data[band][cat]
            lines.append(f"#### [{cat}](./{band}/{cat}/) — {CATEGORY_LABEL[cat]} "
                         f"({len(items)})")
            lines.append("")
            lines.append(", ".join(f"[{it['name']}](./{band}/{cat}/{it['name']}/)"
                                   for it in items))
            lines.append("")
    lines += ["## Was ist hier dokumentiert?", "",
              "Jede Komponente hat einen festen Dateisatz:", "",
              "- **description.md** – Steckbrief, Beschreibung, Verwendungszweck, Varianten, Abgrenzung",
              "- **appearance.md** – Aussehen: Layout, Größen, Farben, Zustände, Reaktiv",
              "- **attributes.md** – nur **eigene** Attribute + Verweis auf `primitives/basics/base.md`",
              "- **usage.md** – Anwendung, Szenarien und Beispiele", "",
              "Die Listen und Zahlen auf dieser Seite erzeugt `scripts/gen_component_indexes.py`."
              " `scripts/check_components.py` prüft den Standard.", "", "## Siehe auch", "",
              "- [Gesten](../interactions/gestures/) und [Animationen](../interactions/animations/)",
              "- [Standardisierte Daten](../data/)", "- [Programs](../programs/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def nav_block(data):
    """Volstaendiger Nav-Abschnitt: Band, Typgruppe, index.md und jede Komponente mit
    ihrem Dateisatz, damit keine Seite ohne Navigationspfad ist."""
    lines = ["  - de/components/:", "      - de/components/index.md"]
    for band in BANDS:
        lines.append(f"      - de/components/{band}/:")
        lines.append(f"          - de/components/{band}/index.md")
        for cat in ordered_cats(band, data):
            lines.append(f"          - de/components/{band}/{cat}/:")
            lines.append(f"              - de/components/{band}/{cat}/index.md")
            if (band, cat) == BASE_ENTRY[:2]:
                lines.append(f"              - de/components/{band}/{cat}/base.md")
            for it in data[band][cat]:
                base = f"de/components/{band}/{cat}/{it['name']}"
                lines.append(f"              - {it['name']}:")
                for part in ("description.md", "appearance.md", "attributes.md", "usage.md"):
                    if (COMPONENTS / band / cat / it["name"] / part).is_file():
                        lines.append(f"                  - {base}/{part}")
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

    data = inventory()
    stale = []
    targets = {COMPONENTS / "index.md": components_page(data)}
    for band in BANDS:
        if band in data:
            targets[COMPONENTS / band / "index.md"] = band_page(band, data)
        for cat, items in data.get(band, {}).items():
            targets[COMPONENTS / band / cat / "index.md"] = category_page(band, cat, items)
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

    total = sum(len(items) for groups in data.values() for items in groups.values())
    if args.check and stale:
        print("Veraltet (Bitte scripts/gen_component_indexes.py ausführen):")
        for s in stale:
            print(f"  - {s}")
        return 1
    n_cats = len({c for groups in data.values() for c in groups})
    print(f"{len(BANDS)} Bänder, {n_cats} Typgruppen, {total} Komponenten, "
          f"{'geprüfte' if args.check else 'geschriebene'} Dateien: {len(targets)} + mkdocs.yml")
    return 0


if __name__ == "__main__":
    sys.exit(main())

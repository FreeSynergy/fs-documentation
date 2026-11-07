#!/usr/bin/env python3
"""Erzeugt die Uebersichtsseiten der Komponenten aus den Steckbriefen.

Layout (Beschluss 0001 und 0004): components/ traegt drei Bander (= Ebenen),
in jedem Band die Typgruppen, in der Typgruppe die Komponente:

    components/<band>/<typgruppe>/<komponente>/

- docs/<lang>/components/index.md                      (Baender, Typgruppen, Zahlen)
- docs/<lang>/components/<band>/index.md               (Typgruppen des Bands)
- docs/<lang>/components/<band>/<typgruppe>/index.md   (Elemente der Typgruppe)

Die Zuordnung Komponente -> Band steht in ASSIGNMENT und ist die Maschine-Lesung
von conventions/CONVENTIONS.md Abschnitt 3. Sie ist verbindlich: fehlt eine
Komponente in der Liste oder steht eine auf der Platte, die nicht gelistet ist,
bricht das Skript mit Hinweis ab (statt still eine Luecke zu erzeugen).

Die Zahlen stimmen damit immer mit dem Bestand ueberein (Konzept Abschnitt 8).
Einleitungsabsaetze sind im Skript hinterlegt, damit sie bei jedem Lauf gleich bleiben.

Aufforderung:
    python3 scripts/gen_component_indexes.py [--lang en|de]          # schreiben (Standard: en)
    python3 scripts/gen_component_indexes.py --check     # Pruefen (CI), exit 1 bei Abweichung
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["en", "de"]  # en ist die Hauptsprache (ADR 0011); Reihenfolge = Nav-Reihenfolge


def components_dir(lang):
    return ROOT / "docs" / lang / "components"


BANDS = ["primitives", "widgets", "workbenches"]

# Zuordnung aus conventions/CONVENTIONS.md Abschnitt 3 (ADr 0004). Sie gilt fuer beide
# Sprachbaeume; im Baum `de` duerfen Komponenten noch fehlen (maschinelle Uebersetzung
# hinkt hinterher), im Baum `en` nicht.
ASSIGNMENT = {
    "primitives": {
        "basics": ["base", "kbd", "label", "link", "separator"],
        "actions": ["button", "button-group", "floating-action-button"],
        "feedback": ["alert", "badge", "empty-state", "encryption-state", "message-status",
                     "progress", "skeleton", "spinner", "toast"],
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
        "overlays": ["alert-dialog", "context-menu", "drawer", "hover-card",
                     "key-verification", "modal", "popover", "tooltip"],
        "data": ["avatar", "calendar-view", "chart", "description-list", "grid-view",
                 "link-preview", "list-view", "mail-view", "message-bubble",
                 "message-list", "reaction-bar", "repeater", "table",
                 "table-of-contents", "timeline", "tree-view"],
        "fields": ["date-picker", "emoji-picker", "file-upload", "range-calendar",
                   "rule-editor", "time-picker"],
        "media": ["audio", "video", "media-player", "call-controls", "carousel",
                  "gallery"],
        "special": ["map-view"],
    },
    "workbenches": {
        "special": ["code-editor", "dashboard", "embed", "html-view", "message-composer",
                    "whiteboard"],
        "fields": ["block-editor", "rich-text-editor"],
    },
}

# base.md ist die Basisklasse: keine eigenen Dateien, eigener Pfad im Band basics.
BASE_ENTRY = ("primitives", "basics", "base")

# Reihenfolge der Typgruppen pro Band (Gruppen ohne Eintrag fallen weg).
CATEGORY_ORDER = ["basics", "actions", "navigation", "containers", "overlays", "feedback",
                  "fields", "data", "media", "special"]

# Texte pro Sprache. Steckbrief-Schluessel (`keys`) heissen in der Datei je nach Sprache
# anders; `desc` ist die Ueberschrift des Beschreibungsabschnitts.
TEXTS = {
    "de": {
        "keys": {"inherits": "Erbt von", "variants": "Varianten", "role": "Rolle",
                 "status": "Status"},
        "desc": "beschreibung",
        "band_label": {"primitives": "Grundbausteine",
                       "widgets": "Bausteine mit bekanntem Inhalt",
                       "workbenches": "Offene Arbeitsflaechen"},
        "band_intro": {
            "primitives": "Nicht weiter zerlegbar: ein Wert, eine Geste, ein Zustand. "
                          "Kein Band enthält Inhalte, die es erst zur Laufzeit bekommt.",
            "widgets": "Kennt seine Inhalte beim Bauen: bindet ein bekanntes Datenmodell, "
                       "hat endliche Kinder und eigenen Zustand.",
            "workbenches": "Erhält seinen Inhalt erst zur Laufzeit: offene Fläche, die "
                           "selbst primitives und widgets aufnehmen darf.",
        },
        "band_test": {"primitives": "nicht weiter zerlegbar",
                      "widgets": "kennt seine Inhalte beim Bauen",
                      "workbenches": "erhält Inhalte erst zur Laufzeit"},
        "cat_intro": {
            "basics": "Grundlagen, von denen alle anderen Komponenten ausgehen: die "
                      "Basisklasse mit ihren geerbten Attributen, Zuständen und Tokens "
                      "sowie die kleinsten Bausteine.",
            "actions": "Action-Elemente lösen eine einzelne Handlung aus oder bündeln "
                       "zusammengehörige Handlungen. Sie verändern Daten oder Zustände, "
                       "aber nicht die Adresse.",
            "navigation": "Elemente, die den Weg durch das Programm zeigen oder "
                          "umschalten: Menüs, Leisten, Reiter, Seitenleisten und "
                          "Pfadangaben.",
            "containers": "Boxen und Flächen, die anderen Inhalt aufnehmen: Karten, "
                          "Panels, aufklappbare Gruppen, geteilte Ansichten und "
                          "Assistenten.",
            "overlays": "Elemente, die über anderem Inhalt erscheinen und eigenen Fokus "
                        "bekommen. Sie haben eine eigene Lebensdauer und schließen mit "
                        "`Esc` oder Klick außerhalb.",
            "feedback": "Elemente, die den Zustand einer Anwendung sichtbar machen: "
                        "Meldungen, Fortschritt, Ladezustände und Kennzeichnungen.",
            "fields": "Elemente zum Eingeben und Auswählen von Werten. Das Feld (`field`) "
                      "hält dabei Beschriftung, Hilfetext und Fehlermeldung zusammen.",
            "data": "Elemente, die Daten darstellen: Listen, Tabellen, Raster, Bäume, "
                    "Zeitachsen und Diagramme. Sie bearbeiten Werte, sondern zeigen sie "
                    "— zum Ändern kommen die Felder zum Einsatz.",
            "media": "Elemente, die Medien wiedergeben oder darstellen. `media-player` "
                     "ist die Elternklasse von `audio` und `video`.",
            "special": "Zusammengesetzte Elemente mit eigener Datenstruktur: Editoren, "
                       "Einbettungen, Karten und Ansichten, die es bei generischen "
                       "Bibliotheken nicht gibt.",
        },
        "cat_label": {
            "basics": "Grundlagen", "actions": "Aktionen", "navigation": "Navigation",
            "containers": "Container", "overlays": "Overlays", "feedback": "Rückmeldung",
            "fields": "Felder", "data": "Daten", "media": "Medien",
            "special": "Spezielle Elemente"},
        "t": {
            "test": "Testfrage", "groups": "Typgruppen", "components": "Komponenten",
            "see_also": "Siehe auch", "overview": "Komponenten-Übersicht",
            "base_class": "Basisklasse", "base_comp": "Basiskomponente",
            "band": "Band", "gestures": "Gesten", "animations": "Animationen",
            "elements": "Elemente", "profiles": "Steckbriefe",
            "h_comp": "Komponente", "h_inh": "Erbt von", "h_var": "Varianten",
            "h_role": "Rolle", "h_status": "Status",
            "fields_change": "zum Ändern",
            "title": "UI-Komponenten & Elemente",
            "intro": ["Diese Dokumentation beschreibt die UI-Elemente, die in "
                      "FreeSynergy-Programmen",
                      "verwendet werden. Sie sind nach Ebene sortiert: `primitives` → "
                      "`widgets` →",
                      "`workbenches` (Beschlüsse 0001 und 0004); die Typgruppen (basics, "
                      "fields, …)",
                      "bleiben innerhalb der Bänder erhalten."],
            "fundamentals": "Grundlagen",
            "fund_text": ["Alle Komponenten erben von der **Basisklasse** "
                          "[base](primitives/basics/base.md): geerbte Attribute, "
                          "Größen-Raster, Zustände,",
                          "Barrierefreiheit, Dateisatz und Namenskonvention. Eine "
                          "Komponentendatei",
                          "listet nur ihre **eigenen** Attribute."],
            "bands": "Bänder", "groups_n": "Typgruppen",
            "what": "Was ist hier dokumentiert?",
            "fileset": "Jede Komponente hat einen festen Dateisatz:",
            "files": [
                "- **description.md** – Steckbrief, Beschreibung, Verwendungszweck, "
                "Varianten, Abgrenzung",
                "- **appearance.md** – Aussehen: Layout, Größen, Farben, Zustände, "
                "Reaktiv",
                "- **attributes.md** – nur **eigene** Attribute + Verweis auf "
                "`primitives/basics/base.md`",
                "- **usage.md** – Anwendung, Szenarien und Beispiele"],
            "generated": "Die Listen und Zahlen auf dieser Seite erzeugt "
                         "`scripts/gen_component_indexes.py`. "
                         "`scripts/check_components.py` prüft den Standard.",
            "data_std": "Standardisierte Daten", "programs": "Programs",
            "and": "und",
        },
    },
    "en": {
        "keys": {"inherits": "Inherits from", "variants": "Variants", "role": "Role",
                 "status": "Status"},
        "desc": "description",
        "band_label": {"primitives": "building blocks",
                       "widgets": "building blocks with known content",
                       "workbenches": "open work surfaces"},
        "band_intro": {
            "primitives": "Cannot be broken down further: one value, one gesture, one "
                          "state. No band contains content it only receives at runtime.",
            "widgets": "It knows its contents when it is built: it binds a known data "
                       "model, has finite children and its own state.",
            "workbenches": "It receives its content only at runtime: an open surface "
                           "that may itself hold primitives and widgets.",
        },
        "band_test": {"primitives": "cannot be broken down further",
                      "widgets": "knows its contents when it is built",
                      "workbenches": "receives its content only at runtime"},
        "cat_intro": {
            "basics": "The fundamentals all other components start from: the base class "
                      "with its inherited attributes, states and tokens, plus the "
                      "smallest building blocks.",
            "actions": "Action elements trigger a single action or bundle related "
                       "actions. They change data or state, but not the address.",
            "navigation": "Elements that show or switch the way through the program: "
                          "menus, bars, tabs, sidebars and path indications.",
            "containers": "Boxes and surfaces that hold other content: cards, panels, "
                          "collapsible groups, split views and assistants.",
            "overlays": "Elements that appear above other content and get their own "
                        "focus. They have a lifetime of their own and close with `Esc` "
                        "or a click outside.",
            "feedback": "Elements that make the state of an application visible: "
                        "messages, progress, loading states and markers.",
            "fields": "Elements for entering and selecting values. The field (`field`) "
                      "holds the label, help text and error message together.",
            "data": "Elements that present data: lists, tables, grids, trees, "
                    "timelines and charts. They do not edit values but show them — the "
                    "fields are what changes them.",
            "media": "Elements that play or show media. `media-player` is the parent "
                     "class of `audio` and `video`.",
            "special": "Composite elements with a data structure of their own: editors, "
                       "embeds, maps and views that generic libraries do not offer.",
        },
        "cat_label": {
            "basics": "fundamentals", "actions": "actions", "navigation": "navigation",
            "containers": "containers", "overlays": "overlays", "feedback": "feedback",
            "fields": "fields", "data": "data", "media": "media",
            "special": "special elements"},
        "t": {
            "test": "Test question", "groups": "Type groups", "components": "components",
            "see_also": "See also", "overview": "Component overview",
            "base_class": "Base class", "base_comp": "Base component",
            "band": "Band", "gestures": "Gestures", "animations": "Animations",
            "elements": "Elements", "profiles": "Profiles",
            "h_comp": "Component", "h_inh": "Inherits from", "h_var": "Variants",
            "h_role": "Role", "h_status": "Status",
            "fields_change": "for making changes",
            "title": "UI components & elements",
            "intro": ["This documentation describes the UI elements used in "
                      "FreeSynergy programs. They",
                      "are sorted by level: `primitives` → `widgets` → `workbenches` "
                      "(decisions 0001 and",
                      "0004); the type groups (basics, fields, …) are kept inside the "
                      "bands."],
            "fundamentals": "Fundamentals",
            "fund_text": ["All components inherit from the **base class** "
                          "[base](primitives/basics/base.md):",
                          "inherited attributes, size grid, states, accessibility, file "
                          "set and naming",
                          "convention. A component file lists only its **own** "
                          "attributes."],
            "bands": "Bands", "groups_n": "type groups",
            "what": "What is documented here?",
            "fileset": "Every component has a fixed file set:",
            "files": [
                "- **description.md** – profile, description, purpose, variants, "
                "distinction",
                "- **appearance.md** – looks: layout, sizes, colours, states, "
                "responsive",
                "- **attributes.md** – only **own** attributes + reference to "
                "`primitives/basics/base.md`",
                "- **usage.md** – application, scenarios and examples"],
            "generated": "The lists and numbers on this page are generated by "
                         "`scripts/gen_component_indexes.py`. "
                         "`scripts/check_components.py` checks the standard.",
            "data_std": "Standardised data", "programs": "Programs",
            "and": "and",
        },
    },
}

# Aktive Sprache; set_lang() setzt die Modulvariablen (COMPONENTS, TX, ...).
LANG = "en"
COMPONENTS = components_dir(LANG)
TX = TEXTS[LANG]


def set_lang(lang):
    global LANG, COMPONENTS, TX
    LANG, COMPONENTS, TX = lang, components_dir(lang), TEXTS[lang]


def T(key):
    return TX["t"][key]
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
    """Erster Satz aus dem Beschreibungsabschnitt."""
    on, out = False, []
    for line in text.splitlines():
        if line.startswith("## "):
            if on:
                break
            on = line[3:].strip().lower() == TX["desc"]
        elif on and line.strip():
            out.append(line.strip())
    sentence = " ".join(out)
    m = re.match(r"^(.*?[.!?])(\s|$)", sentence)
    return (m.group(1) if m else sentence[:120]).strip()


def inventory():
    """Bestand der aktiven Sprache von der Platte, gegen ASSIGNMENT geprueft.

    Liefert {band: {typgruppe: [ {name, fields, kurz, has_usage} ]}}.
    Auf der Platte stehende, nicht zugeordnete Komponenten brechen immer ab. Fehlende
    brechen nur im Baum `en` ab; im Baum `de` (maschinelle Uebersetzung) werden sie
    uebersprungen.
    """
    on_disk = {}
    for band in BANDS:
        for cat in COMPONENTS.glob(f"{band}/*/"):
            if not cat.is_dir():
                continue
            for comp in sorted(d for d in cat.iterdir() if d.is_dir()):
                on_disk.setdefault(band, {}).setdefault(cat.name, []).append(comp.name)

    problems = []
    if LANG == "en":
        for band, groups in ASSIGNMENT.items():
            for cat, names in groups.items():
                got = on_disk.get(band, {}).get(cat, [])
                for name in names:
                    if name == "base":
                        if not (COMPONENTS / band / cat / "base.md").is_file():
                            problems.append(f"{band}/{cat}/base.md fehlt auf der Platte")
                    elif name not in got:
                        problems.append(f"{band}/{cat}/{name} fehlt auf der Platte")
    for band, groups in on_disk.items():
        for cat, names in groups.items():
            for name in names:
                if name not in ASSIGNMENT.get(band, {}).get(cat, []):
                    problems.append(f"{band}/{cat}/{name} steht nicht in ASSIGNMENT "
                                    f"(conventions/CONVENTIONS.md Abschnitt 3)")
    if problems:
        print(f"[{LANG}] Bestand passt nicht zur Zuordnung:")
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
    lines = [f"# {band} – {TX['band_label'][band]}", "",
             f"{TX['band_intro'][band]} {T('test')}: *{TX['band_test'][band]}*.", "",
             f"## {T('groups')} ({len(data[band])}) — {total} {T('components')}", ""]
    for cat in ordered_cats(band, data):
        items = data[band][cat]
        lines.append(f"### [{cat}](./{cat}/) — {TX['cat_label'][cat]} ({len(items)})")
        lines.append("")
        lines.append(TX["cat_intro"][cat])
        lines.append("")
        lines.append(", ".join(f"[{it['name']}](./{cat}/{it['name']}/)" for it in items))
        lines.append("")
    lines += [f"## {T('see_also')}", "",
              f"- [{T('overview')}](../index.md)"]
    if band == "primitives":
        lines += [f"- [{T('base_class')}](./basics/base.md)"]
    else:
        lines += [f"- [{T('base_class')}](../primitives/basics/base.md)"]
    for other in BANDS:
        if other != band:
            lines.append(f"- [{other}](../{other}/) – {TX['band_label'][other]}")
    lines += [f"- [{T('gestures')}](../../interactions/gestures/) {T('and')} "
              f"[{T('animations')}](../../interactions/animations/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def category_page(band, cat, items):
    k = TX["keys"]
    head = f"# {cat}" if LANG == "en" else f"# {cat} ({TX['cat_label'][cat]})"
    lines = [head, "",
             f"{T('band')} [{band}](../) – {TX['band_test'][band]}.", "",
             TX["cat_intro"][cat], "", f"## {T('elements')}", ""]
    for it in items:
        lines.append(f"- [**{it['name']}**](./{it['name']}/) – {it['kurz']}")
    lines += ["", f"## {T('profiles')}", "",
              f"| {T('h_comp')} | {T('h_inh')} | {T('h_var')} | {T('h_role')} | "
              f"{T('h_status')} |",
              "|" + "-" * 12 + "|" + "-" * 10 + "|" + "-" * 11 + "|" + "-" * 7 + "|"
              + "-" * 8 + "|"]
    for it in items:
        f = it["fields"]
        lines.append("| [{0}](./{0}/) | {1} | {2} | {3} | {4} |".format(
            it["name"], f.get(k["inherits"], "-"), f.get(k["variants"], "-"),
            f.get(k["role"], "-"), f.get(k["status"], "-")))
    lines += ["", f"## {T('see_also')}", "",
              f"- [{T('overview')}](../../index.md)",
              f"- [{T('band')} {band}](../)"]
    if (band, cat) != BASE_ENTRY[:2]:
        lines.append(f"- [{T('base_comp')}]({base_link(band, cat)})")
    if cat == "data":
        lines.append(f"- [{TX['cat_label']['fields']}](../../primitives/fields/) "
                     f"{T('fields_change')}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def components_page(data):
    total = sum(len(items) for groups in data.values() for items in groups.values())
    cats = sorted({c for groups in data.values() for c in groups})
    lines = [f"# {T('title')}", ""] + T("intro") + [
        "", f"## {T('fundamentals')}", ""] + T("fund_text") + [
        "", f"## {T('bands')} ({len(BANDS)}) — {total} {T('components')}, "
            f"{len(cats)} {T('groups_n')}", ""]
    for band in BANDS:
        n = sum(len(v) for v in data.get(band, {}).values())
        lines.append(f"### [{band}](./{band}/) — {TX['band_label'][band]} ({n})")
        lines.append("")
        lines.append(TX["band_intro"][band])
        lines.append("")
        for cat in ordered_cats(band, data):
            items = data[band][cat]
            lines.append(f"#### [{cat}](./{band}/{cat}/) — {TX['cat_label'][cat]} "
                         f"({len(items)})")
            lines.append("")
            lines.append(", ".join(f"[{it['name']}](./{band}/{cat}/{it['name']}/)"
                                   for it in items))
            lines.append("")
    lines += [f"## {T('what')}", "", T("fileset"), ""] + T("files") + [
              "", T("generated"), "", f"## {T('see_also')}", "",
              f"- [{T('gestures')}](../interactions/gestures/) {T('and')} "
              f"[{T('animations')}](../interactions/animations/)",
              f"- [{T('data_std')}](../data/)", f"- [{T('programs')}](../programs/)", ""]
    return "\n".join(lines).rstrip() + "\n"


def build_targets(data):
    targets = {COMPONENTS / "index.md": components_page(data)}
    for band in BANDS:
        if band in data:
            targets[COMPONENTS / band / "index.md"] = band_page(band, data)
        for cat, items in data.get(band, {}).items():
            targets[COMPONENTS / band / cat / "index.md"] = category_page(band, cat, items)
    return targets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nichts schreiben, exit 1 bei Abweichung")
    ap.add_argument("--lang", choices=LANGS, default="en",
                    help="Sprachbaum fuer die Indexseiten (Standard: en)")
    args = ap.parse_args()

    # Die Navigation folgt den Ordnern (awesome-pages), es gibt nichts mehr in mkdocs.yml zu schreiben.
    set_lang(args.lang)
    data = inventory()

    stale = []
    targets = build_targets(data)
    for path, content in targets.items():
        current = path.read_text(encoding="utf-8") if path.is_file() else ""
        if current != content:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")

    total = sum(len(items) for groups in data.values() for items in groups.values())
    if args.check and stale:
        print(f"[{args.lang}] Veraltet (bitte scripts/gen_component_indexes.py "
              f"--lang {args.lang} ausführen):")
        for s in stale:
            print(f"  - {s}")
        return 1
    n_cats = len({c for groups in data.values() for c in groups})
    print(f"[{args.lang}] {len(BANDS)} Bänder, {n_cats} Typgruppen, {total} Komponenten, "
          f"{'geprüfte' if args.check else 'geschriebene'} Dateien: {len(targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

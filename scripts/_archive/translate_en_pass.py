#!/usr/bin/env python3
"""Mechanischer de->en Grunddurchlauf fuer components-Dokumente.

Uebersetzt die wiederkehrende Struktur (Ueberschriften, Steckbrief-Felder,
Tabellenkoepfe, Standardphrasen, Linktexte). Freie Prosa bleibt stehen und wird
danach von Hand uebersetzt; der Lauf meldet sie.

Aufruf:
    python3 scripts/_archive/translate_en_pass.py <datei> [...]
"""
import re
import sys
from pathlib import Path

# Seitentitel, die nicht nach dem Muster "Name (Glosse)" gebaut sind
TITLES = {
    "workbenches – Offene Arbeitsflaechen": "workbenches – open work surfaces",
    "widgets – Bausteine mit bekanntem Inhalt": "widgets – building blocks with known content",
    "primitives – Grundbausteine": "primitives – building blocks",
}

HEADINGS = {
    "Grundlayout": "Base layout",
    "Varianten": "Variants",
    "Größen": "Sizes",
    "Farben und Zustände": "Colours and states",
    "Hover- und Fokus-Effekte": "Hover and focus effects",
    "Hover-Effekte": "Hover effects",
    "Reaktiv": "Responsive",
    "Hauptattribute": "Main attributes",
    "Geerbt von": "Inherited from",
    "Barrierefreiheit": "Accessibility",
    "Events": "Events",
    "Verhalten": "Behaviour",
    "Beispiele": "Examples",
    "Darstellung": "Presentation",
    "Anwendung": "Application",
    "Szenarien": "Scenarios",
    "Elemente": "Elements",
    "Steckbriefe": "Profiles",
    "Hinweise": "Notes",
    "Siehe auch": "See also",
    "Beschreibung": "Description",
    "Verwendungszweck": "Purpose",
    "Abgrenzung": "Distinction",
    "Features": "Features",
    "Best Practices": "Best Practices",
    "Features-Attribute": "Features attributes",
    "Validation-Attribute": "Validation attributes",
    "Item-Attribute": "Item attributes",
    "Auto-Complete-Attribute": "Auto-complete attributes",
    "Steuerungs-Attribute": "Control attributes",
    "Navigation-Attribute": "Navigation attributes",
    "Interaktions-Attribute": "Interaction attributes",
    "Marker-Attribute": "Marker attributes",
    "API-Attribute": "API attributes",
    "Filter-Attribute": "Filter attributes",
    "Carousel-Attribute": "Carousel attributes",
    "Image-Attribute": "Image attributes",
    "Formate": "Formats",
    "Map-Types": "Map types",
    "Mit Event-Handlern": "With event handlers",
    "Mit Icons": "With icons",
    "In App": "In an app",
    "In Card": "In a card",
    "In Modal": "In a modal",
    "In Formular": "In a form",
}

CELLS = {
    "Feld": "Field",
    "Wert": "Value",
    "Kategorie": "Category",
    "Erbt von": "Inherits from",
    "Varianten": "Variants",
    "Zustände": "States",
    "Gesten": "Gestures",
    "Animationen": "Animations",
    "Verwandt": "Related",
    "Rolle": "Role",
    "Status": "Status",
    "Typ": "Type",
    "Attribut": "Attribute",
    "Beschreibung": "Description",
    "Verwendung": "Use",
    "Größe": "Size",
    "Größen": "Sizes",
    "Breite": "Width",
    "Höhe": "Height",
    "Breite/Höhe": "Width/height",
    "Icon-Größe": "Icon size",
    "Schriftgröße": "Font size",
    "Farbe": "Colour",
    "Farben und Zustände": "Colours and states",
    "Effekt": "Effect",
    "Zustand": "State",
    "Status": "State",
    "Aussehen": "Appearance",
    "Variante": "Variant",
    "Verhalten": "Behaviour",
    "Icon": "Icon",
    "Funktion": "Function",
    "Control": "Control",
    "Button": "Button",
    "Breakpoint": "Breakpoint",
    "Komponente": "Component",
    "Format": "Format",
    "dokumentiert": "documented",
    "Standard": "Standard",
}

LINKS = {
    "navigation – Übersicht": "navigation – overview",
    "media – Übersicht": "media – overview",
    "data – Übersicht": "data – overview",
    "fields – Übersicht": "fields – overview",
    "overlays – Übersicht": "overlays – overview",
    "containers – Übersicht": "containers – overview",
    "special – Übersicht": "special – overview",
    "basics – Übersicht": "basics – overview",
    "actions – Übersicht": "actions – overview",
    "feedback – Übersicht": "feedback – overview",
    "Komponenten-Übersicht": "Component overview",
    "Basiskomponente": "Base component",
    "Basisklasse": "Base class",
    "Gesten": "Gestures",
    "Animationen": "Animations",
    "Standardisierte Daten": "Standardised data",
}

PHRASES = [
    (r"\*\*Nicht verwechseln mit\*\*", "**Do not confuse with**"),
    (r'!!! info "Standardisierung"', '!!! info "Standardisation"'),
    (r'!!! info "Einordnung"', '!!! info "Classification"'),
    (r'!!! note "Herkunft"', '!!! note "Origin"'),
    (r'!!! important "Festlegung \(Standardisierung\)"',
     '!!! important "Decision (standardisation)"'),
    (r"^Nur \*\*eigene\*\* Attribute\. Alles andere kommt aus der Basisklasse, siehe$",
     "Only **own** attributes. Everything else comes from the base class, see"),

    (r"^Band \[workbenches\]\(\.\./\) – erhält Inhalte erst zur Laufzeit\.$",
     "Band [workbenches](../) – receives its contents only at runtime."),
    (r"^Band \[widgets\]\(\.\./\) – kennt seine Inhalte beim Bauen\.$",
     "Band [widgets](../) – knows its contents when it is built."),
    (r"^Band \[primitives\]\(\.\./\) – [^"]*\.$",
     "Band [primitives](../) – cannot be broken down further."),

    (r"Ist geöffnet\?", "is open?"),
    (r"Wird beim Selektieren ausgeführt", "runs when selecting"),
    (r"Eindeutige ID", "unique ID"),
    (r"Icon-Name", "icon name"),
    (r"Array von Menüpunkten", "array of menu items"),
    (r"Klick auf Overlay schließt\?", "a click on the overlay closes it?"),
    (r"Ein-/Ausklappbar\?", "can collapse and expand?"),
    (r"Hintergrund ändert sich", "the background changes"),
    (r"Aktive Sprache", "active language"),
    (r"Aktiver Menüpunkt", "active menu item"),
    (r"^\| \*\*Left Drawer\*\* \| Links \| Links \|$", "| **Left Drawer** | Left | Left |"),
    (r"^\| \*\*Right Drawer\*\* \| Rechts \| Rechts \|$", "| **Right Drawer** | Right | Right |"),
    (r"^\| \*\*Bottom Drawer\*\* \| Unten \| Unten \|$", "| **Bottom Drawer** | Bottom | Bottom |"),
    (r"unter dem Element", "below the element"),
    (r"über dem Element", "above the element"),
    (r"neben dem Element", "beside the element"),
    (r"Standard-Style", "standard style"),
    (r"^### Horizontal \(Standard\)$", "### Horizontal (standard)"),
    (r"Wird beim Start ausgeführt", "runs at the start"),
    (r"Wird beim Pausieren ausgeführt", "runs when pausing"),
    (r"Wird beim Ende ausgeführt", "runs at the end"),
    (r"Wird bei Zeitaktualisierung ausgeführt", "runs when the time updates"),
    (r"Wird bei Auswahl ausgeführt", "runs on selection"),
    (r"Wird beim Hover ausgeführt", "runs on hover"),
    (r"Wird beim Klick auf Bild ausgeführt", "runs when an image is clicked"),
    (r"Wird beim Klick auf Marker ausgeführt", "runs when a marker is clicked"),
    (r"Wird bei Änderung ausgeführt", "runs on change"),
    (r"Wird bei Zoom-Änderung ausgeführt", "runs when the zoom changes"),
    (r"Wird beim Ziehen beendet ausgeführt", "runs when dragging ends"),
    (r"Wird beim Kürzen ausgeführt", "runs when the path is shortened"),
    (r"Wird bei Navigation ausgeführt", "runs on navigation"),
    (r"Wird beim Laden des Bildes ausgeführt", "runs when the image has loaded"),
    (r"Wird bei Galerie-Wechsel ausgeführt", "runs when the gallery changes"),
    (r"Wird bei Slide-Wechsel ausgeführt", "runs when the slide changes"),
    (r"Wird beim Swipe ausgeführt", "runs on swipe"),
    (r"Wird beim Zoom ausgeführt", "runs on zoom"),
    (r"Wird beim Klick auf Home ausgeführt", "runs when home is clicked"),
    (r"Wird beim Öffnen ausgeführt", "runs when opened"),
    (r"Wird beim Schließen ausgeführt", "runs when closed"),
    (r"Wird bei Tastendruck ausgeführt", "runs on a key press"),
    (r"Event bei Auswahl", "event on selection"),
    (r"Event bei Änderung", "event on change"),
    (r"ARIA-Rolle: ", "ARIA role: "),
    (r"Responsives Layout\?", "responsive layout?"),
    (r"Animationen aktivieren\?", "enable animations?"),
    (r"Dauer in ms", "duration in ms"),
    (r"Intervall in ms", "interval in ms"),
    (r"Vorschaubilder anzeigen\?", "show preview images?"),
    (r"Steuerung anzeigen\?", "show controls?"),
    (r"Steuerungselemente anzeigen\?", "show controls?"),
    (r"Steuerungselemente", "control elements"),
    (r"Auto-Wiedergabe\?", "autoplay?"),
    (r"Auto-Play\?", "autoplay?"),
    (r"Wiederholen\?", "repeat?"),
    (r"Endlosschleife\?", "endless loop?"),
    (r"Vollbild erlauben\?", "allow fullscreen?"),
    (r"Untertitel anzeigen\?", "show subtitles?"),
    (r"Playlist anzeigen\?", "show the playlist?"),
    (r"Vor/Zurück-Buttons\?", "forward/back buttons?"),
    (r"Vor/Zurück-Navigation anzeigen\?", "show forward/back navigation?"),
    (r"Vorschaubilder\?", "preview images?"),
    (r"Icons anzeigen\?", "show icons?"),
    (r"Marker anzeigen\?", "show markers?"),
    (r"Verkehr anzeigen\?", "show traffic?"),
    (r"Filter anzeigen\?", "show the filter?"),
    (r"Loading-Zustand anzeigen\?", "show loading state?"),
    (r"Anzahl Spalten", "number of columns"),
    (r"Abstand zwischen Bildern", "spacing between images"),
    (r"Array von Bildern \(src, alt, title\)", "array of images (src, alt, title)"),
    (r"Array von Bildern", "array of images"),
    (r"Array von Markern", "array of markers"),
    (r"Bild-URL", "image URL"),
    (r"Video-URL", "video URL"),
    (r"Quell-URL", "source URL"),
    (r"Alt-Text", "alt text"),
    (r"Seitenverhältnis \(z\.B\. \"([^\"]+)\"\)", r"aspect ratio (e.g. \"\1\")"),
    (r"Übergang:", "transition:"),
    (r"Lautstärke \(0-1\)", "volume (0-1)"),
    (r"Live-Ankündigung", "live announcement"),
    (r"Suchanfrage", "search query"),
    (r"Filter nach Kategorie", "filter by category"),
    (r"API-Schlüssel \(Google Maps\)", "API key (Google Maps)"),
    (r"Mittelpunkt \{lat, lng\}", "centre point {lat, lng}"),
    (r"Zoom-Level", "zoom level"),
    (r"Standard-Wiedergabegeschwindigkeit", "default playback speed"),
    (r"Aktiver Nav-Punkt", "active nav item"),
    (r"Array von Nav-Objekten \(id, icon, label\)", "array of nav objects (id, icon, label)"),
    (r"Array von Breadcrumb-Objekten \(label, href, icon\)",
     "array of breadcrumb objects (label, href, icon)"),
    (r"Runde Buttons\?", "round buttons?"),
    (r"Runde Icons\?", "round icons?"),
    (r"Aktueller Index \(für Highlighting\)", "current index (for highlighting)"),
    (r"Eingeklappt bei wenig Platz\?", "collapsed when space is tight?"),
    (r"Kürzen bei wenig Platz\?", "shorten when space is tight?"),
    (r"Breakpoint für Kürzen", "breakpoint for shortening"),
    (r"Aktueller Pfad", "current path"),
    (r"Nicht aktuelle Pfade", "inactive paths"),
    (r"Hover-Zustand", "hover state"),
    (r"Aktiver Punkt", "active item"),
    (r"Inaktive Punkte", "inactive items"),
    (r"aktiver Punkt", "active item"),
    (r"Farbe ändert sich", "the colour changes"),
    (r"Unterstrich erscheint", "an underline appears"),
    (r"Deckkraft ändert sich", "the opacity changes"),
    (r"Bild vergrößert sich \(1\.1x\)", "the image grows (1.1x)"),
    (r"Bild vergrößert sich", "the image grows"),
    (r"Bild skaliert leicht", "the image scales slightly"),
    (r"Bild skaliert", "the image scales"),
    (r"Overlay mit Info/Icons", "overlay with information/icons"),
    (r"Overlay mit Info", "overlay with information"),
    (r"Rand leuchtet auf", "the border lights up"),
    (r"Schatten stärker", "stronger shadow"),
    (r"Controls erscheinen", "the controls appear"),
    (r"Zoom beim Scrollen", "zoom on scrolling"),
    (r"Mit Pfeil-Separator \(>\)", "with arrow separator (>)"),
    (r"Mit Pfeil \(→\)", "with arrow (→)"),
    (r"Mit Schrägstrich \(/\)", "with slash (/)"),
    (r"Mit spitzen Klammern \(›\)", "with angle brackets (›)"),
]

BASE_INHERIT = re.compile(r"^`visible`,.*→ \[Basiskomponente\]\(([^)]+)\)$")

# Mehrzeilige Standardblöcke (werden vor dem Zeilendurchlauf ersetzt)
BLOCKS = [
    (re.compile(
        r"Die Beispiele sind syntaxneutral gehalten\. Sobald die Umsetzung auf Rust und\n"
        r"\s*Blinc umgestellt wird, werden `usage\.md`-Beispiele in einem eigenen Durchlauf\n"
        r"\s*ersetzt\."),
     "The examples are kept syntax-neutral. As soon as the implementation moves to\n"
     "    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass."),
    (re.compile(r"Die Beispiele sind syntaxneutral gehalten\."),
     "The examples are kept syntax-neutral."),
]


def fix_table_row(line):
    cells = line.split("|")
    if len(cells) < 3:
        return line
    out = []
    for c in cells:
        s = c.strip()
        if s in CELLS:
            out.append(" " + CELLS[s] + " ")
        elif s.startswith("**") and s.strip("*") in CELLS:
            out.append(" **" + CELLS[s.strip("*")] + "** ")
        else:
            t = s
            for pat, rep in PHRASES:
                t = re.sub(pat, rep, t)
            out.append(" " + t + " " if t else c)
    return "|".join(out)


def fix_links(line):
    def rep(m):
        label, target = m.group(1), m.group(2)
        return "[%s](%s)" % (LINKS.get(label, label), target)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", rep, line)


def translate(text):
    for pat, rep in BLOCKS:
        text = pat.sub(rep, text)
    out = []
    fence = False
    for l in text.split("\n"):
        if l.strip().startswith("```"):
            fence = not fence
            out.append(l)
            continue
        if fence:
            out.append(l)
            continue
        m = re.match(r"^(#{1,4}) (.*)$", l)
        if m:
            level, title = m.group(1), m.group(2).strip()
            if level == "#":
                if title in TITLES:
                    title = TITLES[title]
                else:
                    # deutsche Klammerglosse abwerfen; (FAB)/(base) bleiben
                    title = re.sub(r"\s*\((?!FAB\b|base\b)[^)]*\)", "", title)
                    title = re.sub(r" - (Verwendung|Nutzung)$", " - Usage", title)
                    title = re.sub(r" - Aussehen$", " - Appearance", title)
            else:
                if title in HEADINGS:
                    title = HEADINGS[title]
                else:
                    m2 = re.match(r"^Beispiel (\d+): (.*)$", title)
                    if m2:
                        title = "Example %s: %s" % (m2.group(1), m2.group(2))
            out.append(f"{level} {title}")
            continue
        if l.startswith("|"):
            out.append(fix_table_row(l))
            continue
        if BASE_INHERIT.match(l):
            out.append(
                "`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,\n"
                "`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,\n"
                "`aria-label`, `aria-*` → [Base component]("
                + BASE_INHERIT.match(l).group(1) + ")")
            continue
        l = fix_links(l)
        for pat, rep in PHRASES:
            l = re.sub(pat, rep, l)
        out.append(l)
    return "\n".join(out)


DE_RE = re.compile(
    r"\b(der|die|das|den|dem|des|und|oder|mit|für|auf|von|zu|zur|zum|ist|sind|war|waren|ein|eine|einer|einem|einen|"
    r"nicht|auch|als|wenn|dann|diese|dieser|diesem|diesem|dessen|deren|man|es|"
    r"Beispiel|Beispiele|Nutzung|Verwendung|Eigenschaften|Parameter|Beschreibung|Hinweis|Hinweise|Wichtig|"
    r"Standard|Wert|Wert|Typ|Name|Funktion|Inhalt|Zweck|Grundlagen|Überblick|Optionen|Einstellung|"
    r"Einstellungen|Elemente|Komponente|Datei|Ordner|Anwendung|Beachten|Sie|Ihre|Ihren|Ihrem|kann|muss|"
    r"sollte|werden|hat|haben|kein|keine|aber|sondern|wird|nur|schon|hier|dort|wie|was|wann|warum|bitte|"
    r"Links|Rechts|Oben|Unten|Varianten|Siehe|zeigt|zeigen|über|unter|zwischen|innerhalb|außerhalb|immer|oft|"
    r"gilt|siehe|ausgeklappt|eingeklappt|aktiv|deaktiviert|beschriftet|genutzt|verwendet|angeboten|gehört|"
    r"bleibt|steht|liegen|liegt|hält|trägt|sich|mitführen|anbieten|setzen|halten|wählen|wechseln|wechselte)\b",
    re.IGNORECASE)


def leftovers(text):
    res, fence = [], False
    for l in text.split("\n"):
        if l.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        t = re.sub(r"`[^`]*`", "", l)
        t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
        if DE_RE.search(t):
            res.append(l)
    return res


def main(argv):
    report = argv and argv[0] == "--report"
    if report:
        argv = argv[1:]
    for f in argv:
        p = Path(f)
        if report:
            new = p.read_text(encoding="utf-8")
        else:
            new = translate(p.read_text(encoding="utf-8"))
            p.write_text(new, encoding="utf-8")
        left = leftovers(new)
        print(f"### {f} | {len(left)}")
        for i, l in enumerate(left):
            print(f"[{i}]<{l}>")


if __name__ == "__main__":
    main(sys.argv[1:])

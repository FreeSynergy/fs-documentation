#!/usr/bin/env python3
"""Erzeugt skins/index.md je App-Kategorie und aktualisiert den
Skin-Dokumentation-Abschnitt in <kategorie>/index.md.
Läuft idempotent; kann nach jeder Welle erneut ausgeführt werden."""
import os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "docs", "de", "apps")
CATS = ["calendar", "contact", "helpdesk", "crm", "projectmanagement",
        "whiteboards", "workflows", "erp", "maps", "marketing", "democracy",
        "marketplace"]

FILE_ORDER = ["index", "menu", "features", "description", "structure", "shortcuts", "api"]

def titles_from_index(skin_dir):
    """Programm-Titel aus der ersten Überschrift von index.md ziehen."""
    out = []
    for prog in sorted(os.listdir(skin_dir)):
        idx = os.path.join(skin_dir, prog, "index.md")
        if not os.path.isfile(idx):
            continue
        title = prog
        with open(idx, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"^#\s+(.+?)\s+Dokumentation\s*$", line.strip())
                if m:
                    title = m.group(1)
                    break
        out.append((prog, title))
    return out

def gen_skin_index(cat, entries):
    lines = [
        f"# {cat.capitalize()} Skin-Dokumentation",
        "",
        "## Übersicht",
        "",
        "Dieses Verzeichnis enthält die Dokumentation der Programme dieser Kategorie nach dem Wiki-Schema: "
        "Menüpunkte, Funktionen, Beschreibung, Struktur/UI-UX, Tastatur-Shortcuts und API — sieben Dateien pro Programm.",
        "",
        "Alle hier dokumentierten Programme sind **keine** FreeSynergy-Eigenentwicklungen, sondern fremde Programme, "
        "deren Oberfläche und Schnittstellen als Skin nachgebildet bzw. angebunden werden.",
        "",
        "## Enthaltene Dokumentationen",
        "",
    ]
    for prog, title in entries:
        lines.append(f"- [{title}](./{prog}/index.md)")
    lines += [
        "",
        "## Verzeichnisstruktur",
        "",
        "```",
        f"docs/de/apps/{cat}/skins/",
        "├── index.md              (diese Datei)",
    ]
    for i, (prog, _) in enumerate(entries):
        branch = "└──" if i == len(entries) - 1 else "├──"
        lines.append(f"{branch} {prog}/   (index, menu, features, description, structure, shortcuts, api)")
    lines += [
        "```",
        "",
        "## Inhalt jeder Dokumentation",
        "",
        "Jedes Programmverzeichnis enthält **sieben** Dateien:",
        "",
        "1. **index.md** – Übersicht des Programms und Links auf die sechs Detail-Dateien",
        "2. **menu.md** – alle Hauptmenüpunkte, Kontext-Menüs, rollenabhängige Menüs",
        "3. **features.md** – Hauptfunktionen, was das Programm kann und NICHT kann, Erweiterungen",
        "4. **description.md** – Beschreibung, Vorteile, Abgrenzung, technische Details, Zielgruppen",
        "5. **structure.md** – Fenster-/Seitenstruktur, UI/UX, Interaktionen, Responsive Design, Accessibility",
        "6. **shortcuts.md** – alle Tastatur-Shortcuts inklusive Mac-Varianten",
        "7. **api.md** – API-Art, Authentifizierung, Endpunkte, Beispiele, Rate Limits, Webhooks, SDKs",
        "",
        "## Hinweise",
        "",
        "- Alle Dokumentationen sind auf Deutsch verfasst",
        "- Die Inhalte sind für Anwender und Administratoren geeignet",
        "- **Tastatur-Shortcuts sind immer in der separaten Datei `shortcuts.md`**",
        "- **API-Dokumentation ist immer in der separaten Datei `api.md`**",
        "- Fehlende Funktionen sind ausdrücklich als nicht vorhanden markiert (❌)",
        "",
        "## Verwandte Bereiche",
        "",
        "- [Kategorie-Übersicht](../) – Überblick über diese Programmkategorie",
        "- [Wiki-Skins](../../wiki/skins/) – Referenzschema dieser Dokumentation",
        "- [Desktop-Skins](../../desktop/skins/) – gleiche Dateistruktur",
        "- [Standardisierte Daten](../../../data/) – Felder und Modelle für alle Skin-APIs",
        "",
    ]
    path = os.path.join(ROOT, cat, "skins", "index.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return path

def update_category_index(cat, entries):
    path = os.path.join(ROOT, cat, "index.md")
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    links = "\n".join(f"- [{t}](./skins/{p}/index.md) - {t}" for p, t in entries)
    block = (
        "## Skin-Dokumentation\n\n"
        "Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: "
        "`index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter "
        f"`apps/{cat}/skins/<programm>/`.\n\n"
        f"**dokumentiert ({len(entries)} Programme):**\n\n"
        f"{links}\n\n"
        "Übersicht: [Skin-Verzeichnis](./skins/index.md)\n\n"
        "Referenzschema: [Wiki-Skins](../wiki/skins/index.md) · [Desktop-Skins](../desktop/skins/index.md) · "
        "[Standardisierte Daten](../../data/api.md)"
    )
    pattern = re.compile(r"## Skin-Dokumentation.*?Referenzschema:.*?$", re.S | re.M)
    if pattern.search(text):
        text = pattern.sub(block, text, count=1)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path

def main():
    done, skipped = [], []
    for cat in CATS:
        skins = os.path.join(ROOT, cat, "skins")
        entries = titles_from_index(skins) if os.path.isdir(skins) else []
        if not entries:
            skipped.append(cat)
            continue
        gen_skin_index(cat, entries)
        update_category_index(cat, entries)
        done.append(f"{cat}: {len(entries)} Programme")
    print("Aktualisiert:\n  " + "\n  ".join(done))
    if skipped:
        print("Ohne Skins (übersprungen): " + ", ".join(skipped))

if __name__ == "__main__":
    main()

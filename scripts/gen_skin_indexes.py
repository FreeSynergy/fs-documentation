#!/usr/bin/env python3
"""Erzeugt skins/index.md je Programmkategorie und aktualisiert den
Skin-Dokumentation-Abschnitt in <kategorie>/index.md.

Seit dem programs-Umzug liegen die Kategorien dreistufig:
    docs/de/programs/<ebene>/<kategorie>/skins/<programm>/
ebene = apps | suites | platform. Der Pfadtext in den erzeugten Dateien folgt
dieser Struktur (frueher: docs/de/apps/<kategorie>/...).

Kategorien ohne skins/-Ordner werden uebersprungen, ebenso von Hand gepflegte
skins/index.md (erkennbar am fehlen der "Verwandte Bereiche"-Ueberschrift) —
die werden nicht ueberschrieben.

Laeuft idempotent; kann nach jeder Welle erneut ausgefuehrt werden.

Aufruf:
    python3 scripts/gen_skin_indexes.py
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "docs", "de", "programs")
LEVELS = ["apps", "suites", "platform"]

# Signatur dieses Skripts: nur Dateien mit dieser Einleitung werden ueberschrieben.
# wiki/, messenger/ und desktop/skins/index.md sind von Hand gepflegt und breiter —
# die bleiben unberuehrt.
GENERATOR_INTRO = ("Dieses Verzeichnis enthält die Dokumentation der Programme dieser "
                   "Kategorie nach dem Wiki-Schema")

def categories():
    """[(ebene, kategorie)] aus der Ordnerstruktur unter programs/."""
    out = []
    for level in LEVELS:
        base = os.path.join(ROOT, level)
        if not os.path.isdir(base):
            continue
        for cat in sorted(os.listdir(base)):
            if os.path.isfile(os.path.join(base, cat, "index.md")):
                out.append((level, cat))
    return out

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
                m = re.match(r"^#\s+(.+?)\s*$", line.strip())
                if not m:
                    continue
                # "Merkuro – Dokumentation" -> "Merkuro"; "Merkuro Calendar" bleibt stehen
                title = re.sub(r"\s+[–-]?\s*Dokumentation\s*$", "", m.group(1)).strip(" –-")
                break
        out.append((prog, title))
    return out

def rel(path, base):
    """Relativer Link: Ordner enden auf /, Dateien nicht."""
    link = os.path.relpath(path, base).replace(os.sep, "/")
    if not link.startswith("."):
        link = "./" + link
    if not os.path.isdir(path):
        return link
    return link if link.endswith("/") else link + "/"

def gen_skin_index(level, cat, entries):
    cat_dir = os.path.join(ROOT, level, cat)
    skin_dir = os.path.join(cat_dir, "skins")
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
        lines.append(f"- [{title}]({prog}/index.md)")
    lines += [
        "",
        "## Verzeichnisstruktur",
        "",
        "```",
        f"docs/de/programs/{level}/{cat}/skins/",
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
        f"- [Kategorie-Übersicht](../) – Überblick über diese Programmkategorie",
        f"- [Wiki-Skins]({rel(os.path.join(ROOT, 'apps', 'wiki', 'skins'), skin_dir)}) – Referenzschema dieser Dokumentation",
        f"- [Desktop-Skins]({rel(os.path.join(ROOT, 'platform', 'desktop', 'skins'), skin_dir)}) – gleiche Dateistruktur",
        f"- [Standardisierte Daten]({rel(os.path.join(ROOT, '..', 'data'), skin_dir)}) – Felder und Modelle für alle Skin-APIs",
        "",
    ]
    path = os.path.join(skin_dir, "index.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return path

def category_block_authored(text):
    """True, wenn der Skin-Abschnitt diesem Skript folgt (oder noch fehlt)."""
    if "## Skin-Dokumentation" not in text:
        return True
    return bool(re.search(r"## Skin-Dokumentation.*?Referenzschema:.*?$", text, re.S | re.M))


def update_category_index(level, cat, entries):
    cat_dir = os.path.join(ROOT, level, cat)
    path = os.path.join(cat_dir, "index.md")
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    links = "\n".join(f"- [{t}](skins/{p}/index.md) - {t}" for p, t in entries)
    block = (
        "## Skin-Dokumentation\n\n"
        "Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: "
        "`index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter "
        f"`programs/{level}/{cat}/skins/<programm>/`.\n\n"
        f"**dokumentiert ({len(entries)} Programme):**\n\n"
        f"{links}\n\n"
        "Übersicht: [Skin-Verzeichnis](skins/index.md)\n\n"
        f"Referenzschema: [Wiki-Skins]({rel(os.path.join(ROOT, 'apps', 'wiki', 'skins', 'index.md'), cat_dir)})"
        f" · [Desktop-Skins]({rel(os.path.join(ROOT, 'platform', 'desktop', 'skins', 'index.md'), cat_dir)})"
        f" · [Standardisierte Daten]({rel(os.path.join(ROOT, '..', 'data', 'api.md'), cat_dir)})"
    )
    pattern = re.compile(r"## Skin-Dokumentation.*?Referenzschema:.*?$", re.S | re.M)
    if pattern.search(text):
        text = pattern.sub(block, text, count=1)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path

def generator_authored(skin_index):
    """True, wenn skins/index.md diesem Skript gehoert (oder noch fehlt)."""
    if not os.path.isfile(skin_index):
        return True
    with open(skin_index, encoding="utf-8") as fh:
        return GENERATOR_INTRO in fh.read()

def main():
    done, skipped, protected = [], [], []
    for level, cat in categories():
        skins = os.path.join(ROOT, level, cat, "skins")
        if not os.path.isdir(skins):
            skipped.append(f"{level}/{cat}")
            continue
        if not generator_authored(os.path.join(skins, "index.md")):
            protected.append(f"{level}/{cat} (skins/index.md)")
            continue
        cat_index = os.path.join(ROOT, level, cat, "index.md")
        with open(cat_index, encoding="utf-8") as fh:
            if not category_block_authored(fh.read()):
                protected.append(f"{level}/{cat} (Skin-Abschnitt von Hand)")
                continue
        entries = titles_from_index(skins)
        if not entries:
            skipped.append(f"{level}/{cat}")
            continue
        gen_skin_index(level, cat, entries)
        update_category_index(level, cat, entries)
        done.append(f"{level}/{cat}: {len(entries)} Programme")
    print("Aktualisiert:\n  " + "\n  ".join(done))
    if protected:
        print("Von Hand gepflegt (nicht angefasst): " + ", ".join(protected))
    if skipped:
        print("Ohne Skins (übersprungen): " + ", ".join(skipped))

if __name__ == "__main__":
    sys.exit(main())

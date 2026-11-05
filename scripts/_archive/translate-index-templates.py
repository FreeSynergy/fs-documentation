#!/usr/bin/env python3
"""Translate the category-level masks/index.md template de -> en.

The tail of these files (from '## Inhalt jeder Dokumentation') is byte-identical
across the categories, verified with md5sum, so a fixed line map is safe. The
head (title + included-documentation list + directory tree) is per category and
is taken verbatim from the German source except for the translated sentences.
"""
import os
import sys

ROOT = "/srv/FreeSynergy/fs-documentation"
DE = os.path.join(ROOT, "docs/de")
EN = os.path.join(ROOT, "docs/en")

MAP = {
    "{c} Masken-Dokumentation": "{C} Mask Documentation",
    "## Übersicht": "## Overview",
    "Dieses Verzeichnis enthält die Dokumentation der Programme dieser Kategorie nach dem "
    "Wiki-Schema: Menüpunkte, Funktionen, Beschreibung, Struktur/UI-UX, Tastatur-Shortcuts "
    "und API — sieben Dateien pro Programm.":
        "This directory contains the documentation of the programs in this category following "
        "the wiki schema: menu items, features, description, structure/UI-UX, keyboard "
        "shortcuts and API — seven files per program.",
    "Alle hier dokumentierten Programme sind **keine** FreeSynergy-Eigenentwicklungen, sondern "
    "fremde Programme, deren Oberfläche und Schnittstellen als Maske nachgebildet bzw. "
    "angebunden werden.":
        "All programs documented here are **not** FreeSynergy in-house developments, but foreign "
        "programs whose surface and interfaces are recreated or connected as a mask.",
    "## Enthaltene Dokumentationen": "## Included documentation",
    "## Verzeichnisstruktur": "## Directory structure",
    "├── index.md              (diese Datei)": "├── index.md              (this file)",
    "## Inhalt jeder Dokumentation": "## Content of each documentation",
    "Jedes Programmverzeichnis enthält **sieben** Dateien:":
        "Each program directory contains **seven** files:",
    "1. **index.md** – Übersicht des Programms und Links auf die sechs Detail-Dateien":
        "1. **index.md** – overview of the program and links to the six detail files",
    "2. **menu.md** – alle Hauptmenüpunkte, Kontext-Menüs, rollenabhängige Menüs":
        "2. **menu.md** – all main menu items, context menus, role-dependent menus",
    "3. **features.md** – Hauptfunktionen, was das Programm kann und NICHT kann, Erweiterungen":
        "3. **features.md** – main features, what the program can and CANNOT do, extensions",
    "4. **description.md** – Beschreibung, Vorteile, Abgrenzung, technische Details, Zielgruppen":
        "4. **description.md** – description, advantages, differentiation, technical details, "
        "target groups",
    "5. **structure.md** – Fenster-/Seitenstruktur, UI/UX, Interaktionen, Responsive Design, "
    "Accessibility":
        "5. **structure.md** – window/page structure, UI/UX, interactions, responsive design, "
        "accessibility",
    "6. **shortcuts.md** – alle Tastatur-Shortcuts inklusive Mac-Varianten":
        "6. **shortcuts.md** – all keyboard shortcuts including Mac variants",
    "7. **api.md** – API-Art, Authentifizierung, Endpunkte, Beispiele, Rate Limits, Webhooks, "
    "SDKs":
        "7. **api.md** – API type, authentication, endpoints, examples, rate limits, webhooks, "
        "SDKs",
    "## Hinweise": "## Notes",
    "- Alle Dokumentationen sind auf Deutsch verfasst":
        "- All documentation is written in German",
    "- Die Inhalte sind für Anwender und Administratoren geeignet":
        "- The content is suitable for users and administrators",
    "- **Tastatur-Shortcuts sind immer in der separaten Datei `shortcuts.md`**":
        "- **Keyboard shortcuts are always in the separate file `shortcuts.md`**",
    "- **API-Dokumentation ist immer in der separaten Datei `api.md`**":
        "- **API documentation is always in the separate file `api.md`**",
    "- Fehlende Funktionen sind ausdrücklich als nicht vorhanden markiert (❌)":
        "- Missing features are explicitly marked as not present (❌)",
    "## Verwandte Bereiche": "## Related areas",
    "- [Kategorie-Übersicht](../) – Überblick über diese Programmkategorie":
        "- [Category overview](../) – overview of this program category",
    "- [Wiki-Masken](../../wiki/masks/) – Referenzschema dieser Dokumentation":
        "- [Wiki masks](../../wiki/masks/) – reference schema for this documentation",
    "- [Desktop-Masken](../../../platform/desktop/masks/) – gleiche Dateistruktur":
        "- [Desktop masks](../../../platform/desktop/masks/) – same file structure",
    "- [Standardisierte Daten](../../../../data/) – Felder und Modelle für alle Masken-APIs":
        "- [Standardised data](../../../../data/) – fields and models for all mask APIs",
}

CATEGORIES = {
    "marketing": "Marketing",
    "projectmanagement": "Projectmanagement",
    "streaming": "Streaming",
    "whiteboards": "Whiteboards",
}


def translate(cat, de_text):
    out = []
    unmapped = []
    for line in de_text.split("\n"):
        s = line.rstrip()
        if s in MAP:
            out.append(MAP[s].format(c=cat, C=CATEGORIES[cat]))
        elif s.startswith("# ") and s.endswith(" Masken-Dokumentation"):
            out.append("# " + CATEGORIES[cat] + " Mask Documentation")
        elif s.startswith(("docs/de/", "- [", "├──", "└──", "│")) or s == "" or s.startswith("```"):
            out.append(line)  # paths, links and trees are kept verbatim
        else:
            unmapped.append(s)
            out.append(line)
    return "\n".join(out), unmapped


def main():
    for cat, cap in CATEGORIES.items():
        rel = f"programs/apps/{cat}/masks/index.md"
        de_path = os.path.join(DE, rel)
        en_path = os.path.join(EN, rel)
        with open(de_path, encoding="utf-8") as fh:
            de_text = fh.read()
        en_text, unmapped = translate(cat, de_text)
        os.makedirs(os.path.dirname(en_path), exist_ok=True)
        with open(en_path, "w", encoding="utf-8") as fh:
            fh.write(en_text)
        print(f"{cat}: {len(de_text.splitlines())} -> {len(en_text.splitlines())} lines, "
              f"unmapped={unmapped}")


if __name__ == "__main__":
    main()

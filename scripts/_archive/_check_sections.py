#!/usr/bin/env python3
"""Einmalige Pruefung: Pflichtabschnitte je App-Datei (de) + Konsistenz der Index-Tabellen."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs" / "de" / "apps"

REQUIRED_SECTIONS = {
    "description.md": ["Übersicht", "Vorteile", "Für wen"],
    "features.md": ["Übersicht", "Funktionen"],
    "menu.md": ["Übersicht", "Menü"],
    "structure.md": ["Übersicht", "Struktur"],
    "shortcuts.md": ["Übersicht", "Shortcut"],
    "api.md": ["Übersicht", "Authentifizierung"],
}

problems = 0
for skin_dir in sorted(ROOT.glob("*/skins/*")):
    if not skin_dir.is_dir():
        continue
    rel = skin_dir.relative_to(ROOT)
    for fname, sections in REQUIRED_SECTIONS.items():
        p = skin_dir / fname
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        heads = [h.strip().lower() for h in re.findall(r"^## (.+)$", text, re.M)]
        for sec in sections:
            if not any(sec.lower() in h for h in heads):
                print(f"{rel}/{fname}: Abschnitt fehlt: '{sec}'")
                problems += 1
        # Steckbrief-Tabelle in description.md?
        if fname == "description.md":
            first_h2 = text.find("\n## ")
            head_part = text[:first_h2] if first_h2 != -1 else text
            if "|" not in head_part:
                print(f"{rel}/description.md: keine Steckbrief-Tabelle")
                problems += 1
    # index.md verlinkt die 6 Dateien?
    idx = skin_dir / "index.md"
    if idx.is_file():
        text = idx.read_text(encoding="utf-8")
        for f in ["description", "features", "menu", "structure", "shortcuts", "api"]:
            if f not in text:
                print(f"{rel}/index.md: Link auf {f} fehlt")
                problems += 1

# skins/index.md listen alle Skin-Ordner?
for cat_index in sorted(ROOT.glob("*/skins/index.md")):
    cat = cat_index.parts[-3]
    text = cat_index.read_text(encoding="utf-8")
    for skin_dir in sorted(ROOT.glob(f"*/skins/*/")):
        if skin_dir.parts[-3] != cat:
            continue
        if skin_dir.name not in text:
            print(f"{cat}/skins/index.md: Skin '{skin_dir.name}' nicht aufgelistet")
            problems += 1

print(f"\nProbleme: {problems}")
sys.exit(0)

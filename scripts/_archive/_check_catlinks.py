#!/usr/bin/env python3
"""Soll pruefen, ob jede Kategorie-Indexseite alle Skin-Ordner verlinkt."""
from pathlib import Path

root = Path("docs/de/apps")
for cat in sorted(p for p in root.iterdir() if p.is_dir()):
    idx = cat / "index.md"
    if not idx.is_file():
        print(f"{cat.name}: KEIN index.md")
        continue
    text = idx.read_text(encoding="utf-8")
    skins = sorted(p.name for p in (cat / "skins").iterdir() if p.is_dir())
    missing = [s for s in skins if f"skins/{s}/" not in text]
    print(f"{cat.name}: {len(skins)} skins, nicht verlinkt: {missing}")

#!/usr/bin/env python3
"""One-off analysis: find incomplete app skin documentation."""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
REQUIRED = ["index.md", "description.md", "features.md", "structure.md", "menu.md", "shortcuts.md", "api.md"]

def scan(lang):
    apps_dir = os.path.join(ROOT, lang, "apps")
    if not os.path.isdir(apps_dir):
        print(f"NO apps dir for {lang}")
        return
    for app in sorted(os.listdir(apps_dir)):
        skins = os.path.join(apps_dir, app, "skins")
        if not os.path.isdir(skins):
            print(f"{lang}/{app}: NO skins dir")
            continue
        for skin in sorted(os.listdir(skins)):
            d = os.path.join(skins, skin)
            if not os.path.isdir(d):
                continue
            missing = [f for f in REQUIRED if not os.path.isfile(os.path.join(d, f))]
            tiny = []
            for f in REQUIRED:
                p = os.path.join(d, f)
                if os.path.isfile(p):
                    size = os.path.getsize(p)
                    if size < 200:
                        tiny.append((f, size))
            if missing or tiny:
                print(f"{lang}/{app}/{skin}: missing={missing} tiny={tiny}")

for lang in ["de", "en"]:
    print(f"===== {lang} =====")
    scan(lang)

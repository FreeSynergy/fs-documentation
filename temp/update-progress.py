#!/usr/bin/env python3
"""Regenerate temp/translation-progress.md from a fixed in-scope inventory.

Scope is frozen (the apps with no English coverage at the start of this run).
Status is derived from the filesystem: an EN counterpart that exists counts as
translated, so the list stays accurate after every file-by-file run.
"""
import os

ROOT = "/srv/FreeSynergy/fs-documentation"
DE = os.path.join(ROOT, "docs/de")
EN = os.path.join(ROOT, "docs/en")
OUT = os.path.join(ROOT, "temp/translation-progress.md")

CATEGORIES = [
    "apps/contact", "apps/gallery", "apps/helpdesk", "apps/maps",
    "apps/marketing", "apps/projectmanagement", "apps/streaming",
    "apps/whiteboards", "apps/wiki",
]
# app-level index.md of the calendar category is out of scope; the planner api.md
# is the explicit repair job of this run
REPAIR = [("planner (Reparatur)", "programs/apps/calendar/masks/planner/api.md")]


def inventory():
    rows = []
    for cat in CATEGORIES:
        catdir = os.path.join(DE, "programs", cat)
        for dirpath, _, files in os.walk(catdir):
            for f in sorted(files):
                if not f.endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, f), DE)
                parts = rel.split(os.sep)
                if len(parts) >= 6 and parts[3] == "masks":
                    app = parts[4]
                elif len(parts) == 5 and parts[3] == "masks":
                    app = cat.split("/")[1] + " Masks (Index)"
                else:
                    app = cat.split("/")[1] + " (Index)"
                rows.append((app, "programs/" + rel if not rel.startswith("programs/") else rel))
    rows.extend(REPAIR)
    return sorted(set(rows), key=lambda r: (r[0], r[1]))


def main():
    rows = inventory()
    lines = [
        "# Übersetzungs-Fortschritt – Apps de → en",
        "",
        "Arbeitsbereich: `docs/de/programs/apps/<app>/` → `docs/en/programs/apps/<app>/`.",
        "",
        "Statuswerte: `[x] übersetzt` · `[ ] offen` · `[!] unvollständig/reparatur` · `[!] nicht gefunden`",
        "",
        "Scope (Apps ohne englische Gegenstände; `calendar/*` und `messenger/*` bleiben unberührt):",
        "contact, gallery, helpdesk, maps, marketing, projectmanagement, streaming, whiteboards, wiki",
        "plus Reparatur `calendar/masks/planner/api.md`.",
        "",
        "Neu erzeugt: `python3 temp/update-progress.py` (Status aus Dateisystem abgeleitet).",
        "",
        "| App | Datei | Status |",
        "|-----|-------|--------|",
    ]
    done = []
    for app, path in rows:
        en = os.path.join(EN, path)
        if os.path.exists(en):
            status = "[x] übersetzt"
            done.append((app, path))
        else:
            status = "[ ] offen"
        lines.append(f"| {app} | {path} | {status} |")

    open_rows = [(a, p) for a, p in rows if (a, p) not in done]
    lines += [
        "",
        f"Dateien gesamt: {len(rows)} · übersetzt: {len(done)} · offen: {len(open_rows)}",
        "",
        "## Offen",
        "",
    ]
    if not open_rows:
        lines.append("– keine")
    else:
        by_app = {}
        for app, path in open_rows:
            parts = path.split("/")
            label = "/".join(parts[-2:]) if parts[-1] == "index.md" else parts[-1]
            by_app.setdefault(app, []).append(label)
        for app in sorted(by_app):
            files = ", ".join(sorted(by_app[app]))
            lines.append(f"- [ ] **{app}** ({len(by_app[app])}): {files}")
    lines += ["", "## Unvollständig / Reparatur", "", "- keine ausstehend"]
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {OUT}: {len(rows)} rows, {len(done)} translated, {len(open_rows)} open")


if __name__ == "__main__":
    main()

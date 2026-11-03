#!/usr/bin/env python3
"""Einmal-Aktion: temp/apps-plan.md um Legende, Markierungs-Bedeutung und eine
Zeile 'Pflichtmenge einfrieren' je Kategorie ergaenzen (ADR 0006)."""
from pathlib import Path

PLAN = Path(__file__).resolve().parents[1] / "temp" / "apps-plan.md"

LEVEL = {
    "calendar": "apps", "contact": "apps", "gallery": "apps", "helpdesk": "apps",
    "maps": "apps", "marketing": "apps", "messenger": "apps",
    "projectmanagement": "apps", "streaming": "apps", "whiteboards": "apps",
    "wiki": "apps",
    "crm": "suites", "democracy": "suites", "erp": "suites",
    "marketplace": "suites", "workflows": "suites",
    "desktop": "platform", "crates": "platform",
}

HEAD_OLD = """Checkliste aller Dateien unter `docs/de/apps/` (Pfade relativ zu `docs/de/`).
Eine Datei nach der Fertigstellung mit `[x]` markieren.

**Übersicht:** 17 Kategorien · 119 Programme (Skins) · 869 Markdown-Dateien
"""

HEAD_NEW = """Checkliste aller Dateien unter `docs/de/programs/` (Pfade relativ zu `docs/de/`).

**Bedeutung der Markierung** (festgelegt 2026-11-03, `conventions/decisions/0006`):

| Zeichen | Heißt |
|---------|-------|
| `[x]` | **an Primärquellen verifiziert** — Quelltext-Tag, offizielle API-Referenz oder offizielle Hilfeseite; Fundstellen in `index.md` der Skin |
| `[~]` | Datei **vorhanden**, Inhalt **nicht** an Primärquellen verifiziert — kann veraltet oder mit einem anderen Produkt vermischt sein |
| `[ ]` | Datei fehlt |

Der Haken ist kein Zähler für geschriebene Dateien, sondern der Nachweis, dass nachgeprüft
wurde. `[~]` ist Restarbeit — aber geringere als `[ ]`.

**Abbruchkriterium pro Kategorie** (ADR 0006): **3–5 Masken** der Kategorie vollständig
verifizieren, dann die Schnittmenge dieser Masken als **Pflichtmenge** in
`programs/<ebene>/<kategorie>/requirements.md` **einfrieren** und die Zeile
„Pflichtmenge eingefroren“ abhaken. Die übrigen Masken der Kategorie sind **Stichprobe**:
nur abarbeiten, wenn sie eine Fähigkeit zeigen, die in `requirements.md` fehlt.
Die Dateien sind das Mittel, nicht das Ziel.

**Übersicht:** 17 Kategorien · 119 Programme (Skins) · 869 Markdown-Dateien —
davon `[x]` verifiziert 42, `[~]` vorhanden ohne Beleg 827, `[ ]` fehlt 0
"""


def freeze_line(cat: str) -> str:
    level = LEVEL[cat]
    done = "x" if cat == "calendar" else " "
    return ("- [ ] Pflichtmenge einfrieren → `programs/%s/%s/requirements.md`\n"
            % (level, cat)).replace("- [ ]", "- [%s]" % done, 1)


text = PLAN.read_text(encoding="utf-8")
assert HEAD_OLD in text, "Kopfabschnitt nicht gefunden"
text = text.replace(HEAD_OLD, HEAD_NEW, 1)

out, cats = [], []
for line in text.splitlines(keepends=True):
    if line.startswith("## ") and line[3:].strip() in LEVEL:
        cat = line[3:].strip()
        cats.append(cat)
        out.append(line)
        out.append("\n" + freeze_line(cat))
        continue
    out.append(line)

PLAN.write_text("".join(out), encoding="utf-8")
print("freeze-Zeilen eingefuegt:", len(cats))
print(", ".join(cats))

#!/usr/bin/env python3
"""Einmal-Migration: temp/apps-plan.md auf programs/-Pfade ziehen, Bestand markieren.

Marker-Bedeutung (nach P1, 2026-11-03):
  [x] = an Primärquellen verifiziert
  [~] = Datei vorhanden, Inhalt nicht an Primärquellen verifiziert
  [ ] = Datei fehlt
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "temp" / "apps-plan.md"
DOCS = ROOT / "docs" / "de" / "programs"

# Kategorie -> Ebene (ADR 0001)
LEVEL = {
    "calendar": "apps", "contact": "apps", "gallery": "apps", "helpdesk": "apps",
    "maps": "apps", "marketing": "apps", "messenger": "apps",
    "projectmanagement": "apps", "streaming": "apps", "whiteboards": "apps",
    "wiki": "apps",
    "crm": "suites", "democracy": "suites", "erp": "suites",
    "marketplace": "suites", "workflows": "suites",
    "desktop": "platform", "crates": "platform",
}

# Gruppe 4 = Pfad NACH der Vorsilbe apps/
LINE = re.compile(r"^(\- \[)([ x~])(\] )apps/(\S+)$")

def target(rest: str) -> str:
    """<kategorie>/... -> <ebene>/<kategorie>/... ; index.md -> index.md"""
    if "/" not in rest:  # apps/index.md -> programs/index.md
        return rest
    cat = rest.split("/", 1)[0]
    level = LEVEL.get(cat)
    if level is None:
        return None
    return f"{level}/{rest}"


def main() -> int:
    lines = PLAN.read_text(encoding="utf-8").splitlines()
    out, stats = [], {"x": 0, "tilde": 0, "empty": 0, "unmapped": []}
    seen_targets = set()

    for line in lines:
        m = LINE.match(line)
        if not m:
            out.append(line)
            continue
        pre, mark, post, plan_rel = m.groups()
        tgt = target(plan_rel)
        if tgt is None:
            stats["unmapped"].append(plan_rel)
            out.append(line)
            continue
        seen_targets.add(tgt)
        exists = (DOCS / tgt).is_file()
        if mark == "x":
            new = "x"
        elif exists:
            new = "~"
        else:
            new = " "
        stats[{"x": "x", "~": "tilde", " ": "empty"}[new]] += 1
        out.append(f"{pre}{new}{post}programs/{tgt}")

    PLAN.write_text("\n".join(out) + "\n", encoding="utf-8")

    # Dateien auf der Platte, die im Plan fehlen
    on_disk = {
        str(p.relative_to(DOCS))
        for p in DOCS.rglob("*.md")
    }
    missing_in_plan = sorted(on_disk - seen_targets)
    print("markiert: verifiziert=%s vorhanden-unverifiziert=%s fehlt=%s"
          % (stats["x"], stats["tilde"], stats["empty"]))
    print("nicht zuordenbar:", stats["unmapped"] or "keine")
    print("auf Platte, aber nicht im Plan (%d):" % len(missing_in_plan))
    for p in missing_in_plan:
        print("  ", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())

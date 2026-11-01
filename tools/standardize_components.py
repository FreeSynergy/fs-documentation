#!/usr/bin/env python3
"""Standardisiert docs/de/components/ nach dem Konzept (Abschnitt 7 + Beschlüsse):

1. `examples.md` in `usage.md` überführen (Beschluss 2).
2. Aus `attributes.md` die generischen, von `basics/base.md` geerbten Attribute
   entfernen und einen Abschnitt „Geerbt von“ anhängen (Beschluss 4).

Sicherheit:
- Ohne `--apply` läuft der Dry-Run (berichtet nur, ändert nichts).
- `role`, `label`, `id`, `onChange` u. ä. bleiben stehen (komponentenspezifische Werte).
- `size`/`theme`/`variant` werden nur entfernt, wenn sie den Basis-Standardwerten
  entsprechen bzw. die Varianten bereits in `description.md` dokumentiert sind.
- Komponenten, die den neuen Standard bereits haben („Geerbt von“ vorhanden), werden übersprungen.

Aufruf:
    python3 tools/standardize_components.py            # Dry-Run
    python3 tools/standardize_components.py --apply    # Änderungen schreiben
"""
import argparse
import sys
from pathlib import Path

COMPONENTS = Path(__file__).resolve().parent.parent / "docs" / "de" / "components"

# Attribute, die immer von base geerbt werden und keine komponentenspezifischen Werte tragen
INHERITED = {
    "visible", "enabled", "disabled", "rounded", "theme",
    "tabIndex", "animation", "gesture",
    "onClick", "onFocus", "onBlur", "aria-label",
}

GEERBT_SECTION = """
## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
"""


def attr_of_row(line):
    """Extrahiert den Attributnamen aus einer Markdown-Tabellenzeile der Form | `name` | ..."""
    line = line.strip()
    if not line.startswith("|"):
        return None
    first = line.strip("|").split("|")[0].strip()
    if first.startswith("`") and first.endswith("`") and len(first) > 2:
        return first[1:-1]
    return None


def removable(attr, row, description_has_variants):
    if attr in INHERITED:
        return True
    if attr == "size":
        return all(w in row for w in ("small", "medium", "large"))
    if attr == "theme":
        return all(w in row for w in ("default", "dark"))
    if attr == "variant":
        return description_has_variants
    return False


def clean_attributes(text, description_has_variants):
    """Entfernt geerbte Zeilen; leere Tabellen und Abschnitte werden getilgt."""
    lines = text.splitlines()
    # Abschnitte (## ...) mit ihrem Inhalt zerlegen
    sections = []  # (heading_or_None, [lines])
    current_head, current_body = None, []
    preamble = []
    for line in lines:
        if line.startswith("## "):
            if current_head is not None:
                sections.append((current_head, current_body))
            elif current_body:
                preamble = current_body
            current_head, current_body = line, []
        else:
            current_body.append(line)
    if current_head is not None:
        sections.append((current_head, current_body))
    elif preamble is not None:
        preamble = current_body

    removed = []
    out = []
    if preamble:
        out.extend(preamble)
    for head, body in sections:
        kept = []
        for line in body:
            attr = attr_of_row(line)
            if attr and removable(attr, line, description_has_variants):
                removed.append(attr)
                continue
            kept.append(line)
        data_rows = [l for l in kept if attr_of_row(l) is not None]
        if not data_rows:
            has_text = any(l.strip() and not l.strip().startswith("|") for l in kept)
            if not has_text:
                # Abschnitt war nur eine Tabelle -> komplett entfernen
                continue
            # Prosa bleibt, aber leere Tabellenreste (Kopf/Trennzeile) entfernen
            kept = [l for l in kept if not l.strip().startswith("|")]
        out.append(head)
        out.extend(kept)
    text2 = "\n".join(out).rstrip() + "\n"
    return text2, removed


def merge_examples(comp, apply_):
    usage = comp / "usage.md"
    examples = comp / "examples.md"
    if not examples.is_file():
        return False
    ex = examples.read_text(encoding="utf-8")
    lines = ex.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:]
        if title.endswith(" - Beispiele"):
            title = title[: -len(" - Beispiele")] + " - Verwendung"
        body = "\n".join(lines[1:]).strip()
        if usage.is_file():
            usg = usage.read_text(encoding="utf-8").rstrip()
            merged = usg + "\n\n## Beispiele\n\n" + body + "\n"
        else:
            merged = "# " + title + "\n\n" + body + "\n"
    else:
        if usage.is_file():
            merged = usage.read_text(encoding="utf-8").rstrip() + "\n\n" + ex
        else:
            merged = ex
    if apply_:
        usage.write_text(merged, encoding="utf-8")
        examples.unlink()
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Dateien tatsächlich ändern")
    args = parser.parse_args()

    merged = attrs_changed = skipped_new = 0
    removed_total = 0
    for comp in sorted(COMPONENTS.glob("*/*/")):
        if not (comp / "description.md").is_file():
            continue
        if merge_examples(comp, args.apply):
            merged += 1
        attrs = comp / "attributes.md"
        if not attrs.is_file():
            continue
        text = attrs.read_text(encoding="utf-8")
        if "Geerbt von" in text:
            skipped_new += 1
            continue
        desc = comp / "description.md"
        has_variants = "## Varianten" in desc.read_text(encoding="utf-8")
        new_text, removed = clean_attributes(text, has_variants)
        if removed:
            removed_total += len(removed)
            attrs_changed += 1
            if args.apply:
                attrs.write_text(new_text.rstrip() + "\n" + GEERBT_SECTION, encoding="utf-8")

    mode = "ANGEWENDET" if args.apply else "DRY-RUN (nichts geändert)"
    print(f"{mode}")
    print(f"  examples.md -> usage.md zusammengefuehrt : {merged}")
    print(f"  attributes.md mit entfernten Zeilen      : {attrs_changed}")
    print(f"  entfernte Tabellenzeilen gesamt          : {removed_total}")
    print(f"  Komponenten im neuen Standard (ueberspr.) : {skipped_new}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

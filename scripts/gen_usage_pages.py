#!/usr/bin/env python3
"""Erzeugt fehlende `usage.md` (Pflichtdatei aus Konzept Abschnitt 7).

Der Inhalt wird aus den vorhandenen Dateien der Komponente abgeleitet:
Anwendung aus Beschreibung und Verwendungszweck, Beispiele aus den echten Attributnamen
von `attributes.md`, Hinweise aus dem Steckbrief. erfunden wird nichts.

Die Beispiele bleiben syntaxneutral; sie werden ersetzt, sobald die Umsetzung auf
Rust (voraussichtlich Blinc) umgestellt wird (Beschluss 2).

Aufruf:
    python3 tools/gen_usage_pages.py            # Dry-Run
    python3 tools/gen_usage_pages.py --apply    # schreiben
"""
import argparse
import re
import sys
from pathlib import Path

COMPONENTS = Path(__file__).resolve().parent.parent / "docs" / "de" / "components"
CELL_SPLIT = re.compile(r"(?<!\\)\|")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")

NOTE = ['!!! note',
        '    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und',
        '    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf',
        '    ersetzt.']


def cells_of(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in CELL_SPLIT.split(s)]


def sections(text):
    out, head, body = {}, None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if head:
                out.setdefault(head.lower(), []).extend(body)
            head, body = line[3:].strip(), []
        elif head is not None:
            body.append(line)
    if head:
        out.setdefault(head.lower(), []).extend(body)
    return out


def title_of(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def first_sentence(text):
    para = []
    for line in sections(text).get("beschreibung", []):
        if line.strip():
            para.append(line.strip())
    joined = " ".join(para)
    m = re.match(r"^(.*?[.!?])", joined)
    return m.group(1) if m else joined


def attr_rows(attributes_text, wanted):
    """[(name, typ, default, beschreibung)] aus den Standard-Abschnitten."""
    rows = []
    for head in ("hauptattribute", "verhalten", "darstellung"):
        for line in sections(attributes_text).get(head, []):
            s = line.strip()
            if not s.startswith("|") or SEP_RE.match(s):
                continue
            cells = cells_of(s)
            if len(cells) < 3 or not cells[0].startswith("`"):
                continue
            name = cells[0].strip("`")
            if name in ("id", "label", "size", "theme", "variant", "role"):
                continue
            rows.append((name, cells[1], cells[2] if len(cells) > 3 else "-", " ".join(cells[3:]), head))
    rows = [r for r in rows if r[4] in wanted]
    return rows


TEXT_WERT = {
    "title": "Titel", "subtitle": "Untertitel", "text": "Text", "content": "Inhalt",
    "message": "Nachricht", "description": "Beschreibung", "name": "Name",
    "value": "Wert", "placeholder": "Platzhalter", "alt": "Bildbeschreibung",
    "src": "/beispiel/pfad", "url": "https://example.org", "href": "/ansicht",
    "icon": "icon-name", "query": "suchbegriff", "color": "#4f46e5",
}


def prop_for(name, typ, default, desc):
    """Ein Beispiel-Attribut als JSX-Ausdruck, abgeleitet aus Typ und Vorgabewert."""
    default = default.strip().strip("`")
    t = typ.lower()
    enum = re.findall(r"`([a-z0-9-]+)`", desc)
    if "boolean" in t:
        value = default if default in ("true", "false") else "true"
        return f"{name}={{{value}}}"
    if "number" in t:
        return f"{name}={{{default}}}" if re.fullmatch(r"-?\d+(\.\d+)?", default) else None
    if "function" in t:
        return f"{name}={{aktion}}"
    if t.startswith("enum"):
        first = default if default not in ("-", "", "null") else (enum[0] if enum else "standard")
        return f'{name}="{first}"'
    if "array" in t:
        return f"{name}={{eintraege}}"
    if "object" in t:
        return f"{name}={{einstellungen}}"
    if default not in ("-", "", "null"):
        return f'{name}="{default}"'
    key = name.lower()
    for suffix, wert in sorted(TEXT_WERT.items(), key=lambda kv: -len(kv[0])):
        if key == suffix or key.endswith(suffix):
            return f'{name}="{wert}"'
    return f'{name}="{name}"'


def pascal(name):
    return "".join(p.capitalize() for p in name.split("-"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="von diesem Skript erzeugte usage.md neu schreiben")
    args = ap.parse_args()

    made = 0
    for comp in sorted(d for d in COMPONENTS.glob("*/*") if d.is_dir()):
        usage = comp / "usage.md"
        desc = comp / "description.md"
        generated = usage.is_file() and "## Anwendung" in usage.read_text(encoding="utf-8")
        if (usage.exists() and not (args.force and generated)) or not desc.is_file():
            continue
        dtext = desc.read_text(encoding="utf-8")
        atext = (comp / "attributes.md").read_text(encoding="utf-8") if (comp / "attributes.md").is_file() else ""
        title = title_of(dtext)
        dsec = sections(dtext)
        purpose = [l.lstrip("- ").strip() for l in dsec.get("verwendungszweck", []) if l.strip().startswith("-")]
        rows = attr_rows(atext, ("hauptattribute",)) or attr_rows(atext, ("verhalten", "darstellung"))
        extra = attr_rows(atext, ("verhalten", "darstellung"))

        fields = {}
        for line in dtext.splitlines():
            s = line.strip()
            if s.startswith("## "):
                break
            if s.startswith("|") and not SEP_RE.match(s):
                c = cells_of(s)
                if len(c) >= 2:
                    fields[c[0].strip("*").strip()] = c[1]

        out = [f"# {title} - Verwendung", ""] + NOTE + ["", "## Anwendung", "",
                first_sentence(dtext), ""]
        for p in purpose[:6]:
            out.append(f"- {p}")
        out.append("")

        comp_name = pascal(comp.name)
        out += ["## Beispiele", ""]
        base = [prop_for(*row[:4]) for row in rows]
        base = [p for p in base if p][:3]
        more = [prop_for(*row[:4]) for row in extra if prop_for(*row[:4])]
        for i in range(min(3, max(1, len(purpose)))):
            label = (purpose[i][:1].upper() + purpose[i][1:]) if i < len(purpose) else "Standardfall"
            props = list(base)
            if i > 0 and more:
                props = props[: max(1, len(props) - 1)] + [more[(i - 1) % len(more)]]
            out += [f"### {label}", "", "```jsx",
                    f"<{comp_name}" + ("".join(" " + p for p in props)) + " />",
                    "```", ""]

        hints = []
        if fields.get("Zustände", "-") != "-":
            hints.append(f"- Zustände: {fields['Zustände']} (zusätzlich zu den Zuständen aus `base`)")
        if fields.get("Rolle", "-") != "-":
            hints.append(f"- Barrierefreiheit: Rolle {fields['Rolle']}; Bedienelemente zusätzlich mit `label` oder `aria-label` benennen")
        if fields.get("Gesten", "-") != "-":
            hints.append(f"- Gesten: {fields['Gesten']}")
        if fields.get("Animationen", "-") != "-":
            hints.append(f"- Übergänge: {fields['Animationen']}")
        related = re.findall(r"`([a-z0-9-]+)`", fields.get("Verwandt", ""))
        if related:
            links = ", ".join(f"[{r}](../../{cat}/{r}/)"
                              for r in related[:4]
                              for cat in [next((c.parent.name for c in COMPONENTS.glob(f"*/{r}")), None)] if cat)
            if links:
                hints.append(f"- Siehe auch: {links}")
        if hints:
            out += ["## Hinweise", ""] + hints

        content = "\n".join(out).rstrip() + "\n"
        made += 1
        print(f"  usage.md: {comp.parent.name}/{comp.name}")
        if args.apply:
            usage.write_text(content, encoding="utf-8")

    print(f"\n{'ANGEWENDET' if args.apply else 'DRY-RUN'}: usage.md erzeugt {made}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Umsortierung des Komponentenbestands in die 10 Zielkategorien (Konzept Abschnitt 6)
inklusive der Merge-Vorschlaege aus Abschnitt 4.

Beschluss 1: alte Ordnernamen werden ersatzlos gestrichen, es gibt keine
Weiterleitungs-Seiten. Bestehende Querverweise werden deshalb im selben Schritt
auf die neuen Pfade (bzw. auf das Merge-Ziel) umgeschrieben.

Ablauf:
1. MOVES  - Komponentenordner in die Zielkategorie verschieben (auch umbenennen).
2. MERGES - Merkmale der Quellkomponente in die Zielkomponente uebernehmen
   (Attribute-Zeilen, Varianten-Zeilen, Standardisierungs-Hinweis), Quellordner loeschen.
3. Links  - alle Markdown-Links unter docs/ auf die neuen Pfade umschreiben.

Sicherheit: ohne --apply laeuft der Dry-Run und aendert nichts.

Aufruf:
    python3 tools/restructure_components.py            # Dry-Run
    python3 tools/restructure_components.py --apply    # aendern
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
COMPONENTS = DOCS / "de" / "components"

# ----------------------------------------------------------------MOVES------
# "alt/kategorie/name": ("neue_kategorie", "neuer_name")
INPUTS_TO_FIELDS = [
    "checkbox", "color-input", "combobox", "date-input", "emoji-picker",
    "file-upload", "mention-input", "number-input", "radio-group", "rating",
    "rich-text-editor", "search-field", "slider", "switch", "tags-input",
    "textarea", "text-input",
]
LISTS_TO_DATA = [
    "calendar-view", "grid-view", "list-view", "repeater", "table",
    "table-of-contents", "timeline", "tree-view",
]

MOVES = {f"inputs/{n}": ("fields", n) for n in INPUTS_TO_FIELDS}
MOVES.update({f"lists/{n}": ("data", n) for n in LISTS_TO_DATA})
MOVES.update({
    "inputs/dropdown": ("fields", "select"),          # native-select wird Variante
    "lists/slideshow": ("media", "carousel"),         # Galerie != Karussell
    "media/avatar": ("data", "avatar"),               # Anzeige, nicht Medienwiedergabe
    "special/chart": ("data", "chart"),
    "special/media-player": ("media", "media-player"),  # Elternklasse der Medien
    "containers/modal": ("overlays", "modal"),
    "containers/drawer": ("overlays", "drawer"),
    "containers/alert": ("feedback", "alert"),
    "containers/toast": ("feedback", "toast"),
    "navigation/context-menu": ("overlays", "context-menu"),  # erbt von menu
    "navigation/floating-action-button": ("actions", "floating-action-button"),
})

# Kategorien-Index-Links: alte Kategorie -> neue Kategorie (die index.md der alten
# Kategorien werden ersatzlos gestrichen, ihre Inhalte stecken in der neuen Kategorie)
CATEGORY_MAP = {"inputs": "fields", "lists": "data"}

# Titel der neuen Datei-H1 fuer umbenannte Ordner: (englischer Name, Klammerzusatz)
TITLES = {
    "inputs/dropdown": ("Select", "Auswahlliste"),
    "lists/slideshow": ("Carousel", "Karussell"),
}

# ----------------------------------------------------------------MERGES-----
# (quelle, ziel, Hinweis fuer description.md, [Variantenzeilen fuer Ziel-Tabelle])
MERGES = [
    ("containers/banner", "feedback/alert",
     "Die frühere Komponente `banner` ist als Variante in `alert` aufgegangen: "
     "`inline` (in einem Inhalt) und `banner` (über einer Ansicht, fixiert).",
     ["| **banner** | quer über einer Ansicht, fixiert (`sticky`) |"]),
    ("inputs/range-slider", "fields/slider",
     "Die frühere Komponente `range-slider` ist als Variante in `slider` aufgegangen: "
     "`einfach` (ein Wert) und `bereich` (zwei Werte).",
     ["| **bereich** | Bereichsauswahl mit zwei Griffen |"]),
    ("inputs/email-input", "fields/text-input", None, []),
    ("inputs/url-input", "fields/text-input", None, []),
    ("inputs/phone-input", "fields/text-input", None, []),
    ("inputs/datetime-input", "fields/date-input",
     "Die früheren Komponenten `datetime-input` und `time-input` sind als `type`-Werte "
     "in `date-input` aufgegangen: `date`, `time`, `datetime`.",
     ["| **datetime** | Datum und Uhrzeit gemeinsam |",
      "| **time** | nur Uhrzeit |"]),
    ("inputs/time-input", "fields/date-input", None, []),
    ("inputs/search-input", "fields/search-field",
     "Die frühere Komponente `search-input` ist als Variante in `search-field` "
     "aufgegangen: `simple`, `autocomplete`, `filter`.",
     []),
    ("containers/stepper", "containers/wizard",
     "Die frühere Komponente `stepper` ist als Variante in `wizard` aufgegangen: "
     "`assistent` (mit Führung) und `schrittanzeige` (nur Anzeige der Schritte).",
     ["| **schrittanzeige** | nur Anzeige der Schritte, ohne Führung |"]),
    ("navigation/context-toolbar", "navigation/toolbar",
     "Die früheren Komponenten `context-toolbar` und `ribbon` sind als Varianten in "
     "`toolbar` aufgegangen: `standard`, `kontext`, `ribbon`.",
     ["| **kontext** | blendet abhängig vom Auswahl-Zustand eigene Aktionen ein |",
      "| **ribbon** | mehrzeilige Leiste mit Gruppen, Desktop-Programme |"]),
    ("navigation/ribbon", "navigation/toolbar", None, []),
    ("navigation/hamburger-menu", "navigation/menu",
     "Die frühere Komponente `hamburger-menu` ist als Variante in `menu` aufgegangen: "
     "`dropdown`, `menubar`, `hamburger` (eingeklapptes Mobilmenü).",
     ["| **hamburger** | eingeklapptes Menü mit Icon, Mobile und schmale Fenster |"]),
    ("special/wiki-editor", "fields/rich-text-editor",
     "Die frühere Komponente `wiki-editor` ist als Variante in `rich-text-editor` "
     "aufgegangen: `wysiwyg` und `wiki-syntax`.",
     ["| **wiki-syntax** | Eingabe in Wiki-Syntax, ohne Formatierungsleiste |"]),
    ("special/app-embed", "special/embed",
     "Die früheren Komponenten `app-embed`, `widget-embed` und `iframe-embed` sind in "
     "`embed` mit dem Attribut `source` aufgegangen: `app`, `widget`, `iframe`.",
     ["| **app** | ein anderes FreeSynergy-Programm im Fenster |"]),
    ("special/iframe-embed", "special/embed", None, []),
    ("special/widget-embed", "special/embed", None, []),
]

# -------------------------------------------------------------Utilities-----
ROW_RE = re.compile(r"^\|(.+)\|\s*$")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")
CELL_SPLIT = re.compile(r"(?<!\\)\|")


def cells_of(line):
    """Zellen einer Markdown-Tabelle; `\\|` innerhalb einer Zelle ist kein Trennzeichen."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in CELL_SPLIT.split(s)]


def split_sections(text):
    """Gibt [(heading_or_None, [lines])] zurueck; Prosa vor der ersten Ueberschrift
    bekommt heading None."""
    sections, head, body = [], None, []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append((head, body))
            head, body = line, []
        else:
            body.append(line)
    sections.append((head, body))
    return sections


def join_sections(sections):
    blocks = [("\n".join([h] + b) if h else "\n".join(b)) for h, b in sections]
    return "\n".join(blocks).rstrip() + "\n"


def table_header(body):
    """Spalten der ersten Tabelle eines Abschnitts, oder None."""
    for i, line in enumerate(body):
        if SEP_RE.match(line.strip()) and i > 0:
            return cells_of(body[i - 1]), i - 1
    return None


def attr_rows(body):
    """[(attributname, {spalte: wert}), ...] einer Abschnitts-Tabelle. Hat eine Zeile
    mehr Zellen als die Kopfzeile, laufen die ueberschuessigen Werte in die letzte
    Spalte zusammen (kein Informationsverlust)."""
    hd = table_header(body)
    if not hd:
        return []
    cols, _ = hd
    out = []
    for line in body:
        s = line.strip()
        if not ROW_RE.match(s) or SEP_RE.match(s):
            continue
        cells = cells_of(s)
        if len(cells) < 2 or cells[0].startswith("---"):
            continue
        name = cells[0].strip("`")
        if not name or name.lower() in ("attribut", "variante", "zustand", "typ"):
            continue
        values = cells[1:]
        want = len(cols) - 1
        if want > 0 and len(values) > want:
            values = values[:want - 1] + [" ".join(values[want - 1:])]
        row = {cols[j + 1]: values[j] for j in range(min(want, len(values)))}
        out.append((name, row))
    return out


def repair_attribute_tables(text):
    """Legacy-Tabellen haben oft die Kopfzeile `Attribut | Typ | Beschreibung`, aber
    Zeilen mit vier Zellen (Default fehlt in der Kopfzeile). Beim HTML-Rendern fallen
    die ueberschuessigen Zellen weg. Wird die Kopfzeile um eine Default-Spalte
    ergaenzt, wenn ausnahmslos jede Zeile genau eine Zelle mehr hat."""
    lines = text.splitlines()
    fixed, i = 0, 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip()):
            cols = cells_of(s)
            j, rows = i + 2, []
            while j < len(lines) and lines[j].strip().startswith("|"):
                if ROW_RE.match(lines[j].strip()):
                    rows.append(j)
                j += 1
            surplus = all(len(cells_of(lines[k])) == len(cols) + 1 for k in rows)
            if rows and surplus and cols[:2] == ["Attribut", "Typ"] and "Default" not in cols:
                new = cols[:2] + ["Default"] + cols[2:]
                lines[i] = "| " + " | ".join(new) + " |"
                lines[i + 1] = "|" + "|".join(["---"] * len(new)) + "|"
                fixed += 1
            i = j
        else:
            i += 1
    return "\n".join(lines) + "\n", fixed


def all_attrs(text):
    found = set()
    for _, body in split_sections(text)[1:]:
        for name, _ in attr_rows(body):
            found.add(name)
    return found


def insert_rows(body, rows, cols):
    """Fuegt Zeilen ans Ende der ersten Tabelle des Abschnitts ein."""
    hd = table_header(body)
    rendered = []
    for row in rows:
        cells = [f"`{row[0]}`"] + [row[1].get(c, "-") or "-" for c in cols[1:]]
        rendered.append("| " + " | ".join(cells) + " |")
    if not hd:
        return body + rendered
    last = hd[1]
    for i, line in enumerate(body):
        s = line.strip()
        if ROW_RE.match(s) and not SEP_RE.match(s) and i > hd[1]:
            last = i
    return body[:last + 1] + rendered + body[last + 1:]


def normalize(row, want_cols):
    """Zeile auf die Spalten der Ziel-Tabelle bringen. Hat das Ziel keine Default-
    Spalte, wandert der Vorgabewert in die letzte Spalte."""
    out = {c: row.get(c, "-") for c in want_cols}
    if "Default" not in want_cols and row.get("Default", "-") not in ("-", ""):
        last = want_cols[-1]
        out[last] = f"{row['Default']} {out[last]}".strip()
    return out


def merge_attributes(src_dir, dst_dir):
    src, dst = src_dir / "attributes.md", dst_dir / "attributes.md"
    if not src.is_file() or not dst.is_file():
        return 0
    src_text, dst_text = src.read_text(encoding="utf-8"), dst.read_text(encoding="utf-8")
    have = all_attrs(dst_text)
    add = {}
    for head, body in split_sections(src_text)[1:]:
        for name, row in attr_rows(body):
            if name in have:
                continue
            have.add(name)
            add.setdefault(head or "## Hauptattribute", []).append((name, row))
    if not add:
        return 0
    sections = split_sections(dst_text)
    headings = [h for h, _ in sections if h]
    # Ziel-Abschnitt waehlen: gleicher Name, sonst Verhaltens-/Hauptattribute, neu anlegen
    for src_head, rows in add.items():
        target = src_head if src_head in headings else None
        if target is None:
            for cand in ("## Verhaltens-Attribute", "## Hauptattribute", "## Display-Attribute"):
                if cand in headings:
                    target = cand
                    break
        if target is None:
            sections.append((src_head, [""]))
            headings.append(src_head)
            target = src_head
        for i, (h, body) in enumerate(sections):
            if h == target:
                hd = table_header(body)
                cols = hd[0] if hd else ["Attribut", "Typ", "Beschreibung"]
                sections[i] = (h, insert_rows(body, [(n, normalize(r, cols)) for n, r in rows], cols))
                break
    dst.write_text(join_sections(sections), encoding="utf-8")
    return sum(len(v) for v in add.values())


def merge_variants(dst_dir, rows):
    if not rows:
        return False
    desc = dst_dir / "description.md"
    if not desc.is_file():
        return False
    text = desc.read_text(encoding="utf-8")
    sections = split_sections(text)
    headings = [h for h, _ in sections if h]
    new_rows = [r.strip() for r in rows]
    if "## Varianten" in headings:
        for i, (h, body) in enumerate(sections):
            if h == "## Varianten":
                existing = "\n".join(body)
                sections[i] = (h, body + [r for r in new_rows if cells_of(r)[1] not in existing])
                break
    else:
        pos = headings.index("## Features") + 1 if "## Features" in headings else len(sections)
        sections.insert(pos, ("## Varianten", [""] + new_rows))
    desc.write_text(join_sections(sections), encoding="utf-8")
    return True


def add_note(dst_dir, note):
    if not note:
        return
    desc = dst_dir / "description.md"
    if not desc.is_file():
        return
    text = desc.read_text(encoding="utf-8")
    if note[:30] in text:
        return
    block = ['!!! info "Standardisierung"', f"    {note}", ""]
    sections = split_sections(text)
    first = next((i for i, (h, _) in enumerate(sections) if h), len(sections))
    body = sections[first - 1][1]
    while body and not body[-1].strip():
        body.pop()
    sections[first - 1] = (None, body + [""] + block)
    desc.write_text(join_sections(sections), encoding="utf-8")


def retitles(moved):
    """H1-Zeile umbenannter Komponenten anpassen."""
    for old, (new_cat, new_name) in moved.items():
        if old not in TITLES:
            continue
        eng, de = TITLES[old]
        d = COMPONENTS / new_cat / new_name
        for f in d.glob("*.md"):
            lines = f.read_text(encoding="utf-8").splitlines()
            if lines and lines[0].startswith("# "):
                lines[0] = re.sub(r"^# [^ (]+( \([^)]*\))?", f"# {eng} ({de})", lines[0], count=1)
                f.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------Links-------
def rewrite_links(path_map):
    link_re = re.compile(r"(\]\()([^)\s#]+)(#[^)]*)?(\))")
    changed = 0
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        base = md.parent

        def repl(m):
            nonlocal changed
            target = m.group(2)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                return m.group(0)
            clean = target.split("#")[0]
            if not clean:
                return m.group(0)
            try:
                resolved = (base / clean).resolve() if not clean.startswith("/") else (DOCS / clean.lstrip("/")).resolve()
            except OSError:
                return m.group(0)
            try:
                rel = resolved.relative_to(DOCS)
            except ValueError:
                return m.group(0)
            parts = rel.parts
            # components/<kat>/<name>/... oder components/<kat>/<name>
            if len(parts) >= 3 and parts[0] == "de" and parts[1] == "components":
                new_rel = None
                if len(parts) == 3:
                    # Verweis auf eine Kategorie selbst
                    if parts[2] in CATEGORY_MAP:
                        new_rel = Path("de/components") / CATEGORY_MAP[parts[2]]
                else:
                    key = f"{parts[2]}/{parts[3]}"
                    if parts[3] == "index.md" and parts[2] in CATEGORY_MAP:
                        new_rel = Path("de/components") / CATEGORY_MAP[parts[2]] / "index.md"
                    elif key in path_map:
                        new_cat, new_name = path_map[key]
                        new_rel = Path("de/components") / new_cat / new_name
                        if len(parts) > 4:
                            new_rel = new_rel / Path(*parts[4:])
                if new_rel is not None:
                    newlink = relpath_link(md, DOCS / new_rel)
                    changed += 1
                    return m.group(1) + newlink + (m.group(3) or "") + m.group(4)
            return m.group(0)

        new_text = link_re.sub(repl, text)
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
    return changed


def relpath_link(from_file, to_path):
    """Relativer Link von from_file zu to_path unterhalb von docs/ (Verzeichnis endet auf '/')."""
    src, dst = from_file.parent, to_path
    src_parts, dst_parts = src.relative_to(DOCS).parts, dst.relative_to(DOCS).parts
    common = 0
    while common < len(src_parts) and common < len(dst_parts) and src_parts[common] == dst_parts[common]:
        common += 1
    out = "/".join([".."] * (len(src_parts) - common) + list(dst_parts[common:]))
    if dst.suffix == "":
        out += "/"
    return out or "./"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--links-only", action="store_true",
                    help="nur Links auf das Zielbild umschreiben (Moves/Merges bereits erfolgt)")
    args = ap.parse_args()

    # Pfadkarte vorab deklarativ aufbauen (gilt auch, wenn die alten Pfade schon
    # weg sind, z. B. bei --links-only).
    path_map = {old: new for old, new in MOVES.items()}
    for src, dst, _note, _rows in MERGES:
        cat, name = dst.split("/", 1)
        path_map[src] = (cat, name)

    if args.links_only:
        print(f"Nur Links umgeschrieben: {rewrite_links(path_map)}")
        return 0

    moved, planned = {}, set()
    print("== MOVES ==")
    for old, new in sorted(MOVES.items()):
        src = COMPONENTS / old
        dst = COMPONENTS / new[0] / new[1]
        if not src.is_dir():
            print(f"  uebersprungen (fehlt): {old}")
            continue
        if dst.exists():
            print(f"  FEHLER: Ziel existiert bereits: {dst}")
            return 1
        path_map[old] = new
        moved[old] = new
        planned.add(f"{new[0]}/{new[1]}")
        print(f"  {old} -> {new[0]}/{new[1]}")
        if args.apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    retitles(moved) if args.apply else None

    print("\n== TABELLEN (fehlende Default-Spalte ergaenzt) ==")
    repaired = 0
    if args.apply:
        for md in sorted(COMPONENTS.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            new, n = repair_attribute_tables(text)
            if n:
                repaired += n
                md.write_text(new, encoding="utf-8")
    print(f"  Kopfzeilen repariert: {repaired}")

    print("\n== MERGES ==")
    total_attrs = 0
    for src, dst, note, vrows in MERGES:
        s, d = COMPONENTS / src, COMPONENTS / dst
        if not s.is_dir():
            print(f"  uebersprungen (fehlt): {src}")
            continue
        if not d.is_dir() and dst not in planned:
            print(f"  FEHLER: Ziel existiert nicht: {dst} (vorher anlegen oder in MOVES eintragen)")
            return 1
        n = merge_attributes(s, d) if args.apply else 0
        total_attrs += n
        if args.apply:
            merge_variants(d, vrows)
            add_note(d, note)
            shutil.rmtree(s)
        path_map[src] = (dst.split("/")[0], dst.split("/")[1])
        print(f"  {src} -> {dst}  ({n} Attribute uebernommen)")

    print("\n== LINKS ==")
    if args.apply or args.links_only:
        n = rewrite_links(path_map)
        print(f"  umgeschriebene Links: {n}")
    else:
        print(f"  betroffene Pfade: {len(path_map)}")

    print(f"\n{'ANGEWENDET' if args.apply else 'DRY-RUN (nichts geaendert)'}")
    print(f"  Verschoben: {len(moved)}   Zusammengelegt: {len(MERGES)}   Attribute uebernommen: {total_attrs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

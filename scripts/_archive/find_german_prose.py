#!/usr/bin/env python3
"""List en/components docs that still contain German prose.

Kept-on-purpose German is skipped: code fences, ASCII diagrams, and variant/state
identifiers (``inhalt``, ``facher`` and bold table cells like ``**einklappbar**``),
which stay German per ADR 0002.
"""
import re
import sys
from pathlib import Path

WORDS = [
    "und", "der", "die", "das", "dem", "den", "des", "ein", "eine", "einen", "einem",
    "einer", "ist", "sind", "war", "waren", "wird", "werden", "wurde", "kann", "muss",
    "soll", "nicht", "auch", "oder", "aber", "wenn", "dann", "f\u00fcr", "mit", "von",
    "zur", "zum", "im", "am", "auf", "aus", "bei", "nach", "vor", "\u00fcber", "unter",
    "als", "diese", "dieser", "dieses", "siehe", "beschreibung", "verwendung",
    "verwendungszweck", "beispiel", "beispiele", "eigenschaften", "zust\u00e4nde",
    "hinweis", "hinweise", "komponente", "komponenten", "anwendung", "einsatz",
    "aufbau", "unterscheidung", "verwechslung", "\u00fcbersicht", "weiterf\u00fchrende",
    "kategorie", "kategorien", "erbt", "verwandt", "dokumentiert", "kein", "keine",
    "sowie", "etwa", "jeweils", "dabei", "dadurch", "daher", "danach", "bevor",
    "w\u00e4hrend", "durch", "gegen", "ohne", "links", "rechts", "oben", "unten",
    "immer", "bzw", "usw", "deswegen", "ebenso", "bereits", "welche", "jedes",
    "jeder", "jede", "etwas", "sehr", "beste", "aussehen", "gr\u00f6\u00dfe",
    "gr\u00f6\u00dfen", "h\u00f6he", "farbe", "farben", "verhalten", "effekte",
    "reaktiv", "barrierefreiheit", "geerbt", "hauptattribute", "darstellung",
    "variante", "grundlayout", "men\u00fcleiste", "men\u00fcpunkt", "men\u00fcpunkte",
    "einklappbar", "ausgegraut", "aktionen", "auswahl", "einstellungen",
    "werkzeugleiste", "seitenleiste", "objekt", "objekte", "bereit", "fehler",
    "geladen", "leer", "klein", "gro\u00df", "schnell", "einfach", "speichern",
    "l\u00f6schen", "\u00f6ffnen", "schlie\u00dfen", "bearbeiten", "abbruch",
    "best\u00e4tigen", "vorschau", "vorschlag", "beschriftung", "einordnung",
    "szenarien", "merkmale", "abgrenzung", "eintr\u00e4ge", "eintrag", "zeige",
    "fl\u00e4che", "fl\u00e4chen", "klick", "klickt", "aufl\u00f6sung", "benutzer",
    "eigene", "eigener", "eigenes", "eigenen", "sondern", "wobei", "damit",
    "mehrere", "einzelne", "bereits", "deutlich", "dauerhaft", "dauerhafte",
    "bleibt", "bleiben", "gew\u00e4hlt", "getroffen", "gestellt", "gesetzt",
    "gel\u00f6scht", "gemerkt", "verlassen", "verwenden", "vorhanden", "verschiedene",
    "verbessern", "vollst\u00e4ndig", "wichtig", "wichtige", "zusammen", "zur\u00fcck",
    "zur\u00fcckkehrt", "zeigen", "zeigt", "ziehen", "setzen", "setzt", "suchen",
    "starten", "stellen", "stellt", "laufen", "legen", "legt", "lesen", "laden",
    "halten", "h\u00e4lt", "gehen", "geht", "folgen", "folgt", "fahren", "denken",
    "brauchen", "braucht", "bedienen", "bedient", "achten", "\xf6ffnet", "schlie\u00dft",
    "l\u00e4uft", "wird", "werden", "wurde", "knnen", "bekommt", "bekommen",
    "bleibst", "erreicht", "erm\u00f6glicht", "erlaubt", "erzeugt", "enth\u00e4lt",
    "entscheidet", "entwickelt", "erg\u00e4nzt", "erh\u00f6ht", "verhindert",
    "verhindern", "verursacht", "verwenden", "vergleichen", "verschieben",
    "verst\u00e4rkt", "verteilt", "versteckt", "verwendet", "w\u00e4hlen", "w\u00e4hlt",
    "zurecht", "zus\u00e4tzlich", "zurzeit",
]
# identical or near-identical in English -> not evidence of German
IGNORE = {
    "element", "elemente", "struktur", "auto", "daten", "bereich", "bereiche",
    "wert", "werte", "werten", "feld", "felder", "punkt", "punkte", "datum",
    "in", "an", "auf", "bei", "nur", "man", "events", "links", "mit", "aktiv",
    "optionen", "typ", "typen", "plan", "filter", "status", "text", "texts",
}
WORDS = sorted({w for w in WORDS if w not in IGNORE})
GER_WORD = re.compile(
    r"(?i)(?<![A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df])(?:%s)(?![A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df])"
    % "|".join(WORDS)
)
UMLAUT_INSIDE = re.compile(r"[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc][\u00e4\u00f6\u00fc\u00df]")
FENCE = re.compile(r"^\s*(```|~~~)")
# box-drawing art only; ASCII "|" stays checked because it starts markdown tables
BOX = re.compile(
    r"^\s*[\u250c\u2514\u251c\u2500\u2502\u2554\u2550\u2551\u250e\u256d\u2570\u256e\u2552\u2518\u2510]"
)


def prose(text):
    """Yield (lineno, prose-only text) outside code fences, identifiers stripped."""
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or BOX.match(line):
            continue
        line = re.sub(r"`[^`]*`", "", line)          # inline identifiers
        line = re.sub(r"\*\*[^*]+\*\*", "", line)    # variant / state names
        yield i, line


def hits(path):
    out = []
    for i, line in prose(path.read_text(encoding="utf-8")):
        if GER_WORD.search(line) or UMLAUT_INSIDE.search(line):
            out.append((i, line))
    return out


def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            found = hits(Path(arg))
            print(f"\n### {arg} ({len(found)})")
            for i, line in found:
                print(f"  {i}: {line}")
        return
    rows = []
    for f in sorted(Path("docs/en/components").rglob("*.md")):
        found = hits(f)
        if found:
            rows.append((len(found), str(f)))
    rows.sort(reverse=True)
    for n, f in rows:
        print(f"{n:4d} {f}")
    print("FILES:", len(rows), "LINES:", sum(r[0] for r in rows))


if __name__ == "__main__":
    main()

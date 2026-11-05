#!/usr/bin/env python3
"""Check en/components for leftover German prose.

Convention (ADR 0002 / existing translations): identifiers inside backticks keep their
German names (e.g. `inhalt`, `facher`), so they are excluded. Words that are identical in
English are excluded too.
"""
import re, sys
from pathlib import Path

WORDS = [
    "und", "der", "die", "das", "dem", "den", "des", "ein", "eine", "einen", "einem", "einer",
    "ist", "sind", "war", "waren", "wird", "werden", "wurde", "kann", "koennen", "kann", "muss",
    "soll", "nicht", "auch", "oder", "aber", "wenn", "dann", "fuer", "für", "mit", "von", "zur",
    "zum", "im", "am", "auf", "aus", "bei", "nach", "vor", "über", "unter", "als", "diese",
    "dieser", "dieses", "siehe", "beschreibung", "beschreibung", "verwendung", "verwendungszweck",
    "beispiel", "beispiele", "eigenschaften", "eigenschaft", "zustände", "zustand", "hinweis",
    "hinweise", "komponente", "komponenten", "anwendung", "einsatz", "aufbau", "struktur",
    "funktionen", "funktion", "unterscheidung", "verwechslung", "übersicht", "weiterführende",
    "kategorie", "kategorien", "erbt", "verwandt", "dokumentiert", "kein", "keine", "sowie",
    "etwa", "jeweils", "dabei", "dadurch", "daher", "danach", "bevor", "während", "durch",
    "gegen", "ohne", "links", "rechts", "oben", "unten", "immer", "bzw", "usw", "deswegen",
    "ebenso", "bereits", "welche", "jedes", "jeder", "jede", "etwas", "mehr", "weniger", "sehr",
    "gut", "beste", "aussehen", "größe", "größen", "höhe", "farbe", "farben", "verhalten",
    "effekte", "effekt", "reaktiv", "barrierefreiheit", "geerbt", "hauptattribute", "darstellung",
    "variante", "varianten", "grundlayout", "menüleiste", "menüpunkt", "menüpunkte", "untermenü",
    "einklappbar", "ausgegraut", "inhalt", "aktionen", "aktion", "auswahl", "einstellungen",
    "datum", "sprache", "sprachen", "benutzer", "gruppe", "gruppen", "ansicht", "ansichten",
    "werkzeugleiste", "seitenleiste", "objekt", "objekte", "bereit", "fehler", "geladen",
    "leer", "voll", "klein", "groß", "groesse", "schnell", "einfach", "neue", "neu", "speichern",
    "löschen", "oeffnen", "öffnen", "schließen", "bearbeiten", "abbruch", "bestätigen",
    "vorschau", "vorschläge", "vorschlag", "element", "elemente", "feld", "felder", "werten",
    "werte", "wert", "punkte", "punkt", "bereich", "bereiche", "ebene", "ebenen", "zeige",
    "einträge", "einträge", "eintrag", "einigen", "gespeichert", "gemerkt", "bleibt", "bleiben",
    "einfach", "mit", "ohne", "szenarien", "grundlayout", "größen", "farben", "zustände",
    "effekte", "reaktiv", "varianten", "barrierefreiheit", "geerbt",
    "hauptattribute", "darstellung", "verhalten", "abgrenzung", "merkmale", "verwendung",
    "einstellung", "einstellungen", "klick", "fläche", "flächen", "bezug", "bezeichnung",
    "beschriftung", "aussehen", "einziges", "jeweils", "jeweils", "jeweilige", "jeweiligen",
    "gemacht", "gebracht", "gesucht", "gewählt", "getroffen", "geladen", "gestellt", "gesetzt",
    "zeigen", "zeigt", "ziehen", "zieht", "setzen", "setzt", "suchen", "sucht", "speichert",
    "schreiben", "schreibt", "sprechen", "spricht", "springen", "springt", "starten", "startet",
    "stellen", "stellt", "laufen", "läuft", "legen", "legt", "lesen", "liest", "laden", "lädt",
    "halten", "hält", "gehen", "geht", "folgen", "folgt", "fallen", "fällt", "fahren", "fährt",
    "denken", "denkt", "brauchen", "braucht", "bedienen", "bedient", "achten", "achtet",
]
# words identical or near-identical in English -> ignore
IGNORE = {"element", "elemente", "struktur", "auto", "daten", "bereich", "bereiche", "wert",
          "werte", "werten", "feld", "felder", "punkt", "punkte", "datum", "in", "an",
          "auf", "bei", "nur", "man", "events", "links"}
WORDS = [w for w in WORDS if w not in IGNORE]

GER = re.compile(r"(?i)(?<![A-Za-zÄÖÜäöüß])(?:" + "|".join(WORDS) + r")(?![A-Za-zÄÖÜäöüß])")
UMlaut = re.compile(r"[A-Za-zÄÖÜäöü][äöüß]")
FENCE = re.compile(r"^\s*(```|~~~)")

def prose_lines(text):
    """Yield (lineno, line) outside code fences, with `inline code` stripped."""
    out = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        # variant/state names are kept in German (ADR 0002), incl. bold table cells
        line = re.sub(r"\*\*[^*]+\*\*", "", line)
        out.append((i, line))
    return out

def german_hits(text):
    hits = []
    for i, line in prose_lines(text):
        if GER.search(line) or UMlaut.search(line):
            hits.append((i, line))
    return hits

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        f = Path(arg)
        hits = german_hits(f.read_text(encoding="utf-8"))
        print(f"\n### {f} ({len(hits)})")
        for i, line in hits:
            print(f"  {i}: {line}")
else:
    root = Path("docs/en/components")
    rows = []
    for f in sorted(root.rglob("*.md")):
        hits = german_hits(f.read_text(encoding="utf-8"))
        if hits:
            rows.append((len(hits), str(f)))
    rows.sort(reverse=True)
    for n, f in rows:
        print(f"{n:4d} {f}")
    print("TOTAL FILES:", len(rows), " TOTAL LINES:", sum(r[0] for r in rows))

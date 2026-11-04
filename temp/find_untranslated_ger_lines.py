#!/usr/bin/env python3
"""TODO list + per-file German lines for en/components. Usage: tmp_ger.py [files...]"""
import re, sys
from pathlib import Path

WORDS = "|".join([
    r"und", r"der", r"die", r"das", r"dem", r"den", r"des", r"ein", r"eine", r"einen", r"einem",
    r"einer", r"ist", r"sind", r"war", r"waren", r"wird", r"werden", r"wurde", r"kann", r"muss",
    r"soll", r"nicht", r"auch", r"oder", r"aber", r"wenn", r"dann", r"für", r"mit", r"von", r"zur",
    r"zum", r"im", r"am", r"auf", r"aus", r"bei", r"nach", r"vor", r"über", r"unter", r"als",
    r"diese", r"dieser", r"dieses", r"siehe", r"beschreib\w*", r"verwendungs?\w*", r"beispiele?",
    r"eigenschaft\w*", r"zuständen?", r"hinweise?", r"komponente?\w*", r"anwendung", r"einsatz",
    r"aufbau", r"struktur", r"funktionen?", r"unterscheidung", r"verwechslung", r"übersicht",
    r"weiterführende", r"feld", r"feldern?", r"wert", r"kategorien?", r"erbt?", r"verwandt",
    r"dokumentiert", r"kein", r"keine", r"sowie", r"etwa", r"jeweils", r"dabei", r"dadurch",
    r"daher", r"danach", r"bevor", r"während", r"durch", r"gegen", r"ohne", r"nur", r"links",
    r"rechts", r"oben", r"unten", r"immer", r"bzw", r"usw", r"deswegen", r"ebenso", r"bereits",
    r"welche?", r"jedes", r"jeder", r"jede", r"etwas", r"mehr", r"weniger", r"sehr", r"gut",
    r"beste", r"aussehen", r"größe\w*", r"höhe", r"farbe?", r"farben", r"zustand", r"verhalten",
    r"effekte?", r"reaktiv", r"barrierefreiheit", r"geerbt", r"hauptattribute", r"darstellung",
    r"variante", r"grundlayout", r"menüleiste", r"menüpunkt\w*", r"untermenü", r"einklappbar",
    r"ausgegraut", r"inhalt", r"events", r"varianten", r"auswahl", r"einstellungen", r"datum",
    r"sprache", r"sprachen", r"benutzer", r"gruppe", r"gruppen", r"ansicht", r"ansichten",
    r"werkzeugleiste", r"seitenleiste", r"overlay", r"aktion", r"aktionen", r"objekt", r"objekte",
    r"bereit", r"feHLT", r"fehler", r"geladen", r"leer", r"voll", r"klein", r"groß", r"schnell",
    r"einfach", r"neue?", r"neu", r"speichern", r"löschen", r"öffnen", r"schließen", r"bearbeiten",
    r"abbrechen", r"abbrechen", r"bestätigen", r"abbruch", r"hinweis", r"vorschlag", r"vorschläge",
])
# drop German words that collide with common English words
WORDS = "|".join(w for w in WORDS.split("|") if w not in (r"events", r"links", r"feld", r"wert", r"in", r"an", r"auf", r"aus", r"bei", r"nur", r"man"))
GER = re.compile(r"(?i)(?<![A-Za-zÄÖÜäöüß])(?:" + WORDS + r")(?![A-Za-zÄÖÜäöüß])|[a-zäöü][äöüß]")

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        f = Path(arg)
        print(f"\n### {f}")
        n = 0
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if GER.search(line):
                print(f"  {i}: {line}")
                n += 1
        print(f"  -> {n}")
else:
    root = Path("docs/en/components")
    rows = []
    for f in sorted(root.rglob("*.md")):
        t = f.read_text(encoding="utf-8")
        de = Path("docs/de/components") / f.relative_to(root)
        n = len(GER.findall(t))
        if n:
            rows.append((n, str(f)))
    rows.sort(reverse=True)
    for n, f in rows:
        print(f"{n:4d} {f}")
    print("TOTAL FILES:", len(rows), " TOTAL MATCHES:", sum(r[0] for r in rows))

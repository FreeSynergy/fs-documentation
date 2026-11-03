#!/usr/bin/env python3
"""Report EN component docs that still contain untranslated German prose.

Method: a line counts as untranslated when it is byte-identical to the same
line in the DE source AND it carries German evidence (an umlaut/scharf-sz outside
identifiers, or a German function word). Code fences and ASCII-art rows are
ignored; identifiers in backticks / bold table keys are ignored, because the
project convention keeps the German variant/state slugs verbatim in EN too.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/srv/FreeSynergy/fs-documentation")

DE_WORDS = {
    "und", "oder", "nicht", "mit", "von", "für", "das", "die", "der", "ein", "eine",
    "einem", "einen", "einer", "eines", "ist", "sind", "war", "waren", "wird",
    "werden", "wurde", "wurden", "kann", "können", "muss", "müssen", "soll",
    "sollen", "bei", "aus", "nach", "über", "unter", "zwischen", "innerhalb",
    "außerhalb", "sich", "auch", "aber", "wenn", "dann", "hier", "diese", "dieser",
    "dieses", "kein", "keine", "sondern", "wobei", "damit", "dadurch", "jeweils",
    "des", "dem", "den", "denen", "deren", "als", "um", "am", "im", "zur", "zum",
    "vor", "gegen", "durch", "ohne", "statt", "bzw", "mehrere", "einzelne",
    "einige", "viele", "wenige", "manche", "nichts", "etwas", "viel", "wenig",
    "immer", "nie", "oft", "etwa", "bereits", "weiter", "dabei", "hierfür",
    "hierzu", "etwa", "sodass", "sowie", "etwa", "et cetera",
}
DE_ONLY = re.compile(
    r"\b(Beschreibung|Verwendungszweck|Varianten|Abgrenzung|Siehe auch|Verhalten|"
    r"Darstellung|Barrierefreiheit|Geerbt von|Hauptattribute|Anwendung|Szenarien|"
    r"Grundlayout|Größen|Farben und Zustände|Hover- und|Reaktiv|Einordnung|Hinweis|"
    r"Wichtig|Übersicht|Eigenschaften|Verwendung|Aussehen|Optionen|Zustände|"
    r"Fläche|Bedienung|Benutzer|Anzeige|Auswahl|Bereich|Knopf|Inhalt|Platzhalter|"
    r"zusätzlich|beachten|verwenden|ermöglicht|erfordert|gehört|bleibt|zeigt|"
    r"stellen|steht|bildet|aufbau|eintrag|einträge|feld|felder|gruppe|werte|"
    r"typisch|betont|normaler|normale)\b",
    re.IGNORECASE,
)
UMLAUT = re.compile(r"[äöüÄÖÜß]")
IDENT = re.compile(r"`[^`]*`|\*\*[^*]+\*\*")
ART = re.compile(r"^\s*[│┌└├┤┬┴┼─═╔╚╠╣»«◀▶⏮⏭🎬🎥🎞📺📽🖼🔊🔇🔄🔀♻]")
WORDS = re.compile(r"[A-Za-zÄÖÜäöüß]+")


def read_lines(p: Path):
    return p.read_text(encoding="utf-8").splitlines()


def untranslated(en_lines, de_lines):
    hits = []
    fence = False
    for i, line in enumerate(en_lines):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if ART.match(line):
            continue
        same = i < len(de_lines) and de_lines[i] == line
        if not same:
            continue
        probe = IDENT.sub(" ", line)
        if not probe.strip():
            continue
        why = []
        if UMLAUT.search(probe):
            why.append("umlaut")
        low = {w.lower() for w in WORDS.findall(probe)}
        got = sorted(low & DE_WORDS)
        if got:
            why.extend(got)
        m = DE_ONLY.search(probe)
        if m:
            why.append(m.group(1).lower())
        if why:
            hits.append((i + 1, line, sorted(set(why))))
    return hits


def main():
    scope = sys.argv[1] if len(sys.argv) > 1 else "docs/en/components"
    base = ROOT / scope
    report = []
    for en in sorted(base.rglob("*.md")):
        de = ROOT / str(en.relative_to(ROOT)).replace("docs/en/", "docs/de/", 1)
        if not de.exists():
            print(f"NO-DE-SOURCE {en.relative_to(ROOT)}")
            continue
        hits = untranslated(read_lines(en), read_lines(de))
        if hits:
            report.append((len(hits), en.relative_to(ROOT), hits))
    report.sort(key=lambda r: (str(r[1])))
    verbose = "-v" in sys.argv
    for n, rel, hits in report:
        print(f"{n:4d}  {rel}")
        if verbose:
            for ln, line, why in hits:
                print(f"        {ln}: {line}   <{','.join(why)}>")
    print(f"--- files needing work: {len(report)} ---")


if __name__ == "__main__":
    main()

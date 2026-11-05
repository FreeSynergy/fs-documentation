# 0007 – `skins/` wird `masks/`

## Kontext
ADR 0001 und die Doku-Struktur benutzen für die Nachbau-Oberflächen eines Programms den Ordner
`skins/`. Das Architektur-Protokoll §2 hat den Begriff längst korrigiert: **Maske** = Struktur
(Menüs, Raumaufteilung, Interaktion, Tastenkürzel), **Theme** = Farben/Abstände/Typografie.
„Skin“ wird als Aussehen gelesen und trägt zu viel. Die Doku hinkte dem Begriff hinterher.

## Entscheidung
Der Unterordner heißt **`masks/`**:

```
docs/<sprache>/programs/<ebene>/<kategorie>/masks/<programm>/
```

- Sprachlich: **mask / masks** (englische Identifikatoren, ADR 0002).
- Das Wort „Skin“ bleibt in **historischen Notizen** und in Zitaten fremder Produkte stehen,
  beschreibt aber nicht mehr unsere Struktur.
- Der Generator heißt weiterhin `scripts/gen_skin_indexes.py` (Pfad-Mathematik unverändert,
  CONVENTIONS §5); umbenennen, wenn er das nächste Mal ohnehin angefasst wird.

## Folgen
- 19 Verzeichnisse `skins/` → `masks/` in `docs/de/` und `docs/en/` per `git mv`, danach
  `scripts/fix_links.py --force` (Link-Mitschrift, CONVENTIONS §9) und `mkdocs build` als
  Verifikation.
- Pfadtexte in `docs/de/programs/index.md`, `conventions/doku-standard.md`,
  `data/conventions.md`, `data/index.md` und `temp/apps-plan.md` folgen.
- Neue Kategorie-Anlage (ADR 0001/0004 Ablauf) nutzt `masks/`.
- Eine Maske ist pro Programm und steht beim Start fest (Protokoll §2) — die Doku-Struktur
  bildet genau das ab: eine Maske = ein Verzeichnis mit den sieben Dateien.

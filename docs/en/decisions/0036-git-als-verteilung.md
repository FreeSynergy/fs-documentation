# 0036 – Git als dezentrale Verteilung: Pakete, Themes, Programme, Medien

Status: akzeptiert (2026-11-05) · Name des Ladens: `fs-store` (ADR 0060; die heutige Datenablage wird `fs-objects`)

## Entscheidung (Nutzer)
- **Git wird zum Paketinstaller** — über **gitoxide (`gix`)**, reines Rust. Man macht es selbst und
  kommt von überall dran.
- In Git-Repositorys liegen: **Installationen**, der **„Shop“** (Angebote von uns oder anderen:
  selbstgemachte Themes, Programme, Frontends, …) und **Medien** (Bilder, GIFs, Sticker).
- **Dezentral:** jeder kann ein Repository anbieten (eigene, Gemeinschaft, kostenlose Angebote);
  wer will, bindet es ein.
- **GIF-/Bildsuche** gibt es — aber über diese Repositorys, nicht über fremde Dienste, die
  mitlesen, was man tippt.

## Ergänzung des Nutzers (2026-11-07, zu besprechen)
- **Die Leute sollen etwas sehen:** Dafür müssen die Pakete alle online kommen.
- **Ein Launcher** sammelt die Programme und stellt sie automatisch online, ähnlich wie bei ArtCraft (vom Nutzer genannt, noch nicht analysiert; nur Funktionsanalyse, nichts kopieren, ADR 0013).
- **Er aktualisiert sich selbst** automatisch.
- **Liste von Git-Servern:** erweiterbar. Unserer ist fest drin, man kann ihn deaktivieren, aber nicht löschen; er dient als Referenz.
- **Wir fangen mit einem an,** aber installiert wird mehr als Programme: Frontends, andere Programme usw.
- Offen: was alles in das Paket oder die Pakete kommt und dann fertig programmiert wird.

## Folgen
- Programm/Kategorie für Paketverwaltung planen (Name offen); Format eines Paket-Repositorys
  (Manifest, Signatur — FEP-8b32/ADR 0035 Vertrauen) festlegen.
- Verhältnis gix ↔ Aktivitätsprotokoll (ADR 0020) bleibt Gesprächspunkt.

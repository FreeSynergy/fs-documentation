# 0036 – Git als dezentrale Verteilung: Pakete, Themes, Programme, Medien

Status: akzeptiert (2026-11-05) · Name des „Shops“ offen (`store` ist durch `fs-store` belegt)

## Entscheidung (Nutzer)
- **Git wird zum Paketinstaller** — über **gitoxide (`gix`)**, reines Rust. Man macht es selbst und
  kommt von überall dran.
- In Git-Repositorys liegen: **Installationen**, der **„Shop“** (Angebote von uns oder anderen:
  selbstgemachte Themes, Programme, Frontends, …) und **Medien** (Bilder, GIFs, Sticker).
- **Dezentral:** jeder kann ein Repository anbieten (eigene, Gemeinschaft, kostenlose Angebote);
  wer will, bindet es ein.
- **GIF-/Bildsuche** gibt es — aber über diese Repositorys, nicht über fremde Dienste, die
  mitlesen, was man tippt.

## Folgen
- Programm/Kategorie für Paketverwaltung planen (Name offen); Format eines Paket-Repositorys
  (Manifest, Signatur — FEP-8b32/ADR 0035 Vertrauen) festlegen.
- Verhältnis gix ↔ Aktivitätsprotokoll (ADR 0020) bleibt Gesprächspunkt.

# 0017 – Programme heißen nach Kategorie, ein Repo pro Programm

Status: akzeptiert (2026-11-05)

## Kontext
Fremde Programmnamen (Matrix, Outlook) sagen nichts über die Aufgabe. Unsere Programme
bilden eine Kategorie ab, nicht ein Vorbild.

## Entscheidung
- **Name = Kategorie:** `FreeSynergy.Messenger`, `FreeSynergy.Calendar`, `FreeSynergy.Wiki` …
- **Ein Repo pro Programm**, Kurzform `fs-<category>`: `fs-messenger`, `fs-calendar`.
  Components, Plattform-Teile und Suiten folgen demselben Muster (`fs-<name>`).
- **Doku liegt zentral** in `fs-documentation`; Code-Repos enthalten nur Hilfs-Doku (ADR 0003).
- **Jedes Programm läuft allein.** Mehrere Programme zusammen **teilen sich die Arbeit** über die
  gemeinsamen Standarddaten (ADR 0014): Kontakte, die ich einmal eingebe, sind im Messenger, im
  Projektmanagement und im ERP da — und umgekehrt. Wie Speicherung und Abgleich genau laufen,
  ist offen (Protokoll §3, eigenes Gespräch).
- Jedes Programm liefert eine **Schnittstelle**; Frontends (ADR 0012) baut jeder, wie er möchte —
  nach einem Vorbild oder frei.

## Folgen
- Doku-Kategorien heißen wie die Programme (`programs/apps/messenger/` = `fs-messenger`).
- Unterkategorien sind kein eigenes Programm; siehe ADR 0018 (Messenger inkl. E-Mail).

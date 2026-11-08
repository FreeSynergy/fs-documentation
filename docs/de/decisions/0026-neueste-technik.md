# 0026 – Immer die neueste Technik

Status: akzeptiert (2026-11-05)

## Kontext
Bis die Programme fertig sind, ist heute Neues schon älter. Wer mit Altem beginnt, endet veraltet.

## Entscheidung
- Wir wählen die **neueste tragfähige** Technik: aktuelle Standards (JMAP vor IMAP, MLS,
  JSContact/JSCalendar vor vCard/iCalendar intern), aktuelle Major-Versionen der Crates, aktuelle
  Rust-Edition.
- Ältere Protokolle nur als **Brücke nach außen** (IMAP, vCard, iCalendar für Fremdprogramme).
- Vor jeder Wahl prüfen, ob es etwas Neueres gibt (Recherche nach ADR 0013 speichern).
- Grenze: offen, ohne Paywall (ADR 0015/0016); „neu“ heißt nicht „ungepflegt“ — gepflegte,
  aktive Projekte bevorzugen, wie bei den „Early-Bird“-Projekten (Blinc, Turso, tuwunel).

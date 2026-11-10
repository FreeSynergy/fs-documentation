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

## Ergänzung 2026-11-11: neueste Rust-Version, aber gepinnt
- „Neueste“ heißt nicht „ungeprüft“: Die Rust-Toolchain ist an **einer** Stelle gepinnt,
  `RUST_VERSION` in fs-release. Gates (`gates.sh`), GitHub-CI und Release-Build nutzen genau diese
  Version, damit lokal, CI und Release dasselbe Ergebnis liefern.
- Hochziehen geschieht **gemeinsam**: ein Bump-PR in fs-release; vorher läuft `gates.sh` auf allen
  Programm-Repos mit der neuen Version. Erst wenn alle grün sind, wird gemergt.
- Ziel bleibt die neueste stabile Version; der Bump soll zeitnah nach jedem Rust-Release passieren.

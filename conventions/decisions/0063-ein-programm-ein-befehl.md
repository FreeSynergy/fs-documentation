# 0063 – Ein Programm, ein Befehl: `fs-<programm>` mit Unterbefehlen

Status: akzeptiert (Nutzer, 2026-11-08) · ergänzt ADR 0021 (Motor und Frontend), 0061 (Facetten)

## Entscheidung (Nutzer)
Keine eigene Datei je Rolle (`fs-store-cli`, `fs-store-app`, `fs-tasks-server`). Jedes Programm hat **ein** ausführbares Programm, das so heißt wie das Programm, und Unterbefehle. Alles in Rust, kein Shell-Skript als Weiche.

## Regel
- `fs-store` ohne Argumente startet die Oberfläche (ist keine gebaut: Hilfe ausgeben).
- Kommandozeile als Unterbefehle direkt, wie bei `git`: `fs-store install fs-tasks`, `fs-store installed`, `fs-store sources add …`. Kein `cli`-Zwischenwort nötig.
- Server: `fs-store serve` (bzw. `fs-tasks serve`).
- Facetten (ADR 0061): `fs-people --facet contacts`; der Menüeintrag „Contacts“ ruft genau das auf. Admin-Frontend: `fs-people admin` bzw. `fs-people admin --facet contacts`.
- Umsetzung: Ein Crate mit `[[bin]] name = "fs-<programm>"` verteilt die Unterbefehle an die vorhandenen Crates (`-app`, `-server`, CLI), die als Bibliotheken bleiben. Muster: Command (je Unterbefehl ein Typ hinter einem Trait) bzw. Facade.
- **Ohne Grafik bauen:** Cargo-Feature `gui` (Standard an). Server und Rechner ohne Bildschirm bauen mit `--no-default-features`; derselbe Name, `fs-x` ohne Argumente gibt dann Hilfe aus. So hängt ein Server nicht an Grafik-Bibliotheken.

## Folgen
- Gilt für neue Arbeit sofort und für den Laden zuerst. Bestehende Programme werden umgestellt, wenn sie ohnehin angefasst werden; Pakete (rpm/deb) und Menüeinträge nur noch auf `fs-<programm>`.

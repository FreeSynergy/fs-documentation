# 0063 – Ein Programm, ein Befehl: `fs-<programm>` mit Unterbefehlen

Status: akzeptiert (Nutzer, 2026-11-08) · ergänzt ADR 0021 (Motor und Frontend), 0061 (Facetten)

## Entscheidung (Nutzer)
Keine eigene Datei je Rolle (`fs-store-cli`, `fs-store-app`, `fs-tasks-server`). Jedes Programm hat **ein** ausführbares Programm, das so heißt wie das Programm, und Unterbefehle. Alles in Rust, kein Shell-Skript als Weiche.

## Regel
- `fs-store` ohne Argumente startet die Oberfläche (ist keine gebaut: Hilfe ausgeben).
- Kommandozeile als Unterbefehle direkt, wie bei `git`: `fs-store install fs-tasks`, `fs-store installed`, `fs-store sources add …`. Kein `cli`-Zwischenwort nötig.
- Server: `fs-store serve` (bzw. `fs-tasks serve`).
- **Facetten wie Programme (Nutzer, 2026-11-08):** Jede Facette hat einen eigenen Befehl `fs-<facette>`, z. B. `fs-contacts`. Er ist ein **symbolischer Link** auf `fs-people`; das Programm liest, unter welchem Namen es gestartet wurde (`argv[0]`, wie busybox), und öffnet die Facette. Rein in Rust. `fs-contacts admin` öffnet das Admin-Frontend der Facette, `fs-people admin` das des Programms. `--facet contacts` bleibt als gleichwertige Schreibweise.
- Den Link legt das Paket bzw. der Laden bei der Installation an (Windows: Verknüpfung oder Hardlink). Menüeinträge und Icons gibt es für beide: „FreeSynergy.People“ und „FreeSynergy.Contacts“ (Anzeigename in GUIs immer `FreeSynergy.<Name>`).
- Facetten-Namen sind projektweit reserviert: kein Repo und kein anderes Programm darf `fs-<facette>` heißen.
- Umsetzung: Ein Crate mit `[[bin]] name = "fs-<programm>"` verteilt die Unterbefehle an die vorhandenen Crates (`-app`, `-server`, CLI), die als Bibliotheken bleiben. Muster: Command (je Unterbefehl ein Typ hinter einem Trait) bzw. Facade.
- **Ohne Grafik bauen:** Cargo-Feature `gui` (Standard an). Server und Rechner ohne Bildschirm bauen mit `--no-default-features`; derselbe Name, `fs-x` ohne Argumente gibt dann Hilfe aus. So hängt ein Server nicht an Grafik-Bibliotheken.

## Folgen
- Gilt für neue Arbeit sofort und für den Laden zuerst. Bestehende Programme werden umgestellt, wenn sie ohnehin angefasst werden; Pakete (rpm/deb) und Menüeinträge nur noch auf `fs-<programm>`.

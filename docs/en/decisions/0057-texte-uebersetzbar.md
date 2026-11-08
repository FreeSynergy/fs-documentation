# 0057 – Was ein Mensch liest, ist übersetzbar; die Bibliothek kommt später

Status: akzeptiert (2026-11-07) · ergänzt ADR 0011, 0036, 0053 · Regeln: `conventions/coding.md` §2a · öffentlich: `docs/en/programs/apps/roadmap.md`

## Entscheidung (Nutzer)
„Strings sollten so geschrieben werden, dass sie übersetzbar sind.“ Vorgehen: Erst Trait und Regeln, die Bibliothek nach einer Recherche.

## Vorschlag (Strategie)
1. **Schnittstelle zuerst:** Ein Trait (Strategy) bekommt eine Text-Kennung und benannte Werte und gibt den Satz zurück. Bis zur Entscheidung steht dahinter eine einfache englische Umsetzung.
2. **Engine und Frontend getrennt:** Die Engine liefert Kennungen und Daten, etwa einen Problem-Typ. Den Satz macht das Frontend, das die Sprache des Lesers kennt.
3. **Sprachen als Pakete** über Git (ADR 0036), ohne neue Programmversion. Fehlt ein Text, erscheint er auf Englisch.

## Recherche (2026-11-07, gelesen, nichts ausgeführt)
- **Zwei Aufgaben:** Sätze (MF2 oder Fluent) und Zahlen, Daten, Sortierung (ICU4X `icu`, Unicode-3.0). Beides gehört hinter die Schnittstelle.
- **`mf2`** (`EvanCarroll/rust-mf2`, MIT und Unicode-3.0): MF2 in Rust, Version 3.0.0. Laut eigener Angabe besteht es die Testsuite der Arbeitsgruppe; **nicht geprüft**. Risiko: erst seit 2026-09, ein einziger Autor, keine Sterne, zielt auch auf Leptos.
- **ICU4X:** MF2 noch nicht fertig, Parser in Arbeit (Eintrag 8568, zuletzt 2026-11-03).
- **Fluent** (`fluent-bundle`, Apache-2.0): reif, kein Unicode-Standard; `.ftl`-Dateien lassen sich nicht unverändert in MF2 nutzen. In seinen Abhängigkeiten steht kein ICU4X (`intl_pluralrules`, `intl-memoizer`).

**Entschieden (Nutzer, 2026-11-07): `mf2`,** dazu ICU4X, falls `mf2` es nicht schon nutzt (es hat die Option `datetime-icu`). Zu prüfen: Blinc ist nicht genannt, nur Leptos, Ratatui und Kommandozeile; Kataloge sind eingebaut, Sprachen als Pakete (Punkt 3) brauchen Nachladen; drei Hauptversionen in zwei Wochen, also fest pinnen.
Ursprünglicher Vorschlag: Die Übersetzungsdateien in MF2-Syntax schreiben, das ist der Standard und überlebt jeden Bibliothekswechsel; `mf2` hinter `Words` in einem Probelauf prüfen; ICU4X für Zahlen und Daten. Entscheidung beim Nutzer.

## Offen
- **Bibliothek, Recherche in der Woche ab 2026-11-09:** Unicode MessageFormat 2 ist der Standard und damit erste Wahl (ADR 0014). Eine fertige Rust-Umsetzung ist nicht bestätigt, in ICU4X nur offene Einträge. Project Fluent (`fluent-rs`, Apache-2.0) gibt es in Rust, es ist kein Unicode-Standard, seine Reife ist nicht geprüft.
- Plural, Datum und Zahl je Sprache; andere Schreibrichtung (nicht geprüft, ob Blinc das kann).
- Wer übersetzt: später llama oder die API (ADR 0053).

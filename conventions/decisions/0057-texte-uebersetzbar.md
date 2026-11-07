# 0057 – Was ein Mensch liest, ist übersetzbar; die Bibliothek kommt später

Status: akzeptiert (2026-11-07) · ergänzt ADR 0011, 0036, 0053 · Regeln: `conventions/coding.md` §2a · öffentlich: `docs/en/programs/apps/roadmap.md`

## Entscheidung (Nutzer)
„Strings sollten so geschrieben werden, dass sie übersetzbar sind.“ Vorgehen: Erst Trait und Regeln, die Bibliothek nach einer Recherche.

## Vorschlag (Strategie)
1. **Schnittstelle zuerst:** Ein Trait (Strategy) bekommt eine Text-Kennung und benannte Werte und gibt den Satz zurück. Bis zur Entscheidung steht dahinter eine einfache englische Umsetzung.
2. **Engine und Frontend getrennt:** Die Engine liefert Kennungen und Daten, etwa einen Problem-Typ. Den Satz macht das Frontend, das die Sprache des Lesers kennt.
3. **Sprachen als Pakete** über Git (ADR 0036), ohne neue Programmversion. Fehlt ein Text, erscheint er auf Englisch.

## Offen
- **Bibliothek, Recherche in der Woche ab 2026-11-09:** Unicode MessageFormat 2 ist der Standard und damit erste Wahl (ADR 0014). Eine fertige Rust-Umsetzung ist nicht bestätigt, in ICU4X nur offene Einträge. Project Fluent (`fluent-rs`, Apache-2.0) gibt es in Rust, es ist kein Unicode-Standard, seine Reife ist nicht geprüft.
- Plural, Datum und Zahl je Sprache; andere Schreibrichtung (nicht geprüft, ob Blinc das kann).
- Wer übersetzt: später llama oder die API (ADR 0053).

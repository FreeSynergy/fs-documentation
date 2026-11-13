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

## Umsetzung 2026-11-13
Die Entscheidung (Nutzerentscheid 2026-11-07) bleibt unverändert. Dieser Abschnitt hält fest, wie sie umgesetzt wurde und was von den Vorbehalten oben jetzt geprüft ist.

### Crate und Austausch
- **`fs-components-mf2`** (Repo `fs-components`) setzt den Trait `Words` mit `mf2` um (`Mf2Texts`). `fs-components-words` bleibt abhängigkeitsfrei; der Austausch der Bibliothek geschieht allein über den Trait `Words`, `Mf2Texts` ist eine Umsetzung davon.

### Pin und Lizenz
- `mf2 = "=3.0.0"`, Commit `d598787b23e5c7841dd2a021ae2beffef32303c8`, nur die Features `compile`, `host-std`, `number`.
- Weitere neun `mf2-*`-Crates (MIT) kommen über `Cargo.lock`; die CI muss mit `--locked` bauen.
- Lizenz: `mf2` und `mf2-locale-data` stehen unter `MIT AND Unicode-3.0`. Die Texte beider Lizenzen werden mit dem Binary ausgeliefert. Ein `cargo-deny`-Lizenzgate als eigener CI-Job ist Folgeauftrag.

### Konfig-Orte (XDG)
- Gemeinsame Einstellung: `$XDG_CONFIG_HOME/freesynergy/language`. Überschreibung je Programm: `$XDG_CONFIG_HOME/freesynergy/<programm>/language`.
- Kette: Programm > gemeinsam > `FS_LANG` > `LC_ALL` > `LC_MESSAGES` > `LANGUAGE` (erstes unterstützte Element) > `LANG` > `en`. `C`, `POSIX`, leere und kaputte Werte werden übersprungen.
- Die Einstellung wird atomar geschrieben. Die Sprache ist wählbar im Programm-Menü und in den Einstellungen (Admin-Frontend). Portal-Sprachschlüssel gibt es in V1 nicht.

### Prüfung zur Bauzeit
- Jede Kennung muss in `de` und `en` vorhanden sein, mit gleichen Variablen: als Test `check_pairs` in jedem Crate mit Texten.
- Gate-Skript `contract/texts-check`: findet festkodierte UI-Texte und einsprachige Tabellen.

### ICU4X: in V1 nicht für Plural und Zahlen
- In V1 kein ICU4X für Plural und Zahlen: die CLDR-Daten in `mf2` genügen; ADR 0057 lässt das zu.
- **OFFEN, nötig vor der fs-calendar-Sprachumstellung:** Datum, Zeit und Währung (`:date`, `:time`, `:datetime`, `:currency`) sind in V1 nicht registriert, Calendar und Tasks brauchen sie. Dafür ist ICU4X laut ADR 0057 der vorgesehene Weg.
- Bis dahin werden Datum und Zeit neutral in UTC gezeigt.
- Bidi-Isolation ist aus, sonst erscheinen Kästchen in Schriften ohne die Steuerzeichen. Bei der ersten Rechts-nach-links-Sprache wird sie eingeschaltet.

### Vorbehalte, jetzt geprüft
- **Konformität:** Suite der Arbeitsgruppe (`unicode-org/message-format-wg`, Commit `16372a6`, 462 Fälle): 405 bestanden (87,7 %), 0 fehlgeschlagen, 57 nicht unterstützt. Die 57 sind 25 `:test:*`-Funktionen der Suite und 32 Fälle zu `:currency`, `:date`, `:time`, `:datetime`, die in unserer Konfiguration nicht registriert sind (Datum, Zeit, Währung: siehe OFFEN oben). Unsere Kernfälle (23 plus 5 Syntaxfehler) bestehen zu 100 %. `expParts` wird nicht geprüft. Bericht und Test: [CONFORMANCE.md](https://github.com/FreeSynergy/fs-components/blob/main/crates/fs-components-mf2/CONFORMANCE.md) im Crate `fs-components-mf2` (die Datei liegt ab der Veröffentlichung des Crates in fs-components auf `main`).
- **Fund und Korrektur:** Ohne `.with_numbers` formatiert `mf2` Zahlen neutral (`1.3` statt `1,3`); behoben.
- **Wartungsrisiko:** `mf2` gibt es erst seit 2026-09, mit einem Autor. Das Risiko ist akzeptiert (Strategie). Ein Austausch über den Trait ist möglich (Fork oder ICU4X-MF2, sobald fertig).
- **Kataloge:** jetzt eingebaut (`include_str!`); Nachladen als Sprachpaket später (ADR 0036: die Schnittstelle erlaubt beides).
- **Kosten:** `compile_str` bei der ersten Kompilierung je Nachricht ist ungemessen.

### Migration
826 einsprachige Tabellen (Stand des Gates). Umstellung je Crate zusammen mit der Umbau-Gruppe (erst Texte, dann Tokens), Programme einzeln.

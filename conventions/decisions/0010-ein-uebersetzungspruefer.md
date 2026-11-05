# 0010 – Ein Prüfer für die Übersetzung: `scripts/doc_sync.py`

## Kontext
Für dieselbe Aufgabe (was ist noch nicht übersetzt, was hat deutschen Rest) existierten
neben einander neun Helfer: `temp/find_german_prose.py`, `temp/find_untranslated.py`,
`temp/find_untranslated_ger_lines.py`, `temp/check-translation.sh`, `temp/check-box-width.py`,
`temp/boxgen.py`, `temp/update-progress.py`, `temp/mark-progress.py`,
`temp/translate-index-templates.py` – dazu drei verschiedene
Fortschrittslisten (`translation-progress.md`, `translation-checklist.md`, `component-progress.md`)
und eine Zustandsdatei (`temp/state.md`), die jede Laufanweisung einzeln aufsagte.

Kein Helfer kannte den anderen. Sie widersprachen sich in den Zahlen, weil jede Wortliste
andere zweisprachige Wörter (`in`, `an`, `auf`, `was`) als Befund zählte. Eine Liste, die bei
sauberen Dateien Alarm schlägt, wird nicht abgearbeitet. Beim Abgleich meldete
`find_untranslated.py` vier Dateien, die der neue Prüfer zuerst übersah – umgekehrt fand der
neue Prüfer deutsche Texte in Codebeispielen, die keiner der alten Helfer je betrachtete.

## Entscheidung
**`scripts/doc_sync.py` ist der einzige Prüfer für Übersetzungsstand.** Er wird erweitert,
nicht ersetzt. Alle genannten Helfer sind ersatzlos archiviert (`scripts/_archive/`), ihre
Listen sind stillgelegt.

Ein Lauf:

```
python3 scripts/doc_sync.py --en docs/en --de docs/de \
        --state temp/sync_state.json --list temp/translation-queue.md
```

- `temp/sync_state.json` ist die Wahrheit (Hash je Seite, Status je Datei).
- `temp/translation-queue.md` ist nur die Ansicht davon; sie darf annotiert werden, Notizen und
  Changelog bleiben beim Neu-Erzeugen erhalten.
- Abhaken in der Liste ist Absicht. Erst `--confirm <pfad>` setzt `VERIFIED`; danach bleibt die
  Datei ruhig, bis sich ihr Hash ändert.
- Befunde: `needs_en`, `needs_de`, `copy`, `en_german`, `code_german`, `de_english`, `parity`,
  `rename`, `review`. Neue Befundarten kommen als Abschnitt dazu.
- Reparaturen gehören ins selbe Skript: `--fix-boxes`, `--gen-box`.

Regeln, die die alten Helfer brauchten oder nicht hatten – sie sitzen jetzt im Prüfer:

| Regel | Grund |
|-------|-------|
| Zweisprachige Wörter sind kein Befund | `in`, `an`, `was`, `mit` stehen in korrektem Englisch **und** Deutsch |
| Zitate sind Belege, keine Prosa | deutsche Produkt-Labels in `en/`, englische Spezifikat-Sätze in `de/` (ADR 0002/0006) |
| Bezeichner bleiben deutsch | `vorlage`, `anordbar` sind Variantnamen; Inline-Code und Codeblöcke liefern die Ausnahmewörter |
| Inline-Code darf nicht über Codeblöcke hinweg paaren | `` ` `` + `jsx` + `` ` `` aus ``` ```jsx ``` machte ganze Blöcke Ausnahme-frei und versteckte deutschen Rest |
| Umlaut gilt auch am Wortanfang | `ändern` wurde übersehen, weil nur `Büch`-Muster geprüft waren |
| Deutscher Text in Codebeispielen ist ein Befund | ADR 0002: Code ist englisch – die alten Helfer haben Codezeilen übersprungen |
| Geschlossene Wortklasse wiegt schwer, Substantive leicht | `Müller`, `Ben Klein`, `Tübingen` in Beispieldaten sind keine Übersetzungsarbeit |
| Box-Breiten nur melden, wenn `en/` schlechter ist als `de/` | Breitenfehler existieren meist auf beiden Seiten und sind kein Übersetzungsproblem |

## Folgen
- Neun Helfer nach `scripts/_archive/`, nichts gelöscht. Vergleichsläufe gegen sie waren Teil der
  Abnahme: alle Funde der drei Sprachdetektoren werden jetzt von `doc_sync.py` gemeldet.
- `temp/translation-progress.md` und `temp/translation-checklist.md` sind stillgelegt,
  `temp/translation-queue.md` ist die eine Liste.
- `temp/state.md` verweist auf `doc_sync.py` statt auf Einzelwerkzeuge.
- `todo/translator.md` nennt Befundart, Ebene, Dateien und Status wie in CONVENTIONS §7 gefordert.
- Der Prüfer ist kein CI-Schritt: er meldet 687 offene Übersetzungen, ein harter Exit wäre
  Lärm. `check_components.py` bleibt der CI-Prüfer für Formstandard.
- Bekannte Grenze: englische Prosa in `de/` außerhalb von Zitaten wird nicht gemeldet.

# 0045 – Jedes Thema eine Schnittstelle; Schnittstellen sind Ziele; Hot-Plugins

Status: akzeptiert (2026-11-06) · Form der Plugins: Vorschlag · ergänzt ADR 0014, 0021, 0043

## Entscheidung (Nutzer)
1. **Jedes Thema bekommt eine eigene Schnittstelle**, ab sofort und für alles, was schon gebaut ist: Mail-Client,
   Mail-Server, Matrix, Telegram (auch wenn nicht selbst gehostet), Datenbank, Nachrichten, Dateien, Personen,
   Gruppen … Die Schnittstellen müssen gleich sein, damit man austauschen oder hinzufügen kann. Deshalb sind
   Standards absolut notwendig.
2. **Eine Schnittstelle ist ein Ziel und wächst nicht.** Wachsen hat keinen Endpunkt, ein Ziel schon. Muss sie sich
   ändern, ist das ein **Sprung**, kein Wachsen. Lose zusammenarbeitende Projekte wissen sonst nicht, wann sich was ändert.
3. **Plugins sind immer Hot-Plugins.**
4. Das Backend darf mehr können, als ein Frontend nutzt. Frontends mit eingebauten Filtern sind Mini-Server oder
   Engines (ADR 0021 weitergedacht).

## Vorschlag zur Umsetzung
- Katalog: `docs/en/interfaces/index.md`. Zwei Ebenen: Thema (Nachrichten) und Anbieter (Mail, Matrix, Telegram).
- **Korrektur des Nutzers (2026-11-06), ersetzt „Kern plus optionale Fähigkeiten“:** Wie eine Elternklasse: Jeder Anbieter bietet **alle** Methoden und Attribute. Fehlt einem Anbieter etwas, suchen wir einen Weg, es trotzdem umzusetzen. Geht das wirklich nicht, antwortet er ausdrücklich „nicht möglich“. Erst nachdenken, wie es geht, statt zu sagen, dass es nicht geht. Rust: Trait mit Standardmethode, die `Unsupported` liefert.
- Ablauf: Entwurf → mindestens zwei unabhängige Nutzer der Schnittstelle (bei Anbieter-Schnittstellen: zwei Anbieter) → 1.0 fest → danach nur Sprünge. Korrigiert 2026-11-06: Ein Thema hat nach ADR 0050 nur einen Besitzer, also kann nicht „zwei Umsetzungen“ die Bedingung sein.
- **Hot-Plugins nach dem Vorbild Zentinel** (Hinweis des Nutzers): Viele Schnittstellen sind nur Konfiguration, die geprüft und atomar getauscht wird. Größere sind Agenten: eigene, absturzsichere Prozesse über eine lokale Verbindung, die ihre Fähigkeiten melden. Bei uns mit Cap'n Proto. Zeichnet ein Agent, liefert er eine Szenenbeschreibung. Nicht gemessen, Textmessung ungelöst.
- **Öffentliches Repo `fs-interfaces`: vom Nutzer bestätigt.**
- Das Ziel darf schrittweise genauer werden, solange wir es nicht ganz kennen (Nutzer): erst Ziel festlegen, dann weitersehen.
- **Der Umbau gilt für alles, auch für Fertiges (Nutzer).**

## Folgen
- **ADR 0021** erlaubt Erweiterung ohne Bruch. Das bleibt technisch möglich, aber nach 1.0 ist es nicht mehr der Weg:
  Änderungen kommen als neue Version, mit Übergang, in dem beide angeboten werden.
- Die bestehenden Kerne werden gegen den Katalog geprüft und umgebaut.

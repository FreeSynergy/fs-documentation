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
- Kern plus vorab erklärte optionale Fähigkeiten, damit nicht alle auf den schwächsten Anbieter schrumpfen.
- Ablauf: Entwurf → mindestens zwei unabhängige Nutzer der Schnittstelle (bei Anbieter-Schnittstellen: zwei Anbieter) → 1.0 fest → danach nur Sprünge. Korrigiert 2026-11-06: Ein Thema hat nach ADR 0050 nur einen Besitzer, also kann nicht „zwei Umsetzungen“ die Bedingung sein.
- Hot-Plugin = eigener Prozess mit Cap'n Proto; zeichnet er, liefert er eine Szenenbeschreibung. WASM als Alternative.
  Nicht gemessen, Textmessung ungelöst.
- Öffentliches Repo `fs-interfaces`.

## Folgen
- **ADR 0021** erlaubt Erweiterung ohne Bruch. Das bleibt technisch möglich, aber nach 1.0 ist es nicht mehr der Weg:
  Änderungen kommen als neue Version, mit Übergang, in dem beide angeboten werden.
- Die bestehenden Kerne werden gegen den Katalog geprüft und umgebaut.

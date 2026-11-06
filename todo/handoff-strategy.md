# Übergabe: Strategie-Sitzung (Stand 2026-11-06)

Für eine neue Sitzung, die entscheidet und dokumentiert. Programmieren macht die andere Sitzung (`todo/handoff-programming.md`).

## Zuerst lesen
`docs/en/manifesto.md`, `docs/en/programs/apps/roadmap.md`, `docs/en/interfaces/index.md`, ADR 0045–0054.

## Regeln dieser Rolle
- Der Nutzer entscheidet, wir empfehlen. Jede Entscheidung landet im selben Schritt in der öffentlichen Doku.
- Vergibt ADR-Nummern. Prüft Meldungen der Programmier-Sitzung gegen GitHub und gegen den Wortlaut des Nutzers.
- Nur eigene Dateien committen (`git commit -- <pfade>`). Nach Änderungen an `docs/*/components`: `scripts/gen_component_indexes.py --lang en` und `--lang de`, sonst scheitert das Deployment.
- Keine Übersetzung von selbst starten (ADR 0053). Die Haiku-Stapel sind beendet.

## Offen beim Nutzer
1. **KIs aussperren:** Strategie (ADR 0054). Markierung schützt nur vor ehrlichen KIs.
2. **Mail läuft jetzt** (`support@freesynergy.net`): Schlüssel auf keys.openpgp.org hochladen? GitHub-Adresse bestätigen?
3. **Schlüssel:** Privater Schlüssel und Passphrase liegen zusammen in `~/FreeSynergy-release-key`; getrennt sichern.
4. **Eigenständige Ansichten:** Sollen Galerie, Kanban usw. auch eigene Programme sein? (später)
5. **Export beim Verlassen** (später, ADR 0046).
6. **SignPath:** ab 2026-11-13 erneut fragen (ADR 0051).

## Offen bei uns
- Strata (`Niko1221/Strata`, MIT, C++, lokale Inferenz) und CodeAF (`Agent-Field/CodeAF`, Apache-2.0, Go) analysieren, Zed-Ausgabe ansehen, ACP und MCP lesen.
- Rollen: SKOS lesen, Kunde/Lieferant/Mitarbeiter recherchieren, Format für eigene Rollen.
- Schnittstelle `Trust` über Web of Trust.
- Dateien-Frontends analysieren; `requirements.md` von surveys, streaming, tasks an den Zuschnitt angleichen.
- Manifest ausführlicher und schöner schreiben (Nutzer hat „Anfälle“: immer ergänzen).
- `programs/apps/contact/`, `data/contacts/` umbenennen; `whiteboards/` → `whiteboard/`; `projectmanagement` unter `suites/`.

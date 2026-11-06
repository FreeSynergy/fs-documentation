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
0. **Sprint bis Sonntag 2026-11-08: `todo/sprint.md`.**
1. **KIs aussperren:** vorerst bestätigt (ADR 0054). Offen: ein Mensch, ein Konto, ohne die Anonymität zu verlieren; RLTP erklären und entscheiden.
2. **Schlüssel auf keys.openpgp.org** hochgeladen; Nutzer muss den Bestätigungslink in der Mail an `support@freesynergy.net` klicken. GitHub-Adresse bestätigen?
3. **Schlüssel:** vom Nutzer offline gesichert (bestätigt 2026-11-06), nicht mehr auf dem Rechner.
4. **Vorläufig von der Programmier-Sitzung entschieden, noch nicht bestätigt (Empfehlung: bestätigen):** mehrere Eltern je Gruppe, Zyklen verboten; `files.capnp` vor der Frontend-Analyse; Repo-Name `fs-identity`.
4a. **Rollen-Datenschutz (ADR 0029):** Der Hub prüft nach Typ; wer `Relationship` lesen darf, könnte Rollen-Zuweisungen sehen. Gehört zur Schnittstelle Sharing.
4b. **Eigenständige Ansichten:** Sollen Galerie, Kanban usw. auch eigene Programme sein? (später)
5. **Export beim Verlassen** (später, ADR 0046).
6. **SignPath:** ab 2026-11-13 erneut fragen (ADR 0051).

## Offen bei uns
- Zed-Ausgabe ansehen, ACP und MCP lesen. (Strata und CodeAF sind analysiert, Seite `assistant`.)
- Rollen: SKOS lesen, Kunde/Lieferant/Mitarbeiter recherchieren, Format für eigene Rollen.
- Schnittstelle `Trust`: RLTP weiterlesen (`personhood-predicates`, `trust-layer`), Betreiber-Verweis klären.
- Dateien-Frontends analysieren; `requirements.md` von surveys, streaming, tasks an den Zuschnitt angleichen.
- Manifest ausführlicher und schöner schreiben (Nutzer hat „Anfälle“: immer ergänzen).
- `programs/apps/contact/`, `data/contacts/` umbenennen; `whiteboards/` → `whiteboard/`; `projectmanagement` unter `suites/`.

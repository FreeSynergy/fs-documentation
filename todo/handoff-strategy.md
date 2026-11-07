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
2. **Schlüssel auf keys.openpgp.org:** Nutzer hat bestätigt (2026-11-07). GitHub-Adresse bestätigen?
3. **Schlüssel ersetzt (2026-11-07):** neu `16A4A3EE563AEF51FCF0C55DED7B57C4A1904342`, vom Nutzer erzeugt, auf keys.openpgp.org bestätigt, in `fs-release` und `releases.md`. Alte Secrets gelöscht, alter Entwurf gelöscht. **Offen:** Widerruf des alten (`.rev` ließ sich nicht importieren). Neue Secrets erst, wenn ein Release ansteht.
4. **Bestätigt (2026-11-07):** mehrere Eltern je Gruppe, Zyklen verboten; `files.capnp` vor der Frontend-Analyse; Repo-Name `fs-identity`. Einseitiges Folgen: ADR 0056.
4a. **Rollen-Datenschutz (ADR 0029):** Muss geschlossen werden (Nutzer „ja“, 2026-11-07). Der Hub prüft nach Typ; wer `Relationship` lesen darf, könnte Rollen-Zuweisungen sehen. Gehört zur Schnittstelle Sharing; bis dahin bekommt kein Programm dieses Leserecht.
4c. **Kontakte sind Profile (ADR 0058):** Idee des Nutzers; Ausgestaltung zu bestätigen. `fs-people` bleibt. Keine Umbauten im Sprint.
4d. **Umfrage weiterreichen:** Prozent plus Mindestzahl; die Eltern-Gruppe legt die Regel fest, die Kindgruppe darf nur strenger sein (Nutzer). Recherche offen (LiquidFeedback Policies, EU-Bürgerinitiative, Consul nicht bestätigt).
4b. **Eigenständige Ansichten:** Sollen Galerie, Kanban usw. auch eigene Programme sein? (später)
5. **Export beim Verlassen** (später, ADR 0046).
6. **SignPath:** ab 2026-11-13 erneut fragen (ADR 0051).

## Offen bei uns
- **P2P (ADR 0059):** Richtung vom Nutzer: jeder Client ein Knoten, iroh als Kandidat. Probelauf und offene Punkte nach dem Sprint besprechen.
- Übersetzungs-Bibliothek recherchieren (Woche ab 2026-11-09, ADR 0057): MessageFormat 2 in Rust oder Fluent; Schreibrichtung in Blinc.
- Strata, CodeAF, Zed, ACP, MCP sind gelesen (Seite `assistant`); zwei Entscheidungen beim Nutzer.
- Rollen: Forschung fertig (`temp/research/roles-standards.md`), fünf Entscheidungen beim Nutzer.
- Schnittstelle `Trust`: RLTP weiterlesen (`personhood-predicates`, `trust-layer`), Betreiber-Verweis klären.
- Manifest ausführlicher und schöner schreiben (Nutzer hat „Anfälle“: immer ergänzen).

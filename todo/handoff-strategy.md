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
2. **Schlüssel auf keys.openpgp.org:** bestätigt (2026-11-07).
3. **Schlüssel ersetzt (2026-11-07):** neu `16A4A3EE563AEF51FCF0C55DED7B57C4A1904342`, vom Nutzer erzeugt, auf keys.openpgp.org bestätigt, in `fs-release` und `releases.md`. Alte Secrets gelöscht, alter Entwurf gelöscht. Alter Schlüssel widerrufen (2026-11-07), Widerruf auf keys.openpgp.org (Signatur 0x20 geprüft) und in `fs-release`. Neue Secrets erst, wenn ein Release ansteht.
4. **Bestätigt (2026-11-07):** mehrere Eltern je Gruppe, Zyklen verboten; `files.capnp` vor der Frontend-Analyse; Repo-Name `fs-identity`. Einseitiges Folgen: ADR 0056.
4a. **Rollen-Datenschutz (ADR 0029):** Muss geschlossen werden (Nutzer „ja“, 2026-11-07). Der Hub prüft nach Typ; wer `Relationship` lesen darf, könnte Rollen-Zuweisungen sehen. Gehört zur Schnittstelle Sharing; bis dahin bekommt kein Programm dieses Leserecht.
4c. **Kontakte sind Profile (ADR 0058):** Idee des Nutzers; Ausgestaltung zu bestätigen. `fs-people` bleibt. Keine Umbauten im Sprint.
4d. **Umfrage weiterreichen:** Prozent plus Mindestzahl; die Eltern-Gruppe legt die Regel fest, die Kindgruppe darf nur strenger sein (Nutzer). Recherche offen (LiquidFeedback Policies, EU-Bürgerinitiative, Consul nicht bestätigt).
4b. **Eigenständige Ansichten:** ja, als eigene Starter ohne eigene Daten (Nutzer, 2026-11-07).
5. **Export beim Verlassen:** einmal fragen, mit „merken“ (Nutzer, 2026-11-07, ADR 0046).
5a. **Gruppenbeitritt:** die Gruppe legt es fest: Einladung, offen oder auf Anfrage; Abstimmung über `fs-surveys` möglich (Nutzer, 2026-11-07).
6. **SignPath:** ab 2026-11-13 erneut fragen (ADR 0051).

## Offen bei uns
- **Erster Punkt nach dem Sprint: Umbenennung (ADR 0060).** `fs-store` → `fs-objects` in allen 18 Repos, danach wird `fs-store` der Laden. Der Launcher liegt bis dahin nur lokal unter `/srv/FreeSynergy/fs-launcher` (5 Commits, 13 Tests, nicht gepusht).
- **Launcher und Pakete online (Nutzer, 2026-11-07, besprechen):** ADR 0036, Abschnitt „Ergänzung des Nutzers“. Erster Punkt für die Planung nach dem Sprint.
- **Rollen als volle IRIs sind schon auf `main`** (`fs-people` v0.4.0/v0.5.0). Geprüft 2026-11-07: Es gibt noch keine Implementierung von `AiMarking`, und kein Produktcode vergleicht die Kurz-ID `ai`. **Regel für jeden künftigen Host** (Brücke `fs-people` → `fs-groups` `AiMarking` bzw. Wächter `SenderLookup`): nur über `is_ai_role()` entscheiden, mit Test für Kurz-ID und volle IRI. Dazu: `anonymousOpen` in `fs-surveys` braucht eine Person vom Host, sonst gilt der Teilnehmer als KI.
- **Nach dem Sprint (Nutzer, 2026-11-07): Pause, erst gemeinsam planen.** Ab Sonntag, 2026-11-08, 18:00 ruhen die Threads, bis der Plan steht. Kandidaten: Funde aus dem Handtest, automatische Prüfung bei jedem Push, Probeläufe `mf2` und iroh, Kontakte als Profile (ADR 0058), quadratische Listen in Kalender und Aufgaben, Verbindung Kalender–Aufgaben über Vertrag.
- **Automatische Prüfung bei jedem Push (Nutzer, 2026-11-07, ja):** gemeinsamer Ablauf in `fs-release`, ohne Secrets: fmt, clippy, Tests, `check_rust_rules.py`.
- **API-Guthaben:** erst nach sieben Tagen im Paket verknüpfbar (Nutzer am 2026-11-07: „erst der 2. Tag“). Danach schreibt die Strategie das Skript für Agenten ohne Rücksprache.
- **P2P (ADR 0059):** Richtung vom Nutzer: jeder Client ein Knoten, iroh als Kandidat. Probelauf und offene Punkte nach dem Sprint besprechen.
- Übersetzungs-Bibliothek recherchieren (Woche ab 2026-11-09, ADR 0057): MessageFormat 2 in Rust oder Fluent; Schreibrichtung in Blinc.
- Strata, CodeAF, Zed, ACP, MCP sind gelesen (Seite `assistant`); zwei Entscheidungen beim Nutzer.
- Rollen: Forschung fertig (`temp/research/roles-standards.md`), fünf Entscheidungen beim Nutzer.
- Schnittstelle `Trust`: RLTP weiterlesen (`personhood-predicates`, `trust-layer`), Betreiber-Verweis klären.
- Manifest ausführlicher und schöner schreiben (Nutzer hat „Anfälle“: immer ergänzen).

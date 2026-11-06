# Sprint bis Sonntag, 2026-11-08 (Stand 2026-11-06)

**Ziel:** So viel wie möglich bauen, aber nichts, was wir wegwerfen müssten. Nur Besprochenes: `docs/en/programs/apps/roadmap.md`,
`docs/en/interfaces/index.md`, ADR 0045–0054. Keine neuen Ideen, keine neuen Standards ohne Rückfrage.

**Annahme zum Ende:** Alles Wichtige ist bis Samstagabend gepusht. Danach läuft es weiter, aber es wird nach jedem Schritt gepusht.

## Start für jeden Thread
Einzeilig einfügen, N ersetzen:

```text
/loop Du bist Thread N im Sprint. Lies /srv/FreeSynergy/fs-documentation/todo/sprint.md, dann arbeite deine Liste der Reihe nach ab, auch mit vielen Agenten, und nimm nach jedem fertigen Punkt den nächsten.
```

## Die Threads

| Thread | Aufgabe | Schreibt in | Wartet auf |
|--------|---------|-------------|------------|
| 1 (`freesynergy-65`) | Components, Wiki-Workbench | `fs-components`, `fs-wiki` | nichts |
| 2 (`freesynergy-7c`) | `fs-messenger` mit KI-Teilnehmern und Notaus | `fs-messenger` (neu), `messenger.capnp` | nichts |
| 3 (`freesynergy-24`) | Schnittstellen in Betrieb: RPC, `subscribe`, MCP, CLI | Server- und CLI-Crates aller Programme, `fs-capnpc`, `fs-hub`, `fs-store` | nichts |
| 4 (`freesynergy-f9`) | GUIs der fertigen Kerne auf Blinc | Frontend-Crates der Programme | ersten Tag von `fs-components` |
| 5 (`freesynergy-64`) | Neue Kerne: Umfragen, Verlauf, Ressourcen | `fs-surveys`, `fs-history`, `fs-resources` (neu) | nichts |
| Strategie (`freesynergy-8b`) | Entscheidungen, ADRs, öffentliche Doku, Recherche, Meldungen prüfen | `fs-documentation` | Meldungen |

### Thread 1: Components und Wiki
1. `fs-components` fertig committen und taggen; die Wiki-Workbench auf Blinc so weit, dass sie `fs-documentation` zeigt und bearbeitet.
2. Fehler der Markdown-Rundreise in `fs-text` beheben (`fs-wiki/DESIGN.md`).
3. Gemeinsame Components aus `docs/en/components/planned.md`, Abschnitt „Build first“. Früh taggen, Thread 4 wartet darauf.
4. `charts` (Vega-Lite-Teilmenge, `docs/en/components/charts.md`).
5. Chat-Components `message-list`, `message-composer`, `llm-chat`, `agent-tree`, `tool-call`; Muster aus der Analyse auf der Seite `assistant`.

### Thread 2: Messenger
1. Vertrag `messages` schärfen: Agenten als Absender, sichtbare Werkzeug-Aufrufe, Verweis einer Nachricht auf eine Aufgabe (ADR 0054).
2. Kern `fs-messenger` nach ADR 0018: eigenes Modell auf `fs-store`, nur verschlüsselt.
3. Anbieter in dieser Reihenfolge, jeder gegen einen echten Server geprüft: Mail (JMAP, IMAP, SMTP, rPGP), Matrix (`matrix-sdk`, `tuwunel`), KI-Modell (llama.cpp-API, Anthropic-API).
4. ADR 0054 umsetzen: KI nur per Einladung (Profil anlegen), ohne Freigabe keine Handlung; Bremse (Zerstörendes und Handeln im Namen der Person fragt immer); Notaus in der Engine, außerhalb der Reichweite der KI, ohne Netz, im Zweifel zu; wer ihn ziehen darf, ist eine Berechtigung.
4a. Vertrag `messages` (erledigt, v0.16.0; solange er Entwurf ist, darf er umnummeriert werden, Strategie 2026-11-06: Ordinal 0 ist bei `Encryption` jetzt `unknown`, damit ungesetzt nie „verschlüsselt“ heißt) (Ergebnis der Analyse ACP und MCP, Seite `assistant`, `temp/research/acp-mcp-zed.md`): `ToolCall` mit `risk` (Standard `unknown`, setzt die Engine), Ergebnis, Details, Optionen; `MessageAction` „entscheiden“ nur vom Gerät der Person; Ereignisse für Änderung am Werkzeug-Aufruf und Textstücke; Nachricht mit `reasoning` und Medientyp des Textes; `jobRef` in `MessageSummary`; Stopp und Verbrauch an `Conversation`. Bei MCP beweist ein `accept` keine Person: Die Bremse sitzt in der Engine.
5. **Nicht bauen:** Bewertung und Stufen über Dritte (Vertrauensbasis offen), Telegram, eigener Mailserver.

### Thread 3: Schnittstellen in Betrieb
1. Cap'n-Proto-Server für alle Kerne (tasks zuerst, dann people, calendar, groups, files, maps, wiki); alles, was der Vertrag nennt, statt stiller Lücken.
2. `subscribe` überall.
3. MCP-Werkzeuge aus den Verträgen erzeugen (ADR 0021), nicht von Hand.
4. CLI je Programm als zweiter Nutzer der Schnittstelle. Fehler am Vertrag beheben, solange er Entwurf ist; nichts wird 1.0.
4a. `fs-store` (Besitzer seit 2026-11-06, nur anhängen): Log eines Objekts löschen können (ADR 0029); große Originale einmal ablegen und im Log nur referenzieren; `Store` sagt, ob er verschlüsselt ist, und hat eine Identität.
5. Hub: alle Programme tatsächlich verbinden, mit einem Test über mehrere Programme hinweg. Kein Programm bekommt Leserecht auf den Typ `Relationship` (Rollen-Datenschutz, offen).

### Thread 4: GUIs
Bis der erste Tag von `fs-components` da ist: Blinc-Grundgerüst, gemeinsame Anwendungshülle, Frontend-Struktur nach ADR 0011ff. und 0037. Dann der Reihe nach:
1. `fs-people`
2. `fs-calendar`
3. `fs-tasks`, mit Kanban als Ansicht (ADR 0049)
4. `fs-files`, Workbench `file-manager`; Vertrag ist vorläufig
5. `fs-maps`

Programmspezifische Workbenches darf Thread 4 in `fs-components` ergänzen, Gemeinsames gehört Thread 1. Blinc-Fehler per PR oder Eintrag in `todo/upstream.md`; nicht umgehen, ohne es zu notieren. Erst läuft ein Programm wirklich, dann kommt das nächste.

### Thread 5: Neue Kerne
Jeweils erst Vertrag in `fs-interfaces`, dann Kern ohne GUI, mit eigener `DESIGN.md`:
1. `fs-surveys` (`docs/en/programs/apps/surveys/`, `temp/research/surveys-landscape.md`); erweiterbare Umfrage über Gruppen; Entscheidungen als Objekte, die mit Aufgaben verknüpft sind.
2. `fs-history` als Beobachter des Aktivitätsprotokolls (`history/index.md`); falls es keine eigenen Daten braucht, melden und als Ansicht bauen.
3. `fs-resources` (`resources/index.md`)
4. Erst wenn das steht: `fs-whiteboard`, dann `fs-streaming`, jeweils nur der Kern nach `design.md`.

### Strategie
Rollen (SKOS, Kunde, Lieferant, Mitarbeiter); Zed, ACP, MCP lesen; Datei-Frontends analysieren; `requirements.md` von surveys, streaming, tasks angleichen; Umbenennungen der Doku; Meldungen der Threads gegen GitHub prüfen und Doku nachziehen.

## Regeln für alle
**Qualität**
- Vor jedem Tag: `cargo fmt --check`, clippy `-D warnings` (pedantic), Tests, `scripts/check_rust_rules.py <repo>` = 0 Fehler, frischer Klon nach `/tmp` baut.
- **Vor jedem Tag prüft ein zweiter Agent, der den Code nicht geschrieben hat** (`/code-review high`). Bestätigte Fehler zuerst beheben.
- Fertig heißt: läuft und ist getestet. Was fehlt, sagt ausdrücklich `Unsupported` und steht in der `DESIGN.md`. Keine Attrappen, keine Tests, die nur Attrappen prüfen.
- Grundsätze bleiben: nichts kopieren, 100 % Rust, Muster und Schnittstellen (ADR 0043), ein Standard, ein Programm (ADR 0050).

**Agenten**
- Du planst und prüfst; Agenten setzen nach fertiger Vorgabe um. Nur Unabhängiges parallel, je Agent ein eigener `worktree` oder eigenes Repo.
- Früh und oft committen und pushen. Abbrüche verlieren sonst alles.

**Zusammenarbeit**
- Jeder schreibt nur in seine Repos und Crates. Andere per Nachricht (`ListAgents`, `SendMessage`) um Änderungen bitten.
- `fs-interfaces`: nur die eigene Schema-Datei ändern, `git pull --rebase`, dann die nächste freie Version taggen. Kleine, häufige Tags.
- Abhängigkeiten nur über Git-Tags (coding.md §8).
- `fs-documentation` ist ein geteilter Arbeitsbaum: nur `git commit -- <pfade>`, **kein `--autostash`, kein `git stash`, kein `git reset`, kein `checkout` fremder Dateien.** Wer schreibt, nimmt einen eigenen `git worktree` und pusht von dort; ungepushte Commits im gemeinsamen Baum sind nicht sicher. Tests gegen die Docs nur auf einer Kopie.
- **Nicht warten.** Offene Frage: die wahrscheinlich richtige Antwort nehmen, als vorläufig markieren, an die Strategie melden, weitermachen. Keine ADR-Nummern selbst vergeben.

**Rechner**
- 32 Kerne, 124 GB: Builds mit `-j 4`, höchstens 3 gleichzeitig je Thread (Last lag bei 65). **Frische Klone und Prüfungen nicht in `/tmp`** (nur 50 GB, voll führt zu scheinbar zufälligen Testfehlern), sondern unter `/srv/FreeSynergy/.scratch/<thread>-<name>/`, und danach löschen. llama.cpp bleibt aus und wird nicht gestartet.
- `scripts/clean_rust.py` nur für das eigene Repo, **niemals `--all`**, sonst löscht es die Builds der anderen.

**Nicht tun**
- Keine Releases und kein Signieren: Der Schlüssel ist offline. Keine Übersetzung (ADR 0053). Keine Veröffentlichung auf crates.io ohne Rückfrage. Nur zu GitHub pushen, nichts sonst nach außen.

**Stand melden**
- Nach jedem fertigen Punkt eine Zeile in `todo/handoff-programming.md` (nur diese Datei und `DESIGN.md` im Repo; öffentliche Doku macht die Strategie), und kurz an `freesynergy-8b`.

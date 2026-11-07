# Sprint bis Sonntag, 2026-11-08, 18:00 (Stand 2026-11-07)

**Ziel:** So viel wie möglich bauen, aber nichts, was wir wegwerfen müssten. Nur Besprochenes: `docs/en/programs/apps/roadmap.md`,
`docs/en/interfaces/index.md`, ADR 0045–0054. Keine neuen Ideen, keine neuen Standards ohne Rückfrage.

**Ende (Nutzer, 2026-11-07): Sonntag, 2026-11-08, 18:00 Uhr. Danach ruhen alle Threads, bis ein neuer Plan freigegeben ist.** Vorher alles pushen, offene Arbeit in die `DESIGN.md` und eine Zeile in `todo/handoff-programming.md`. Es wird nach jedem Schritt gepusht.

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
5a. Trait für Texte (ADR 0057), nach deinen laufenden Prüfungen: Muster Strategy, Text-Kennung plus benannte Werte ergibt einen Satz, einfache englische Umsetzung dahinter, keine Bibliothek. Mit Thread 4 abstimmen, er nutzt `words.rs` in den Apps. Vorhandene `labels.rs` nicht in einem Durchlauf umbauen.
5. Chat-Components `message-list`, `message-composer`, `llm-chat`, `agent-tree`, `tool-call`; Muster aus der Analyse auf der Seite `assistant`.

### Thread 2: Messenger
1. Vertrag `messages` schärfen: Agenten als Absender, sichtbare Werkzeug-Aufrufe, Verweis einer Nachricht auf eine Aufgabe (ADR 0054).
2. Kern `fs-messenger` nach ADR 0018: eigenes Modell auf `fs-store`, nur verschlüsselt.
3. Anbieter in dieser Reihenfolge, jeder gegen einen echten Server geprüft: Mail (JMAP, IMAP, SMTP, rPGP), Matrix (`matrix-sdk`, `tuwunel`), KI-Modell (llama.cpp-API, Anthropic-API).
4. ADR 0054 umsetzen: KI nur per Einladung (Profil anlegen), ohne Freigabe keine Handlung; Bremse (Zerstörendes und Handeln im Namen der Person fragt immer); Notaus in der Engine, außerhalb der Reichweite der KI, ohne Netz, im Zweifel zu; wer ihn ziehen darf, ist eine Berechtigung.
4a. Vertrag `messages` (erledigt, v0.16.0; solange er Entwurf ist, darf er umnummeriert werden, Strategie 2026-11-06: Ordinal 0 ist bei `Encryption` jetzt `unknown`, damit ungesetzt nie „verschlüsselt“ heißt) (Ergebnis der Analyse ACP und MCP, Seite `assistant`, `temp/research/acp-mcp-zed.md`): `ToolCall` mit `risk` (Standard `unknown`, setzt die Engine), Ergebnis, Details, Optionen; `MessageAction` „entscheiden“ nur vom Gerät der Person; Ereignisse für Änderung am Werkzeug-Aufruf und Textstücke; Nachricht mit `reasoning` und Medientyp des Textes; `jobRef` in `MessageSummary`; Stopp und Verbrauch an `Conversation`. Bei MCP beweist ein `accept` keine Person: Die Bremse sitzt in der Engine.
4b. **`origin/ai` nicht so auf `main` mergen:** Die Frage „Encrypted only meets a model“ in der `DESIGN.md` ist entschieden, aber anders als dort vorgeschlagen: kein Weg an `gate.rs` vorbei, kein neuer Vertragswert, `PastTheGate` fliegt raus. Die KI ist ein Teilnehmer mit eigenem Schlüssel; ein Programm hält ihn und spricht dahinter mit dem Modell. Transport (Nutzer, 2026-11-07): **zuerst Matrix, MLS später**; das Programm der KI hat ein normales Matrix-Konto. **Tests gegen echte Modelle nicht im Sprint (Nutzer, 2026-11-07):** erst Sonntagabend oder Montag, dann schaltet der Nutzer llama ein; llama.cpp bleibt bis dahin aus, kein Anthropic-Aufruf. Bis dahin „nicht gegen einen echten Server geprüft“ in die `DESIGN.md`.
4d. **Offene Punkte aus `guard` (Strategie, 2026-11-07, vorläufig; Open point 12):** (1) Ja: keine Freigabe irgendeiner Klasse im Programm = `Deny`; mit Freigabe fragen Zerstörendes, Handeln im Namen, `unknown` und Gekennzeichnetes je Aufruf; `allow-class` entfällt. (2) Keine neue Taxonomie: `Gate::check` ohne Objekt zählt als gekennzeichnet, also `Ask`, nie `Allow`; wer `Allow` will, ruft `check_object`; Listen prüft die Werkzeugschicht je Objekt (gilt auch für MCP, Thread 3). (3) Regel statt Liste: Namen auf `secret`, `token`, `key`, `password`, `passphrase`, `proof`, `credential` sind `NeverForAi`, später zusätzlich die Marken aus den Verträgen. (4) `readsSensitive` ans Ende von `ToolCallRisk`, `unknown` bleibt 0; `program` und `goesTo` anhängen. **`goesTo` kommt aus dem, was die Engine über Teilnehmer und Betreiber weiß, nie von der KI;** weiß sie es nicht, steht dort „unbekannt“.
4c. ADR 0054, Abschnitt „KIs in Unterhaltungen“ (Nutzer, 2026-11-06), noch nicht im Code: KI mit eigenem Schlüssel wie jeder Teilnehmer, `gate.rs` bleibt ohne Ausnahme. Hinweis vor dem Eintritt; alle müssen zustimmen, sonst bleibt sie draußen; wer später kommt, nimmt sie an oder bleibt draußen; Zustimmung zurückgezogen: KI muss hinaus; kein Verlauf von vor dem Eintritt; keine Ausnahme für lokale KIs. Fremde Matrix-Programme können wir nicht zwingen: warnen und Verlassen anbieten.
5. **Nicht bauen:** Bewertung und Stufen über Dritte (Vertrauensbasis offen), Telegram, eigener Mailserver.

### Thread 3: Schnittstellen in Betrieb
1. Cap'n-Proto-Server für alle Kerne (tasks zuerst, dann people, calendar, groups, files, maps, wiki); alles, was der Vertrag nennt, statt stiller Lücken.
2. `subscribe` überall.
3. MCP-Werkzeuge aus den Verträgen erzeugen (ADR 0021, Erweiterung vom Nutzer freigegeben 2026-11-07), nicht von Hand. Risikomarken, Ereignisse und Dateien als Ressourcen, Ausschluss für Geheimnisse. Lesen ist nicht harmlos (ADR 0054).
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

**Auch fällig (ADR 0018, 0043):** Sobald der Server eines Programms läuft, spricht seine App über Cap'n Proto statt direkt mit dem Kern. `fs-calendar-app` darf nicht mehr von `fs-tasks-core` abhängen.

Programmspezifische Workbenches darf Thread 4 in `fs-components` ergänzen, Gemeinsames gehört Thread 1. Blinc-Fehler per PR oder Eintrag in `todo/upstream.md`; nicht umgehen, ohne es zu notieren. Erst läuft ein Programm wirklich, dann kommt das nächste.

### Thread 5: Neue Kerne
Jeweils erst Vertrag in `fs-interfaces`, dann Kern ohne GUI, mit eigener `DESIGN.md`:
1. `fs-surveys` (`docs/en/programs/apps/surveys/`, `temp/research/surveys-landscape.md`); erweiterbare Umfrage über Gruppen; Entscheidungen als Objekte, die mit Aufgaben verknüpft sind.
2. `fs-history` als Beobachter des Aktivitätsprotokolls (`history/index.md`); falls es keine eigenen Daten braucht, melden und als Ansicht bauen.
3. `fs-resources` (`resources/index.md`)
4. Erst wenn das steht: `fs-whiteboard`, dann `fs-streaming`, jeweils nur der Kern nach `design.md`.
5. `fs-people`: Rollen wie in `docs/en/interfaces/roles.md`, Abschnitt „Decided“ (Nutzer, 2026-11-07): innen Cap'n Proto, außen JSON-LD, Adresse `https://freesynergy.net/ns/roles/`, Karten `org`, Rollen Lead, Interessent, Kunde. Mit Thread 3 abstimmen, er arbeitet in `fs-people-server`.
6. `fs-groups`: Folgen nach ADR 0056, Abschnitt „Einseitig folgen“: Wer Zugriff erlaubt, liefert (Repository andersherum, kein Baum); der andere bekommt eine Einladung (AS2 `Invite`, Vorschlag) und sein Server trägt die Quelle ein, ohne Bestätigung, entfernen kann er sie. Gegenseitig erlaubt. Nur eigene Rechte, nie mehr als man hat. Weitergeben nur mit ausdrücklicher Erlaubnis der Quelle. „Gehört zu“ mit Eltern bleibt daneben. Erst Muster und Vertrag `groups.capnp`, mit Thread 3 abstimmen.
7. `fs-surveys`: KI als Teilnehmer nur, wenn der Ersteller es je Umfrage erlaubt; ihre Antwort wird immer getrennt gezählt und getrennt angezeigt (Nutzer, 2026-11-07). Kein MCP-Werkzeug dafür, bis das steht.

### Strategie
Rollen (SKOS, Kunde, Lieferant, Mitarbeiter); Zed, ACP, MCP lesen; Datei-Frontends analysieren; `requirements.md` von surveys, streaming, tasks angleichen; Umbenennungen der Doku; Meldungen der Threads gegen GitHub prüfen und Doku nachziehen.

## Nach dem Absturz vom 2026-11-07, 08:59
Alle Sitzungen sind beendet, Arbeit liegt noch in den Worktrees. Zuerst den eigenen Stand lesen: `git status` in `.wt-*`, `.scratch/t*`, offene Branches; `backup/*` auf GitHub ist eine Sicherung ohne Merge. Nicht committet: `.wt-fs-maps-server` (9), `.wt-fs-tasks` (1), `.wt-msg-v4` (30, Branch nur lokal), `.scratch/t5-surveys` (5), ein Agent-Worktree in `fs-wiki` (15).

## Regeln für alle
**Reihenfolge bei jedem neuen Stück Code (Nutzer, 2026-11-07, ADR 0043)**
1. **Muster zuerst:** Eines aus `conventions/coding.md` §2 aussuchen und in einem Satz begründen. Passt keines, nicht eines erfinden, sondern der Strategie melden.
2. **Dann der Trait:** Erst die Schnittstelle schreiben, ohne Umsetzung, passend zum Vertrag in `fs-interfaces`. Zwischen Programmen immer Cap'n Proto, nie der Kern eines anderen Programms.
3. **Dann Tests gegen den Trait,** danach erst die Umsetzung.
4. Muster, Trait und Grund stehen im Modul-Kopf und in der Muster-Karte der `DESIGN.md`. Das Wort `Pattern:` allein ist kein Nachweis: Die Prüfung vor dem Tag vergleicht das genannte Muster mit dem Code.
Kleine Korrekturen in bestehendem Code brauchen keinen neuen Trait, aber das Muster der Datei bleibt.

**Threads auf Sonnet (ab 2026-11-07):** Der Thread schreibt selbst oder über Sonnet-Agenten. Die Prüfung vor jedem Tag macht ein eigener Agent mit `model: opus`, der den Code nicht geschrieben hat.

**Wiederaufnahme:** Zuerst `git pull` im eigenen Repo, dann die offenen Branches und `DESIGN.md` lesen und dort weitermachen. Nichts neu anfangen, was schon auf einem Branch liegt.

**Qualität**
- Vor jedem Tag, im frischen Klon unter `.scratch`: `/srv/FreeSynergy/fs-documentation/scripts/gates.sh <klon> && git push ... && git tag ...`. **`set -e` wirkt in Tool-Aufrufen nicht** (nachgestellt); nur das Skript mit `&&` gibt einen echten Exit-Code.
- **Vor jedem Tag prüft ein zweiter Agent, der den Code nicht geschrieben hat** (`/code-review high`). Bestätigte Fehler zuerst beheben.
- Fertig heißt: läuft und ist getestet. Was fehlt, sagt ausdrücklich `Unsupported` und steht in der `DESIGN.md`. Keine Attrappen, keine Tests, die nur Attrappen prüfen.
- Grundsätze bleiben: nichts kopieren, 100 % Rust, Muster und Schnittstellen (ADR 0043), ein Standard, ein Programm (ADR 0050).

**Agenten**
- **Modelle (Nutzer, 2026-11-06): Sonnet schreibt, Opus plant und prüft.** Agenten mit `model: sonnet` starten; die unabhängige Prüfung bleibt ein eigener Agent.
- Du planst und prüfst; Agenten setzen nach fertiger Vorgabe um. Nur Unabhängiges parallel, je Agent ein eigener `worktree` oder eigenes Repo.
- Früh und oft committen und pushen. Abbrüche verlieren sonst alles.

**Zusammenarbeit**
- Jeder schreibt nur in seine Repos und Crates. Andere per Nachricht (`ListAgents`, `SendMessage`) um Änderungen bitten.
- `fs-interfaces`: nur die eigene Schema-Datei ändern, `git pull --rebase`, dann die nächste freie Version taggen. Kleine, häufige Tags.
- Abhängigkeiten nur über Git-Tags (coding.md §8).
- `fs-documentation` ist ein geteilter Arbeitsbaum: nur `git commit -- <pfade>`, **kein `--autostash`, kein `git stash`, kein `git reset`, kein `checkout` fremder Dateien.** Wer schreibt, nimmt einen eigenen `git worktree` und pusht von dort; ungepushte Commits im gemeinsamen Baum sind nicht sicher. Tests gegen die Docs nur auf einer Kopie.
- **Nicht warten.** Offene Frage: die wahrscheinlich richtige Antwort nehmen, als vorläufig markieren, an die Strategie melden, weitermachen. Keine ADR-Nummern selbst vergeben.

**Rechner**
- **Jeder Build, jeder Test und jede Probe läuft über `scripts/limited.sh`** (eigene Speichergrenze, Standard 32 GB). Am 2026-11-07 um 08:59 nahm sich eine Prüf-Probe aus `thread3-cal-review6` 107 GB; der Kernel beendete Zed und damit alle Sitzungen. Geprüft: Mit der Grenze stirbt nur der Befehl selbst. `gates.sh` nutzt es schon. Proben mit Grenzen wie `usize::MAX` niemals ohne.
- **Höchstens ein Build je Thread gleichzeitig,** außer die Strategie gibt mehr frei.
- 32 Kerne, 124 GB: Builds mit `-j 4`, höchstens 3 gleichzeitig je Thread (Last lag bei 65). **Frische Klone und Prüfungen nicht in `/tmp`** (nur 50 GB, voll führt zu scheinbar zufälligen Testfehlern), sondern unter `/srv/FreeSynergy/.scratch/<thread>-<name>/`, und danach löschen. llama.cpp bleibt aus und wird nicht gestartet.
- `scripts/clean_rust.py` nur für das eigene Repo, **niemals `--all`**, sonst löscht es die Builds der anderen.

**Texte (Nutzer, 2026-11-07):** Was ein Mensch liest, muss übersetzbar bleiben: `coding.md` §2a. Vorhandenes nur ändern, wenn die Datei ohnehin angefasst wird. Es wird noch nichts übersetzt (ADR 0053).

**Nicht tun**
- **Keine Geheimnisse für Menschen erzeugen oder lesen (ADR 0054):** Passwörter, Passphrasen, private Schlüssel. Du schreibst die Anleitung, der Mensch führt sie aus. Testwerte in Tests sind erlaubt.
- **Releases nur als Entwürfe (Nutzer, 2026-11-07):** signiert mit dem neuen Schlüssel `16A4A3EE…4342`. Die Secrets setzt nur der Nutzer selbst; kein Agent liest, setzt oder gibt sie aus, und kein Workflow schreibt sie in ein Log. Keine Übersetzung (ADR 0053). Keine Veröffentlichung auf crates.io ohne Rückfrage. Nur zu GitHub pushen, nichts sonst nach außen.

**Stand melden**
- Nach jedem fertigen Punkt eine Zeile in `todo/handoff-programming.md` (nur diese Datei und `DESIGN.md` im Repo; öffentliche Doku macht die Strategie), und kurz an die Strategie-Sitzung (Name über `ListAgents`, Namen ändern sich beim Neustart; zurzeit `freesynergy-dd`).

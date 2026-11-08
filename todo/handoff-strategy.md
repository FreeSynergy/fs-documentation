# Übergabe: Strategie-Sitzung (Stand 2026-11-08, Sprint-Ende)

## Runde 3 geplant (2026-11-09)
- **ADR 0066:** Grundtypen → Datentypen → Typbeschreibung vom Backend (Felder, Befehle) → Components je Grundtyp (Eingabe, Anzeige, kompakt, Zelle) → vier Frontends je Programm: Admin (erzeugt), Einfach, Apple-Stil, Windows-Stil (nach Maß, eigene Icons, offene Schriften). Pilot People, dann alle; Ziel Freitag: alle Programme mit Admin-Frontend.
- Landkarte (Entwurf, Programmtabelle noch offen): `docs/en/programs/map.md`, 5 offene Punkte (Marketing, Workflows, Helpdesk, Vorbilder für Groups/Identity/History/Store).
- Aufträge: `todo/sprint.md` „Runde 3“, Threads T, P, C, A, M; Thread R (Ausbau) schreibt die Strategie nach dem Pilot.
- **Blinc:** PR 71 ohne KI-Zeile umgeschrieben, git-bug `52784e95…baa1` im Fork `FreeSynergy/Blinc` (`refs/bugs`), Kommentar an Darmie. Klon `/srv/FreeSynergy/blinc`, Darmies CLAUDE.md nur dort und in `blinc-app-fix`. git-bug v0.12.0 in `~/.local/bin`.
- **Kennzeichnung (Nutzer, 2026-11-09):** in unseren Repos bleibt die KI-Kennzeichnung („Dein Verdienst“), bei Blinc keine.

## Arbeitsweise ab Runde 3 (Nutzer, 2026-11-08)
- **Zwei feste Sitzungen:** **Opus = Strategie** (diese Datei; plant mit dem Nutzer, entscheidet, vergibt ADRs, schreibt Aufträge) und **Haiku = Koordinator** (`todo/coordinator.md`; startet auf Kommando Arbeits-Agenten, sammelt deren Meldungen, gibt nur Entscheidungen und Blocker gebündelt an Opus).
- Arbeits-Threads melden **an Haiku, nicht an Opus.** Opus bleibt kurz: lieber eine neue Opus-Sitzung je Thema mit dieser Datei als Gedächtnis als eine sehr lange.
- Aufträge schreibt Opus als Abschnitt in `todo/sprint.md` (Runde N, je Thread eine Liste); Haiku startet je Liste einen Agenten (Sonnet zum Programmieren, Haiku für Mechanisches/Übersetzen, Opus nur für Prüfungen vor Tags).
- Der Nutzer redet mit **Opus über Ideen und Pläne**, mit **Haiku über Status und Kleinkram**.

## Stand am Sprint-Ende (2026-11-08, 18:00, Wochenlimit verbraucht)
- **Store läuft:** `fs-store` v0.0.7 (rpm, signiert, Katalog `fs-catalog` mit TUF-Vorbereitung, Kartenseite, Warteschlange, „Update all“, Einstellungen, Deinstallieren, Root-Sperre). Im Katalog: store, tasks, people, files, maps, calendar (je v0.0.2–0.0.4). Nutzer hat Store per rpm installiert.
- **Versionen zurückgesetzt** (ADR 0064): alle Repos v0.0.N, alte Tags/Releases gelöscht.
- **Neue ADRs dieser Nacht:** 0058 (Kontakte = Profile, Verknüpfen nur nach Rückfrage), 0061 (Facetten), 0062 (Pakete in Git + TUF), 0063 (ein Befehl je Programm, Facetten als Link), 0064 (Versionen), 0065 (Standard-Fensterhülle: Menü, Version, Hilfe, Meldungen, Neustart nach Update).
- **Blinc:** wir haben 4 Fehler gemeldet (Issues 66, 68, 69, 70) und 2 PRs (67 Resize mit Test, 71 Klassenstile). 69 vom Autor behoben, 68 mit Theme-Weg beantwortet. Unser Patch-Fork `FreeSynergy/blinc-app-fix` (a139138) in allen Apps, bis Blinc released.
- **Offen bei den Apps (Handtest des Nutzers):** weiße Schrift beim Tippen; AltGr/@ ergibt „2“ (Tastatur); Trägheit beim Tippen (unser Code <1 ms, Ursache in Blinc-Zeichnen vermutet); Shell-Trait nach ADR 0065 noch nicht getaggt; gegliedertes `email-input` mit Domain-Vorschlägen geplant; eigene eingebettete Schrift.
- **Live-Probe** (echtes Fenster in verschachteltem KWin mit echter Eingabe) von Thread G – Grundlage für automatische Oberflächen-Tests.
- **Aufgeräumt:** 55 Worktrees entfernt (~300 GB). Stehen geblieben mit ungesicherter Arbeit: `.wt-cal-lease` (5), `.wt-fs-maps-server` (10), `.wt-doc-d` (14), `.wt-de-c` (12, wohl verzichtbar), `.wt-fs-store` (nicht gepusht) – in Runde 3 prüfen.
- **Erste Aufgabe Runde 3:** mit dem Nutzer planen (Kandidaten unten unter „Offen bei uns“: Blinc-Fehler, Shell-Trait, Server auf Debian, Web/WASM über den Hub, Marketplace, Nostr/I2P, Messenger-Ideen, Wiki-Vertrag, Resources besprechen).

Für eine neue Sitzung, die entscheidet und dokumentiert. Programmieren macht die andere Sitzung (`todo/handoff-programming.md`).

## Zuerst lesen
`docs/en/manifesto.md`, `docs/en/programs/apps/roadmap.md`, `docs/en/interfaces/index.md`, ADR 0045–0054.

## Regeln dieser Rolle
- Der Nutzer entscheidet, wir empfehlen. Jede Entscheidung landet im selben Schritt in der öffentlichen Doku.
- Vergibt ADR-Nummern. Prüft Meldungen der Programmier-Sitzung gegen GitHub und gegen den Wortlaut des Nutzers.
- Nur eigene Dateien committen (`git commit -- <pfade>`). Nach Änderungen an `docs/*/components`: `scripts/gen_component_indexes.py --lang en` und `--lang de`, sonst scheitert das Deployment.
- Übersetzen ist erlaubt (Nutzer, 2026-11-07): Doku und alles Installierte in Deutsch und Englisch, `en/` ist die Quelle, mechanisch durch Haiku.

## Offen beim Nutzer
0. **Sprint beendet (2026-11-08, 18:00). Runde 3 beginnt mit gemeinsamer Planung.**
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

## Stand 2026-11-07, Abschluss bei ~86 % Wochenlimit
- Alle fünf Threads haben abgeschlossen und reagieren nur noch auf Nachrichten; nichts läuft.
- Erster signierter RPM-Entwurf: `fs-tasks` 0.6.1~rc.2 (App und Server), Signatur `16A4…4342` von der Strategie geprüft. Fehler in `fs-release`: `~` im Namen passt nicht zu `SHA256SUMS.txt`.
- `fs-launcher` nur lokal (`/srv/FreeSynergy/fs-launcher`, 10 Commits, 27 Tests, Regelprüfer 0/0): Kern, rPGP-Prüfung, Quellenliste in TOML, `words.rs`. Wird nach ADR 0060 das neue `fs-store`.
- `fs-wiki` Branch `client`: rebasen und als v0.3.1 taggen (v0.3.0 gibt es schon von Thread 3). `fs-messenger` `matrix`: nicht taggbar, Befunde in der `DESIGN.md`.

## Offen bei uns
- **Server (Nutzer, 2026-11-08), nach dem Sprint planen:** 3 Hetzner-Server. Empfehlung Strategie: keine Container (Rust-Programme als systemd-Dienste mit Sandbox/Landlock); Betriebssystem Debian 13 auf den Servern (Admin kennt es, lange Pflege), Fedora auf dem Rechner des Nutzers; `fs-release`-CI prüft unsere Pakete künftig auf Fedora UND Debian. bootc/eigenes Server-Abbild erst, wenn viele Server gleich gehalten werden sollen. Redox OS beobachten (Nutzer: „richtig gute Alternative, nicht für jetzt“). Web/WASM: statische Dateien; Hub braucht Übergang Cap'n Proto über WebSocket; an Zentinel fragen: `application/wasm`, COOP/COEP-Kopfzeilen, WebSocket/WebTransport-Weiterleitung.
- **Blinc auf dem Prüfstand (Nutzer, 2026-11-08: „Geschwindigkeit, grundsätzliche Fehler, Schnittstelle … leider alles?“), nach dem Sprint:** Belegt bei Blinc: Absturz beim Vergrößern (Issue 66, PR 67), Textarea ohne Farbmethoden (Issue 68), Portal-Farbschema nicht gebaut. Unbelegt: Trägheit (unser Code < 1 ms je Taste, Ursache im Zeichnen/Fensterschleife vermutet), zwei Schriften beim Markieren, weiße Eingabeschrift. Vorschlag Strategie: erst Live-Probe mit Eingabe (kwin --virtual + EIS) und Messung; parallel ein zeitlich begrenzter Gegenversuch, dieselbe Tasks-Workbench mit einem anderen reinen Rust-Toolkit (Kandidat iced, trägt den COSMIC-Desktop; Lizenzen prüfen; früher schon versucht: Archiv `fs-gui-engine-iced`, `dioxus`, `bevy` – Gründe des damaligen Wechsels zuerst lesen). Entscheidung nach Daten. Kerne, Server, Verträge sind davon nicht berührt (ADR 0021).
- **Nostr und I2P (Frage des Nutzers, 2026-11-08), nach dem Sprint besprechen:** Empfehlung Strategie: Nostr als weiterer Anbieter in `fs-messenger` (öffentliche Beiträge, Ausweichweg für Direktnachrichten nach NIP-17/44/59; keine Vorwärts-Geheimhaltung, Relays sehen Metadaten), Matrix bleibt erster Weg. I2P-Bote nicht (Java, Entwicklung weitgehend ruhend, kein Standard); I2P selbst als möglicher Anonymisierungs-Transport zu ADR 0059 prüfen (Rust-Router). Beides vor einer Entscheidung recherchieren.
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
- Manifest als echten Text ausschreiben, dazu ein Werbetext für das Projekt und Beschreibungen der Programme (Nutzer, 2026-11-07: „Texte, die die Menschen umhauen“).

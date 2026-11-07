# Übergabe: Programmier-Sitzung (Stand 2026-11-06)

Für eine neue Sitzung, die programmiert. Zuerst lesen: `conventions/CONVENTIONS.md` (§0 Grundsätze),
`conventions/coding.md` (Muster, kleine Dateien, Abhängigkeiten), ADRs 0019–0049 (Index
`conventions/decisions/README.md`), dann die `DESIGN.md` des Repos, an dem gearbeitet wird.

## Rollen (Nutzer, 2026-11-06)
- **Programmier-Sitzung** (diese Rolle): Code, Tests, Repos, Umbauten, technische Doku (`DESIGN.md`).
- **Entscheidungs-Sitzung** (`freesynergy-9b`, falls noch aktiv): Entscheidungen, ADRs, öffentliche Roadmap,
  `docs/en/interfaces/`. Keine ADR-Nummern selbst vergeben — Entscheidungen dorthin übergeben.
- Öffentliche Doku immer aktuell halten (Transparenz).

## Repos (alle öffentlich, github.com/FreeSynergy, lokal /srv/FreeSynergy/<repo>)
| Repo | Inhalt | Tests | Tag |
|------|--------|-------|-----|
| fs-store | Objektspeicher (AS2-Hülle, Protokoll, Undo, Turso) | 37 | v0.2.0 |
| fs-jscalendar | Gemeinsame JSCalendar-Typen, kein Programm | 6 | v0.1.0 |
| fs-people (früher fs-contacts) | JSContact, vCard, Gleiche-Person-Vorschläge, Rollen, Beziehungen, KI-Markierung | 38 | v0.2.1 |
| fs-groups | Gruppen, Verschachtelung ohne Zyklen, Mitgliedschaft, Einladungen, Delegation | 50 | v0.1.1 |
| fs-identity (Name vorläufig) | Kanidm als `GroupDirectory`, REST v1 | 26 | v0.1.1 |
| fs-files | Dateien; lokaler Ordner, S3 | 55 | v0.2.1 |
| fs-calendar | JSCalendar 2.0 Event, ICS, Einladungen; Aufgaben nur über `TaskItems` | 55 | v0.4.1 |
| fs-tasks | Besitzer von JSCalendar `Task` (ADR 0050); Trait `TaskItems`, Vertrag `tasks.capnp` in fs-interfaces (Entwurf) | 20 | v0.4.1 |
| fs-maps | PMTiles bei Bedarf, Cache, Regionen, Orte, `Places` | 46 | v0.1.1 |
| fs-hub | Programme verbinden, Objekt-Abgleich (Cap'n Proto RPC) | 9 | — |
| fs-wiki (crates fs-text, fs-wiki-core) | Text + Ebenen, Markdown, Links, Vorlagen, `Texts` über fs-store | 73 | v0.1.1 |
| fs-capnpc (crate capnp-compiler) | Cap'n-Proto-Compiler in reinem Rust, 14/14 Orakel | 30 | v0.1.0 |

## Offene Aufgaben (Reihenfolge)
1. ✅ `capnp-compiler` **0.1.1 auf crates.io** (2026-11-06); signierter Release-Entwurf v0.1.1 (26 Dateien, GPG geprüft).
2. ✅ `Task` in fs-tasks umgezogen (2026-11-06), Kalender nutzt nur `TaskItems`, Hub auf Kalender v0.2.0.
   **Offen:** fs-tasks enthält Kopien von Zeit/Zonen, `Participant`, `RecurrenceRule`, ICS-Zerleger aus fs-calendar
   (Doppelung, ADR 0043 §4) → gemeinsame JSCalendar-Basis-Crate? Entscheidung liegt bei der Entscheidungs-Sitzung.
3. Themen-Schnittstellen für das Gebaute (people, events, tasks, places, texts, messages) als versionierte Ziele;
   bestehende Kerne werden Anbieter davon (ADR 0045).
4. Sichtbarer Teil: Wiki-Workbench auf Blinc (zeigt fs-documentation), dann Groupware-Suite.

## Neue Vorgaben (Nutzer über die Entscheidungs-Sitzung, 2026-11-06)
- **Repo `fs-interfaces`** enthält alle Verträge + erzeugten Code (mit unserem `capnp-compiler`); Programme beziehen
  Verträge nur von dort (Git-Tag).
- **Anbieter-Regel (ADR 0045, geändert):** wie eine Elternklasse — jeder Anbieter bietet **alle** Methoden und Attribute;
  erst einen Weg suchen, nur wenn wirklich unmöglich: ausdrücklich `Unsupported` (Trait-Standardmethode). Jeder
  Anbieter meldet, was er kann.
- **Alles Bestehende gegen den Schnittstellen-Katalog umbauen**, Reihenfolge: **people** → groups, files → Rest;
  immer erst den Schnittstellen-Entwurf, dann Code. **`fs-people` mit Rollen bestätigt (ADR 0052,
  `docs/en/interfaces/roles.md`):** ein Datensatz pro Person, mehrere Rollen, keine Vererbung, keine Duplikate;
  „Beziehung zu mir“ (`relatedTo`) ≠ „Rolle in einer Gruppe“ (`org:Role`/`org:Membership`); fs-people hält die Person,
  der Besitzer jeder Rolle hält deren Felder (Nutzer → Identitäts-Wrapper, Mitgliedschaft → fs-groups, Kunde → CRM);
  Rollen-Definitionen sind Objekte (id, Namen, Standard, Felder, Besitzer, Geltung), als Konfiguration ladbar —
  **keine feste Rollenliste** im Code.
- Video: Codecs ausgelagert wie bei GStreamer (eine Codec-Schnittstelle, jeder Codec ein Anbieter), offene zuerst;
  kein H.264 von uns, Dritte dürfen. Neuer Katalogeintrag `Trust` (Web of Trust) — später.
- **`fs-jscalendar`:** nur gemeinsame Typen (kein Programm, keine Daten); fs-calendar/fs-tasks entdoppeln; Aufgaben aus
  **jedem** Import-Format an fs-tasks weitergeben. Zweiter Nutzer für `TaskItems`: erstes Aufgaben-Frontend oder CLI
  (Kanban ist eine Ansicht von fs-tasks, ADR 0049).
- **Plugins** nach Vorbild Zentinel (`crates/agent-protocol`, Hot-Reload in FreeSynergy/zentinel): reine Konfiguration
  geprüft und atomar getauscht; sonst abgeschottete Agenten-Prozesse, bei uns mit Cap'n Proto.
- **Video:** nur offene Formate (AV1, Opus); keinen eigenen H.264-Encoder, kein eigenes OpenH264.
- Zurückgestellt: Zusammenführen, Details Speichern/Export, eigenständige Ansichten.

## Release-Werkzeuge (Nutzer, 2026-11-06)
- Repo **`fs-release`**: gemeinsame Workflows (CI + Release), getestet an capnp-compiler und fs-hub.
- **Nur Kostenloses:** Linux (deb, rpm, tar.gz, AppImage, Flatpak, Arch), Windows (msi, exe, zip, unsigniert),
  macOS universal `.dmg` **unsigniert** (Apple bekommt kein Geld; gespendetes Konto wäre ok), Android über **F-Droid**,
  iOS nur bauen. Releases nur als **Entwurf**, öffentlich erst, wenn es etwas bringt.
- Signatur: **GPG/OpenPGP** (offener Standard, native Paketsignatur); SBOM **SPDX**; Herkunft **SLSA**; SemVer.
- Erstes Blinc-Programm auf Android/iOS testet Blincs Mobil-Teil — Fehler per PR zurück an den Autor.
- **Signaturschlüssel:** `FreeSynergy Release <support@freesynergy.net>`, Ed25519, Fingerabdruck `C40F0FBA5C4CF71D7BEBB5C65478A4738FFEEB69`, bis 2029-11-05. Privater Teil + Passphrase + Widerrufszertifikat sind **nicht mehr auf diesem Rechner** (Nutzer sichert offline, Bestätigung offen). Secrets `GPG_PRIVATE_KEY`/`GPG_PASSPHRASE` nur in fs-capnpc und fs-hub (geprüft 2026-11-06); neue Repos brauchen den Schlüssel vom Nutzer oder ein Org-Secret (braucht admin:org). Öffentlicher Teil: `fs-release/release-signing-key.asc`. Nicht auf Keyservern.
- **Projekt-Adresse überall:** `support@freesynergy.net` (Cargo `authors`, SECURITY.md, Paket-Metadaten).
- **GitHub-Fehler beseitigt (2026-11-06):** Doku-Deploy (veraltete Nav + gleichzeitige Deploys → `concurrency`), fs-release lint (SC2015), kanidm: Sync nur manuell (GITHUB_TOKEN darf keine Workflow-Dateien pushen; optional `SYNC_TOKEN`), Upstream-CI im Fork deaktiviert, `dependabot.yml` entfernt; keine aktiven zeitgesteuerten Workflows mehr.
- **Stand:** fs-release erster Lauf grün an fs-capnpc (`v0.1.1-rc.5`, Entwurf): tar.gz, deb, rpm, Arch, msi, zip, SPDX, Prüfsummen. Offen: GPG-Schlüssel (Adresse vom Nutzer), fs-hub anbinden, AppImage/exe/dmg/Flatpak mit der ersten App.
- **SignPath (Windows-Signatur, kostenlos für OSS): Nutzer am 2026-11-13 erneut fragen.**

## Regeln, die man leicht vergisst
- Abhängigkeiten zwischen Repos nur über Git-Tags (coding.md §8); Probe: frischer Klon nach /tmp baut.
- Vor jedem Commit: `cargo fmt --check` (ohne --all), clippy -D warnings (pedantic), Tests,
  `scripts/check_rust_rules.py <repo>` = 0 Fehler. Nach Rust-Arbeit `scripts/clean_rust.py --root <repo> --apply`
  (`--all` nur, wenn kein Build mehr läuft). RAM: mit llama aktiv nur ~6 GB frei → `-j 4`.
- Agenten früh und oft committen lassen (Abbrüche verlieren sonst alles).

## Stand der Reihenfolge (Programmier-Sitzung, 2026-11-06)
Alle Repos stehen auf `fs-interfaces` v0.5.0. Frische Klone geprüft (Stand vor der Angleichung auf v0.5.0).
1. ✅ `fs-jscalendar` v0.1.0: Kopien entfernt; Aufgaben gehen aus jedem Importformat an fs-tasks.
2. ✅ `people`: fs-people v0.2.1 (Rollen, Beziehungen, KI-Markierung). Offen: `fs-people/DESIGN.md`.
3. ✅ `groups`: fs-groups v0.1.1; `fs-identity` v0.1.1 (Name vorläufig), einmal gegen echtes Kanidm 1.12.0 gelaufen.
4. ✅ `files`: fs-files v0.2.1, lokal und S3, einmal gegen echtes RustFS 1.0.4 gelaufen. Vertrag vorläufig.
5. ✅ soweit Code da ist: fs-tasks v0.4.1, fs-calendar v0.4.1, fs-maps v0.1.1, fs-wiki v0.1.1 (neu: `fs-wiki-core`). **`messages` nur Vertrag: fs-messenger hat keinen Kern.**
6. In Arbeit: `fs-components`, Wiki-Workbench.

Nicht gebaut, überall: Cap'n-Proto-Server, `subscribe`. Nichts ist 1.0; keine Schnittstelle hat zwei unabhängige Nutzer.
Bekannte Fehler: Markdown-Rundreise in fs-text (Dreierketten, nebeneinanderliegende Listen; kein Textverlust), siehe `fs-wiki/DESIGN.md`.

## Sprint Thread 1 (2026-11-06)
- `fs-components` `v0.1.0` (`c058947`) getaggt, zweimal geprüft. `e76cd34` (Entwurfssicherung) in Prüfung für 0.1.1.
- Wiki-App auf `fs-wiki` `main` (`9ddb5e0`), ohne Tag; Entwürfe auf Branch `drafts`. Läuft in echtem Fenster (`kwin_wayland --virtual`), Tippen und Klicken prüft der Nutzer von Hand.
- Markdown-Rundreise behoben (`6781432`): 0 von 1389 Dateien verlieren Wörter, vorher 16.
- `fs-files` echte Namen, in Prüfung. `fs-groups`: sichere Auslegung, **kein Tag bis zur Antwort des Nutzers**.
- Läuft: „Build first“ (fertig: `avatar-group`, `transfer-list`), `charts`. Offen: Chat-Components.

## Nächste Reihenfolge (Empfehlung der Strategie-Sitzung, 2026-11-06, Nutzer kann ändern)
1. `fs-jscalendar`: Kopien in fs-tasks und fs-calendar beseitigen, falls noch nicht erledigt.
2. Schnittstelle `people` in `fs-interfaces` mit Rollen (ADR 0052), dann fs-people als Anbieter umbauen. **ADR 0054 gleich mitdenken:** KIs sind markierte Teilnehmer. Ein Personen-Datensatz muss sagen können „das ist eine KI“ (Rolle plus JSContact `kind` `application`, RFC 9553 §2.1.4, geprüft), ohne sie einzuschränken, und künftig ihren Betreiber nennen (Form offen, Feld nicht verbauen). Aussperren: Der Entwurf ist vorerst bestätigt, gebaut wird er laut `todo/sprint.md` (Thread 2).
3. Schnittstelle `groups` und Kern `fs-groups`: verschachtelt, keine Zyklen, läuft ohne Kanidm. Danach Identitäts-Wrapper über Kanidm REST v1 (`temp/research/kanidm-control.md`, noch kein SCIM).
4. Schnittstelle `files` und Kern `fs-files`: zuerst lokaler Ordner, danach S3 für RustFS.
5. Den Rest gegen den Katalog umbauen: events, tasks, places, texts, messages.
6. `fs-components` beginnen: die gemeinsamen, dazu als erstes Sichtbares die Wiki-Workbench auf Blinc. Erst Components, dann Programm, jeweils wenn das nächste Programm sie braucht (ADR 0049).

`fs-assistant` ist kein eigenes Programm mehr, sondern ein Frontend über `messages` (ADR 0054): dort Agenten als Absender, sichtbare Werkzeug-Aufrufe und den Verweis einer Nachricht auf eine Aufgabe mitdenken (Analyse CodeAF, Seite `assistant`). Noch kein Code dafür.

Der öffentliche Schlüssel liegt in `fs-release`. Vom Nutzer freigegeben und auf keys.openpgp.org hochgeladen (2026-11-06); die Adresse erscheint dort, sobald der Bestätigungslink aus der Mail an `support@freesynergy.net` geklickt ist. **Aktueller Arbeitsauftrag: `todo/sprint.md`.**
- Thread 5 (2026-11-06): `surveys.capnp` in fs-interfaces v0.15.0 (Entwurf, vorläufig); Repo `fs-surveys` angelegt, Kern und Methoden im Bau.
- Thread 2, Punkt 1 und 4a: Vertrag `messages` draft 0.2 in `fs-interfaces` v0.16.0 (Werkzeug-Aufrufe mit Risiko und gebundener Entscheidung, `jobRef`, `stop`, `usage`; Ordinal 0 einmalig auf harmlos umnummeriert). Noch kein Nutzer; maschinenlesbare MCP-Sperre für `decide` fehlt noch. Geprüft vom zweiten Agenten.

- Thread 4 (2026-11-06): Grundgerüst steht in `fs-components` (`crates/fs-components-render`, `crates/fs-components-app`), noch ohne Tag. Frontend-Struktur vorläufig: Crate `fs-<programm>-app` ohne Blinc, Workbench in `fs-components`. Weiter mit `fs-people`.
- Thread 2, Korrektur zum Eintrag davor: Geprüft war der Stand bis `b213ed8`; die letzte Runde (v0.16.0, Feld `ToolCall.revision`) kam ohne erneute Prüfung. Das Review des Kerns hat `revision` inzwischen geprüft und vier Lücken im Wortlaut gefunden; die Klärung liegt im Branch `msg-contract-2`, kommt mit dem nächsten Tag.
- Thread 5 (2026-11-06): `fs-surveys` v0.1.0 getaggt (Kern, zehn Verfahren, 107 Tests, drei Prüfrunden); kein capnp-Server, `survey.publicLink` `Unsupported`. `fs-store` v0.3.0: `UnloggedObjects`.
- Thread 2, vorgemerkt, nicht im Sprint: `fs-surveys` v0.1.0 möchte, dass fs-messenger den Port `TokenDelivery` bedient (Einladungs-Token für anonyme Umfragen). Das Token darf in kein Log, keine Aktivität und keinen für eine KI sichtbaren Werkzeug-Aufruf. Hürde: fs-store schreibt den Inhalt jeder Nachricht ins Aktivitätsprotokoll, eine normale Nachricht erfüllt das also nicht. Bis dahin antwortet `fs-surveys` `Unsupported`.
- Thread 5 (2026-11-06): `fs-history` v0.1.0 getaggt (Kern, Hub-Adapter, 48 Tests, zwei Prüfrunden); eigener Index ohne Inhalte, `actor` leer, Zeit = Empfangszeit bis zum nächsten `fs-hub`-Tag.
- Thread 4 (2026-11-06): `fs-people` hat ein erstes echtes Fenster (`fs-people-app`, `fs-people` main `9c8a3cc`): Liste, Suche, Ansehen, Anlegen, Bearbeiten, Löschen, vCard rein und raus. Noch nicht fertig: Nachprüfung läuft, Handtest durch Kal fehlt, Kern-Korrekturen liegen auf `people-core-fixes` und warten auf `server` (24). Weiter parallel mit `fs-calendar`.
- Thread 5 (2026-11-06): `fs-resources` v0.1.0 getaggt (Kern, 115 Tests, vier Prüfrunden); offener Punkt und Grenzen der Gruppensummen in der `DESIGN.md`.
- Thread 4 (2026-11-06): `fs-people` Korrekturrunde zwei auf `main` (`304a609`, `fs-components` `4db5c43`). Kern-Korrekturen auf `people-core-fixes` (`ca39e0c`), warten auf `server` von 24; bis dahin kein Tag, und der Überschreib-Fehler bleibt auf `main` offen. Danach: drei App-Schritte, Nachprüfung, Handtest durch Kal.
- Thread 2: `fs-interfaces` v0.27.0 enthält Vertrag `messages` draft 0.3 (geprüft vor dem Tag). Stand der Punkte: 2 (Kern) und 3 (Mail) je nach zwei Prüfrunden in Nachbesserung, ohne Tag; Matrix in Arbeit; offen beim Nutzer: v4-Schlüssel (`fs-messenger-mail/DESIGN.md`, Interoperability).
- Thread 2, Punkt 2 fertig: `fs-messenger-core` v0.1.0 (vier Prüfrunden, zweiter Agent, `gates.sh` auf frischem Klon, 162 Tests). Grenzen stehen in der `DESIGN.md`: nur geräte-lokal, Senden nicht genau einmal, Nachrichten nicht ersetzbar außer unentschlüsselten, `decide` und `stop` antworten `Unsupported` bis Punkt 4.
- Thread 5 (2026-11-06): `fs-whiteboard` v0.1.0 getaggt (Kern Stufe 1, 104 Tests, mehrere Prüfrunden); offene Punkte in der `DESIGN.md`; `Presence` und Synchronisierung nicht gebaut.
- Thread 4 (2026-11-06): `fs-calendar` Korrekturen auf `main` (`d1cb4af`, `fs-components` `360ef92`), Nachprüfung läuft, Handtest fehlt, kein Tag. Hülle hat ein Menü (`a2179c8`), noch nicht unabhängig geprüft. Offen im Kern `fs-calendar-core` (24): UID-Überschreiben, Override vor Serienstart, kaputtes Override, unbekanntes `TZID`, Markierung in der Hülle, `fs-jscalendar` v0.1.1. Liste in `fs-calendar/DESIGN.md`.
- Thread 2, Punkt 3 Mail fertig: `fs-messenger-mail` auf `main` von fs-messenger (`af440af`, vier Prüfrunden, `gates.sh`, 32 Server-Tests gegen Stalwart 1.0.3). Liest und schreibt mit GnuPG und RNP nicht (gemessen, `DESIGN.md`, Abschnitt Interoperability); v4 entscheidet Kal. Matrix: gebaut, Review läuft. Wächter (Punkt 4): gebaut, Review läuft. KI-Modell: in Arbeit, „nicht gegen einen echten Server geprüft“.
- Thread 4 (2026-11-06): `fs-calendar` dritte Korrekturrunde auf `main` (`993eb9e`, `fs-components` `1b981c7`). `fs-tasks` und Hülle in Korrektur, `fs-files` und `fs-maps` im Bau. Noch keine App als fertig zu werten: Handtest fehlt überall, Tags warten auf Kern (24) und Abschlussprüfung.
- Thread 4 (2026-11-07): `fs-people-app` spricht über Cap'n Proto (`fs-people` Branch `gui`, `6942fca`; neues Crate `fs-people-client`, `RpcPeople`, Muster Adapter, Worker-Thread als Command, Fristen 5 s/30 s). Opus-Prüfung durch, alle bestätigten Punkte behoben, 80 Tests grün. Kein Tag (Handtest Kal offen). Fragen an die Strategie: (1) eigener Problem-Typ im Server für `Sensitive(id)`; (2) Offset/Paging für die Suche im Vertrag `people`. `fs-tasks-app` in Umstellung; `fs-calendar`, `fs-files` warten auf Server (Thread 3), `fs-maps` Server nur auf Branch.
- Thread 3 (2026-11-07): `fs-wiki` `v0.2.0` getaggt (`12a05be`): Server `fs-wiki-server` für `texts.capnp` (alle 16 Methoden, `subscribe` mit `ended`), `gates.sh` auf frischem Klon, Opus-Prüfung ohne Muss-Fehler. Offen (DESIGN.md): Seiten kosten die ganze Trefferliste (öffentliche `cursor_position` in `fs-interfaces::rpc` würde helfen), Markdown-Grenze 4 MiB, Vertrag `LinkRow` ohne Titel/`internal`, Kommentar an `revision` falsch, `Registry` des Observers dreifach (tasks, wiki, files, calendar, people) -> gemeinsame Crate. Thread 1: die App ist noch nicht auf den Server umgestellt. `fs-files` (`a95acdf`), `fs-calendar` (`5dbe10d`) auf Branch `server`, gebaut, Prüfung läuft/Nachbesserung, kein Tag.
- Thread 5 (2026-11-07): `fs-streaming` v0.1.0 getaggt (`2a8eebe`, Kern + RTMP-Relay, 94 Tests, `gates.sh` auf frischem Klon grün, mehrere Prüfrunden laut DESIGN.md); nur auf Loopback mit ffmpeg geprüft, kein capnp-Server, keine GUI. Weiter mit Punkt 5: Rollen in `fs-people` (mit Thread 3 abstimmen, `fs-people-server`).
- Thread 5 (2026-11-07): Punkt 5 `fs-people` Rollen als SKOS/JSON-LD: Branch `roles-skos` (a43b918, nur `fs-people-core`, auf `server`), drei Opus-Prüfrunden ohne Muss-Fehler, Kern grün; kein Tag, Merge in `server` macht Thread 3 (Server-Tests auf volle IRIs, `RoleRestore::skipped()` ausgeben, fs-interfaces v0.36.0), App `sheet.rs:142` Thread 4. Grenzen in `fs-people/DESIGN.md`: Export als `org:Membership`, `roles.jsonld`, SHACL Unsupported; ein gespeichertes Array friert die mitgelieferten Rollen ein. `fs-groups`/`AiMarking` und Wächter in `fs-messenger` müssen auf `is_ai_role()` bzw. volle IRI. Punkt 6 (Folgen in `fs-groups`) im Bau auf Branch `follow`.
- Thread 5 (2026-11-07): Punkt 6 `fs-groups` Folgen (ADR 0056): Branch `follow` (6d17b4a, nur `fs-groups-core`, auf `server`), Muster Repository andersherum + State + Specification, Trait `Follows` (`deliver`, `pass_on`, `revoke_delivery`, `receive`, `withdraw`, `remove_source`), `fs-interfaces` v0.38.0 (`Groups.follows @6`, `origin`). Zwei Opus-Prüfrunden, zuletzt ohne Muss-Fehler, gates.sh grün; kein Tag, kein capnp-Server (Thread 3: Cargo auf v0.38.0, `follow.*` in `capabilities()`). Vorläufig: kein `Manage` an Fremde, Weitergabe einstufig, Absender nicht authentifiziert (ADR 0035). Alle Punkte der Thread-5-Liste sind damit gebaut; `roles-skos` wartet auf den Merge durch Thread 3 und die Umstellung von `AiMarking` (fs-groups) und Wächter (fs-messenger) auf `is_ai_role()`.
- Thread 2 (2026-11-07): `fs-messenger` v0.2.0 getaggt (`6a7aa18`, auf `main`): Wächter `fs-messenger-guard` (ADR 0054, 0056: Einladung, Freigabe, Bremse, Geräte-Nachweis, Notaus) mit Kern-Ergänzungen, dazu Mail. Fünf Prüfrunden durch Opus-Agenten, die den Code nicht schrieben (Notaus: drei Rennen, hängender Prüfer, Wiederholer, Bericht nach Stopp über `ingest`; alle nachgestellt und behoben), `gates.sh` im frischen Klon grün. Kontotyp `agent` entfernt, KI-Regel hängt am Teilnehmer (`SenderLookup`). Grenzen in `DESIGN.md`: 4c (Zustimmung, Hinweis, Verlauf, fremde Matrix-Programme) nicht gebaut; „Ohne Befugnis nichts“ ergibt heute `Ask`, ein freigegebenes `readsOnly` gibt `Allow` für alles Lesen („Lesen ist nicht harmlos“ offen); 34 Stalwart- und 3 gpg-Tests sind `#[ignore]` und für 0.2.0 nicht neu gelaufen. Für die Strategie: `log.rs`, `digest.rs`, `signed.rs`, `message_index.rs` verstoßen gegen die none-Regel (Open point 0), `enrol.rs` als Facade zu bestätigen. Matrix: Branch `matrix` (`8c2adb6`), fünfte Prüfung läuft, kein Tag. `ai` ruht (Umbau auf Matrix-Konto, wartet auf Wächter), kein Test gegen echtes Modell.
- Thread 3 (2026-11-07): Server getaggt, je mit Opus-Prüfungen (zweiter Agent, mehrere Runden) und `gates.sh` auf frischem Klon: `fs-wiki` v0.2.0, `fs-files` v0.4.0 (Backends nur unter `.fs-files/backends`, Neustart-Fall geprüft), `fs-tasks` v0.6.0 (`editIf`, `revision`), `fs-people` v0.4.0 (`updateIf`, `revision`, Rollen als IRIs mit `type/broader/closeMatch/standardRefs` auf dem Draht, `RoleRestore` auf stderr). `fs-interfaces`: v0.35.0 (Vertragsrunde 2: `updateIf`/`editIf`, `revision`, files-Cursor), v0.36.0 (RoleDefinition-Felder), v0.39.0 (`Problem.extensions`: typisierte Zusatzfelder nach RFC 9457; Server füllen sie noch nicht, eigene Runde). Offen, auf Branch `server` bzw. eigenen Branches, kein Tag: `fs-calendar` (sechste Korrekturrunde: Speichergewicht, Sprung bei Wiederholungen, Semaphor), `fs-store` v0.4.0 (`log-purge`: Log-Löschen, Identität, `is_encrypted`; große Originale nur Entwurf, `Unsupported`), `fs-mcp` (Branch `mcp`, Crate `crates/fs-mcp` in fs-interfaces, vierte Prüfrunde; Marken in `marks/*.toml`, Ort vorläufig), `fs-groups` `follow` (noch nicht gemerged). Nächste Reihenfolge: Server füllen `Problem`-Erweiterungen, `SupportReport.instance`, `fs-groups` server + Follows, CLI je Programm (Punkt 4), Hub-Test über mehrere Programme (Punkt 5).
- Thread 5 (2026-11-07, nach dem Absturz): Punkt 7 `fs-surveys` KI-Teilnahme: Branch `ai-participants` (f1c5f78, gepusht, kein Tag, kein Merge), Vertrag `fs-interfaces` v0.40.0 (`aiAllowed`, `creator`, getrennter `ai`-Teil, `exportAi`); Erlaubnis je Umfrage (Standard nein, nur Ersteller), KI-Antworten in eigener Spur durch alle zehn Verfahren, Export, Ereignisse; Markierung vom Host, Zweifel = KI, Selbstangabe nie gelesen. Opus-Prüfung ohne Muss-Fehler, Soll-Punkte behoben, 133+ Tests, fmt/clippy/Regelprüfung grün (über `limited.sh`). Grenzen: Token-Weitergabe Mensch an KI zählt als Mensch; `anonymousOpen` braucht jetzt `Credential::Person` vom Host (Änderung gegenüber 0.1.0, offene Frage an den Nutzer); `fs-interfaces`-Manifest steht noch auf 0.39.0 (Tag v0.40.0). Kein MCP-Werkzeug.
- Thread 3 (2026-11-07, nach dem Absturz): getaggt `fs-calendar` v0.5.0 (Server, `updateIf`, `revision`, Grenzen; letzte Korrekturrunde ohne eigene Opus-Prüfung, nach Weisung der Strategie), `fs-store` v0.4.0 (Log-Löschen `purge_object`, Identität UUID, `is_encrypted`; Eintrag nach dem Löschen `{"redacted":true,"before":"redacted","after":"redacted"}`; Sperre: Hub und Hub-Client erst auf 0.4, dann `purge_object`), `fs-interfaces` v0.41.0 und v0.42.0 (Crate `fs-mcp`, Generator Stufe 1: 283 Werkzeuge, 13 Ressourcen; Marken in `marks/*.toml`, Accounts und Einladungen ausgeschlossen, 141 Werkzeuge mit freien Fachformat-Feldern als benannte Grenze). Offen im Calendar: Import quadratisch, Schreib-Speicher, Vertragslücke `occurrences` ohne `damaged`. Läuft: Hub (Branch `hub-store04` aus `pull-size`, `fs-store` 0.4, Test über mehrere Programme `fs-hub-e2e`). Danach: `SupportReport.instance`, `fs-groups` `follow` + Server, Server füllen `Problem`-Erweiterungen, CLI.

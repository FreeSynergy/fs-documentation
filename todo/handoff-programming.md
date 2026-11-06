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

# Sprint bis Sonntag, 2026-11-08, 18:00 (Stand 2026-11-07)

**Ziel:** So viel wie möglich bauen, aber nichts, was wir wegwerfen müssten. Nur Besprochenes: `docs/en/programs/apps/roadmap.md`,
`docs/en/interfaces/index.md`, ADR 0045–0054. Keine neuen Ideen, keine neuen Standards ohne Rückfrage.

**Ende (Nutzer, 2026-11-07): Sonntag, 2026-11-08, 18:00 Uhr. Danach ruhen alle Threads, bis ein neuer Plan freigegeben ist.** Vorher alles pushen, offene Arbeit in die `DESIGN.md` und eine Zeile in `todo/handoff-programming.md`. Es wird nach jedem Schritt gepusht.

## Start für jeden Thread
Einzeilig einfügen, N ersetzen:

```text
/loop Du bist Thread N im Sprint. Lies /srv/FreeSynergy/fs-documentation/todo/sprint.md, dann arbeite deine Liste der Reihe nach ab, auch mit vielen Agenten, und nimm nach jedem fertigen Punkt den nächsten.
```

## Runde 3 (Nutzer, 2026-11-09): Datentypen, Components, vier Frontends – Pilot People

**Grundlage:** ADR 0066 (`conventions/decisions/0066-datentypen-und-vier-frontends.md`) und die Landkarte `docs/en/programs/map.md`. **Ziel der Woche:** Bis Freitag haben möglichst alle Programme ein erzeugtes Admin-Frontend, das grundlegend funktioniert; People zusätzlich mit Einfach-, Apple- und Windows-Frontend. **Reihenfolge:** Mo–Di Pilot People (Threads T, P, C, A, M), danach verteilt die Strategie den Ausbau auf die übrigen Programme (Thread R). Die Regeln unten gelten weiter. Meldungen an den Koordinator (Haiku), nicht an die Strategie.

**Blinc-Beiträge (Nutzer, 2026-11-09):** In Commits, PRs und Issues für `project-blinc/Blinc` **keine KI-Kennzeichnung**, Regeln in `/srv/FreeSynergy/blinc/CLAUDE.md` (git-bug, volle 64-stellige ID als Trailer; `git config git-bug.git-transport git`). In unseren eigenen Repos bleibt die Kennzeichnung.

### Thread T – Grundtypen und Typbeschreibung (Sonnet, startet sofort)
1. In `fs-interfaces` ein Schema `types.capnp`: die Grundtypen aus `map.md` (zuerst E-Mail, Telefon, Name, Adresse, Ort, Datum/Zeit, Sprache, Link, Bild, Schlüssel, Auswahl, Stichworte, Verweis), je mit Standard im Kommentar.
2. Im selben Schema die **Typbeschreibung**: Felder (Name, Grundtyp, Pflicht, mehrfach, Beschriftung als Übersetzungs-Schlüssel), Befehle (Name, Eingabe, Ergebnis). Muster: Registry; Trait `DescribesType`.
3. Rust-Umsetzung der Grundtypen (prüfen, normalisieren, vorschlagen) als eigenes Crate, Name vorläufig `fs-types`, Ort nach `coding.md` begründen und in der `DESIGN.md` festhalten.
4. Prüfen, ob ein freies Crate JSContact/vCard abdeckt (Kandidat `calcard`, Lizenz und Reifegrad); Ergebnis in die `DESIGN.md`, nicht selbst nachbauen, was es gibt.
5. Früh einen Entwurf taggen (v0.0.N), damit P, C und A anfangen können.

### Thread P – `fs-people` auf JSContact (Sonnet, startet nach dem ersten Tag von T)
1. `Person` vollständig nach `docs/en/data/people/jscontact/description.md` (RFC 9553 `Card`), alle Felder der Tabelle; vorhandene Daten migrieren, nichts verlieren.
2. Typbeschreibung von `Person` melden (Trait `DescribesType` aus T), mit den Befehlen: anlegen, ändern (PatchObject), suchen, löschen, prüfen, vorschlagen (z. B. E-Mail-Domains aus vorhandenen Kontakten).
3. vCard-Import und -Export über RFC 9554, wenn T ein Crate gefunden hat.

### Thread C – Components je Grundtyp und Stile (Sonnet, startet sofort mit dem Stil-System)
1. In `fs-components` das Stil-System: Tokens für Abstände, Zeilenhöhen, Schriftgrößen, Radien, Farben, Effekte (Glas, Fläche, Schatten) und ein Iconset je Stil. Vier Stile: Admin, Einfach, Apple, Windows. Maße für Apple und Windows aus Thread M.
2. Je Grundtyp vier Components: Eingabe, Anzeige, kompakt, Zelle. Zuerst E-Mail (gegliedert, mit Vorschlägen über den Befehl „vorschlagen“), Name, Telefon, Adresse, Datum.
3. Alles, was Blinc nicht kann (z. B. Glas, eine bestimmte Zeilenhöhe), genau messen und als git-bug-Eintrag mit Beleg in unserem Blinc-Klon festhalten; der Strategie gebündelt melden.

### Thread A – erzeugtes Admin-Frontend (Sonnet, startet nach dem ersten Tag von T)
1. Ein Frontend, das aus einer Typbeschreibung Liste, Detail, Formular und Befehle erzeugt, mit den Components aus C und der Fensterhülle nach ADR 0065.
2. Zuerst für People, dann für jedes Programm, das eine Typbeschreibung liefert.

### Thread M – Maßblätter Apple und Windows (Haiku, startet sofort)
1. Aus den öffentlichen Leitlinien (Apple Human Interface Guidelines, Microsoft Fluent 2) die Maße zusammentragen: Abstände, Raster, Schriftgrößen und Zeilenhöhen, Radien, Materialien (Glas, Mica/Acrylic), Farben, Fokus, Listenzeilen. Mit Quelle je Wert.
2. Offene Schriften mit ähnlichen Maßen vorschlagen (Lizenz je Schrift).
3. Für People: Aufbau der Kontakte-App auf macOS und der Kontaktansicht unter Windows (People/Outlook) beschreiben, mit Maßen. Bildschirmfotos nur lokal unter `/srv/FreeSynergy/.scratch/reference/`, **nie in ein Repo**.
4. Ergebnis: `docs/en/components/styles/apple.md` und `windows.md`; danach `scripts/gen_component_indexes.py --lang en`.

### Thread F – Funktions-Vorbilder prüfen und analysieren (Haiku, startet sofort)
1. Die Tabelle „Function references“ in `docs/en/programs/map.md` prüfen: gibt es das Programm noch, stimmt die genannte Funktion? Korrekturen direkt in die Tabelle, mit Quelle.
2. Für jedes dort genannte Programm, das unter `frontends/` der Kategorie noch fehlt, eine Analyse im üblichen Aufbau anlegen (`index.md`, `latest/description.md`, `features.md`, `layout.md`, `menus.md`, `shortcuts.md`, `api.md`), nur Funktionen, nichts kopiert (ADR 0012, 0013, 0025). Neue Kategorien bei Bedarf: notes, history, store, start.
3. Die Fähigkeiten in die `requirements.md` der Kategorie übernehmen (Status `proposed`).

### Thread R – Ausbau auf alle Programme (ab Mittwoch, Liste folgt von der Strategie)
Je Programm: Datentyp nach seinem Standard, Typbeschreibung, Admin-Frontend. Die Strategie schreibt die Liste, sobald der Pilot steht.

## Runde 2 (Nutzer, 2026-11-07 abends): Laden `fs-store` lauffähig und installierbar

Die fünf Threads der Runde 1 sind fertig. Runde 2 hat fünf neue Threads; S, M und U starten nach dem Ende der Umbenennung (Nutzer), D sofort. **Sprint.md immer von GitHub lesen** (`git -C /srv/FreeSynergy/fs-documentation fetch -q && git -C /srv/FreeSynergy/fs-documentation show origin/main:todo/sprint.md`), der lokale geteilte Baum ist veraltet. Mechanische Arbeit (Suchen und Ersetzen, Doku nachziehen, Listen) an Haiku-Agenten geben, sie verbrauchen am wenigsten; Code-Prüfung vor jedem Tag weiter durch einen zweiten Agenten, der den Code nicht schrieb.

**Verbrauch (Nutzer, 2026-11-08, 93 %):** Keine 95-%-Grenze mehr – arbeiten, bis das Kontingent aufgebraucht ist. Darum nach jedem fertigen Schritt pushen und eine Zeile in `todo/handoff-programming.md`, damit beim Abbruch nichts verloren geht. **Vorrang:** (1) der Store läuft sauber (installieren, öffnen, aktualisieren, Fehler sichtbar); (2) die Programme laufen und funktionieren aus dem Store heraus; Schönheit der Components danach. Das Löschen alter Tags/Releases wartet auf das Ja des Nutzers zur konkreten Liste (morgen).

Startzeilen:
```text
/loop Du bist Thread R (Umbenennung) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“), dann arbeite die Liste von Thread R der Reihe nach ab.
/loop Du bist Thread S (Laden fs-store) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“), dann arbeite die Liste von Thread S der Reihe nach ab.
/loop Du bist Thread D (Doku-Seite) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“), dann arbeite die Liste von Thread D der Reihe nach ab.
/loop Du bist Thread G (Oberflächen) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“), dann arbeite die Liste von Thread G der Reihe nach ab. Keine langen Pausen (höchstens 60–120 s); fehlt eine Entscheidung, vorläufig nehmen, notieren, weiter.
/loop Du bist Thread M (Messenger) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“). Warte, bis Thread R „Umbenennung fertig“ meldet (in todo/handoff-programming.md oder per Nachricht), dann arbeite die Liste von Thread M ab.
/loop Du bist Thread U (Umfragen) im Sprint, Runde 2. Lies sprint.md von GitHub (Befehl im Abschnitt „Runde 2“). Warte, bis Thread R „Umbenennung fertig“ meldet (in todo/handoff-programming.md oder per Nachricht), dann arbeite die Liste von Thread U ab.
```

### Thread R: Umbenennung nach ADR 0060, danach `fs-release`
Schreibt in alle Repos, solange Schritt 1–3 laufen; sonst arbeitet niemand an Rust-Code außer Thread S in `fs-launcher`.
1. GitHub-Repo `fs-store` → `fs-objects` (ADR 0060, vom Nutzer akzeptiert). Crate `fs-objects`/`fs_objects`, Tag `v0.5.0`. Lokalen Ordner `/srv/FreeSynergy/fs-store` → `fs-objects`, Remote-URL anpassen.
2. Alle Repos per Skript umstellen (Git-Adresse, Crate-Name, `use fs_store`, Doku in `DESIGN.md`/`README.md`), je Repo `gates.sh` grün, frischer Klon baut, neuer Patch- oder Minor-Tag in Abhängigkeitsreihenfolge (`fs-interfaces` zuerst, falls betroffen, dann `fs-objects`, `fs-hub`, die Programme). Die Ersetzung dürfen Haiku-Agenten machen; die Prüfung macht der Thread.
3. **Auch offene Branches** (`matrix`, `ai`, `follow`, `client`, `gui`, `ai-participants`, `server`, `files-gui`, `maps-gui` …): je Branch einen Commit mit der Umstellung, ohne Merge, ohne Tag. Liste aller Branches, die noch auf `fs-store` zeigen, mit `git ls-remote` und Suche in `Cargo.toml`/`Cargo.lock` aller Branches. Erst wenn die Liste leer ist: Meldung an Thread S und Strategie „Name `fs-store` frei“.
4. Öffentliche Doku nicht anfassen (macht die Strategie), nur `DESIGN.md`/`README.md` der Repos.
5. `fs-release`: `~` im Versionsnamen passt nicht zu `SHA256SUMS.txt` (rpm `0.6.1~rc.2`); `features` an jedes Paket; ein Binary unter `crates/` ohne `cargo-package`; msi bei mehreren Paketen. Danach: gemeinsamer Prüf-Ablauf bei jedem Push (fmt, clippy pedantic `-D warnings`, Tests, `check_rust_rules.py`), ohne Secrets, in alle Repos (Nutzer „ja“, 2026-11-07).

**Entscheidung für Thread R (Strategie, 2026-11-08, vorläufig):** `fs-resources`/`fs-history` blockiert: **`query_unlogged` in `fs-objects` (v0.6.0)**, keine eigene Id-Liste in den Programmen (eine Stelle der Wahrheit, sonst doppelte Logik). Es liefert nur unlogged Objekte der Typen, die dem aufrufenden Programm gehören; `query` bleibt unverändert und lehnt weiter ab. Danach beide Repos umstellen, taggen.

### Thread S: Laden `fs-store` (heute `/srv/FreeSynergy/fs-launcher`, nur lokal)
**Name (Nutzer, 2026-11-07):** offiziell **FreeSynergy.Store**. **Signatur bereit (2026-11-08, 01:12):** Secrets `GPG_PRIVATE_KEY`/`GPG_PASSPHRASE` sind in allen nicht archivierten `fs-*`-Repos gesetzt (Unterschlüssel `372A583D05BF8362604CF25DE26A2347F2B1C097` von `16A4…4342`, öffentlicher Teil in `fs-release`). Neue Repos (z. B. der Laden) brauchen `fs-release/scripts/set-signing-secrets.sh <repo>` durch den Nutzer. **Nutzer, 2026-11-07 abends:** Vorabversionen dürfen öffentlich werden. **Spätestens Sonntag** soll es installierbare Programme geben, die Freunde testen. Der Nutzer will nicht immer wieder von Hand installieren: **Der Laden ist die App, aus der man Programme installiert, aktualisiert und erweitert.** Darum: CLI nur als dünner Test, die GUI (Punkt 6) ist Ziel, nicht Zugabe. Reihenfolge der ersten Pakete: der Laden selbst, `fs-tasks`, `fs-people`, dann was `fs-release` sauber baut. Signieren: Der Nutzer legt die Secrets für den Signaturschlüssel an; bis dahin Entwürfe bauen und alles andere fertig machen, dann veröffentlichen als **Pre-release**.
Ziel: Auf diesem Rechner (Fedora) installiert der Laden ein echtes FreeSynergy-Programm aus einer Git-Quelle, prüft die OpenPGP-Signatur (Schlüssel `16A4A3EE563AEF51FCF0C55DED7B57C4A1904342`), aktualisiert es, rollt bei Fehlern zurück, und aktualisiert sich selbst. Erst lesen: `fs-launcher/DESIGN.md`, ADR 0036, 0060, 0051, 0021, `temp/research/craft-launcher.md`. Reihenfolge wie immer: Muster, Trait, Tests, Umsetzung.
1. **Sicherung:** Repo jetzt als `FreeSynergy/fs-launcher` auf GitHub anlegen und pushen (Nutzer, 2026-11-07: Push im Sprint erlaubt). Umbenennung in `fs-store` erst nach der Meldung „Name `fs-store` frei“ von Thread R; dann Crates `fs-store-*`, Ordner, Doku.
2. **Katalog (vorläufig, Strategie 2026-11-07):** Eine Quelle ist ein Git-Repo mit einem Katalog im Format **AppStream** (freedesktop, Katalog-YAML/DEP-11 oder XML; einen Standard wählen und begründen) plus abgetrennter OpenPGP-Signatur über den Katalog. Der Katalog nennt je Paket Version, Art (Programm, Frontend, Component, Theme), Format, Download-Adresse der Release-Datei und deren Signatur. Geholt wird der Katalog mit `gix`, die Dateien per HTTPS. Unsere Referenzquelle: neues Repo `FreeSynergy/fs-catalog` (erst anlegen, wenn Schritt 3 lokal läuft). Kein eigenes Format erfinden.
3. **Engine:** `gix`-Abruf, Prüfung, `InstallStrategy` zuerst `tar.gz` nach `~/.local` (ohne root), dann `rpm` über `dnf`/`pkexec` (root fragt der Nutzer selbst). `RunningCheck` für Linux. Selbstaktualisierung: neue Datei daneben, Signatur prüfen, atomar tauschen, alte Version behalten.
4. **Vertrag:** `launcher.capnp` aus der Skizze in `DESIGN.md` nach `fs-interfaces` (nur eigene Datei, `pull --rebase`, nächste freie Version). Server `fs-launcher-server` (später `fs-store-server`), dazu ein CLI als erster Nutzer: `sources`, `available`, `install`, `update`, `installed`.
5. **Probe gegen echt:** Ein Paket, das `fs-release` gebaut und signiert hat (z. B. `fs-tasks` als `tar.gz`), über den Katalog installieren und starten. Entwürfe sind nicht öffentlich: Solange der Nutzer keine Vorabversion freigibt, mit einem lokalen Katalog (`file://`-Git-Repo) und den Dateien des Entwurfs testen (`gh release download`), und das in der `DESIGN.md` sagen.
6. **GUI auf Blinc** (mit `fs-components` v0.3.0): Quellen, Verfügbar, Installiert, Fortschritt eines Auftrags. Texte über `words.rs`.
7. **Paket für den Laden selbst** über `fs-release` (rpm und tar.gz), damit der Nutzer ihn mit `dnf install` installiert. Kein öffentliches Release ohne Rückfrage, nichts signieren (Schlüssel beim Nutzer).

### Thread D: Doku-Seite und READMEs (kann sofort starten, schreibt nur in `fs-documentation`; READMEs der Repos erst nach „Umbenennung fertig“)
**Nutzer, 2026-11-07:** Die Seite https://freesynergy.github.io/fs-documentation/ sieht nicht ernsthaft aus, die Menüstruktur ist kaputt. Wir wollen ernst genommen werden und einladend sein. READMEs immer Englisch. **Doku und alles, was installiert wird, in Deutsch und Englisch** (ändert ADR 0053, Punkt 2: Übersetzen jetzt erlaubt, mechanisch durch Haiku-Agenten, `en/` bleibt die Quelle).
1. Bestand aufnehmen: `mkdocs.yml` (1239 Zeilen, Nav von Hand), kaputte Menüpunkte, tote Links, Seiten ohne Nav, `theme.language: de` obwohl `en/` die Quelle ist. `mkdocs build --strict` auf einer Kopie, Liste der Fehler.
2. Aufbau: Startseite für Menschen (Text aus `temp/drafts/werbung-de.md`, englisch als Quelle), oben wenige klare Bereiche (z. B. Programme, Mitmachen, Schnittstellen, Entscheidungen), Navigation aus Ordnern statt von Hand (Plugin wählen und begründen, z. B. `awesome-pages`), Sprachwechsel Deutsch/Englisch (`mkdocs-static-i18n`). Nur Material-Bordmittel und gepflegte Plugins.
3. Aussehen: eigene Farben und Schrift statt Indigo/Roboto-Standard, Logo, Startseite mit Karten je Programm. Nichts kopieren.
4. Übersetzung der Startseite, des Manifests und der Programmseiten nach `de/` durch Haiku-Agenten, Stichproben durch den Thread.
5. Indexe neu erzeugen (`scripts/gen_frontend_indexes.py` schreibt sonst 29 fremde Kategorie-Seiten; prüfen, warum, und alle sauber erzeugen), `gen_component_indexes.py --lang en/de`. Deploy grün.
6. Nach „Umbenennung fertig“: die README-Entwürfe aus `temp/drafts/readmes/` (vom Nutzer im Ton freizugeben) in die Repos, dabei veraltete Versionsangaben in `DESIGN.md`/`README.md` richtigstellen (Liste in der Meldung des Entwurfs-Agenten: messenger, groups, files, components, fs-interfaces-Tabelle, Lizenzanzeige auf GitHub).

**Für Thread D:** neue Seite `docs/en/programs/index.md` (ADR 0061, Facetten) in die Navigation aufnehmen, gut sichtbar unter „Programme“.
**Für Thread S:** ADR 0061: Der Katalog führt Facetten als eigene Apps mit Logo; installiert wird das Programm. Format der Facetten-Liste im Manifest des Programms festlegen.

**Für Thread S (Nutzer, 2026-11-08): ADR 0062** – Pakete in Git (Katalog-Repo `fs-catalog` mit AppStream + **TUF ganz**, ein Tag je Version in Paket-Repos, flach geholt mit `gix`, Spiegel überall, HTTPS als zweiter Weg). Vorrang bleibt: der Laden ist morgen installierbar.

**Für alle (Nutzer, 2026-11-08): ADR 0063** – ein Programm, ein Befehl: `fs-<programm>` ohne Argumente = Oberfläche, Unterbefehle wie `git` (`fs-store install …`, `fs-tasks serve`), Feature `gui` für Bauten ohne Bildschirm; keine `-cli`/`-app`/`-server`-Binaries mehr. Laden zuerst, andere beim nächsten Anfassen.

### Thread G: Oberflächen (Nutzer, 2026-11-08; neuer Tab)
Reihenfolge: **People** (mit Facette Contacts, ADR 0061/0063), **Groups**, **Maps**, **Whiteboard**, **Files** (mit Facette Gallery). Jede App über Cap'n Proto am Server ihres Programms, auf `fs-components`, mit dem Blinc-Patch (`blinc-app-fix`, rev 1c5d217). Jede App ein Binary `fs-<programm>` (ADR 0063), Admin-Frontend (ADR 0061), Paket über `fs-release`, Eintrag im Katalog `fs-catalog` (mit Thread S abstimmen), damit der Nutzer sie **aus dem Store installiert**. Reihenfolge je Stück: Trait, Muster, Tests, Umsetzung; zweite Prüfung vor dem Tag. Erst läuft eine App wirklich, dann die nächste. Texte über `words`.

### Zusatz für Thread S (Nutzer, 2026-11-08)
- **Programme aus dem Store installieren ist Ziel Nr. 1**, der Nutzer will nichts mehr von Hand herunterladen.
- **Updates von selbst:** Jedes installierte Programm weiß, woher es kommt (Quelle und Katalog im Installationsregister des Stores). Vorschlag Strategie, vorläufig: Der Store prüft regelmäßig (systemd-User-Timer bzw. beim Start) und aktualisiert alle Programme selbst, mit TUF-Prüfung und Rücksprung; ein Programm fragt beim Start den Store über `store.capnp` („gibt es ein Update für mich?“) und zeigt einen Hinweis. Kein Programm lädt selbst herunter (eine Stelle der Wahrheit). Abschalten je Programm möglich.

### Zusatz für Thread R (Nutzer, 2026-11-08), nach Calendar/Wiki
Wiki-Vertrag `texts.capnp` erweitern nach `docs/en/programs/apps/wiki/requirements.md` (Tabelle „Required“): Versionsgeschichte lesen und wiederherstellen, Papierkorb mit Wiederherstellen, Bereiche/Ordner mit Reihenfolge, Vorlagen und Weiterleitungen, Suche mit Ausschnitten und Filtern; `editIf`-Konflikt als typisiertes `Problem`. Erst Trait, dann Muster, dann Tests, dann Kern und Server.

### Zusatz für Thread U (Nutzer, 2026-11-08), nach seiner Liste
ADR 0058 „Verknüpfen“ in `fs-people`: Profile mit oder ohne Person; Vorschlag bei passenden Daten (Telefon, E-Mail, …) nur mit Rückfrage; selbst verknüpfen und lösen; Übernahme nach Freigabe ist ein eigener Schritt (noch nicht bauen, nur Schnittstelle vorsehen). Trait, Muster (Specification + State), Tests, Umsetzung.

### Zusatz für Thread D (Nutzer, 2026-11-08)
Recherche mit Haiku: **Marketplace** (Verschenken, Tauschen, Leihen, auch Verkaufen; Kleinanzeigen-artig). Standards prüfen: ValueFlows (REA, Schenk- und Tauschwirtschaft), schema.org `Offer`/`Demand`, ActivityStreams/ActivityPub (FEPs zu Marktplätzen), GoodRelations. Vorhandene Seiten `docs/*/programs/suites/marketplace/` lesen. Ergebnis `temp/research/marketplace-standards.md`, jede Aussage mit Quelle. Noch kein Code.

### Thread M: Messenger (startet nach der Meldung „Umbenennung fertig“ von Thread R)
1. **Mail-Schlüssel (Nutzer, 2026-11-07):** v6 für unsere eigenen Schlüssel, v4 zusätzlich anbieten, damit GnuPG und RNP lesen können. Branch `mail-v4` (`460c6a6`) ist nur eine ungeprüfte Sicherung: prüfen, neu aufsetzen wo nötig.
2. `matrix` zu v0.4.0: `prev_content`-Nachweis nur für Räume des eigenen Servers; verdrängter Raum aus `away` (über 256) gilt als nie angenommen und wird neu geprüft (Strategie, vorläufig, „im Zweifel zu“).
3. v0.3.1 (Open point 17); Vertragswert `readsSensitive` ans Ende von `ToolCallRisk`; Geheimnisregel: vor dem Vergleich normalisieren (Unicode UTS #39: NFKC, Kleinschreibung, verwechselbare Zeichen), Wörter `passwd`, `pwd`, `pin`, `seed`, `mnemonic`, `private` dazu.
4. ADR 0054 „KIs in Unterhaltungen“ (4c oben): Hinweis vor dem Eintritt, alle stimmen zu, kein Verlauf von vorher, Zustimmung zurückziehen = KI hinaus.

### Thread U: Umfragen (startet nach der Meldung „Umbenennung fertig“ von Thread R)
1. Offene Umfragen nach `docs/en/programs/apps/surveys/design.md`, Abschnitt „Open surveys“ (Nutzer, 2026-11-07): jeder darf antworten, kein Nachweis; Frage „Bist du eine KI?“; Auswertung der Muster (Antwortzeit, gleiche Freitexte, Honeypot-Feld, gleiche Wahl in jeder Zeile, Häufung) wird gezeigt, nie still aussortiert; freiwillige Angaben danach. Ersetzt die Regel „ohne Person vom Host = KI“ auf `ai-participants`; danach `ai-participants` mergen und taggen.
2. Brücke `AiMarking` in `fs-groups` über `is_ai_role()` (mit Test für Kurz-ID und volle IRI).

## Die Threads (Runde 1, abgeschlossen)

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
1. **Muster zuerst:** Eines aus `conventions/coding.md` §2 aussuchen und in einem Satz begründen. Passt keines, nicht eines erfinden, sondern der Strategie melden. **Muster und Trait sind gleich wichtig (Nutzer, 2026-11-08).** Gibt es einen Standard, ist er der Trait: die Schnittstelle folgt ihm.
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

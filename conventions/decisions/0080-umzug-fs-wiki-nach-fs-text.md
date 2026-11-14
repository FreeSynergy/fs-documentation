# 0080 – Umzug fs-wiki → fs-text: Repo, Crates, Version, Daten, Katalog

Status: **akzeptiert** (Strategie, 2026-11-14; Nutzer-JA zu Umbenennung/Löschen und zum Wort „Projekt“; die übrigen Punkte F sind Strategie-Entscheide) · setzt ADR 0076 §5 Punkt 3 um · baut auf ADR 0031/0034 (Textstruktur), 0061 (Facetten), 0063 (ein Befehl), 0064 (Versionen), 0072 (Handbuch als Blöcke), 0077 (Katalog-Arten)

## Kontext
ADR 0076 ordnet die Repositories ein. Wörtlich:

| Repository | Art | Rolle im Modell | Änderung |
|---|---|---|---|
| fs-wiki | **wird Facette von fs-text** | — | Wiki-Code wird der Kern von fs-text (Umbenennung, Schritt 3) |
| **fs-text** | **neu: Programm** | Dokumente aus Text (ODF `.odt`); Facette Wiki | Repository anlegen |

Punkt 5.3 verlangt die Umbenennung „als eigene, geprüfte Schritte, mit Weiterleitung, Katalog und Paketnamen“. Ist-Zustand: `fs-wiki` hat 7 Crates (ca. 46 000 Zeilen Rust), Tags bis v0.0.10, Branch `release-0.0.11` noch nicht veröffentlicht. Die Kern-Bibliothek heißt dort schon `fs-text`. Das Repo `fs-text` existiert als Platzhalter (README, DESIGN, Lizenzen, check.yml), ohne Code und ohne Tags.

## Entscheidung
- **F1 Weg „umbenennen“.** Das Platzhalter-Repo `fs-text` wird **gelöscht** (Nutzer: wird nicht gebraucht); sein Inhalt wird vorher gesichert und Brauchbares in den DESIGN-Abschnitt von fs-text übernommen. Fehlt das Löschrecht (`delete_repo`), wird es nach Konvention in `fs-text-archive` umbenannt. Danach wird `fs-wiki` in `fs-text` umbenannt (Tags, Releases, Issues, Weiterleitung bleiben). Der Nutzer hat Löschen/Umbenennen freigegeben; bis zur Veröffentlichung von 0.0.11 ändert niemand etwas an den Repos. Nach der Umbenennung wird **nie** wieder ein Repo `fs-wiki` angelegt (sonst bricht die Weiterleitung; der Name ist als Facettenbefehl reserviert, ADR 0063).
- **F2 Crates.** Kern-Bibliothek `fs-text-model` (Dokument, Block, Verlauf, Links); Programm-Crates `fs-text-core`, `fs-text-server`, `fs-text-client`, `fs-text-app`; Binärdatei `fs-text`, `fs-wiki` bleibt als Link (argv[0], ADR 0063).
- **F3 Version.** Die Zählung wird fortgesetzt (Crate-Version = Tag, ADR 0064); keine neue Zählung ab v0.0.1, weil die alten Tags im selben Repo liegen.
- **F4 Thema.** Ein Thema `texts`; das Wiki-Eigene (ADR 0072, `WikiProvider.blocks`) wird Fähigkeit darin. Die Ausarbeitung ist ein Folge-ADR.
- **F5 Wortwahl.** Code `shelf`; Oberfläche de „Projekt“, en „Project“ (Nutzerwort; Nachtrag in ADR 0034).
- **F7 Zeitpunkt.** Der Umzug beginnt erst **nach** der Veröffentlichung von wiki 0.0.11.
- **F8 Facetten.** Keine eigenen Repos für Facetten; sie leben in fs-text (ADR 0061), je Facette später ein Katalogeintrag.
- **Datenregel.** Nutzerdaten (Daten, Entwürfe, Socket) werden **kopiert, nie verschoben oder gelöscht**; der alte Stand bleibt lesbar. Der Store muss den Umzug als **Update** erkennen; das ist **vor dem ersten Release als fs-text zu belegen**, sonst entsteht eine Doppelinstallation.

## Umzugsschritte (Reihenfolge fest)
1. **0.0.11 veröffentlichen** (Tag, Release, Katalog). Rückweg: entfällt.
2. **Pakete im alten Repo umbenennen** (Branch): Lib → `fs-text-model`, `fs-wiki-*` → `fs-text-*`, Bin `fs-text` mit Link `fs-wiki`; CI-Dateien (release, typing-test, windows) anpassen. Test: alle Gates. Rückweg: Branch verwerfen.
3. **Repos umbenennen** (nach 0.0.11): Platzhalter `fs-text` sichern und löschen (ersatzweise → `fs-text-archive`), dann `fs-wiki` → `fs-text`; Brauchbares in DESIGN. Rückweg: zurückbenennen (solange `fs-wiki` frei bleibt); der gelöschte Platzhalter ist nur aus der Sicherung wiederherstellbar.
4. **Release-Kette:** Allowlist (`fs-text` neben `fs-wiki`), `binaries`/`cargo-package`/`name` auf `fs-text`; Trockenlauf.
5. **Datenkopie** (Ordner, Entwürfe, Socket `wiki.sock` → `text.sock`, Client probiert beide); Test mit Fixture von 0.0.10, byte-genau. Muss vor Schritt 6 fertig sein.
6. **Erstes Release als fs-text** (erst wenn `replaces` in Katalog und Store fertig ist, siehe Folgen) (nächster Tag der Zählung) und **Katalog** (siehe Folgen). Rückweg: Release zurückziehen, Katalog zurücksetzen.
7. **Doku und Pins:** fs-documentation, `fs-interfaces`-Eigner von `texts.capnp`, Verweise in ADR-Statuszeilen (ADR-Texte werden nicht umgeschrieben, nur Folge-ADR).

## Folgen
- **Katalog-ID:** Eintrag `fs-text` (Programm) mit `repo = FreeSynergy/fs-text`, Asset `fs-text-{version}-linux-x86_64.tar.gz`; Facette Wiki als eigener Eintrag (ADR 0061 §7). Der Eintrag `fs-wiki` bleibt in der Übergangszeit.
- **Paketnamen:** rpm/deb/AppImage heißen `fs-text`; Update-Pfad siehe Belege.
- **CI:** `release.yml` (`binaries`, `cargo-package`, `ignore-binaries`, `name`), `typing-test.yml` (`-p`), `windows.yml` (`-p fs-wiki-*`).
- **Doku:** neue Programmseite `text`, Wiki-Frontends darunter; 21 Dateien mit „fs-wiki“ prüfen.
- **Pins:** in anderen Programmen wurde keine Abhängigkeit von der Crate `fs-wiki` gefunden (nur Wiki-Worktrees; ungeklonte Repos nicht geprüft).
- **fs-components** behält die Wiki-Bausteine (programm-neutral; sonst Zyklus).

### Belege zur Umbenennung als Update (gelesen 2026-11-14)
| Stelle | Befund | Stand |
|---|---|---|
| AppStream `<replaces/>` | „a component completely takes over from another one … typically used when a component has to change its ID“; Anbieter sollen die Tags „carefully“ filtern (sinngemäß, Spezifikation 2.1.3) | belegt |
| AppStream `<provides><id/>` | enthält die Komponenten-ID einer anderen Komponente; nützlich, wenn eine ID umbenannt werden musste; Behandlung durch Software-Center nicht beschrieben | belegt (Spezifikation), Wirkung **nicht belegt** |
| deb | Debian Policy 7.6: `Replaces` mit `Conflicts` bzw. `Breaks`; „A virtual package is one which appears in the Provides control field of another package“ | belegt |
| rpm | `rpm-dependencies(7)`: „Obsoletes: Packages obsoleted by a package. Used for replacing and renaming packages.“ | belegt |
| fs-catalog (`packages.toml`, `scripts/schema_base.py`, `gen_catalog.py`) | kein Feld für Ersatz/Umbenennung; `<provides>` nur mit `<mediatype>`; `fs:provides` meint Fähigkeiten, nicht IDs (`CHANGES-FOR-STORE.md`: „`<provides><mediatype>` (AppStream): not read“) | belegt (Fehlen) |
| fs-store (Stand store-016) | Suche nach `replaces`, `obsolet`, `replaced`, `provides` im Quelltext: keine Ersatz-Logik; „installiert“ wird über den Namen erkannt (`current/<name>`, `installed.toml`, rpm-Abfrage nach Name); `fs-wiki` steht in `demo_data` und Tests | belegt (Fehlen) |

**Entscheidung (Strategie):** Heute würde `fs-text` neben installiertem `fs-wiki` erscheinen. Darum: (a) Katalogfeld `replaces = ["fs-wiki"]`, in `catalog.xml` als `<replaces><id>fs-wiki</id></replaces>`, mit Prüfung in `gen_catalog.py` (ID bestand im Katalog, gleicher Eigner); (b) der Store zeigt `fs-text` als **Update**, wenn eine ID aus `replaces` installiert ist; die Daten werden **kopiert**, nie verschoben; (c) Pakete: rpm `Obsoletes: fs-wiki` und `Provides: fs-wiki`, deb `Replaces`/`Breaks: fs-wiki` und `Provides: fs-wiki`. Das Feld ist Teil von **Schema 2** (`min_store`, ADR 0077) und **Pflicht vor Schritt 6** des Umzugs.

## Alternativen
- **Neues Repo `fs-text` mit Code, `fs-wiki` archivieren:** verworfen; Historie, Tags, Releases und Issues bleiben getrennt, Weiterleitung entfällt.
- **Platzhalter nur umbenennen statt löschen:** nur Rückfall, falls das Löschrecht fehlt (F1).

## Risiken
- Laufende Veröffentlichung 0.0.11 vermischt sich mit dem Namenswechsel (darum F7).
- Doppelinstallation oder „nicht gefunden“ im Store ohne Umzugslogik.
- Menschen-Daten: Kopie fehlerhaft oder unvollständig (darum Fixture-Test, nie löschen).
- Weiterleitung bricht, wenn je wieder ein Repo `fs-wiki` entsteht.
- Signatur-/Prüfsummenkette mit neuem Asset-Namen neu erzeugen.

## Offen [nicht belegt]
- Weiterleitung von **Release-Assets** nach der GitHub-Umbenennung (nur Clone/Web-Weiterleitung angenommen; Test mit Download nötig).
- Wirkung von `<replaces>`/`<provides><id>` in gängigen Software-Centern.
- Umsetzung von `replaces` (entschieden, noch nicht gebaut): Katalog, Schema 2, Store-Erkennung und Datenkopie, Tests mit alter und neuer ID.
- Doku-Weiterleitungen alter Pfade `apps/wiki/…` (Redirect-Plugin in mkdocs nicht belegt).
- Unterstützung von `Obsoletes`/`Replaces` in unserer eigenen Paketlinie (ADR 0078).

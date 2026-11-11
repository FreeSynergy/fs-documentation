# Teil C: Install und Paketbau als Workflow (Entwurf, nur Ableitung aus dem Code)

Stand: fs-store `ea4f359` (lokal, Worktree `/srv/FreeSynergy/.wt-store-par`, Basis v0.0.11). Zeilen = dieser Stand, Pfade relativ zu `crates/`.
Kein gemeinsames Format festgelegt: die Spalten sind nur Inhalt. Handelnde: **Programm** (Store-Prozess), **Maschine** (dnf/apt/systemd/Compositor), **Mensch** (Bestätigung).
Risikostufen: 1 ansehen < 2 öffnen < 3 starten < 4 installieren < 5 systemweit. Kürzel: E = `fs-store-engine/src`, A = `fs-store-app/src`, C = `fs-store-cli/src`, K = `fs-store-core/src`.

## 1. Installieren / Aktualisieren (tar.gz; Update = gleiche Liste mit `previous = Some(v)`)

| # | Befehl | Parameter | Vorbedingung | Rückgängig | Stufe | Klartext-Vorschau | Handelnder | Code |
|---|---|---|---|---|---|---|---|---|
| 1 | `quelle.lesen` | Quell-URL | Quelle aktiv | – (nur Zwischenordner) | 1 | „Die Paketliste von <Quelle> wird geladen.“ | Programm | E/net.rs:76 `clone_catalog`; A/engine.rs `read_source` |
| 2 | `katalog.pruefen` | Katalog, .asc | – | – | 1 | „Die Liste wird gegen den Projektschlüssel geprüft.“ | Programm | E/prepare.rs:79-84; Frische `serials.toml`: `fs-store-sources/src/serials.rs:90` |
| 3 | `angebot.waehlen` | Name, installierte Version | Eintrag vorhanden; nicht älter als installiert (`Downgrade`); Format unterstützt | – | 1 | „<Name> <Version> wird als <Format> geholt.“ | Programm | E/prepare.rs:88-133 |
| 4 | `datei.laden` | URL Datei + .asc | Netz | temporäre Bytes im Speicher verwerfen | 1 | „<n> MiB werden heruntergeladen.“ | Programm | E/prepare.rs:146 |
| 5 | `datei.pruefsumme` | Datei, sha256 | 4 | – | 1 | „Die Prüfsumme wird verglichen.“ | Programm | E/prepare.rs:170 |
| 6 | `datei.signatur` | Datei, .asc, Schlüssel | 5 | – | 1 | „Die Signatur wird geprüft; ohne gültige Signatur wird nichts installiert.“ | Programm | E/prepare.rs:175-192 (`admit` -> `VerifiedPackage`, K/signature.rs) |
| 7 | `dienst.beenden` | Name, Wartezeit 35 s | läuft `fs-<name> serve` (Befehlszeile, gleicher Nutzer) | `dienst.starten` mit denselben Argumenten (nur bei Fehlschlag) | 3 | „Der Hintergrunddienst von <Name> wird beendet.“ | Programm -> Dienst (`Control.stop`, sonst SIGTERM) | E/batch.rs:86-104, E/end.rs:179, E/servers.rs |
| 8 | `programm.nicht_laufend` | Name | kein Prozess mit `exe` unter `packages/<name>/` (eigene PID ausgenommen) | – | 1 | „<Name> darf nicht geöffnet sein.“ | Programm | K/update.rs:47, E/proc.rs, E/batch.rs:133-144 |
| 9 | `ordner.entpacken` | Archiv, Ziel `packages/<name>/<v>.tmp<pid>` | 6; Name schlicht; Ziel-Version noch nicht da | Temp-Ordner löschen | 4 | „<Name> wird in <Ordner> entpackt (Links im Archiv werden abgelehnt).“ | Programm | E/targz.rs:119-157 (Grenzen 4 GiB / 100 000 Einträge) |
| 10 | `ordner.einsetzen` | tmp -> `packages/<name>/<v>` | 9 | Ordner entfernen (nur bei Erstinstallation; sonst bleibt die Version liegen) | 4 | „Die Version <v> liegt bereit.“ | Programm | E/targz.rs:187 |
| 11 | `version.umschalten` | `current/<name>` -> Ziel | 10 | `version.umschalten` auf `previous`, bzw. Link löschen (Erstinstallation) | 4 | „<Name> wird auf <v> umgestellt (die alte Version bleibt liegen).“ | Programm | E/targz.rs:80-87, 193; Gegenstück `restore` 197-214, aufgerufen von K/update.rs:59 |
| 12 | `dienst.alt_beenden` | Name | nach 11 | – | 3 | „Ein noch laufender alter Dienst wird beendet.“ | Programm | E/ending.rs:53, E/batch.rs:113-115 |
| 13 | `register.eintragen` | Name, Version, Quelle, auto_update | 11 gelungen | `register.vergessen` (alter Eintrag nur über erneutes `record` zurück) | 2 | „<Name> <v> wird in der Liste der installierten Programme vermerkt.“ | Programm | A/engine.rs:112-128, `fs-store-sources/src/registry.rs:74,115-125` (atomar: tmp + rename) |
| 14 | `symbol.ablegen` | Name, PNG, sha256 | PNG <= 1 MiB, Hash stimmt | Datei löschen | 4 | „Das Symbol wird abgelegt.“ | Programm | E/icons.rs (nur in C/batch.rs:149 aufgerufen, nicht in der Fenster-Installation) |
| 15 | `befehl.verknuepfen` | Name, Facetten, bin-Ordner | 11; Programmdatei `<n>` oder `<n>-app` da | `befehl.entfernen` (nur eigene Links) | 4 | „Der Befehl fs-<name> wird in ~/.local/bin eingerichtet.“ | Programm | E/facets.rs:66-97; `links.rs:70` (`link_programs`) |
| 16 | `menue.eintragen` | Befehl, Anzeigename, Symbol | 15; Datei fehlt oder trägt `X-FreeSynergy-Managed=true` | `menue.entfernen` | 4 | „Der Menüeintrag FreeSynergy.<Name> wird angelegt.“ | Programm | E/facets.rs:97-115 |
| 17 | `register.facetten` | Facetten die wirklich gelangen | 15 | wie 13 | 2 | – | Programm | A/engine.rs:122 |

Native Variante (rpm/deb) ersetzt 9-11 durch:

| 9n | `paket.schreiben` | Dateien, privater Ordner `0700`, Dateien `0600`, `O_EXCL|O_NOFOLLOW` | 6 | Dateien löschen (immer, auch bei Fehler) | 4 | „Das geprüfte Paket wird in einen privaten Ordner gelegt.“ | Programm | E/native.rs:13-44 |
| 10n | `paket.installieren` | `pkexec dnf install -y --setopt=metadata_expire=never <Dateien>` bzw. `pkexec apt-get install -y --no-remove <Dateien>`; EIN Aufruf für alle Pakete der Sammlung | 9n; 8 | **keins** (`restore` ist leer, E/rpm.rs:138): Gegenstück wäre `paket.entfernen`, aber nur als bewusste Entscheidung des Menschen | 5 | „Das Paket wird systemweit mit dnf/apt installiert; Sie bestätigen das Administratorpasswort.“ | Maschine; **Mensch** (pkexec-Passwort) | E/rpm.rs:115-136, E/deb.rs, E/batch.rs:173-200 |

Sammelschritt: die Schritte 7-12 laufen je Sammlung (Batch), nicht je Paket (alle rpm in einem Aufruf); 4-6 laufen je Paket parallel (`prepare_all`, C/batch.rs).

## 2. Entfernen (`uninstall`, Fenster und CLI)

| # | Befehl | Vorbedingung | Rückgängig | Stufe | Klartext-Vorschau | Code |
|---|---|---|---|---|---|---|
| R1 | `programm.nicht_laufend` | wie 8 (tar.gz) | – | 1 | „<Name> darf nicht geöffnet sein.“ | E/remove.rs:34 |
| R2 | `version.abmelden` (Link `current/<name>` löschen) | Link vorhanden | `version.umschalten` | 4 | „<Name> wird abgemeldet.“ | E/remove.rs:38 |
| R3 | `ordner.loeschen` (`packages/<name>/` mit ALLEN Versionen) | R2 | **keins** (Neuinstallation aus dem Katalog; alte Versionen sind weg, auch die Rückfallstufe) | 4 | „Alle Dateien von <Name> werden gelöscht; Ihre Daten bleiben.“ | E/remove.rs:39 |
| R3n | `paket.entfernen` = `pkexec dnf remove -y <n>` / `apt-get remove` | System-Paket erkannt (`rpm -q`/`dpkg`) | Installation 10n | 5 | „Das Paket wird systemweit entfernt (Passwort nötig); Ihre Daten bleiben.“ | E/rpm.rs:148, E/deb.rs, E/mode.rs:170 |
| R4 | `befehl.entfernen` (Links nach `current/<n>`) | – | 15 | 4 | „Die Befehle werden entfernt.“ | E/links.rs:115 |
| R5 | `befehl.entfernen` Facetten + `menue.entfernen` (nur `X-FreeSynergy-Managed=true`) | Facetten aus `installed.toml` | 15, 16 | 4 | „Menüeinträge von <Name> werden entfernt.“ | E/facets.rs:123-147 |
| R6 | `register.vergessen` | – | 13 | 2 | „<Name> wird aus der Liste entfernt.“ | `registry.rs:107`; A/engine_remove.rs:11-37, C/updates.rs:37-63 |

## 3. Weitere Abläufe, die der Store heute hat

- `zeitgeber.einrichten`: zwei systemd-User-Dateien schreiben, `systemctl --user daemon-reload`, `enable --now` (Stufe 4; Gegenstück `disable --now` + Dateien löschen): C/updates.rs:155-205.
- `menue.eigener_eintrag`: Eintrag „FreeSynergy.Store“ beim ersten Fensterstart (Stufe 4; nie über fremde Datei): E/facets.rs:166.
- `programm.neustart`: eigene Datei neu starten (Stufe 3): E/mode.rs:183 (Auslöser fehlt noch, siehe Befund Update/Neustart).
- `hinweis.senden`: `notify-send`, Starter-Zähler per `gdbus` (Stufe 2, best effort): C/background.rs:136.

## 4. Paketbau als Umkehrung

Eingabe: ein Quellordner oder ein installierter Zustand (`packages/<name>/<v>/`, `current/<name>`, `installed.toml`, Links, Menüeinträge). Ausgabe: Paket + Katalogeintrag + Signaturen.

Spiegelpaare (Installieren <-> Bauen):

| Installieren | Bauen (Spiegel) | Anmerkung |
|---|---|---|
| `ordner.entpacken` (9) | `ordner.packen`: Dateien in `<name>-<v>/` als tar.gz, nur Dateien/Ordner, keine Links, Grenzen prüfen | Der Entpacker lehnt Links ab; der Packer muss sie vor dem Bau ablehnen, sonst entsteht ein Paket, das der Store nie installiert |
| `datei.pruefsumme` (5) | `datei.pruefsumme.berechnen` -> `<checksum type="sha256">` | Katalog-Feld |
| `datei.signatur` (6) | `datei.signieren` (losgelöstes OpenPGP, Unterschlüssel) -> `fs:signature` | Die Probe mit der echten Datei (`FS_PROBE_FILE`) ist der Beweis, dass beide Seiten denselben Schlüssel kennen (Lehre rc.1) |
| `katalog.pruefen` (2) | `katalog.signieren` + `fs-serial`/`fs-expires` setzen | `fs-catalog/scripts/gen_catalog.py`, Wochenlauf |
| `befehl.verknuepfen` / `menue.eintragen` (15, 16) | `facetten.deklarieren`: aus den Links/Menüeinträgen `fs:facets` ableiten; Symbol -> `<icon type="remote" fs-sha256>` | Eintrag ist das Spiegelbild der Links |
| `symbol.ablegen` (14) | `symbol.hashen` | |
| `paket.installieren` (10n) | `paket.bauen_rpm/deb` (`cargo deb --no-strip`, rpm im `fs-release`) | gleiche Binärdatei wie im tar.gz (R5 von v0.0.9) |
| `angebot.waehlen` (3) | `eintrag.schreiben`: Version, Datum, Änderungstext, Größe, Fähigkeiten, Herkunft | die neuen Felder aus `Details` |

Keine Spiegel (nur beim Installieren sinnvoll, hängen am Zustand der Maschine): `version.umschalten`, `dienst.beenden/starten`, `programm.nicht_laufend`, `register.eintragen`, `menue.eigener_eintrag`, `zeitgeber.einrichten`.
Bauen-only: Spiegeln fremder Pakete (Upstream-Signatur prüfen, Quellcode mitnehmen, ADR 0068 §2), Fähigkeiten ableiten (`fs:provides`: aus den Schnittstellen, die das Programm bedient).

Ableiten aus dem Quellordner (nicht aus dem Installierten) braucht ein Manifest; heute gibt es keins: Name, Art, Format, Facetten, Fähigkeiten stehen verstreut (Cargo.toml, `fs-release`-Workflows, `fs-catalog/packages.toml`). Ein Workflow-Schritt `paket.beschreiben` hätte zuerst diese Quelle der Wahrheit festzulegen.

## 5. Lücken: was heute im Code versteckt ist und in einer deklarativen Schrittliste fehlen würde

1. **Zwei Kopien der Ablaufsteuerung.** CLI (`C/batch.rs:149-159`, `C/updates.rs:37-63`) und Fenster (`A/engine.rs:112-128`, `A/engine_remove.rs`) wiederholen die Schritte (der Kommentar dort sagt es). Sie weichen ab: Reihenfolge `link_programs` vs. `link_facets` ist verschieden; `symbol.ablegen` läuft nur in der CLI, das Fenster liest das Symbol nur (`A/engine.rs:225-231`). Eine Schrittliste würde diese Abweichung sichtbar machen; sie ist ein Fehler in sich.
2. **Stille Teilschritte (`let _ =`).** Verknüpfen, Register, Entfernen der Links schlagen still fehl und lassen den Auftrag „erfolgreich“. Eine Liste braucht je Schritt „darf scheitern“ und eine Meldung.
3. **Rückgängig ist nur für tar.gz da.** rpm/deb haben kein Gegenstück (E/rpm.rs:138), `ordner.loeschen` (R3) ist unumkehrbar und nimmt auch die alten Versionen mit; `packages/<name>/` wächst dagegen ohne Aufräumschritt.
4. **Seiteneffekt in einem „Ansehen“-Schritt.** Das Lesen der Quelle schreibt `serials.toml` (Rückfall-/Frische-Merker, `serials.rs:90`): Stufe 1 ist nicht rein lesend.
5. **Implizite Vorbedingungen als Prädikate:** „Name ist ein schlichter Dateiname“ (`PackageName`), „fremde Datei nie ersetzen“ (`ours()` in links.rs/facets.rs), „Menüeintrag nur mit `X-FreeSynergy-Managed=true`“, „nie SIGKILL, nie PID <= 1, nie die eigene PID“ (end.rs), „Programm läuft“ per `/proc` (sieht rpm/deb unter `/usr` nicht, DESIGN.md Zeile 103). Das sind Regeln, keine Schritte; sie gehören in die Vorbedingungen des Befehlssatzes, nicht in den Aufrufer.
6. **Format- und Plattformwahl** (`preferred_format`, `fits_this_machine`, rpm-Besitz per `rpm -qf`) entscheidet schon im Plan, welche Schrittfolge gilt (tar.gz vs. native). Die Schrittliste ist also eine Verzweigung, nicht eine Zeile.
7. **Sammel- statt Einzelschritt:** alle rpm/deb einer Sammlung in einem `pkexec` (ein Passwort); Ausfall = gleiche Ursache für alle. Ein Workflow-Schritt „je Paket“ kann das nicht ausdrücken.
8. **Umgebung als stille Parameter:** `FS_STORE_BIN`, `FS_STORE_APPS`, `FS_STORE_ROOT`, `HOME`, `FS_STORE_TUF_ROOT`; Zeitgrenzen (35 s Dienst beenden, 5 s je Aufruf, 4 GiB/100 000 Einträge, 512 MiB Download).
9. **Quelle der Fähigkeiten fehlt:** `requires` aus ADR 0068 ist noch keine Vorbedingung des Installierens (`resolve` ist gebaut, aber nirgends aufgerufen).
10. **Registerdaten sind unvollständig:** `Package.source` wird fest mit `"catalog"` gefüllt (E/prepare.rs:187); Signierer und Format stehen nicht im Register, nur im Auftrag.
11. **Zwei Handelnde in einem Schritt:** `pkexec` ist Mensch-Bestätigung innerhalb eines Maschinenschritts; die Vorschau muss vor dem Passwort stehen, nicht danach.
12. **Datenregel negativ:** „Daten des Menschen werden nie entfernt“ steht nur in Kommentaren; als Regel an jedem Entfernen-Schritt.

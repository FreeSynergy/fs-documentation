# Befund: Update schliesst ein laufendes Programm und startet es am selben Punkt neu

Stand: 2026-11-11, nur lesend geprueft. GitHub-Links: `https://github.com/FreeSynergy/<repo>/blob/main/<pfad>`
(Zeilennummern = lokaler Stand in /srv/FreeSynergy; fs-interfaces lokal auf Tag v0.0.17, fs-components Linie v0.3.0).

Korrektur zur Aufgabe: `end.rs` und `ending.rs` gibt es in fs-store-engine nicht. Die Logik steckt in `proc.rs` (Laufend-Pruefung),
`servers.rs` (Hintergrund-Server), `batch.rs` (Ablauf), `mode.rs`, `links.rs`. `call_limited` ist NICHT in main/v0.0.17, nur im Arbeitsbaum
`/srv/FreeSynergy/.wt-fsif18` (Branch `v0-0-18`, Commit 5fa4a8f, `crates/fs-interfaces/src/rpc/client/limited.rs`).

## 1. Was heute passiert

### 1a. Laufendes Fenster (Frontend)
- Der Store beendet und startet ein Fenster **nicht**. Er erkennt es nur und **lehnt das Update ab**:
  - `ProcRunningCheck::is_running` prueft `/proc/*/exe` unter `<root>/packages/<name>/`, eigene PID ausgenommen:
    https://github.com/FreeSynergy/fs-store/blob/main/crates/fs-store-engine/src/proc.rs (`/srv/FreeSynergy/fs-store/crates/fs-store-engine/src/proc.rs:34-46`).
  - `run_update` gibt `UpdateError::Running` zurueck: `fs-store-core/src/update.rs:44-49` (Enum Zeile 18-21).
  - Text: `fs-store-core/src/words.rs:24` "is running and was not replaced. Close it and try again."
  - Im Batch: `fs-store-engine/src/batch.rs:131-140` (rpm vorab), tar.gz ueber `run_update` (Zeile 148-157).
- Luecke rpm: Die Laufend-Pruefung sieht Programme unter `/usr` nicht (`fs-store/DESIGN.md:103`). Ein rpm-Update ersetzt ein laufendes Fenster ohne Pruefung;
  es laeuft auf dem geloeschten Inode weiter; `own_exe` schneidet `" (deleted)"` ab (`mode.rs:11-23`).
- tar.gz: Umschalten ist ein atomarer Symlink-Wechsel `current/<name>` (`targz.rs:22-25, 85`), alte Version bleibt liegen. Ein laufendes Fenster waere
  technisch nicht gefaehrdet, wird aber trotzdem blockiert.

### 1b. Hintergrund-Server (Backend, `fs-<name> serve`)
- Wird unterschieden: `is_server_of` erkennt `<name> serve ...` an der Kommandozeile (`servers.rs:23-29`); `find_servers` liest `/proc/*/cmdline`, nur gleicher Nutzer (32-58).
- Ablauf `commit_observed` (`batch.rs:76-109`): SIGTERM per `kill -TERM` (`servers.rs:79-95`, nie SIGKILL), bis 15 s warten, installieren,
  Server mit denselben Argumenten aus der alten cmdline neu starten (`start_server` 100-110, `program_of` 115-132), auch wenn die Installation fehlschlug.
  Endet er nicht rechtzeitig: `UpdateError::Running` (`batch.rs:90-95`).
- **Der Store nutzt `Control.stop` nicht** (nur SIGTERM). `Control.stop`/`Control.version` stehen im Schema
  (`/srv/FreeSynergy/fs-interfaces/schema/common.capnp:38-46`) und sind serverseitig umgesetzt (`rpc/serve.rs:164-199` `run_until_signal_as`, `rpc/control.rs`, `rpc/stop.rs` `stop_self`).
  Gebraucht werden sie vom **Fenster beim Start**: `connect_matching` (`rpc/handshake.rs:30-90`) fragt `Control.version`, stoppt einen abweichenden Server, startet den passenden
  (`ServerStarter`/`CommandStarter`, `rpc/starter.rs`), verbindet neu. Das ist die vorhandene "Server-Austausch beim naechsten Fensterstart"-Schiene.
- `--lease FILE`: Server endet, wenn kein Fenster mehr das Lock haelt (fs-files `fs-files-server/src/program.rs:38`, fs-people `.../program.rs:16`).
  Heute stoppt der Store nur den Server, ohne ein offenes Fenster zu beachten: das Fenster steht dann ohne Server da.

| | erkannt an | Update heute | Neustart danach |
|---|---|---|---|
| Server `serve` | cmdline | SIGTERM, 15 s, Austausch | ja, gleiche Argumente |
| Fenster | exe-Pfad in `packages/` | **abgelehnt** (`Running`) | nein |
| Store-Fenster selbst | eigene PID ausgenommen | wird ersetzt, laeuft alt weiter | nein, erst beim naechsten Start |

### 1c. Selbst-Update des Stores
- Ersetzen geht: eigene PID wird ignoriert (`proc.rs:1-31`); tar.gz: neue Version daneben, Symlink wechselt, das laufende Fenster bleibt auf alten (liegenbleibenden) Dateien.
  `~/.local/bin/fs-store` ist ein Symlink ueber `current/<name>/` (`links.rs:9-19, 30-62`) und zeigt danach von selbst auf die neue Version.
- **Neustart geht nicht:** kein "Jetzt neu starten", kein `spawn` der eigenen Datei. `fs-store/DESIGN.md:282` fuehrt es als **Offen**
  ("Window asks the program to 'save the session and restart' through the update hint (ADR 0065 point 7)").
- `update_hint` (`fs-store-client/src/hint.rs:51-70`) liest `updates.toml`; **kein Programm ausser dem Store benutzt ihn** (grep ueber fs-files/people/tasks/wiki: keine Treffer).
- Formate: `Format::{TarGz, Rpm}`; `.deb` gibt es im Code nicht. Windows: kein Store-Code (alles unix: `/proc`, `kill`, Symlinks). Nur `fs-interfaces` hat Windows-Transport
  (`rpc/transport/windows/`) und vermerkt in `control.rs`, dass Windows kein Signal zum Senden hat.
- Sonderfall Timer: `fs-store update --all` laeuft aus einem systemd-User-Timer (`fs-store-cli/src/updates.rs:167-168`), also **ohne Display**: Fenster-Neustart dort unmoeglich.

## 2. Gibt es Zustand speichern/wiederherstellen? Nein (ausser Entwuerfen)

- ADR 0065 (`origin/main:conventions/decisions/0065-standard-fensterhuelle.md`, Status "Vorschlag der Strategie bis zur Bestaetigung"): Punkt 7 verlangt, das Programm erkenne die ersetzte Datei
  und starte sich neu (Zustand vorher sichern) **oder** biete "Jetzt neu starten" an. Kein Format, kein Ort, kein Trait. "Folgen": Trait `Shell` (Name vorlaeufig).
  Sonst behandelt kein ADR/keine Doku (`conventions/decisions`, `docs/{de,en}/components`, `todo`) Session/Wiederherstellung von Ansichten.
- `fs-components-app` (`/srv/FreeSynergy/fs-components/crates/fs-components-app/src/`):
  - `Shell` (`shell.rs:24-182`): Titel, Screens, aktuelle Screen-ID (`select`, Zeile 76), Menues, Status, alles nur im Speicher. Kein `Session`-Typ.
  - `Surface` (`surface.rs:10-24`): nur `build(w,h)` und `styles()`; "a surface keeps its state outside the element".
  - `WindowOptions` (`window.rs:16-33`): nur Anfangsgroesse (1200x800); `launch` ohne gespeicherte Groesse/Position; `--size` (`args.rs`) ist das Einzige.
  - Keine serde-Abhaengigkeit in `Cargo.toml`. `write_new_file`/`write_new_private_file` (`new_file.rs:21-40`) legen nur neu an und **ueberschreiben nie**: fuer eine Sitzungsdatei nur Vorbild.
  - Einzige Wiederherstellung: Entwurfs-Backup in Reader und `message-composer` ueber vom Programm gestelltes `DraftStore` (`workbenches/src/reader/backup.rs:1-14`, `fs-components/DESIGN.md:32, 226`;
    Restore/Discard-Frage, nie von selbst zurueckgeschrieben, ADR 0046). Das ist Dokumentinhalt, nicht Ansicht.
  - Workbenches haben reine Zustandsautomaten (`calendar/widget.rs:8`, `people/view/mod.rs:1`): gute Basis. `Snapshot` in `shell/picture.rs` ist ein **Bild** (Tests/Export), kein Zustand.
- Programme (fs-files `gui.rs:8-82`, fs-people `gui.rs`/`args.rs`, fs-tasks `program.rs:31-43`): speichern keine Ansicht, Groesse oder Position; nur `--size`, `--socket`, `--store`.
- Sonstige Ablage: Nutzdaten `$XDG_DATA_HOME/freesynergy/<name>/` (files, people/tasks `app.db`); Sockets `$XDG_RUNTIME_DIR/freesynergy/<name>.sock`; Store-Einstellungen
  `~/.local/share/fs-store/{settings.toml,updates.toml}` (`hint.rs:29-37`); Timer unter `~/.config/systemd/user`. **Kein Programm nutzt `~/.config` oder `~/.local/state` fuer eigene Einstellungen**
  (`kdeglobals` wird nur gelesen, `window.rs:97-110`). Es gibt keine bestehende Einstellungs-Konvention.

## 3. Bewertung des Strategie-Vorschlags

Kern richtig: `Shell`/`Surface` ist der einzige Ort, den jedes Fenster durchlaeuft, Screens haben stabile IDs. Praezisierungen:
1. "Programme schreiben nichts selbst": fast. Workbenches aus fs-components liefern ihren Teil ohne Programmcode; eigene `Surface`-Implementierungen brauchen eine kleine Methode (Default: nichts).
2. **Der Store kennt Fenster nicht.** Fenster sind Clients ohne Socket; der Store findet sie nur ueber `/proc`. "Stopp-Anfrage" braucht einen Kanal ins Fenster (3.3).
3. ADR 0065 Punkt 7 (Weg A: Programm bemerkt ersetzte Datei, startet sich selbst) und der Vorschlag (Weg B: Store ruft) sind zwei Wege. A deckt auch `dnf upgrade` ausserhalb des Stores ab,
   B garantiert "Update schliesst und startet neu". Beide nutzen dieselbe Huelle-Funktion `suspend_and_exit()`; A zuerst bauen, B als Ausloeser darauf.
4. Ungespeicherter Text gehoert in den bestehenden `DraftStore`-Weg (ADR 0046), nicht in die Sitzungsdatei (sonst zwei Systeme fuer dasselbe Feld).
5. Fenster zuerst beenden, dann Server (heute umgekehrt/ignoriert), nach dem Install Server zuerst, dann Fenster.

### 3.1 Kleinste tragfaehige Schnittstelle

In `fs-components-app` (Namen vorlaeufig):

```rust
pub trait Restorable {
    fn state_key(&self) -> &str;          // stabil, z. B. "files.list"
    fn state_version(&self) -> u32;       // steigt bei inkompatiblem Wechsel
    fn save_state(&self) -> Option<serde_json::Value>;   // nur Ansicht: Auswahl per ID/Pfad (nie Index), Bildlauf (Offset + Anker-ID), Sortierung, Filter, Ausklappzustand
    fn restore_state(&self, version: u32, value: &serde_json::Value) -> Result<(), RestoreError>; // Fehler = verwerfen
    fn migrate(&self, _from: u32, _v: serde_json::Value) -> Option<serde_json::Value> { None }  // None = verwerfen
}
// Surface: fn restorable(&self) -> Option<&dyn Restorable> { None }
```
Die Huelle sammelt Fenster (Groesse, Position, maximiert), aktuellen Screen und je Screen `save_state()`.

Datei, ein Dokument je Programm:
`{ "schema":1, "program":"fs-files", "program_version":"0.6.0", "saved_at":"...", "window":{"w":1200,"h":800,"x":null,"y":null,"maximized":false}, "screen":"files", "parts":{"files.list":{"v":2,"data":{...}}} }`
- **Format:** serde + JSON. Zustand ist privat zum Programm (kein Austausch), lesbar, Formatwechsel je Teil leicht. capnp lohnt nicht, da nur ein Dateiname/Token ueber `Control` laeuft.
  Neue Abhaengigkeit (serde/serde_json) in fs-components-app; ggf. eigenes Crate `fs-components-session`, damit Server/CLI ohne Blinc es nutzen koennen.
- **Ort:** `$XDG_STATE_HOME/freesynergy/<name>/session.json` (Standard `~/.local/state/...`): Zustand ist weder Daten noch Konfiguration, nicht zu sichern/exportieren.
  Windows: `%LOCALAPPDATA%\FreeSynergy\<name>\state\session.json`. Schreiben: temp im selben Ordner, `fsync`, `rename`, 0600 (neue Funktion, `write_new_private_file` ueberschreibt nicht).
- **Versionierung:** `schema` (Huelle) plus `v` je Teil. Unbekanntes/zu altes `v` ohne Migration: **nur dieser Teil** verworfen (Standardwerte), Rest bleibt. Unbekanntes `schema` oder kaputtes JSON: ganze Datei verwerfen, normal starten, im Log vermerken.
  Programmversion nur zur Diagnose, keine Bedingung (Update ohne Formatwechsel soll wiederherstellen). Wiederherstellen darf den Start nie blockieren oder scheitern lassen.
- **Geheimnisse/Datenschutz:** nur was ein Component ausdruecklich meldet (Positivliste); Freitext standardmaessig nicht. Passwort-/Geheimnisfelder bekommen kein `Restorable`
  (in primitives/widgets gibt es heute kein Passwortfeld, grep ohne Treffer; Regel in ADR und Review-Liste verankern). Pfade/Namen der Auswahl sind persoenlich: 0600, lokal, nicht in Exporten/Backups ("save != export"),
  Menuepunkt "Sitzung vergessen", Maximalalter (z. B. 30 Tage, offen). Auswahl nur per stabiler ID; fehlt sie, still verwerfen.

### 3.2 Wann speichern/anwenden
- Pflicht: bei `suspend` (Update) und beim Schliessen; optional entprellt bei Aenderung (Absturz). Fenstergroesse beim Resize entprellt.
- Anwenden bei `--restore` (oder `FS_RESTORE=1`). Frage an Nutzer: auch beim normalen Start? Empfehlung: immer schreiben, beim normalen Start nur Fenstergroesse anwenden.
- Wayland erlaubt Clients meist kein Setzen der Fensterposition; ob Blinc/winit es kann, ist **nicht geprueft**. Ebenso ist unklar, ob der Blinc-Bildlauf von aussen setzbar ist. Spike vor Zusage.

### 3.3 Orchestrierung durch den Store
1. Fenster finden (`/proc`: exe unter `packages/<name>` oder `/usr/bin`, nicht `serve`, gleicher Nutzer); schliesst die rpm-Luecke.
2. Stopp mit Speichern: Die Huelle bedient `Control` auch im Fenster auf eigenem Socket `$XDG_RUNTIME_DIR/freesynergy/<name>.window.<pid>.sock`;
   neue Methode `Control.suspend @2 () -> (state :Text)` (`common.capnp` ist DRAFT, ADR 0045; aeltere Programme antworten `unimplemented`, `PROTOCOL` unveraendert).
   Alternative `stop(saveState :Bool)` aendert die Signatur; die neue Methode ist abwaertskompatibel. Windows-faehig (kein Signal noetig).
   Fallback ohne Control: SIGTERM, den die Huelle wie suspend behandelt; sonst alter Weg (`Running`, "bitte schliessen").
3. Warten mit Zeitlimit (`call_limited`, z. B. 10 s, danach auf Prozessende wie `stop_servers`), **nie SIGKILL**; Ueberschreitung = `Running`, Programm nicht ersetzt. `call_limited` erst aus `v0-0-18` in eine Version bringen.
4. Server wie heute (spaeter `Control.stop`), installieren, Server starten.
5. Fenster neu starten: Argumente aus `/proc/<pid>/cmdline` **und Umgebung aus `/proc/<pid>/environ`** (DISPLAY/WAYLAND_DISPLAY/XAUTHORITY/XDG_RUNTIME_DIR) vor dem Beenden merken (wie `start_server` es mit cmdline schon tut),
   plus `--restore`; Programmpfad ueber `program_of` (`current/<name>/...`, nie der geloeschte Pfad: ADR 0065 Punkt 7).
   Flackern: alter und neuer Prozess koennen nicht beide Fenster zeigen; Luecke 1 bis 2 s ist unvermeidbar. Mindern: neues Fenster erst zeigen, wenn der Zustand angewandt ist; gleiche Groesse/Position.
6. Kein Display (Timer-Lauf): laufende Fenster nicht anruehren, Update fuer dieses Programm zurueckstellen und im Fenster/Store als "Update wartet" zeigen. Ohne laufendes Fenster aendert sich nichts.

### 3.4 Store-Selbst-Update
- Unix tar.gz: **kein Hilfsprozess noetig.** Alte Dateien bleiben. Nach dem Commit: Zustand schreiben, `spawn(current/fs-store/fs-store --restore)` (Pfad ueber `own_exe`/Symlink, nie `current_exe` roh), erst nach Lebenszeichen des Neuen (Ready-Datei/Sperre) selbst beenden.
- Unix rpm: `pkexec dnf` ersetzt `/usr/bin/fs-store`; der Prozess haengt am geloeschten Inode; `own_exe` liefert den neuen Pfad, dann `spawn` wie oben. `.deb` (nicht im Code) verhaelt sich genauso.
- Selbst-Update immer **letzter Schritt** der Batch. Job-Zustand (laufende Downloads) nicht wiederherstellen, nur Ansicht/Filter/Auswahl.
- Windows: ausser Reichweite heute (Store ist unix-only). Eine laufende `.exe` ist nicht loesch-/ueberschreibbar, aber umbenennbar; ueblich ein kleiner Hilfsprozess (wartet auf Ende, tauscht, startet). Erst entscheiden, wenn ein Windows-Paketformat beschlossen ist.

## 4. Risiken und Gegenvorschlaege
- **Datenverlust bei ungespeicherter Eingabe:** erst Drafts/laufende Speicherungen abschliessen; hat das Programm Ungespeichertes ohne Draft, fragt das Fenster (Speichern/Verwerfen/Abbrechen); Abbruch = Update dieses Programms zurueckgestellt. Schwierigster Teil. Laufende Transfers (fs-files `uploads.rs`) liegen im Server und ueberleben; Fenster-Transferzustand ungeprueft.
- **Zustand nicht verstanden:** Teil-Verwerfen, nie Absturz; je Release Alt-Fixtures testen.
- **Server-vor-Fenster-Reihenfolge** (1b) beheben durch Fenster zuerst.
- **Mehrere Fenster desselben Programms:** `session.json` je Programm nicht eindeutig; Schluessel `<name>/<window-id>` oder "letzter gewinnt" (offen).
- **`dnf upgrade` ohne Store:** nur Weg A (Fenster beobachtet Inode/mtime von `/proc/self/exe`, bietet "Jetzt neu starten") faengt es ab.
- **Zu aggressives Wiederherstellen:** `--restore` nur nach Update/Neustart, nicht bei jedem Start.
- **Mehr Code in `fs-components-app`** (heute 1644 Zeilen): Crate-Trennung erwaegen.

## 5. Offene Fragen
1. Ansicht auch nach normalem Schliessen/Start wiederherstellen, oder nur nach Update?
2. Ungespeicherte Eingaben: Update zurueckstellen und fragen, oder Entwurf sichern und beim Neustart anbieten?
3. Darf das Update ein Fenster ohne Rueckfrage schliessen, oder erst bestaetigen lassen?
4. Maximalalter der Sitzungsdatei?
5. Windows: Termin und Paketformat?

## 6. Aufwand in Schritten und Repos

| # | Schritt | Repo |
|---|---|---|
| 1 | ADR 0065 praezisieren/neues ADR (Format, Ort, Versionierung, Geheimnisregel, `--restore`, Reihenfolge Fenster/Server); DE+EN-Doku | fs-documentation |
| 2 | Spike: Blinc-Bildlauf und Fensterposition/-groesse von aussen lesen/setzen (Wayland, KDE) am Datei-Manager | fs-components |
| 3 | `Restorable`, `Surface::restorable`, Sitzungsdatei (serde_json, atomar, 0600, `$XDG_STATE_HOME`), Verwerfen/Migration, Tests mit Alt-Fixtures | fs-components (app) |
| 4 | `launch`/`WindowOptions` mit Groesse/Maximiert aus Sitzung; gemeinsames `--restore` (wie `parse_size`) | fs-components (app) |
| 5 | `Restorable` fuer Workbenches (files, tasks, people, calendar, reader, chat), nur Ansicht | fs-components (workbenches) |
| 6 | `Control.suspend` im Schema, Serverteil im Fenster, `call_limited` aus v0-0-18 veroeffentlichen, Windows-Pipe | fs-interfaces |
| 7 | Huelle: Fenster-Control-Socket, SIGTERM = suspend, Erkennung der ersetzten eigenen Datei ("Jetzt neu starten", Weg A), Rueckfrage bei Ungespeichertem | fs-components (app) |
| 8 | Store: `find_windows`, `suspend_windows` mit Zeitlimit, Neustart aus cmdline+environ+`--restore`, neue Reihenfolge, rpm-Luecke (`/usr`), Kein-Display-Regel im Timer | fs-store (engine, cli) |
| 9 | Store-Selbst-Update als letzter Schritt mit Ready-Handshake; Store-Ansicht als `Restorable` | fs-store (app, engine) |
| 10 | Meldungstexte DE/EN ("wird neu gestartet", "laeuft noch", "Update wartet") | fs-store (words) |
| 11 | Jedes Programm hebt fs-components-Tag an, eigene Surfaces ergaenzen, Fixtures | fs-files, fs-people, fs-tasks, fs-wiki, fs-messenger, fs-calendar, ... |
| 12 | Ende-zu-Ende-Test: Fenster + Server, Update, Zustand gleich; Fehlerfaelle (Zeitlimit, kaputte Datei, Formatwechsel) | fs-release / fs-store tests |
| 13 | Windows-Pfad (Hilfsprozess, Pipe, Pfade) | fs-store, fs-interfaces, fs-release (spaeter) |

Kleinster nutzbarer Schnitt: Schritte 1, 2, 3, 4, 7 (nur SIGTERM-Fallback) und 8 ohne Control: Fenstergroesse, Screen und Datei-Manager-Ansicht kehren nach einem Update zurueck. Control-Kanal (6) und Rest folgen.

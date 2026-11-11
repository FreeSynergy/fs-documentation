# 0069 – Ein Update schließt ein laufendes Programm und startet es am selben Punkt neu

Status: akzeptiert (Strategie, 2026-11-11); F1 offen beim Nutzer (Wiederherstellen nach normalem Schließen) · präzisiert und ersetzt ADR 0065 Punkt 7 · baut auf ADR 0046 (Speichern ≠ Export, `DraftStore`), 0045 (Themen-Schnittstellen, `Control`), 0063 (ein Befehl, `serve`), 0066 (vier Frontends)

Befund und Quellen: `.scratch/befund-update-neustart.md` (Stand 2026-11-11).

## Ausgangslage
- Der Store lehnt das Update eines laufenden Fensters heute ab (`UpdateError::Running`). Hintergrund-Server (`fs-<name> serve`) beendet er mit SIGTERM (nie SIGKILL), tauscht und startet sie mit den alten Argumenten neu.
- Die Laufend-Prüfung sieht Programme unter `/usr` (rpm) nicht; ein rpm-Update ersetzt ein laufendes Fenster ohne Prüfung.
- Nichts speichert Ansicht, Größe oder Position. Einzige Wiederherstellung: Entwürfe über `DraftStore` (ADR 0046).
- ADR 0065 Punkt 7 verlangt „erkennen, Zustand sichern, neu starten“, nennt aber weder Format noch Ort noch Trait.

## Entscheidung

### 1. Zwei Wege, eine Funktion
- **Weg A (zuerst):** Das Fenster bemerkt, dass seine eigene Datei ersetzt wurde (Inode/mtime von `/proc/self/exe`), speichert den Zustand und startet sich selbst neu. Deckt auch `dnf upgrade` ohne Store ab.
- **Weg B (danach):** Der Store löst aus (findet das Fenster, bittet es zu beenden, installiert, startet neu). Garantiert „Update schließt und startet neu“.
- **Keine doppelten Neustarts:** Unter Weg B besitzt der **Store** den Neustart; die Hülle speichert bei SIGTERM, beendet sich und startet sich **nicht** selbst neu. Weg A greift nur, wenn das Fenster von selbst bemerkt, dass seine Datei ersetzt wurde, **und kein SIGTERM kam**. SIGTERM kann auch von Abmelden/Herunterfahren kommen: dann nur speichern, **ohne Rückfrage**, die das Herunterfahren aufhält (Draft-Weg oder Verwerfen statt Dialog).
- **Nicht mitten im Update neu starten (Weg A):** Bei tar.gz zeigt `/proc/self/exe` auf den Versionsordner und ändert sich nicht; beobachtet wird deshalb das **Ziel des Symlinks `current/<name>`** (Austausch atomar). Bei rpm/deb erst neu starten, wenn die Paket-Transaktion fertig ist (Datei stabil bzw. Sperre von dnf/apt frei); sonst startet das Fenster halb aktualisiert.
- Beide benutzen **eine** Funktion `suspend_and_exit()` in der Fensterhülle (`fs-components`, App-Teil). Sie sammelt den Zustand, schreibt die Sitzungsdatei, sichert Entwürfe und beendet das Fenster sauber. Weg B ist nur ein weiterer Auslöser.
- Ersetzt/präzisiert ADR 0065 Punkt 7: Dort bleibt die Pflicht („nie den Pfad der gelöschten Datei benutzen“; Neustart über `current/<name>/…`, im Store über `program_of`/`own_exe`); Format, Ort, Trait und Ablauf stehen ab jetzt hier. „Oder bietet ‚Jetzt neu starten‘ an“ gilt nur noch als Rückfall, wenn kein Zustand gesichert werden kann.

### 2. Kleinster Schnitt zuerst
Gebaut wird zuerst: Sitzungsdatei und Trait (Schritte 3, 4 des Befunds), Fensterhülle mit SIGTERM = suspend und Weg A (7), Store: Fenster finden, beenden, neu starten, neue Reihenfolge, rpm-Lücke, Kein-Display-Regel (8, ohne `Control`). Davor ein Spike (2, siehe Offene Punkte) und diese Entscheidung (1).
- Ergebnis: Fenstergröße, Screen und Ansicht des Datei-Managers kehren nach einem Update zurück.
- **Später:** `Control.suspend` (Schritt 6) als **eigene `fs-interfaces`-Version, nicht v0.0.19**; ältere Programme antworten `unimplemented`. Bis dahin ist **SIGTERM der einzige Weg** zum Fenster. Danach Workbenches, übrige Programme, Store-Selbst-Update, Ende-zu-Ende-Test, Windows.

### 3. Entscheidungen (Strategie)
| Frage | Entscheidung |
|---|---|
| Ungespeichertes | Wird als **Entwurf über `DraftStore`** gesichert (ADR 0046) und beim Neustart zur Wiederherstellung **angeboten** (nie von selbst zurückgeschrieben). Das Update wird **nicht** zurückgestellt. Gibt es für das Ungespeicherte keinen Draft-Weg, **fragt das Fenster**: Speichern / Verwerfen / Abbrechen (Abbrechen = Update für dieses Programm zurückgestellt). |
| Rückfrage vor dem Schließen | Keine. Das Fenster zeigt kurz „wird aktualisiert, gleich wieder da“. |
| Maximalalter der Sitzungsdatei | 30 Tage; ältere werden verworfen. |
| Windows | Später, nicht jetzt. |
| Mehrere Fenster | Schlüssel `<name>/<window-id>`; **jedes** Fenster kommt zurück. |
| Wiederherstellen nach normalem Schließen | **Offene Frage an den Nutzer.** Bis zur Antwort: Zustand wird **immer geschrieben**; beim normalen Start (ohne `--restore`) werden **nur Größe und Screen** angewandt. |

### 4. Regeln
1. **Positivliste:** gesichert wird nur, was ein Component ausdrücklich als `Restorable` meldet. **Passwort- und Geheimnisfelder bekommen nie `Restorable`** (Regel in die Review-Liste). Freitext standardmäßig nicht. Auswahl nur per stabiler ID/Pfad, nie per Index; fehlt sie, still verwerfen.
2. **Zustand ist kein Export und keine Sicherung** (ADR 0046): nicht in Exporte und Backups, Menüpunkt „Sitzung vergessen“.
3. **Wiederherstellen blockiert den Start nie.** Fehler, kaputte Datei, unbekannte Version: Standardzustand, nur der betroffene Teil wird verworfen, Vermerk im Log.
4. **Kein SIGKILL**, nirgends. Wartet das Fenster nicht rechtzeitig ab (Zeitlimit, z. B. 10 s), bleibt das Programm unersetzt (`Running`, „bitte schließen“).
5. **Datei:** JSON (serde), `$XDG_STATE_HOME/freesynergy/<name>/session.json` (Standard `~/.local/state/…`); Zustand ist weder Daten noch Konfiguration. Schreiben atomar: temp im selben Ordner, `fsync`, `rename`, Rechte 0600 (neue Funktion; `write_new_private_file` überschreibt nie).
   ```json
   {"schema":1,"program":"fs-files","program_version":"0.0.7","saved_at":"…",
    "windows":{"fs-files/main":{"window":{"w":1200,"h":800,"x":null,"y":null,"maximized":false},
      "screen":"files","parts":{"files.list":{"v":2,"data":{}}}}}}
   ```
6. **Versionierung:** `schema` (Hülle) und `v` je Teil. Unbekanntes oder zu altes `v` ohne Migration: nur dieser Teil verworfen. Unbekanntes `schema` oder kaputtes JSON: ganze Datei verwerfen, normal starten. Programmversion nur zur Diagnose. Je Release Tests mit Alt-Fixtures.
7. **Trait (Namen vorläufig), in `fs-components-app`:**
   ```rust
   pub trait Restorable {
       fn state_key(&self) -> &str;           // stabil, z. B. "files.list"
       fn state_version(&self) -> u32;
       fn save_state(&self) -> Option<serde_json::Value>;
       fn restore_state(&self, version: u32, value: &serde_json::Value) -> Result<(), RestoreError>;
       fn migrate(&self, _from: u32, _v: serde_json::Value) -> Option<serde_json::Value> { None }
   }
   // Surface: fn restorable(&self) -> Option<&dyn Restorable> { None }
   ```
   Nur Ansicht: Auswahl, Bildlauf (Offset + Anker-ID), Sortierung, Filter, Ausklappzustand. Workbenches liefern ihren Teil ohne Programmcode. Ein eigenes Crate (`fs-components-session`) ist zu erwägen, damit Server/CLI ohne Blinc es nutzen können.
8. **Start:** `--restore` (Argument, gemeinsam wie `parse_size`) oder `FS_RESTORE=1`. Gilt nur nach Update/Neustart, nicht bei jedem Start.
9. **Neustart-Daten:** Argumente aus `/proc/<pid>/cmdline` werden **vor dem Beenden** gemerkt. Aus `/proc/<pid>/environ` wird **nur eine Positivliste** übernommen: `DISPLAY`, `WAYLAND_DISPLAY`, `XAUTHORITY`, `XDG_RUNTIME_DIR`, `LANG`/`LC_*`; die ganze Umgebung nie (Token möglich). Nichts davon kommt auf die Platte, nur in den Speicher des Stores. Start über `current/<name>/…`, nie über den gelöschten Pfad.
10. **Neues Fenster erst zeigen, wenn der Zustand angewandt ist**, gleiche Größe/Position; eine Lücke von 1 bis 2 s bleibt.

11. **Was gespeichert wird (Spike, `.scratch/spike-restore.md`):** Größe (nur wenn nicht maximiert), maximiert, Screen (die Ansicht der Hülle, `Shell::current().id`), Ordner, Ansicht (Liste/Raster), Sortierung (Feldname + Richtung, nie Spaltenindex), Auswahl **per Schlüssel**, Bildlauf als `{Anker-Schlüssel, Pixel}` (Schlüssel der obersten sichtbaren Zeile; Pixel nur als Rückfall). **Weggelassen:** Fensterposition, Ausgabe (Monitor), Formulare, Fragen, Ergebnisse, Übertragungen, Vorschau, Geheimnisse, Zwischenablage, Bildlauf von Listen ohne stabilen Schlüssel.
12. **Wiederherstellungs-Reihenfolge (zwingend, gemessen):** Ordner → Ansicht → Sortierung → Auswahl (nachladen, bis der Schlüssel da ist) → Bildlauf **erst nach dem ersten Aufbau** (im Build-Closure, `rebuild_count`, nie per Zeitgeber). Grund: Ordnerwechsel, Sortierung und Suche löschen die Auswahl und erzeugen eine neue Liste, die beim nächsten Aufbau auf Zeile 0 springt; gemessen Zeile 40 → 0, nach dem ersten Aufbau gesetzt → 1440. Auswahl nie zweimal auf denselben Schlüssel setzen (öffnet einen Ordner). Liegt die Zeile außerhalb der geladenen Seiten, erst nachladen (sonst Klemmung auf das Ende der geladenen Zeilen); im Kachelraster braucht der Bildlauf einen Pixel-Setzer (`ListPosition::set_offset`).

### 4a. Plattformgrenzen (Wayland, gemessen mit KWin 6.8.2, winit 0.30, Blinc `fs-blinc-3`)
- **Position** wird unter Wayland weder gesetzt noch gelesen (`xdg_toplevel` kennt keine Position, winit-Wayland ignoriert `with_position`/`set_outer_position`); das gilt für alle Kompositoren. Deshalb wird sie **nicht gespeichert**; der Kompositor platziert das Fenster. **Kein KDE-Skript-Trick** (KWin-Skript per D-Bus, KWin-Fensterregeln): nur KDE, Aufblitzen, greift in Nutzereinstellungen ein.
- **Screen/Ausgabe** nur über Vollbild (der Kompositor wählt) und erst nach Blinc-Patch B (`WindowConfig.monitor`). Wo in dieser ADR „Screen“ als Fenstereigenschaft steht, ist bis dahin die **Ansicht der Hülle** gemeint, nicht der Monitor.
- **„Maximiert lesen“** und **„Ausgabe beim Start“** brauchen Blinc-Patches: **A** (`ctx.window_state()`: Größe, maximiert, Vollbild, optional Position/Monitor, plus Änderungs-Callback für entprelltes Speichern) und **B**. Bis A fehlt, wird **keine Größe gespeichert, die von einem maximierten Fenster stammen könnte** (sonst würde die Bildschirmgröße als „normale“ Größe abgelegt); Größe/maximiert werden vor dem Start über `WindowOptions`/`WindowConfig` gesetzt.
- **Standardweg für Position später: `xdg-session-management`** (Blinc-Patch **C**), sobald winit es kann (KWin 6.8.2 meldet v1, winit 0.30 spricht es nicht). Dann merkt der Kompositor Position, Größe, Ausgabe und maximiert je Fenster selbst; die Sitzungsdatei hält nur das Token.
- **Blinc A und D** (D: `app_id` unter Wayland setzen, für Fensterregeln und Desktop-Zuordnung) kommen im Fork, **mit `fs-blinc-4`**. Das in Blinc vorhandene `window_state` (`~/.config/<app>/window_state.json`) wird **nicht** benutzt (falscher Ort, ignoriert maximiert, nirgends aufgerufen).

### 5. Ablauf im Store (Weg B)
1. Fenster finden (`/proc`: exe unter `packages/<name>` **oder** `/usr/bin`, nicht `serve`, gleicher Nutzer). Das schließt die rpm-Lücke.
2. Beenden mit SIGTERM (Fensterhülle behandelt es wie suspend), Zeitlimit, dann auf Prozessende warten.
3. **Reihenfolge:** Fenster zuerst beenden, dann Server (heute umgekehrt bzw. ignoriert: das Fenster stünde ohne Server da). Nach der Installation: **Server zuerst, dann Fenster** (mit `--restore`). Die Server-Schiene (`serve`, SIGTERM, 15 s, gleiche Argumente) bleibt unverändert.
4. **Kein Display** (Timer-Lauf `fs-store update --all`): Fenster nicht anrühren, Update für dieses Programm **zurückstellen** und als „Update wartet“ zeigen. Ohne laufendes Fenster ändert sich nichts.
5. **Store-Selbst-Update (Unix):** immer **letzter Schritt** der Batch. Zustand schreiben, neuen Prozess über `own_exe`/Symlink starten (nie rohes `current_exe`), erst nach Lebenszeichen des Neuen (Ready-Handshake: Ready-Datei/Sperre) selbst beenden. Gilt für tar.gz und rpm. Job-Zustand (Downloads) wird nicht wiederhergestellt. **Windows: offen** (Hilfsprozess nötig, erst nach Paketformat-Entscheidung).

## Verhältnis zu anderen ADRs
- **0065:** Punkt 7 wird hiermit präzisiert (siehe 1.); die Hülle bekommt `suspend_and_exit()` und `Surface::restorable`.
- **0046:** Entwürfe bleiben im `DraftStore`, nicht in der Sitzungsdatei (kein zweites System für dasselbe Feld).
- **0045:** `Control.suspend` ist eine Erweiterung des Entwurfs-Schemas, abwärtskompatibel; kommt später (nicht v0.0.19).

## Tests
Der Ende-zu-Ende-Test (Schritt 12) enthält mindestens diese Fälle, jeder **ohne den Fix rot**, wo möglich: (a) Fenster mit Ungespeichertem (Entwurf gesichert und angeboten bzw. Rückfrage); (b) Fenster hängt (Zeitlimit, dann `Running`, nichts ersetzt); (c) kaputte `session.json` (Start im Standardzustand); (d) Timer-Lauf ohne Display (Fenster unberührt, „Update wartet“); (e) **Reihenfolge der Wiederherstellung:** in falscher Reihenfolge (Bildlauf/Auswahl vor Ordner/Sortierung bzw. vor dem ersten Aufbau) schlägt das Wiederherstellen fehl (Auswahl weg, Bildlauf bei 0), in der richtigen (Regel 12) gelingt es; (f) Größe aus einem maximierten Fenster wird nicht als normale Größe gespeichert; (g) verschwundener Auswahl-/Anker-Schlüssel: still verworfen.

## Risiken und offene Punkte
- **Spike (Schritt 2) erledigt:** Bildlauf, Auswahl, Ansicht, Größe sind lösbar (Regeln 11, 12); Position und Ausgabe unter Wayland nicht (4a), Blinc-Patches A, B, D im Fork (`fs-blinc-4`), C später.
- **Offene Frage an den Nutzer:** Ansicht auch nach normalem Schließen wiederherstellen (siehe Tabelle)?
- Ungespeichertes ohne Draft-Weg ist der schwierigste Teil (Rückfrage im Fenster). Fenster-Transferzustand (z. B. fs-files `uploads.rs`) ungeprüft; Server-Transfers überleben.
- `dnf upgrade` ohne Store: nur Weg A fängt es ab.
- Mehr Code in `fs-components-app`: Crate-Trennung prüfen.
- Windows (Pfad `%LOCALAPPDATA%\FreeSynergy\<name>\state\`, Pipe statt Signal, Hilfsprozess): später.

## Folgen
- `fs-components` (app, workbenches): Trait, Sitzungsdatei, `suspend_and_exit()`, `--restore`; danach alle Programme heben ihren fs-components-Tag an.
- `fs-store`: `find_windows`, Neustart, Reihenfolge, `/usr`, Kein-Display-Regel, Meldungstexte DE/EN („wird aktualisiert, gleich wieder da“, „Update wartet“), Selbst-Update.
- `fs-interfaces`: `Control.suspend` und `call_limited` in einer eigenen späteren Version.
- Doku: `fs-components/DESIGN.md` und Store-`DESIGN.md` (Punkt „Offen“) nachziehen.

## English summary
**Decision:** An update closes a running program and restarts it at the same point. Two paths share one shell function `suspend_and_exit()` in `fs-components`: path A (the window notices its own file was replaced, saves state, re-executes itself) first, path B (the Store triggers it) second. Smallest cut first: session file and `Restorable` trait, shell with SIGTERM = suspend, Store window handling without `Control`; `Control.suspend` follows in its own later `fs-interfaces` version (not v0.0.19).

**Rules:** unsaved input is saved as a draft through `DraftStore` (ADR 0046) and offered on restart, the update is not deferred; if there is no draft path the window asks (save / discard / cancel). Under path B the Store owns the restart (the shell saves on SIGTERM, exits, does not re-exec); path A only fires when the window notices the replaced file itself and no SIGTERM came; SIGTERM may mean logout/shutdown, so then save only, no blocking prompt. Path A watches the target of the `current/<name>` symlink (tar.gz) and waits for the package transaction to finish (rpm/deb). Only an allow-list of the environment is taken from `/proc/<pid>/environ` (DISPLAY, WAYLAND_DISPLAY, XAUTHORITY, XDG_RUNTIME_DIR, LANG/LC_*), kept in memory only. The end-to-end test covers: unsaved work, hanging window (timeout, `Running`), broken session.json, timer run without display. Saved: size (only if not maximised), maximised, shell screen, folder, view, sort (field name, never column index), selection by key, scroll as {anchor key, pixels}; omitted: position, output/monitor, forms, questions, transfers, preview. Restore order is mandatory (measured): folder, view, sort, selection, scroll only after the first build; otherwise a rebuilt list resets selection and scroll (measured row 40 to 0, correct order 1440); a test must fail in the wrong order and pass in the right one. Wayland limits: position is neither settable nor readable (winit/Wayland), no KDE script trick; output only via fullscreen/compositor; reading "maximised" and choosing the output at start need Blinc patches A and B, `xdg-session-management` (Blinc C) later once winit supports it (KWin 6.8.2 has v1, winit 0.30 does not) as the standard way for position; Blinc A and D (app_id) land in the fork with `fs-blinc-4`. Close without confirmation, with a short "updating, back in a moment" notice. Session file max age 30 days. Multiple windows keyed `<name>/<window-id>`, all come back. Windows later. Open question to the user: restore also after a normal close (until answered: always write, apply only size and screen on a normal start).
Only fields explicitly `Restorable` are saved (positive list; never password fields); state is neither export nor backup; restoring never blocks startup (error means default state, part discarded); never SIGKILL. File: JSON (serde) at `$XDG_STATE_HOME/freesynergy/<name>/session.json`, atomic write, mode 0600, `schema` plus per-part `v` with migrate/discard. Start with `--restore`. Restart arguments and environment are read from `/proc/<pid>/cmdline` and `environ` before exit. Order: window first, then server; after install server first, then window. No display (timer run): do not touch windows, defer that program's update and show "update waiting". Store self-update on Unix is the last step (spawn via `own_exe`, ready handshake, then exit); Windows open; the rpm gap (`/usr`) is closed by also scanning `/usr/bin`. Supersedes/specifies ADR 0065 point 7.

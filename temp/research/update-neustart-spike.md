# Spike: Fenster- und Ansichtszustand von aussen lesen und setzen (Schritt 2 des Befunds)

Stand 2026-11-11. Blinc `fs-blinc-3` (winit 0.30.13, wgpu 26), fs-components `v0.0.8` (origin/main), KWin 6.8.2 (`kwin_wayland --virtual` auf privatem D-Bus, `XDG_CONFIG_HOME` privat).
Blinc wurde nicht geaendert. Spike-Branch: `spike-restore` in fs-components (gepusht, kein Merge, kein Tag), Worktree `/srv/FreeSynergy/.wt-spike-restore`.
Testrahmen (nicht im Repo): `/srv/FreeSynergy/.scratch/spike-probe/` (`run.sh`, `case.sh`, `go.sh`, `dump.js`, `move.js`, Ausgaben in `out/`).
Probe-Programm: `crates/fs-components-workbenches/examples/spike_restore.rs` (Dateimanager ueber In-Memory-Quelle, Fenster per Umgebungsvariablen, `SPIKE_RESTORE=folder=..,view=..,sort=..,desc=1,select=..,row=..`).
Test ohne Fenster: `crates/fs-admin-frontend/tests/spike_restore.rs` (gruen).

## Kurzergebnis

| Faehigkeit | ohne Blinc-Aenderung? | Wie (API) | Wayland / KDE |
|---|---|---|---|
| Groesse setzen | ja | `WindowConfig.width/height` (Blinc `blinc_platform/src/window.rs:103-105`, angewandt `extensions/blinc_platform_desktop/src/window.rs:29`); fs-components `WindowOptions` (`fs-components-app/src/window.rs:16-33`) kennt sie schon | geht; KWin zentriert das neue Fenster (800x500 -> Rahmen 240,136) |
| Groesse lesen | ja (nur Inhaltsgroesse) | `WindowedContext.width/height` im Build-Closure von `launch` (`window.rs:46-49`); jeder Resize ruft den Closure neu (Test: `BUILD 900 572` nach Aenderung von aussen) | logische Pixel ohne Titelleiste (Inhalt 1000x700, KWin-Rahmen 1000x728); kein Callback, nur beim Neuaufbau |
| Maximiert setzen | ja | `WindowConfig.maximized` (`window.rs:33`) | geht (KWin: 0,0 1280x800, Inhalt 1280x772) |
| Maximiert lesen | **nein** | Das winit-Fenster ist fuer das Programm nicht erreichbar (`WindowedContext` hat nur `close/drag/minimize/maximize`-Callbacks, `windowed/app_init.rs:60-121`; `window_actions::maximize_window` schaltet nur um) | winit-Wayland kann es (`is_maximized`, `wayland/window/mod.rs:447`), Blinc reicht es nicht durch. Heuristik "Groesse = Bildschirm" unmoeglich: Bildschirmgroesse unbekannt |
| Vollbild setzen | teilweise | `WindowConfig.fullscreen` -> immer `Borderless(None)` (`window.rs:38-40`); geht (fullScreen=true) | Bildschirm waehlt der Kompositor (Test mit 2 Ausgaben: blieb auf Virtual-0); `Borderless(Some(monitor))` kann winit/Wayland, Blinc bietet es nicht an |
| Screen (Ausgabe) waehlen | nein | kein `monitor`-Feld in `WindowConfig`, `available_monitors()` nirgends genutzt (`grep`: nur `current_monitor().refresh_rate` in `windowed/event_loop/lifecycle.rs:117`) | nur Vollbild waehlbar (winit); normales Fenster: Wayland erlaubt dem Client keine Ausgabenwahl. KDE-Ausweg unten |
| Position setzen | **nein unter Wayland** | `WindowConfig.position` -> `with_position` (`window.rs:47-49`), `center` -> `set_outer_position` (`window.rs:57-65`) | winit-Wayland: `set_outer_position` ist leer ("Not possible on Wayland", `wayland/window/mod.rs:273`), `with_position` wird nicht ausgewertet. Test: `SPIKE_POS=300,200` und `1500,100` (2 Ausgaben) -> Fenster unveraendert bei 140,36; `SPIKE_CENTER` ebenso wirkungslos. Unter XWayland (`--xwayland`, DISPLAY gesetzt) kam 300,200 -> 280,72 an: KWin setzt Platzierung selbst, nicht verlaesslich |
| Position lesen | **nein** | nicht erreichbar (kein winit-Fenster); selbst mit Zugriff gaebe es unter Wayland `Err(NotSupported)` (`wayland/window/mod.rs:263`) | auch mit Blinc-Patch unmoeglich unter Wayland |
| Bildlauf lesen | ja | `ListPosition::offset()` in Pixel (`fs-components-widgets/src/list_view/position.rs:88`); darunter `ScrollRef::offset()/scroll_y()` (Blinc `scroll_ref.rs:326,331`) und `ScrollPhysics.offset_y`. Test: Klick + 3x PageDown -> `offset=528` -> `996`, Cursor und Auswahl folgen | `ListPosition` ist im `FileManagerWidget` privat (`file_manager/widget.rs:39`) und im `AdminSurface` `pub(super)` (`view/surface.rs:43`): Zugriff braucht eine kleine fs-components-Methode (im Spike: `FileManagerWidget::position()`) |
| Bildlauf setzen | ja, mit Haken | `ListPosition::scroll_to_row(row)` (Zeile 75; Liste), Pixel-Setzer `apply_offset` ist `pub(crate)` (Zeile 181), `ScrollRef::set_scroll_offset(x,y)` (Blinc `scroll_ref.rs:304`). Test: `row=120` -> `offset=4320` (=120 x 36) | siehe Haken unten |
| Auswahl lesen/setzen | ja | Dateimanager: `FilesState::selected_key()` / `select(key)` (`select.rs:36,72`), `FileManagerWidget::context()`/`with_state`. Admin-Frontend (das nutzt fs-files): `Session::list().selected()` / `list_mut().select(id)` / `open_detail(id)` | nur ueber stabile Schluessel/IDs; `select` findet nur geladene Zeilen (Seiten zu 200, `PAGE`) |
| Ansicht lesen/setzen | ja | Dateimanager: `view()`/`set_view(List/Grid)` (`reading.rs:33,38`), `sort()` = `SortOrder{key,descending}` (`reading.rs:86`), `set_sort(key)`, `toggle_direction()`, `open_folder(key)`, `term()`/`search`, `filter()`. Admin-Frontend: `list().sort()` = `(Spaltenindex, Direction)`, `cycle_sort(col)` (1x aufsteigend, 2x absteigend), `set_filter`, `Screen` | Reihenfolge zwingend (unten); Admin: Sortierspalte per Feldname speichern, nicht per Index |

## Befunde im Einzelnen

### Fenster (a, b)
- Alles, was Blinc anbietet, geht nur **vor** dem Start ueber `WindowConfig`. `launch` reicht heute nur Breite/Hoehe durch (`window.rs:38-44`); `maximized`, `fullscreen`, `position` liessen sich in `WindowOptions` ergaenzen (fs-components, keine Blinc-Aenderung).
- Nach dem Start ist das winit-Fenster fuer das Programm unerreichbar. Lesen: nur Inhaltsgroesse ueber `ctx.width/height`. **Maximiert- und Vollbildzustand sind nicht lesbar**: Ein "Groesse speichern" kann ein maximiertes Fenster nicht von einem normalen unterscheiden und wuerde die Bildschirmgroesse als "normale" Groesse ablegen.
- Blinc hat `blinc_app::window_state` (`SavedWindowState`, `WindowStateStore`: x, y, Breite, Hoehe, maximiert). Das Modul wird nirgends aufgerufen (kein Treffer ausser der Definition), `apply_to` ignoriert `maximized`, der Ort ist `~/.config/<app>/window_state.json` (passt nicht zur Regel `$XDG_STATE_HOME`). Nicht verwenden.
- **Wayland-Position**: Weder das Protokoll (`xdg_toplevel` hat keine Position) noch winit erlauben es. Das gilt fuer alle Kompositoren. Gemessen: `with_position` und `center` ohne Wirkung.
- **app_id**: Blinc setzt unter Wayland keinen Namen (`apply_platform_attrs` nutzt nur X11-`with_name`, `window.rs:277-282`; `WindowAttributesExtWayland::with_name` fehlt). KWin zeigte trotzdem `class=[spike_restore]` (Programmname). Fuer Fensterregeln/Desktop-Dateizuordnung ist das fragil; Patch unten.
- **KDE-spezifische Wege (gemessen, beide gehen)**:
  1. *KWin-Fensterregel* (`kwinrulesrc`, Abgleich nach `wmclass`, `position=`, `positionrule=2`, `screen=1`, `screenrule=2`): Fenster erschien bei 1900,200 auf Virtual-1 (2 Ausgaben). Das ist eine Nutzereinstellung, kein Programmcode; ein Programm koennte die Regel selbst schreiben, das greift aber in die Konfiguration des Nutzers ein: nicht empfohlen.
  2. *KWin-Skript ueber D-Bus* (`org.kde.KWin /Scripting loadScript` + `run`): setzte nach dem Start `frameGeometry` (Position, Groesse **und** Ausgabe: 1500,100 900x600, Virtual-1); das Fenster bekam danach einen Neuaufbau mit 900x572. Dasselbe Skript kann Position/Ausgabe/Maximiert **lesen** (`dump.js`, `callDBus` zurueck). Braucht D-Bus-Client im Programm, nur KDE, kurzes Aufblitzen an der alten Stelle. Als Ausloeser nicht tragfaehig, hoechstens als optionale KDE-Zugabe.
- **Wayland-Standardweg ist da, wird aber nicht genutzt**: KWin 6.8.2 meldet `xdg_session_manager_v1` v1 (`wayland-info` im verschachtelten KWin). Das Protokoll (`xdg-session-management`, staging, im Crate `wayland-protocols 0.32.13` enthalten) laesst den Kompositor Position, Groesse, Ausgabe und Maximiert je Toplevel merken (`add_toplevel`/`restore_toplevel`, Sitzungs-Token als Text). winit 0.30 spricht es nicht und gibt das `xdg_toplevel` nicht heraus. Andere Kompositoren: nicht geprueft.

### Bildlauf (c)
- Blinc `ScrollRef` kann alles (`offset`, `set_scroll_offset`, `scroll_to`, `watch_y`, `max_scroll`, `content_size`). fs-components kapselt es in `ListPosition` (`Dateimanager`-Liste, Kachelraster, Admin-Liste, `agent_tree`, Zeitleiste hat eigenes Handle `fs-components-timeline/src/handle.rs`).
- **Haken 1, Reihenfolge**: Jede neue Liste (Ordner oeffnen, Sortierung, Suche -> `new_list()`/`list_generation`) setzt beim naechsten Aufbau `scroll_to_row(0)` (`view/work.rs:180-181`) und ueberschreibt eine vorher gesetzte Zeile. Gemessen: `folder=d3,row_early=40` -> `offset=0`; spaeter gesetzt (nach dem ersten Aufbau) -> `1440`. Sauber ohne Zeitgeber: im Build-Closure nach dem ersten `build` (`ctx.rebuild_count == 0`) `scroll_to_row` setzen und `refresh()` (gemessen: `BUILD ... rebuild_count=0`, dann `=1`, `offset=1440`).
- **Haken 2, Kachelraster**: `scroll_to_row` wirkt im Raster nicht (`file_tile/grid.rs:147-153` kennt nur Pixel, `at_top`); gemessen `view=grid,row_hook=40` -> `offset=0`. Es braucht einen oeffentlichen Pixel-Setzer (`ListPosition::set_offset`, ein Einzeiler auf `apply_offset`).
- **Haken 3, Klemmung**: `settle` klemmt auf `total - view` (`list_view/view.rs:75-83`). Liegt die Zeile ausserhalb der geladenen Seiten (200 je Seite, `load_more`), wird auf das Ende der geladenen Zeilen geklemmt. Erst Zeilen nachladen (wie beim Auswahl-Test `select=f00450`: 600 Zeilen geladen), dann scrollen.
- **Haken 4, Inhalt aendert sich**: Zeilen-/Pixelindex ist nach einem Update unzuverlaessig. Besser: Schluessel der obersten sichtbaren Zeile (`rows[offset / ROW_HEIGHT].key`) speichern und beim Wiederherstellen dessen Index suchen; Pixelwert nur als Rueckfall.
- Mausrad nicht eingespeist (das `inject`-Werkzeug hat kein Rad); Tastatur (PageDown) lief. Die Liste liest dasselbe `ScrollPhysics`, das Blincs Scroll-Widget beschreibt (`position.rs:164`, `Scroll::with_physics(Arc::clone(&position.physics))` in `list_view/view.rs:63`), daher gleicher Wert.

### Auswahl und Ansicht (d)
- Die Zustandsautomaten sind fenster- und Blinc-frei: `FilesState` (Dateimanager-Workbench) und `Session`/`ListModel` (Admin-Frontend, das fs-files heute nutzt: `fs-files/crates/*/src/window.rs`, `AdminSurface` je Datentyp). Beides ist ueber oeffentliche Methoden les- und setzbar. Beleg: `fs-admin-frontend/tests/spike_restore.rs` (Sortierung nach Feldname absteigend, Filter, Auswahl, Detailbildschirm: aus Session A gelesen, in frischer Session B wiederhergestellt, gleich; verschwundene ID: still verworfen, Liste bleibt) und das Probe-Programm (`r3`: `select=f00450,sort=size,desc=1,row=300` -> `selected=Some("f00450") sort=Size/true`, `offset=10800`; `r8`: Ordner + Zeile + Auswahl).
- **Reihenfolge beim Wiederherstellen** (Dateimanager): Ordner -> Ansicht -> Sortierung -> Auswahl (nachladen, bis der Schluessel da ist) -> Bildlauf. Grund: `open_folder`, `set_sort`, `search` loeschen die Auswahl (`navigate.rs` `leave_for`: `selected = None`) und erzeugen eine neue Liste (Bildlauf oben). `select` auf den schon gewaehlten Schluessel oeffnet einen Ordner (`select.rs:37-46`): nie zweimal rufen.
- Admin: `cycle_sort` kennt kein "setze auf"; 1 bzw. 2 Aufrufe tun es (im Test genutzt). Ein `set_sort(Option<(usize, Direction)>)` waere sauberer (fs-components).
- `Shell`: `current().id` lesbar, `select(id)` setzbar (`shell.rs:71,76`).
- Nicht wiederherstellen: offene Formulare/Fragen (`Ask`, `Screen::Command/Confirm/Result`; Entwuerfe laufen ueber `DraftStore`), Uebertragungen, Notizen, Vorschau-Inhalt, Suchfeld-Text nur wenn gewollt (Suche ist "in allen Ordnern": eigene Entscheidung).

## Empfehlung fuer `Restorable` / Sitzungsdatei

Speichern (Positivliste, nur Schluessel/IDs, nie Indizes):
- Fenster: `w`, `h` (nur wenn nicht maximiert, siehe Patch A; bis dahin nur beim Start angewandt, ohne Maximiert-Wissen wuerde sonst die Bildschirmgroesse gespeichert), `maximized` (nur nach Patch A lesbar; setzen geht heute), optional `fullscreen`.
- Aktueller Screen der Huelle (`Shell::current().id`).
- Dateimanager-Teil: `folder`, `in_trash`, `view`, `sort.key/descending`, `selected` (Schluessel), `scroll` als `{anchor_key, offset_px}`; Filter (`ListFilter`) optional.
- Admin-Teil: `screen` (List oder Detail(id)), Sortierspalte (Feldname) + Richtung, Filtertext, `selected`, `scroll` wie oben.
- Auswahl und Anker nur als Schluessel; fehlt er beim Wiederherstellen: verwerfen.

Weglassen:
- **Position** (Wayland nicht setz- und nicht lesbar; auf X11/Windows/macOS lesbar nur nach Patch A, dann optional und nur dort anwenden, auf Wayland nie). Besser: gar nicht speichern; Wayland-Fenster platziert der Kompositor.
- **Ausgabe/Screen** (Wayland nicht waehlbar ausser Vollbild; Blinc kann es nicht): nicht speichern, bis Patch B/C vorliegt.
- Formulare, Fragen, Ergebnisse, Uebertragungen, Vorschau, Geheimnisse, Zwischenablage; Bildlaufposition von Listen ohne stabilen Schluessel.

Anwendung: Fenstergroesse/Maximiert in `WindowOptions`/`WindowConfig` vor `launch`; Ansicht in der Reihenfolge oben **vor** dem ersten Aufbau; Bildlauf **nach** dem ersten Aufbau im Build-Closure (`rebuild_count`), nie per Zeitgeber.

## Kleinste noetige Patches

In fs-components (kein Blinc):
1. `WindowOptions` um `maximized`, `fullscreen` (und `position` fuer Nicht-Wayland) erweitern und in `WindowConfig` durchreichen.
2. `ListPosition`: oeffentlich `set_offset(px)`; Zugriff auf die Position im `FileManagerWidget` und `AdminSurface` (`position()`).
3. Build-Closure von `launch` merkt die letzte Inhaltsgroesse (Atomics) fuer das Speichern beim Beenden/Suspend.
4. `ListModel::set_sort(Option<(usize, Direction)>)`.

Blinc (nur Beschreibung, Upstream/Fork `FreeSynergy/Blinc`):
- **A. Fensterzustand lesen**: in `WindowedContext` ein Handle, z. B. `ctx.window_state() -> WindowState { inner_size, maximized, fullscreen, outer_position: Option<(i32,i32)>, monitor: Option<String> }`, gespeist aus dem `Arc<winit::Window>` (`DesktopWindow::winit_window_arc`, `extensions/blinc_platform_desktop/src/window.rs:88`; `is_maximized`, `is_fullscreen`, `outer_position().ok()`, `current_monitor().name()`), plus ein Aenderungs-Callback (Resize/Maximize) fuer entprelltes Speichern. Rund 40 Zeilen; ohne das ist "maximiert" nicht lesbar.
- **B. Ausgabe beim Start**: `WindowConfig.monitor: Option<String>`; in `DesktopWindow::new` ueber `event_loop.available_monitors()` finden und bei `fullscreen` `Borderless(Some(m))` nehmen (Wayland: `xdg_toplevel.set_fullscreen(output)`).
- **C. Wayland-Sitzung** (optional, grosser): `xdg-session-management` (Position/Groesse/Ausgabe/Maximiert vom Kompositor) braucht das `xdg_toplevel`; winit 0.30 gibt es nicht heraus, also winit-Patch/Fork oder eigener Wayland-Client auf der rohen `wl_display`. Aufwand deutlich groesser, Nutzen nur auf Kompositoren mit dem Protokoll (KWin 6.8.2 ja).
- **D. app_id unter Wayland**: `WindowConfig` ein Name-Feld, in `apply_platform_attrs` `WindowAttributesExtWayland::with_name(general, instance)` (wenige Zeilen). Gewuenscht fuer Fensterregeln und Desktop-Zuordnung, nicht fuer das Wiederherstellen selbst.

## Vorfall

Beim Aufbau des Testrahmens habe ich einmal `kdump.sh` (liest nur die Fensterliste per KWin-Skript, schreibt nichts) mit `bash -x` ausserhalb des verschachtelten KWin aufgerufen; es sprach dabei die D-Bus-Sitzung des Nutzers an (`loadScript`/`run`/`unloadScript` eines reinen Lese-Skripts namens `dumpt`, ohne sichtbare Wirkung, wieder entladen). Seitdem prueft das Skript, dass die Adresse der private Bus unter `/tmp/dbus-*` ist, und verweigert sonst. Alle weiteren Laeufe liefen nur im verschachtelten KWin.

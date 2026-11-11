# FreeSynergy Files (fs-files): Empfehlung aus der Dateimanager-Recherche

Stand: 2026-11-11. Grundlage: Haiku-Recherche in `/srv/FreeSynergy/.scratch/filemanager-research/` (`00-vergleich.md` und je Programm eine Datei), eigene Nachprüfung im Web (Quellen in Abschnitt f), Code und Doku von fs-files und dem Datei-Workbench in fs-components.
Regel (ADR 0066 und Gründungsideen): Vorbilder dürfen kostenpflichtig oder eingestellt sein. Wir kopieren nichts, wir lernen aus Mustern und bauen nach eigenem Design. Leitlinien: „people first“, „friert nie ein“, Zustand-Wiederherstellung, Topic-Interfaces als Ziele.

## 0. Nachprüfung der Haiku-Recherche (Korrekturen und geschlossene Lücken)

| Programm | Haiku-Stand | Nachgeprüft (2026-11-11) |
|---|---|---|
| Directory Opus | Preis leer, Undo „?“ | Windows only, Version 13 (13.16 laut FileHorse). Die Lizenz gilt unbefristet, Updates gibt es nur mit Abo: ein Jahr inklusive, danach Verlängerung (FAQ-Beispiel 25 AUD, abgelaufen 50 AUD). Den Listenpreis zeigt die Seite nur per Skript, also nicht belegt. **Undo vorhanden**: Liste der letzten 10 Aktionen, die Länge ist einstellbar, dazu ein dauerhaftes Protokoll der Dateioperationen. Außerdem Find-as-you-type (FAYT), Flat View, Statusleiste mit Ordnerstatistik, Utility Panel (Suchen, Sync, Duplikate, Logs) und eine Warteschlange für Kopieraufträge. |
| Total Commander | Preis/Version offen | **11.58.1 vom 2026-10-29**. Lizenz 42 EUR zzgl. MwSt.; Updates kostenlos „until further notice“ (bis auf Weiteres). Lister zeigt Dateien jeder Größe; Auswahl nach Muster, Größe, Datum und Inhalt; die vorige Auswahl lässt sich mit NUM / wiederherstellen. |
| XYplorer | Dual-Pane „?“, Preis offen | **Dual Pane vorhanden** (Featureseite). Mehrstufiges Undo/Redo, Action Log, Live-Filter, Farbfilter, Visual Filters, Tabsets, Mini Tree, Branch View (flache Ansicht), Batch-Rename mit Vorschau, portabel. Preis: Standard 34,95 USD laut Homepage-Snippet, Lifetime etwa 69,95 USD (abgeleitet). PC-WELT nennt 39,95 / 79,95 USD, die Angaben widersprechen sich. |
| ForkLift | offizielle Seite nicht abrufbar | Abrufbar. **4.7.7 vom 2026-10-20, ab macOS 14.6.** Einzelplatz 19,95 USD (1 Jahr Updates) bzw. 34,95 USD (2 Jahre), Familie 29,95 USD, Firma 69,95 USD. Die Lizenz bleibt gültig, nur Updates laufen aus. Belegt: Sync (ein- und zweiseitig, mit Vorschau der Unterschiede), Tags, Tabs, Workspaces, Quick Open, Multi-Rename-Presets, Git, viele Protokolle (SFTP, WebDAV, S3, B2, Drive, OneDrive, Dropbox, SMB, NFS), Aktivitäts- und Log-Ansicht. Haiku hatte bei Tabs und Tags „?“ und bei Sync „teilweise“; das ist jeweils **ja**. |
| Path Finder | offizielle Seite nicht abrufbar | cocoatech.io lädt nur per Skript, deshalb weiter nur Drittquellen. Preise laut Drittseiten im Oktober 2026: 32,95 USD/Jahr, 2 Jahre 55,95 USD, 5 Jahre 123 USD. Drop Stack ist bestätigt (Setapp und Cocoatech-Text): Dateien werden in einer Ablage geparkt und später abgelegt. Dazu Dual Pane, Size Browser, FolderSync, Folder Merging. |
| Files (files-community) | Lizenz MIT, Kritik fehlt | Lizenz **MIT und MPL-2.0** (GitHub), 46,6k Sterne. **v4.0 (2025-09)**: Omnibar (Pfad, Suche und Befehlspalette in einem Feld) und Dual Pane. **4.1 (2026-05)**: Toolbar anpassbar, Tags leichter bearbeitbar. **4.2 (~2026-07)**: Baumansicht in der Seitenleiste. **Kritik:** Geschwindigkeit und Speicherbedarf. Nutzer nennen es langsam und schwer; die Maintainer räumen ein, dass die Wahl von WinUI/WinAppSdk Leistung kostet (GitHub-Issue). Nur Windows, keine Linux-Version gefunden. |
| Finder | dünn | Belegt: Quick Look (Leertaste, mit Option als Vollbild), Spaltenansicht mit Vorschau, Spring-loaded Folders (Ordner öffnet sich beim Ziehen darüber), Pfadleiste als Ablageziel. Was Nutzer vermissen: am häufigsten Dual Pane, dazu kein FTP/SSH und wenig Anpassung. Die Quellen dazu sind überwiegend Herstellerblogs der Alternativen, also schwach belegt. |
| Marta | aktiv? | Letzte Version 0.8.2 vom 2024-07, seitdem keine neue. Der Entwickler meldet sich „back on track“ (undatiert); nach der Beta soll es eine Bezahllizenz geben. Status: **ruhend**. |
| yazi | dünn | Belegt (README): asynchrone Ein-/Ausgabe, Task-Planung mit Fortschritt, Abbruch und Priorität, Vorschau für Bild, Video, PDF, Archiv, Code und Ordner, Bulk-Rename, Anbindung an rg/fd/fzf/zoxide, Tabs, Visual Mode, Lua-Plugins, DDS (Publish/Subscribe zwischen Instanzen, Zustand bleibt erhalten). Lizenz auf der README-Seite nicht genannt (vermutlich MIT, **nicht verifiziert**). Undo nicht belegt. |
| Spacedrive | „Alpha, Tabs geplant“ | **Veraltet.** v2-Alpha im Dezember 2025 (macOS/Linux). Im März 2026 Schwenk auf **v3**, ein Produkt, das vom Suchindex ausgeht (Rust, Tokio, SQLite, LanceDB). Keine stabile Version. Als Vorbild nur für die Idee „Index plus Jobs“ brauchbar. |
| Dolphin | ohne Undo | Undo mit Strg+Z. **Lehre aus Bug 451745:** Strg+Z macht still eine Aktion aus einem anderen Ordner rückgängig, was Nutzer verwirrt. Redo kommt erst über KIO. Filterleiste mit Strg+I. |

Zusätzliche Kandidaten, die jetzt sichtbar wurden (nur kurz):
- **Thunar** (Xfce): Bulk Renamer mit Plugins (Nummerieren, Suchen/Ersetzen, Groß/klein), *Custom Actions* im Kontextmenü, Dual Pane mit F3. Der Bulk Renamer ist ein gutes Vorbild für eine Umbenennung, die man vorher sieht.
- **Nemo** (Cinnamon): Aktionen als Dateien (`.nemo_action`). Ein eigener Bulk-Renamer ist nicht belegt; Nutzer binden den von Thunar ein.
- **Open Salamander** (vormals Altap): 2023 als GPLv2 veröffentlicht, die Entwicklung ruht seit 2019. Klassischer, schneller Commander.
- **One Commander** (Windows): Miller-Spalten wie im Finder, Dual Pane, für Heimnutzer kostenlos. Ein Nutzer bemängelt Fokusfehler in der Spaltenansicht.
- Q-Dir, Xplorer², muCommander, Explorer++ und Nexus File: nicht geprüft. Nichts deutet darauf hin, dass sie Muster bieten, die oben fehlen.

## a) Funktionsmatrix (Pflicht / Erwartet / Differenzierend)

Herkunft = Programm, an dem man das Muster am besten studieren kann (nicht kopieren).

| Stufe | Funktion | Herkunft (Vorbild) | fs-files Kern | fs-files Fenster |
|---|---|---|---|---|
| **Pflicht** | Ordner durchsuchen, Liste mit Spalten (Name, Größe, Datum, Typ), Sortieren | alle; Finder/Dolphin für Spalten | ja (`list_sorted`) | nur generierte Tabelle, ohne Seiten |
| Pflicht | Seitenleiste mit Orten (Start, Favoriten, Papierkorb, Speicher) | Dolphin Places, Finder | Papierkorb, Backends ja | im Workbench (`places.rs`), im Fenster nicht |
| Pflicht | Pfad als Brotkrumen, editierbar | Path Finder, Files Omnibar, DO Location Bar | Ordner per ID (`get_folder`) | im Workbench (`crumbs_row`) |
| Pflicht | Anlegen, Umbenennen, Verschieben, Kopieren, Papierkorb, Wiederherstellen | alle | **ja, stark** (atomar, nie überschreiben, `OnConflict`) | ja (als Formulare) |
| Pflicht | Konflikt-Dialog (verweigern / beide behalten) | TC, DO, Finder | ja (Ersetzen bewusst nicht) | Workbench fragt (`NameTaken`) |
| Pflicht | Mehrfachauswahl (Shift/Strg, Rahmen, alles) | alle | Operationen je Datei | **fehlt** (Workbench: „one thing selected“) |
| Pflicht | Tastaturbedienung (Pfeile, Enter, Rück, F2, Entf, Strg+C/X/V) | Explorer-Standard, TC | – | **fehlt** |
| Pflicht | Fortschritt, Abbruch, Warteschlange für lange Aufgaben, UI blockiert nie | yazi Tasks, DO Kopier-Queue, ForkLift Aktivität, Spacedrive Jobs | Uploads fortsetzbar, `run_to_end` | Workbench `transfers.rs`; Fenster ohne Timeout |
| Pflicht | Suche nach Name | alle | ja (`find`) | ja |
| **Erwartet** | Undo/Redo mit sichtbarer Liste | XYplorer (mehrstufig), DO (Undo-Liste), Dolphin (Warnung: Bereich zeigen) | Disk-Schritte mit Undo intern (`repo/steps.rs`), **kein Nutzer-Undo** (`undo` unsupported) | fehlt |
| Erwartet | Live-Filter im aktuellen Ordner beim Tippen | XYplorer Live Filter Box, Dolphin Strg+I, DO FAYT | Größe/Datum-Filter | Workbench `filter.rs` (Entwurf) |
| Erwartet | Vorschau-Panel und Schnellansicht mit Leertaste | Finder Quick Look, DO Viewer Pane, yazi | **fehlt** (`preview` unsupported) | Workbench `file_preview` |
| Erwartet | Tabs, mit Wiederherstellung beim Start | XYplorer Tabsets, Double Commander Tabsätze, Files | – | fehlt |
| Erwartet | Raster/Kacheln mit Vorschaubildern | Finder Galerie, Files, Dolphin | fehlt | Workbench-Raster; Gallery-Grid-Komponente |
| Erwartet | Batch-Umbenennen mit Vorschau | Thunar Bulk Renamer, XYplorer, TC Strg+M | fehlt (`renameBulk`) | fehlt |
| Erwartet | Statusleiste (Anzahl, Auswahlgröße, freier Platz) | DO, TC | Daten teils vorhanden | fehlt |
| Erwartet | Drag & Drop, auch auf Pfadleiste und Seitenleiste | Finder (Spring-loaded, Pfadleiste) | – | fehlt |
| Erwartet | Änderungen von außen live sehen | Dolphin/Nautilus (Watcher) | **nur `rescan`**, kein Watcher | fehlt |
| Erwartet | Tags/Favoriten | Finder, XYplorer, DO, Files, ForkLift | fehlt (`tag`) | fehlt |
| **Differenzierend** | Dual Pane mit F5/F6 „in die andere Seite“ | TC, Double Commander, DO, Files 4.0 | – | fehlt |
| Differenzierend | Omnibar: Pfad, Suche und Befehle in einem Feld | Files 4.x | – | fehlt |
| Differenzierend | Ablage („Drop Stack“) als Ziel für spätere Aktionen; Übergabe an andere FreeSynergy-Programme | Path Finder Drop Stack | Datei per ID referenzierbar (`file.resolve`) | fehlt |
| Differenzierend | Ordnervergleich/Sync mit Vorschau der Unterschiede | ForkLift, TC, DO, Krusader-Profile | `rescan` meldet Abweichungen | fehlt |
| Differenzierend | Duplikate per Prüfsumme | DO, TC | BLAKE3 ist schon gespeichert | fehlt (`duplicates`) |
| Differenzierend | Flache Ansicht (alle Unterordner) | DO Flat View, XYplorer Branch View | `find` über alles | fehlt |
| Differenzierend | Mehrere Speicher (lokal, S3) gleich behandelt | ForkLift, Commander One | **ja** (`BlobBackend`, Registry) | Typ `StorageBackend` |
| Differenzierend | Wiederaufnehmbare Übertragungen nach Absturz | ForkLift (Queue), Spacedrive (Crash-Recovery) | **ja**, getestet | teilweise |

## b) UX- und UI-Muster

**UX-Muster**
- **Navigation:** Zurück/Vor/Hoch und Brotkrumen, Klick auf ein Segment springt dorthin, Tippen ins Feld macht den Pfad editierbar (Path Finder, Files). Rück-Taste geht eine Ebene hoch. Der Baum ist nur optional (DO, Files 4.2).
- **Auswahl:** Explorer-Konventionen (Klick, Shift, Strg, Strg+A, Rahmen). Dazu aus TC: Auswahl nach Muster und „vorige Auswahl wiederherstellen“. Die Auswahl bleibt über eine Navigation zurück erhalten.
- **Vorschau:** Ein Panel rechts (Finder, DO) plus Leertaste für eine große Schnellansicht (Finder Quick Look). Vorschauen werden asynchron geladen; was noch nicht da ist, zeigt einen Platzhalter und blockiert nichts (yazi).
- **Suche:** Zwei Stufen. (1) Live-Filter: Tippen in der Liste filtert sofort den aktuellen Ordner (XYplorer, Dolphin, DO FAYT). (2) Echte Suche über alles mit Ergebnisliste als eigener „Ort“ (DO Collections). Nicht vermischen: Dolphins Nutzer streiten genau darüber.
- **Batch:** Jede Massenaktion zeigt vorher, was passiert (Thunar/XYplorer-Vorschau), läuft als Job mit Fortschritt und ist danach als **eine** Undo-Einheit rückgängig zu machen.
- **Tastatur:** Standardbelegung wie im Explorer (F2, Entf, Strg+C/X/V, Strg+Z/Y, Strg+F, Strg+L für Pfad, Strg+T für Tab, Leertaste für Vorschau). Optional eine Commander-Belegung (F3 bis F8, Tab wechselt die Seite) und eine Befehlspalette (Strg+Umschalt+P), die jede Aktion mit ihrem Kürzel zeigt. Damit lernt man die Tasten nebenbei (Files).
- **Undo:** Eine Liste der Aktivitäten mit Klartext („„Foto.jpg“ nach Urlaub verschoben“), Undo/Redo mehrstufig (XYplorer, DO). Lehre aus Dolphin: Undo sagt immer, **was** und **wo** es rückgängig macht, und springt dorthin. Endgültiges Löschen (purge) ist nicht rückgängig zu machen und sagt das vorher.
- **Tabs/Dual Pane:** Tabs pro Fensterhälfte. Dual Pane ist ein Schalter (F3 wie bei Dolphin und Thunar), nicht der Normalzustand. Tabsätze werden beim Schließen gespeichert und beim Start wiederhergestellt (Double Commander, XYplorer).
- **Schnellzugriff:** Favoriten in der Seitenleiste per Drag & Drop (Finder, Dolphin Places), dazu die zuletzt besuchten Orte und eine Hotlist, die man per Tastatur unscharf durchsucht (XYplorer Fuzzy-Favoriten, yazi und zoxide).

**UI-Muster**
- **Dichte:** Zwei Stufen, „bequem“ (Standard, Files/Finder) und „kompakt“ (TC/DO). Die 600 Farb- und Schriftoptionen von DO bewusst nicht; Themen kommen aus fs-components.
- **Seitenleiste:** Gruppen „Orte“, „Speicher“ (Backends), „Tags“, „Papierkorb“. Einklappbar.
- **Statusleiste:** Anzahl der Einträge, Auswahl (Anzahl und Größe), laufende Jobs (klickbar zur Jobliste), freier Platz des Speichers (DO, TC).
- **Kontextmenü:** kurz, nach Häufigkeit sortiert. Seltenes steht unter „Mehr“ und in der Befehlspalette. Jeder Eintrag zeigt sein Kürzel.
- **Drag & Drop:** Ziehen auf Ordner, Pfadleiste, Seitenleiste und die andere Seite. Ein Ordner öffnet sich beim Darüberhalten (Spring-loaded wie Finder). Strg wechselt zwischen Kopieren und Verschieben, sichtbar am Cursor. Ziehen nach außen und von außen hinein ist der Weg zum Upload.

## c) Was fs-files heute kann und was fehlt

Quellen: [DESIGN.md](https://github.com/FreeSynergy/fs-files/blob/main/DESIGN.md) (`/srv/FreeSynergy/fs-files/DESIGN.md`), [README.md](https://github.com/FreeSynergy/fs-files/blob/main/README.md) (`/srv/FreeSynergy/fs-files/README.md`), Crates unter `/srv/FreeSynergy/fs-files/crates/`, Workbench [file_manager](https://github.com/FreeSynergy/fs-components/tree/main/crates/fs-components-workbenches/src/file_manager) (`/srv/FreeSynergy/fs-components/crates/fs-components-workbenches/src/file_manager/`), Anforderungen [files/requirements.md](https://github.com/FreeSynergy/fs-documentation/blob/main/docs/de/programs/apps/files/requirements.md) (`/srv/FreeSynergy/fs-documentation/docs/de/programs/apps/files/requirements.md`).

**Stark (Kern `fs-files-core`, Server `fs-files-server`, Version 0.0.5):**
- Backends: `LocalFolder` (echte Namen, nie überschreiben, atomares `renameat2` unter Linux, fsync) und `S3Backend` (Multipart, übersteht einen Neustart); `BackendRegistry` mit atomarem Austausch.
- Ordner und Dateien: anlegen, umbenennen, verschieben, kopieren, Papierkorb, wiederherstellen (auch in einen anderen Ordner), endgültig löschen, Papierkorb leeren. Konfliktregel `Refuse`/`KeepBoth`. Erst die Platte, dann die Datenbank; schlägt ein Schritt fehl, wird der andere zurückgenommen.
- Uploads lassen sich fortsetzen, BLAKE3-Prüfsumme während des Streams, `pending_uploads`.
- Suche nach Name, Sortierung (Name, Datum, Größe, Typ), Filter nach Größe und Datum, Seiten zu 100.
- `rescan` übernimmt Dateien von außen. Änderungs-Feed `FileFeed` (Created/Updated/Deleted). Sensible Dateien markieren (ADR 0029).
- Typbeschreibungen `File`, `Folder`, `StorageBackend`, `Picture`, `Album` (AS2) für das generierte Frontend.

**Fenster heute (`fs-files-app`):** die **generierte Admin-Oberfläche** (`fs-admin-frontend` @4688cee). Laut DESIGN.md: Listen sind Tabellen, es gibt keine Seiten und kein Raster, Upload und Download laufen über ein Formularfeld mit `file:`-Link (kein Dateiwähler). Der Datei-Workbench in fs-components (Baum, Orte, Brotkrumen, Liste und Raster, Vorschau, Transfers, Picker, Filterentwurf) wird **vom Fenster nicht genutzt**. **Widerspruch in DESIGN.md:** Der Abschnitt „ADR 0063“ beschreibt noch das Workbench-Fenster, der Abschnitt „ADR 0066“ sagt, es sei entfernt. Das sollte bereinigt werden.

**Lücken (nach Gewicht):**
1. Keine eigene Datei-Oberfläche (Tabelle statt Dateiansicht), keine Mehrfachauswahl, kein Tastaturmodell, kein Drag & Drop.
2. Kein Nutzer-Undo (`undo` unsupported), obwohl der Kern umkehrbare Schritte hat und die Contracts AS2-Aktivitäten (`Move`, `Update`, `Delete`) nennen.
3. Keine Vorschau (`preview`, `previewGenerate` unsupported), keine Thumbnails.
4. Kein Watcher: Änderungen von außen sieht man nur über `rescan`, und der hält die Schreibsperre. Das kollidiert mit „friert nie ein“.
5. Keine Tabs, kein Dual Pane, keine Zustand-Wiederherstellung des Fensters.
6. Kein Batch-Umbenennen (`renameBulk`), keine Tags (`tag`), keine Duplikate (`duplicates`), obwohl die Prüfsummen schon gespeichert sind.
7. **Windows:** Server und Fenster sprechen über einen Unix-Socket, und `renameat2` gibt es nur unter Linux (für andere Systeme ist ein Ausweichweg da). Ob und wie es auf Windows läuft, ist offen.
8. Grundsatzfrage: fs-files verwaltet **eine Ablage unter einer Wurzel** (`FS_FILES_ROOT`) plus Backends. Ein klassischer Dateimanager zeigt das ganze Dateisystem. Das bestimmt, welche Vorbilder überhaupt passen (siehe Frage 1).

## d) Empfehlung

**Reihenfolge der ersten 8 Schritte** (jeder baut auf dem vorigen auf):

1. **Eine echte Dateiansicht statt der generierten Tabelle.** Den Datei-Workbench aus fs-components zum Fenster von fs-files machen: Liste mit Spalten, Seiten bzw. virtuelles Scrollen, Seitenleiste mit Orten und Speichern, Brotkrumen, Statusleiste. *Grund:* Ohne diese Ansicht ist alles Weitere unsichtbar, und die Bausteine gibt es schon. *Vorbild:* Files für Optik und Aufgeräumtheit, Finder und Dolphin für Spalten und Orte.
2. **„Friert nie ein“ als Architekturregel.** Jede Operation ist ein Job mit Fortschritt, Abbruch und Liste in der Statusleiste. Listen und Vorschauen laden asynchron, und das Warten auf den Server hat einen Timeout. *Grund:* Das ist ein Gründungsprinzip, und die Kritik an Files (WinUI langsam und schwer) und ForkLift (große Ordner, Abstürze) zeigt, wo Nutzer abspringen. *Vorbild:* yazi (Task-Planung), DO (Kopier-Warteschlange), ForkLift (Aktivitätsansicht).
3. **Mehrfachauswahl und Standard-Tastaturmodell**, dazu Drag & Drop in der App. *Grund:* Pflicht in jedem Vorbild; Batch, Undo und Dual Pane brauchen es. *Vorbild:* Explorer- und Finder-Konventionen, TC für Auswahl nach Muster und „Auswahl wiederherstellen“.
4. **Undo/Redo als sichtbares Aktivitätsprotokoll.** Jede Änderung wird als AS2-Aktivität erfasst (`Move`, `Update`, `Delete`, `Undo`), auch eine Massenaktion als eine Einheit. Undo zeigt, was und wo es zurücknimmt. *Grund:* „people first“ (Fehler ohne Angst), passt genau zu den Topic-Interfaces (Aktivitäten statt eigenem Format) und zum Kern, der seine Schritte schon umkehren kann. Unter den freien Linux-Programmen ist es selten gut gelöst. *Vorbild:* XYplorer (mehrstufig, Action Log), DO (Undo-Liste), Dolphin als Warnung.
5. **Live-Filter und Befehlspalette (Omnibar).** Wer in der Liste tippt, filtert den aktuellen Ordner. Strg+L bzw. Strg+Umschalt+P öffnet ein Feld für Pfad, Suche und Befehle. *Grund:* Damit sind Maus- und Tastaturnutzer gleich schnell, und neue Funktionen finden sich ohne Menüsuche. *Vorbild:* XYplorer und Dolphin für den Filter, Files 4.x für die Omnibar.
6. **Vorschau-Panel und Schnellansicht mit der Leertaste**, für Bild, Text und PDF zuerst, asynchron und mit Größenlimit. *Grund:* Am häufigsten gelobt (Finder, DO, yazi). Sie ersetzt das Öffnen in einem anderen Programm. *Vorbild:* Finder Quick Look und Spaltenansicht, DO Viewer Pane.
7. **Tabs und Wiederherstellung des Zustands.** Tabs, Ordner, Auswahl, Scrollposition, Ansicht und Sortierung pro Ordner werden beim Schließen gespeichert und beim Start (auch nach einem Absturz) wiederhergestellt. *Grund:* Gründungsprinzip Zustand-Wiederherstellung. *Vorbild:* Double Commander (Tabsätze), XYplorer (Tabs bleiben über Sitzungen).
8. **Dual Pane als Schalter (F3) und Batch-Umbenennen mit Vorschau.** *Grund:* Das ist der Unterschied zu Finder und Nautilus. Dual Pane ist die meistvermisste Funktion im Finder (schwache Quelle), und Massen-Umbenennen gibt es in allen Power-Tools; mit Undo (Schritt 4) ist es sicher. *Vorbild:* TC und Double Commander für Tastatur und Dual Pane, Thunar und XYplorer für die Umbenennung mit Vorschau.

**Danach (Kandidaten):** Watcher statt nur `rescan`, Tags (AS2 `tag`), Duplikate per BLAKE3, Ablage nach Art des Drop Stack als Übergabe an andere FreeSynergy-Programme (Topic-Interface als Ziel: „an Kalender/Aufgaben/Nachricht anhängen“), Ordnervergleich mit Vorschau (ForkLift-Muster), flache Ansicht.

**Bewusst NICHT (vorerst) und warum:**
- **Eigene Skriptsprache oder Makros** (DO, XYplorer): großer Aufwand und eine eigene Welt. Erweiterung später über Topic-Interfaces und Programme, nicht über Skripte im Prozess (yazi-Kritik: Plugins im Prozess sind ein Sicherheitsrisiko).
- **Ein ganzer Zoo von Protokollen im Dateimanager** (FTP, SMB, Dropbox …, ForkLift und Commander One): Speicher kommen als `BlobBackend` in den Kern, nicht ins Fenster. WebDAV steht in den Anforderungen; FTP nicht.
- **Eingebautes Terminal und Git-Integration** (Files, Path Finder, Marta): fremder Zweck. „Im Terminal öffnen“ als Aktion genügt.
- **Kompatibilität zu TC-Plugins** (Double Commander): bindet an eine fremde Binärschnittstelle unter Windows.
- **Hunderte Optik-Optionen** (DO, 600 Farben): Optik kommt aus fs-components; nur zwei Dichtestufen.
- **Miller-Spalten als Standard**: Finder und One Commander zeigen, dass sie fokus- und lesefehleranfällig sind; höchstens später als Ansicht.
- **Ersetzen beim Namenskonflikt**: Die bewusste Entscheidung des Kerns (nie überschreiben) bleibt. Die Oberfläche bietet „beide behalten“ und „umbenennen“.
- **Sicheres Löschen, App-Deinstaller, eigener Archivierer** (Path Finder, ForkLift, TC): Randfunktionen. Archive höchstens später als „Ordner“-Ansicht (`Folder.archive` steht schon in der Liste).

**Welches Vorbild für welchen Teil (Kurzform):**
| Teil | Lernen von |
|---|---|
| Optik, Aufgeräumtheit, Omnibar/Befehlspalette | Files (files-community); Warnung: Leistung |
| Tastatur, Dual Pane, Auswahl nach Muster | Total Commander, Double Commander |
| Filter, Undo, Tabsätze, Batch-Vorschau | XYplorer |
| Undo-Liste, Statusleiste, Kopier-Warteschlange, flache Ansicht | Directory Opus |
| Spalten, Quick Look, Pfadleiste als Ziel, Spring-loaded | Finder |
| Ablage (Drop Stack) | Path Finder |
| Asynchronität, Jobs, Tastatur-Effizienz, Zoxide-artige Sprünge | yazi |
| Sync mit Vorschau, Aktivitäts-Log, mehrere Speicher | ForkLift |
| Orte, Filterleiste, Undo-Fallstrick | Dolphin |
| Bulk-Renamer, Aktionen im Kontextmenü | Thunar (Nemo-Aktionen) |

## e) Risiken und offene Fragen an den Nutzer

Risiken: (1) **Leistung**: Files zeigt, dass eine moderne Optik mit schwerem Unterbau Nutzer vertreibt. Blinc muss große Ordner (über 10 000 Einträge) flüssig zeigen; dafür vor Schritt 1 messen. (2) `rescan` hält die Schreibsperre, ohne Watcher bleibt die Ansicht veraltet. (3) Windows-Lauffähigkeit ist ungeklärt (Unix-Socket, `renameat2`). (4) Generiertes Frontend gegen eigenen Workbench widerspricht der Regel „keine Optik im Programm“ (ADR 0066), wenn es nicht sauber getrennt wird.

**Fragen (gebündelt):**
1. **Reichweite:** Soll fs-files nur die eigene Ablage (`FS_FILES_ROOT` plus Backends) zeigen, oder als richtiger Dateimanager auch beliebige Ordner des Rechners (Home, USB-Stick)? Davon hängt ab, ob TC/DO/Finder überhaupt die richtigen Vorbilder sind.
2. **Fenster:** Darf fs-files statt der generierten Admin-Tabelle den Datei-Workbench aus fs-components als Hauptansicht nutzen (Ausnahme oder Erweiterung zu ADR 0066)?
3. **Undo:** Soll der Verlauf einen Neustart überdauern (gespeichert als AS2-Aktivitäten im Objektspeicher) oder nur für die Sitzung gelten?
4. **Tastatur und Layout als Standard:** Explorer/Finder-Belegung mit Einzelansicht als Standard und Commander-Modus (F5/F6, Dual Pane) zum Umschalten? Oder umgekehrt?
5. **Windows:** Ab wann muss fs-files unter Windows laufen, also vor oder nach den ersten 8 Schritten?

## f) Quellenverzeichnis (abgerufen 2026-11-11)

Lokal:
- Haiku-Recherche: `/srv/FreeSynergy/.scratch/filemanager-research/00-vergleich.md` und die Einzeldateien im selben Ordner (Quellen dort).
- fs-files: https://github.com/FreeSynergy/fs-files/blob/main/DESIGN.md (`/srv/FreeSynergy/fs-files/DESIGN.md`), https://github.com/FreeSynergy/fs-files/blob/main/README.md (`/srv/FreeSynergy/fs-files/README.md`), https://github.com/FreeSynergy/fs-files/tree/main/crates (`/srv/FreeSynergy/fs-files/crates/`).
- Workbench: https://github.com/FreeSynergy/fs-components/tree/main/crates/fs-components-workbenches/src/file_manager (`/srv/FreeSynergy/fs-components/crates/fs-components-workbenches/src/file_manager/`).
- Anforderungen: https://github.com/FreeSynergy/fs-documentation/blob/main/docs/de/programs/apps/files/requirements.md (`/srv/FreeSynergy/fs-documentation/docs/de/programs/apps/files/requirements.md`).

Web (Nachprüfung):
- Directory Opus: https://www.gpsoft.com.au/ ; https://docs.dopus.com/doku.php?id=basic_concepts:the_lister ; https://resource.dopus.com/t/common-purchasing-upgrading-and-licensing-questions/23553 ; https://resource.dopus.com/t/directory-opus-13-now-available/48103 ; https://chaoses-ib.gitbook.io/directory-opus/manual/file_operations/tracking_and_undoing_file_operations ; https://chaoses-ib.gitbook.io/directory-opus/manual/basic_concepts/flat_view ; https://www.filehorse.com/download-directory-opus
- Total Commander: https://www.ghisler.com/ ; https://www.ghisler.com/order.htm ; https://www.ghisler.com/featurel.htm
- XYplorer: https://www.xyplorer.com/features.php ; https://xyplorer.com/ ; https://www.pcwelt.de/article/1141576/xyplorer-3.html
- ForkLift: https://binarynights.com/ ; https://binarynights.com/store
- Path Finder: https://setapp.com/apps/path-finder ; https://www.techbloat.com/software/path-finder/pricing/ ; https://talk.tidbits.com/t/path-finder-26-0/33442 ; https://cocoatech.io/post/why-apples-finder-is-not-enough-if-you-are-in-tech/
- Files: https://github.com/files-community/Files ; https://files.community/docs ; https://alternativeto.net/news/2025/9/files-v4-0-is-out-now-with-a-new-omnibar-dual-pane-mode-expanded-cloud-support-and-more ; https://alternativeto.net/news/2026/5/files-4-1-brings-toolbar-customization-revamped-settings-easier-tag-editing-and-more/ ; https://www.comss.ru/page.php?id=21154 ; https://github.com/files-community/Files/issues/14939 ; https://alternativeto.net/software/files-uwp/about/
- Finder: https://www.macrumors.com/guide/top-tips-macos-finder/ ; https://macmost.com/10-tips-for-using-the-finder-preview-pane.html ; https://macos-tahoe.com/blog/best-finder-alternatives-mac-file-managers-2026/ (Herstellerumfeld, schwach) ; https://forums.macrumors.com/threads/professional-workflows-broken-finder-sidebar-network-priority-wacom-input.2467047
- Marta: https://marta.sh/changelog/ ; https://marta.sh/blog/back-on-track/
- yazi: https://yazi-rs.github.io/ ; https://github.com/sxyazi/yazi
- Spacedrive: https://spacedrive.com/blog/spacedrive-v3-launch ; https://spacedrive.com/blog/spacedrive-v2-release
- Dolphin: https://docs.kde.org/trunk_kf6/en/dolphin/dolphin/command-reference.html ; https://bugs.kde.org/show_bug.cgi?id=451745 ; https://bugs.kde.org/show_bug.cgi?id=451746
- Thunar/Nemo: https://docs.xfce.org/xfce/thunar/bulk-renamer/start ; https://docs.xfce.org/xfce/thunar/custom-actions ; https://forum.endeavouros.com/t/wiki-customising-nemos-context-menu-with-nemo-actions/54611
- Open Salamander: https://github.com/OpenSalamander/salamander ; https://en.wikipedia.org/wiki/Altap_Salamander
- One Commander: https://www.onecommander.com ; https://alternativeto.net/software/bitcommander/about

Nicht abrufbar oder nicht belegt: der Listenpreis von Directory Opus (Seite per Skript), cocoatech.io (Skript), die Lizenz von yazi auf der README-Seite, die Nautilus-Undo-Details, Q-Dir, Xplorer², muCommander, Explorer++ und Nexus File (nicht geprüft).

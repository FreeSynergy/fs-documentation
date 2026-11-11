# Vergleich Dateiprogramme (Stand 2026-11-11)

Legende: **ja** = in den Quellen belegt; **teilweise** = belegt mit Einschränkung; **nein** = belegt als fehlend oder geplant; **?** = in den Quellen nicht gefunden (Lücke, kein Nachweis des Gegenteils).
Spaltenkürzel: DO = Directory Opus, TC = Total Commander, XY = XYplorer, Files = Files (files-community), Finder = Finder (macOS), PF = Path Finder, FL = ForkLift, C1 = Commander One, DC = Double Commander, MC = Midnight Commander, yazi = yazi, Kru = Krusader, Dol = Dolphin, Nau = Nautilus/GNOME Files, Marta = Marta, SD = Spacedrive.

Vorlage zum Lesen: Einzelnachweise siehe jeweilige Datei in diesem Ordner.

| Merkmal | DO | TC | XY | Files | Finder | PF | FL | C1 | DC | MC | yazi | Kru | Dol | Nau | Marta | SD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tabs | ja | ja | ja | ja | ? | ja | ? | ja | ja | ? | ja | ja | ja | ja | ? | nein (geplant) |
| Dual-Pane | ja | ja | ? | ja | ? | ja | ja | ja | ja | ja | ? | ja | ja (Split) | ? | ja | nein (geplant) |
| Spaltenansicht | ? | ? | ? | ja | ja | ? | ? | teilweise (3 Ansichtsmodi) | ? | ? | ? | ? | ? | ? | ? | ? |
| Vorschau | ja | teilweise | ja | ja | ja | ? | ja | ja | ? | teilweise (Viewer) | ja | ? | ja | ? | ? | ? |
| Suche / Filter | ja (Filter) | ja | ja (Live-Filter) | ? | ? | ? | ja (Regex) | ja (Regex) | ? | ? | ? | ? | ? | ja (Tracker) | ? | ? |
| Tags / Labels | ja | ? | ja | ja | ja | ja (OpenMeta) | ? | ? | ? | ? | ? | ? | ja | teilweise (2017, unklar) | ? | ? |
| Batch-Umbenennen | ja (Makros) | ja (Regex) | ja (Vorschau) | ? | ? | ja | ? | ? | ja | ? | ? | ? | ? | ? | ? | ? |
| Ordner-Vergleich / Sync | ja | ja | ? | ? | ? | ja | teilweise | ? | ja | teilweise (Diff) | ? | ja (Profile) | ? | ? | nein (fehlt laut Nutzer) | ? |
| Archive | ja | ja | ? | ja | ? | ja | ja | ja | ? | ja (VFS) | ja (Vorschau) | ? | ? | ? | ? | ? |
| FTP / SFTP | ja (FTP) | ja | ? | ja | ? | ? | ja | ja | ? | ja (VFS) | ? | ja | ? | ja | ? | nein |
| Cloud-Anbindung | nein (nicht auf Seite) | ? | ? | ja | ? | ja | ja | ja | ? | ? | ? | ? | ? | ja | ? | teilweise (geplant) |
| Befehlspalette | ? | ? | ? | ja | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Tastatur-Bedienung | ja | ja | ja | ? | ja | ? | ? | ja | ? | ja | ja | ? | ? | ? | ja | ? |
| Undo | ? | ? | ja (mehrstufig) | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Papierkorb | ? | ? | ? | ? | ? | ja (sicheres Löschen) | ? | ? | ? | ? | ? | ? | ja (Places) | ? | ? | ? |
| Favoriten / Schnellzugriff | ? | ? | ja (Hotlist) | ? | ? | ? | ja (Lesezeichen) | ? | ? | ? | ? | ? | ja (Places) | ? | ? | ? |
| Konfigurierbarkeit | ja | ja | ja | ja | teilweise | ? | ? | teilweise (Hotkeys) | ? | ? | ja (TOML) | ? | ja | ? | ja | ? |
| Scripting / Erweiterung | ja | ja (Plugins) | ja | ? | ? | ? | ? | ? | ja (Plugins) | ? | ja (Lua) | ? | ? | ? | ja | ? |
| Terminal integriert | ? | teilweise (Befehlszeile) | ? | ja | ? | ja | ? | ja | ? | ja (Subshell) | ja (Terminal-App) | ? | ja | ? | ja | ? |
| Git-Integration | ? | ? | ? | ja | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Plattform | Win | Win | Win | Win | macOS | macOS | macOS | macOS | Linux, Win, macOS | Unix (Terminal) | Terminal | Linux | Linux | Linux | macOS | Win, Linux, macOS |
| Preis / Status | kommerziell | Shareware | kommerziell | kostenlos (Store: kostenpflichtig) | inkl. macOS | kommerziell | kommerziell | frei + Pro | frei | frei | frei | frei | frei | frei | frei (unsicher) | Open Source, Alpha |

## Was die besten gemeinsam haben

Die "besten" Programme im Sinne des Auftrags sind hier Directory Opus, Total Commander, XYplorer, Path Finder, ForkLift, Double Commander und Files. Gemeinsam (in den Quellen belegt):
1. **Tabs und Doppelbereich** (fast alle, Ausnahme Finder und Spacedrive).
2. **Batch-Umbenennen mit Vorschau oder Regex** (DO, TC, XY, PF, DC).
3. **Ordnervergleich und Synchronisation** (DO, TC, PF, DC, Krusader).
4. **Eingebaute Archive und Server-Anbindung** (FTP/SFTP bei DO, TC, FL, C1, Krusader).
5. **Anpassbare Oberfläche und Tastatur** (DO, TC, XY, Files, Marta, yazi).

Außerdem häufig: Vorschau (DO, XY, FL, C1, yazi), Tags (DO, XY, Files, PF, Dolphin).

## Was nur einzelne haben (Alleinstellungsmerkmale)

- **XYplorer:** Filter (Farb-, Live-, Auswahlfilter) und mehrstufiges Undo, beides in den Quellen klar belegt.
- **Path Finder:** "Drop Stack" als Zwischenablage für Dateien.
- **Directory Opus:** Scripting-Oberfläche mit eigenen Dialogen, Makro-Umbenennen.
- **yazi:** Terminal-Bildvorschau (Kitty, iTerm2, Sixel) mit Lua-Plugins und eigenem Paketmanager.
- **Spacedrive:** geräteübergreifende Sicht mit Indexer und Identifier (noch Alpha, Tabs und Doppelbereich geplant).
- **Files:** Omnibar und Befehlspalette, Git-Integration.

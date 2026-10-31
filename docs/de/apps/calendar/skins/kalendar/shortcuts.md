# Kalendar - Tastatur-Shortcuts

## Übersicht

Kalendar dokumentiert **keine festen, stabilen Tastatur-Shortcuts** in seiner offiziellen Hilfe; die Kirigami-Oberfläche folgt den Qt-/Plasma-Konventionen. Diese Datei listet, was tatsächlich funktioniert (inkl. Qt-Standards), und markiert verbreitet angenommene, aber nicht dokumentierte Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: KDE-Gear-Versionen (Kirigami 2). Nach Updates sollte diese Liste geprüft werden.

## Allgemein (Qt-/Desktop-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | zwischen Bedienelementen springen |
| `Enter` / `Leertaste` | ausgewähltes Element öffnen / umschalten |
| `Esc` | Dialog, Panel oder Suchfeld schließen |
| `F10` oder `Alt+F` | Menü/Seitenleiste öffnen (Qt-Konvention, je nach Version) |
| `Alt+E` / `Alt+S` | Unterstrich-Buchstaben in Beschriftungen (Access-Keys) |
| `Ctrl+Q` | Anwendung beenden (Plasma-Standard) |

## Navigation und Ansicht

| Shortcut | Funktion |
|----------|----------|
| `←` / `→` | vorheriger/nächster Tag bzw. Woche/Monat, wenn die Ansicht den Fokus hat |
| `Ctrl+F` | Suchfeld fokussieren |
| `Pos1` / `Ende` | (nicht dokumentiert) Anfang/Ende des Zeitraums |

## Ereignisse

| Shortcut | Funktion |
|----------|----------|
| `N` | neues Ereignis — **nicht dokumentiert**; Anlage über die Schnellerfassungszeile oder den `+`-Knopf |
| `Entf` | markiertes Ereignis löschen — funktioniert in Listenansichten (Qt-Standard), in Kalenderzellen unzuverlässig |
| `Doppelter Klick` / `Enter` auf Zelle | neues Ereignis an dieser Zeit anlegen |

## Schnellerfassung

In der Agenden-Ansicht kann die Eingabezeile direkt beschrieben werden; `Enter` legt das Ereignis an. Datumsangaben wie `morgen`, `Fr 15:00`, `in 2 h` werden erkannt.

## Mac-Varianten

Kalendar läuft primär unter Linux; ein Mac-Build ist nicht offiziell supported. Wo es gebaut wird, ersetzt `Cmd` die `Ctrl`-Tasten.

## Ausdrücklich nicht vorhanden

- Keine Vim-/Thunderbird-artigen Ein-Tasten-Shortcuts
- Kein „Heute"-Shortcut dokumentiert (Navigation über die Datumsanzeige in der Kopfzeile)
- Keine globalen Plasma-Shortcuts zum Öffnen voreingestellt (`Alt+C` o. Ä. muss selbst in den Plasma-Tastatureinstellungen zugeordnet werden)

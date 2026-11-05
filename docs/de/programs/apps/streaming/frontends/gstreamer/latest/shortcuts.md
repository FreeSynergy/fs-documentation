# GStreamer - Tastatur-Shortcuts

## Übersicht

GStreamer ist ein Framework ohne eigenes Fenster — es gibt **keine globalen Shortcuts**. Tasten existieren nur in den mitgelieferten Werkzeugen (`gst-play-1.0`) und in Anwendungen, die auf GStreamer aufbauen.

## gst-play-1.0 (Wiedergabe im Terminal)

| Taste | Funktion |
|-------|----------|
| `SPACE` | Pause / Fortsetzen |
| `→` / `←` | 5 Sekunden vor/zurück |
| `PAGE UP` / `PAGE DOWN` | ein Kapitel bzw. größerer Sprung |
| `+` / `-` | Lautstärke erhöhen / senken |
| `M` | Stummschalten |
| `N` / `P` | nächster / vorheriger Titel |
| `S` | aktuellen Stand ausgeben |
| `Q` | Beenden |

## gst-launch-1.0

| Taste | Funktion |
|-------|----------|
| `Strg+C` | Pipeline stoppen (EOS wird gesendet) |
| `r` (neuere Versionen) | Pipeline neu starten, wenn gestartet mit `--repeat` |

## Eigene Anwendungen (Empfehlung für Skin-Umsetzung)

Diese Belegung ist **Vorschlag**, nicht GStreamer-Festlegung — sie folgt der Konvention anderer Media-Player:

| Shortcut | Funktion |
|----------|----------|
| `Space` | Play/Pause |
| `Strg+Shift+P` | Pipeline neu aufbauen (Source-Wechsel) |
| `Entf` | aktiven Sink-Zweig entfernen |
| `F5` | `PLAYING` erzwingen / Pipeline starten |
| `F6` | `PAUSED` setzen |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+C` | `Cmd+C` im Terminal | Abbrechen; im Terminal funktioniert `Strg+C` auf macOS ebenfalls |
| `Alt`-Kombinationen | `Option` | nur in GTK-/Qt-Oberflächen |

## Zusammenfassung

- Kurz: **GStreamer selbst hat keine Shortcuts**; `gst-play-1.0` bietet die übliche Transport-Steuerung im Terminal
- Alle Tasten in einer FreeSynergy-Oberfläche müssen selbst definiert und in dieser Datei dokumentiert werden
- Für Automatisierung sind Shortcuts irrelevant — dort zählen `GST_DEBUG`, Bus-Handler und `run-command`-Hooks

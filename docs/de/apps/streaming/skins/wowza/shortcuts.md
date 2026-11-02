# Wowza Streaming Engine - Tastatur-Shortcuts

## Übersicht

Der Wowza Streaming Engine Manager hat **keine dokumentierten Shortcuts**. Er folgt üblichen Web-Konventionen; Serversteuerung läuft über Dienstbefehle, Automatisierung über die REST API.

## Web-Manager (`http://host:8088`)

| Taste | Funktion |
|-------|----------|
| `Tab` / `Shift+Tab` | Formularfelder wechseln |
| `Enter` | Dialoge bestätigen (Restart, Properties speichern) |
| `Esc` | Bestätigungsdialoge abbrechen |
| `Strg+F` | Filtern in langen Application-/ Verbindungslisten |

## Dienst und Konsole

| Befehl | Funktion |
|--------|----------|
| `systemctl start wowza` / `stop` / `restart` | Engine als Dienst (Linux) |
| `<Install>/bin/WowzaStreamingEngine start` | Start ohne systemd |
| Windows: Dienste-Konsole → „Wowza Streaming Engine“ | Dienststeuerung Windows |
| `tail -f <Install>/logs/wowzastreamingengine_access.log` | Live-Log beobachten |

Die genaue Skript-/Unit-Bezeichnung ist **installationsabhängig** (Paket, Docker-Image).

## REST-Aufrufe als „Kurzbefehle“

| Aufgabe | Aufruf |
|---------|--------|
| Anwendungen auflisten | `curl -u user:pass http://localhost:8087/v2/instances` |
| Anwendung neu starten | `curl -u user:pass -X POST http://localhost:8087/v2/instances/_definst_/applications/myapp/restart` |
| Verbindungen zeigen | `curl -u user:pass http://localhost:8087/v2/connections` |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+F` | `Cmd+F` | Browser-Suche im Manager |
| `Esc` | `Esc` | Dialoge abbrechen |
| Dienstbefehle | — | Engine läuft nicht auf macOS; Manager ist plattformunabhängig erreichbar |

## Zusammenfassung

- Kurz: **keine Shortcuts** im Manager; Serversteuerung über Dienstbefehle, Automatisierung über REST v2
- Für eine FreeSynergy-Skin-Oberfläche gibt Wowza keine Tasten vor — eigene Hotkeys sind frei wählbar
- Wiederkehrende Abläufe (Application anlegen, Neustart, Restream-Ziele pflegen) gehören in Skripte gegen die REST API, nicht in Tastenkombinationen

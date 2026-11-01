# MediaMTX - Tastatur-Shortcuts

## Übersicht

MediaMTX läuft als Daemon ohne interaktive Konsole — es gibt **keine Tastatur-Shortcuts**. Bedient wird über Kommandozeile, Dienstverwaltung, YAML und HTTP-API.

## Kommandozeile

| Aufruf | Funktion |
|--------|----------|
| `mediamtx` | startet mit `mediamtx.yml` im aktuellen Verzeichnis |
| `mediamtx /pfad/zu/config.yml` | startet mit anderer Konfiguration |
| `mediamtx --version` | Versionsinformation |
| `Strg+C` (Foreground) | geordneter Shutdown (Hooks `runOnShutdown`) |

## Dienstverwaltung

| Befehl | Funktion |
|--------|----------|
| `systemctl start mediamtx` | starten |
| `systemctl restart mediamtx` | Konfigänderung wirksam machen |
| `journalctl -u mediamtx -f` | Log-Stream |
| `docker compose up -d` | Container-Start (Config als Volume) |

## API statt Shortcuts (Typische „Kurzbefehle")

| Aufgabe | Aufruf |
|---------|--------|
| Pfade anzeigen | `curl -s localhost:9997/v3/paths/list` |
| Verbindungen anzeigen | `curl -s localhost:9997/v3/connections/list` |
| dynamischen Pfad anlegen | `curl -X POST localhost:9997/v3/config/paths/add/mypath -d '{"source":"publisher"}'` |
| Metrics abfragen | `curl -s localhost:9998/metrics` |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `systemctl …` | `launchctl …` / brew services | MediaMTX hat kein eigenes UI |
| `Strg+C` | `Cmd+C` | `Strg+C` funktioniert im Terminal ebenfalls |

## Zusammenfassung

- Kurz: **keine Shortcuts** — MediaMTX wird über Datei, Ports und API gesteuert
- Für eine FreeSynergy-Skin-Oberfläche sind keine Tasten vorzugeben; relevant sind nur API-Aufrufe und Port-Liste
- Wer „Hotkeys" braucht, legt sie in der eigenen Oberfläche fest und dokumentiert sie dort

# Ant Media Server - Tastatur-Shortcuts

## Übersicht

Das Web-Panel des Ant Media Server hat **keine dokumentierten Shortcuts**. Es folgt üblichen Web-Konventionen. Bedienung läuft über Maus, Formulare und REST-Aufrufe.

## Kommandozeile und Dienst

| Befehl | Funktion |
|--------|----------|
| `antmedia-service start` | Server starten (Installation unter `/usr/local/antmedia`) |
| `antmedia-service stop` | stoppen |
| `antmedia-service restart` | Neustart (Settings werden neu geladen) |
| `antmedia-service status` | Prozessstatus |
| `systemctl start antmedia` | auf Systemen mit systemd-Unit |
| `tail -f logs/error.log` | Live-Log beobachten |

Die genaue Skript-/Unit-Bezeichnung ist **installationsabhängig** (Image, Paketmanager, Docker).

## Web-Panel (`http://host:5080`)

| Taste | Funktion |
|-------|----------|
| `Tab` / `Shift+Tab` | Formularfelder wechseln |
| `Enter` | Dialoge bestätigen, Suche auslösen |
| `Esc` | Modals (URL-Dialog, Token-Dialog) schließen |
| `Strg+F` | Filtern in langen Stream-/VoD-Listen |

## REST-Aufrufe als „Kurzbefehle"

| Aufgabe | Aufruf |
|---------|--------|
| Streams auflisten | `curl -s localhost:5080/live/rest/v2/broadcasts/list/0/10` |
| Stream stoppen | `curl -s -X POST localhost:5080/live/rest/v2/broadcasts/<id>/stop` |
| Serverinfo (Management-API) | `curl -s localhost:5080/rest/v2/…` (Details laut Swagger) |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+F` | `Cmd+F` | Browser-Suche |
| `Esc` | `Esc` | Modals schließen |
| `antmedia-service …` | — | Panel ist plattformunabhängig |

## Zusammenfassung

- Kurz: **keine Shortcuts** im Panel; Serversteuerung über Dienstbefehle, Automatisierung über REST v2
- Für eine FreeSynergy-Skin-Oberfläche gibt AMS keine Tasten vor — eigene Hotkeys sind frei wählbar
- Wiederkehrende Abläufe (Stream anlegen, Aufnahme starten) gehören in Skripte gegen die REST-API, nicht in Tastenkombinationen

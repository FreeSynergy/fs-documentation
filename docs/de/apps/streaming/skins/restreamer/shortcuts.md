# Restreamer - Tastatur-Shortcuts

## Übersicht

Die Webui des Restreamers hat **keine dokumentierten Shortcuts**. Sie folgt üblichen Web-Konventionen; Bedienung läuft über Formulare und Buttons. Automatisierung und Wartung passieren über die Kommandozeile im Container.

## Webui

| Taste | Funktion |
|-------|----------|
| `Tab` / `Shift+Tab` | Formularfelder wechseln |
| `Enter` | Formulare absenden |
| `Esc` | Sicherheitsabfragen/Dialoge abbrechen |
| `Strg+C` auf markierten URL-/Snippet-Feldern | Push-URL, Play-URL oder Einbettungscode kopieren |

## Container und CLI

| Befehl | Funktion |
|--------|----------|
| `docker restart restreamer` | Einstellungen neu anwenden |
| `docker exec -it restreamer sh` | Shell im Container öffnen |
| `docker exec restreamer /opt/restreamer/bin/restreamer-cli help` | CLI-Befehle anzeigen |
| `docker exec restreamer tail -f /opt/restreamer/var/log/nginx/access.log` | Zugriffe live beobachten |

Die genaue CLI-Syntax ist **versionabhängig** — maßgeblich ist `restreamer-cli help` im jeweiligen Image.

## RTMP-Gegenseite (OBS als Beispiel)

Der Restreamer selbst steuert man vom Encoder aus: In OBS genügt ein Ziel (`rtmp://host:1935/live/stream?key=<pushKey>`); OBS-eigene Hotkeys siehe [obs-studio/shortcuts.md](../obs-studio/shortcuts.md).

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+C` | `Cmd+C` | Snippet-Felder kopieren |
| `Esc` | `Esc` | Dialoge abbrechen |
| `docker …` | `docker …` | Befehle sind plattformunabhängig |

## Zusammenfassung

- Kurz: **keine Shortcuts** in der Webui; Steuerung über Formulare, Wartung über Docker/`restreamer-cli`
- Wiederkehrende Abläufe (Push-Key rotieren, Ziel-Listen pflegen) gehören in CLI-/Hook-Skripte, nicht in Tastenkombinationen
- Für eine FreeSynergy-Skin-Oberfläche gibt der Restreamer keine Tasten vor — eigene Hotkeys sind frei wählbar

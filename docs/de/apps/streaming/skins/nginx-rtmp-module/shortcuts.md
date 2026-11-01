# nginx-rtmp-module - Tastatur-Shortcuts

## Übersicht

Das Modul hat **keine Oberfläche und keine Shortcuts**. Bedient wird über die nginx-Kommandozeile und `nginx.conf`. Die Statusseite (`/stat`) ist eine normale HTML-/XML-Seite ohne eigene Tasten.

## nginx-Kommandozeile

| Befehl | Funktion |
|--------|----------|
| `nginx -t` | Konfiguration prüfen (Syntax und Pfade) |
| `nginx -s reload` | Konfiguration ohne Downtime neu laden |
| `nginx -s stop` | sofort beenden |
| `nginx -s quit` | geordnet beenden |
| `nginx -v` / `nginx -V` | Version / Build-Optionen (Modul sichtbar) |
| `nginx -c /pfad/nginx.conf` | andere Konfigurationsdatei verwenden |

## Dienstverwaltung

| Befehl | Funktion |
|--------|----------|
| `systemctl start nginx` | starten |
| `systemctl reload nginx` | Konfigänderung anwenden |
| `journalctl -u nginx -f` | Log-Stream (auch RTMP-Ereignisse) |

## Statusseite (`http://host/stat`)

| Taste | Funktion |
|-------|----------|
| `F5` / `Strg+R` | Status neu laden |
| `Strg+F` | Suchen in der Stream-Liste |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+R` | `Cmd+R` | Browser-Neuladen |
| `systemctl …` | `brew services restart nginx` | keine eigene UI |

## Zusammenfassung

- Kurz: **keine Shortcuts** — alles läuft über `nginx.conf`, `nginx -t` und `nginx -s reload`
- Für eine FreeSynergy-Skin-Oberfläche gibt das Original keine Tasten vor; eigene Hotkeys (z. B. „Konfiguration prüfen", „Reload") sind frei definierbar
- Automatisierung ersetzt Tastatur: Hooks (`on_publish`, `on_record_done`) und `exec`-Kommandos

# MistServer - Tastatur-Shortcuts

## Übersicht

MistServer ist ein Dienst mit Web-Oberfläche — es gibt **keine dokumentierten Shortcuts**. Die Oberfläche folgt den üblichen Browser-Tastaturgewohnheiten (Tab/Enter), eigene Tasten existieren nicht.

## Kommandozeile und Dienst

| Aufruf | Funktion |
|--------|----------|
| `MistServer` | startet Controller und konfigurierte Connector |
| `MistServer -h` | Hilfe zu den Start- und API-Parametern (Port über Parameter änderbar) |
| `systemctl start mistserver` | Dienst starten |
| `systemctl restart mistserver` | Änderungen anwenden |
| `journalctl -u mistserver -f` | Log-Stream |

## Browser-Oberfläche (`http://host:4242`)

| Taste | Funktion |
|-------|----------|
| `Tab` / `Shift+Tab` | Felder in Formularen wechseln |
| `Enter` | Formulare bestätigen |
| `Strg+R` | Oberfläche neu laden (Status aktualisieren) |
| Rechtsklick | Kontextmenü eines Streams (öffnen, löschen, anlegen) |

## API-Aufrufe als „Kurzbefehle"

| Aufgabe | Aufruf |
|---------|--------|
| Konfiguration lesen | `curl -s 'http://localhost:4242/api?command={"config":{}}'` |
| Aktive Streams | `curl -s 'http://localhost:4242/api?command={"active_streams":[]}'` |
| Statistik | `curl -s 'http://localhost:4242/api?command={"stats_streams":["clients"]}'` |
| Systemdaten | `curl -s 'http://localhost:4242/api?command={"capabilities":{}}'` |

## Mac-Varianten

| Windows/Linux | Mac | Hinweis |
|---------------|-----|---------|
| `Strg+R` | `Cmd+R` | Browser-Neuladen |
| `systemctl …` | `launchctl …` | MistServer läuft auf macOS als Prozess/Dienst |

## Zusammenfassung

- Kurz: **keine echten Shortcuts**; Interaktion läuft über Tabellen, Kontextmenüs und JSON-Kommandos
- Für eine FreeSynergy-Skin-Oberfläche sind keine Tasten des Originals vorzugeben — eigenes Tastenlayout ist frei definierbar und dann hier zu ergänzen
- Automatisierung ersetzt in der Praxis jede „Tastenkombination": Streams, Pushes und Protokolle werden per API gesetzt

# Homer - API Dokumentation

## Keine offizielle API

Homer ist eine **statische Seite ohne Backend**. Es existieren keine REST-, GraphQL- oder WebSocket-Schnittstelle, keine Authentifizierung, keine API-Schlüssel und keine Webhooks. Homer stellt ausschließlich Dateien bereit und wertet die Konfiguration im Browser aus.

**Was Homer ausliefert**

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/` | HTML-Grundseite (`index.html`) |
| `GET` | `/assets/config.yml` | Die komplette Dashboard-Beschreibung (lesbar für jeden, der die Seite erreicht) |
| `GET` | `/assets/<name>.yml` | Weitere Konfigurationen, ansprechbar über `?config=<name>.yml` (neuere Versionen) |
| `GET` | `/assets/icons/<datei>` | Eigene Symbole |
| `GET` | `/assets/<css-datei>` | Eigenes Stylesheet |
| `GET` | `/assets/js/…` | JavaScript der Single-Page-Anwendung |

> Das sind Dateiabrufe, keine API-Endpunkte. Es gibt keine Antwortformate, keine Statuscodes für Fachfehler und keine Versionierung.

## Authentifizierung

- **Keine.** Homer fragt keine Zugangsdaten ab und kennt keine Sitzungen.
- Schutz ausschließlich vorgelagert: Basic Auth im Webserver, Forward-Auth mit Authelia/Authentik, IP-Filter, VPN oder Netzwerksegmentierung.
- **Wichtig**: Auch `assets/config.yml` ist ohne diesen Schutz öffentlich. Die Datei enthält interne Hostnamen und Portnummern.

## Die Konfigurationsdatei als Schnittstelle

`assets/config.yml` ist der einzige Ort, an dem Homer „gesteuert“ wird. Sie wird beim Aufruf der Seite geladen, ist aber **nicht** Teil einer API: Es gibt kein Schreiben, keine Prüfung durch einen Server und keine Antwortmeldung.

### Laden und Varianten

| Mechanismus | Beschreibung |
|-------------|--------------|
| Standardpfad | `assets/config.yml` wird automatisch geladen |
| Query-Parameter | `https://home.example/?config=team.yml` lädt eine andere Datei (neuere Versionen) |
| Download-Knopf | `download-config` stellt die aktive Datei zum Herunterladen bereit |
| Volume im Container | Datei kann ohne Image-Neubau ausgetauscht werden |
| Vorlagen im Image | Das offizielle Image legt bei fehlender Konfiguration eine Vorlage an (Umschalter `INIT_ASSETS`, versionsabhängig); Platzhalter aus Umgebungsvariablen werden beim Start ersetzt (versionsabhängig) |

### Felder der Konfiguration

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `title` | Text | Überschrift der Seite |
| `subtitle` | Text | Zeile unter dem Titel |
| `document-title` | Text | Titel im Browser-Tab |
| `logo` | Pfad/URL | Bild links in der Kopfzeile |
| `icon` | Pfad | Favicon |
| `header` | Schalter | Kopfzeile ein-/ausblenden |
| `footer` | Text/HTML | Fußzeile |
| `links` | Liste | Icon-Links rechts oben (`name`, `icon`, `url`, `target`) |
| `columns` | Zahl/Text | Spaltenanzahl und Breitenverhalten (Details versionsabhängig) |
| `theme` | Text | helles oder dunkles Grundschema |
| `stylesheet` | Liste eigener Pfad | eigenes CSS |
| `search` | Schalter | Suchfeld an/aus |
| `message` | Objekt | Texte für Lade-, Fehler- und Offline-Zustand |
| `download-config` | Text/Schalter | Download der eigenen Konfiguration |
| `apps` | Liste | Gruppen mit `name`, `logo`, `class` und den darin enthaltenen `services` |

### Felder einer Kachel (`services`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `name` | Text | sichtbarer Name |
| `url` | URL | Ziel der Verknüpfung |
| `icon` | Text/Pfad | Symbol aus Icon-Set, eigene Datei oder URL |
| `target` | Text | `_blank`, `_self` usw. |
| `keywords` | Liste/Text | zusätzliche Suchwörter, Format versionsabhängig |
| `tag` | Text/Objekt | kleine Markierung an der Kachel (Farbdefinition versionsabhängig) |
| `type` | Text | Anzeige-Typ für erweiterte Kacheln (neuere Versionen) |

### Vollständiges Beispiel

```yaml
title: "Homelab"
subtitle: "Unsere Startseite"
document-title: "Homelab"
logo: "assets/logo.png"
icon: "assets/icons/favicon.png"
header: true
footer: "<p>Stand: heute</p>"
columns: "4"
theme: light
stylesheet:
  - "assets/styles.css"
search: true
message:
  offline: "Keine Verbindung"
  error: "Konfiguration konnte nicht geladen werden"
  loading: "Wird geladen …"
links:
  - name: "Git"
    icon: "fab fa-git-alt"
    url: "https://git.local"
    target: "_blank"
apps:
  - name: "Medien"
    logo: "assets/icons/media.png"
    class: "fa-solid fa-photo-film"
    services:
      - name: "Jellyfin"
        url: "https://jellyfin.local"
        icon: "sh-jellyfin"
        target: "_blank"
        keywords: "[film, serie]"
        tag: "aktiv"
      - name: "Radarr"
        url: "https://radarr.local"
        icon: "sh-radarr"
  - name: "Netzwerk"
    services:
      - name: "Router"
        url: "http://192.168.1.1"
        icon: "fas fa-network-wired"
```

## Beispiele mit curl

```bash
# Eingebaute Konfiguration ansehen (nur mit Proxy-Schutz sinnvoll)
curl -s https://home.example/assets/config.yml

# Alternative Konfiguration laden (Parameter wirkt in der Seite)
curl -s "https://home.example/?config=team-a.yml"

# Eigene CSS-Datei prüfen
curl -sI https://home.example/assets/styles.css
```

Erwartete Antwort: YAML-Text mit dem HTTP-Status `200`; fehlt die Datei, liefert der Webserver `404`. Eine strukturierte Fehlermeldung wie bei einer API gibt es nicht.

## Request/Response-Beispiele (erweiterte Anzeige-Typen)

Zeigt eine Kachel Werte aus einem fremden Endpunkt, ist dieser Endpunkt **fremde Infrastruktur** — Homer stellt nur die Anzeige bereit. Typischer Ablauf (versionsabhängig):

```bash
# Eigener Endpunkt, dessen Wert in einer Kachel erscheinen soll
curl -s https://grafana.local/api/health
```

```json
{
  "database": "ok",
  "version": "11.2.0"
}
```

In der Kachel wird per Konfiguration ein Pfad zu einem Feld angegeben; die genaue Feldbezeichnung ist der Dokumentation der eingesetzten Homer-Version zu entnehmen.

## Rate Limits

- **Nicht anwendbar**: Homer erzeugt keine Anfragen an einen eigenen Dienst.
- Begrenzung und Caching entstehen im Webserver oder CDN (Cache-Header für `assets/`, HTTP/2, Kompression).
- Bei erweiterten Anzeige-Typen gilt das Rate Limit des **fremden** Endpunkts; zu kurze Intervalle belasten dortige Systeme.

## Webhooks und internes Eventing

- **Nicht vorhanden.** Homer sendet keine Ereignisse und empfangen keine.
- Aktualisierung der Anzeige erfolgt durch Neuladen der Seite.
- Automatisierung läuft vollständig außerhalb: Git-Commit, Pipeline, Dateiaustausch, danach Neu laden.

## SDKs und Client-Bibliotheken

- **Nicht vorhanden.** Es gibt keine Bibliothek, um Homer zu steuern.
- Integrationswege sind Dateien und Deployment:
  - **Git-Repository** mit `config.yml` und Icons, Änderungen über Pull Requests
  - **CI/CD**, die Dateien in den Zielordner, ins Volume oder in einen Bucket kopiert
  - **Container-Volume**, das `assets/config.yml` austauscht, ohne das Image zu ändern
  - **Mehrere Dateien** (`?config=`), um Teams oder Geräte zu trennen

## Sicherheitshinweise

- `assets/config.yml` vor dem Zugriff aus dem Internet schützen oder bewusst als öffentlich betrachten.
- `download-config` nur aktivieren, wenn die Konfiguration geteilt werden darf.
- Keine Geheimnisse (API-Keys, Passwörter) in die Datei schreiben — sie ist lesbar.
- Geschützte Dienste weiterhin mit Single-Sign-On oder Proxy-Auth sichern; Homer ersetzt nichts davon.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)

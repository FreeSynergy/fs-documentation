# Homepage - Menüpunkte

## Übersicht

Homepage hat **kein Anwendungs-Menü**: Es gibt keine Menüleiste, keine Seitenleiste und keine Einstellungsdialoge. Die gesamte Oberfläche ist eine einzige, statisch gerenderte Seite; geändert wird in Konfigurationsdateien. Dieser Artikel beschreibt deshalb die **Bedien- und Konfigurationsbereiche** in der Reihenfolge, in der sie auf der Seite erscheinen, und kennzeichnet jeden Punkt als „nur lesbar“ oder „nur per Datei änderbar“.

> Wer ein Dashboard mit Menüs und Mauskonfiguration sucht, findet das in [../homarr/menu.md](../homarr/menu.md).

## Hauptmenüpunkte (Bedien- und Konfigurationsbereiche)

### 1. Kopfzeile (`header`)
- **Funktion**: Begrüßung, Uhrzeit/Datum, Suchleiste, Lesezeichenleiste
- **Details**:
  - Nur lesbar; Inhalt über `config/settings.yaml` (`header`, `language`, Zeitformat)
  - Lesezeichen aus `config/bookmarks.yaml` erscheinen als kleine Icons
  - Suchleiste nur sichtbar, wenn ein Such-Provider konfiguriert ist

### 2. Informations-Widgets oben (`widgets`)
- **Funktion**: Wetter, Auslastung, Aktien, Glances-Werte, Kubernetes-Status
- **Details**:
  - Nur lesbar; Reihenfolge und Position in `config/widgets.yaml`
  - Jeder Eintrag hat `type` und `position` (`left`/`right`)

### 3. Dienstgruppen (`services`)
- **Funktion**: Der eigentliche Inhalt: Gruppen mit Kacheln
- **Details**:
  - Nur per Datei: `config/services.yaml` definiert Gruppen, Icons, Links, Beschreibungen
  - Service-Widgets hängen als `_<dienst>` an der Kachel
  - Anordnung der Gruppen über `layout` in `settings.yaml`

### 4. Docker-/Kubernetes-Ansichten
- **Funktion**: Automatisch erzeugte Kacheln aus Containern oder Pods
- **Details**:
  - Provider in `config/settings.yaml` aktivieren
  - Container-Labels bzw. Annotations an der workload setzen
  - Feinschliff (Name, Icon, Gruppe) in `config/docker.yaml` / `config/kubernetes.yaml`

### 5. Fußzeile (`footer`)
- **Funktion**: eigener Text, Hinweis auf Version
- **Details**: Nur per Datei in `config/settings.yaml`

### 6. Design- und Theme-Bereich
- **Funktion**: Farbschema, Hintergrund, Deckkraft, Schrift
- **Details**:
  - `theme` (hell/dunkell/systemkompatibel), `color`, `background`, `image`, `opacity` in `settings.yaml`
  - Eigenes Design über `config/custom_css.css`
  - Browser-Umschaltung hell/dunkel wirkt nur, wenn `theme: system` gesetzt ist

### 7. Konfigurationsdateien (der „Einstellungsdialog“)
- **Funktion**: alle Einstellungen der Instanz
- **Details**:

| Datei | Bereich | Typische Schlüssel |
|-------|---------|--------------------|
| `settings.yaml` | globales Verhalten | `title`, `theme`, `color`, `layout`, `providers`, `launch`, `language` |
| `services.yaml` | Gruppen und Kacheln | `name`, `href`, `icon`, `description`, `_sonarr` |
| `widgets.yaml` | Info-Widgets | `type`, `position`, `properties` |
| `docker.yaml` | Container-Zuordnung | Dienstname → Container |
| `kubernetes.yaml` | Pod-Ansicht | Gruppierung, Namespaces |
| `bookmarks.yaml` | Lesezeichen | `name`, `icon`, `href` |
| `custom_css.css` / `custom_js.js` | Feinschliff | Selektoren, Browserlogik |

### 8. Serverseitige Bereiche (keine UI)
- **Funktion**: Proxy-Routen, Protokoll, Health-Check
- **Details**:
  - `/api/services/proxy`, `/api/widgets/...` (siehe [api.md](api.md))
  - Docker-/Container-Log für Konfigurations- und Verbindungsfehler
  - `/api/healthcheck` für Container-Healthchecks
  - **Hinweis**: Diese Endpunkte gehören nicht zur Bedienoberfläche und sind nicht als stabile API dokumentiert

## Kontext-Menüs

**Es gibt keine Kontext-Menüs.** Weder Rechtsklick auf eine Kachel noch Hover-Werkzeuge stehen zur Verfügung. Ersetzt durch:

| Erwartet | Stattdessen vorhanden |
|----------|----------------------|
| Rechtsklick → Kachel bearbeiten | Eintrag in `config/services.yaml` ändern, Seite neu laden |
| Hover → Aktionen (Stopp, Start) | nicht vorhanden – Homepage löst keine Aktionen aus |
| Drag & Drop der Kacheln | nicht vorhanden – Raster steht in `layout` |
| Dialog „Widget hinzufügen“ | `_<dienst>`-Schlüssel an der Kachel ergänzen |
| Icon-Auswahl per Galerie | `icon:`-Wert schreiben (SVG/PNG im Config-Ordner oder Icon-Set) |

## Menüs nach Benutzerrolle

Homepage unterscheidet **keine Rollen** in der Anwendung. Wirksam sind nur die Zugriffsstufen, die der Betrieb vorgibt:

### Besucher (Standard, ohne Anmeldung)
- Komplette Seite ansehen, Kacheln anklicken, Suchleiste benutzen
- Keine Bearbeitung, keine persönlichen Einstellungen
- **Wichtig**: Ohne Proxy-Schutz sieht jeder Besucher alle Daten und Icons – Homepage ist kein Zugangsschutz

### Besucher hinter Proxy-Authentifizierung
- Zugang nur nach Login beim Proxy (Basic Auth, OAuth-Proxy, Authentik, Tailscale)
- Danach identische Ansicht wie oben
- Feiner als „alles oder nichts“ wird nicht unterschieden

### Angemeldeter Nutzer (nur mit `HOMEPAGE_AUTH_ENABLED`)
- Sitzungsanmeldung der Anwendung, danach dieselbe Seite
- Dient dem Schutz der internen Proxy-Routen, nicht der Rechteverwaltung
- Es gibt weiterhin keine Rollen wie „Redakteur“ oder „Nur-Lesen“

### Administrator (Dateiebene)
- Zugriff auf `config/`, `.env` und das Container-Volume
- Darf YAML-Dateien, CSS/JS und Umgebungsvariablen ändern
- Entscheidet über Docker-Socket-Zugriff und MCP-Endpunkt (`HOMEPAGE_MCP_ENABLED`)
- **Empfehlung**: Config-Ordner in Git pflegen und Änderungen über Pull Requests freigeben

### Nur-Lesen-Arbeitsplatz
- Erreichen über einen zweiten virtuellen Host oder einen `/r/`-Pfad des Proxys mit Readonly-Weiterleitung auf denselben Container
- Rechtlich/technisch identisch, da Homepage keine Schreiboberfläche bietet

## Shortcuts

Tastatursteuerung existiert nur in Form von Browser- und Feldstandards; eine Aufstellung samt als fehlend markierter Tasten siehe [shortcuts.md](shortcuts.md).

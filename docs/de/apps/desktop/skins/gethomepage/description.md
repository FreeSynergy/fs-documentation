# gethomepage (Bibliothek) - Beschreibung

## Übersicht

Hinter jedem Live-Wert auf einem Homepage-Dashboard steckt dieselbe Code-Schicht: die **Service-Client-Bibliothek** von `gethomepage/homepage`. Sie übersetzt einen Konfigurationseintrag (`_sonarr: {}` an einer Kachel) in einen authentifizierten HTTP-Aufruf gegen die API des Zieldienstes, kürzt die Antwort und liefert JSON an die React-Komponente. Sie hat keinen Bildschirm, kein Menü und keine eigenen Einstellungen.

## Was die Bibliothek macht

Die Bibliothek besteht aus drei zusammenspielenden Teilen: **Deskriptoren** beschreiben je Dienst, welche API-Endpunkte es gibt und wie Antworten zu formen sind (`api`-Schablone, `mappings`, `validate`, `map`). **Handler** führen die Anfrage aus: ein generischer HTTP-Handler, ein Handler für Dienste mit Login-Schritt, ein JSON-RPC-Handler und Sonderfälle wie UniFi oder Synology. **Hilfsfunktionen** erledigen URL-Bau, Cookie-Ablage, Caching, Übersetzung der YAML-Konfiguration, Logging und die Prüfung, ob erwartete Felder in der Antwort vorhanden sind. Der Browser fragt nie den Zieldienst direkt, sondern immer die Route `/api/services/proxy` – Schlüssel und Session-Cookies bleiben damit im Prozess.

## Vorteile

- **Ein Muster für über 170 Dienste**: neuer Dienst = Deskriptor plus optional spezieller Handler
- **Secrets bleiben serverseitig**: API-Keys und Passwörter verlassen den Browser nicht
- **CORS-frei**: Der Browser spricht nur dieselbe Origin an
- **Endpunkt-Whitelist**: Nur in `mappings` hinterlegte Endpunkte sind aufrufbar, Pfade werden segmentweise escaped
- **Robustheit**: Antwortvalidierung, Fehler als JSON statt als Exception, Neustart-freundliches Logging
- **Caching und Bündelung**: identische Abfragen im Zeitfenster treffen den Zieldienst nur einmal
- **Testbarkeit**: zu jedem Modul existiert eine Testdatei (Vitest), Handler lassen sich ohne UI prüfen

## Abgrenzung zu anderen Systemen

### gethomepage-Bibliothek vs. Homepage-Dashboard
- **Dashboard** = Seiten, Raster, Themes; **Bibliothek** = Datenbeschaffung unter der Haube
- **Dashboard** konfigurierbar per YAML, **Bibliothek** erweiterbar nur im Quellcode
- Dokumentation des Dashboards: [../homepage/index.md](../homepage/index.md)

### gethomepage-Bibliothek vs. Homer
- **Homer** hat keine Clients: dort zeigen Kacheln nur statische Links, Live-Daten fehlen
- **gethomepage** bringt fertige Client-Module samt Authentifizierungsablauf mit
- **Homer** ist reine Statik, **gethomepage** braucht einen Node-Prozess für die Proxy-Schicht

### gethomepage-Bibliothek vs. Heimdall
- **Heimdall** integriert über PHP-App-Pakete auf dem eigenen Server, **gethomepage** über JS-Module im Node-Prozess
- **Heimdall** speichert Integrate-Keys in der Datenbank, **gethomepage** liest sie aus YAML/Umgebung
- **gethomepage** ist auf Abfragen (Read-Only) ausgerichtet, **Heimdall** ebenso, aber mit anderer Laufzeit

### gethomepage-Bibliothek vs. Dashy
- **Dashy** fragt Status-Endpunkte direkt aus dem Browser oder über einen kleinen Node-Server, **gethomepage** zentral über eine Proxy-Route
- **Dashy** bietet dafür eigene Widget-Syntax in `conf.yml`, **gethomepage** legt Endpunkte im Code fest
- **gethomepage** deckt deutlich mehr Fachdienste ab, **Dashy** mehr allgemeine HTTP-/Status-Checks

## Technische Details

- **Backend**: JavaScript (ESM) in Node.js, eingebettet in eine Next.js-Anwendung (pages router)
- **Database**: **keine** – Zustände sind Prozess-Caches (`memory-cache`) und Cookies im Arbeitsspeicher
- **Frontend-Anteil**: nur ein Hook (`useWidgetAPI`) für das Nachladen per SWR; Darstellung gehört zum Dashboard
- **Authentication**: pro Dienst unterschiedlich – API-Key in Query/Header, Session-Login mit Cookie-Ablage, Basic Auth, Token (Proxmox), Zertifikate für interne HTTPS-Dienste
- **Hosting**: läuft im selben Container wie das Dashboard (`ghcr.io/gethomepage/homepage`), alternativ als Quellbaum mit `pnpm dev`
- **Kein npm-Paket**: Die Module sind Teil des Repository und werden nicht als eigene Bibliothek veröffentlicht; Nutzung erfolgt durch Fork und Beitrag

## Für wen ist die Bibliothek geeignet?

- **Entwickler**, die einen neuen Dienst anbinden oder einen vorhandenen Deskriptor korrigieren wollen
- **Fortgeschrittene Nutzer**, die verstehen möchten, welche Anfrage ein Widget tatsächlich sendet (Log, Netzwerk-Reiter des Browsers)
- **Sicherheitsbewusste Betriebe**, die nachvollziehen wollen, warum Schlüssel den Browser nie erreichen
- **Weniger geeignet** als allgemeine Integrationsbibliothek für eigene Projekte: Sie ist auf die Konfigurationsform des Homepage-Dashboards zugeschnitten

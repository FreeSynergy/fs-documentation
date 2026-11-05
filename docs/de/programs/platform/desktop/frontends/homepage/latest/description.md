# Homepage - Beschreibung

## Übersicht

Homepage ist ein quelloffenes, **statisch gerendertes** Dashboard für selbst gehostete Umgebungen. Der Zustand des Dashboards liegt vollständig in YAML-Dateien im Ordner `config/`; es gibt keine Datenbank und keine Benutzerverwaltung. Über 170 mitgelieferte Widget-Module holen Live-Daten von Diensten wie Sonarr, Radarr, Pi-hole, Jellyfin, Proxmox, UniFi oder Tailscale.

## Was Homepage macht

Homepage baut aus Konfigurationsdateien eine einzelne Übersichtsseite: eine Kopfzeile mit Suchleiste und Informations-Widgets (Wetter, Systemauslastung, Aktien, Datum), darunter **Gruppen** von Diensten. Jeder Dienst ist eine Kachel mit Icon, Name, Beschreibung und optional einem **Service-Widget**, das Zahlen und Status des Dienstes anzeigt (z. B. laufende Downloads, offene Requests, Blockstatistik).

Die Anfragen an die Dienste laufen über interne Proxy-Routen des Containers (`/api/services/proxy`). Schlüssel bleiben damit auf dem Server, CORS-Probleme verschwinden. Docker- und Kubernetes-Umgebungen können Dienste automatisch liefern: Container-Labels bzw. Ingress-/Pod-Annotations erzeugen Kacheln ohne Handarbeit. Änderungen an den YAML-Dateien werden beim nächsten Seitenaufruf wirksam; eine Weboberfläche zum Bearbeiten existiert nicht.

## Vorteile

- **Konfiguration als Code**: Alles in `config/*.yaml`, versionierbar in Git, backbar durch Dateikopie
- **Kein Backend-Zustand**: keine Datenbank, keine Benutzer, keine Migrationen
- **Sehr viele Integrationen**: über 170 Widget-Module für Medien-, Netzwerk- und Infrastrukturdienste
- **Live-Daten ohne eigene API-Arbeit**: Proxy-Handler übernehmen Authentifizierung und JSON-Zuschnitt
- **Automatische Erkennung**: Docker-Labels und Kubernetes-Annotations erzeugen Kacheln
- **Leichtgewichtig**: ein Container, Port 3000, keine Workers, keine Queues
- **Anpassbar**: Themes, Hintergrundbilder, eigenes CSS/JS, benutzerdefinierte API-Widgets

## Abgrenzung zu anderen Systemen

### Homepage vs. Homer
- **Beide** sind statisch und YAML-konfiguriert; **Homer** bleibt bei Links und Icons
- **Homepage** hat Live-Widgets, Docker-/Kubernetes-Erkennung und einen Server-Proxy, **Homer** nicht
- **Homer** läuft als reine HTML-Auslieferung, **Homepage** braucht einen laufenden Next.js-Prozess

### Homepage vs. Dashy
- **Dashy** bietet Anmeldefunktionen, Rollen und ein umfangreiches Theme-System, **Homepage** verzichtet bewusst darauf
- **Dashy** konfiguriert `conf.yml` mit optionalem UI-Editor, **Homepage** nur Dateien
- **Homepage** hat deutlich mehr fertige Service-Integrationen, **Dashy** punktet bei Status-Checks und Widgets für Eigendaten

### Homepage vs. Homarr
- **Homarr** konfiguriert alles in der Weboberfläche und speichert in SQLite, **Homepage** speichert YAML-Dateien
- **Homarr** kann Aktionen auslösen (Container neu starten), **Homepage** zeigt überwiegend an
- **Homepage** ist ohne Login und Datenbank betreibbar, **Homarr** verlangt beides

## Technische Details

- **Backend**: Node.js mit Next.js (pages router); interne API-Routen unter `src/pages/api/`
- **Database**: **keine** – Zustand liegt ausschließlich in `config/*.yaml` und optional `.env`
- **Frontend**: React, Tailwind CSS, SWR für das Abfragen der Widget-Daten, `next-i18next` für Übersetzungen
- **Authentication**: standardmäßig **keine** (Schutz über Reverse Proxy, VPN oder Firewall); neuere Versionen bieten eine optionale, schlanke Sitzungsanmeldung über `HOMEPAGE_AUTH_ENABLED`
- **Hosting**: Docker/OCI-Image `ghcr.io/gethomepage/homepage` (Port 3000), Kubernetes, Bare-Metal mit Node.js; HTTPS und Host-Header-Prüfung über den Proxy

## Für wen ist Homepage geeignet?

- **Homelab-Nutzer**, die ihre Konfiguration in Dateien und Git pflegen wollen
- **Umgebungen mit vielen Diensten**, die Live-Zahlen (Medien-Stack, DNS-Filter, Virtualisierung) in einer Übersicht brauchen
- **Admins, die keinen zusätzlichen Login möchten** und den Zugang über Reverse Proxy, Tailscale oder VPN regeln
- **Weniger geeignet** für Teams mit individuellen Rechten, für Nutzer, die alles per Maus einstellen wollen, und für Umgebungen, in denen Aktionen (Neustart, Steuerung) aus dem Dashboard heraus nötig sind

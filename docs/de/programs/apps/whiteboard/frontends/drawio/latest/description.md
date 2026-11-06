# draw.io - Beschreibung

## Übersicht

draw.io (seit der Umbenennung auch diagrams.net) ist eine quelloffene Diagramm-Anwendung mit klassischer Menüleiste, Formbibliotheken und einem speicherbaren XML-Dateiformat. Sie läuft ohne Konto, offline und in jeder Cloud-Umgebung.

## Was draw.io macht

- Technische Diagramme: Flussdiagramme, Netzwerkpläne, UML, BPMN, ER-Diagramme, Mockups
- Riesige Formbibliotheken: General, Arrows, BPMN, UML, Flowchart, Network, AWS, Azure, GCP, Kubernetes, Cisco und weitere
- Dateien als `.drawio`/XML mit eingebetteter Grafik in PNG, SVG und PDF; Import/Export von VSDX
- Speichern auf Datenträger, im Browser, bei Google Drive, OneDrive, Dropbox, GitHub, GitLab oder Trello
- Echtzeit-Zusammenarbeit über „Realtime Sync“ auf Cloud-Dateien (versionsabhängig)
- Einbettung in fremde Anwendungen per iframe (postMessage-Protokoll) und eigene JS-Plugins

## Vorteile

- **Kostenlos und quelloffen**: Apache-2.0-lizenziert, Web-App und Desktop-Version gratis
- **Ohne Konto**: lokal starten, Daten bleiben in der eigenen Datei
- **Offenes Format**: XML-Diagramme sind lesbar, diff-bar und Git-tauglich
- **Formtiefe**: professionelle Bibliotheken inklusive Cloud-Anbieter-Icons
- **Einbettbar**: Referenz-Diagrammfunktion in Confluence, Jira und eigenen Apps
- **Offline**: Desktop-Version und Browser-Cache funktionieren ohne Netz

## Abgrenzung zu anderen Systemen

### draw.io vs. Excalidraw
- **draw.io** erzeugt exakte, normgerechte Diagramme mit Verbindungspunkten und Rastern
- **Excalidraw** skizziert bewusst im handgezeichneten Stil
- **draw.io** punktet mit Formbibliotheken und XML, **Excalidraw** mit Geschwindigkeit und Kollaborations-Verschlüsselung

### draw.io vs. Miro
- **Miro** ist kommerzielle Team-Plattform mit Vorlagen, Abstimmungen, Rechten und REST-API
- **draw.io** ist reines Zeichenwerkzeug ohne Moderations-Funktionen
- **Miro** speichert in der eigenen Cloud, **draw.io** in deiner Datei oder deinem Speicher

### draw.io vs. PlantUML
- **PlantUML** erzeugt Diagramme aus Textquellen (Code als Diagramm)
- **draw.io** bearbeitet Diagramme grafisch, XML entsteht als Nebenprodukt
- **PlantUML** ist versionskontroll-freundlicher, **draw.io** ist direkt manipulierbar

## Technische Details

- **Backend**: Die Web-App ist fast vollständig clientseitig; der eigene Server (Java/Jetty, Docker-Image `jgraph/drawio`) liefert nur statische Dateien und optionale Konfiguration
- **Database**: Keine eigene Datenbank; Dateien liegen beim Nutzer bzw. im angebundenen Cloud-Speicher
- **Frontend**: JavaScript/TypeScript auf Basis der mxGraph-Bibliothek (Eigenentwicklung von jgraph)
- **Authentication**: OAuth bei Cloud-Speichern (Google, Microsoft, Dropbox); die App selbst kennt keine Nutzerkonten
- **Hosting**: diagrams.net (offiziell), Self-Hosted per Docker/WAR, Desktop (Electron), Einbettung per iframe

## Für wen ist draw.io geeignet?

- **IT-Architekten und Netzwerkplaner**: Cloud-Icon-Sets, Referenzarchitekturen
- **Entwickler**: UML, Sequenz- und ER-Diagramme als Dateien im Repository
- **Dokumentationsteams**: Confluence/Jira-Integration, PNG/SVG aus CLI automatisierbar
- **Datenschützer**: Offline-Betrieb und Dateiablage ohne Anbieterbindung
- **Werkzeugbauer**: eigene Plugins und Einbettung in Produkt-Oberflächen

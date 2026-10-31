# Excalidraw - Beschreibung

## Übersicht

Excalidraw ist eine quelloffene Whiteboard-Anwendung (MIT-Lizenz) für skizzenhafte Diagramme, Mockups und Brainstorming. Sie startet ohne Konto, speichert lokal und ermöglicht Echtzeit-Kollaboration mit Ende-zu-Ende-Verschlüsselung.

## Was Excalidraw macht

- Skizzen im handgezeichneten Stil: Rechtecke, Ellipsen, Rauten, Pfeile, Linien, Freihandlinien, Text, Bilder und Frames
- Echtzeit-Kollaboration: gemeinsame Räume mit Cursor-Anzeige und geteilter Szene
- Dateien im offenen JSON-Format (`.excalidraw`) sowie Export als PNG, SVG und `.excalidraw.png`
- Wiederverwendbare Formensammlungen (`.excalidrawlib`) und eine öffentliche Bibliothek (libraries.excalidraw.com)
- Einbettung in eigene Anwendungen über das npm-Paket `@excalidraw/excalidraw` (React-Komponente)
- Umwandlung von Mermaid-Textdiagrammen in bearbeitbare Excalidraw-Elemente

## Vorteile

- **Kostenlos und Open Source**: MIT-lizenziert, vollständig selbst hostbar
- **Sofort startklar**: auf excalidraw.com ohne Registrierung loslegen
- **Handgezeichneter Look**: Rough.js-Optik senkt die Hürde für Entwürfe
- **Privatsphäre**: geteilte Räume sind Ende-zu-Ende-verschlüsselt (Schlüssel im URL-Fragment)
- **Einfaches Format**: `.excalidraw` ist lesbares, versionierbares JSON
- **Einbettbar**: Whiteboard-Funktionen direkt in eigene Web-Apps integrierbar
- **Schlank**: kurze Werkzeugleiste, minimale Einarbeitungszeit

## Abgrenzung zu anderen Systemen

### Excalidraw vs. draw.io
- **draw.io** auf exakte Technik-Diagramme mit großen Formbibliotheken und XML-Format
- **Excalidraw** auf schnelle Skizzen mit wenig Werkzeugen und großem Zeichenfluss
- **draw.io** bietet Cloud-Speicher (Drive, OneDrive), **Excalidraw** speichert primär lokal

### Excalidraw vs. Miro
- **Miro** ist eine kommerzielle Plattform mit Vorlagen, Abstimmungen, Rechteverwaltung und Admin-Konsolen
- **Excalidraw** ist ein schlankes Werkzeug ohne Verwaltungsfunktionen
- **Miro** hat eine dokumentierte REST-API, **Excalidraw** bewusst keine öffentliche API

### Excalidraw vs. tldraw
- **tldraw** versteht sich primär als Whiteboard-Bibliothek/SDK für eigene Apps
- **Excalidraw** liefert eine fertige App und bietet Einbettung zusätzlich an
- **Excalidraw** hat den markanten handgezeichneten Stil, **tldraw** zeichnet clean

## Technische Details

- **Backend**: Kein klassisches App-Backend; optionale Kollaborationsserver (Node.js, WebSocket), auf excalidraw.com zusätzlich Firebase für die Raumspeicherung (versionsabhängig)
- **Database**: Keine eigene Datenbank der Kern-App; Szenen liegen als JSON-Dateien bzw. in der Raum-Persistenz des Kollaborationsservers
- **Frontend**: React + TypeScript, Rendering auf HTML-Canvas mit Rough.js
- **Authentication**: Für die Community-Version keine; Konten existieren nur im kommerziellen Plus-Angebot (versionsabhängig)
- **Hosting**: Self-Hosted per Docker (App plus Kollaborationsserver) oder über excalidraw.com

## Für wen ist Excalidraw geeignet?

- **Produkt- und Design-Teams**: schnelle Wireframes, Userflows und Workshop-Ergebnisse
- **Entwickler**: Architektur- und Ablaufskizzen, direkt als Text-JSON versionierbar (Git-tauglich)
- **Lehrende und Lernende**: erklärungsbedürftige Konzepte ohne Zeichenfrust
- **Datenschkritische Umgebungen**: Selbsthost ohne Nutzerkonten, verschlüsselte Links
- **App-Entwickler**: Whiteboard-Funktionen als React-Komponente in eigene Produkte

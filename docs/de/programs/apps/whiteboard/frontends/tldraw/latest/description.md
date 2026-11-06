# tldraw - Beschreibung

## Übersicht

tldraw verbindet zwei Produkte: eine fertige Whiteboard-App (tldraw.com) und eine React-Bibliothek, mit der Entwickler eigene Zeichen- und Diagramm-Apps bauen. Beide teilen denselben Canvas, dasselbe Datenmodell und denselben Synchronisations-Layer.

## Was tldraw macht

- Freies Zeichnen auf unendlicher Fläche: Rechtecke, Ellipsen, Pfeile, Notizen, Text, Linien, Freihand, Bilder, Frames, Gruppen
- Werkzeuge mit Stilen: Farben, Füllarten, Linienstile, Größen, Schriftarten, Ausrichtung
- Dateien mit mehreren Seiten, automatischer lokaler Speicherung und Snapshot-Dateien (`.tldraw`)
- Mehrbenutzer-Betrieb: Shared Links, fremde Cursors, Folgen, Präsenz — mit eigenem Sync-Server oder gehosteter Sync-Cloud
- SDK für eigene Shapes, Werkzeuge, Panels und Ableitungen (custom bindings/derivations)
- Einbettbarer Read-only-Modus für die Anzeige fremder Produkte

## Vorteile

- **SDK zuerst**: Whiteboard-Funktionen als saubere TypeScript-Bausteine (`@tldraw/editor`, `@tldraw/tlschema`)
- **Modernes Datenmodell**: record-basiert, versioniert, migrierbar — ideal für Synchronisation
- **Synchronisation inklusive**: Sync-Pakete und Server sind Teil des Projekts
- **Lokal-first**: ohne Netz voll arbeitsfähig, Dateien bleiben beim Nutzer
- **Aktive Entwicklung**: gut dokumentierte Website tldraw.dev, häufige Releases
- **Kostenlos nutzbar**: App und Quellcode offen (neuere Lizenz-Konditionen versionsabhängig)

## Abgrenzung zu anderen Systemen

### tldraw vs. Excalidraw
- **tldraw** zeichnet clean und zielt als Bibliothek auf Produkt-Entwickler
- **Excalidraw** ist die fertige Skizzen-App im Hand-Stil
- **Excalidraw** verschlüsselt Kollaboration Ende-zu-Ende, **tldraw** nicht

### tldraw vs. draw.io
- **draw.io** ist Seiten- und Formbibliotheks-getriebenes Diagramm-Werkzeug mit Menüleiste
- **tldraw** ist freier Canvas ohne Formkatalog, dafür mit Multiplayer-Infrastruktur
- **draw.io** exportiert VSDX/XML, **tldraw** PNG/SVG/Snapshots

### tldraw vs. Miro
- **Miro** ist kommerzielle Plattform mit Vorlagen, Rechten, REST-API und Admin-Konsolen
- **tldraw** liefert den Rohbau: App plus SDK, aber keine Verwaltung
- **Miro** hostet alles, **tldraw** betreibst du selbst (oder nutzt die angebotene Sync-Cloud)

## Technische Details

- **Backend**: Die App ist lokal-first ohne eigenes Backend; Mehrbenutzer-Betrieb über `@tldraw/sync`-Client mit TLSync-Server (Node.js, Redis) oder der gehosteten tldraw-sync-Cloud (versionsabhängig)
- **Database**: Kein Server-Standard-DB-Zwang; lokal IndexedDB, serverseitig je nach Sync-Aufbau (Redis bei tlsync)
- **Frontend**: React + TypeScript, eigener Canvas-Renderer, Atom-artiger State-Layer
- **Authentication**: Keine in Kern und App; beim Selbsthost-Betrieb bringst du Login und Raum-Rechte mit
- **Hosting**: Statische Web-App (Vite/Next), TLSync-Server oder Managed-Cloud; Starter: `npm create tldraw@latest`

## Für wen ist tldraw geeignet?

- **Produkt-Teams**, die ein Whiteboard in die eigene SaaS einbauen wollen
- **Workshop-Moderatoren**, die schnell teilen und zusammen zeichnen wollen
- **Prototyp-Bauer**: eigene Shape-Typen und Werkzeuge in Stunden machbar
- **Open-Source-Communitys**, die ein wartbares Canvas-Fundament suchen

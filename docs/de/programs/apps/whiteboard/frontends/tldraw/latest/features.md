# tldraw - Funktionen

## Übersicht

tldraw kombiniert eine schlanke Whiteboard-App mit einem Entwickler-SDK. Funktionen gruppieren sich in Werkzeuge/Shapes, das Record-Datenmodell, Dateien und Seiten, Multiplayer-Synchronisation und die SDK-Erweiterbarkeit.

---

## 1. Werkzeuge und Shapes

- **Auswahl-Werkzeug** (`V`): auswählen, verschieben, skalieren, Multi-Select
- **Hand-Werkzeug** (`H`): Canvas bewegen
- **Stift** (`D`): Freihandlinien mit Druck-Optik
- **Radierer** (`E`): Formen wegradieren
- **Pfeil** (`A`): verbindungsfähige Pfeile mit Endpunkten und Beschriftung
- **Rechteck** (`R`) und **Ellipse** (`O`): Basic-Geometrien mit Füll- und Linienstilen
- **Notiz** (`N`): klebrige Post-its in mehreren Farben
- **Text** (`T`) und **Linie** (`L`)
- **Frame** (`F`): begrenzende Fläche für Gruppierung und Export-Zuschnitte
- **Bild/Bookmark**: Medien per Drag & Drop oder URL
- **Laser-Pointer**: zeitlich begrenzter Zeigestrahl (über Werkzeugleiste)

### Stile

- Farbe, Füllung (solid/semi/schraffiert je nach Version), Linienstil (gestrichelt/gepunktet)
- Drei bis vier Größenstufen, mehrere Schriftfamilien, Beschriftungsfarben
- Ausrichten, Verteilen, Ebenen (nach vorne/hinten), Gruppieren, Sperren

## 2. Objektmodell (Records)

- Der gesamte Dokumentzustand besteht aus **Records** in einem versionierten Store
- Shape-Records tragen `type` (`rect`, `ellipse`, `arrow`, `draw`, `note`, `text`, `line`, `image`, `frame`, `group`, `bookmark`, `embed`) und `props` (Position, Größe, Stil, Beschriftung)
- **Bindings** verbinden Pfeile dauerhaft mit Shapes (Follow beim Verschieben)
- **Groupen** und **Frames** strukturieren die Fläche; `parentId`-Hierarchie wie bei Szenengraphen
- Neben Shapes existieren systemeigene Records: `document`, `page`, `camera`, `pointer`, `user`, `styles`, `instance`
- Das Schema (`@tldraw/tlschema`) ist versioniert und migriert alte Dateien automatisch

## 3. Dateien und Seiten

- **Mehrere Seiten** pro Datei, verwaltet über das Seiten-Menü
- **Lokale Automatispeicherung** in IndexedDB (sitzungsgebunden über `persistenceKey`)
- **Export/Import**: PNG, SVG und Snapshot-Datei (`.tldraw`) über das Hauptmenü
- **Auswahl-Export**: nur markierte Formen als Bild
- PDF-Export existiert nicht (PDF-Workflow: SVG exportieren und konvertieren)

## 4. Multiplayer und Echtzeit-Synchronisation

- **Share-Dialog**: Gemeinsamen Link erzeugen; wer den Link öffnet, zeichnet mit
- Präsenz: farbige Cursors, Namenschilder, „Folgen“ anderer Teilnehmender
- Synchronisation erfolgt **record-basiert**: Änderungen an Shapes werden als Datensatz-Deltas ausgetauscht, Konfliktlösung übernimmt der Sync-Layer (historienbehafteter Store, kein klassisches Last-write-wins)
- Betrieb wahlweise über **TLSync-Serverselbsthost** (Node.js + Redis) oder die **gehostete tldraw-sync-Cloud** (versions-/plänabhängig)

## 5. SDK (tldraw als Bibliothek)

- `<Tldraw />`-Komponente mit voller Ausstattung: Werkzeuge, Panels, Menüs (abschaltbar)
- **Editor-API**: Dokument lesen/schreiben, Kamera steuern, Export (`getSnapshot`, `loadSnapshot`, `exportToSvg`, `zoomToFit`)
- **Eigene Shapes/Werkzeuge/Bindings**: Klassen-basierte Erweiterungen mit eigenem Schema
- **Custom UI**: eigene Panels, Menüs und Overlays im Design des Produkts
- **Read-only-Modus** (`readonly`): Canvas anzeigen ohne Bearbeiten

---

## Konfiguration

- **Komponenten-Props**: `persistenceKey`, `initialState`, `snapshot`, `options` (Menüpunkte und Panels einzeln ausblenden), `readonly`
- **Sync-Anbindung**: Client-Paket `@tldraw/sync` mit Server-URL, Raumnamen und Nutzerinfo
- **UI-Anpassung**: Theme hell/dunkel/system, Tastaturkürzel-Aktivierung, Canvas-Hintergrund

---

## Was tldraw NICHT kann

- **Keine öffentliche REST-API und keine Webhooks** (siehe [api.md](api.md))
- **Keine Kommentare** — Kommunikation nur über Cursors und Präsenz
- **Keine feingranulare Rechteverwaltung im Standard-Setup** — Link heißt meist bearbeiten
- **Kein Vorlagen-Katalog** wie bei Miro — eigene Start-Snapshots ersetzen das
- **Kein PDF-Export**, keine VSDX-/XML-Kompatibilität
- **Keine Administration**: keine Nutzerlisten, Audit-Logs oder SSO von Haus aus
- **Keine native Mobile-App** — Web-App mit Touch-Gesten

---

## Module und Integrationen

- **`tldraw`** (npm): Komplettpaket für React-Apps
- **`@tldraw/editor`, `@tldraw/tlschema`**: Low-Level-Schichten für eigene Bauten
- **`@tldraw/sync`**: Client für die Synchronisation; **TLSync** als Referenz-Server (Redis)
- **Beispiel-Apps** auf tldraw.dev: Custom-Shapes, Kollaboration, Chat-Overlays,_whiteboard-Produkte

## Erweiterungen und Plugins

- **Kein Plugin-Marktplatz** — Erweiterungen sind SDK-Code
- **Ableitungen (derivations)**: abgeleitete Formen automatisch aus anderen Records erzeugen
- **Community-Beispiele**: Diagramme aus Markdown, Timer-Panels, Abstimmungs-Overlays (Selbstbau, Qualität prüfen)

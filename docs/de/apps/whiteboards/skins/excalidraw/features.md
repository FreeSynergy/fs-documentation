# Excalidraw - Funktionen

## Übersicht

Excalidraw besteht im Kern aus Canvas, Werkzeugleiste und Eigenschaften-Panel. Die Funktionen gliedern sich in fünf Bereiche: Zeichenwerkzeuge, Objektmodell, Echtzeit-Kollaboration, Dateien/Bibliotheken und Einbettung in eigene Anwendungen.

---

## 1. Zeichenwerkzeuge

- **Auswahl-Werkzeug** (`V`): Elemente auswählen, verschieben, skalieren; `Shift`+Klick für Mehrfachauswahl
- **Hand-Werkzeug** (`H`): Canvas bewegen, ohne Elemente auszuwählen
- **Radierer** (`E`): Elemente durch Ziehen entfernen; beim Zurückziehen bleiben sie erhalten
- **Formen**: Rechteck (`R`), Ellipse (`O`), Raute (`D`)
- **Linien und Pfeile** (`L`, `A`): Pfeile lassen sich an Formen andocken und folgen beim Verschieben
- **Freihand zeichnen** (`P`): Stiftstriche, auch mit Grafiktablett oder Touch-Stift
- **Text** (`X`): eigene Textfelder oder Beschriftungen, an Formen gebunden
- **Bilder**: aus Datei, Ablage (Clipboard) oder per Drag & Drop einfügen
- **Frames**: begrenzende Flächen wie Seiten; Inhalte können an Frames andocken
- **Werkzeug-Sperre** (`Q`): gewähltes Werkzeug bleibt nach dem Zeichnen aktiv

### Modifikatoren beim Zeichnen

- **`Shift`**: Winkel bei Linien/Pfeilen auf 15°-Schritte festlegen, proportional skalieren
- **`Alt`+Ziehen**: Element klonen statt verschieben
- **Doppelklick** auf eine Form: eingebundene Beschriftung bearbeiten
- **Pfeiltasten**: markierte Elemente pixelweise verschieben

---

## 2. Objektmodell (Elemente)

- Eine Szene ist ein geordnetes Array von Elementen mit Typen wie `rectangle`, `ellipse`, `diamond`, `arrow`, `line`, `freedraw`, `text`, `image`, `frame`, `embeddable`
- Gemeinsame Eigenschaften: `x`, `y`, `width`, `height`, `angle`, `strokeColor`, `backgroundColor`, `fillStyle` (hachure/solid), `strokeWidth`, `strokeStyle` (solid/dashed/dotted), `roughness`, `opacity`
- Gruppierung über `groupIds`, Frames über `frameId`, Textbindung über `boundElements`
- Pfeile speichern Bezugspunkte auf andere Elemente und folgen beim Verschieben
- Synchronisationsfelder: `seed`, `version`, `versionNonce` — Änderungen werden elementweise ausgetauscht, pro Element gewinnt die höchste Version (Last-write-wins, kein vollwertiger CRDT)
- Löschungen markieren Elemente mit `isDeleted`, statt sie sofort aus der Szene zu entfernen

### Szenen-Datei (Ausschnitt)

```json
{
  "type": "excalidraw",
  "version": 2,
  "elements": [ { "type": "rectangle", "x": 10, "y": 10, "strokeColor": "#1e1e1e" } ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

---

## 3. Echtzeit-Kollaboration

- Start über das Live-Kollaboration-Menü; der Raum-Link wird mit Rechten zum Bearbeiten oder Ansehen kopiert
- Alle Teilnehmenden sehen Cursors, Auswahl und (optional) Namen der anderen
- Ende-zu-Ende-Verschlüsselung: Der Server leitet nur verschlüsselte Nachrichten weiter, der Schlüssel steht im URL-Fragment (`#`)
- Cursor anderer Teilnehmender lassen sich verfolgen ("Follow")
- Integrierter **Laserpointer** zum Zeigen, ohne Spuren auf der Zeichenfläche zu hinterlassen

### Synchronisation

Die Kollaboration überträgt Differenzen auf Element-Ebene über WebSocket-Nachrichten. Bei Gleichstand entscheidet die `versionNonce`. Details in [api.md](api.md).

---

## 4. Dateien, Export und Bibliotheken

- **Speichern**: `.excalidraw` (JSON mit Szene und AppState); in unterstützten Browsern direkt `.excalidraw.png` mit eingebetteter Szene
- **Export**: PNG und SVG, optional nur die Auswahl; Kopie als PNG/SVG in die Zwischenablage
- **Bibliotheken**: eigene Formensammlungen als `.excalidrawlib`, laden und speichern über das Bibliotheks-Panel; öffentliche Bibliothek unter libraries.excalidraw.com
- **Mermaid**: Mermaid-Text in bearbeitbare Excalidraw-Elemente umwandeln (Plus-Menü)

---

## 5. Einbettung in eigene Anwendungen

- npm-Paket `@excalidraw/excalidraw` liefert eine React-Komponente inklusive Werkzeugleiste
- Props wie `initialData`, `onChange`, `viewModeEnabled`, `theme` und `langCode` steuern Verhalten und Aussehen
- **View mode** (`viewModeEnabled`): schreibgeschützter Canvas mit Zoom und Verschieben
- Callbacks wie `onPointerUpdate` und `onLinkOpen` ermöglichen eigene Integrationen

---

## Konfiguration

- **Eigene Instanz**: Umgebungsvariablen wie `VITE_APP_WS_SERVER_URL` (Kollaborationsserver) und `VITE_APP_FIREBASE_CONFIG` (Raum-Persistenz); Namen und Umfang sind versionsabhängig
- **Oberfläche**: Theme (hell/dunkel), Sprache, Gitter (`Ctrl+'`), Zen-Modus (`?`)
- **Sitzung**: Letzter Canvas bleibt im Browser erhalten (localStorage); Räume sind optional beständig

---

## Was Excalidraw NICHT kann

- **Kein PDF-Export** — nur PNG, SVG und das native JSON-Format
- **Keine Kommentare und kein Chat** — Kommunikation läuft außerhalb der App
- **Keine feingranulare Rechteverwaltung** — nur Link „kann bearbeiten“ oder „kann ansehen“
- **Keine Versionshistorie von Dateien** — nur Undo/Redo innerhalb der Sitzung
- **Keine Präsentations-, Abstimmungs- oder Agenda-Funktionen** (das bietet z. B. Miro)
- **Keine öffentliche REST-API und keine Webhooks** (siehe [api.md](api.md))
- **Kein Aufgaben- oder Kanban-Board** — es bleibt eine freie Zeichenfläche

---

## Erweiterungen und Plugins

- **Kein offizieller Plugin-Marktplatz** — Erweiterbarkeit über Bibliotheken, Einbettung und Abspaltungen
- **Obsidian-Plugin „Excalidraw“** (Community): Whiteboards direkt in der Notiz-App
- **VS-Code-Erweiterung** (Community): `.excalidraw`-Dateien im Editor öffnen und bearbeiten
- **excalidraw-room** und der neue Collab-Server: quelloffene WebSocket-Server für Self-Hosted-Instanzen
- **Beispiel-Apps** im Projekt-Repository („Kitchen Sink“) zeigen alle Einbettungsvarianten

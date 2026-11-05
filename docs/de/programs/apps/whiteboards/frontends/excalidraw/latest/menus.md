# Excalidraw - Menüpunkte

## Übersicht

Excalidraw hat kein klassisches Anwendungsmenü, sondern eine schmale Kopfzeile, eine Werkzeugleiste, ein Plus-Menü zum Einfügen und ein Eigenschaften-Panel für die Auswahl. Rechtsklicks öffnen kontextabhängige Menüs. Die Verfügbarkeit einzelner Punkte hängt von der Version und davon ab, ob die Community-Version oder das Plus-Angebot genutzt wird.

## Hauptmenüpunkte

### 1. Hauptmenü (Hamburger-Symbol, oben links)
- **Funktion**: Datei- und Grundeinstellungen
- **Details**:
  - Neue Zeichenfläche
  - Öffnen (Datei vom Datenträger)
  - Speichern (als `.excalidraw`)
  - Bild exportieren (PNG, SVG, Auswahl)
  - Zeichenfläche leeren
  - Theme (hell/dunkel) und Sprache
  - Hilfe und Kurzbefehle
  - Eigene Dateien bzw. Plus-Konto (nur im Plus-Angebot, versionsabhängig)

### 2. Werkzeugleiste
- **Funktion**: Wahl des Zeichenwerkzeugs
- **Details**:
  - Auswahl, Hand, Radierer
  - Rechteck, Raute, Ellipse
  - Pfeil, Linie, Freihand
  - Text, Bild
  - Frame und Werkzeug-Sperre (`Q`)
  - Rückgängig/Wiederholen und Zoom-Stufe (je nach Version in der Kopf- oder Werkzeugleiste)

### 3. Live-Kollaboration (Kollaborations-Symbol)
- **Funktion**: Gemeinsame Räume starten und teilen
- **Details**:
  - „Live-Kollaboration starten“
  - Link zum Bearbeiten kopieren
  - Link zum Ansehen kopieren
  - Kollaboration stoppen
  - Teilnehmendenliste und „Cursor folgen“

### 4. Plus-Menü („Elemente hinzufügen“)
- **Funktion**: Erweiterte Inhalte einfügen
- **Details**:
  - Bibliothek durchsuchen
  - Bild einfügen
  - Mermaid-Diagramm einfügen
  - Einbettung/Frame-Objekte (versionsabhängig)

### 5. Eigenschaften-Panel (links, nur bei Auswahl)
- **Funktion**: Ausgewählte Elemente gestalten
- **Details**:
  - Linienfarbe, Hintergrundfarbe, Füllmuster
  - Linienstärke und Linienstil (durchgehend, gestrichelt, gepunktet)
  - Rauheit (Sketch-Grad) und Deckkraft
  - Schriftfamilie und Schriftgröße, Textausrichtung
  - Ebene nach vorne/hinten, Duplizieren, Löschen, Sperren
  - Link zu Element hinzufügen

### 6. Bibliotheks-Panel (rechts)
- **Funktion**: Formensammlungen verwalten
- **Details**:
  - Eigene Bibliotheken erstellen und speichern (`.excalidrawlib`)
  - Öffentliche Bibliotheken laden
  - Auswahl aktueller Elemente zur Bibliothek hinzufügen

## Kontext-Menüs (Rechtsklick)

### Auf Elementen
- Nach vorne / nach hinten, nach vorne holen / nach hinten schicken
- Duplizieren, Kopieren, Einfügen, Ausschneiden
- Gruppieren / Gruppierung aufheben
- Löschen
- Sperren / Entsperren (versionsabhängig)
- Link hinzufügen, zur Bibliothek hinzufügen
- Ausrichten und Verteilen (bei Mehrfachauswahl)
- Horizontal/vertikal spiegeln

### Auf dem Canvas (leere Fläche)
- Alles auswählen
- Einfügen
- Alle Objekte nach vorne/hinten

### Auf Text
- Schriftart und Größe (bei aktiver Auswahl)
- Zeilenumbrüche und Ausrichtung

## Menüs nach Benutzerrolle

### Betreiber einer Instanz (Admin)
- Konfiguration der Instanz über Umgebungsvariablen (Kollaborationsserver, Persistenz)
- Entscheidungen über Plus-Konten und Dateispeicher
- Kein Admin-Menü in der Oberfläche selbst — Verwaltung ist rein Dateibasierend

### Bearbeiter (Bearbeitungs-Link)
- Alle Werkzeuge, Eigenschaften-Panel, Kollaboration, Speichern und Export
- Undo/Redo, Gruppieren, Frames, Bibliotheken

### Leser (Ansehen-Link bzw. View-Modus)
- Nur Zoomen und Verschieben (Hand-Werkzeug, Scrollen)
- Keine Werkzeuge, kein Eigenschaften-Panel, kein Speichern der Szene
- Eigener Name für Cursor-Anzeige optional setzbar

## Hinweise

- Die exakte Beschriftung und Anordnung der Punkte ändert sich mit den Versionen; diese Liste beschreibt die Community-Oberfläche als Standardfall
- Shortcuts zu den Menüpunkten stehen in [shortcuts.md](shortcuts.md)

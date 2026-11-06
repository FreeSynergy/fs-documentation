# draw.io - Menüpunkte

## Übersicht

draw.io besitzt die klassischste Menüleiste aller Whiteboard-Werkzeuge: **Datei, Bearbeiten, Ansicht, Anordnen, Extras, Hilfe**. Dazu kommen die Formbibliothek links, das Formatierungs-Panel rechts und kontextabhängige Rechtsklick-Menüs. Die Bezeichnungen folgen der deutschen Oberfläche; einzelne Punkte existieren je nach Version (Web, Desktop, Einbettung) unterschiedlich.

## Hauptmenüpunkte

### 1. Datei
- **Funktion**: Neue Diagramme, Öffnen, Speichern, Exportieren
- **Details**:
  - Neu, Öffnen aus (Gerät, URL, diesem Browser, Google Drive, OneDrive, Dropbox, GitHub, GitLab, Trello)
  - Zuletzt geöffnete Dateien
  - Diagramm bearbeiten (XML-Editor)
  - Speichern nach (Gerät, Google Drive, OneDrive, Dropbox, ...)
  - Exportieren als (PNG, JPEG, SVG, PDF, HTML, XML, VSDX)
  - Versionen (Historie des Cloud-Speichers)
  - Dokument-Eigenschaften, Drucken, PDF, Schließen

### 2. Bearbeiten
- **Funktion**: Zwischenablage, Zellen-Operationen, Text und Daten
- **Details**:
  - Rückgängig, Wiederholen
  - Ausschneiden, Kopieren, Einfügen, Duplizieren, Duplizieren und verschieben (Clone)
  - Löschen, Alle auswählen
  - Stil bearbeiten, Link einfügen/bearbeiten, Daten bearbeiten, Kurzinfo bearbeiten
  - Formen suchen, Sperren/Entsperren
  - Gruppieren/Aufheben, Reihenfolge (nach vorne/hinten)

### 3. Ansicht
- **Funktion**: Darstellung der Leinwand und Panels
- **Details**:
  - Outline (Übersicht), Such- und Formfelder ein-/ausblenden
  - Raster, Rasterfarbe, Werkzeugtipps, Griffe, Verbindungen, Seitenansicht
  - Bildlaufleisten, Maßstäbe (versionsabhängig)
  - Ebenen-Dialog
  - Theme hell/dunkel (versionsabhängig), Aktuell verkleinern/vergrößern (Zoom)

### 4. Anordnen
- **Funktion**: Layout, Reihenfolge, Ausrichtung
- **Details**:
  - Layout-Anwendungen: Baum, Organisch, Kreis, Kompakt, Fluss, Horizontaler/Vertikaler Fluss, Fächer, Radial, Konzentrisch u. a.
  - Gruppe betreten/verlassen
  - Einfügen (Bild, Kurve, Formvorlagen)
  - Reihenfolge, Ausrichten, Verteilen, Drehen, Spiegel
  - Weitere Aktionen (zellabhängig)

### 5. Extras
- **Funktion**: Seiten, Links, Stile, Kollaboration, Sprache
- **Details**:
  - Realtime-Sync (Echtzeit-Kollaboration an Cloud-Dateien, versionsabhängig)
  - Seiten: einfügen, duplizieren, umbenennen, Hintergrund, löschen
  - Links: Link bearbeiten, Link öffnen, Kurzinfo bearbeiten
  - Stil bearbeiten, Farben, Ansichten zurücksetzen
  - To-dos (Aufgaben-Marker im Diagramm)
  - Aktuelle Sprache, Umblatten/Seiten neu brechen (versionsabhängig)

### 6. Hilfe
- **Funktion**: Dokumentation und Tastenkürzel
- **Details**:
  - Kurzreferenz der Tastenkombinationen
  - Verweise auf diagrams.net-Dokumentation
  - Info/Über-Dialog der Desktop-Version

## Seitenleiste (links)

- **Suchfeld**: findet Formen über alle aktiven Bibliotheken
- **Formbibliotheken**: aufklappbare Ordner (General, Arrows, BPMN, UML, AWS, Azure, ...)
- **Weitere Formen**: zusätzliche Bibliotheken aktivieren
- **Meine Formen**: eigene SVG-Formen ablegen

## Formatierungs-Panel (rechts)

- **Optionen**: Dokument-Einstellungen (Raster, Hintergrund, Auto-Save)
- **Stil**: Füllung, Linie, Schrift, Kantenausführung
- **Anordnen**: Position, Größe, Drehung, Textausrichtung, Daten

## Kontext-Menüs (Rechtsklick)

### Auf Formen
- Link bearbeiten, Stil bearbeiten, Reihenfolge, Ausrichten/Verteilen
- Gruppieren/Aufheben, Duplizieren, Löschen
- Ersetzen (Form austauschen), In Gruppe einfügen

### Auf Kanten
- Wegpunkte bearbeiten, Richtung/Pfeilspitzen, Stil, Löschen

### Auf Seitenreiter (unten)
- Seite einfügen, duplizieren, umbenennen, Hintergrundfarbe, löschen

### Auf leerer Leinwand
- Einfügen, hier einfügen, Alles auswählen, Raster/Ansicht-Verknüpfungen

## Menüs nach Benutzerrolle

### Betreiber / Self-Hosted-Admin
- Configure-Bildschirm der Instanz (Storage-Keys, erlaubte Dienste)
- `configure.js`/Zusatzkonfiguration, Theme-Vorgaben, Plugin-Auswahl
- Die Desktop-Version: Berechtigungen fürs Dateisystem über das Betriebssystem

### Bearbeiter
- Volle Menüleiste, alle Werkzeuge, Speichern und Export
- Realtime-Sync starten/verlassen, Seiten verwalten

### Leser
- draw.io unterscheidet **keine App-Rollen**: „Nur lesen“ entsteht durch
  - Öffnen einer Datei ohne Schreibrecht im Cloud-Speicher
  - Eingebettete Ansicht ohne Speicher-Buttons (`chrome=0`, `noSaveBtn`, versionsabhängig)
- In diesen Modi bleiben Ansicht, Zoom und Export benutzbar, Speichern entfällt

## Hinweise

- Web-, Desktop- und eingebettete Version zeigen unterschiedliche Anteile der Menüs (z. B. entfällt „Öffnen aus Cloud“ offline)
- Shortcuts zu allen Punkten: [shortcuts.md](shortcuts.md)

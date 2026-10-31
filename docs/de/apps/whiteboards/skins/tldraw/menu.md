# tldraw - Menüpunkte

## Übersicht

tldraw hat bewusst wenige Menüs: linkes Hauptmenü (Datei), Werkzeugleiste unten, Stil-Panel rechts und ein Seiten-/Share-Menü. Alles Weitere läuft über Kontextmenüs.

## Hauptmenü (tldraw-Logo, oben links)

| Menüpunkt | Beschreibung |
|-----------|--------------|
| Export document | Datei als `.tldr` (JSON), PNG, SVG, JSON |
| New project / New page | Neue Datei / neue Seite |
| Print document | Druckansicht |
| Preferences | Dark Mode, Zoom-Kurzbefehle, Snap-Verhalten |
| Static image export | PNG/SVG mit Background/Bounds-Optionen |
| Toggle debug mode / Editor content | Entwicklerhilfen |

## Share-Menü (oben rechts)

- **Share…** — Link erzeugen (nur in der tldraw-Cloud bzw. mit Sync-Server)
- **Duplicate**, **Save as**, **Rename**, **Document metadata**

## Seiten-Menü

- Seitenliste, Seite umbenennen, duplizieren, löschen, neue Seite

## Werkzeugleiste (unten, mittig)

Select · Hand · Laser · Stift · Radierer · Pfeil · Rahmen · Rechteck · Ellipse · Linie · Dreieck · Wolke · Notiz · Text · Bild · Bookmark · (eigene Tools via SDK)

## Stil-Panel (rechts, je nach Auswahl)

Farbe, Füllung, Linienstil, Größe, Schrift, Ausrichtung, Deckkraft, Bindings lösen.

## Kontextmenü (Rechtsklick)

| Eintrag | Beschreibung |
|---------|--------------|
| Copy / Paste / Duplicate | Zwischenablage |
| Bring to front / Send to back | Ebenen |
| Group / Ungroup | Gruppierung |
| Lock / Unlock | Sperren |
| Add to new page | Auswahl auslagern |
| Align / Distribute | Ausrichtungswerkzeuge |
| Delete | Auswahl löschen |
| Arrow bindings | Bindings bearbeiten (bei Pfeilen) |

## Menüs nach Rolle

| Rolle | Sichtbares |
|-------|-----------|
| Editor (Schreibrecht) | alle Menüs |
| Viewer (Nur-Lese-Link) | nur Navigation/Export |
| Eigentümer | zusätzlich Teilen/Löschen |

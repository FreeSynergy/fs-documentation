# QGIS - Struktur und UI/UX

## Fensterlayout

```
┌────────────────────────────────────────────────────────────────┐
│ Menü · Werkzeugleisten (Digit.: ✏ snap identify messen…)       │
├──────────┬──────────────────────────────────┬──────────────────┤
│ Layer-Baum│   Kartenansicht (CRS on-the-fly) │ Processing-Toolbox│
│ ▸ Standpkt│      (Zoom/Pan, Eingeblendet)    │ ▸ Analyse…        │
│ ▸ Gewässer│                                  │ ▸ Überlagerung…   │
├──────────┴──────────────────────────────────┴──────────────────┤
│ Status: Koordinaten | Maßstab | Schnapp-Radius | Rendering-Log │
└────────────────────────────────────────────────────────────────┘
Attributtabelle unten andockbar; Layereigenschaften als Dialog
```

- Layertree oben = Zeichenreihenfolge (unten = oben in der Karte)
- Rechts Processing-Toolbox mit Suchfeld (der „Alles-Finder“ der Analysen)

## UI/UX

- Desktop-Klassik: Dialoge, Rechtsklick-Kontextmenü je Layer/Werkzeug
- Stile als qml-Dateien (austauschbar, in Projekten versionierbar)

## Interaktionen

- Editier-Modus:vertices ziehen, snapping (Umschalt für Temp-Breakout)
- Identify-Tool = Attribut-Popups; Maßstabs-/Selection-Reiter in Attributtabelle

## Responsive Design

entfällt (Desktop; QField für Mobil)

## Accessibility

-Qt-Standard; Menüs/Shortcuts tastaturvoll; Farbflächen für Farbschwache (Muster-Stile)

## Performance

- große Layer: Generalisierung/Overviews, Indizes in PostGIS; Render-Parallelismus nutzen

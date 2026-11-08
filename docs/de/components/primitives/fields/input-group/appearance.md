# Input Group - Erscheinungsbild

## Grundlayout

```
┌──────────┬────────────────────────────┐
│ https:// │ free-synergy.org           │   Präfix links, Wert rechts davon
└──────────┴────────────────────────────┘

┌────────────────────────────┬─────┐
│ Nach Dateien suchen        │ 🔍  │   Aktion rechts, gemeinsame äußere Ecke
└────────────────────────────┴─────┘
```

Feld und angesetzte Teile bilden eine Fläche. Innere Kanten sind gemeinsam,
nur die äußeren Ecken sind abgerundet.

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **praefix** | versetzter Streifen links, gleiche Höhe wie das Feld |
| **suffix** | versetzter Streifen rechts |
| **aktion** | Button in Feldhöhe, durch eine innere Kante abgetrennt |
| **auswahl** | Präfix mit Pfeil, öffnet ein kleines Menü |

## Größen

Gekoppelt an die Größenstufen der [Base-Komponente](../../basics/base.md):

| Größe | Höhe | Icon im angesetzten Teil | Schrift |
|-------|------|--------------------------|---------|
| `small` | 28 px | 14 px | 13 px |
| `medium` | 36 px | 16 px | 14 px |
| `large` | 44 px | 20 px | 16 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | angesetztes Teil auf neutraler Fläche, Trennkante sichtbar |
| `focus-within` | Feldrahmen in der Primärfarbe, angesetztes Teil bleibt neutral |
| `filled` | Wert gesetzt, der Aktions-Button wird aktiv |
| `error` | Rahmen der ganzen Gruppe in der Fehlerfarbe |
| `disabled` | Gruppe abgedunkelt, angesetztes Teil mit ihr |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `highlight` | angesetztes Teil und Feld reagieren gemeinsam auf den Fokus |
| `tone` | Aktions-Button wird beim Hover eine Stufe dunkler |
| `ring` | Fokusring um die ganze Gruppe für die Tastaturnavigation |

## Responsiv

```css
.input-group { display: flex; align-items: stretch; }
.input-group > * { border-radius: 0; }
.input-group > :first-child { border-top-left-radius: 6px; border-bottom-left-radius: 6px; }
.input-group > :last-child  { border-top-right-radius: 6px; border-bottom-right-radius: 6px; }

@media (max-width: 480px) {
  .input-group--aktion { flex-direction: column; }   /* Aktion unter dem Feld */
}
```

Auf einer schmalen Fläche rutscht die Aktion unter das Feld. Präfixe bleiben am
Feld, weil sie zum Wert gehören.

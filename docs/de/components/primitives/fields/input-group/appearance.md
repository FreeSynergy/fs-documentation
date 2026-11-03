# Input Group (Feldgruppe) - Aussehen

## Grundlayout

```
┌──────────┬────────────────────────────┐
│ https:// │ free-synergy.org           │   Vorsatz links, Wert rechts davon
└──────────┴────────────────────────────┘

┌────────────────────────────┬─────┐
│ Suche nach Dateien         │ 🔍  │   Aktion rechts, gemeinsame Außenecke
└────────────────────────────┴─────┘
```

Feld und Anbauteile bilden eine Fläche: Innenkanten werden geteilt, nur die äußeren Ecken
sind gerundet.

## Varianten

| Variante | Aussehen |
|----------|----------|
| **praefix** | abgesetzter Streifen links, gleiche Höhe wie das Feld |
| **suffix** | abgesetzter Streifen rechts |
| **aktion** | Schaltfläche in Feldhöhe, getrennt durch Innenkante |
| **auswahl** | Vorsatz mit Pfeil, öffnet ein kleines Menü |

## Größen

Anschluss an das Größen-Raster der [Basiskomponente](../../basics/base/):

| Größe | Höhe | Icon im Anbauteil | Schrift |
|-------|------|-------------------|---------|
| `small` | 28 px | 14 px | 13 px |
| `medium` | 36 px | 16 px | 14 px |
| `large` | 44 px | 20 px | 16 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Anbauteil auf-neutraler Fläche, Trennkante sichtbar |
| `focus-within` | Feldrand in Primärfarbe, Anbauteil bleibt neutral |
| `filled` | Wert gesetzt, Aktions-Schaltfläche wird aktiv |
| `error` | Rand der ganzen Gruppe in Fehlerfarbe |
| `disabled` | Gruppe abgeblendet, Anbauteil mit |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `highlight` | Anbauteil und Feld reagieren gemeinsam auf Fokus |
| `tone` | Aktions-Schaltfläche eine Stufe dunkler bei Hover |
| `ring` | Fokusring um die gesamte Gruppe bei Tastaturnavigation |

## Reaktiv

```css
.input-group { display: flex; align-items: stretch; }
.input-group > * { border-radius: 0; }
.input-group > :first-child { border-top-left-radius: 6px; border-bottom-left-radius: 6px; }
.input-group > :last-child  { border-top-right-radius: 6px; border-bottom-right-radius: 6px; }

@media (max-width: 480px) {
  .input-group--aktion { flex-direction: column; }   /* Aktion unter das Feld */
}
```

Auf schmaler Fläche rutscht die Aktion unter das Feld; Vorsätze bleiben am Feld, weil sie
zum Wert gehören.

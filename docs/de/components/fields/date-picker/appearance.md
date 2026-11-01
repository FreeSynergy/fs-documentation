# Date Picker (Datumsauswahl) - Aussehen

## Grundlayout

```
┌───────────────────────────────┐
│  ‹  Oktober 2026           ⌄  │
├───────────────────────────────┤
│  Mo Di Mi Do Fr Sa So         │
│   1  2  3  4  5  6  7         │
│  12 ● 14 ▪▪ 15 ▓ 16 ·         │
│  …                            │
├───────────────────────────────┤
│  14. Oktober                  │
│  ● 10:00 Stand-up             │
│  ▪ 15:00 Review  · 2 Tage     │
│  + 3 weitere                  │
│  [+ Eintrag]                  │
├───────────────────────────────┤
│  Heute · Morgen · Nächste Wo. │
└───────────────────────────────┘

▓ ausgewählt   ● Termin   ▪ Aufgabe   · ein weiterer Eintrag
```

Ohne Datenanbindung (`sources` leer) entfallen Rastermarken und Tagesliste; das Overlay
besteht dann nur aus Monatsraster und Schnellauswahl.

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzeln** | ein Tag farbig gefüllt |
| **bereich** | Start und Ende gefüllt, dazwischen hell unterlegt |
| **wiederkehrend** | Kalender plus Regelzeile darunter |

## Größen

| Größe | Tagfläche | Overlaybreite | Tagesliste |
|-------|-----------|---------------|------------|
| `small` | 28 px | 260 px | zwei Zeilen, Punkte 4 px |
| `medium` | 36 px | 320 px | vier Zeilen, Punkte 6 px |
| `large` | 44 px | 400 px | sechs Zeilen, Punkte 6 px |

## Tageseinträge

| Element | Aussehen |
|---------|----------|
| Tagemarke | ein Punkt je Eintrag, horizontal gereiht, max. `entryLimit` |
| Zählermarke | mehr Einträge als `entryLimit`: ein Punkt mit Zahl |
| Serienmarke | Punkt mit unterbrochenem Rand, Signal für `recurrenceRule` |
| Erledigt | Punkt abgedämpft, Titel durchgestrichen (`status = done`) |
| Mehrtägig | Marke setzt sich über die betroffenen Tage als durchgehender Balken fort |
| Tagesliste | Titel, Uhrzeit bzw. `allDay`, Typ als Punkt; Einträge des gewählten Tages |
| Schnellaufnahme | eine Zeile mit Titel und Zeitfeld unter der Liste, nur bei `creatable` |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Tage neutral, Wochenende gedämpft |
| `hover` | Tagfläche leicht hinterlegt |
| `active` | Tag in Primärfarbe gefüllt, heller Text |
| `outOfRange` | Tag ausgegraut, nicht wählbar |
| `open` | Overlay mit Schatten, aktueller Monat hervorgehoben |
| `loading` | Raster weiter bedienbar, Tagesliste mit Skeletonzeilen |
| `error` | Tagesliste mit Fehlerzeile und Wiederholen, Marken des Fensters fehlen |

Eintragstypen behalten ihre Farbe über alle Ansichten hinweg; die Zuordnung kommt aus
dem Datensatz (`color`), sonst aus dem Typ.

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Fokusring auf dem gewählten Tag, Tastaturnavigation |
| `fade-in` | Overlay blendet ein, Monatswechsel seitlich |
| `tooltip` | Zeigt bei einer Tagemarke die Titel der Einträge (max. drei) |
| `lift` | Gezogener Eintrag folgt dem Zeiger, Zieltag wird hinterlegt |

## Reaktiv

- Unter 500 px Breite wird das Overlay zur bodenbündigen Fläche mit Listenansicht.
- Monatswechsel per Wischgeste.
- Tagesliste wird unter dem Raster vollständig ausgespielt; die Punkte entfallen, der
  Zähler steht am Wochentag.
- Langer Druck auf einen Tag öffnet die Schnellaufnahme für diesen Tag.

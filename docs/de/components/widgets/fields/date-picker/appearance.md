# Date Picker - Erscheinungsbild

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
│  Heute · Morgen · Nächste Woche │
└───────────────────────────────┘

▓ ausgewählt   ● Termin   ▪ Aufgabe   · ein weiterer Eintrag
```

Ohne Datenverbindung (`sources` leer) entfallen die Markierungen im Raster und die Tagesliste;
das Overlay besteht dann nur aus dem Monatsraster und der Schnellauswahl.

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einzeln** | ein Tag in Farbe gefüllt |
| **bereich** | Anfang und Ende gefüllt, dazwischen leicht getönt |
| **wiederkehrend** | Kalender plus eine Regelzeile darunter |

## Größen

| Größe | Tagesfläche | Overlay-Breite | Tagesliste |
|-------|-------------|----------------|------------|
| `small` | 28 px | 260 px | zwei Zeilen, Punkte 4 px |
| `medium` | 36 px | 320 px | vier Zeilen, Punkte 6 px |
| `large` | 44 px | 400 px | sechs Zeilen, Punkte 6 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Tage neutral, Wochenende gedämpft |
| `hover` | Tagesfläche leicht getönt |
| `active` | Tag in der Primärfarbe gefüllt, helle Schrift |
| `outOfRange` | Tag ausgegraut, nicht auswählbar |
| `open` | Overlay mit Schatten, aktueller Monat hervorgehoben |
| `loading` | Raster bleibt bedienbar, Tagesliste mit Skeleton-Zeilen |
| `error` | Tagesliste mit Fehlerzeile und Wiederholen, die Markierungen des Fensters fehlen |

Eintragstypen behalten ihre Farbe in allen Ansichten; die Zuordnung kommt aus
dem Datensatz (`color`), sonst aus dem Typ.

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Fokusring auf dem ausgewählten Tag, Tastaturnavigation |
| `fade-in` | das Overlay blendet ein, Monatswechsel gleiten seitlich |
| `tooltip` | zeigt die Titel der Einträge für eine Tagesmarkierung (max. drei) |
| `lift` | ein gezogener Eintrag folgt dem Zeiger, der Zieltag wird getönt |

## Responsiv

- Unter 500 px Breite wird das Overlay zu einer am unteren Rand verankerten Fläche mit einer Listenansicht.
- Monatswechsel per Wischgeste.
- Die Tagesliste wird unter dem Raster vollständig ausgeklappt; die Punkte entfallen, der
  Zähler sitzt beim Wochentag.
- Ein langes Drücken auf einen Tag öffnet die Schnelleingabe für diesen Tag.

## Einträge pro Tag

| Element | Erscheinungsbild |
|---------|------------------|
| Tagesmarkierung | ein Punkt pro Eintrag, waagerecht aufgereiht, max. `entryLimit` |
| Zählermarkierung | mehr Einträge als `entryLimit`: ein Punkt mit einer Zahl |
| Serienmarkierung | Punkt mit gestricheltem Rand, Hinweis auf `recurrenceRule` |
| Erledigt | Punkt gedämpft, Titel durchgestrichen (`status = done`) |
| Mehrtägig | die Markierung läuft als ununterbrochener Balken über die betroffenen Tage |
| Tagesliste | Titel, Uhrzeit oder `allDay`, Typ als Punkt; die Einträge des gewählten Tages |
| Schnelleingabe | eine Zeile mit Titel- und Zeitfeld unter der Liste, nur bei `creatable` |

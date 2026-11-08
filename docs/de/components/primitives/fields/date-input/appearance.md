# Datumsfeld – Erscheinungsbild

## Grundlayout
Ein Datumsfeld ist ein Feld zur Datumsauswahl mit einem Kalender.

```
┌─────────────────────────────────────────┐
│ Datum                                   │
├─────────────────────────────────────────┤
│  📅 2024-01-15                          │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante (`type`) | Erscheinungsbild |
|------------------|------------|
| **date** | Feld mit Kalendersymbol, darunter das Kalender-Overlay |
| **time** | Feld mit Uhrsymbol, statt Kalender ein Raster mit Uhrzeiten |
| **datetime** | zwei Segmente in einem Feld, zuerst Kalender, dann Uhrzeit |

## Größen

| Größe | Höhe | Verwendung |
|------|--------|-----|
| small | 32px | im Textfluss |
| medium | 48px | Standard |
| large | 64px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|--------|-------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Das Kalender-Overlay ist mindestens 280 px breit; auf schmalen Bildschirmen öffnet es sich unten verankert
  als Vollbild-Dialog.
- Monatswechsel über `swipe`, der Übergang ist `slide-in`.
- Die Tagesflächen bleiben auch in einem schmalen Raster mindestens 40 px hoch; unterhalb der
  Bildschirmbreite `small` wird das Feld auf `large` gesetzt.

## Kalender-Overlay

```
┌─────────────────────────────────────────┐
│        Januar 2024                      │
│ Mo Di Mi Do Fr Sa So                    │
│          1  2  3  4  5  6  7            │
│  8  9 10 11 12 13 14 [15] 16 17         │
│ 18 19 20 21 22 23 24 25 26 27 28 29 30  │
│ 31                                       │
└─────────────────────────────────────────┘
```

## Bereichsauswahl

```
┌─────────────────────────────────────────┐
│ Von - Bis                               │
├─────────────────────────────────────────┤
│  [01/01/2024] ━━━━━━━━━━━ [15/01/2024] │
└─────────────────────────────────────────┘
```

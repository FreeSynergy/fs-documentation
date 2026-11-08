# Number Input - Erscheinungsbild

## Grundlayout
Ein Number Input ist ein Eingabefeld für Zahlen.

```
┌─────────────────────────────────────────┐
│ Menge                                   │
├─────────────────────────────────────────┤
│  [ 123 ]                                │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | Zahlenfeld ohne Bedienelemente |
| **stepper** | kleine Pfeiltasten übereinander rechts am Feld |
| **formatiert** | Wert rechts ausgerichtet, Einheit grau hinter dem Wert |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| small | 32px | inline |
| medium | 48px | Standard |
| large | 64px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Schrittbuttons sind quadratisch und mindestens 32 px groß, auf Touchgeräten 44 px.
  Bei der Breite `small` stehen sie außerhalb, links neben dem Feld.
- Der Wert bleibt rechts ausgerichtet. Lange Zahlen werden nicht gekürzt, das Feld wächst mit.
- Auf Touchgeräten erscheint die Zahlentastatur. Bei `formatiert` ohne Tausendertrennzeichen.

## Schrittbuttons

```
┌─────────────────────────────────────────┐
│ Menge                                   │
├─────────────────────────────────────────┤
│  [ 123 ]   [▲]                          │
│            [▼]                          │
└─────────────────────────────────────────┘
```

## Validierungszustände

| Zustand | Beschreibung |
|---------|--------------|
| **valid** | grün |
| **invalid** | rot |
| **warning** | orange |

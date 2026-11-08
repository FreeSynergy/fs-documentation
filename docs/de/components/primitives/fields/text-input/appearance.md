# Text Input - Erscheinungsbild

## Grundlayout

Ein Text Input ist ein einzeiliges Eingabefeld für Text.

## Varianten

### Standard

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  Max Mustermann                         │
│                                         │
└─────────────────────────────────────────┘
```

### Schwebendes Label

```
┌─────────────────────────────────────────┐
│  Name                                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  Max Mustermann                         │
└─────────────────────────────────────────┘
```

### Unterstrichen

```
┌─────────────────────────────────────────┐
│ Name                                    │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     │
│ Max Mustermann                          │
└─────────────────────────────────────────┘
```

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

- In Formularen stehen die Felder auf schmalen Bildschirmen voll breit unter ihrem Label.
  Zweispaltige Raster fallen auf eine Spalte zurück.
- Auf Touchgeräten ist die Höhe mindestens 44 px. Der Text bleibt linksbündig und scrollt
  im Feld. Die Schrift wird nicht größer als 16 px (kein Zoom auf dem Handy).
- Das aktive Feld bleibt über der Tastatur sichtbar. Die Fehlerzeile rutscht darunter,
  ohne das nächste Feld zu verdecken.

## Validierungszustände

| Zustand | Beschreibung |
|---------|--------------|
| **valid** | grün |
| **invalid** | rot |
| **warning** | orange |

## Platzhalter

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  Vorname Nachname                       │
│                                         │
└─────────────────────────────────────────┘
```

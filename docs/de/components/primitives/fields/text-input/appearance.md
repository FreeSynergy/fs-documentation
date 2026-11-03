# Text Input (Einzeiliges Textfeld) - Aussehen

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

### Floating Label

```
┌─────────────────────────────────────────┐
│  Name                                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│  Max Mustermann                         │
└─────────────────────────────────────────┘
```

### Underline

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
| Small | 32px | Inline |
| Medium | 48px | Standard |
| Large | 64px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Reaktiv

- In Formularen stehen die Felder auf schmalen Bildschirmen vollbreit unter ihrem Label,
  Zwei-Spalten-Raster fallen auf eine Spalte zurück.
- Auf Touch-Geräten wird die Höhe mindestens 44 px; der Text bleibt linksbündig und scrollt
  innerhalb des Feldes, die Schriftgröße wächst nicht über 16 px (kein Zoom auf Mobil).
- Das aktive Feld wird über die Tastatur hinweg sichtbar gehalten, die Fehlerzeile rutscht
  darunter, ohne das nächste Feld zu überdecken.

## Validation States

| State | Beschreibung |
|-------|--------------|
| **Valid** | Grün |
| **Invalid** | Rot |
| **Warning** | Orange |

## Placeholder

```
┌─────────────────────────────────────────┐
│ Name                                    │
├─────────────────────────────────────────┤
│  Vorname Nachname                       │
│                                         │
└─────────────────────────────────────────┘
```

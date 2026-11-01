# Number Input - Aussehen

## Grundlayout
Ein Number Input ist ein Eingabefeld für Zahlen.

```
┌─────────────────────────────────────────┐
│ Anzahl                                  │
├─────────────────────────────────────────┤
│  [ 123 ]                                │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einfach** | Zahlenfeld ohne Bedienelemente |
| **stepper** | kleine Pfeiltaste gestapelt rechts am Feld |
| **formatiert** | Wert rechtsbündig, Einheit grau hinter dem Wert |

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

## Step-Buttons

```
┌─────────────────────────────────────────┐
│ Anzahl                                  │
├─────────────────────────────────────────┤
│  [ 123 ]   [▲]                          │
│            [▼]                          │
└─────────────────────────────────────────┘
```

## Validation States

| State | Beschreibung |
|-------|--------------|
| **Valid** | Grün |
| **Invalid** | Rot |
| **Warning** | Orange |

## Reaktiv

- Die Schritt-Knöpfe sind quadratisch und mindestens 32 px, auf Touch-Geräten 44 px;
  bei `small` Bildschirmbreite werden sie links und außen neben das Feld gestellt.
- Der Wert bleibt rechtsbündig; zu lange Zahlen kürzen nicht, das Feld wächst mit.
- Auf Touch-Geräten erscheint die Zifferntastatur, bei `formatiert` ohne Gruppierungszeichen.

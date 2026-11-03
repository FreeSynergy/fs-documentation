# Table of Contents - Aussehen

## Grundlayout
Ein Table of Contents ist eine Übersicht über Kapitel/Sectionen.

```
┌─────────────────────────────────────────┐
│ 📚 Inhaltsverzeichnis                   │
│                                         │
│  1. Kapitel 1                           │
│  2. Kapitel 2                           │
│  3. Kapitel 3                           │
│    3.1. Unterkapitel 1                  │
│    3.2. Unterkapitel 2                  │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **randspalte** | schmaler Streifen am Rand, Kopfzeile sticky |
| **block** | Liste im Textfluss, leicht eingerückt |
| **aufklappbar** | Knopf mit Liste darüber, Liste überdeckt den Text |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktueller Abschnitt |
| **Inactive** | Grau | Inaktive Abschnitte |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `border-bottom` | Unterstrich erscheint |

## Reaktiv

- Als Randspalte ist die Liste maximal 240 px breit und bleibt beim Scrollen stehen
  (eigener Scrollbereich, wenn sie höher als der Viewport ist).
- Unter `small` Bildschirmbreite entfällt die Randspalte; die Variante `aufklappbar`
  öffnet sich über dem Text und schließt nach der Auswahl.
- Unterpunkte klappen mit `expand`/`collapse` auf, der aktive Punkt bleibt markiert,
  auch wenn die Liste selbst gescrollt hat.

## Collapsible Sections

```
┌─────────────────────────────────────────┐
│ 📚 Inhaltsverzeichnis                   │
│                                         │
│ ▶ 1. Kapitel 1                          │
│ ▶ 2. Kapitel 2                          │
│   └─ 2.1. Unterkapitel 1               │
│   └─ 2.2. Unterkapitel 2               │
│ ▶ 3. Kapitel 3                          │
└─────────────────────────────────────────┘
```

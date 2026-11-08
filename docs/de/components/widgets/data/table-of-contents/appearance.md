# Table of Contents - Erscheinungsbild

## Grundlayout
Ein Inhaltsverzeichnis ist eine Übersicht über Kapitel und Abschnitte.

```
┌─────────────────────────────────────────┐
│ 📚 Inhalt                               │
│                                         │
│  1. Kapitel 1                           │
│  2. Kapitel 2                           │
│  3. Kapitel 3                           │
│    3.1. Unterkapitel 1                  │
│    3.2. Unterkapitel 2                  │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **randspalte** | schmaler Streifen am Rand, Kopfzeile bleibt stehen |
| **block** | Liste im Textfluss, leicht eingerückt |
| **aufklappbar** | Knopf mit der Liste darüber, die Liste verdeckt den Text |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|--------------|------------|
| small | 12px | inline |
| medium | 14px | Standard |
| large | 16px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | aktueller Abschnitt |
| **Inactive** | grau | inaktive Abschnitte |
| **Hover** | heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | die Farbe ändert sich |
| `border-bottom` | eine Unterstreichung erscheint |

## Responsiv

- Als Randspalte ist die Liste höchstens 240 px breit und bleibt beim Scrollen stehen
  (mit eigenem Scrollbereich, wenn sie höher als der Viewport ist).
- Unterhalb einer kleinen Bildschirmbreite (`small`) entfällt die Randspalte; die Variante `aufklappbar`
  öffnet sich über dem Text und schließt sich nach einer Auswahl.
- Unterpunkte klappen mit `expand`/`collapse` auf; der aktive Punkt bleibt markiert,
  auch wenn die Liste selbst gescrollt wurde.

## Einklappbare Abschnitte

```
┌─────────────────────────────────────────┐
│ 📚 Inhalt                               │
│                                         │
│ ▶ 1. Kapitel 1                          │
│ ▶ 2. Kapitel 2                          │
│   └─ 2.1. Unterkapitel 1                │
│   └─ 2.2. Unterkapitel 2                │
│ ▶ 3. Kapitel 3                          │
└─────────────────────────────────────────┘
```

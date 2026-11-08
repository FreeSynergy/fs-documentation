# Checkbox – Erscheinungsbild

## Grundlayout
Eine Checkbox ist ein Ja/Nein- oder Mehrfachauswahl-Feld.

```
┌─────────────────────────────────────────┐
│ [✓] Option 1                            │
│ [ ] Option 2                            │
│ [✓] Option 3                            │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Default** | normales Quadrat |
| **Toggle** | Schalter-Optik |
| **Indeterminate** | teilweise ausgewählt |

## Größen

| Größe | Breite | Verwendung |
|------|-----|-----|
| small | 20px | im Textfluss |
| medium | 24px | Standard |
| large | 28px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|--------|-------------|
| **checked** | Primärfarbe | ausgewählt |
| **unchecked** | grau | nicht ausgewählt |
| **disabled** | grau | deaktiviert |
| **hover** | heller | Hover-Zustand |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `scale` | Vergrößerung |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Bei schmalen Breiten rutscht die Beschriftung unter das Kästchen; die Trefferfläche bleibt mindestens 44 px hoch.
- Optionsgruppen werden in einer Spalte gestapelt, der Einzug von Unterpunkten bleibt erhalten.
- Auf Touchgeräten wächst das Kästchen auf `large` (28 px), die Beschriftung behält die Schriftgröße von `medium`.

## Mit Icons

```
┌─────────────────────────────────────────┐
│ [✓] Option 1   [Icon]                   │
│ [ ] Option 2   [Icon]                   │
│ [✓] Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```

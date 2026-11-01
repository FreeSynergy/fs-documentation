# Checkbox (Ankreuzfeld) - Aussehen

## Grundlayout
Ein Checkbox ist ein Ja/Nein- oder Mehrfachauswahlfeld.

```
┌─────────────────────────────────────────┐
│ [✓] Option 1                            │
│ [ ] Option 2                            │
│ [✓] Option 3                            │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Standard-Quadrat |
| **Toggle** | Schalter-Stil |
| **Indeterminate** | Teilweise ausgewählt |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 20px | Inline |
| Medium | 24px | Standard |
| Large | 28px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Checked** | Primärfarbe | Ausgewählt |
| **Unchecked** | Grau | Nicht ausgewählt |
| **Disabled** | Grau | Deaktiviert |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |

## With Icons

```
┌─────────────────────────────────────────┐
│ [✓] Option 1   [Icon]                   │
│ [ ] Option 2   [Icon]                   │
│ [✓] Option 3   [Icon]                   │
└─────────────────────────────────────────┘
```

## Reaktiv

- Bei schmaler Breite rutscht das Label unter die Box; die Trefferfläche bleibt mindestens 44 px hoch.
- Optionsgruppen werden einspaltig gestapelt, der Einzug der Unterpunkte bleibt erhalten.
- Auf Touch-Geräten wird die Box auf `large` (28 px) hochskaliert, das Label bleibt in der Schriftgröße von `medium`.

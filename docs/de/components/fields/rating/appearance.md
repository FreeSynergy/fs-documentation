# Rating - Aussehen

## Grundlayout

Ein Rating ist eine Sterne- oder Punktebewertung.

## Varianten

### Star Rating

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆                                   │
└─────────────────────────────────────────┘
```

### Heart Rating

```
┌─────────────────────────────────────────┐
│ ❤️❤️❤️❤️                                 │
└─────────────────────────────────────────┘
```

### Number Rating

```
┌─────────────────────────────────────────┐
│ 4/5                                     │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 80px | Inline |
| Medium | 120px | Standard |
| Large | 160px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Filled** | Gold | Gefüllte Symbole |
| **Empty** | Grau | Leere Symbole |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `transform` | Hebung |

## With Count

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (4.5)                            │
└─────────────────────────────────────────┘
```

## Read-only

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (123 Bewertungen)                │
└─────────────────────────────────────────┘
```

## Reaktiv

- Symbole bleiben mindestens 24 px groß; auf Touch-Geräten wird die Trefferfläche pro Stufe
  auf 44 px erweitert, ohne dass der Streifen breiter wird.
- Bei schmalem Raum rutscht die Bewertungszahl unter den Streifen statt daneben.
- Einmal tippen genügt; `drag` über den Streifen erlaubt feines Nachjustieren, loslassen bestätigt.

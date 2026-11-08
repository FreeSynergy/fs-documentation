# Rating - Erscheinungsbild

## Grundlayout

Eine Bewertung ist eine Bewertung mit Sternen oder Punkten.

## Varianten

### Sternbewertung

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆                                   │
└─────────────────────────────────────────┘
```

### Herzbewertung

```
┌─────────────────────────────────────────┐
│ ❤️❤️❤️❤️                                 │
└─────────────────────────────────────────┘
```

### Zahlenbewertung

```
┌─────────────────────────────────────────┐
│ 4/5                                     │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 80px | inline |
| medium | 120px | Standard |
| large | 160px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **filled** | gold | gefüllte Symbole |
| **empty** | grau | leere Symbole |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `transform` | Anheben |

## Responsiv

- Die Symbole bleiben mindestens 24 px groß. Auf Touchgeräten wächst der Trefferbereich
  pro Stufe auf 44 px, ohne dass die Leiste breiter wird.
- Auf schmalem Raum rutscht die Bewertungszahl unter die Leiste statt daneben.
- Ein Tipp genügt. Mit `drag` über die Leiste lässt sich fein einstellen. Loslassen bestätigt.

## Mit Anzahl

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (4.5)                            │
└─────────────────────────────────────────┘
```

## Nur lesen

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (123 Bewertungen)                │
└─────────────────────────────────────────┘
```

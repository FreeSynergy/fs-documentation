# Description List - Erscheinungsbild

## Grundlayout

```
Label                Wert
──────────────────────────────
Name                 Anna Berger
Rolle                Projektplanung
Fällig am            12. Nov. 2026
Status               ● offen
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **zweispaltig** | Label 160 px, Wert füllt den Rest |
| **gestapelt** | Label klein und gedämpft über dem Wert |
| **inline** | `Name: Anna Berger · Rolle: Projektplanung` |

## Größen

| Größe | Zeilenhöhe | Label-Breite |
|-------|------------|--------------|
| `small` | 24 px | 120 px |
| `medium` | 32 px | 160 px |
| `large` | 40 px | 200 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Label gedämpft, Wert in der Grundfarbe |
| `hover` | Zeile leicht getönt, Kopiersymbol erscheint |
| `empty` | „kein Wert“ in der dritten Farbstufe, oder die Zeile ist ausgeblendet |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Kopiersymbol rechts in der Zeile |
| `line` | dezente Trennlinie zwischen den Zeilen, optional |

## Responsiv

- Unter 600 px Breite automatisch `gestapelt`.
- `inline` bricht an den Trennzeichen um, nie mitten in einem Wert.

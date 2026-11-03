# Description List (Beschreibungsliste) - Aussehen

## Grundlayout

```
Bezeichnung        Wert
──────────────────────────────
Name               Anna Berger
Rolle              Projektplanung
Frist              12.11.2026
Status             ● offen
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **zweispaltig** | Bezeichnung 160 px, Wert füllt den Rest |
| **gestapelt** | Bezeichnung klein und gedämpft über dem Wert |
| **inline** | `Name: Anna Berger · Rolle: Projektplanung` |

## Größen

| Größe | Zeilenhöhe | Bezeichnungsbreite |
|-------|------------|--------------------|
| `small` | 24 px | 120 px |
| `medium` | 32 px | 160 px |
| `large` | 40 px | 200 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Bezeichnung gedämpft, Wert in Grundfarbe |
| `hover` | Zeile leicht hinterlegt, Kopieren-Icon erscheint |
| `empty` | „kein Wert“ in dritter Farbstufe oder Zeile ausgeblendet |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Kopieren-Icon rechts in der Zeile |
| `line` | dezente Trennlinie zwischen Zeilen, optional |

## Reaktiv

- Unter 600 px Breite automatisch `gestapelt`.
- `inline` bricht an Trennzeichen um, nie mitten im Wert.

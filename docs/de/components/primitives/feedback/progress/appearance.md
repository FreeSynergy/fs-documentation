# Progress - Erscheinungsbild

## Grundlayout

```
linear:
┌───────────────────────────────┐
│ ████████████░░░░░░░░░░░░░░░░░ │  45 %
└───────────────────────────────┘

circular:
        ╭─────╮
       ╱  45% ╲
       ╲      ╱
        ╰─╮ ╭╯
          ╰─╯
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **linear** | Balken in der Primärfarbe, der Rest als neutrale Spur |
| **circular** | Ring, der Fortschritt läuft im Uhrzeigersinn ab 12 Uhr |
| **mit-label** | Prozentwert oder Text über dem Balken oder im Kreis |
| **unbestimmt** | ein Segment läuft über die Spur, ohne Prozentangabe |

## Größen

| Größe | Höhe linear | Durchmesser circular | Ringstärke |
|-------|-------------|----------------------|------------|
| `small` | 4 px | 24 px | 2 px |
| `medium` | 8 px | 48 px | 4 px |
| `large` | 12 px | 96 px | 6 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Primärfarbe |
| `success` (100 %) | grün |
| `error` (Abbruch/Fehler) | rot |
| `indeterminate` | Segment in der Primärfarbe, Spur sichtbar |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | optionale Details („12 von 40 Dateien“) |
| – | ein eigener Hover oder Fokus ist nicht vorgesehen |

## Responsiv

- `linear` folgt der Breite des Containers. `circular` skaliert mit `size`
  oder einer festen `strokeWidth`.

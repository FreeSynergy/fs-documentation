# Progress (Fortschrittsanzeige) - Aussehen

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

| Variante | Aussehen |
|----------|----------|
| **linear** | Balken in Primärfarbe, Rest neutrale Spur |
| **circular** | Ring, Fortschritt im Uhrzeigersinn ab 12 Uhr |
| **mit-label** | Prozentwert oder Text über dem Balken bzw. im Kreis |
| **unbestimmt** | Segment wandernd in der Spur, ohne Prozentangabe |

## Größen

| Größe | Höhe linear | Durchmesser circular | Ringstärke |
|-------|-------------|----------------------|------------|
| `small` | 4 px | 24 px | 2 px |
| `medium` | 8 px | 48 px | 4 px |
| `large` | 12 px | 96 px | 6 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Primärfarbe |
| `success` (100 %) | grün |
| `error` (Abbruch/Fehler) | rot |
| `indeterminate` | Segment in Primärfarbe, Spur sichtbar |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | optional Details („12 von 40 Dateien“) |
| – | eigener Hover/Fokus ist nicht vorgesehen |

## Reaktiv

- `linear` folgt der Containerbreite; `circular` skaliert mit `size`
  oder explizitem `strokeWidth`.

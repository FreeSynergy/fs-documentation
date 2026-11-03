# Command (Befehlspalette) - Aussehen

## Grundlayout

```
        ┌────────────────────────────────────────┐
        │ 🔍  Aufgabe anlegen…                   │
        ├────────────────────────────────────────┤
        │ Aktionen                               │
        │   Aufgabe anlegen               Strg N │
        │ Ansichten                                │
        │   Zum Kalender wechseln         Strg 3 │
        │ Programme                                │
        │   Whiteboard öffnen             Strg W │
        └────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **palette** | Overlay mittig, 640 px breit, dunkler Hintergrund dahinter |
| **inline** | ohne Hintergrund, Breite der Elternbox |

## Größen

| Größe | Eingabehöhe | Zeilenhöhe | Max. Treffer |
|-------|-------------|------------|--------------|
| `small` | 32 px | 28 px | 6 |
| `medium` | 40 px | 34 px | 10 |
| `large` | 48 px | 40 px | 14 |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Eingabefeld hell, Trefferliste neutral |
| `open` | Fokus im Eingabefeld, erster Treffer markiert |
| `hover` | Zeilenhintergrund eine Stufe dunkler |
| `empty` | Hinweis „Kein Treffer“ plus Vorschläge |
| `loading` | Skeleton in der Trefferliste |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Kürzel rechts in der Zeile, dezent |
| `ring` | Markierung des aktiven Treffers über die ganze Zeile |

## Reaktiv

- Auf schmalen Bildschirmen füllt die Palette die volle Breite und Höhe.
- Die Trefferliste scrollt; Eingabezeile bleibt oben stehen.

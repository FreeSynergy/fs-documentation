# Command - Erscheinungsbild

## Grundlayout

```
        ┌────────────────────────────────────────┐
        │ 🔍  Aufgabe anlegen…                   │
        ├────────────────────────────────────────┤
        │ Aktionen                               │
        │   Aufgabe anlegen               Strg N │
        │ Ansichten                              │
        │   Zum Kalender wechseln         Strg 3 │
        │ Programme                              │
        │   Whiteboard öffnen             Strg W │
        └────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **palette** | zentriertes Overlay, 640 px breit, dunkler Hintergrund dahinter |
| **inline** | kein Hintergrund, Breite des übergeordneten Feldes |

## Größen

| Größe | Eingabehöhe | Zeilenhöhe | Max. Treffer |
|-------|-------------|------------|--------------|
| `small` | 32 px | 28 px | 6 |
| `medium` | 40 px | 34 px | 10 |
| `large` | 48 px | 40 px | 14 |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Eingabefeld hell, Trefferliste neutral |
| `open` | Fokus im Eingabefeld, erster Treffer markiert |
| `hover` | Zeilenhintergrund eine Stufe dunkler |
| `empty` | Hinweis „Kein Treffer“ plus Vorschläge |
| `loading` | Skeleton in der Trefferliste |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `reveal` | Tastenkürzel rechts in der Zeile, dezent |
| `ring` | Markierung des aktiven Treffers über die ganze Zeile |

## Responsiv

- Auf schmalen Bildschirmen füllt die Palette die volle Breite und Höhe.
- Die Trefferliste scrollt; die Eingabezeile bleibt oben fixiert.

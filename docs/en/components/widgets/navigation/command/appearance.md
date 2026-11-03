# Command (Befehlspalette) - Appearance

## Base layout

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

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **palette** | Overlay mittig, 640 px breit, dunkler Hintergrund dahinter |
| **inline** | ohne Hintergrund, Breite der Elternbox |

## Sizes

| Size | Eingabehöhe | Zeilenhöhe | Max. Treffer |
| ------- | ------------- | ------------ | -------------- |
| `small` | 32 px | 28 px | 6 |
| `medium` | 40 px | 34 px | 10 |
| `large` | 48 px | 40 px | 14 |

## Colours and states

| State | Appearance |
| --------- | ---------- |
| `default` | Eingabefeld hell, Trefferliste neutral |
| `open` | Fokus im Eingabefeld, erster Treffer markiert |
| `hover` | Zeilenhintergrund eine Stufe dunkler |
| `empty` | Hinweis „Kein Treffer“ plus Vorschläge |
| `loading` | Skeleton in der Trefferliste |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `reveal` | Kürzel rechts in der Zeile, dezent |
| `ring` | Markierung des aktiven Treffers über die ganze Zeile |

## Responsive

- Auf schmalen Bildschirmen füllt die Palette die volle Breite und Höhe.
- Die Trefferliste scrollt; Eingabezeile bleibt oben stehen.

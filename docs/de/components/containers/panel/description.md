# Panel (Container)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `einklappbar`, `verschiebbar`, `filter` |
| **Zustände** | `geöffnet`, `geschlossen` |
| **Gesten** | `tap`, `drag`, `long-press` |
| **Animationen** | `expand`, `collapse`, `reorder` |
| **Verwandt** | `card`, `split-view`, `scroll-area`, `accordion`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Panel ist ein großer Container mit Header, Inhalt und Footer. Unterscheidet sich von Card durch größere Größe und Layout-Verwendung.

## Verwendungszweck

- Große Inhalt Blöcke
- Layout-Container
- Filter-Panel
- Dashboard-Widget

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Standard-Panel mit Header |
| **Collapsible** | Header klappt Inhalt ein/aus |
| **Draggable** | Verschiebbar |
| **Filter** | Mit Filter-Optionen |

## Features

- Collapsible (Ein/Ausklappen)
- Draggable (Verschieben)
- Resize (Größe ändern)
- Custom Header (benutzerdefinierter Header)

## Abgrenzung

- **Nicht verwechseln mit** [card](../card/): die Karte zeigt einen Inhalt mit Titel und Aktionen,
  das Panel fasst Bedienelemente oder einen Arbeitsbereich zusammen (Plan Abschnitt 4, Zeile 16 —
  beide bleiben, gemeinsame Container-Basis).
- **Nicht verwechseln mit** [split-view](../split-view/): die geteilte Ansicht zerlegt die Fläche
  in Bereiche, das Panel ist einer dieser Bereiche.
- **Nicht verwechseln mit** [drawer](../../overlays/drawer/) oder [modal](../../overlays/modal/):
  ein Panel bleibt im Layout und überdeckt nichts.
- **Nicht verwechseln mit** [accordion](../accordion/): das Akkordeon ist eine Gruppe von
  Köpfen, das Panel ein einzelner Bereich.

## Best Practices

- Header nennt den Bereich, nicht die Aktion.
- Größe und Innenabstand in einer Anwendung einheitlich halten.
- Einklappbaren Panel-Zustand merken, `aria-expanded` setzen.
- Panelkörper scrollt selbst, die Seite nicht mitscrollen lassen.

## Struktur

```
┌─────────────────────────────────────────┐
│ Header / Titel                          │  ← Header
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │  ← Body
├─────────────────────────────────────────┤
│ Footer / Aktionen                       │  ← Footer
└─────────────────────────────────────────┘
```

## Siehe auch

- [containers – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)

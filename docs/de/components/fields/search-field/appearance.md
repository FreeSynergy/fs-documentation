# Search Field (Suchfeld mit Filter) - Aussehen

## Grundlayout
Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                             │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Einfache Suche |
| **Filter** | Mit Filtern |
| **Auto-complete** | Mit Vorschlägen |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 150px | Inline |
| Medium | 250px | Standard |
| Large | 350px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Clear-Button

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                    [✕]      │
└─────────────────────────────────────────┘
```

## Filter-Overlay

```
┌─────────────────────────────────────────┐
│ 🔍 Suche...                             │
├─────────────────────────────────────────┤
│  [Filter 1] [Filter 2] [Filter 3]       │
│  [Reset]                                │
└─────────────────────────────────────────┘
```

## Reaktiv

- In Werkzeugleisten kann das Feld eingeklappt sein; ein Klick auf das Suchsymbol klappt es
  auf volle Leistenbreite auf (`expand`).
- Unter `small` Bildschirmbreite wird das Feld vollbreit über der Liste gesetzt, die Filter
  rutschen hinter einen Aufklapp-Knopf.
- Vorschlagsliste maximal acht Zeilen, danach scrollt sie; Trefferstellen werden `highlight`et.

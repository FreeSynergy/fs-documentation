# Search Field - Erscheinungsbild

## Grundlayout
Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                              │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **simple** | Einfache Suche |
| **filter** | Mit Filtern |
| **auto-complete** | Mit Vorschlägen |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 150px | inline |
| medium | 250px | Standard |
| large | 350px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | der Rand leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- In Toolbars kann das Feld eingeklappt werden; ein Klick auf das Suchsymbol klappt es auf die
  volle Leistenbreite auf (`expand`).
- Unterhalb einer kleinen Bildschirmbreite (`small`) wird das Feld oberhalb der Liste auf volle
  Breite gesetzt, die Filter wandern hinter eine Schaltfläche zum Ausklappen.
- Die Vorschlagsliste zeigt höchstens acht Zeilen, danach wird gescrollt; Treffer werden
  mit `highlight` markiert.

## Clear-Knopf

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                     [✕]      │
└─────────────────────────────────────────┘
```

## Filter-Overlay

```
┌─────────────────────────────────────────┐
│ 🔍 Suchen…                              │
├─────────────────────────────────────────┤
│  [Filter 1] [Filter 2] [Filter 3]       │
│  [Zurücksetzen]                         │
└─────────────────────────────────────────┘
```

# Rich Text Editor - Appearance

## Base layout
Ein Rich Text Editor ist ein WYSIWYG-Editor für formatierten Text.

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] [ Strikes] [ Color]         │  ← Toolbar
├─────────────────────────────────────────┤
│                                         │
│  (Editor-Bereich)                       │
│                                         │
│  Hier ist der Text...                   │
│                                         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **wysiwyg** | Formatierungsleiste oben, Text wie im Druckbild |
| **wiki-syntax** | Syntaxfeld links, Vorschau rechts (oder als Reiter) |

## Sizes

| Size | Height | Use |
| ------- | ------ | ------------ |
| Small | 200px | Inline |
| Medium | 400px | Standard |
| Large | 600px | Featured |
| Full | 100% | Volle Breite |

## Colours and states

| State | Appearance |
| --------- | ---------- |
| `default` | heller Grund, randloser Textbereich |
| `focus` | Rand in Primärfarbe, Cursor sichtbar |
| `unspeichert` | kleiner Punkt am Rand, Speichern-Knopf hervorgehoben |
| `error` | roter Rand, betroffene Stelle unterstrichen |
| `disabled` | grauer Grund, Leiste ausgegraut |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `border` | the border lights up |
| `shadow` | stronger shadow |

## Responsive

- Die Formatierungsleiste bleibt beim Scrollen oben stehen; passt sie nicht in eine Zeile,
  rutschen weitere Werkzeuge hinter ein ``+``-Aufklappfeld.
- Unter `small` Bildschirmbreite wird die Vorschau von `wiki-syntax` zum Reiter statt
  zur Nebenspalte.
- Der Editorbereich wächst mit dem Text (`auto-resize`), `Full` füllt die Viewport-Höhe
  abzüglich Leiste.

## Toolbar-Buttons

| Button | Function |
| -------- | ---------- |
| **B** | Fett |
| **I** | Kursiv |
| **U** | Unterstrichen |
| ** Strikes** | Durchgestrichen |
| ** Color** | Colour |
| ** Heading** | Überschriften |
| ** List** | Listen |
| ** Link** | Links |
| ** Image** | Bilder |
| ** Code** | Code-Block |

## Placeholder

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] ...                         │
├─────────────────────────────────────────┤
│  Dies ist ein Platzhalter...            │
└─────────────────────────────────────────┘
```

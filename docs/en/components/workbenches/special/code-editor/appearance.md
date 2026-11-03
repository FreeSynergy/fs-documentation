# Code Editor - Appearance

## Base layout
Ein Code Editor ist ein Editor für Quellcode.

```
┌─────────────────────────────────────────┐
│ 1  const greeting = "Hello";            │
│ 2  console.log(greeting);               │
│ 3                                       │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **voll** | Zeilennummern links, Vorschlageliste am Cursor |
| **nur-lesen** | keine Cursor, Kopieren-Knopf oben rechts |
| **vergleich** | zwei Hälften, geänderte Zeilen rot und grün markiert |

## Sizes

| Size | Height | Use |
| ------- | ------ | ------------ |
| Small | 200px | Inline |
| Medium | 400px | Standard |
| Large | 600px | Featured |
| Full | 100% | Volle Breite |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Background** | Dunkel | Dunkles Theme |
| **Text** | Hell | Text-Farbe |
| **Keyword** | Lila | Schlüsselwörter |
| **String** | Orange | Strings |
| **Comment** | Grau | Kommentare |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `line-number` | Zeilennummer hervorheben |
| `cursor` | Cursor ändern |

## Responsive

- Der Editor füllt die Breite; Code bricht nicht um, sondern scrollt waagerecht (`swipe`).
- Unter `small` Bildschirmbreite wird die Vorschlageliste über die Tastatur-blende gesetzt,
  der Zeilennummernblock wird schmaler.
- Die Vergleichsvariante stellt die beiden Hälften untereinander statt nebeneinander,
  die Höhe bleibt pro Hälfte begrenzt.

## Features

| Feature | Description |
| --------- | -------------- |
| **Syntax Highlighting** | Farbige Hervorhebung |
| **Line Numbers** | Zeilennummern |
| **Auto-completion** | Autovervollständigung |
| **Error Detection** | Fehlererkennung |
| **Multiple Cursors** | Mehrere Cursor |

## Themes

| Theme | Description |
| ------- | -------------- |
| **Dark** | Dunkles Theme |
| **Light** | Helles Theme |
| **Custom** | Benutzerdefiniert |

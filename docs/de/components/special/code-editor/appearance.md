# Code Editor - Aussehen

## Grundlayout
Ein Code Editor ist ein Editor für Quellcode.

```
┌─────────────────────────────────────────┐
│ 1  const greeting = "Hello";            │
│ 2  console.log(greeting);               │
│ 3                                       │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **voll** | Zeilennummern links, Vorschlageliste am Cursor |
| **nur-lesen** | keine Cursor, Kopieren-Knopf oben rechts |
| **vergleich** | zwei Hälften, geänderte Zeilen rot und grün markiert |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 200px | Inline |
| Medium | 400px | Standard |
| Large | 600px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | Dunkel | Dunkles Theme |
| **Text** | Hell | Text-Farbe |
| **Keyword** | Lila | Schlüsselwörter |
| **String** | Orange | Strings |
| **Comment** | Grau | Kommentare |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `line-number` | Zeilennummer hervorheben |
| `cursor` | Cursor ändern |

## Features

| Feature | Beschreibung |
|---------|--------------|
| **Syntax Highlighting** | Farbige Hervorhebung |
| **Line Numbers** | Zeilennummern |
| **Auto-completion** | Autovervollständigung |
| **Error Detection** | Fehlererkennung |
| **Multiple Cursors** | Mehrere Cursor |

## Themes

| Theme | Beschreibung |
|-------|--------------|
| **Dark** | Dunkles Theme |
| **Light** | Helles Theme |
| **Custom** | Benutzerdefiniert |

## Reaktiv

- Der Editor füllt die Breite; Code bricht nicht um, sondern scrollt waagerecht (`swipe`).
- Unter `small` Bildschirmbreite wird die Vorschlageliste über die Tastatur-blende gesetzt,
  der Zeilennummernblock wird schmaler.
- Die Vergleichsvariante stellt die beiden Hälften untereinander statt nebeneinander,
  die Höhe bleibt pro Hälfte begrenzt.

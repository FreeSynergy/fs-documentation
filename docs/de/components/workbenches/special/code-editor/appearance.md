# Code-Editor – Aussehen

## Grundlayout
Ein Code-Editor ist ein Editor für Quellcode.

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
| **voll** | Zeilennummern links, Vorschlagsliste am Cursor |
| **nur-lesen** | kein Cursor, Kopieren-Button oben rechts |
| **vergleich** | zwei Hälften, geänderte Zeilen rot und grün markiert |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 200px | inline |
| Medium | 400px | Standard |
| Large | 600px | hervorgehoben |
| Full | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Hintergrund** | dunkel | dunkles Thema |
| **Text** | hell | Textfarbe |
| **Schlüsselwort** | violett | Schlüsselwörter |
| **Zeichenkette** | orange | Zeichenketten |
| **Kommentar** | grau | Kommentare |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `line-number` | hebt die Zeilennummer hervor |
| `cursor` | ändert den Cursor |

## Responsiv

- Der Editor füllt die Breite; Code bricht nicht um, sondern scrollt horizontal (`swipe`).
- Unterhalb der Breite `small` wird die Vorschlagsliste über die Tastatur gelegt, der Block mit den
  Zeilennummern wird schmaler.
- Die Vergleichsvariante stellt die beiden Hälften untereinander statt nebeneinander; die
  Höhe bleibt pro Hälfte begrenzt.

## Funktionen

| Funktion | Beschreibung |
|----------|--------------|
| **Syntax Highlighting** | farbige Hervorhebung |
| **Zeilennummern** | Zeilennummern |
| **Auto-Vervollständigung** | Autovervollständigung |
| **Fehlererkennung** | Fehlererkennung |
| **Mehrfache Cursor** | mehrere Cursor |

## Themes

| Theme | Beschreibung |
|-------|--------------|
| **Dunkel** | dunkles Theme |
| **Hell** | helles Theme |
| **Benutzerdefiniert** | eigenes Theme |

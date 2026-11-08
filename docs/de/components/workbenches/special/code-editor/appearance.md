# Code-Editor – Erscheinungsbild

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

| Variante | Erscheinungsbild |
|---------|------------|
| **voll** | Zeilennummern links, Vorschlagsliste am Cursor |
| **nur-lesen** | kein Cursor, Kopierknopf oben rechts |
| **vergleich** | zwei Hälften, geänderte Zeilen rot und grün markiert |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|-------------|
| Klein | 200px | im Textfluss |
| Mittel | 400px | Standard |
| Groß | 600px | hervorgehoben |
| Voll | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|--------------|--------|----------------------|
| **Hintergrund** | dunkel | dunkles Thema |
| **Text** | hell | Textfarbe |
| **Schlüsselwort** | lila | Schlüsselwörter |
| **Zeichenkette** | orange | Zeichenketten |
| **Kommentar** | grau | Kommentare |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|-------------|-----------------------------|
| `line-number` | hebt die Zeilennummer hervor |
| `cursor` | ändert den Cursor |

## Responsiv

- Der Editor füllt die Breite; Code bricht nicht um, sondern scrollt horizontal (`swipe`).
- Unterhalb der Bildschirmbreite `small` wird die Vorschlagsliste über die Tastatur gelegt, der Zeilennummernbereich wird schmaler.
- Die Vergleichsvariante stellt die beiden Hälften untereinander statt nebeneinander; die
  Höhe bleibt pro Hälfte begrenzt.

## Funktionen

| Funktion | Beschreibung |
|---------------------|---------------------------|
| **Syntax-Highlighting** | farbige Hervorhebung |
| **Zeilennummern** | Zeilennummern |
| **Autovervollständigung** | Autovervollständigung |
| **Fehlererkennung** | Fehlererkennung |
| **Mehrere Cursor** | mehrere Cursor |

## Themes

| Theme | Beschreibung |
|-------|-------------|
| **Dunkel** | dunkles Theme |
| **Hell** | helles Theme |
| **Eigenes** | benutzerdefiniert |

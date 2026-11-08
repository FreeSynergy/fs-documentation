# Rich Text Editor - Erscheinungsbild

## Grundaufbau
Ein Rich-Text-Editor ist ein WYSIWYG-Editor für formatierten Text.

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] [ Durchgestrichen] [ Farbe] │  ← Toolbar
├─────────────────────────────────────────┤
│                                         │
│  (Editorbereich)                        │
│                                         │
│  Hier steht der Text...                 │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **wysiwyg** | Formatierungsleiste oben, Text wie im gedruckten Layout |
| **wiki-syntax** | Syntaxfeld links, Vorschau rechts (oder als Reiter) |

## Größen

| Größe | Höhe | Verwendung |
|------|--------|-------------|
| Klein | 200px | in Textzeilen |
| Mittel | 400px | Standard |
| Groß | 600px | hervorgehoben |
| Voll | 100% | volle Breite |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|-------------|-------------------------------------------------------|
| `default` | heller Grund, Textfläche ohne Rahmen |
| `focus` | Rahmen in der Primärfarbe, Cursor sichtbar |
| `unspeichert` | kleiner Punkt am Rand, Speichern-Schaltfläche hervorgehoben |
| `error` | roter Rahmen, die betroffene Stelle ist unterstrichen |
| `disabled` | grauer Grund, Leiste ausgegraut |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | stärkerer Schatten |

## Responsives Verhalten

- Die Formatierungsleiste bleibt beim Scrollen oben stehen. Passt sie nicht in eine Zeile,
  wandern weitere Werkzeuge hinter ein Aufklappfeld `+`.
- Unterhalb der Breite `small` wird die Vorschau bei `wiki-syntax` zu einem Reiter statt einer
  Seitenspalte.
- Der Editorbereich wächst mit dem Text (`auto-resize`). `Voll` füllt die Bildschirmhöhe
  abzüglich der Leiste.

## Toolbar-Schaltflächen

| Schaltfläche | Funktion |
|------------|--------------------|
| **B** | fett |
| **I** | kursiv |
| **U** | unterstrichen |
| ** Durchgestrichen** | durchgestrichen |
| ** Farbe** | Farbe |
| ** Überschrift** | Überschriften |
| ** Liste** | Listen |
| ** Link** | Links |
| ** Bild** | Bilder |
| ** Code** | Codeblock |

## Platzhalter

```
┌─────────────────────────────────────────┐
│ [B] [I] [U] ...                         │
├─────────────────────────────────────────┤
│  Das ist ein Platzhaltertext...         │
└─────────────────────────────────────────┘
```

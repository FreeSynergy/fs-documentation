# Code Editor (Code-Editor)

| Feld | Wert |
|------|------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `voll`, `nur-lesen`, `vergleich` |
| **Zustände** | `ungespeichert`, `fehler` |
| **Gesten** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animationen** | `highlight`, `fade-in` |
| **Verwandt** | `rich-text-editor`, `textarea`, `whiteboard`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Code Editor ist ein Editor für Quellcode.

## Verwendungszweck

- Code
- Programmierung
- Skripte

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **voll** | bearbeiten mit Hervorhebung, Vervollständigung und Fehlermarkierung |
| **nur-lesen** | hervorgehobener Code zum Ansehen und Kopieren |
| **vergleich** | zwei Versionen nebeneinander, Unterschiede markiert |

## Features

- Syntax Highlighting
- Line Numbers
- Auto-completion
- Error Detection

## Abgrenzung

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): dort entsteht
  formatted Text, hier Quelltext. Wiki-Syntax ist eine Variante des Texteditors, nicht hiervon.
- **Nicht verwechseln mit** [textarea](../../fields/textarea/): ohne Zeilennummern,
  Hervorhebung und Klammerschluss ist es einfach ein Textfeld.
- Ausgabe von Programmen ist keine Editor-Aufgabe — sie gehört in eine Ergebnisanzeige.

## Best Practices

- Sprache immer explizit angeben, sonst fehlt die Hervorhebung und die Einrückung ist falsch.
- `Tab` rückt ein; zum Verlassen des Editors `Esc` oder `Strg+Tab` anbieten.
- Zeilennummern und horizontales Lineal erst ab mehrzeiligem Inhalt.
- Ungespeicherte Änderungen deutlich markieren, Schließen rückfragen.
- Shortcuts an der üblichen Stelle dokumentieren (`Strg+/`, `Strg+F`, `Strg+D`).

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — formatierter Text
- [Whiteboard](../whiteboard/) — Skizzen statt Code
- [Basiskomponente](../../basics/base/)

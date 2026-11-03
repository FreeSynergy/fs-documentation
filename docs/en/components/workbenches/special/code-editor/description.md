# Code Editor

| Field | Value |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `voll`, `nur-lesen`, `vergleich` |
| **States** | `ungespeichert`, `fehler` |
| **Gestures** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animations** | `highlight`, `fade-in` |
| **Related** | `rich-text-editor`, `textarea`, `whiteboard`, `dashboard` |
| **State** | documented |

## Description
Ein Code Editor ist ein Editor für Quellcode.

## Purpose

- Code
- Programmierung
- Skripte

## Variants

| Variant | Description |
| ---------- | -------------- |
| **voll** | bearbeiten mit Hervorhebung, Vervollständigung und Fehlermarkierung |
| **nur-lesen** | hervorgehobener Code zum Ansehen und Kopieren |
| **vergleich** | zwei Versionen nebeneinander, Unterschiede markiert |

## Features

- Syntax Highlighting
- Line Numbers
- Auto-completion
- Error Detection

## Distinction

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): dort entsteht
  formatted Text, hier Quelltext. Wiki-Syntax ist eine Variante des Texteditors, nicht hiervon.
- **Nicht verwechseln mit** [textarea](../../../primitives/fields/textarea/): ohne Zeilennummern,
  Hervorhebung und Klammerschluss ist es einfach ein Textfeld.
- Ausgabe von Programmen ist keine Editor-Aufgabe — sie gehört in eine Ergebnisanzeige.

## Best Practices

- Sprache immer explizit angeben, sonst fehlt die Hervorhebung und die Einrückung ist falsch.
- `Tab` rückt ein; zum Verlassen des Editors `Esc` oder `Strg+Tab` anbieten.
- Zeilennummern und horizontales Lineal erst ab mehrzeiligem Inhalt.
- Ungespeicherte Änderungen deutlich markieren, Schließen rückfragen.
- Shortcuts an der üblichen Stelle dokumentieren (`Strg+/`, `Strg+F`, `Strg+D`).

## See also

- [special – overview](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — formatierter Text
- [Whiteboard](../whiteboard/) — Skizzen statt Code
- [Base component](../../../primitives/basics/base.md)

# Code-Editor

| Feld | Wert |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `voll`, `nur-lesen`, `vergleich` |
| **States** | `ungespeichert`, `fehler` |
| **Gestures** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animations** | `highlight`, `fade-in` |
| **Related** | `rich-text-editor`, `textarea`, `whiteboard`, `dashboard` |
| **Status** | documented |

## Beschreibung
Ein Code-Editor ist ein Editor für Quellcode.

## Zweck

- Code
- Programmierung
- Skripte

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **voll** | Bearbeiten mit Hervorhebung, Vervollständigung und Fehlermarkierung |
| **nur-lesen** | hervorgehobener Code zum Ansehen und Kopieren |
| **vergleich** | zwei Versionen nebeneinander, Unterschiede markiert |

## Funktionen

- Syntax Highlighting
- Zeilennummern
- Auto-Vervollständigung
- Fehlererkennung

## Abgrenzung

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): Dort entsteht
  formatierter Text, hier Quellcode. Wiki-Syntax ist eine Variante des Texteditors, nicht dieses Editors.
- **Nicht verwechseln mit** [textarea](../../../primitives/fields/textarea/): Ohne Zeilennummern,
  Hervorhebung und automatisches Schließen von Klammern ist es einfach ein Textfeld.
- Die Ausgabe von Programmen ist keine Editor-Aufgabe – sie gehört in eine Ergebnisansicht.

## Best Practices

- Immer die Sprache ausdrücklich angeben, sonst fehlen die Hervorhebung und die richtige Einrückung.
- `Tab` rückt ein; biete `Esc` oder `Strg+Tab` an, um den Editor zu verlassen.
- Zeilennummern und ein waagerechtes Lineal erst ab mehrzeiligem Inhalt.
- Ungespeicherte Änderungen deutlich kennzeichnen und vor dem Schließen nachfragen.
- Tastenkürzel an der üblichen Stelle dokumentieren (`Strg+/`, `Strg+F`, `Strg+D`).

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — formatierter Text
- [Whiteboard](../whiteboard/) — Skizzen statt Code
- [Basiskomponente](../../../primitives/basics/base.md)

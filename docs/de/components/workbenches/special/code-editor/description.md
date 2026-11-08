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

- Syntax-Highlighting
- Zeilennummern
- Autovervollständigung
- Fehlererkennung

## Abgrenzung

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): dort entsteht formatierter
  Text, hier Quellcode. Wiki-Syntax ist eine Variante des Texteditors, nicht dieses hier.
- **Nicht verwechseln mit** [textarea](../../../primitives/fields/textarea/): ohne Zeilennummern,
  Hervorhebung und automatisches Schließen von Klammern ist es nur ein Textfeld.
- Die Ausgabe von Programmen ist keine Aufgabe des Editors – sie gehört in eine Ergebnisansicht.

## Best Practices

- Immer die Sprache ausdrücklich angeben, sonst fehlen Hervorhebung und Einrückung.
- `Tab` rückt ein; biete `Esc` oder `Ctrl+Tab` an, um den Editor zu verlassen.
- Zeilennummern und ein horizontales Lineal erst ab mehrzeiligem Inhalt.
- Ungespeicherte Änderungen deutlich kennzeichnen und vor dem Schließen nachfragen.
- Tastenkürzel an der üblichen Stelle dokumentieren (`Ctrl+/`, `Ctrl+F`, `Ctrl+D`).

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich-Text-Editor](../../fields/rich-text-editor/) — formatierter Text
- [Whiteboard](../whiteboard/) — Skizzen statt Code
- [Basiskomponente](../../../primitives/basics/base.md)

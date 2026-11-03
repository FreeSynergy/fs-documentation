# Hover Card

| Field | Value |
| ------ | ------ |
| **Category** | `overlays` |
| **Inherits from** | `base`, `popover` |
| **Variants** | `profil`, `dokument`, `vorschau` |
| **States** | `open`, `loading` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `tooltip`, `popover`, `avatar` |
| **Role** | `tooltip` |
| **State** | documented |

## Description

Die Vorschaukarte zeigt zu einem Verweis die wichtigsten Informationen zum Ziel —
ohne die Adresse zu wechseln. Sie erscheint bei Zeiger über dem Verweis und verschwindet
wieder, wenn der Zeiger abzieht.

## Purpose

- Profilvorschau, wenn ein Name in einem Chat oder einer Liste angetippt wird
- Kurzfassung eines Wiki-Artikels oder einer Aufgabe beim Überfahren des Verweises
- Zieladresse eines externen Verweises lesbar machen

## Variants

| Variant | Description |
| ---------- | -------------- |
| **profil** | Avatar, Name, Rolle, letzte Aktivität |
| **dokument** | Titel, Auszug, Bearbeiter, Änderungsdatum |
| **vorschau** | Bild oder erstes Element des Zieles |

## Features

- Inhalt wird nach einer Verzögerung geladen, nicht beim ersten Drauffahren
- Karte bleibt offen, wenn der Zeiger in die Karte wandelt (Inhalt ist bedienbar)
- Auf Touch-Geräten erscheint die Karte nach Langdruck, schließt mit `Esc` oder Tippen

## Distinction

- **Nicht verwechseln mit** [tooltip](../tooltip/): ein Tooltip erklärt ein Bedienelement
  in einem Satz, die Karte zeigt Inhalt.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover enthält Aktionen,
  die Karte zeigt eine Zusammenfassung.

## Best Practices

- Höchstens fünf Informationen pro Karte.
- Kein Scrollen in der Karte; wer alles lesen will, folgt dem Verweis.
- Karten nicht in Listen mit vielen Zeilen gleichzeitig laden.

## See also

- [Tooltip](../tooltip/)
- [Popover](../popover/)
- [Base component](../../../primitives/basics/base.md)

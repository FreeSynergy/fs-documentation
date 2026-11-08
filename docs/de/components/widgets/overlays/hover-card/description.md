# Hover Card

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base`, `popover` |
| **Varianten** | `profil`, `dokument`, `vorschau` |
| **Zustände** | `open`, `loading` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `fade-in`, `expand` |
| **Verwandt** | `tooltip`, `popover`, `avatar` |
| **Rolle** | `tooltip` |
| **Status** | dokumentiert |

## Beschreibung

Die Vorschaukarte zeigt die wichtigsten Informationen zum Ziel eines Verweises —
ohne die Adresse zu verändern. Sie erscheint, wenn der Zeiger über dem Verweis liegt,
und verschwindet wieder, wenn der Zeiger weggeht.

## Verwendungszweck

- Profilvorschau, wenn in einem Chat oder einer Liste ein Name angetippt wird
- Kurzfassung eines Wiki-Artikels oder einer Aufgabe beim Überfahren des Verweises
- Lesbar machen der Zieladresse eines externen Verweises

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **profil** | Avatar, Name, Rolle, letzte Aktivität |
| **dokument** | Titel, Auszug, Bearbeiter, Änderungsdatum |
| **vorschau** | Bild oder erstes Element des Ziels |

## Funktionen

- Der Inhalt wird nach einer Verzögerung geladen, nicht schon beim ersten Überfahren
- Die Karte bleibt offen, wenn der Zeiger in die Karte wechselt (der Inhalt ist bedienbar)
- Auf Touch-Geräten erscheint die Karte nach einem langen Drücken, schließt mit `Esc` oder einem Tippen

## Abgrenzung

- **Nicht verwechseln mit** [tooltip](../tooltip/): ein Tooltip erklärt ein Bedienelement in einem
  Satz, die Karte zeigt Inhalt.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover enthält Aktionen, die Karte zeigt
  eine Zusammenfassung.

## Best Practices

- Höchstens fünf Informationen pro Karte.
- Kein Scrollen in der Karte; wer alles lesen will, folgt dem Verweis.
- Lade in Listen mit vielen Zeilen nicht gleichzeitig alle Karten.

## Siehe auch

- [Tooltip](../tooltip/)
- [Popover](../popover/)
- [Basiskomponente](../../../primitives/basics/base.md)

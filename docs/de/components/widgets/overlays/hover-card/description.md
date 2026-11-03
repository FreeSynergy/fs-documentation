# Hover Card (Vorschaukarte)

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

Die Vorschaukarte zeigt zu einem Verweis die wichtigsten Informationen zum Ziel —
ohne die Adresse zu wechseln. Sie erscheint bei Zeiger über dem Verweis und verschwindet
wieder, wenn der Zeiger abzieht.

## Verwendungszweck

- Profilvorschau, wenn ein Name in einem Chat oder einer Liste angetippt wird
- Kurzfassung eines Wiki-Artikels oder einer Aufgabe beim Überfahren des Verweises
- Zieladresse eines externen Verweises lesbar machen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **profil** | Avatar, Name, Rolle, letzte Aktivität |
| **dokument** | Titel, Auszug, Bearbeiter, Änderungsdatum |
| **vorschau** | Bild oder erstes Element des Zieles |

## Features

- Inhalt wird nach einer Verzögerung geladen, nicht beim ersten Drauffahren
- Karte bleibt offen, wenn der Zeiger in die Karte wandelt (Inhalt ist bedienbar)
- Auf Touch-Geräten erscheint die Karte nach Langdruck, schließt mit `Esc` oder Tippen

## Abgrenzung

- **Nicht verwechseln mit** [tooltip](../tooltip/): ein Tooltip erklärt ein Bedienelement
  in einem Satz, die Karte zeigt Inhalt.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover enthält Aktionen,
  die Karte zeigt eine Zusammenfassung.

## Best Practices

- Höchstens fünf Informationen pro Karte.
- Kein Scrollen in der Karte; wer alles lesen will, folgt dem Verweis.
- Karten nicht in Listen mit vielen Zeilen gleichzeitig laden.

## Siehe auch

- [Tooltip](../tooltip/)
- [Popover](../popover/)
- [Basiskomponente](../../basics/base/)

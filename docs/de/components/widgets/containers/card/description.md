# Card

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `flach`, `umrandet`, `medien` |
| **Zustände** | `selected` |
| **Gesten** | `tap`, `drag`, `long-press` |
| **Animationen** | `lift`, `fade-in`, `stagger` |
| **Verwandt** | `panel`, `grid-view`, `list-view`, `hover-card`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Die Card (Karte) ist ein Container-Element, das Inhalte in einer strukturierten Box mit Titel, Inhalt und optionalen Aktionen darstellt. Wird häufig in Dashboards, Listen und Grid-Layouts verwendet.

## Verwendungszweck

- Gruppierung zusammengehöriger Informationen
- Visuelle Trennung von Inhalten
- Anzeige von Mini-Übersichten (z.B. Kunde, Aufgabe, Nachricht)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | leichte Erhebung, weicher Rand |
| **flach** | ohne Schatten, nur Flächenfarbe |
| **umrandet** | dünner Rand, kein Schatten |
| **medien** | Bild- oder Medienbereich über oder neben dem Inhalt |

## Features

- Kopf mit Titel und maximal zwei Aktionen
- Medien-, Inhalts- und Fußbereich sind optional
- Auswahl- und Verschiebezustand (in Rastern und Dashboards)
- Einklappbar bei langen Karten

## Abgrenzung

- **Nicht verwechseln mit** [panel](../panel/): das Panel fasst Bedienelemente oder einen
  Arbeitsbereich zusammen, die Karte stellt **einen** Inhalt mit Titel und Aktionen dar.
- **Nicht verwechseln mit** einer Zeile in [list-view](../../data/list-view/): die Zeile ist kompakt
  und gleichförmig, die Karte frei aufgebaut.
- **Nicht verwechseln mit** [hover-card](../../overlays/hover-card/): die Vorschaukarte ist ein Overlay.
- **Nicht verwechseln mit** [grid-view](../../data/grid-view/): das Raster ordnet Karten, es ist
  nicht die Karte selbst.

## Best Practices

- Eine Karte, ein Thema; höchstens drei Aktionen, eine davon deutlich.
- Titel kurz halten, Untertitel für den Kontext, beides nicht vertauschen.
- Karten in Serien gleich hoch bauen; zu lange Texte kürzen statt umbrechen lassen.
- Klickbare Karten brauchen eine deutliche Rückmeldung und eine Tastaturalternative.

## Typische Inhalte

- Titel/Überschrift
- Textinhalt
- Icons/Emojis
- Buttons/Aktionen
- Bilder/Thumbnails
- Status-Badges

## Siehe auch

- [containers – Übersicht](../index.md)
- [Panel](../panel/) — Rahmen für Bedienung
- [Grid View](../../data/grid-view/) — Karten anordnen
- [Basiskomponente](../../basics/base/)

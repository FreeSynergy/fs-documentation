# Card (Karte)

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
Die Card ist ein Container-Element. Es zeigt Inhalte in einem strukturierten Kasten
mit Titel, Inhalt und optionalen Aktionen. Oft wird sie in Dashboards, Listen und
Rasterlayouts genutzt.

## Verwendungszweck

- Zusammengehörige Informationen gruppieren
- Inhalte optisch trennen
- Kleine Übersichten zeigen (z. B. Kunde, Aufgabe, Nachricht)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | leichte Erhöhung, weiche Kante |
| **flach** | kein Schatten, nur die Flächenfarbe |
| **umrandet** | dünner Rahmen, kein Schatten |
| **medien** | Bild- oder Medienbereich über oder neben dem Inhalt |

## Funktionen

- Eine Kopfzeile mit Titel und höchstens zwei Aktionen
- Medien-, Inhalts- und Fußbereich sind optional
- Zustand „ausgewählt“ und Ziehen (in Rastern und Dashboards)
- Einklappbar bei langen Karten

## Abgrenzung

- **Nicht verwechseln mit** [panel](../panel/): Das Panel fasst Bedienelemente oder einen
  Arbeitsbereich zusammen. Die Card zeigt **einen** Inhalt mit Titel und Aktionen.
- **Nicht verwechseln mit** einer Zeile in [list-view](../../data/list-view/): Die Zeile ist kompakt
  und gleichförmig, die Card frei gestaltet.
- **Nicht verwechseln mit** [hover-card](../../overlays/hover-card/): Die Vorschau-Karte ist ein Overlay.
- **Nicht verwechseln mit** [grid-view](../../data/grid-view/): Das Raster ordnet Cards an. Es ist
  nicht die Card selbst.

## Best Practices

- Eine Card, ein Thema. Höchstens drei Aktionen, davon eine hervorgehoben.
- Den Titel kurz halten. Den Untertitel für Kontext nutzen, die beiden nicht vertauschen.
- Cards in einer Reihe auf gleiche Höhe bringen. Zu lange Texte eher kürzen als umbrechen lassen.
- Klickbare Cards brauchen eine klare Rückmeldung und eine Tastaturalternative.

## Typischer Inhalt

- Titel und Überschrift
- Textinhalt
- Icons und Emojis
- Buttons und Aktionen
- Bilder und Vorschaubilder
- Status-Badges

## Siehe auch

- [containers – Übersicht](../index.md)
- [Panel](../panel/) — Rahmen für Bedienelemente
- [Grid View](../../data/grid-view/) — Anordnen von Cards
- [Base-Komponente](../../../primitives/basics/base.md)

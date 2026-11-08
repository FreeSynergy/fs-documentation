# Skeleton

## Beschreibung

Skeleton zeigt beim Laden statische Platzhalterformen im Layout des späteren Inhalts – Balken, Kreise und Blöcke mit einem wandernden Schimmer. Der Nutzer erkennt die kommende Struktur, bevor die Daten da sind, und das Layout springt nicht, wenn der echte Inhalt erscheint.

## Verwendung

- Listenansichten, bevor die ersten Daten eintreffen, siehe [list-view](../../../../components/widgets/data/list-view/description.md)
- Rasteransichten beim Nachladen, siehe [grid-view](../../../../components/widgets/data/grid-view/description.md)
- Tabellen, während die Seite aufgebaut wird, siehe [table](../../../../components/widgets/data/table/description.md)
- Detailseiten und Karten, die asynchron gefüllt werden
- Ladezustände: ein Ersatz für den Spinner, wenn das Layout des Inhalts bekannt ist

## Dauer

- Typisch: 1200–1800 ms pro Schimmerzyklus

## Unterschied zu Progress und Glow

- Progress: zeigt einen messbaren Wert (z. B. 40 %). Skeleton sagt nichts darüber, wie weit das Laden ist.
- Glow: ein Leuchten als Statussignal (Auswahl, Live). Skeleton ist ein Platzhalter, der verschwindet, sobald echter Inhalt da ist.

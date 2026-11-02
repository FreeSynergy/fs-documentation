# Kombinations-Gesten (combined)

Kombinations-Gesten setzen sich aus einfachen Gesten zusammen oder entstehen
aus dem Zusammenspiel von Geste und Kontext (Liste, Liste + Zeit). Sie werden
eigenständig dokumentiert, weil sie eigene Attribute und Abbruchregeln haben.

## Elemente

- **pull-to-refresh** - Ziehen nach unten an der Listen-Obergrenze (Aktualisieren)
- **drag-and-drop** - Greifen, Ziehen, Ablegen auf Ablagezone (Verschieben)

## Zuordnung

| Situation | Geste |
|-----------|-------|
| Inhalt neu laden | pull-to-refresh |
| Element an anderen Ort bringen | drag-and-drop |
| Reihenfolge ändern | drag-and-drop (mit Reorder-Animation) |

## Barrierefreiheit

Nach WCAG 2.5.7 (Dragging Movements) braucht jede Drag-Interaktion eine
Einzelzeiger-Alternative (Buttons „Nach oben/Nach unten“, Auswählen +
Einfügen). `pull-to-refresh` immer durch expliziten Aktualisieren-Button
ergänzen.

## Siehe auch

- [Gesten Übersicht](../index.md)
- [Drag](../single/drag/description.md) - Basisgeste von drag-and-drop
- [Reorder-Animation](../../animations/transition/reorder/description.md) - Antwort auf Drag-and-drop

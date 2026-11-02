# Drag and Drop - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `draggable` | boolean | `false` | Element darf gegriffen werden |
| `onDragStart` | function | - | Greifen (Long Press/Instant) erkannt |
| `onDrag` | function | - | Bewegung während des Ziehens |
| `onDrop` | function | - | Loslassen in gültiger Ablagezone |
| `onDragEnd` | function | - | Ziehen beendet (gültig oder abgebrochen) |

## Ziel-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `dropZones` | string[] | `[]` | Erlaubte Ablagen (`self`, `list`, `trash`, …) |
| `onDragEnter` | function | - | Drag betritt eine Zone |
| `onDragLeave` | function | - | Drag verlässt eine Zone |
| `onDragOver` | function | - | Bewegung über einer Zone (Position für Insert) |
| `dataTransfer` | object | - | Daten des Drags ( MIME, Payload ) |

## Greif-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `grabMethod` | string | `long-press` \| `instant` \| `handle` | Wie wird gegriffen? |
| `longPressThreshold` | number | `300` | Haltezeit zum Greifen in ms |
| `liftThreshold` | number | `10` | Bewegung in px bis Drag als gestartet gilt |
| `dragAxis` | string | `x` \| `y` \| `xy` | Erlaubte Zugrichtung |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `dragImage` | node \| auto | `auto` | Vorschau beim Ziehen |
| `ghostAtOrigin` | boolean | `true` | Halbdunkler Platzhalter an Startposition? |
| `targetHighlight` | boolean | `true` | Ablagezone hervorheben? |
| `insertIndicator` | boolean | `true` | Einfügelinie zwischen Elementen? |
| `hapticFeedback` | boolean | `true` | Vibration bei Greifen/Ablegen? |
| `dropAnimation` | string | `settle` \| `fly` \| `none` | Einlager-Animation |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Auf/Ab-Buttons oder Ausschneiden/Einfügen (WCAG 2.5.7) |
| `keyboardDrag` | boolean | `false` | Leertaste zum Greifen, Pfeile zum Ablegen? |
| `announceDrop` | boolean | `true` | Ablage per Screenreader ansagen |

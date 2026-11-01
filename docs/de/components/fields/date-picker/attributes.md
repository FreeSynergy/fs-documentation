# Date Picker (Datumsauswahl) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | date | `null` | gewähltes Datum |
| `rangeStart` | date | `null` | Beginn des Bereichs |
| `rangeEnd` | date | `null` | Ende des Bereichs |
| `entries` | array[] | `[]` | Einträge für das sichtbare Fenster (vom Aufrufer geliefert) |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `min` | date | `null` | frühestes wählbares Datum |
| `max` | date | `null` | spätestes wählbares Datum |
| `firstDayOfWeek` | number | `1` | Montag = 1, Sonntag = 0 |
| `quickPick` | array[] | `[heute, morgen]` | Schnellauswahl unter dem Raster |
| `closeOnSelect` | boolean | `true` | nach der Auswahl schließen |

## Datenanbindung

Ohne `sources` ist der Wähler ein reiner Kalender. Mit `sources` liest er den
Datenbestand über das Muster in [Daten-API](../../../data/api.md).

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `sources` | array[] | `[]` | Modelle mit Datumsbezug, je als Name (`events`) oder als Objekt (`resource`, `dateField`, `filter`) |
| `dateField` | string | `start` | Feld, das den Tag liefert: `start`, `dueAt`, `createdAt`, …; pro Quelle überschreibbar |
| `endField` | string | `end` | Feld für das Ende, für mehrtägige Einträge |
| `titleField` | string | `title` | Feld für den Titel in der Tagesliste |
| `typeField` | string | `type` | Feld für die Zuordnung zu einem Eintragstyp |
| `filter` | string | `null` | Filter nach API-Muster, z. B. `status:eq:open;assigneeId:eq:user_01HZXA` |
| `scopeId` | reference | `null` | auf einen Kalender, ein Board oder ein Projekt eingrenzen |
| `loadWindow` | number | `1` | Monate über das sichtbare Fenster hinaus, die mitgeladen werden |
| `entryLimit` | number | `4` | Einträge pro Tag, danach „+ n weitere“ |
| `showEntries` | enum | `beides` | `aus`, `punkte`, `liste`, `beides` |
| `autoReload` | boolean | `true` | folgt `updatedSince` bzw. Webhooks des geladenen Fensters |

## Schreiben

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `creatable` | boolean | `false` | Schnellaufnahme im Overlay anbieten (`POST`) |
| `createFields` | array[] | `[title, start, end]` | Felder der Schnellaufnahme, ein Pflichtfeld genügt |
| `movable` | boolean | `false` | Eintrag per Ziehen auf einen anderen Tag verschieben (`PATCH`) |
| `editable` | boolean | `false` | Eintrag aus der Tagesliste heraus bearbeiten |
| `deletable` | boolean | `false` | Eintrag aus der Tagesliste löschen (Soft-Delete) |
| `confirmDelete` | boolean | `true` | vor dem Löschen [alert-dialog](../../overlays/alert-dialog/) zeigen |

## Eintragsobjekt

Ein Eintrag in `entries` folgt den [Standardfeldern](../../../data/felder.md).

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | reference | ID des Datensatzes in der Quelle |
| `title` | string | Titel in der Tagesliste |
| `start` | datetime | Beginn; der Wert kommt aus `dateField` |
| `end` | datetime | Ende; fehlt, gilt ein Tag |
| `allDay` | boolean | Termin ohne Uhrzeit |
| `type` | enum | `event`, `task`, `document`, … — bestimmt die Marke |
| `color` | string \| null | eigener Farbakzent, sonst nach `type` |
| `done` | boolean | erledigt (Aufgaben), gedämpfte Darstellung |
| `recurrenceRule` | string \| null | RRULE nach RFC 5545, Serie mit Unterbrechung am Punkt |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onChange` | function | Datum oder Bereich geändert |
| `onMonthChange` | function | angezeigter Monat gewechselt, lädt das Fenster nach |
| `onEntriesLoad` | function | Einträge eines Fensters sind geladen |
| `onEntryClick` | function | Eintrag in der Tagesliste geöffnet |
| `onEntryCreate` | function | Eintrag aus der Schnellaufnahme gespeichert |
| `onEntryUpdate` | function | Eintrag aus der Tagesliste geändert |
| `onEntryMove` | function | Eintrag auf einen anderen Tag gezogen |
| `onEntryDelete` | function | Eintrag aus der Tagesliste gelöscht |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` mit `grid` im Raster, Zellen `gridcell` |
| `aria-selected` | boolean | markiert den gewählten Tag |
| `label` | string | Pflicht, z. B. „Termin“ |
| `aria-label` (Tag) | string | Tag nennt Datum und Einträge, z. B. „14. Oktober, 3 Einträge“ |
| `role` (Tagesliste) | string | `list` mit `listitem`, Einträge zusätzlich `button` |
| `aria-busy` | boolean | `true`, während das Fenster nachgeladen wird |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)

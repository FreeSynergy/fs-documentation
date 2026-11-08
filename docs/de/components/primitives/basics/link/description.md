# Link

| Feld | Wert |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `muted`, `icon`, `unterstrichen` |
| **States** | `visited`, `current` |
| **Gestures** | `tap` |
| **Animations** | `highlight` |
| **Related** | `button`, `breadcrumb`, `tabs`, `base` |
| **Status** | documented |

## Beschreibung

Ein Link ändert die Adresse – er führt zu einer anderen Seite, einem anderen Objekt oder einer
Stelle innerhalb der aktuellen Ansicht. Er ist das Navigationselement schlechthin.

## Zweck

- Verzweigung zwischen Objekten (Wiki-Artikel, Kontakte, Aufgaben)
- Externe Verweise auf Webseiten und Dateien
- Sprungmarken innerhalb langer Dokumente

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **standard** | Text in der Primärfarbe, bei Hover unterstrichen |
| **muted** | Sekundärfarbe, für Fußzeilen und Metazeilen |
| **icon** | Icon vor oder nach dem Text (z. B. ein Pfeil nach außen) |
| **unterstrichen** | durchgehend unterstrichen (im Fließtext) |

## Funktionen

- `external` öffnet einen neuen Tab und kennzeichnet das sichtbar
- Download-Verweise als eigener Fall (`download`)
- Markierung des aktuellen Ziels in der Navigation (`aria-current`)

## Abgrenzung

- **Nicht verwechseln mit** [button](../../actions/button/): ein Button löst eine
  Aktion aus, ohne die Adresse zu ändern.

- **Nicht verwechseln mit** [breadcrumb](../../../widgets/navigation/breadcrumb/): der
  Breadcrumb zeigt einen Pfad, seine Einträge sind Links.

- **Nicht verwechseln mit** [tabs](../../../widgets/navigation/tabs/): Tabs wechseln eine
  Ansicht innerhalb derselben Seite.

## Best Practices

- Der Linktext muss ohne Kontext eindeutig sein („Datenschutzerklärung“, nicht „hier“).
- Im Fließtext immer unterstreichen.
- Externe Links zusätzlich im Text oder mit Icon plus `aria-label` kennzeichnen.
- Links nur mit Icon sind nicht erlaubt.

## Siehe auch

- [Button](../../actions/button/)
- [Breadcrumb](../../../widgets/navigation/breadcrumb/)
- [Basiskomponente](../base.md)

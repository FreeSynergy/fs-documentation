# Link (Verweis)

| Feld | Wert |
|------|------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `muted`, `icon`, `unterstrichen` |
| **Zustände** | - |
| **Gesten** | - |
| **Animationen** | - |
| **Verwandt** | `button`, `breadcrumb`, `tabs`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Link wechselt die Adresse – er führt zu einer anderen Seite, einem
anderen Objekt oder einer Stelle innerhalb der aktuellen Ansicht.
Er ist das Navigationselement schlechthin.

## Verwendungszweck

- Verzweigung zwischen Objekten (Wiki-Artikel, Kontakte, Aufgaben)
- Externe Verweise auf Webseiten und Dateien
- Sprungmarken innerhalb langer Dokumente

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Text in Primärfarbe, Unterstreichung bei Hover |
| **muted** | Sekundärfarbe, für Fußzeilen und Metazeilen |
| **icon** | Icon vor oder nach dem Text (z. B. Extern-Pfeil) |
| **unterstrichen** | durchgehend unterstrichen (in Fließtext) |

## Features

- `external` öffnet neuen Tab und kennzeichnet das sichtbar
- Download-Verweise als eigener Fall (`download`)
- Kennzeichnung des aktuellen Ziels bei der Navigation (`aria-current`)

## Abgrenzung

- **Nicht verwechseln mit** [button](../../actions/button/): ein Button löst
  eine Aktion ohne Adresswechsel aus.

- **Nicht verwechseln mit** [breadcrumb](../../navigation/breadcrumb/): der
  Breadcrumb zeigt einen Pfad, seine Einträge sind Links.

- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs wechseln eine
  Ansicht innerhalb derselben Seite.

## Best Practices

- Linktext eindeutig ohne Kontext („Datenschutzbestimmungen“, nicht „hier“).
- In Fließtext immer unterstrichen.
- Externe Links zusätzlich im Text oder per Icon mit `aria-label` kennzeichnen.
- Icon-only-Links sind nicht zulässig.

## Siehe auch

- [Button](../../actions/button/)
- [Breadcrumb](../../navigation/breadcrumb/)
- [Basiskomponente](../base/)

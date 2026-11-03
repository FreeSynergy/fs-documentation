# Progress (Fortschrittsanzeige)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `linear`, `circular`, `mit-label`, `unbestimmt` |
| **Zustände** | `indeterminate`, `completed` |
| **Gesten** | keine — reine Anzeige |
| **Animationen** | `progress`, `pulse` |
| **Verwandt** | `spinner`, `slider`, `skeleton`, `toast`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Eine Progress-Anzeige zeigt, wie weit eine begonnene Aktion fortgeschritten ist –
oder dass sie läuft, ohne dass der Wert bekannt ist.

## Verwendungszweck

- Dateitransfers, Import/Export, Generierung von Berichten
- Rückmeldung bei mehrstufigen Aktionen (Wizard-Schritte)
- Kapazitätsanzeige (Speicher, Kontingent)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **linear** | Balken von links nach rechts |
| **circular** | Kreisring, für kompakte Flächen |
| **mit-label** | Prozentwert oder Text über bzw. im Balken |
| **unbestimmt** | Animation ohne Wert, wenn die Dauer unbekannt ist |

## Features

- frei konfigurierbarer Wertebereich (`min`/`max`)
- Farbumschaltung bei Erfolg oder Fehler
- Weiche Wertänderung statt Sprung

## Abgrenzung

- **Nicht verwechseln mit** [spinner](../spinner/): ein Spinner zeigt keine
  Fortschrittsmenge an.

- **Nicht verwechseln mit** [slider](../../fields/slider/): ein Slider ist eine
  **Eingabe**, Progress ist reine Anzeige.

- **Nicht verwechseln mit** [skeleton](../skeleton/): Skeleton zeigt ein Layout,
  Progress eine begonnene Aktion.

## Best Practices

- Unbestimmte Anzeige nur, wenn ein Wert wirklich nicht ermittelbar ist.
- Fortschritt niemals als einzige Rückmeldung lassen – am Ende eine Meldung
  ([toast](../toast/)).

- Wert in Prozent nur anzeigen, wenn er aussagekräftig ist („3 von 10 Dateien“
  ist besser als „30 %“).

## Siehe auch

- [Spinner](../spinner/)
- [Skeleton](../skeleton/)
- [Toast](../toast/)
- [Basiskomponente](../../basics/base/)

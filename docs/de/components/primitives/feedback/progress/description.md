# Progress (Fortschrittsanzeige)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `linear`, `circular`, `mit-label`, `unbestimmt` |
| **Zustände** | `indeterminate`, `completed` |
| **Gesten** | keine – nur Anzeige |
| **Animationen** | `progress`, `pulse` |
| **Verwandt** | `spinner`, `slider`, `skeleton`, `toast`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Eine Fortschrittsanzeige zeigt, wie weit eine gestartete Aktion ist. Oder sie zeigt,
dass sie läuft, ohne dass der Wert bekannt ist.

## Verwendungszweck

- Dateiübertragungen, Import und Export, Erstellen von Berichten
- Rückmeldung bei mehrstufigen Aktionen (Schritte eines Assistenten)
- Anzeige von Kapazität (Speicher, Kontingent)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **linear** | Balken von links nach rechts |
| **circular** | Ring, für kompakte Flächen |
| **mit-label** | Prozentwert oder Text über oder im Balken |
| **unbestimmt** | Animation ohne Wert, wenn die Dauer unbekannt ist |

## Funktionen

- Frei konfigurierbarer Wertebereich (`min`/`max`)
- Die Farbe wechselt bei Erfolg oder Fehler
- Sanfte Wertänderung statt eines Sprungs

## Abgrenzung

- **Nicht verwechseln mit** [spinner](../spinner/): Ein Spinner zeigt keinen Fortschritt
  in Zahlen.

- **Nicht verwechseln mit** [slider](../../fields/slider/): Ein Slider ist eine
  **Eingabe**. Progress dient nur der Anzeige.

- **Nicht verwechseln mit** [skeleton](../skeleton/): Ein Skeleton zeigt einen Aufbau,
  Progress eine gestartete Aktion.

## Best Practices

- Die unbestimmte Anzeige nur nutzen, wenn sich ein Wert wirklich nicht bestimmen lässt.
- Fortschritt nie als einzige Rückmeldung lassen. Am Ende eine Meldung zeigen
  ([toast](../toast/)).

- Den Wert nur dann in Prozent zeigen, wenn er aussagekräftig ist („3 von 10 Dateien“
  ist besser als „30 %“).

## Siehe auch

- [Spinner](../spinner/)
- [Skeleton](../skeleton/)
- [Toast](../toast/)
- [Base-Komponente](../../basics/base.md)

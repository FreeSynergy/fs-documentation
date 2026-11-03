# Pagination (Seitennavigation)

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `zahlen`, `vor-zurueck`, `nachladen`, `endlos` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `progress` |
| **Verwandt** | `repeater`, `list-view`, `table`, `scroll-area`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Seitennavigation teilt eine lange Liste in Portionen und bietet den Wechsel zwischen ihnen.

## Verwendungszweck

- Große Datenmengen übersichtlich darstellen
- Performance verbessern (nur sichtbare Daten laden)
- Benutzerfreundlichkeit erhöhen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zahlen** | Seitenzahlen mit aktueller Seite und `…` |
| **vor-zurueck** | nur vorherige und nächste Seite |
| **nachladen** | angehängte Portion auf Knopfdruck |
| **endlos** | Portion lädt automatisch beim Erreichen des listenendes |

## Features

- Total Items (Gesamtanzahl)
- Current Page (aktuelle Seite)
- Items per Page (Elemente pro Seite)
- Jump to Page (direkt zu Seite springen)
- Page Size Selector (Anzahl pro Seite ändern)

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln den Inhalt, hier bleibt es dieselbe
  Liste in Portionen.
- **Nicht verwechseln mit** [scroll-area](../../containers/scroll-area/): die Scrollfläche ist der
  Rahmen, die Seitennavigation entscheidet, was darin nachgeladen wird.
- In [repeater](../../data/repeater/) ist diese Komponente bereits enthalten — nicht doppelt bauen.

## Best Practices

- Mindestens 25 Elemente pro Seite, sonst ist Blättern langsamer als Scrollen.
- Gesamtzahl und aktuellen Bereich anzeigen ("41–80 von 312").
- Nach dem Seitenwechsel nach oben scrollen, sonst beginnt die neue Seite halb sichtbar.
- `endlos` nur, wo kein bestimmter Punkt gesucht wird; zum gezielten Springen gehören Zahlen.
- Mit den Pfeiltasten bedienbar, aktuelle Seite mit `aria-current`.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Repeater](../../data/repeater/) — Liste inklusive Seitennavigation
- [Scroll Area](../../containers/scroll-area/) — endlose Scrollfläche
- [Basiskomponente](../../basics/base/)

# Pagination

| Feld | Wert |
| ------ | ------ |
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `zahlen`, `vor-zurueck`, `nachladen`, `endlos` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `progress` |
| **Verwandt** | `repeater`, `list-view`, `table`, `scroll-area`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Pagination teilt eine lange Liste in Abschnitte auf und bietet den Wechsel zwischen ihnen an.

## Verwendungszweck

- Große Datenmengen übersichtlich darstellen
- Leistung verbessern (nur sichtbare Daten laden)
- Bedienbarkeit erhöhen

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **zahlen** | Seitenzahlen mit der aktuellen Seite und `…` |
| **vor-zurueck** | nur die vorherige und die nächste Seite |
| **nachladen** | angehängter Abschnitt auf Knopfdruck |
| **endlos** | der Abschnitt lädt automatisch, wenn das Listenende erreicht ist |

## Funktionen

- Total Items (Gesamtzahl)
- Current Page (aktuelle Seite)
- Items per Page (Elemente pro Seite)
- Jump to Page (direkt zu einer Seite springen)
- Page Size Selector (Anzahl der Elemente pro Seite ändern)

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln den Inhalt, hier bleibt es dieselbe Liste
  in Abschnitten.
- **Nicht verwechseln mit** [scroll-area](../../containers/scroll-area/): der Scroll-Bereich ist der
  Rahmen, die Pagination bestimmt, was in ihn geladen wird.
- In [repeater](../../data/repeater/) ist diese Komponente bereits enthalten — nicht doppelt bauen.

## Best Practices

- Mindestens 25 Einträge pro Seite, sonst ist Blättern langsamer als Scrollen.
- Zeig die Gesamtzahl und den aktuellen Bereich („41–80 von 312“).
- Nach einem Seitenwechsel nach oben scrollen, sonst beginnt die neue Seite halb sichtbar.
- Verwende `endlos` nur dort, wo nicht nach einem bestimmten Eintrag gesucht wird; gezieltes Springen braucht Zahlen.
- Bedienbar mit den Pfeiltasten, aktuelle Seite mit `aria-current`.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Repeater](../../data/repeater/) — Liste mit Pagination
- [Scroll Area](../../containers/scroll-area/) — endloser Scroll-Bereich
- [Basiskomponente](../../../primitives/basics/base.md)

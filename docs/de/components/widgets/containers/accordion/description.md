# Accordion (Akkordeon)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `mehrere`, `einzel`, `deaktiviert` |
| **Zustände** | `geöffnet`, `geschlossen` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `expand`, `collapse` |
| **Verwandt** | `tabs`, `panel`, `tree-view`, `table-of-contents`, `card` |
| **Status** | dokumentiert |

## Beschreibung
Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein- und ausklappen.

## Verwendungszweck

- Platz sparen durch Ein- und Ausklappen
- FAQ-Abschnitte
- Einstellungsgruppen
- Kategorien mit Unterpunkten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Stapel von Kopfzeilen, nacheinander jeweils eine offen |
| **mehrere** | mehrere Bereiche gleichzeitig offen |
| **einzel** | nur eine Kopfzeile, kein Stapel |
| **deaktiviert** | Kopfzeile sichtbar, aber nicht umschaltbar |

!!! info "Einordnung"
    Ein einzelnes einklappbares Element ohne Gruppierung (in Bibliotheken `collapsible`
    genannt) ist die Variante `einzel` dieses Accordions: `items` mit einem Eintrag
    und `multiple = false`.

## Funktionen

- Auf- und Zuklappen
- Animation beim Auf- und Zuklappen
- Tastaturnavigation
- Barrierefreiheit

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs zeigen immer nur einen Inhalt.
  Das Accordion kann mehrere gleichzeitig zeigen.
- **Nicht verwechseln mit** [panel](../panel/): Ein Panel steht für sich allein. Die Kopfzeilen
  eines Accordions gehören zu einer gemeinsamen Gruppe.
- **Nicht verwechseln mit** [tree-view](../../data/tree-view/): Hier werden Inhalte
  ein- und ausgeklappt. Dort wird durch eine Datenhierarchie geblättert.
- **Nicht verwechseln mit** [table-of-contents](../../data/table-of-contents/): Das Inhaltsverzeichnis
  springt zum Inhalt. Es blendet ihn nicht aus.

## Best Practices

- Der wichtigste Bereich ist beim Start offen, der Rest geschlossen.
- Die ganze Kopfzeile ist der Button. Der Pfeil ist nur die Anzeige.
- Tastatur: `Enter`/`Leertaste` schaltet um, Pfeiltasten springen zwischen den Kopfzeilen.
  `aria-expanded` beschreibt den Zustand.
- Höchstens etwa acht Kopfzeilen. Darüber ist eine Navigation besser als Einklappen.
- Lange Inhalte, die Nutzer zum Vergleichen brauchen, nicht einklappen.

## Verhalten

| Verhalten | Beschreibung |
|-----------|--------------|
| **einzeln öffnen** | nur einer ist offen |
| **mehrfach öffnen** | mehrere sind offen |
| **Accordion-Gruppe** | Gruppen von Accordion-Einträgen |

## Siehe auch

- [containers – Übersicht](../index.md)
- [Panel](../panel/) — ein eigenständiger Bereich
- [Tabs](../../navigation/tabs/) — immer nur ein Inhalt
- [Base-Komponente](../../../primitives/basics/base.md)

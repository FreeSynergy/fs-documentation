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
Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein-/ausklappen können.

## Verwendungszweck

- Platz sparen durch Ein-/Ausklappen
- FAQ-Sectionen
- Einstellungs-Gruppen
- Kategorien mit Unterpunkten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Stapel von Köpfen, einer nach dem anderen offen |
| **mehrere** | mehrere Bereiche gleichzeitig offen |
| **einzel** | nur ein Kopf, kein Stapel |
| **deaktiviert** | Kopf sichtbar, aber nicht schaltbar |

!!! info "Einordnung"
    Ein einzelnes aufklappbares Element ohne Gruppierung (in Bibliotheken `collapsible`) ist
die Variante `einzel` dieses Akkordeons: `items` mit einem Eintrag und
`multiple = false`.

## Features

- Expand/Collapse
- Animation (Ein-/Ausklapp-Animation)
- Keyboard-Navigation
- Accessibility (Barrierefreiheit)

## Abgrenzung

- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs zeigen immer nur einen Inhalt,
  das Akkordeon kann mehrere gleichzeitig zeigen.
- **Nicht verwechseln mit** [panel](../panel/): ein Panel steht für sich, die Akkordeonköpfe
  gehören zu einer gemeinsamen Gruppe.
- **Nicht verwechseln mit** [tree-view](../../data/tree-view/): hier wird Inhalt ein- und ausgeklappt,
  dort Datenhierarchie durchblättert.
- **Nicht verwechseln mit** [table-of-contents](../../data/table-of-contents/): das Verzeichnis
  springt zu Inhalten, es verbirgt sie nicht.

## Best Practices

- Der wichtigste Bereich ist anfangs offen, der Rest geschlossen.
- Die ganze Kopfzeile ist der Schaltfläche, der Pfeil ist nur das Hinweiszeichen.
- Tastatur: `Enter`/`Leertaste` schaltet, Pfeiltasten springen zwischen den Köpfen;
  `aria-expanded` beschreibt den Zustand.
- Höchstens etwa acht Köpfe; darüber ist eine Navigation besser als Einklappen.
- Lange Inhalte nicht einklappen, die man zum Vergleichen braucht.

## Verhalten

| Verhalten | Beschreibung |
|-----------|--------------|
| **Single Expand** | Nur einer offen |
| **Multiple Expand** | Mehrere offen |
| **Accordion Group** | Gruppen von Accordion-Items |

## Siehe auch

- [containers – Übersicht](../index.md)
- [Panel](../panel/) — eigenständiger Bereich
- [Tabs](../../navigation/tabs/) — immer nur ein Inhalt
- [Basiskomponente](../../basics/base/)

# Panel (Bereich)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `einklappbar`, `verschiebbar`, `filter` |
| **Zustände** | `geöffnet`, `geschlossen` |
| **Gesten** | `tap`, `drag`, `long-press` |
| **Animationen** | `expand`, `collapse`, `reorder` |
| **Verwandt** | `card`, `split-view`, `scroll-area`, `accordion`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Panel ist ein großer Container mit Kopfzeile, Inhalt und Fußzeile. Es unterscheidet
sich von einer Card durch seine größere Fläche und seinen Einsatz in Layouts.

## Verwendungszweck

- Große Inhaltsblöcke
- Layout-Container
- Filterbereich
- Dashboard-Widget

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Standard-Panel mit Kopfzeile |
| **einklappbar** | die Kopfzeile klappt den Inhalt ein und aus |
| **verschiebbar** | kann verschoben werden |
| **filter** | mit Filteroptionen |

## Funktionen

- Einklappbar (Ein- und Ausklappen)
- Verschiebbar (Bewegen)
- Größenänderung (Größe anpassen)
- Eigene Kopfzeile

## Abgrenzung

- **Nicht verwechseln mit** [card](../card/): Die Card zeigt einen Inhalt mit Titel und Aktionen.
  Das Panel fasst Bedienelemente oder einen Arbeitsbereich zusammen (Plan Abschnitt 4, Zeile 16 —
  beide bleiben, mit einer gemeinsamen Container-Basis).
- **Nicht verwechseln mit** [split-view](../split-view/): Die Split View teilt die Fläche
  in Bereiche. Das Panel ist einer dieser Bereiche.
- **Nicht verwechseln mit** [drawer](../../overlays/drawer/) oder [modal](../../overlays/modal/):
  Ein Panel bleibt im Layout und überdeckt nichts.
- **Nicht verwechseln mit** [accordion](../accordion/): Das Accordion ist eine Gruppe von
  Kopfzeilen, das Panel ein einzelner Bereich.

## Best Practices

- Die Kopfzeile benennt den Bereich, nicht die Aktion.
- Größe und innerer Abstand bleiben innerhalb einer Anwendung gleich.
- Den Zustand eines einklappbaren Panels merken und `aria-expanded` setzen.
- Der Panel-Inhalt scrollt selbst. Die Seite darf nicht mitscrollen.

## Aufbau

```
┌─────────────────────────────────────────┐
│ Kopfzeile / Titel                       │  ← Kopfzeile
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │  ← Inhalt
├─────────────────────────────────────────┤
│ Fußzeile / Aktionen                     │  ← Fußzeile
└─────────────────────────────────────────┘
```

## Siehe auch

- [containers – Übersicht](../index.md)
- [Base-Komponente](../../../primitives/basics/base.md)

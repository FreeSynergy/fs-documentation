# Tabs

| Feld | Wert |
| ------ | ------ |
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `reiter`, `pille`, `karte` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap`, `swipe`, `long-press` |
| **Animationen** | `slide-in`, `highlight` |
| **Verwandt** | `bottom-navigation`, `accordion`, `breadcrumb`, `radio-group`, `carousel` |
| **Status** | dokumentiert |

## Beschreibung
Tabs (Reiter) dienen dazu, zwischen Ansichten zu wechseln.

## Zweck

- Ansichten
- Kategorien
- Optionen

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **reiter** | klassische Reiter, der aktive ist unterstrichen |
| **pille** | abgerundete gefüllte Fläche, passt in Toolbars |
| **karte** | die Reiter sitzen auf einer Karte, der Rahmen gehört zum Inhalt |

## Funktionen

- Aktiver Reiter
- Schließbar
- Tastaturnavigation

## Abgrenzung

- **Nicht verwechseln mit** [accordion](../../containers/accordion/): Reiter zeigen immer nur
  einen Bereich, das Akkordeon mehrere, untereinander gestapelt.
- **Nicht verwechseln mit** [breadcrumb](../breadcrumb/): Reiter wechseln den Inhalt, die
  Breadcrumb zeigt eine Ebene in einer Hierarchie.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): Diese wechselt die
  Ansicht, Reiter wechseln nur den Inhalt **innerhalb** der Ansicht.
- Eine Auswahl für ein Formular ist eine [radio-group](../../../primitives/fields/radio-group/),
  keine Reiterleiste.

## Best Practices

- Zwei bis sieben Reiter; darüber gehört die Auswahl in eine Liste oder Navigation.
- Beim Wechseln den Inhalt behalten (nicht neu laden), die Scroll-Position pro Reiter merken.
- Pfeiltasten zum Wechseln, `role="tab"` und `aria-selected` für Screenreader.
- Schließen-Knopf nur, wenn Reiter geöffnete Dokumente darstellen (z. B. in Editoren).
- Zu lange Titel kürzen und den vollen Namen als Tooltip zeigen.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Accordion](../../containers/accordion/) — untereinander gestapelte Bereiche
- [Bottom Navigation](../bottom-navigation/) — Ansichten wechseln
- [Base-Komponente](../../../primitives/basics/base.md)

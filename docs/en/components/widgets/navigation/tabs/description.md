# Tabs

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `reiter`, `pille`, `karte` |
| **States** | `aktiv` |
| **Gestures** | `tap`, `swipe`, `long-press` |
| **Animations** | `slide-in`, `highlight` |
| **Related** | `bottom-navigation`, `accordion`, `breadcrumb`, `radio-group`, `carousel` |
| **State** | documented |

## Description
Tabs sind Reiter zum Umschalten zwischen Ansichten.

## Purpose

- Ansichten
- Kategorien
- Optionen

## Variants

| Variant | Description |
| ---------- | -------------- |
| **reiter** | klassische Reiter mit Unterstreichung des aktiven |
| **pille** | abgerundete Fläche, passt in Werkzeugleisten |
| **karte** | Reiter sitzen auf einer Karte, der Rahmen gehört zum Inhalt |

## Features

- Active Tab
- Closable
- Keyboard-Navigation

## Distinction

- **Nicht verwechseln mit** [accordion](../../containers/accordion/): Reiter zeigen immer nur einen
  Bereich, das Akkordeon mehrere untereinander.
- **Nicht verwechseln mit** [breadcrumb](../breadcrumb/): Reiter wechseln Inhalte, der Brotpfad
  zeigt eine Ebene in einer Hierarchie.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): die wechselt die Ansicht,
  Reiter wechseln nur den Inhalt **innerhalb** der Ansicht.
- Eine Auswahl für ein Formular ist eine [radio-group](../../../primitives/fields/radio-group/), keine Reiterleiste.

## Best Practices

- Zwei bis sieben Reiter; darüber gehört die Auswahl in eine Liste oder Navigation.
- Inhalte beim Wechsel behalten (nicht neu laden), Scrollposition je Reiter merken.
- Pfeiltasten zum Wechseln, `role="tab"` und `aria-selected` für Screenreader.
- Schließen-Knopf nur, wenn Reiter geöffnete Dokumente darstellen (z. B. Editoren).
- Zu lange Titel kürzen und den vollen Namen als Tooltip zeigen.

## See also

- [navigation – overview](../index.md)
- [Accordion](../../containers/accordion/) — Bereiche untereinander
- [Bottom Navigation](../bottom-navigation/) — Ansichtswechsel
- [Base component](../../../primitives/basics/base.md)

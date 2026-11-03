# Toolbar

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `kontext`, `ribbon` |
| **States** | `aktiv`, `geklebt` |
| **Gestures** | `tap`, `long-press`, `drag` |
| **Animations** | `expand`, `collapse`, `fade-in` |
| **Related** | `button`, `button-group`, `menu`, `context-menu`, `rich-text-editor` |
| **State** | documented |

!!! info "Standardisierung"
    Die früheren Komponenten `context-toolbar` und `ribbon` sind als Varianten in `toolbar` aufgegangen: `standard`, `kontext`, `ribbon`.

## Description
Eine Toolbar ist eine Reihe von Buttons/Icons für häufige Aktionen. Sie wird oft direkt unter der Titelzeile platziert.

## Purpose

- Schneller Zugriff auf häufige Funktionen
- Konsolidierung von Aktionen in einer Leiste
- Visuelle Organisation von Tools

## Variants

| Variant | Description |
| ---------- | -------------- |
| **standard** | feste Leiste mit den häufigen Aktionen |
| **kontext** | zeigt andere Aktionen, je nachdem was ausgewählt ist |
| **ribbon** | mehrzeilige Leiste mit benannten Gruppen (Desktop-Programme) |

## Features

- Customizable (benutzerdefiniert)
- Keyboard-Shortcuts
- Tooltip (bei Hover)
- Disabled States

## Distinction

- **Nicht verwechseln mit** [menu](../menu/): das Menü verbirgt Befehle hinter einer Beschriftung,
  die Leiste zeigt sie sofort als Symbol.
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): das Kontextmenü ist ein
  Overlay am Klickpunkt, die Variante `kontext` bleibt im Layout stehen.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): eine Leiste enthält
  Aktionen, eine Navigation enthält Ziele.
- Zusammengehörige Knopfpaare sind eine [button-group](../../../primitives/actions/button-group/), die Leiste
  selbst ist die gesamte Reihe.

## Best Practices
- Nur häufig verwendete Funktionen
- Konsistente Icon-Größe
- Hover-Effekt
- Keyboard-Shortcuts anzeigen

- Nur häufig genutzte Aktionen in die Leiste, der Rest ins Menü.
- Gruppieren und Gruppen trennen; die Reihenfolge über alle Ansichten gleich halten.
- Jedes Symbol braucht Tooltip mit Tastenkürzel, sonst wird es geraten.
- Deaktivierte Knöpfe bleiben sichtbar (kein Sprung in der Leiste), aber ohne Wirkung.
- Auf schmalen Bildschirmen in ein ``+``-Menü übergehen, nicht zusammenquetschen.

## Aktionsgruppen

| Art | Beispiele |
| ----- | ----------- |
| **Datei** | Neu, Speichern, Drucken |
| **Formatierung** | Fett, Kursiv, Unterstrichen |
| **Navigation** | Zurück, Vor, Aktualisieren |
| **Suche und Filter** | Suchen, Filtern, Anzeigefelder |
| **Gefährlich** | Löschen, Verwerfen — nur mit Bestätigung |

## Positionen

| Position | Description |
| ---------- | -------------- |
| **Top** | Unterhalb der Titelzeile (Standard) |
| **Sidebar** | In der Seitenleiste |
| **Floating** | Freischwebend (z.B. im Chat) |
| **Bottom** | Unten am Bildschirm (Mobile) |

## See also

- [navigation – overview](../index.md)
- [Button Group](../../../primitives/actions/button-group/) — zusammengehörige Knöpfe
- [Menu](../menu/) — Befehle im Menü
- [Base component](../../../primitives/basics/base.md)

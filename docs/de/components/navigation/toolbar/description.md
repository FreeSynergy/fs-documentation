# Toolbar (Symbolleiste)

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `kontext`, `ribbon` |
| **Zustände** | `aktiv`, `geklebt` |
| **Gesten** | `tap`, `long-press`, `drag` |
| **Animationen** | `expand`, `collapse`, `fade-in` |
| **Verwandt** | `button`, `button-group`, `menu`, `context-menu`, `rich-text-editor` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die früheren Komponenten `context-toolbar` und `ribbon` sind als Varianten in `toolbar` aufgegangen: `standard`, `kontext`, `ribbon`.

## Beschreibung
Eine Toolbar ist eine Reihe von Buttons/Icons für häufige Aktionen. Sie wird oft direkt unter der Titelzeile platziert.

## Verwendungszweck

- Schneller Zugriff auf häufige Funktionen
- Konsolidierung von Aktionen in einer Leiste
- Visuelle Organisation von Tools

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | feste Leiste mit den häufigen Aktionen |
| **kontext** | zeigt andere Aktionen, je nachdem was ausgewählt ist |
| **ribbon** | mehrzeilige Leiste mit benannten Gruppen (Desktop-Programme) |

## Features

- Customizable (benutzerdefiniert)
- Keyboard-Shortcuts
- Tooltip (bei Hover)
- Disabled States

## Abgrenzung

- **Nicht verwechseln mit** [menu](../menu/): das Menü verbirgt Befehle hinter einer Beschriftung,
  die Leiste zeigt sie sofort als Symbol.
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): das Kontextmenü ist ein
  Overlay am Klickpunkt, die Variante `kontext` bleibt im Layout stehen.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): eine Leiste enthält
  Aktionen, eine Navigation enthält Ziele.
- Zusammengehörige Knopfpaare sind eine [button-group](../../actions/button-group/), die Leiste
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
|-----|-----------|
| **Datei** | Neu, Speichern, Drucken |
| **Formatierung** | Fett, Kursiv, Unterstrichen |
| **Navigation** | Zurück, Vor, Aktualisieren |
| **Suche und Filter** | Suchen, Filtern, Anzeigefelder |
| **Gefährlich** | Löschen, Verwerfen — nur mit Bestätigung |

## Positionen

| Position | Beschreibung |
|----------|--------------|
| **Top** | Unterhalb der Titelzeile (Standard) |
| **Sidebar** | In der Seitenleiste |
| **Floating** | Freischwebend (z.B. im Chat) |
| **Bottom** | Unten am Bildschirm (Mobile) |

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Button Group](../../actions/button-group/) — zusammengehörige Knöpfe
- [Menu](../menu/) — Befehle im Menü
- [Basiskomponente](../../basics/base/)

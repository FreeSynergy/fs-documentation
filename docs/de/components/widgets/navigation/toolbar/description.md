# Toolbar

| Feld | Wert |
|-------|-------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `standard`, `kontext`, `ribbon` |
| **Zustände** | `aktiv`, `geklebt` |
| **Gesten** | `tap`, `long-press`, `drag` |
| **Animationen** | `expand`, `collapse`, `fade-in` |
| **Verwandt** | `button`, `button-group`, `menu`, `context-menu`, `rich-text-editor` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die bisherigen Komponenten `context-toolbar` und `ribbon` sind Varianten von `toolbar`
    geworden: `standard`, `kontext`, `ribbon`.

## Beschreibung
Eine Toolbar ist eine Reihe von Schaltflächen/Icons für häufige Aktionen. Sie steht oft direkt
unter der Titelleiste.

## Verwendungszweck
- Schneller Zugriff auf häufige Funktionen
- Aktionen in einer Leiste bündeln
- Werkzeuge übersichtlich ordnen

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **standard** | feste Leiste mit den häufigen Aktionen |
| **kontext** | zeigt je nach Auswahl andere Aktionen |
| **ribbon** | mehrzeilige Leiste mit benannten Gruppen (Desktop-Programme) |

## Funktionen

- Anpassbar
- Tastenkürzel
- Tooltip (beim Hover)
- Deaktivierte Zustände

## Abgrenzung

- **Nicht verwechseln mit** [menu](../menu/): Das Menü verbirgt Befehle hinter einer Beschriftung,
  die Leiste zeigt sie sofort als Icon.
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): Das Kontextmenü ist
  ein Overlay an der Klickstelle, die Variante `kontext` bleibt im Layout.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): Eine Leiste enthält
  Aktionen, eine Navigation enthält Ziele.
- Zusammengehörige Schaltflächenpaare sind eine [button-group](../../../primitives/actions/button-group/);
  die Leiste selbst ist die ganze Zeile.

## Best Practices

- Nur häufig genutzte Funktionen
- Einheitliche Icon-Größe
- Hover-Effekt
- Tastenkürzel anzeigen

- Nur häufige Aktionen in der Leiste, der Rest gehört ins Menü.
- Gruppieren und Gruppen trennen; die Reihenfolge in allen Ansichten gleich halten.
- Jedes Icon braucht einen Tooltip mit seinem Tastenkürzel, sonst müssen Nutzer raten.
- Deaktivierte Schaltflächen bleiben sichtbar (die Leiste springt nicht), haben aber keine Wirkung.
- Auf schmalen Bildschirmen in ein `+`-Menü verschieben, die Schaltflächen nicht zusammenquetschen.

## Aktionsgruppen

| Typ | Beispiele |
|------|----------|
| **Datei** | Neu, Speichern, Drucken |
| **Formatierung** | Fett, Kursiv, Unterstrichen |
| **Navigation** | Zurück, Vor, Aktualisieren |
| **Suchen und Filtern** | Suchen, Filtern, Felder anzeigen |
| **Gefährlich** | Löschen, Verwerfen — nur mit Bestätigung |

## Positionen

| Position | Beschreibung |
|----------|-------------|
| **Oben** | unter der Titelleiste (Standard) |
| **Sidebar** | in der Sidebar |
| **Schwebend** | frei schwebend (z. B. im Chat) |
| **Unten** | am unteren Bildschirmrand (mobil) |

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Button Group](../../../primitives/actions/button-group/) — zusammengehörige Schaltflächen
- [Menu](../menu/) — Befehle im Menü
- [Base-Komponente](../../../primitives/basics/base.md)

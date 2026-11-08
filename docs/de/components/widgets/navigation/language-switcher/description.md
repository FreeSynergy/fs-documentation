# Language Switcher

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `dropdown`, `knopetreihe`, `flaggen`, `kombiniert` |
| **Zustände** | `aktiv` |
| **Gesten** | `tap` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `select`, `menu`, `toolbar`, `bottom-navigation` |
| **Status** | dokumentiert |

## Beschreibung
Ein Sprachumschalter ist ein Bedienelement zum Wechseln der Sprache der Anwendung.

## Verwendungszweck

- Ändern der Spracheinstellung
- Mehrsprachigkeit
- Regionale Anpassung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **dropdown** | aktuelle Sprache plus eine aufklappbare Liste |
| **knopetreihe** | jede Sprache als eigene Schaltfläche (bis zu drei Sprachen) |
| **flaggen** | nur Symbole, mit Tooltip |
| **kombiniert** | Reihe von Schaltflächen mit einem `…`-Dropdown für weitere Sprachen |

## Funktionen

- Automatische Erkennung
- Dauerhaft gespeicherte Einstellung
- Wechsel im laufenden Betrieb
- Kein Neuladen nötig

## Abgrenzung

- **Nicht verwechseln mit** [select](../../../primitives/fields/select/): ein Feldwert bleibt im
  Formular, die Sprache gilt für die ganze Anwendung und wird dauerhaft gemerkt.
- **Nicht verwechseln mit** [menu](../menu/): ein Menü löst Aktionen aus, dieser Umschalter ändert
  nur eine Einstellung.
- Flaggen stehen nicht für Sprachen: Englisch wird in vielen Ländern gesprochen.

## Best Practices

- Schreib Sprachnamen in der Sprache selbst („Deutsch“, „English“, „Français“).
- Zeig Sprachcodes (`de`, `en`) statt Flaggen, wenn es um Sprache und nicht um Region geht.
- Übernimm die Standardsprache aus dem System, merke die Auswahl im Profil und auf dem Gerät.
- Wechsle ohne Neuladen; markiere Überschriften, die in der Zweitsprache fehlen.
- Denk an Rechts-nach-links-Sprachen (gespiegeltes Layout), nicht nur an Übersetzungen.

## Größenvarianten

| Größe | Verwendung |
|-------|------------|
| Small | in der Kopfleiste |
| Medium | in den Einstellungen |
| Large | auf der Startseite |

## Farbvarianten

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Standard** | normal | Standardstil |
| **Aktiv** | Primärfarbe | aktive Sprache |

## Sprachen

| Sprache | Code | Flagge |
|---------|------|--------|
| Deutsch | de | 🇩🇪 |
| English | en | 🇬🇧 |
| Français | fr | 🇫🇷 |
| **Español** | es | 🇪🇸 |
| Italiano | it | 🇮🇹 |

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Select](../../../primitives/fields/select/) — ein Wert in einem Formular
- [Toolbar](../toolbar/) — der übliche Platz für den Umschalter
- [Basiskomponente](../../../primitives/basics/base.md)

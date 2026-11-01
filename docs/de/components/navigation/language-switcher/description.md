# Language Switcher (Sprachumschalter)

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
Ein Language Switcher ist ein UI-Element zum Wechseln der Anwendungssprache.

## Verwendungszweck

- Spracheinstellungen ändern
- Mehrsprachigkeit
- Regionale Anpassung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **dropdown** | aktuelle Sprache plus Aufklappliste |
| **knopetreihe** | jede Sprache als eigener Knopf (bis drei Sprachen) |
| **flaggen** | nur Zeichen, mit Tooltip |
| **kombiniert** | Knopfreihe mit `…`-Dropdown für weitere Sprachen |

## Features

- Automatische Erkennung
- Persistente Einstellung
- Live-Wechsel
- Kein Reload nötig

## Größe-Varianten

| Größe | Verwendung |
|-------|------------|
| Small | In der Header-Leiste |
| Medium | In den Einstellungen |
| Large | Auf der Startseite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Normal | Standard-Style |
| **Active** | Primärfarbe | Aktive Sprache |

## Sprachen

| Sprache | Code | Flagge |
|---------|------|--------|
| Deutsch | de | 🇩🇪 |
| English | en | 🇬🇧 |
| Français | fr | 🇫🇷 |
| **Español** | es | 🇪🇸 |
| Italiano | it | 🇮🇹 |

## Abgrenzung

- **Nicht verwechseln mit** [select](../../fields/select/): ein Feldwert bleibt im Formular,
  die Sprache gilt für die ganze Anwendung und wird dauerhaft gemerkt.
- **Nicht verwechseln mit** [menu](../menu/): das Menü ruft Aktionen auf, dieser Schalter
  wechselt nur eine Einstellung.
- Flaggen stehen nicht für Sprachen: Englisch wird in vielen Ländern gesprochen.

## Best Practices

- Sprachnamen in der jeweiligen Sprache schreiben ("Deutsch", "English", "Français").
- Sprachkurse (`de`, `en`) zeigen statt Flaggen, wenn es um Sprache und nicht um Region geht.
- Standardsprache aus dem System übernehmen, Auswahl im Profil und am Gerät merken.
- Ohne Neuladen umschalten; fehlende Überschriften in der Zweitsprache kennzeichnen.
- Rechts-nach-links-Sprachen mitdenken (Layoutspiegelung), nicht nur übersetzen.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Select](../../fields/select/) — Wert in einem Formular
- [Toolbar](../toolbar/) — üblicher Ort des Schalters
- [Basiskomponente](../../basics/base/)

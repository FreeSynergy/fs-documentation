# Basiskomponente (base)

Die **Basiskomponente** ist die gemeinsame Elternklasse aller FreeSynergy-Komponenten.
Sie legt die Attribute, Zustände und Abschnitte fest, die *jede* Komponente erbt.

!!! important "Entscheidung (Standardisierung)"
    Seit der Standardisierung listet die `attributes.md` einer Komponente nur **ihre eigenen
    Attribute** plus den Verweis `Inherited from: base`. Alles, was in dieser
    Datei steht, wird **nicht** pro Komponente wiederholt. Änderungen an der Basisklasse wirken
    deshalb automatisch auf alle Komponenten.

## Profil (Pflichtmaske)

Jede `description.md` beginnt mit dieser Tabelle. Sie ist bewusst kein YAML-Frontmatter
(das Frontmatter wurde absichtlich aus diesem Repo entfernt), sondern eine Markdown-Tabelle. Sie ist
für Menschen lesbar **und** kann von `scripts/check_components.py` ausgewertet werden.

| Feld | Bedeutung | Beispiel (`search-field`) |
|------|-----------|---------------------------|
| **Category** | Ordner unter `components/` | `fields` |
| **Inherits from** | Elternklassen, beginnend mit `base` | `base`, `text-input` |
| **Variants** | Varianten auf derselben Seite | `simple`, `autocomplete`, `filter` |
| **States** | zusätzliche Zustände gegenüber `base` | `loading`, `error` |
| **Gestures** | Verweis auf [Gesten](../../../interactions/gestures/) | `tap`, `type` |
| **Animations** | Verweis auf [Animationen](../../../interactions/animations/) | `fade-in`, `expand` |
| **Related** | Abgrenzung und Querverweise | `search-input`, `combobox` |
| **Status** | `documented` / `sketch only` / `missing` | `documented` |

## Geerbte Attribute

### Identität und Sichtbarkeit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|----------|--------------|
| `id` | string | - | eindeutiger Bezeichner |
| `label` | string | - | Beschriftung (siehe [label](label/)) |
| `visible` | boolean | `true` | sichtbar? |
| `enabled` | boolean | `true` | bedienbar? (`disabled` ist das Gegenteil) |

### Darstellung

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|----------|--------------|
| `size` | enum | `medium` | `small`, `medium`, `large` (siehe Größenskala) |
| `theme` | enum | `default` | `default`, `dark` (folgt der Systemfarbpalette) |
| `rounded` | boolean | `true` | abgerundete Ecken? |
| `variant` | enum | - | Variante der Komponente, Werte werden pro Komponente festgelegt |

### Größenskala

| Größe | Höhe | Icon | Schrift | Verwendung |
|------|--------|------|-----|------|
| `small` | 28 px | 14 px | 13 px | dichte Flächen, Tabellen |
| `medium` | 36 px | 16 px | 14 px | Standard |
| `large` | 44 px | 20 px | 16 px | Touch, Hauptaktionen |

44 px ist auch die minimale Trefferfläche für die Touch-Bedienung.

### Zustände (`state`)

Jede Komponente kennt diese Zustandsnamen. `appearance.md` beschreibt, was sich pro Zustand optisch ändert;
Komponenten dürfen eigene Zustände ergänzen.

| Zustand | Auslöser |
|-------|---------|
| `default` | Ruhezustand |
| `hover` | Zeiger über dem Element |
| `active` | gedrückt / ausgewählt |
| `focus` | Tastatur- oder Fokusnavigation |
| `disabled` | `enabled = false` |
| `loading` | die Komponente wartet auf eine Antwort |
| `error` | Eingabe- oder Aktionsfehler |

### Interaktion und Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `tabIndex` | number | Reihenfolge der Tastaturnavigation |
| `onClick` | function | wird durch Zeiger oder Tastatur ausgelöst |
| `onFocus` | function | Fokus erhalten |
| `onBlur` | function | Fokus verloren |
| `gesture` | string[] | unterstützte Gesten (siehe [Gesten](../../../interactions/gestures/)) |
| `animation` | string | Übergang beim Ein- und Ausblenden (siehe [Animationen](../../../interactions/animations/)) |

### Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle; der **Wert** ist komponentenspezifisch und im Profil genannt |
| `aria-label` | string | zugänglicher Name, wenn es kein sichtbares `label` gibt |
| `aria-*` | - | Zustandsmarkierungen (`aria-disabled`, `aria-busy`, `aria-expanded`, …) |

## Variante oder eigene Komponente?

| Kriterium | → **Variante** (`variant`/`type`) | → **eigene Komponente** |
|-----------|----------------------------------|---------------------|
| Gleicher Datensatz, gleiche Ereignisse | ja | |
| Nur Aussehen oder Andockung ändert sich | ja (`size`, `placement`, `orientation`) | |
| Eigene Datenstruktur nötig (Vorschlagsliste, Dateistream, Kalender) | | ja |
| Eigene Lebensdauer oder eigenes Fokusverhalten (Overlay, Modal) | | ja |
| Barrierefreie Rolle ändert sich (`button` → `menu`) | | ja |
| Attributüberschneidung ≥ 75 % | ja | |

Echte Vererbung wird über das Feld **Inherits from** im Profil ausgedrückt
(z. B. erbt `context-menu` von `menu`, `audio` erbt von `media-player`).

## Dateisatz pro Komponente

| Datei | Pflicht | Inhalt (die Reihenfolge der Abschnitte ist festgelegt) |
|------|---------|--------------------------------------|
| `description.md` | ja | Profil → Beschreibung → Zweck → Varianten → Funktionen → Abgrenzung → Best Practices → Siehe auch |
| `appearance.md` | ja | Grundlayout → Varianten → Größen → Farben und Zustände → Hover/Fokus → Responsiv |
| `attributes.md` | ja | Hauptattribute → Verhalten → Darstellung → Ereignisse → Barrierefreiheit → **geerbt von** |
| `usage.md` | ja | Anwendung, Szenarien und Beispiele in einer Datei |

## Namenskonvention

Verzeichnisse auf Englisch, klein geschrieben mit Bindestrichen; Abschnittsüberschriften folgen der Sprache
des Dokuments; Attributnamen `camelCase` auf Englisch.

| Suffix | Bedeutung | Beispiel |
|--------|---------|------|
| `-input` | Feld mit einem Datentyp | `text-input` |
| `-picker` | Auswahl mit Overlay oder Dialog | `date-picker` |
| `-editor` | Bearbeiten von Inhalten | `code-editor` |
| `-view` | Datenansicht | `list-view` |
| `-menu` / `-bar` | Navigationsleiste | `context-menu`, `menubar` |

## Siehe auch

- [Basics – Übersicht](./index.md)
- [Komponentenübersicht](../index.md)
- [Gesten](../../../interactions/gestures/) und [Animationen](../../../interactions/animations/)
- [Standardisierte Daten](../../widgets/data/) – dieselbe Idee, nur für Felder und Typen

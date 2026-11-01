# Basiskomponente (base)

Die **Basiskomponente** ist die gemeinsame Elternklasse aller FreeSynergy-Komponenten.
Sie definiert Attribute, Zustände und Abschnitte, die *jede* Komponente erbt.

!!! important "Festlegung (Standardisierung)"
    Seit der Standardisierung listet `attributes.md` einer Komponente **nur noch eigene
    Attribute** plus den Verweis `Geerbt von: base`. Alles, was in dieser Datei steht,
    wird **nicht** mehr pro Komponente wiederholt. Änderungen an der Basisklasse wirken
    damit automatisch auf alle Komponenten.

## Steckbrief (Pflichtmaske)

Jede `description.md` beginnt mit dieser Tabelle. Sie ist bewusst keine YAML-Frontmatter
(Frontmatter wurde in diesem Repo bewusst entfernt), sondern eine Markdown-Tabelle:
sie ist für Menschen lesbar **und** kann von `tools/check_components.py` ausgewertet werden.

| Feld | Bedeutung | Beispiel (`search-field`) |
|------|-----------|---------------------------|
| **Kategorie** | Ordner unter `components/` | `fields` |
| **Erbt von** | Elternklassen, von `base` ausgehend | `base`, `text-input` |
| **Varianten** | Varianten auf derselben Seite | `simple`, `autocomplete`, `filter` |
| **Zustände** | zustätzliche Zustände gegenüber `base` | `loading`, `error` |
| **Gesten** | Bezug zu [Gesten](../../gestures/) | `tap`, `type` |
| **Animationen** | Bezug zu [Animationen](../../animations/) | `fade-in`, `expand` |
| **Verwandt** | Abgrenzung und Querverweise | `search-input`, `combobox` |
| **Status** | `dokumentiert` / `nur Skizze` / `fehlt` | `dokumentiert` |

## Geerbte Attribute

### Identität und Sichtbarkeit

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `id` | string | - | eindeutige Kennung |
| `label` | string | - | Beschriftung (siehe [label](../label/)) |
| `visible` | boolean | `true` | sichtbar? |
| `enabled` | boolean | `true` | bedienbar? (`disabled` = Umkehrwert) |

### Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `size` | enum | `medium` | `small`, `medium`, `large` (siehe Größen-Raster) |
| `theme` | enum | `default` | `default`, `dark` (folgt der Systemfarbpalette) |
| `rounded` | boolean | `true` | abgerundete Ecken? |
| `variant` | enum | - | Variante der Komponente, Werte pro Komponente definiert |

### Größen-Raster

| Größe | Höhe | Icon | Schrift | Verwendung |
|-------|------|------|---------|------------|
| `small` | 28 px | 14 px | 13 px | dichte Oberflächen, Tabellen |
| `medium` | 36 px | 16 px | 14 px | Standard |
| `large` | 44 px | 20 px | 16 px | Touch, principale Aktionen |

44 px entspricht zugleich der Mindesttrefferfläche für Touch-Bedienung.

### Zustände (`state`)

Jede Komponente kennt diese Zustandsnamen. `appearance.md` beschreibt, was sich
pro Zustand visuell ändert; Komponenten dürfen eigene Zustände ergänzen.

| Zustand | Auslösung |
|---------|-----------|
| `default` | Ruhezustand |
| `hover` | Zeiger über dem Element |
| `active` | gedrückt / ausgewählt |
| `focus` | Tastatur- oder Fokusnavigation |
| `disabled` | `enabled = false` |
| `loading` | Komponente wartet auf eine Antwort |
| `error` | Eingabe- oder Aktionsfehler |

### Interaktion und Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `tabIndex` | number | Reihenfolge der Tastaturnavigation |
| `onClick` | function | Auslösen per Zeiger oder Tastatur |
| `onFocus` | function | Fokus erhalten |
| `onBlur` | function | Fokus verloren |
| `gesture` | string[] | unterstützte Gesten (siehe [Gesten](../../gestures/)) |
| `animation` | string | Übergang beim Ein-/Ausblenden (siehe [Animationen](../../animations/)) |

### Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle; der **Wert** ist komponentenspezifisch und wird im Steckbrief genannt |
| `aria-label` | string | zugänglicher Name, falls kein sichtbares `label` |
| `aria-*` | - | Zustands-Markierungen (`aria-disabled`, `aria-busy`, `aria-expanded`, …) |

## Wann Variante, wann eigene Komponente?

| Kriterium | → **Variante** (`variant`/`type`) | → **eigene Komponente** |
|-----------|-----------------------------------|--------------------------|
| Gleicher Datensatz, gleiche Events | ja | |
| Nur Aussehen oder Andockung ändert sich | ja (`size`, `placement`, `orientation`) | |
| Eigene Datenstruktur nötig (Vorschlagsliste, Dateistrom, Kalender) | | ja |
| Eigene Lebensdauer oder Fokus-Verhalten (Overlay, Modal) | | ja |
| Accessible Role ändert sich (`button` → `menu`) | | ja |
| Attribute-Überschneidung ≥ 75 % | ja | |

Echte Vererbung wird über das Feld **Erbt von** im Steckbrief ausgedrückt
(z. B. `context-menu` erbt von `menu`, `audio` erbt von `media-player`).

## Dateisatz pro Komponente

| Datei | Pflicht | Inhalt (Abschnittsreihenfolge ist fix) |
|-------|---------|----------------------------------------|
| `description.md` | ja | Steckbrief → Beschreibung → Verwendungszweck → Varianten → Features → Abgrenzung → Best Practices → Siehe auch |
| `appearance.md` | ja | Grundlayout → Varianten → Größen → Farben und Zustände → Hover/Fokus → Reaktiv |
| `attributes.md` | ja | Hauptattribute → Verhalten → Darstellung → Events → Barrierefreiheit → **Geerbt von** |
| `usage.md` | ja | Anwendung, Szenarien und Beispiele in einer Datei |

## Namenskonvention

Verzeichnisse englisch, Kleinbuchstaben mit Bindestrich; Abschnittsüberschriften deutsch;
Attributnamen `camelCase` englisch.

| Endung | Bedeutung | Beispiel |
|--------|-----------|----------|
| `-input` | Feld mit Datentyp | `text-input` |
| `-picker` | Auswahl mit Overlay oder Dialog | `date-picker` |
| `-editor` | Bearbeiten von Inhalten | `code-editor` |
| `-view` | Datenansicht | `list-view` |
| `-menu` / `-bar` | Navigationsleiste | `context-menu`, `menubar` |

## Siehe auch

- [Basics – Übersicht](./index.md)
- [Komponenten-Übersicht](../index.md)
- [Gesten](../../gestures/) und [Animationen](../../animations/)
- [Standardisierte Daten](../../data/) — gleiche Idee, nur für Felder und Typen

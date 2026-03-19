# Theme Manager — Aussehen & Design

> Lebt in **FreeSynergy.Desktop** (`crates/fsd-theme/`). Eigenständiges Programm, im Desktop direkt aufrufbar.

[← Zurück zum Index](../../INDEX.md) | [Desktop](../desktop/README.md) | [CSS-System](../../technik/css.md)

---

## Bereiche

### Themes

Zeigt alle verfügbaren Themes (aus dem Store) als Karten an. Jedes Theme hat:
- Vorschau-Farbe
- Name
- "Aktivieren"-Button

Das aktive Theme wird mit einem "Active"-Badge markiert.

Themes kommen aus dem Store (Typ `theme`). Das eingebaute Standard-Theme ist **Midnight Blue**.

### Farben (Colors)

Zeigt alle CSS-Variablen des aktiven Themes in einer Liste:

| Variable | Farbe | Wert |
|---|---|---|
| `--fsn-color-primary` | 🟦 | `#00bcd4` |
| `--fsn-color-bg-base` | ⬛ | `#0f172a` |
| ... | | |

Jede Variable hat ein Farbvorschau-Kästchen und ein editierbares Textfeld mit dem Hex-Wert. Änderungen werden sofort auf die aktuelle Sitzung angewendet.

> **Speichern:** Die geänderten Farben gelten nur für die aktuelle Sitzung. Um sie dauerhaft zu speichern, kann man sie als eigenes Theme im Store veröffentlichen.

### Mauszeiger (Cursor)

Auswahl des aktiven Cursor-Sets aus allen installierten Sets. Der Theme Manager zeigt:

- Eine Vorschau-Reihe der wichtigsten Slots (`default`, `pointer`, `text`, `busy`, `grab`)
- Name und Autor des Sets
- **"Aktivieren"**-Button — übernimmt das Set für das aktuelle Theme

Die vollständige Verwaltung (neue Sets erstellen, Repositories verwalten) liegt im **Cursor Manager** — der Theme Manager ist nur der Auswahl-Punkt.

→ [Cursor Manager](../icons/cursor-manager.md)

### Fenster-Stil (Chrome)

Drei Einstellungsgruppen:

**Fenster-Stil (Window Chrome):**
- macOS — runde farbige Kreise (Ampel)
- KDE — rechteckige Buttons
- Windows — quadratische Buttons
- Minimal — kein Chrome

**Sidebar-Stil:**
- Solid — undurchsichtig
- Glass — Glasmorphismus (backdrop-filter)
- Transparent — vollständig transparent

**Animationen:**
- Ein / Aus — respektiert `prefers-reduced-motion`

---

## Synthesizer-Integration

Wenn ein Dienst mit Rolle `synthesizer.structured` aktiv ist, erscheint in zwei Bereichen ein **"Mit Synthesizer erstellen"**-Button:

### Farben (Theme erstellen)

Im Bereich **Farben** gibt es neben "Als Theme speichern" den Button "Mit Synthesizer erstellen". Der Synthesizer bekommt:

```toml
[context]
type    = "theme"
base    = "dark"           # dark | light
primary = "#00bcd4"        # optional: Hauptfarbe vorgeben
```

Er gibt N Farbpaletten-Vorschläge zurück — jeder als vollständiges Set aller CSS-Variablen. Der Nutzer sieht eine Vorschau-Karte pro Vorschlag (Hintergrund + Akzentfarbe + Text) und wählt per Checkbox.

### Fenster-Stil

Für den Fenster-Stil (Window Chrome, Sidebar-Stil, Animationen) ist kein Synthesizer-Button vorgesehen — das sind Auswahl-Optionen aus einem festen Set, kein kreativer Freiformprozess.

→ Vollständige Beschreibung: [Synthesizer-Konzept](../../konzepte/synthesizer.md)

---

## Repo

https://github.com/FreeSynergy/Desktop (Crate: `crates/fsd-theme/`)

---

Weiter: [Themes-Konzept](../../konzepte/themes.md) | [CSS-System](../../technik/css.md) | [Synthesizer](../../konzepte/synthesizer.md) | [Cursor Manager](../icons/cursor-manager.md)

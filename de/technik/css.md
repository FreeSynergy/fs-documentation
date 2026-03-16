# CSS-System

[← Zurück zum Index](../INDEX.md) | [Themes](../konzepte/themes.md)

---

## CSS-Variablen-Strategie

### Problem

Wenn alle Programme denselben CSS-Prefix nutzen (`--fsn-`), können Konflikte entstehen wenn z.B. Wiki.rs andere Farben braucht als Desktop.

### Lösung: Shared + Spezifisch

**Im Store (shared/themes/):** CSS-Variablen werden OHNE Prefix gespeichert:
```css
/* Store: shared/themes/midnight-blue.css */
:root {
    --bg-base: #0c1222;
    --text-primary: #e8edf5;
    --primary: #4d8bf5;
}
```

**Beim Laden:** Der Theme-Manager jedes Programms fügt den Prefix automatisch hinzu:
```css
/* Desktop lädt das Theme und prefixed mit --fsn- */
:root {
    --fsn-bg-base: #0c1222;
    --fsn-text-primary: #e8edf5;
    --fsn-primary: #4d8bf5;
}

/* Wiki.rs lädt dasselbe Theme und prefixed mit --wiki- */
:root {
    --wiki-bg-base: #0c1222;
    --wiki-text-primary: #e8edf5;
    --wiki-primary: #4d8bf5;
}
```

**Spezifische Themes** (nur für ein Programm) können im programmspezifischen Store-Verzeichnis liegen und haben den Prefix schon drin.

### Namenskonvention

Erlaubte Variablen-Namen (OHNE Prefix):

**Farben:**
```
--bg-base, --bg-surface, --bg-elevated, --bg-sidebar, --bg-card, --bg-input, --bg-hover
--text-primary, --text-secondary, --text-muted, --text-bright
--primary, --primary-hover, --primary-text, --primary-glow
--accent, --accent-hover
--success, --warning, --error, --info
--border, --border-focus, --border-hover
--sidebar-bg, --sidebar-text, --sidebar-active, --sidebar-active-bg, --sidebar-hover
```

**Effekte:**
```
--shadow, --shadow-glow, --radius, --radius-sm, --radius-lg, --transition
```

**Typografie:**
```
--font-family, --font-mono, --font-size, --font-size-sm, --font-size-lg
```

Ein Parser prüft bei Store-Upload ob alle Pflicht-Variablen gesetzt sind.

---

Weiter: [Themes](../konzepte/themes.md) | [UI-Objekte](ui-objekte.md)

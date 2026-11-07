# Wiki.js 3.1.1: Themes

Das Erscheinungsbild wird je Standort in der Datenbank gespeichert, nicht in einer Theme-Datei. Die Admin-Seite ist Admin → Theme (`frontend/src/pages/AdminTheme.vue`, Route `:siteid/theme`). Die Standardwerte kommen aus `backend/models/sites.ts`. Quellbaum: https://github.com/requarks/wiki/tree/3.1.1

Im Quellcode von 3.1.1 wurde kein Format für Theme-Dateien, kein Theme-Marktplatz und kein Theme je Nutzer gefunden. Ein Nutzer kann nur dann zwischen hell und dunkel wählen, wenn der Standort es erlaubt (nicht verifiziert; die Admin-Seite hat einen standortweiten Schalter `dark`).

## Einstellungen (Block `theme` eines Standorts)

| Schlüssel | Typ / Werte | Standard | Was er ändert | Quelle |
|-----|---------------|---------|-----------------|--------|
| `dark` | boolean | `false` | dunkles Farbschema | `AdminTheme.vue` (Schalter „darkMode“), `sites.ts` |
| `colorPrimary` | Farbe | `#1976D2` | `--color-primary` (Schaltflächen, Links, Akzente) | `sites.ts`, `tailwind.css` |
| `colorSecondary` | Farbe | `#02C39A` | `--color-secondary` | ebenso |
| `colorAccent` | Farbe | `#FF9800` | `--color-accent` | ebenso |
| `colorHeader` | Farbe | `#000000` | `--color-header` (obere Leiste) | ebenso |
| `colorSidebar` | Farbe | `#1976D2` | `--color-sidebar` (Schublade) | ebenso |
| `baseFont` | `inter`, `opensans`, `montserrat`, `roboto`, `rubik`, `tajawal`, `user` | `roboto` | UI-Schrift | `AdminTheme.vue` (`fonts`), `sites.ts` |
| `contentFont` | dieselbe Liste | `roboto` | Schrift des Seitentextes | ebenso |
| `contentWidth` | `full`, `centered` | `full` | Breite des Seiteninhalts | `AdminTheme.vue` (`widthOptions`), `sites.ts` |
| `sidebarPosition` | `left`, `right` | `left` | Seite der Schublade | `MainLayout.vue`, `sites.ts` |
| `tocPosition` | `off`, `left`, `right` (die Admin-Liste) | `right` | Platzierung des Inhaltsverzeichnisses | `AdminTheme.vue` (`rightLeftOptions`), `sites.ts` |
| `codeBlocksTheme` | Name eines highlight.js-Stils (247 Optionen in der Admin-Liste) | `github-dark` | Farben der Codeblöcke | `AdminTheme.vue` (`codeThemes`), `sites.ts`, `highlight.js` 11.12.0 in `frontend/package.json` |
| `showPrintBtn` | boolean | `true` | Druckknopf | `sites.ts` |
| `showPageProgress` | boolean | `true` | Lesefortschrittsbalken | `sites.ts` |
| `pageTransitions` | boolean | `true` | Ansichtsübergänge zwischen Seiten | `sites.ts` |
| `injectCSS` | Text | leer | eigenes CSS, das jeder Seite hinzugefügt wird | `sites.ts` |
| `injectHead` | Text | leer | eigenes HTML im `<head>` | `sites.ts` |
| `injectBody` | Text | leer | eigenes HTML am Ende von `<body>` | `sites.ts` |

`injectCSS`, `injectHead`, `injectBody` sind der Weg, eigenes Styling oder Markup hinzuzufügen. Sie werden auf der Admin-Seite Theme bearbeitet (`AdminTheme.vue`, Felder in den Zeilen ~336 und ~352). Wer sie bearbeiten darf und ob sie bereinigt werden, wurde nicht geprüft.

Die Liste der UI-Schriften enthält `user`, also die persönliche Schriftwahl jedes Nutzers (Locale-Text `fontUserDefaults`).

## Farbsystem

- Fünf Markenfarben (`primary`, `secondary`, `accent`, `header`, `sidebar`) werden zur Laufzeit als CSS-Custom-Properties `--q-<name>` geschrieben (`frontend/src/helpers/cssVars.js`).
- Tailwind-4-Tokens in `frontend/src/css/tailwind.css` bilden `--color-<name>` auf diese Eigenschaften ab. Abgeleitete Töne sind `color-mix(...)` der Markenfarbe mit Weiß (`--color-primary-light`, `--color-primary-lighter`, `--color-secondary-lighter`, `--color-sidebar-light`).
- Feste Neutraltöne: `--color-white`, `--color-black`, `--color-cancel` (`#616161`), und eine dunkle Stufenleiter `--color-dark` bis `--color-dark-6` (`#0d1117`, `#343b48`, `#292f39`, `#1e232a`, `#161b22`, `#070a0d`). Quelle: `tailwind.css`.
- Die SCSS-Markenstandards in `frontend/src/css/_theme.scss` sind Werte aus der Quasar-Zeit (`$primary: #1976d2` und andere). Zur Laufzeit werden sie durch die Datenbankwerte überschrieben.
- `_palette.scss` enthält die Material-Farbstufen, die ältere Stylesheets verwenden.

### Dunkler Modus

- Der dunkle Modus ist die Klasse `body--dark` auf `<body>` (`frontend/CLAUDE.md`).
- Ein Panel, das in beiden Themes dunkel ist, verwendet `.w-dark-surface` (`frontend/CLAUDE.md`).
- Die Tailwind-Variante `dark:` hängt an `body--dark` (`frontend/CLAUDE.md`).

## Typografie

- Schriftfamilien kommen aus den sechs oben genannten Auswahlmöglichkeiten. Die Schriftdateien werden vom Standort ausgeliefert (`frontend/public/_assets/…`). Dateiliste und Lizenzen nicht geprüft. Nicht verifiziert: ob die Schriftdateien mitgeliefert oder von einem CDN geladen werden.
- Größen für Überschriften, Fließtext und Code: nicht extrahiert. Die Stylesheets von 3.1.1 sind `frontend/src/css/_base.scss`, `_page-contents.scss` und `_page-contents-asciidoc.scss`. Nicht vollständig gelesen.

## Abstände und Layoutmaße

| Maß | Wert | Quelle |
|--------|------|--------|
| Breite der Seitenleiste | `$rail-width: 48px` | `frontend/src/css/_theme.scss` (Kommentar: Breite der Seitenaktionsleiste und der Einfügeleiste des Editors; auch die Höhe der Leistenschaltflächen, `h-12`) |
| Inhaltsbreite | `full` oder `centered` (Theme) | `sites.ts` |
| Breite der Schublade | in `MainLayout.vue` gesetzt (`sidebarWidth`); Wert nicht extrahiert | `MainLayout.vue` |
| Abstandsskala | Tailwind-Standard wird angenommen; die Datei `tailwind.css` wurde nicht auf eine eigene Skala geprüft | nicht verifiziert |

## Was in einem FreeSynergy-Frontend im Stil nachgebaut werden kann

| Element | Nachbaubar | Hinweise |
|---------|-----------|----------|
| Fünf Markenfarben plus Neutraltonleiter | ja | Dieselben fünf Rollen verwenden: primary, secondary, accent, header, sidebar. |
| Helles und dunkles Schema | ja | Eine Klasse am Wurzelelement verwenden; die Regel „immer dunkles Panel“ beibehalten. |
| Umschalter der Inhaltsbreite (full, centered) | ja | Nur Verhalten. |
| Seite der Schublade (links oder rechts) | ja | Nur Verhalten. |
| Position des Inhaltsverzeichnisses | ja | |
| Highlight-Theme für Codeblöcke | ja | Jeden Highlighter verwenden; die Namensliste wird nicht kopiert. |
| Sechs Schriftauswahlen | ja | Unsere eigene Schriftliste verwenden. Die Lizenz jeder Schrift vor der Auslieferung prüfen. |
| Einfügen von eigenem CSS, Head und Body | ja, aber als Admin-Funktion | Nur für Admins halten. |
| Genaue Pixelwerte, Easing, Schatten | nicht extrahiert | Nicht kopieren; eigenes Design messen. |

Regel für FreeSynergy: die Einstellungen und Rollen übernehmen, nicht den CSS-Text. Kein Stylesheet wird kopiert (ADR 0013).

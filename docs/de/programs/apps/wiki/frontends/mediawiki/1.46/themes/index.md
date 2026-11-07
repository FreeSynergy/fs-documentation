# MediaWiki 1.46 — Themes (Vector 2022 und Codex-Tokens)

Version: 1.46.2. Quellen:
- Codex-Tokens des hellen Themes: https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/themes/wikimedia-ui.json
- Codex-Tokens des Dunkelmodus: https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/modes/dark.json
- Codex-Anwendungstokens (Abstände, Radius, Schriftgrößenskala): https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/application.json
- LESS-Variablen von Vector 2022: https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/resources/skins.vector.styles/variables.less
- Vector ADR 0002 (CSS-Custom-Properties): https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/adr/0002-use-css-custom-properties.md
- Vector-Konfiguration (Darstellungseinstellungen): https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/configuration/configuration.md

## Wie Themes funktionieren

- Die Styles von Vector 2022 stammen aus den Codex-Design-Tokens (das Theme "WikimediaUI"). Die Token-Namen werden in die LESS-Variablen von Vector übernommen. Quelle: `variables.less`, Kommentar zum Schriftstapel.
- Die eigenen Tokens von Vector sind wenige und in ADR 0002 als `@private` und `@experimental` markiert. Ein äußeres Frontend sollte sich nicht darauf verlassen. Stattdessen die Codex-Token-Namen und -Werte verwenden.
- Die Darstellung ist eine Benutzereinstellung, keine eigene Theme-Datei. Der Nachtmodus ist `vector-theme` mit den Werten `day`, `night`, `os`. Angemeldete Benutzer können den Nachtmodus mit `?vectornightmode=night` oder `=1` erzwingen (configuration.md).
- Textgröße: `vector-font-size` = 0 (normal), 1 (groß), 2 (sehr groß) (configuration.md).
- Breite: `vector-limited-width` = 1 (begrenzt) oder 0 (volle Breite) (configuration.md).

## Farben (helles Theme, Codex WikimediaUI)

Gelesen aus `themes/wikimedia-ui.json`. Zuordnung der Tokens `wmui-color.base*` (die Skala für Text und Hintergrund):

| Token | Wird aufgelöst zu | Hex |
|-------|-------------------|-----|
| `base0` | schwarz | #000 |
| `base10` | gray900 | #202122 (Haupttext) |
| `base20` | gray600 | #54595d |
| `base30` | gray500 | #72777d |
| `base50` | gray400 | #a2a9b1 |
| `base70` | gray300 | #c8ccd1 |
| `base80` | gray100 | #eaecf0 |
| `base90` | gray50 | #f8f9fa (Seitenhintergrund, leichte Tönung) |
| `base100` | weiß | #fff |
| `modifier-base10--lighten` | gray700 | #404244 |

Akzent (Links, fortschreitende Aktionen): Der helle Wert von `color.progressive` wurde in diesem Lauf nicht gelesen. Das Token `accent` wird zu `blue700` aufgelöst (themes/wikimedia-ui.json, `color.accent`). Den Hex-Wert von progressive vor der Verwendung prüfen.

## Farben (Dunkelmodus, Codex)

Gelesen aus `modes/dark.json`:

| Token | Wird aufgelöst zu |
|-------|-------------------|
| `color.progressive` | blue400 |
| `color.progressive--hover` | blue300 |
| `color.progressive--active` | blue200 |
| `background-color.progressive-subtle` | blue1000 |
| `border-color.progressive` | blue500 |
| `box-shadow.color.progressive--focus` | blue500 |

Die Hex-Werte der Blau-Skala wurden in diesem Lauf nicht gelesen. Auch die dunklen Basiswerte für Text und Hintergrund wurden nicht gelesen. Beim Aufbau direkt aus `modes/dark.json` übernehmen.

## Typografie

Aus `themes/wikimedia-ui.json` (Tokens für Schriftfamilien):

| Token | Stapel (erste Einträge) |
|-------|-------------------------|
| `font-family.sans-100` | -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Inter, Helvetica, Arial, sans-serif |
| `font-family.serif-100` | 'Linux Libertine', Georgia, Times, 'Source Serif 4', serif |
| `font-family.monospace-100` | Menlo, Consolas, 'Liberation Mono', 'Fira Code', 'Courier New', monospace |

Größen von Vector (variables.less):

| Variable | Wert |
|----------|------|
| `@font-size-heading-1` | 1.8em |
| `@font-size-heading-2` | 1.5em |
| `@font-size-heading-3` | 1.2em |
| `@font-size-footer` | entspricht 12px (12/16 em) |
| `@font-size-search-input` | entspricht 13px (13/16 em) |
| `@line-height-base` | 1.6 |
| `@line-height-code` | 1.3 |
| `@line-height-nav` | 1.125em |
| `@size-icon` | entspricht 20px (20/16 em) |

Schriftgrößenskala von Codex (application.json): x-small = 75, small = 90, medium = 100, large = 110, x-large = 125, xx-large = 150, xxx-large = 175 (Tokens in Prozent).

## Abstände und Radius

| Token | Zuordnung (application.json) |
|-------|------------------------------|
| `spacing.25` … `spacing.400` | jeweils auf `dimension.<n>` abgebildet; genaue px-Werte von `dimension.*` wurden in diesem Lauf nicht gelesen |
| `border-radius.base` | `dimension.absolute.2` (2 px) |
| `border-radius.pill` | `dimension.absolute.9999` |
| `border-radius.circle` | `dimension.half` |

Vector verwendet `@spacing-150` und `@spacing-300` für den Innenabstand des Inhaltsbereichs (variables.less). Ihre px-Werte stammen aus `dimension.*` und wurden in diesem Lauf nicht gelesen.

## Layout-Tokens

Layoutwerte von Vector (variables.less): maximale Breite des Seitencontainers 1596px, Inhalt maximal 948px, Seitenabstand am Desktop 44px (52px auf breiten Bildschirmen), Kopfzeile 50px, Suche maximal 500px, Rasterabstand 24px, Scroll-Abstand für Überschriften 75px. Vollständige Tabelle in `../layout.md`.

## Was nachgebaut werden kann

| Element | Nachbaubar? | Hinweise |
|---------|-------------|----------|
| Helle und dunkle Palette mit Codex-Token-Namen | ja | Die Werte oben verwenden. Vorher die Farbe progressive und die dunklen Basiswerte prüfen. |
| Schriftstapel | ja | Die Namen der Familien übernehmen, nicht die Dateien. Schriften sind die Stapel des Betriebssystems. |
| Schriftgrößenskala und Zeilenhöhe | ja | Aus den LESS-Variablen; Werte oben aufgeführt. |
| Dreispaltiges Raster und Breiten | ja | Aus `layout.md`. |
| Klebende Kopfzeile und angeheftete Bereiche | ja, als Verhalten | Das Verhalten steckt im JavaScript von Vector; wir beschreiben es und bauen unser eigenes. |
| Genaue Icons und Bilder von Vector | nein | Icons sind Assets im Repository von Vector. Wir dürfen sie nicht kopieren (Regel ADR 0013: kein Kopieren). Eigene Icons verwenden. |
| CSS-Custom-Properties von Vector | nicht als API | `@private` und `@experimental` in ADR 0002. Eigene Tokens verwenden, benannt nach den Codex-Namen. |

## Nicht geprüft

- Hex-Werte von Blau (progressive) im hellen Modus.
- Dunkle Basis- und Oberflächenfarben.
- Genaue px-Werte der Codex-Abstands- und Radius-Tokens.
- Vector-Haltepunkte der responsiven Variante.

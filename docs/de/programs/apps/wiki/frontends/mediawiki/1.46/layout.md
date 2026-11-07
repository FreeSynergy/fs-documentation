# MediaWiki 1.46 — Layout (Vector 2022, Standard-Skin)

Quellen: Vorlagen und Komponenten von Vector 2022 im Skin-Repository REL1_46 (https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46): `includes/templates/skin.mustache`, `Header.mustache`, `MainMenu.mustache`, `PageTools.mustache`, `includes/SkinVector22.php`, `includes/Components/*`. Layoutmaße aus `resources/skins.vector.styles/variables.less`.

Das folgende Layout ist die Struktur der gerenderten Seite. Die Positionen beschreiben, wie Vector sie auf einem Desktop-Bildschirm anordnet. Geprüft gegen die Vorlage, nicht gegen einen Screenshot.

## Bereiche (oben nach unten, links nach rechts)

```
+-------------------------------------------------------------------------+
| Header: [menu toggle] [logo]   [search box]   [appearance] [languages] [user links] |
+-----------+-------------------------------------------------------------+
| Main menu | Site notice                                                  |
| (sidebar, | Page titlebar: <h1 title>        [TOC toggle]               |
| pinnable) | Page toolbar: views (Read | Edit | History ...) | tools menu  |
|           | +--------------------------------------------------------+ |
| TOC       | | Subtitle / user messages                                | |
| (pinnable,| | Body (mw-body / vector-body), wikitext rendered          | |
| left of   | | Categories (below the body)                              | |
| content)  | | Language list (optional, bottom of content)              | |
|           | +--------------------------------------------------------+ |
|           | Footer (info, copyright, links)                               |
+-----------+-------------------------------------------------------------+
  Bottom dock (optional, fixed at the bottom); sticky header (appears on scroll)
```

## Benannte Teile (Vorlagen-Teilstücke)

| Teil | Vorlage | Inhalt | Hinweise |
|------|---------|--------|----------|
| Kopfzeile | `Header.mustache` | Logo, Suche, persönliche Werkzeuge, Sprachzugang | Sprachschaltfläche wird angezeigt, wenn die Erweiterung ULS geladen ist und Sprachen im Kopfbereich angezeigt werden (`SkinVector22.php`, `shouldHideLanguages`) |
| Hauptmenü | `MainMenu.mustache`, `MainMenuPinned.mustache`, `MainMenuDropdown.mustache` | Navigationsleiste | Angeheftet oder ausgeblendet je nach Einstellung `vector-main-menu-pinned` |
| Suche | `SearchBox.mustache` | Sucheingabe mit Vorschlägen (Typeahead) | Das Sucheingabefeld trägt die Zugriffstaste `f` (siehe `shortcuts.md`) |
| Titelleiste | `PageTitlebar.mustache` | Seitentitel, Untertitel, Untertitelzeile | |
| Werkzeugleiste | `PageToolbar.mustache` | Ansichten (lesen, bearbeiten, Verlauf) und Aktionen | Beschriftungen der Menüs p-tb und p-cactions überarbeitet in `VectorComponentPageTools.php` |
| Werkzeuge | `PageTools.mustache` | Werkzeugmenü, rechts angeheftet wenn aktiviert | Einstellung `vector-page-tools-pinned` |
| Darstellung | `Appearance.mustache` | Textgröße, Breite, Thema | Einstellungen `vector-font-size`, `vector-limited-width`, `vector-theme` (`doc/configuration/configuration.md`) |
| Inhaltsverzeichnis | `TableOfContents.mustache` | Abschnittsliste der aktuellen Seite | Anheftbar; klappt standardmäßig ein, wenn die Seite mindestens 28 Abschnitte hat (`wgVectorTableOfContentsCollapseAtCount` = 28, `configuration.md`) |
| Inhalt | `skin.mustache` `#bodyContent` | gerendertes Seiten-HTML | Abschnitte sind Ankerziele |
| Kategorien | Slot `html-categories` | Kategorieliste unter dem Inhalt | |
| Fußzeile | `Footer.mustache` | Informationen und Links | |
| Klebende Kopfzeile | `StickyHeader.mustache` | Kopfzeile, die beim Scrollen bleibt | Nur vorhanden, wenn `data-vector-sticky-header` gesetzt ist |
| Untere Leiste | `BottomDock.mustache` | optionale untere Leiste | |

## Breiten und Abstände (Variablen von Vector 2022)

| Variable | Wert | Bedeutung |
|----------|------|-----------|
| `@max-width-page-container` | 1596px (`unit(1596px / 16, rem)`) | Obergrenze des äußeren Containers |
| `@max-width-content-container` | 948px | Obergrenze der Artikelspalte (Standard; Einstellung für begrenzte Breite) |
| `@padding-horizontal-page-container-desktop` | 44px | Seitenabstand am Desktop |
| `@height-header` | 50px | Höhe der klebenden Kopfzeile |
| `@max-width-search` | 500px | Obergrenze des Suchfelds |
| `@grid-column-gap` / `@grid-row-gap` | 24px | Abstände im Layout |
| `@scroll-margin-heading` | 75px | Versatz beim Springen zu einer Überschrift |
| `@min-width-supported` | 300px | Unterhalb dieser Breite scrollt das Layout horizontal |
| `@font-size-browser` | 16 | Grundannahme für px-zu-rem |

Quelle: `resources/skins.vector.styles/variables.less`.

## Responsives Verhalten

- Vector 2022 hat eine responsive Variante hinter einem experimentellen Schalter (`wgVectorResponsive`); sie ist als experimentell dokumentiert und nicht verlässlich (`configuration.md`).
- Schmale Bildschirme: Hauptmenü und Inhaltsverzeichnis werden zu Schubladen oder blenden sich aus (Verhalten aus `skin.js`, `pinnableElement.js`; genaue Haltepunkte ungeprüft).

## Was unser Frontend davon braucht

- Ein dreispaltiges Desktop-Raster mit anheftbarer linker Navigation und optionaler rechter Werkzeugleiste.
- Eine Kopfzeile mit Suche, Sprache und Benutzerbereich.
- Eine Werkzeugleiste mit Ansichts-Reitern und einem Werkzeugmenü.
- Eine Inhaltsspalte mit einer maximalen Breite entsprechend 948px.
- Eine klebende Kopfzeile beim Scrollen (optional).

Punkte, die in dieser Datei als "ungeprüft" markiert sind, wurden nicht gegen eine gerenderte Seite geprüft.

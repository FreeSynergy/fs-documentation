# Wiki.js 3.1.1: Layout

Quellen: `frontend/src/layouts/MainLayout.vue`, `frontend/src/components/HeaderNav.vue`, `NavSidebar.vue`, `PageActionsCol.vue`, `frontend/src/css/_theme.scss` (alle unter https://github.com/requarks/wiki/tree/3.1.1/frontend/src). Das Layout wird teilweise durch das Theme des Standorts bestimmt (siehe `themes/index.md`).

## Bereiche des Hauptlayouts

```
+------------------------------------------------------------------------+
| Header (w-header): logo/site title · search · create · library ·       |
|                    inbox (badge) · administration · login/account      |
+----------------+-------------------------------------------+-----------+
| Drawer         | Content                                   | Page      |
| (sidebar)      |  - page header, tags, last edited          | actions   |
|  - locale      |  - page body (view or editor)              | rail      |
|  - browse menu |  - Table of contents (position: theme)     | (48 px)   |
|  - nav tree    |                                            |           |
|  - Edit Nav    |                                            |           |
+----------------+-------------------------------------------+-----------+
```

Die Schublade liegt standardmäßig links. Die Theme-Einstellung `sidebarPosition` kann sie nach rechts setzen. Das Inhaltsverzeichnis wird durch `tocPosition` platziert (Standard `right`). Die Breite der Seitenleiste ist `$rail-width: 48px` (`frontend/src/css/_theme.scss`). Quellen: `backend/models/sites.ts` (Theme-Standards), `MainLayout.vue`.

## Kopfzeile

| Element | Verhalten | Quelle |
|---------|-----------|--------|
| Startschaltfläche | führt zur Startseite des Standorts | `HeaderNav.vue` (`homePath`) |
| Suche | schaltet eine Suchzeile ein oder aus; ARIA-Label „Search...“ | `HeaderNav.vue`, Locale `common.header.search` |
| Erstellen (+) | öffnet das Menü „Neue Seite“ mit den aktiven Editoren | `HeaderNav.vue`, Locale `common.header.create`, `frontend/src/helpers/editors.js` |
| Bibliothek (Museums-Symbol) | Schaltfläche mit Beschriftung „Library“; Ziel nicht geprüft | `HeaderNav.vue`, Locale `common.header.library` |
| Posteingang | Nachrichten, Beobachtungen, Prüfwarteschlange; zeigt ein Abzeichen | `HeaderNav.vue`, `routes.js` (`/_inbox/*`) |
| Administration (Werkzeug-Symbol) | Admin-Bereich | `HeaderNav.vue`, Locale `common.header.admin` |
| Anmeldung / Konto | Anmeldung oder Kontomenü mit Profil und Abmeldung | `HeaderNav.vue`, Locale `common.header.login` |
| Locale-Auswahl | in der Schublade, wenn der Standort mehr als eine Locale hat | `MainLayout.vue` (`siteStore.locales.showMenu`) |

## Schublade (Seitenleiste)

- Oben: Schaltfläche der Locale-Auswahl und eine Schaltfläche „Browse“ (Sitemap-Symbol), die ein Durchsuchen-Menü öffnet (`NavBrowseMenu.vue`).
- Mitte: der Navigationsbaum (`NavSidebar.vue`). Die Einträge kommen aus der Navigation des Standorts (Admin „Navigation“).
- Unten: Schaltfläche „Edit Nav“, nur für Nutzer sichtbar, die die Navigation bearbeiten dürfen (`NavEditMenu.vue`, `NavEditOverlay.vue`).
- Schmale Bildschirme: die Schublade wird zu einem Overlay. Die Schaltfläche zum Öffnen liegt unten links am Bildschirm, nicht oben (Kommentar in `MainLayout.vue` zu `corner-btn`). Im Quellcode verifiziert.
- Die Schublade hat eine „Mini“-Variante mit reinen Symbolschaltflächen (Klasse `sidebar-mini`).

## Inhaltsbereich

- Seitenansicht mit Titel und Text. Die Route `/:catchAll(.*)*` rendert jeden Seitenpfad über `pages/Index.vue`.
- Editor-Ansicht: dieselbe Route mit `/_edit/<path>`; `/_create/<editor>` für eine neue Seite.
- Versionsansicht: `/_version/:versionId`, nur lesend (`PageVersion.vue`).
- Fehleransicht: `/_error/:action?`.
- Live-Notizen: `/n/:noteKey`, Layout `LiveNoteLayout.vue`.
- Suchergebnisse: `/_search`. Tag-Browser: `/_tags`. Öffentliche Nutzerseite: `/_user/:userId`.

Es gibt eine Breadcrumb-Komponente (`frontend/src/components/shared/WBreadcrumbs.vue`), ihre Verwendung in der Seitenansicht wurde aber nicht geprüft. Die Breadcrumb-Aussage der alten Seite ist nicht verifiziert.

## Seitenaktionsleiste (rechter Rand, 48 px breit)

Aus `PageActionsCol.vue`. Die Schaltflächen sind quadratisch und zeigen nur Symbole mit einem `aria-label`:

| Schaltfläche | aria-label | Handler (Funktionsname in der Datei) |
|--------|-----------|-------|
| Seiteneigenschaften | „Page Properties“ | `togglePageProperties`, Seitendialog `PagePropertiesDialog` |
| Seitendaten | „Page Data“ | `togglePageData`, Seitendialog `PageDataDialog` |
| Verlauf | „Page History“ | `viewPageHistory` |
| Quelle | „Page Source“ | `viewPageSource` |
| Aktionen (…) | „Page Actions“ | Menü mit `convertPage` (`PageConvertDialog`) und `rerenderPage` (`RerenderPageDialog`), nur sichtbar, wenn der Nutzer schreiben darf |
| Duplizieren | „Duplicate Page“ | `duplicatePage` |
| Umbenennen / Verschieben | „Rename / Move Page“ | `renamePage` (Dialog mit Baum-Browser) |
| Löschen | „Delete Page“ | `deletePage` (`PageDeleteDialog`) |

Die Editoren Markdown, AsciiDoc und Visual haben eine eigene Einfügeleiste links vom Editor, mit demselben Breiten-Token (`$rail-width`). Ob die Seitenleiste im Editormodus unverändert angezeigt wird, wurde nicht geprüft. Quellen: `PageActionsCol.vue`, `frontend/src/css/_theme.scss`.

## Editor-Layout

- Markdown und AsciiDoc: Monaco-Editor mit einem Vorschaubereich. Die Vorschau scrollt synchron (`frontend/src/composables/previewScrollSync.js`).
- Visual: ProseMirror-Dokument mit einem Blockmenü (Slash) und einer Formatierungsleiste (`frontend/src/editor/visual/bar.js`).
- Excalidraw und Feedback: Komponentendateien existieren (`EditorExcalidraw.vue`, `EditorFeedback.vue`, `EditorFeedbackConfigOverlay.vue`); ihr Layout wurde nicht gelesen.

Genaue Bereichsverhältnisse und der Inhalt der Werkzeugleisten wurden nicht gemessen. Nicht verifiziert.

## Barrierefreiheit laut Quellcode

- Symbolschaltflächen haben ein `aria-label` (geprüft in `HeaderNav.vue`, `PageActionsCol.vue`).
- Tastaturfokus und ein „Überspringen“-Mechanismus wurden nicht geprüft. Nicht verifiziert.

## Nicht verifiziert

- Responsive Haltepunkte in Pixeln. Das Layout nutzt `composables/screen.js`; die Zahlen wurden nicht gelesen.
- Druck-Layout (`frontend/src/css/_print.scss` existiert; nicht gelesen).

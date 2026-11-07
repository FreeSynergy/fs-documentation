# Wiki.js 3.1.1: Menüs

Quellen: `frontend/src/routes.js` und die unten genannten Komponenten unter https://github.com/requarks/wiki/tree/3.1.1/frontend/src. Die Menüliste der alten Seite (Pages, Editor, Trash, Media, Users, Groups, Access, Settings, Appearance, Extensions, Logs, Search) wird durch die folgende Liste ersetzt, weil diese Namen nicht zur Oberfläche von 3.1.1 passen.

## Kopfzeilenmenü

| Eintrag | Wer ihn sieht | Ziel | Quelle |
|-------|-------------|--------|--------|
| Home | alle | Startseite des Standorts | `HeaderNav.vue` |
| Suche | alle | Suchzeile, dann `/_search` | `HeaderNav.vue` |
| Erstellen (+) → Neue Seite | Nutzer mit Schreibrechten | einen aktiven Editor wählen, dann `/_create/<editor>` | `HeaderNav.vue`, `helpers/editors.js` |
| Bibliothek | nicht geprüft | nicht geprüft | `HeaderNav.vue` |
| Posteingang | angemeldete Nutzer | `/_inbox/messages`, `/_inbox/watching`, `/_inbox/review/:id?` | `routes.js` |
| Administration | Nutzer mit Admin-Zugriff | `/_admin` | `HeaderNav.vue`, `routes.js` |
| Anmelden | Gäste | `/login` | `HeaderNav.vue` |
| Konto | angemeldete Nutzer | `/_profile/*` und Abmelden | `HeaderNav.vue` |

## Schubladenmenüs

| Menü | Inhalt | Quelle |
|------|---------|--------|
| Locale | Liste der Standort-Locales | `locale-selector-menu` in `MainLayout.vue` |
| Durchsuchen | Baum-Browser für Ordner und Seiten | `NavBrowseMenu.vue` |
| Edit Nav | Navigation bearbeiten: Einträge hinzufügen, bearbeiten, löschen | `NavEditMenu.vue`, `NavEditItemMenu.vue`, `NavEditOverlay.vue` |

## Seitenaktionsleiste

In `layout.md` aufgeführt. Die Schaltfläche „Actions (…)“ öffnet ein Menü mit `Convert Page` und `Rerender Page`; beide sind nur sichtbar, wenn der Nutzer Schreibrechte hat. Quelle: `PageActionsCol.vue`.

Weitere Punkte der Leiste: Duplicate, Rename / Move, Delete sowie die Ansichtsschaltflächen Page Properties, Page Data, History, Source.

## Profilmenü (`/_profile/*`)

| Abschnitt | Route | Quelle |
|-----------|-------|--------|
| Infos | `/_profile/info` | `routes.js` |
| Avatar | `/_profile/avatar` | `routes.js` |
| Authentifizierung (Passwörter, 2FA, Passkeys) | `/_profile/auth` | `routes.js` |
| Gruppen | `/_profile/groups` | `routes.js` |
| Live-Notizen | `/_profile/notes` | `routes.js` |
| Zugriffstoken | `/_profile/tokens` | `routes.js` |
| Benachrichtigungen | `/_profile/notifications` | `routes.js` |

## Posteingang (`/_inbox/*`)

| Reiter | Route | Inhalt |
|-----|-----|--------|
| Nachrichten | `/_inbox/messages` | Benachrichtigungen |
| Beobachtet | `/_inbox/watching` | Seiten, die der Nutzer beobachtet |
| Prüfung | `/_inbox/review/:submissionId?` | Änderungsvorschläge und Freigaben (Prüfer) |

## Administration (`/_admin/*`)

Jeder Abschnitt unten ist eine Route in `frontend/src/router/routes.js`. Standortbezogene Abschnitte nehmen ein Segment `:siteid`. Die Rechteprüfungen laufen auf dem Server (`permissions: ['access:admin']` ist das Beispiel aus `backend/api/pages.ts`).

| Gruppe | Abschnitte (Routenname) |
|-------|-----------------------|
| Übersicht | Dashboard (`dashboard`), Standorte (`sites`) |
| Standort (`:siteid/…`) | Allgemein (General), Freigaben (Approvals), Analytik (Analytics), Blöcke (Blocks), Kommentare (Comments), Editoren (Editors), Locale, Anmeldung (Login), Navigation, Speicher (Storage), Theme |
| Konten | Authentifizierung (`auth`), Gruppen (`groups`), Nutzer (`users`), SCIM (`scim`) |
| Integration | API (`api`), MCP (`mcp`), Webhooks (`webhooks`) |
| System | Audit, Erweiterungen (Extensions), Icons, Instanzen (Instances), Mail, Metriken (Metrics), Benachrichtigungen, Rendering, Scheduler, Suche (Search), Sicherheit (Security), System, Terminal, Hilfsprogramme (Utilities), Flags |

## Kontextmenüs

| Kontext | Einträge | Quelle |
|---------|----------|--------|
| Editor-Einfügen (Monaco, Markdown) | fett, kursiv, Überschriftenebene und die eigenen Kontextaktionen von Monaco | `EditorMarkdown.vue` (`editor.addAction`) |
| Blockmenü des Visual-Editors | Slash-Menüeinträge | `frontend/src/editor/visual/slash.js` |
| Codeblock-Menü | Aktionen für Codeblöcke | `frontend/src/components/EditorCodeBlockMenu.vue` |
| Emoji-Menü | Emoji-Auswahl | `frontend/src/components/EditorEmojiMenu.vue` |
| Reiter-Block (Visual) | neuer Reiter, Reiter entfernen, Reitersatz entfernen | Locale `editor.visual.tabs.*` |

## Menüs nach Rolle

Menüs werden auf dem Client gefiltert und auf dem Server erneut geprüft. Im Quellcode verifizierte Beispiele:

| Menüeintrag | Voraussetzung | Quelle |
|-----------|-----------|--------|
| Rerender Page, Convert Page | `write:pages` | `PageActionsCol.vue` |
| Administration | Admin-Zugriff | `HeaderNav.vue`, `routes.js` |
| Edit Nav | Recht, die Navigation zu bearbeiten | `MainLayout.vue` (`showEditNav`) |
| Erstellen (+) | Schreibrecht für mindestens einen aktiven Editor | `HeaderNav.vue` (nicht Zeile für Zeile gelesen) |

Gäste (nicht angemeldet) sehen Aktionen für Änderungsvorschläge statt Bearbeitungsaktionen (Locale `common.actions.suggestEdits`).

## Nicht verifiziert

- Die vollständige Liste der Einträge unter der Schaltfläche Bibliothek.
- Genaue Reihenfolge der Einträge in jedem Menü.
- Ob der Papierkorb nur im Admin-Bereich liegt. Der Locale-Text sagt, dass gelöschte Seiten „aus dem Verwaltungsbereich“ wiederhergestellt werden können.

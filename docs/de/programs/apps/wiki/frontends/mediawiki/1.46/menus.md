# MediaWiki 1.46 — Menüs

Version: 1.46.2. Quellen: Vorlagen und Portlet-Code von Vector 2022 im Skin-Repository REL1_46 (https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46: `includes/templates/skin.mustache`, `includes/SkinVector22.php`, `includes/Components/VectorComponentPageTools.php`), Tooltip-Meldungen in `languages/i18n/en.json` (https://github.com/wikimedia/mediawiki/blob/REL1_46/languages/i18n/en.json).

Die Menüinhalte sind nicht festgelegt. Welche Einträge erscheinen, hängt von der Skin, den geladenen Erweiterungen, dem Namensraum der Seite und den Benutzerrechten ab. Die bestehende Seite listete Menüs, als wären sie festgelegt; siehe `../changelog.md`.

## Menügruppen in Vector 2022

| Gruppe (Portlet) | Ort | Typischer Inhalt | Quelle |
|------------------|-----|------------------|--------|
| Persönliche Werkzeuge (`data-personal`) | Kopfzeile, rechts | Benutzerseite, Diskussionsseite, Beiträge, Einstellungen, Beobachtungsliste, Abmelden oder Anmelden | `skin.mustache`, Liste der data-portlets |
| Zugehörige Seiten (`data-associated-pages`) | Werkzeugleiste | Reiter des Namensraums: Inhaltsseite und Diskussionsseite | `skin.mustache` |
| Varianten (`data-variants`) | Werkzeugleiste | Sprach- oder Schriftvarianten, wo das Wiki sie hat | `skin.mustache` |
| Ansichten (`data-views`) | Werkzeugleiste | Lesen, Bearbeiten (Quelltext oder VisualEditor), Versionsverlauf anzeigen | `skin.mustache` |
| Aktionen (`data-actions`) | Werkzeugleiste | weitere Seitenaktionen wie verschieben, schützen, löschen, beobachten | `skin.mustache` |
| Werkzeuge (Seitenwerkzeuge) | rechte Leiste oder Dropdown | Links auf diese Seite, verwandte Änderungen, dauerhafter Link, Seiteninformationen, drucken | `PageTools.mustache`, `tooltip-t-whatlinkshere`, `tooltip-t-recentchangeslinked`, `tooltip-t-permalink`, `tooltip-t-info`, `tooltip-t-print` |
| Hauptmenü | linke Seitenleiste | Website-Navigation (Hauptseite, letzte Änderungen, Zufallsseite, Hilfe, Gemeinschaftsportal, Hochladen, Spezialseiten) | `MainMenu.mustache`; Tooltips `tooltip-n-mainpage`, `tooltip-n-recentchanges`, `tooltip-n-randompage`, `tooltip-n-help`, `tooltip-n-portal`, `tooltip-t-upload` |

## Einträge mit geprüftem Tooltip

Dies sind die englischen Tooltip-Texte. Die Beschriftungen, die ein Benutzer sieht, stammen aus den Meldungsschlüsseln mit denselben Namen in derselben Datei.

| Eintrag | Tooltip-Meldung | Text (Englisch) |
|---------|-----------------|-----------------|
| Bearbeiten | `tooltip-ca-edit` | Edit this page |
| Verlauf | `tooltip-ca-history` | Past revisions of this page |
| Diskussion | `tooltip-ca-talk` | Discussion about the content page |
| Beobachten | `tooltip-ca-watch` | Add this page to your watchlist |
| Nicht mehr beobachten | `tooltip-ca-unwatch` | Remove this page from your watchlist |
| Verschieben | `tooltip-ca-move` | Move this page |
| Löschen | `tooltip-ca-delete` | Delete this page |
| Schützen | `tooltip-ca-protect` | Protect this page |
| Drucken | `tooltip-t-print` | Printable version of this page |
| Dauerhafter Link | `tooltip-t-permalink` | Permanent link to this revision of this page |
| Seiteninformationen | `tooltip-t-info` | More information about this page |
| Links auf diese Seite | `tooltip-t-whatlinkshere` | A list of all wiki pages that link here |
| Verwandte Änderungen | `tooltip-t-recentchangeslinked` | (Meldung existiert; Text in diesem Lauf nicht geprüft) |
| Anmelden | `tooltip-pt-login` | You are encouraged to log in; however, it is not mandatory |
| Abmelden | `tooltip-pt-logout` | Log out |
| Einstellungen | `tooltip-pt-preferences` | Your preferences (geschlechtsabhängiger Text) |
| Beiträge | `tooltip-pt-mycontris` | A list of your contributions |
| Beobachtungsliste | `tooltip-pt-watchlist` | A list of pages you are monitoring for changes |
| Hochladen | `tooltip-t-upload` | Upload files |
| Letzte Änderungen | `tooltip-n-recentchanges` | A list of recent changes in the wiki |
| Zufallsseite | `tooltip-n-randompage` | Load a random page |
| Hauptseite | `tooltip-n-mainpage` | Visit the main page |
| Spezialseiten | `tooltip-t-specialpages` | (Text ist in en.json "None"; der Eintrag hat keinen Tooltip) |

## Menüs nach Rolle

Nicht geprüft. Welche Aktion jede Rolle sieht, hängt von den Rechten in `$wgGroupPermissions` und vom Code der Hooks ab. Die rollenbezogenen Listen der bestehenden Seite wurden nicht geprüft und sind in `../changelog.md` markiert.

## Kontextmenüs

MediaWiki-Kern hat kein allgemeines Kontextmenü per Rechtsklick auf Seiten. Kontextähnliche Menüs (Dropdowns zum Bearbeiten, Vergleichswerkzeuge) sind Teil der Werkzeugleiste und der Editoren. Der genaue Inhalt der Dropdowns im Editor hängt vom Editor ab (Wikitext-Quelltext oder VisualEditor) und ist hier nicht aufgeführt (ungeprüft).

## Hinweise für unser Frontend

- Ein benanntes, gruppiertes Menümodell führen: persönlich, Ansichten, Aktionen, Werkzeuge, Hauptmenü.
- Die Menüeinträge von Rechten abhängig machen. Rollenlisten nicht fest codieren.
- Tooltip-Texte nur als Referenz für die Bedeutung verwenden. Unsere eigenen Beschriftungen formulieren wir selbst.

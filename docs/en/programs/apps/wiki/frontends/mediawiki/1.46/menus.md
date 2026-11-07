# MediaWiki 1.46 — Menus

Version: 1.46.2. Sources: Vector 2022 templates and portlet code in the REL1_46 skin repository (https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46: `includes/templates/skin.mustache`, `includes/SkinVector22.php`, `includes/Components/VectorComponentPageTools.php`), tooltip messages in `languages/i18n/en.json` (https://github.com/wikimedia/mediawiki/blob/REL1_46/languages/i18n/en.json).

The menu contents are not fixed. Which items appear depends on the skin, the extensions loaded, the namespace of the page and the user rights. The existing page listed menus as if they were fixed; see `../changelog.md`.

## Menu groups in Vector 2022

| Group (portlet) | Where | Typical content | Source |
|-----------------|-------|-----------------|--------|
| Personal tools (`data-personal`) | header, right | user page, talk page, contributions, preferences, watchlist, log out or log in | `skin.mustache` data-portlets list |
| Associated pages (`data-associated-pages`) | toolbar | namespace tabs: content page and talk page | `skin.mustache` |
| Variants (`data-variants`) | toolbar | language or script variants where the wiki has them | `skin.mustache` |
| Views (`data-views`) | toolbar | Read, Edit (source or VisualEditor), View history | `skin.mustache` |
| Actions (`data-actions`) | toolbar | more page actions such as move, protect, delete, watch | `skin.mustache` |
| Tools (page tools) | right rail or dropdown | what links here, related changes, permanent link, page information, print | `PageTools.mustache`, `tooltip-t-whatlinkshere`, `tooltip-t-recentchangeslinked`, `tooltip-t-permalink`, `tooltip-t-info`, `tooltip-t-print` |
| Main menu | left sidebar | site navigation (main page, recent changes, random page, help, community portal, upload, special pages) | `MainMenu.mustache`; tooltips `tooltip-n-mainpage`, `tooltip-n-recentchanges`, `tooltip-n-randompage`, `tooltip-n-help`, `tooltip-n-portal`, `tooltip-t-upload` |

## Items with a verified tooltip

These are the English tooltip texts. The labels a user sees come from the message keys with the same names in the same file.

| Item | Tooltip message | Text (English) |
|------|-----------------|----------------|
| Edit | `tooltip-ca-edit` | Edit this page |
| History | `tooltip-ca-history` | Past revisions of this page |
| Talk | `tooltip-ca-talk` | Discussion about the content page |
| Watch | `tooltip-ca-watch` | Add this page to your watchlist |
| Unwatch | `tooltip-ca-unwatch` | Remove this page from your watchlist |
| Move | `tooltip-ca-move` | Move this page |
| Delete | `tooltip-ca-delete` | Delete this page |
| Protect | `tooltip-ca-protect` | Protect this page |
| Print | `tooltip-t-print` | Printable version of this page |
| Permanent link | `tooltip-t-permalink` | Permanent link to this revision of this page |
| Page information | `tooltip-t-info` | More information about this page |
| What links here | `tooltip-t-whatlinkshere` | A list of all wiki pages that link here |
| Related changes | `tooltip-t-recentchangeslinked` | (message exists; text not checked in this run) |
| Log in | `tooltip-pt-login` | You are encouraged to log in; however, it is not mandatory |
| Log out | `tooltip-pt-logout` | Log out |
| Preferences | `tooltip-pt-preferences` | Your preferences (gender-dependent text) |
| Contributions | `tooltip-pt-mycontris` | A list of your contributions |
| Watchlist | `tooltip-pt-watchlist` | A list of pages you are monitoring for changes |
| Upload | `tooltip-t-upload` | Upload files |
| Recent changes | `tooltip-n-recentchanges` | A list of recent changes in the wiki |
| Random page | `tooltip-n-randompage` | Load a random page |
| Main page | `tooltip-n-mainpage` | Visit the main page |
| Special pages | `tooltip-t-specialpages` | (text is "None" in en.json; the item has no tooltip) |

## Menus by role

Not verified. Which action each role sees depends on the rights in `$wgGroupPermissions` and on hook code. The existing page's per-role lists were not checked and are marked in `../changelog.md`.

## Context menus

MediaWiki core has no general right-click context menu on pages. Context-like menus (edit dropdowns, diff tools) are part of the toolbar and the editors. Exact contents of editor dropdowns depend on the editor (wikitext source vs VisualEditor) and are not listed here (unverified).

## Notes for our frontend

- Keep a named, grouped menu model: personal, views, actions, tools, main menu.
- Let the menu items depend on rights. Do not hard-code role lists.
- Use tooltip texts only as a reference for meaning. Our own labels are written in our own words.

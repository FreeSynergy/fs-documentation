# MediaWiki 1.46 — Funktionen (was es kann und was nicht)

Version: 1.46.2. Funktionsliste geprüft gegen https://www.mediawiki.org/wiki/MediaWiki_1.46, https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46 und den Quellbaum REL1_46 (https://github.com/wikimedia/mediawiki/tree/REL1_46).

"Kern" bedeutet: im Repository des MediaWiki-Kerns vorhanden. "Erweiterung" bedeutet: ein eigenes Repository, das durch die Konfiguration geladen wird.

## Kann (Kern)

| Funktion | Kern? | Nachweis |
|----------|-------|----------|
| Seiten in Wikitext lesen, erstellen und bearbeiten | ja | Action-API-Modul `edit` (`includes/Api/ApiEditPage.php`) |
| Bearbeitung vor dem Speichern in der Vorschau ansehen | ja | Tooltip der Bearbeitungsleiste `tooltip-preview` (`languages/i18n/en.json`) |
| Unterschied zwischen Versionen anzeigen | ja | REST-Route `compare` und `tooltip-diff` |
| Versionsverlauf | ja | Tooltip `history` `tooltip-ca-history`; REST `/v1/page/{title}/history` (`coreRoutes.json`) |
| Mehrere Versionen auf einmal rückgängig machen (fügt eine automatische Zusammenfassung hinzu) | ja, neu in 1.46 | RELEASE-NOTES-1.46, "New user-facing features" |
| Zurücksetzen auf den letzten Bearbeiter | ja | `ApiRollback.php`; Token-Typ `rollback` (`ApiQueryTokens.php`) |
| Seite verschieben (umbenennen), mit Weiterleitung und Diskussionsseite | ja | `ApiMove.php`; 1.46 kann über eine bestehende Diskussionsseite verschieben (RELEASE-NOTES-1.46) |
| Löschen und Wiederherstellen | ja | `ApiDelete.php`, `ApiQueryDeletedRevisions.php` |
| Schützen und Schutz aufheben | ja | `ApiProtect.php` |
| Benutzer sperren und entsperren | ja | `ApiBlock.php`, `ApiUnblock.php` |
| Benutzerrechte (Gruppen) ändern | ja | `ApiUserrights.php`; Token-Typ `userrights` |
| Beobachtungsliste (beobachten, nicht mehr beobachten, auflisten) | ja | `ApiWatch.php`, `ApiQueryWatchlist.php`, `ApiQueryWatchlistRaw.php`; `tooltip-ca-watch`, `tooltip-pt-watchlist` |
| Liste der letzten Änderungen mit Filtern | ja | `ApiQueryRecentChanges.php`; API:RecentChanges |
| Kategorien (Mitgliedschaft und Auflistung) | ja | `ApiQueryCategories.php`, `ApiQueryCategoryMembers.php` |
| Dateien hochladen | ja | `ApiUpload.php`; `tooltip-t-upload` |
| Volltext- und Titelsuche | ja (einfach) | `ApiQuerySearch.php`, `ApiQueryPrefixSearch.php`; Wahl des Suchsystems ungeprüft |
| Diskussionsseite zu jeder Inhaltsseite | ja | `tooltip-ca-talk`, `tooltip-pt-mytalk` (Namensraummodell) |
| Weiterleitungen | ja | REST `RedirectHandler` (coreRoutes.json) |
| Sprachverknüpfungen zwischen Seiten | ja | REST `/v1/page/{title}/links/language` (coreRoutes.json) |
| Persönliche Einstellungen | ja | `tooltip-pt-preferences`; Liste der Vector-Einstellungen (`doc/configuration/configuration.md`) |
| Druckversion | ja | `tooltip-t-print` |
| Dauerhafter Link zu einer Version | ja | `tooltip-t-permalink` |
| Bot-Passwörter für Skripte | ja | `includes/User/BotPassword.php` |
| Spezialseiten (Listen, Verwaltungswerkzeuge) | ja | Spezialseiten existieren; vollständige Liste in diesem Lauf ungeprüft |
| Umschalten der Oberflächensprache (`uselang`) | ja | RELEASE-NOTES-1.46: `uselang` bleibt bei der Vorschau erhalten |
| Markierungen der Beobachtungsliste | ja, aber standardmäßig aus | `$wgEnableWatchlistLabels` Standard `false` (RELEASE-NOTES-1.46) |

## Kann nicht (Kern), oder nur mit einer Erweiterung

| Funktion | Status | Nachweis |
|----------|--------|----------|
| OAuth-Anmeldung für Werkzeuge Dritter | Erweiterung | kein OAuth-Modul im Kernbaum REL1_46; API:Login empfiehlt OAuth, "wenn es verfügbar ist" |
| LDAP-Anmeldung | Erweiterung | keine LDAP-Datei im Kernbaum REL1_46 |
| Benachrichtigungen (Hinweise, E-Mail-Übersichten) | Erweiterung (Echo) | https://www.mediawiki.org/wiki/Extension:Echo |
| Webhooks (HTTP-Push an eine URL) | nicht in Echo | Die Echo-Seite beschreibt Push-Einstellungen und Benachrichtigungen; keine URL-Webhook-Funktion gefunden (siehe `../../changelog.md`) |
| Quelltexteditor mit Syntaxhervorhebung | Erweiterung (CodeMirror) | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| Visueller (WYSIWYG-) Editor | Erweiterung (VisualEditor) | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| GraphQL-Endpunkt | nicht im Kern | keine GraphQL-Datei im Baum REL1_46; die bestehende Seite ist falsch |
| Gleichzeitiges Bearbeiten einer Seite in Echtzeit | ungeprüft | in keiner gelesenen offiziellen Seite gefunden |
| Ziehen und Ablegen von Dateien in den Quelltexteditor | ungeprüft | nicht geprüft |
| Dunkelmodus pro Benutzer | ja, in Vector 2022 | Einstellung `vector-theme`: day, night, os (`doc/configuration/configuration.md`) |

## Editoren

| Editor | Kern? | Fakten |
|--------|-------|--------|
| Wikitext-Quelltexteditor | ja (Seitenformular) | Einfaches Textfeld mit Bearbeitungsleiste und Speichern/Vorschau über Zugriffstasten (`shortcuts.md`). Die Erweiterung CodeMirror ergänzt Hervorhebung, Zeilennummern, Suche, Sprung zu Zeile, Klammerabgleich und einen Dialog mit Tastenkürzeln (https://www.mediawiki.org/wiki/Extension:CodeMirror). |
| VisualEditor | Erweiterung | Rich-Text-Oberfläche mit Ctrl+B, Ctrl+I, Ctrl+K, Ctrl+Z, Ctrl+Shift+Z, Vorlagendialog, Zitaten (https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts). Kann pro Wiki abgeschaltet werden. |
| CodeMirror als Standard | ab 1.47 (laut Erweiterungsseite) | "Ab MediaWiki 1.47 verwenden die meisten Integrationen CodeMirror standardmäßig, außer dem Dialog für Codeblöcke im VisualEditor" (https://www.mediawiki.org/wiki/Extension:CodeMirror). 1.47 ist am 2026-11-07 nicht veröffentlicht. |

## Hinweise für unser Frontend

- Keine VisualEditor-Gleichwertigkeit versprechen. Es ist eine große, eigenständige Codebasis.
- Den Editor als einfachen Texteditor mit Werkzeugleiste planen. Die Aktionen der Leiste werden auf Wikitext-Ausschnitte abgebildet. Die Tastenkürzel für diese Aktionen sind unser eigenes Design, nicht das von MediaWiki (siehe `shortcuts.md`).
- Der "Quelltexteditor" der bestehenden Seite beschrieb Funktionen (Zeilennummern, Syntaxfärbung, Unterschied in geteilter Ansicht). Zeilennummern und Hervorhebung kommen von CodeMirror, nicht vom Kern. Die Angabe zur geteilten Ansicht ist ungeprüft.

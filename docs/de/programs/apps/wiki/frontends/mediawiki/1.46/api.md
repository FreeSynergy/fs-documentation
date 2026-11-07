# MediaWiki 1.46 — APIs, Authentifizierung, Ratenbegrenzungen

Version: 1.46.2. Quellen sind je Abschnitt angegeben. "Quellbaum" meint https://github.com/wikimedia/mediawiki/tree/REL1_46.

## 1. Action API (`api.php`)

- Endpunkt-Muster: `https://<host>/<script path>/api.php`. Der Pfad unterscheidet sich je Wiki (zum Beispiel `/w/api.php` auf Wikimedia-Seiten). Zu finden auf Special:Version. Quelle: https://www.mediawiki.org/wiki/API:Main_page (Abschnitt Endpunkt).
- Parameter: `action=<module>` plus Modulparameter. Abfragen verwenden `action=query` mit `list=`, `prop=`, `meta=` oder `generator=`. Quelle: https://www.mediawiki.org/wiki/API:Main_page
- Ausgabeformate: `json`, `jsonfm`, `none`, `rawfm`, `xml`, `xmlfm`. Der Serverstandard ist `jsonfm` (HTML-Seitenausgabe). Maschinelle Clients müssen `format=json` übergeben. Quellen: https://www.mediawiki.org/wiki/API:Main_page; `API_DEFAULT_FORMAT = 'jsonfm'` in `includes/Api/ApiMain.php`.
- `xml` und `xmlfm` haben in 1.46 den Parameter `xslt` verloren (RELEASE-NOTES-1.46, "Action API changes").
- `action=parse` mit `prop=sections` ist in 1.46 veraltet; `prop=tocdata` verwenden (RELEASE-NOTES-1.46).

### Im Quellbaum geprüfte Module (REL1_46)

| Zweck | Modul | Quelldatei |
|-------|-------|------------|
| Seite erstellen oder bearbeiten | `action=edit` | `ApiEditPage.php` |
| Löschen / Verschieben / Schützen | `action=delete`, `action=move`, `action=protect` | `ApiDelete.php`, `ApiMove.php`, `ApiProtect.php` |
| Cache leeren | `action=purge` | `ApiPurge.php` |
| Zurücksetzen | `action=rollback` | `ApiRollback.php` |
| Hochladen | `action=upload` | `ApiUpload.php` |
| Beobachten | `action=watch` | `ApiWatch.php` (es gibt einen Token-Typ für Beobachtung, siehe Tokens) |
| Sperren / Entsperren | `action=block`, `action=unblock` | `ApiBlock.php`, `ApiUnblock.php` |
| Benutzerrechte | `action=userrights` | `ApiUserrights.php` |
| Anmelden / Abmelden | `action=clientlogin`, `action=login`, `action=logout` | `ApiClientLogin.php`, `ApiLogin.php`, `ApiLogout.php` |
| Wikitext parsen | `action=parse` | `ApiParse.php` |
| Suchvorschläge | `action=opensearch` | `ApiOpenSearch.php` |
| Feed der letzten Änderungen | `action=feedrecentchanges` | `ApiFeedRecentChanges.php` (Parameter nicht gelesen) |
| Alle Seiten | `list=allpages` | `ApiQueryAllPages.php` |
| Alle Dateien | `list=allimages` | `ApiQueryAllImages.php` |
| Auf einer Seite verwendete Dateien | `prop=images` | `ApiQueryImages.php` |
| Suche | `list=search`, `list=prefixsearch` | `ApiQuerySearch.php`, `ApiQueryPrefixSearch.php` |
| Letzte Änderungen | `list=recentchanges` | `ApiQueryRecentChanges.php` |
| Beobachtungsliste | `list=watchlist`, `list=watchlistraw` | `ApiQueryWatchlist.php`, `ApiQueryWatchlistRaw.php` |
| Versionen | `prop=revisions` | `ApiQueryRevisions.php` |
| Gelöschte Versionen | `list=deletedrevs` (Moduldatei heißt `ApiQueryDeletedRevisions.php`) | `ApiQueryDeletedRevisions.php` |
| Kategorien einer Seite | `prop=categories` | `ApiQueryCategories.php` |
| Kategorienmitglieder | `list=categorymembers` | `ApiQueryCategoryMembers.php` |
| Links / Rückverweise | `prop=links`, `list=backlinks` | `ApiQueryLinks.php`, `ApiQueryBacklinks.php` |
| Benutzer | `list=users`, `meta=userinfo` | `ApiQueryUsers.php`, `ApiQueryUserInfo.php` |
| Beiträge | `list=usercontribs` | `ApiQueryUserContribs.php` |
| Tokens | `meta=tokens` | `ApiQueryTokens.php` |

Modulnamen stammen aus den Dateinamen und der dokumentierten API; der genaue registrierte Name jedes Moduls sollte vor der Verwendung mit `action=help` auf einem Live-Wiki bestätigt werden. Die Namen `list=deletedrevs` und `list=usercontribs` stammen aus der dokumentierten API und wurden in diesem Lauf nicht gelesen.

### Nicht im Kern von REL1_46 (geprüft)

- `action=deletefile` hat im Baum keine Datei `ApiDeleteFile.php`. Das Löschen von Dateien läuft über `action=delete` auf der Dateiseite (welchen Pfad der Code nutzt, ist ungeprüft; keine Datei gefunden).
- `list=images` existiert nicht als oberste Liste. `list=allimages` listet Dateien; `prop=images` listet die Dateien, die eine Seite verwendet.
- `list=userprop` existiert nicht; Benutzereigenschaften kommen aus `list=users` (`usprop`) und `meta=userinfo`.
- `action=history` existiert nicht; der Versionsverlauf ist `prop=revisions` oder die REST-Route `/v1/page/{title}/history`.
- `meta=globalinfo` ist nicht im Kern (keine `ApiQueryGlobalInfo.php`); es gehört zu einer Erweiterung.
- GraphQL ist nicht im Kern (kein GraphQL-Modul im Baum).

## 2. Tokens

Schreibaktionen benötigen ein Token. Token-Typen im Kern (`ApiQueryTokens.php`, `getTokenTypeSalts`): `csrf`, `watch`, `patrol`, `rollback`, `userrights`, `login`, `createaccount`. Ein Hook kann weitere hinzufügen.

| Verwendung | Token-Typ | Aufruf |
|------------|-----------|--------|
| Bearbeiten, Löschen, Verschieben, Schützen, Hochladen | `csrf` | `action=query&meta=tokens&type=csrf` |
| Anmeldung (clientlogin) | `login` | `action=query&meta=tokens&type=login` |
| Zurücksetzen | `rollback` | `type=rollback` |
| Beobachten | `watch` | `type=watch` |

Der Token-Typ `edit` (das alte `edittoken`) steht nicht in der Liste; das `type=edit` der bestehenden Seite ist daher falsch (siehe `../changelog.md`). Quelle: `includes/Api/ApiQueryTokens.php`.

## 3. Authentifizierung

| Methode | Status | Quelle |
|---------|--------|--------|
| Sitzungscookies aus einer normalen Anmeldung | ja; Clients müssen Cookies bei allen Anfragen behalten | https://www.mediawiki.org/wiki/API:Login |
| `clientlogin` (Token, Felder, Status PASS/FAIL/UI/REDIRECT/RESTART) | für interaktive Clients empfohlen | API:Login |
| Aktion `login` | veraltet; für Hauptkonten nicht mehr vorgesehen; für Bot-Passwörter | API:Login |
| Bot-Passwörter | im Kern (`includes/User/BotPassword.php`, `BotPasswordSessionProvider.php`); von API:Login empfohlen, wenn OAuth nicht verfügbar ist | API:Login, Quellbaum |
| OAuth 1.0a / OAuth 2 | nicht im Kern; OAuth ist eine Erweiterung. Die Angabe "OAuth 1.0a" der bestehenden Seite ist für den Kern nicht geprüft. API:Login sagt, OAuth sei zu bevorzugen, "wenn es verfügbar ist". | API:Login |
| LDAP, PATRICIA, andere Tokens | im Kern nicht gefunden | Quellbaum |
| `assert=user` / `assert=bot` | prüft den angemeldeten Zustand des Aufrufs | https://www.mediawiki.org/wiki/API:Main_page (Abschnitt Authentifizierung, nur Zusammenfassung) |

Die Seite API:Login wurde über eine Zusammenfassung gelesen (mediawiki.org lieferte für einige API-Seiten in diesem Lauf HTTP 403 bei direktem Abruf). Die Anmeldeschritte auf einem Testwiki bestätigen.

## 4. REST API (`rest.php`)

- Basis: `https://<host>/<script path>/rest.php/v1/...`. Quelle: https://www.mediawiki.org/wiki/API:REST_API (Zusammenfassung) und Quellbaum (`rest.php`).
- Kleinere Auswahl als die Action API: Seiten, Versionen, Suche, Transformationen, Verlauf, Lint, Dateilinks, Sitemap, OpenSearch-Beschreibung. Quelle: `includes/Rest/coreRoutes.json` (REL1_46).
- Leseroutes (Beispiele aus `coreRoutes.json`):
  - `GET /v1/page/{title}` (Quelle), `/v1/page/{title}/html`, `/v1/page/{title}/bare`, `/v1/page/{title}/history`, `/v1/page/{title}/links/language`
  - `GET /v1/revision/{id}`, `/v1/revision/{id}/html`, `/v1/revision/{from}/compare/{to}`
  - `GET /v1/search/page`, `/v1/search/title`, `/v1/search` (OpenSearch)
  - `GET /v1/file/{title}`
- Schreibroutes: `PUT /v1/page/{title}` (aktualisieren), `POST /v1/page` (erstellen), `POST /v1/transform/...` (Wikitext und HTML umwandeln).
- Auth- und Token-Regeln für REST-Schreibvorgänge wurden in diesem Lauf nicht gelesen (ungeprüft).

## 5. Weitere Endpunkte

- Feed der letzten Änderungen: `action=feedrecentchanges` (Modul vorhanden). Feed-Einstellungen: `$wgFeed`, `$wgFeedLimit` (Standard 50), `$wgFeedCacheTimeout` (60), `$wgFeedDiffCutoff` (32768), in `includes/config-schema.php`.
- Lokalisierung: Meldungen werden über die Action API oder Special:AllMessages gelesen; nicht geprüft.

## 6. Client-Etikette (nur Zusammenfassung)

Quelle: https://www.mediawiki.org/wiki/API:Etiquette (HTTP 403 bei direktem Abruf; über eine Zusammenfassung gelesen).

- Einen aussagekräftigen User-Agent mit Kontaktdaten senden. Den String eines Browsers nicht kopieren. Wikimedia-Wikis können Clients ohne ihn per IP sperren.
- Für nicht interaktive Aufträge `maxlag=<seconds>` übergeben.
- Lesezugriffe nach Möglichkeit einzeln senden. Mit `|` als Trennzeichen bündeln.
- Bei `ratelimited` (Fehlercode) zurückhalten (exponentielles Zurückweichen wird als Strategie vorgeschlagen).

## 7. Client-Bibliotheken

In diesem Lauf nicht geprüft. Die Liste der bestehenden Seite (mwclient, wikipedia-api, mediawiki-api-client, mwapi, mediawiki-gems, go-mediawiki) wurde nicht bestätigt; als ungeprüft behandeln.

## Hinweise für unser Frontend

- Unsere Engine ist ein anderer Vertrag (texts.capnp). Die MediaWiki-API ist nur für Kompatibilität oder Migration (Import/Export) relevant.
- Die Token- und Fehlerbehandlung nach dem Muster der Action API modellieren: zuerst Token, dann Schreibvorgang, `ratelimited` und `maxlag` behandeln.

# MediaWiki 1.46 — APIs, authentication, rate limits

Version: 1.46.2. Sources are given per section. "Source tree" means https://github.com/wikimedia/mediawiki/tree/REL1_46.

## 1. Action API (`api.php`)

- Endpoint pattern: `https://<host>/<script path>/api.php`. The path differs per wiki (for example `/w/api.php` on Wikimedia sites). Find it on Special:Version. Source: https://www.mediawiki.org/wiki/API:Main_page (endpoint section).
- Parameters: `action=<module>` plus module parameters. Queries use `action=query` with `list=`, `prop=`, `meta=` or `generator=`. Source: https://www.mediawiki.org/wiki/API:Main_page
- Output formats: `json`, `jsonfm`, `none`, `rawfm`, `xml`, `xmlfm`. The server default is `jsonfm` (HTML page output). Machine clients must pass `format=json`. Sources: https://www.mediawiki.org/wiki/API:Main_page; `API_DEFAULT_FORMAT = 'jsonfm'` in `includes/Api/ApiMain.php`.
- `xml` and `xmlfm` lost the `xslt` parameter in 1.46 (RELEASE-NOTES-1.46, "Action API changes").
- `action=parse` `prop=sections` is deprecated in 1.46; use `prop=tocdata` (RELEASE-NOTES-1.46).

### Modules verified in the source tree (REL1_46)

| Purpose | Module | Source file |
|---------|--------|-------------|
| Create or edit a page | `action=edit` | `ApiEditPage.php` |
| Delete / move / protect | `action=delete`, `action=move`, `action=protect` | `ApiDelete.php`, `ApiMove.php`, `ApiProtect.php` |
| Purge cache | `action=purge` | `ApiPurge.php` |
| Rollback | `action=rollback` | `ApiRollback.php` |
| Upload | `action=upload` | `ApiUpload.php` |
| Watch | `action=watch` | `ApiWatch.php` (a watch token type exists, see tokens) |
| Block / unblock | `action=block`, `action=unblock` | `ApiBlock.php`, `ApiUnblock.php` |
| User rights | `action=userrights` | `ApiUserrights.php` |
| Login / logout | `action=clientlogin`, `action=login`, `action=logout` | `ApiClientLogin.php`, `ApiLogin.php`, `ApiLogout.php` |
| Parse wikitext | `action=parse` | `ApiParse.php` |
| Search suggestions | `action=opensearch` | `ApiOpenSearch.php` |
| Feed of recent changes | `action=feedrecentchanges` | `ApiFeedRecentChanges.php` (parameters not read) |
| All pages | `list=allpages` | `ApiQueryAllPages.php` |
| All files | `list=allimages` | `ApiQueryAllImages.php` |
| Files used on a page | `prop=images` | `ApiQueryImages.php` |
| Search | `list=search`, `list=prefixsearch` | `ApiQuerySearch.php`, `ApiQueryPrefixSearch.php` |
| Recent changes | `list=recentchanges` | `ApiQueryRecentChanges.php` |
| Watchlist | `list=watchlist`, `list=watchlistraw` | `ApiQueryWatchlist.php`, `ApiQueryWatchlistRaw.php` |
| Revisions | `prop=revisions` | `ApiQueryRevisions.php` |
| Deleted revisions | `list=deletedrevs` (module file is `ApiQueryDeletedRevisions.php`) | `ApiQueryDeletedRevisions.php` |
| Categories of a page | `prop=categories` | `ApiQueryCategories.php` |
| Category members | `list=categorymembers` | `ApiQueryCategoryMembers.php` |
| Links / backlinks | `prop=links`, `list=backlinks` | `ApiQueryLinks.php`, `ApiQueryBacklinks.php` |
| Users | `list=users`, `meta=userinfo` | `ApiQueryUsers.php`, `ApiQueryUserInfo.php` |
| Contributions | `list=usercontribs` | `ApiQueryUserContribs.php` |
| Tokens | `meta=tokens` | `ApiQueryTokens.php` |

Module names are from the file names and the documented API; the exact registered name of each module should be confirmed with `action=help` on a live wiki before use. `list=deletedrevs` and `list=usercontribs` names are from the documented API, not read in this run.

### Not in REL1_46 core (checked)

- `action=deletefile` has no file `ApiDeleteFile.php` in the tree. File deletion goes through `action=delete` on the File page (unverified which path the code uses; no file found).
- `list=images` does not exist as a top-level list. `list=allimages` lists files; `prop=images` lists files used by a page.
- `list=userprop` does not exist; user properties come from `list=users` (`usprop`) and `meta=userinfo`.
- `action=history` does not exist; revision history is `prop=revisions`, or the REST `/v1/page/{title}/history`.
- `meta=globalinfo` is not in core (no `ApiQueryGlobalInfo.php`); it belongs to an extension.
- GraphQL is not in core (no GraphQL module in the tree).

## 2. Tokens

Write actions need a token. Token types in core (`ApiQueryTokens.php`, `getTokenTypeSalts`): `csrf`, `watch`, `patrol`, `rollback`, `userrights`, `login`, `createaccount`. A hook can add more.

| Use | Token type | Call |
|-----|-----------|------|
| Edit, delete, move, protect, upload | `csrf` | `action=query&meta=tokens&type=csrf` |
| Login (clientlogin) | `login` | `action=query&meta=tokens&type=login` |
| Rollback | `rollback` | `type=rollback` |
| Watch | `watch` | `type=watch` |

The token type `edit` (the old `edittoken`) is not in the list, so the existing page's `type=edit` is wrong (see `../changelog.md`). Source: `includes/Api/ApiQueryTokens.php`.

## 3. Authentication

| Method | Status | Source |
|--------|--------|--------|
| Session cookies from a normal login | yes; clients must keep cookies on all requests | https://www.mediawiki.org/wiki/API:Login |
| `clientlogin` (token, fields, status PASS/FAIL/UI/REDIRECT/RESTART) | recommended for interactive clients | API:Login |
| `login` action | legacy; deprecated for main accounts; for bot passwords | API:Login |
| Bot passwords | in core (`includes/User/BotPassword.php`, `BotPasswordSessionProvider.php`); recommended by API:Login when OAuth is not available | API:Login, source tree |
| OAuth 1.0a / OAuth 2 | not in core; OAuth is an extension. The existing page's "OAuth 1.0a" claim is not verified for core. API:Login says prefer OAuth "if it is available". | API:Login |
| LDAP, PATRICIA, other tokens | not found in core | source tree |
| `assert=user` / `assert=bot` | verifies the logged-in state of the call | https://www.mediawiki.org/wiki/API:Main_page (Authentication section, summary-only) |

The API:Login page was read through a summary (mediawiki.org returned HTTP 403 to direct fetch for some API pages in this run). Confirm the login steps on a test wiki.

## 4. REST API (`rest.php`)

- Base: `https://<host>/<script path>/rest.php/v1/...`. Source: https://www.mediawiki.org/wiki/API:REST_API (summary) and the source tree (`rest.php`).
- Smaller set than the Action API: pages, revisions, search, transforms, history, lint, file links, sitemap, OpenSearch description. Source: `includes/Rest/coreRoutes.json` (REL1_46).
- Read routes (examples from `coreRoutes.json`):
  - `GET /v1/page/{title}` (source), `/v1/page/{title}/html`, `/v1/page/{title}/bare`, `/v1/page/{title}/history`, `/v1/page/{title}/links/language`
  - `GET /v1/revision/{id}`, `/v1/revision/{id}/html`, `/v1/revision/{from}/compare/{to}`
  - `GET /v1/search/page`, `/v1/search/title`, `/v1/search` (OpenSearch)
  - `GET /v1/file/{title}`
- Write routes: `PUT /v1/page/{title}` (update), `POST /v1/page` (create), `POST /v1/transform/...` (convert wikitext and HTML).
- Auth and token rules for REST writes were not read in this run (unverified).

## 5. Other endpoints

- Recent changes feed: `action=feedrecentchanges` (module exists). Feed settings: `$wgFeed`, `$wgFeedLimit` (50 default), `$wgFeedCacheTimeout` (60), `$wgFeedDiffCutoff` (32768), in `includes/config-schema.php`.
- Localisation: messages are read through the Action API or Special:AllMessages; not checked.

## 6. Client etiquette (summary-only)

Source: https://www.mediawiki.org/wiki/API:Etiquette (HTTP 403 to direct fetch; read through summary).

- Send a descriptive User-Agent with contact details. Do not copy a browser's string. Wikimedia wikis may IP-block clients without one.
- For non-interactive jobs, pass `maxlag=<seconds>`.
- Send reads one at a time where possible. Batch with `|` separators.
- On `ratelimited` (error code), back off (exponential backoff is the suggested strategy).

## 7. Client libraries

Not checked in this run. The existing page's list (mwclient, wikipedia-api, mediawiki-api-client, mwapi, mediawiki-gems, go-mediawiki) was not verified; treat as unverified.

## Notes for our frontend

- Our engine is a different contract (texts.capnp). The MediaWiki API is relevant only for compatibility or migration (import/export).
- Model our token and error handling on the Action API pattern: token first, then write, handle `ratelimited` and `maxlag`.

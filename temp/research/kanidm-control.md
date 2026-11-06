# Controlling Kanidm from a FreeSynergy wrapper

Research note. Retrieved 2026-11-06.

**Source read:** `https://github.com/kanidm/kanidm`, `master` at commit `8b5382f2037bcaf2bf84cb67e7e6353d73de173a`
(committed 2026-11-05 03:26 UTC), workspace version `1.13.0-dev`, licence MPL-2.0. Latest GitHub release:
`v1.12.0` (2026-11-01). Latest on crates.io: `kanidm_client 1.11.2` (2026-09-11). I downloaded the master tarball
through `gh api repos/kanidm/kanidm/tarball/master` and read it locally; paths below are relative to the repo root.
Issues were read through `gh api` (read only). No code was executed against a running Kanidm, so every claim of the
form "the server does X" comes from reading source, not from a test. Marker ⚠️ = unverified or inferred.

Context: ADR 0024 (Kanidm runs in the server behind the REST API, we program what is missing; SCIM shape still
changing, kanidm#4638) and ADR 0035 (OpenID Federation is added next to Kanidm, since Kanidm cannot do it).

---

## 1. Ways to control it

### 1.1 REST API
- **Route table:** `server/core/src/https/v1.rs`, `v1_oauth2.rs`, `v1_scim.rs`, `v1_domain.rs`. About 150 `utoipa`
  annotated operations.
- **OpenAPI:** yes, generated from code (`server/core/src/https/apidocs/mod.rs`, utoipa 5). Served at runtime as
  `/docs/v1/openapi.json` (OpenAPI 3.1.0, asserted in `server/testkit/tests/testkit/apidocs.rs`) and Swagger UI at
  `/docs/swagger-ui`. No checked-in `openapi.json` file in the repo (searched `find -name 'openapi*'`: only
  `pykanidm/kanidm/openapi*.py` and `scripts/openapi_tests`). The description itself says "This is a work in
  progress". ⚠️ The `paths(...)` list is hand-maintained (it has leftover commented-out duplicates), so I did not
  prove that it covers every route; the route table in `v1.rs` is the truth.
- **Authentication:** `Authorization: Bearer <JWT>` (security scheme `token_jwt`). Two ways to get a token:
  1. Interactive multi-step `POST /v1/auth` (password, TOTP, passkey, ...), session token, "read only" until
     `POST /v1/reauth` gives a short privileged window (privilege expiry at most 3600 s,
     `book/src/accounts/account_policy.md`).
  2. **Service-account API token**, optionally with an expiry, created with the read-write flag (`-w`). Used as
     Bearer token (`book/src/accounts/service_accounts.md`). This is the right fit for a machine wrapper. Bootstrap
     of the first admin: `kanidmd recover-account admin|idm_admin` (`book/src/server_configuration.md`).
  The wrapper's service account needs only the groups for what it does (`idm_group_admins`,
  `idm_account_policy_admins`, `idm_oauth2_admins`, ... all built in, `migration_data/dl15/groups.rs`).
- **Stability promise (this is the key finding)**, `book/src/support.md`, section "API stability":
  - *Stable* (breaking changes only for ethics, security or data corruption): LDAP operations and "JSON HTTP end
    points which use elements from `proto/src/v1`".
  - *Not stable*: JSON endpoints that use `proto/src/internal.rs` types, **SCIM operations from
    `proto/src/scim_v1`**, entry schema, CLI interface, unixd socket API, web UI.
  - Deprecation: "may be removed with 1 release notice", announced in `RELEASE_NOTES.md`.
  - Practical reading: group, person and service-account endpoints that exchange the plain `v1::Entry`
    (`attrs: BTreeMap<String, Vec<String>>`, `proto/src/v1/mod.rs:114`) are in the stable class. OAuth2, credential
    update, API tokens, schema and SCIM use `internal`/`scim_v1` types and are not. ⚠️ I did not check every
    endpoint's type origin one by one.
- **Version coupling:** the server adds header `X-KANIDM-VERSION` to responses
  (`server/core/src/https/middleware/mod.rs`, `proto/src/constants`). Support policy (`support.md`): CLI and sync
  tools "must be matched versions with the server at all times"; stable releases get 4 months of support; upgrades
  only from the previous minor.
- **Cadence:** releases 2026-02-17 (1.9), 2026-05-01 (1.10), 2026-08-01 (1.11), 2026-11-01 (1.12), that is
  quarterly (`RELEASE_NOTES.md`). Last 30 days up to 2026-11-05: 30 commits on master, 14 by the lead maintainer
  (Firstyear), 9 by dependabot (`gh api repos/kanidm/kanidm/commits?since=2026-10-06`). So: a small team, steady,
  conservative on API shape.

### 1.2 `kanidm_client` crate
- **Published:** yes, crates.io `kanidm_client`, 52 versions, newest 1.11.2 (2026-09-11), MPL-2.0, MSRV 1.96
  (crates.io API, `libs/client/Cargo.toml`). 59k downloads total. Version always equals the server version. At
  retrieval, crates.io is one release behind GitHub (1.11.2 vs v1.12.0) ⚠️ may be published later.
- **What it is:** the client the CLI itself uses (`tools/cli`). `KanidmClient` with ~200 `pub async fn`
  (`libs/client/src/lib.rs` 2212 lines, plus `group.rs`, `person.rs`, `service_account.rs`, `oauth.rs`,
  `sync_account.rs`, `scim.rs`, `system.rs`, `domain.rs`, `application.rs`, `schema.rs`). It also implements the
  login steps (`auth_step_*`, passkey and password flows) and the credential-update session helpers.
- **Public API?** The functions are `pub`, and the doc link is docs.rs, but `support.md` does not list the crate
  among the stable APIs, so by its own policy it is "not considered stable".
  Observed behaviours that matter for a wrapper:
  - It compares the server's `X-KANIDM-VERSION` to its own version and logs a warning on mismatch
    (`lib.rs expect_version`); **in debug builds (`cfg(debug_assertions)`) it calls `process::exit(1)`** unless
    `KANIDM_DEV_YOLO` is set. A wrapper built in debug mode would die on a version skew.
  - It pulls `kanidm_proto`, `reqwest`, `compact_jwt`, `webauthn-rs-proto` and others, and demands a very recent Rust
    (1.96).
  - MPL-2.0 is file-level copyleft: using it unmodified as a dependency is fine, modified Kanidm files must stay MPL.
    ⚠️ Compatibility with our own licence needs a decision outside this note.
- A Python client (`pykanidm/`) and a generated OpenAPI client (`pykanidm/kanidm_openapi_client`) also exist. ⚠️ Not
  evaluated.

### 1.3 CLI (`kanidm`, crate `kanidm_tools`)
- Thin wrapper over `kanidm_client` (`tools/cli/src/cli/*.rs`). Top-level: `login`, `reauth`, `session`, `self`,
  `person`, `group`, `service-account`, `graph` (prints the group graph as DOT), `system`, `recycle-bin`, hidden
  `schema` and `raw`, plus `oauth2`, `domain`, `webauthn`, `sync` (`tools/cli/src/cli/`).
- Has `--output json` (`OutputMode` in `tools/cli/src/opt/kanidm.rs`), but ⚠️ I did not check that every command
  honours it. Output text and flags are explicitly "not stable" (`support.md`). Needs a login token cache on disk
  and an interactive login unless a token is supplied. Poor fit for a daemon.

### 1.4 SCIM as implemented (`server/core/src/https/v1_scim.rs`, `proto/src/scim_v1/`, `libs/scim_proto/`)
- **Not RFC 7644 resource paths.** There is no `/Users` or `/Groups`. Instead:
  - `GET /scim/v1/Entry` (list: `filter`, `sortBy`, `sortOrder`, `startIndex`, `count`, `attributes`,
    `extAccessCheck`; type `ScimEntryGetQuery`, `proto/src/scim_v1/mod.rs:61`), `GET /scim/v1/Entry/{id}`.
  - `PUT /scim/v1/Entry` (set or remove any schema attribute by name, `ScimEntryPutGeneric`),
    `DELETE /scim/v1/Entry/{id}`.
  - `GET /scim/v1/Person/{id}`, `/Application` (GET, POST, GET/DELETE by id), `/Class`, `/Attribute` (schema),
    `/Message`, `/Feature`, plus `/scim/v1/Sync` (the sync-connector path) and `/v1/sync_account/*`.
  - Attribute names are Kanidm's own (`member`, `memberof`, `displayname`, ...); values use Kanidm-specific types
    (`ScimReference {uuid, value}`, `ScimOAuth2ScopeMap`, ...).
- **Write gaps:** `POST /scim/v1/Entry` calls `scim_entry_create(..., &[], ...)` with an empty class list
  (`v1_scim.rs:380`), and `ScimCreateEvent::try_from` returns `SC0027ClassSetInvalid` ("THIS IS A BUG") when the
  class list is empty (`server/lib/src/server/scim.rs:72-95`). Reading the code, **generic SCIM create cannot
  work on this commit**; only the typed Application POST and the internal web-UI group/person creation pass classes.
  ⚠️ Not executed. So creating groups/people via SCIM is not possible; use `POST /v1/group`, `/v1/person`.
- Pagination, sorting and filters exist (RFC 7644 sections 3.4.2.x are cited in the code). Batch operations
  are used internally for migrations (`ScimAssertEvent`, release notes: "scim-batch migration framework").
  ⚠️ I found no public batch HTTP endpoint.
- **Stability:** explicitly unstable (`support.md`), confirmed by maintainer Firstyear on kanidm#4638, 2026-10-28:
  "we are still changing the shape of that API and I don't want to declare it stable yet". The book still says SCIM
  is "only supported for synchronisation" (`book/src/supported_features.md`), also confirmed outdated by the
  maintainer's answer. The RFC refresh (RFC 9865/9967) asked about in that issue: no answer from the maintainer
  at retrieval.
- The issue kanidm#4227 (open, 2026-03-23) asks for **outbound** SCIM (Kanidm pushing to other systems). Not
  implemented. Maintainer: it would not provide decentralised authentication.

### 1.5 Recommendation for the wrapper
1. **Primary channel: REST v1 over HTTPS with a service-account API token (read-write),** called from our own thin
   Rust client that uses the stable `v1::Entry` shape for groups, people and service accounts. Reasons: the only
   surface with a written stability promise; one HTTP dependency we already have; no coupling to Kanidm's MSRV, to
   `kanidm_proto` releases, nor to the debug-build `exit(1)`; the OpenAPI file lets us check drift in CI.
2. **Use `kanidm_client` only where flows are intricate** (interactive login, credential-update/passkey ceremony,
   OAuth2 client helpers), and keep it behind the same wrapper trait, pinned to the server minor version. ⚠️ Decide
   later if even that is worth the dependency; an own implementation of those few endpoints is possible.
3. **SCIM: do not build on it yet** (unstable, no create). Read-only `GET /scim/v1/Entry` with filters is useful for
   bulk reads; plan an adapter slot for it (ADR 0024 already says so) and re-check when kanidm#4638 closes.
4. **CLI: only for operator tasks** (`kanidmd recover-account`, backups), never as the programmatic path.
5. **CI contract test:** start a pinned Kanidm container, fetch `/docs/v1/openapi.json`, run our adapter's smoke
   suite. Fail on any drift before upgrading the pinned version.

---

## 2. Capability table

"Client" = a function exists in `kanidm_client` (names shortened, prefix `idm_` omitted). "SCIM" = what
`/scim/v1/*` can do on this commit. Legend: Y = yes, P = partly, N = no, ? = unverified ⚠️.

| Capability | REST | Client crate | CLI | SCIM |
|---|---|---|---|---|
| People: create, read, update (name, displayname, legalname, mail), delete | Y `/v1/person`, `/v1/person/{id}`, `_attr/{attr}` | Y `person_account_*` | Y `person` | Read `GET /Person/{id}`, `/Entry`; update via `PUT /Entry`; create N (see 1.4) |
| Service accounts: CRUD, attrs | Y `/v1/service_account*` | Y `service_account_*` | Y `service-account` | Read, PUT only |
| Service account API tokens (read-only / read-write, expiry) | Y `/v1/service_account/{id}/_api_token` | Y `service_account_*_api_token` | Y | N |
| Groups: create (name, `entry_managed_by`), delete, rename | Y `/v1/group`, `/v1/group/{id}` (PATCH renames) | Y `group_create`, `group_delete`, `group_rename` | Y `group` | Read, PUT, DELETE; create N |
| Nested groups (group as member of group) | Y, just put a group in `member` | Y `group_*_members` (names or UUIDs) | Y `add-members` | PUT `member` |
| Membership add/remove/set/purge | Y `/v1/group/{id}/_attr/member` (POST/PUT/DELETE) | Y `group_add_members`, `_remove_`, `_set_`, `_purge_` | Y | PUT `member` (replaces) |
| Read effective membership (`memberof`, `directmemberof`) | Y on the entry | Y via entry | Y `person get` | Y read attrs ⚠️ |
| Dynamic groups (`dyngroup_filter`) | ? `dyngroup` class exists in schema, no group-admin ACP for it | N | N | ? |
| Group description, mail | Y `_attr/description`, `_attr/mail` | Y `group_set_description`, `group_set_mail` | Y | PUT |
| Delegated management of one group (`entry_managed_by`) | Y set at create; later only by `idm_access_control_admins` | Y `group_set_entry_managed_by` | Y | PUT ⚠️ |
| OAuth2 clients (basic and public): create, origins, scope map, claim map, PKCE, secret, key rotate | Y `/v1/oauth2*` | Y `oauth2_rs_*` (about 35 functions) | Y `oauth2` | Application/OAuth2 attrs readable, PUT ⚠️ |
| Credentials: set password | P via credential-update session (`/v1/person/{id}/_credential/_update*`) | Y `person_account_primary_credential_set_password` (helper over the session) | Y | N |
| Credentials: passkeys, TOTP, backup codes | P: needs a WebAuthn ceremony on the user's device; wrapper can only issue a **credential-update intent link** (`/_credential/_update_intent`, can mail it) | Y `credential_update_passkey_*`, `_attested_passkey_*`, `_totp_*` | Y (CLI is the authenticator) | N |
| Credential status, remove credentials | Y `_credential/_status` | Y | Y | N |
| Sessions: list, revoke user auth tokens | Y `/v1/account/{id}/_user_auth_token[/{token_id}]` | Y `account_list_user_auth_token`, `_destroy_` | Y `person/service-account session` | N |
| Password policy per group (min length, credential type minimum, auth/privilege expiry, WebAuthn attestation CA list, search limits) | Y group attrs, class `account_policy` (`dl15/schema.rs`) | Y `group_account_policy_*` (14 functions) | Y `group account-policy` | PUT attrs ⚠️ |
| System password badlist, denied names | Y `/v1/system/_attr/...` | Y `system_*` | Y `system` | N |
| POSIX attrs, person | Y `/v1/person/{id}/_unix` (+ `_unix/_credential`) | Y `person_account_unix_extend`, `_unix_cred_put` | Y `person posix` | PUT `gidnumber`, `loginshell` ⚠️ |
| POSIX attrs, group | Y `/v1/group/{id}/_unix`, `/_unix/_token` | Y `group_unix_extend`, `group_unix_token_get` | Y `group posix` | PUT `gidnumber` ⚠️ |
| SSH public keys | Y `/v1/person/{id}/_ssh_pubkeys` | Y | Y | PUT `ssh_publickey` ⚠️ |
| Sync accounts (import from FreeIPA/LDAP) | Y `/v1/sync_account*`, `/scim/v1/Sync` | Y `sync_account_*`, `scim_v1_sync_*` | Y `sync` | Y, this is the original SCIM use |
| RADIUS secret, token | Y `/v1/person/{id}/_radius` | Y `account_radius_*` | Y | N |
| Domain settings (display name, LDAP basedn, image, recovery, signup) | Y `/v1/domain*` | Y `domain_*` | Y `domain` | N |
| Schema read | Y `/v1/schema*` | Y `schema_*` | Y (hidden) | Y `/scim/v1/Class`, `/Attribute` |
| Schema write (new attribute types and classes) | P `POST /v1/raw/create` as `idm_schema_admins` member; the typed schema routes are commented as "TODO" | P via `create()` raw | P hidden `raw` | N |
| Recycle bin list/revive | Y `/v1/recycle_bin*` | Y `recycle_bin_*` | Y | N |
| Account signup (new in 1.12), recovery by mail | ⚠️ domain settings; signup route not checked | Y `set_domain_allow_account_recovery` (signup ⚠️) | ⚠️ | N |

Notes: "SCIM PUT" works on any attribute the caller's access profile (ACP) allows, because the generic PUT is
class-agnostic (`resolve_scim_json_put`, `server/lib/src/server/scim.rs:371`). Rows marked ⚠️ in the SCIM column are
derived from that design, not tested.

---

## 3. Groups in depth

- **Attributes of class `group`** (`server/lib/src/migration_data/dl15/schema.rs:1140`): `name`, `spn`
  (generated, must), `member`, `description`, `mail`, `grant_ui_hint`. Supplementing classes: `posixgroup`
  (`gidnumber`), `account_policy` (the 8 policy attributes), `dyngroup` (`dyngroup_filter`, `dynmember`),
  `memberof` (back references, maintained by the server). Also `entry_managed_by` (via ACP). `idm_group_admins`
  can create and modify only `name`, `description`, `mail`, `member`, `entry_managed_by`
  (`IDM_ACP_GROUP_MANAGE_DL9`, `dl15/access.rs:1203`).
- **Nesting:** yes, unlimited depth in code (no explicit depth limit found in `plugins/memberof.rs`). A group is a
  member of another by listing its UUID in `member`. `memberof` is the transitive closure, `directmemberof` the one
  hop set (`plugins/memberof.rs`, `do_group_memberof`). The book states membership decisions use `memberof`
  (`book/src/accounts/groups.md`).
- **Cycles:** allowed and handled. The plugin iterates to a fixed point; tests `test_create_mo_cycle`,
  `test_modify_mo_add_cycle`, `test_delete_mo_cycle` (and multi-cycle variants). In a cycle every member group
  becomes `memberof` of every other **and of itself**. A hierarchy that must be a tree needs to be enforced by the
  wrapper, Kanidm will not reject a loop.
- **Reference integrity:** deleting a group removes dangling `member` references first (`refint` runs before
  `memberof`, comment at top of `memberof.rs`).
- **Limits:** search results default 1024 for normal accounts, effectively unlimited for API paths
  (`DEFAULT_LIMIT_SEARCH_MAX_RESULTS = 1024`, `DEFAULT_LIMIT_API_SEARCH_MAX_RESULTS`, `constants/mod.rs:206`).
  Filter limits: 32 elements, depth 12 (`DEFAULT_LIMIT_FILTER_*`). These can be set per group through account
  policy. I found no hard cap on the number of members. ⚠️ Performance with very large or deep graphs not measured;
  memberof recomputation walks affected sets and rewrites entries, so bulk edits of a heavily nested tree are costly.
- **Group naming:** the SPN is `name@domain`; names are unique; groups can be renamed (`group_rename`), UUID is stable.
  Use UUID as our key. Denied names list exists (`system_denied_names_*`).
- **Delegation per group:** `entry_managed_by` (a group or account) lets its members modify the group without new
  ACPs (`book/src/accounts/groups.md`). It is all-or-nothing; finer rights (read-only, add-only, remove-only) were
  requested in **kanidm#4641** (open, filed by FreeSynergy 2026-10-19), parked by the maintainer until the access
  control review **kanidm#4062** (open, last update 2026-04-07).
- **What can we store on a group?** Name, description, one or more mails, members, manager, UI hints, POSIX gid,
  account policy. **Nothing else**: a group has no free key/value field.
- **Custom attributes / schema extension:** not offered as a feature. The maintainer on kanidm#3493 ("Custom fields",
  open, 36 comments, 2026-06-24): the missing piece is "schema and access management", not the API; "I don't want
  to just open that door today". Technically a member of `idm_schema_admins` (default: `system_admins`) may create
  `attributetype` and `classtype` entries (`IDM_ACP_SCHEMA_WRITE_ATTRS_V1`, `dl15/access.rs:236`) through
  `/v1/raw/create`; the proto layer accepts unknown names (`Attribute::Custom`, `proto/src/attribute.rs:234`), and
  the book mentions "custom schema elements" needing reindex (`book/src/database_maintenance.md:33`). But:
  - group admins' ACP cannot add a class to an existing group, nor write unknown attributes; we would need our own
    ACP (`idm_access_control_admins`), a custom class that supplements `group`, and raw modify calls on the
    unstable `/v1/raw/*` and internal types. ⚠️ I did not try this end to end; the second half is inferred from the ACP
    lists. Schema is stated "not stable" in `support.md`, and the maintainer signalled he does not want it as a
    supported path.
- **Can our hierarchy be represented?**
  - *Fully in Kanidm:* membership graph (nested groups, cycles tolerated), effective membership, delegated manager,
    password policy and POSIX per group, OAuth2 scope and claim mapping per group (a group can grant scopes and
    claim values to an OAuth2 client, which is the closest thing to "per-group roles", see section 5).
  - *Only partly:* group type/kind (team vs. project vs. role), parent pointer as a first-class field, per-group
    roles, visibility rules (kanidm#4642 asks for min/max size and hidden groups; maintainer: later, with self
    group signup), per-group metadata, ordering, labels, ownership model with several permission levels.
  - *Recommended:* Kanidm holds **identity + membership + effective authorisation** only. Everything else about a
    group (kind, roles, parent, metadata) lives in a FreeSynergy store keyed by the Kanidm group **UUID**, and is
    projected into Kanidm as plain groups and nesting (for instance one Kanidm group per `(group, role)`, whose
    membership is derived by us). Then Kanidm can still answer "is X in Y" and apps can use `memberof`/OAuth2
    group claims without knowing about our model.

---

## 4. System access

Source: `unix_integration/`, `book/src/integrations/pam_and_nsswitch*.md`, `radius.md`, `ssh_key_distribution.md`,
`RELEASE_NOTES.md`.

| Component | What it does | Requirements | Platforms | Maturity |
|---|---|---|---|---|
| `kanidm-unixd` (crate `resolver_kanidm`, 1.x) | Local daemon: resolves and caches users/groups, caches credentials (optionally TPM-bound, `hsm_type`), creates homes (bind mount or symlink), caches `/etc/passwd`/`group`; talks to Kanidm with anonymous access or a service-account token (member of `idm_unix_authentication_read`) | Users/groups must have POSIX attrs (`gidnumber`); separate `kanidm-unixd-tasks` daemon is required; client and server within one minor version (`support.md`) | Linux full (tasks daemon is `cfg(target_os = "linux")` in `resolver_common/src/cli/tasks.rs`). FreeBSD: packaged (`pkg install kanidm-client`), documented PAM/NSS setup (`pam_and_nsswitch/freebsd.md`). macOS: ⚠️ only the CLI is packaged (Homebrew cask, `installing_client_tools.md`); 1.12 release note "Fix pam.h constants for FreeBSD/MacOS" suggests PAM modules compile, but there is no documentation for a macOS login integration. Windows: no PAM/NSS/unixd; only the `kanidm` CLI "built and tested", not packaged, a WebAuthn crash is open (kanidm#4367) | Production use by the project's own docs; cadence quarterly. Passkey/FIDO2 login over PAM still open (kanidm#1553, 26 comments) |
| NSS (`nss_kanidm`, new `nss_sparkle`) | Name service module that asks unixd | unixd running; must be first in `nsswitch.conf` (before `compat`/`files`) | Linux, FreeBSD (`files` instead of `compat`) | as above ⚠️ `sparkle` modules are new, purpose not documented in the book (grep found nothing) |
| PAM (`pam_kanidm`, `pam_sparkle`) | Authenticates against unixd: password (UNIX password set separately), MFA/TOTP prompts; account and session phases; home creation | Careful PAM config, backup `/etc/pam.d`. Password change through PAM "not yet supported" (FreeBSD doc) | Linux (Fedora, SUSE, Debian/Ubuntu packages), FreeBSD | as above |
| SSH keys | Accounts hold public keys (`/v1/person/{id}/_ssh_pubkeys`); `kanidm_ssh_authorizedkeys` (package `kanidm-unix-clients`) serves them to `sshd` via `AuthorizedKeysCommand`, with unixd cache | unixd for caching | Linux, FreeBSD | stable feature, all accounts can self-manage keys |
| RADIUS | `rlm_kanidm` (rewritten from Python to Rust in 1.11.0, `rlm_kanidm/`), FreeRADIUS module: PEAP/MSCHAPv2 with a **separate RADIUS secret** per account (stored in clear text by design, `radius.md`), EAP-TLS possible; access only for members of an allowed group; reader account in `idm_radius_servers`; service accounts cannot have a RADIUS secret | FreeRADIUS, container image provided by the project | Server side Linux/container | Works; the clear-text storage is a documented trade-off. kanidm#1637 (CA for VPN/RADIUS certs) open |
| LDAP (read-only) | Compatibility interface for apps; stable API (listed in `support.md`) | basedn set via domain config | any | stable |

Consequence for FreeSynergy: PAM/RADIUS are optional adapters we can switch on later; all of them read what the
wrapper already writes (POSIX attrs, SSH keys, groups). Neither requires wrapper code beyond setting those
attributes, and a machine-login feature should be offered only on Linux/FreeBSD hosts. For Windows and macOS desktops
plan on OAuth2/OIDC logins, not PAM. ⚠️ I did not install or run any of these components.

---

## 5. What Kanidm cannot do (that a group-based program needs)

Retrieved 2026-11-06 with `gh api search/issues` and issue reads. "Activity" = last update and comment count.

| Need | Kanidm status | Evidence / activity |
|---|---|---|
| Fine-grained delegation (read-only, add-only, remove-only manager) | Only all-or-nothing `entry_managed_by`; custom ACPs by `idm_access_control_admins` | #4641 open (2026-10-19, 3 comments, maintainer 2026-10-28: wait for #4062); #4062 access control review, open, last update 2026-04-07, 1 comment. Slow |
| Per-group roles | Not a concept. Nearest: OAuth2 scope map and claim map per group (`/v1/oauth2/{rs}/_scopemap/{group}`, `_claimmap`) and `grant_ui_hint` | No dedicated issue found ⚠️ (searched "role") |
| Custom group/person attributes | No | #3493 open since 2025-03, 36 comments, last 2026-06-24, maintainer reluctant; #256 "Business/Admin attributes" (2020) open |
| Min/max size, hidden groups, self group signup | No | #4642 open, 8 comments, 2026-10-29: "eventually but not soon" |
| Invitations / registration tokens | Account **signup** exists since 1.12 (per #4659 it is only fully open or fully closed); **credential reset intent tokens** exist for existing accounts; no invite tokens for new accounts | #4659 "Registration tokens", open, 2026-10-30, 7 comments, active discussion, no maintainer decision yet |
| Group federation between instances / trusts | No | #149 "Implement trusts" open since 2019, last update 2024-08, "We have other priorities" |
| Upstream OIDC login (Keycloak etc.) | Not usable yet | #4015 open, 2026-05-22: "very, very long time away" for the wider unixd goal; maintainer links it to #149 as "in progress, very early" (yaleman). ⚠️ I found no auth-source code on master |
| **OpenID Federation 1.0** (trust anchors, trust chains, trust marks) | No | `gh search` for "OpenID Federation" in open issues: the only hit is #2025 (SAML) which mentions it in passing; no dedicated issue. Matches ADR 0035 (we build it beside Kanidm) |
| SAML | No | #2025 open since 2023, last 2026-02-19; #4508 "Connect proxy e.g. SAML" |
| Dynamic client registration (RFC 7591) | No | #4095 open, maintainer sceptical; CIMD alternative in discussion #4499 |
| Outbound SCIM / provisioning to other systems | No | #4227 open, 2026-03-25 |
| Stable SCIM | Not yet | #4638 open; maintainer 2026-10-28 |
| Group-based multi-tenancy | No tenant concept; one domain per server. Mandates tenant separation by groups + OAuth2 scope maps | ⚠️ inferred from schema; ADR 0024 already plans tenants over OAuth2/SSO |
| Replication beyond 2 nodes | Max 2 nodes in a topology (`support.md`) | affects HA planning, not groups |

Overall activity: the lead maintainer answers fast (within days) and is deliberately conservative with schema,
access control and API shape. Features are queued behind an access control review (#4062) and schema design.
Planning on "Kanidm will add it soon" is not safe for anything in this table.

---

## 6. Wrapper design notes (one page)

**Keep the interface ours.** Define a FreeSynergy trait set per capability, in our vocabulary, not Kanidm's:
`Directory` (people, service accounts), `Groups` (create, move under a parent, add/remove member, effective
members, roles), `Clients` (OAuth2/OIDC registrations), `Credentials` (start enrolment, reset intent, sessions),
`Policy` (password, session), `Posix`. Types are ours (`GroupId` = Kanidm UUID, kinds, roles); the Kanidm adapter
maps them. Never expose Kanidm attribute names (`memberof`, `entry_managed_by`) or `kanidm_proto` types above the
adapter.

**Capability flags instead of version checks.** Each trait method group has a runtime capability entry:
`provider = kanidm | fs-native | none`, `since` and `verified_against` (Kanidm version). At start the adapter reads
`X-KANIDM-VERSION`, `/docs/v1/openapi.json` and `/scim/v1/Class` + `/Attribute`, and enables only what it can
prove exists. Unknown version: fall back to the last tested set and log. Pin Kanidm in the server bundle to one
minor, upgrade deliberately (upgrades are one minor at a time, `support.md`).

**Stay on the stable surface.** Use REST v1 with `v1::Entry` shapes as default; use `internal`/SCIM endpoints
behind a second, smaller adapter that can be replaced. Convert to SCIM later per capability by flipping the provider
in the capability entry, nothing above changes. Contract tests in CI against the pinned container and against
`master` (nightly, informational) give early warning of the "shape still changing" API.

**What we take over now.** Store in an FreeSynergy-owned database (keyed by Kanidm UUIDs): group kind, parent
pointer, roles, metadata, visibility, delegation levels, invitations. Project into Kanidm only what Kanidm can
express: plain groups, nesting, memberships, `entry_managed_by` where all-or-nothing is acceptable, OAuth2 scope or
claim maps for roles. Enforce tree shape and no-cycle rules ourselves (Kanidm accepts cycles). Make projection
idempotent and reconciling (desired state versus `GET /v1/group`), so a restore of Kanidm or manual edits heal.

**Kanidm absent (ADR 0024).** A program running alone uses a local `fs-native` provider that implements the same
traits over the local store: local persons, groups, memberships, and local OAuth2/SSO/SCIM endpoints as ADR 0024
requires. The program never calls Kanidm directly; the server bundle (Hub + Kanidm) simply registers the Kanidm
adapter as the provider. Moving from alone to server mode is an export/import across the same trait (UUIDs
preserved, `PUT`-able via `POST /v1/group` plus membership calls). Secrets (API token) belong in the key vault from
ADR 0024.

**Handing a capability back to Kanidm.** Each FS-owned feature has a one-line adapter flag and a data mapping:
1. Kanidm ships the feature (watch #4641/#4062 for delegation, #4659 for invites, #3493 for custom fields,
   #4015 for upstream OIDC). A release note or issue closure triggers a review, never an automatic switch.
2. Implement the Kanidm adapter for the trait, run the same contract tests against both providers.
3. Migrate data: write the FS-held values into Kanidm, verify with a read-back comparison, then flip
   `provider = kanidm` for that capability, keep the fs-native code as fallback for the standalone case (it must stay
   anyway).
4. Mark the FS-owned store read-only for that capability for one release, then remove the projection code.
Features Kanidm will probably never provide (OpenID Federation, ADR 0035; tenant concept) stay FS-native permanently.

**Pitfalls to design around.** (a) `kanidm_client` exits the process on version mismatch in debug builds. (b) SCIM
create is broken on master; do not depend on it. (c) Passkeys cannot be registered by a server-side wrapper, only
enrolment links can be issued. (d) The API token in use must be read-write and should have an expiry with rotation.
(e) `memberof` is recomputed on every membership write; batch changes per group. (f) Deleting a Kanidm entry
goes to the recycle bin first (`/v1/recycle_bin`), our delete semantics must account for revive.

---

### Sources (all retrieved 2026-11-06)
- Repo `https://github.com/kanidm/kanidm` at `8b5382f2037bcaf2bf84cb67e7e6353d73de173a`: `Cargo.toml`,
  `RELEASE_NOTES.md`, `book/src/support.md`, `book/src/supported_features.md`, `book/src/accounts/groups.md`,
  `book/src/accounts/account_policy.md`, `book/src/accounts/service_accounts.md`,
  `book/src/integrations/{pam_and_nsswitch.md,pam_and_nsswitch/freebsd.md,radius.md,ssh_key_distribution.md}`,
  `book/src/installing_client_tools.md`, `server/core/src/https/{v1.rs,v1_scim.rs,apidocs/mod.rs}`,
  `server/core/src/actors/v1_scim.rs`, `server/lib/src/server/scim.rs`, `server/lib/src/plugins/memberof.rs`,
  `server/lib/src/migration_data/dl15/{schema.rs,access.rs,groups.rs}`, `server/lib/src/constants/mod.rs`,
  `libs/client/src/*.rs`, `proto/src/{v1/mod.rs,scim_v1/*.rs,attribute.rs}`, `tools/cli/src/**`,
  `unix_integration/**`.
- crates.io API: `https://crates.io/api/v1/crates/kanidm_client` (versions, licence, MSRV).
- GitHub releases API: `repos/kanidm/kanidm/releases/latest` (v1.12.0, 2026-11-01).
- Issues: kanidm#4638, #4641, #4642, #4659, #4062, #3493, #4227, #4015, #4095, #149, #2025, #1553, #4367
  (`https://github.com/kanidm/kanidm/issues/<n>`).
- FreeSynergy ADRs: `conventions/decisions/0024-*.md`, `0035-*.md`.

### Not verified
Nothing was run against a live Kanidm. Unchecked: whether SCIM PUT on groups behaves as designed; whether the CLI
`--output json` covers all commands; that the dynamic-group ACP is not exposed to group admins; end-to-end custom
schema on groups; the macOS PAM/NSS status; the purpose of the `*_sparkle` modules; behaviour at very large group
graphs; the origin type of every REST endpoint (stable vs. internal class); the licence compatibility decision.

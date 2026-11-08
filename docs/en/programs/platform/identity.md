# Identity wrapper

## In short

Identity is meant to become the one place where signing in and access to systems are handled. We describe how it should behave, and Kanidm, an open identity server, does the work where it can. Today it is a small bridge, not yet a sign-in.

**Command:** `fs-identity`, one command per program with subcommands ([ADR 0063](../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- Kanidm never decides who belongs to what. [Groups](groups.md) decides, and Kanidm mirrors it.
- Kanidm sits behind our own interface. We take on what it cannot do and hand control back when it can.
- If you do not run Kanidm, all programs still run alone.
- Our own small client talks to Kanidm's REST interface, checked against Kanidm 1.12.0.

## Where it stands today

Latest tag: `v0.2.0`. The adapter creates, reads, updates, lists and removes groups in Kanidm so that they match Groups, and can be repeated safely. It ran once against a real Kanidm 1.12.0 container. There is no sign-in yet: no passwords, OAuth2 clients, SCIM, PAM or RADIUS. It cannot create invitations or grant rights in Kanidm. The name of the repository is provisional.

Signing in, and access to systems. We define how it behaves; Kanidm carries it out where it can.

**Status: only a Kanidm adapter for groups, `v0.2.0`; no sign-in yet.** Back to the [overall plan](../apps/roadmap.md). The repository name `fs-identity` is provisional. Details: 
[Kanidm research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md), source read
at Kanidm 1.13.0-dev (latest release 1.12.0), not run against a live server.

## Idea

Kanidm is remotely controlled behind our own [interface](../../interfaces/index.md). We take on what it cannot do, and
hand control back when it can (ADR 0047). If it is not there, programs still work alone (ADR 0024).

## How we control it

| Way | Use |
|-----|-----|
| **REST API v1** with a service-account token, through our own small Rust client | Default: it is the surface Kanidm's docs call stable, with an OpenAPI description |
| `kanidm_client` crate, pinned to the server version | Only for intricate flows such as login and passkey enrolment; not covered by the stability promise |
| SCIM | **Not yet**: stated as unstable, and generic creation of entries looks broken in the source |

This narrows ADR 0024, which planned to use Kanidm's SCIM behind our abstraction.

## Possibilities, not obligations

| What | State |
|------|-------|
| OAuth2, OIDC, passkeys | Yes |
| Login to machines via PAM and NSS (`kanidm-unixd`) | Linux and FreeBSD only |
| RADIUS | Exists; not examined in depth for us |
| Windows, macOS login | Not available or not established |

## Limits we take on

Invitations, fine-grained delegation, federation (OpenID Federation is not in Kanidm; ADR 0035). Passkeys cannot be
registered on the server's side; only enrolment links can be issued. See [groups](groups.md).

## Open

- Whether Kanidm's licence, MPL-2.0, raises any question: we call it over the network and do not link to it, but this has not been checked.
- Working with the Kanidm team, whose pace is slow and whose docs lag behind.

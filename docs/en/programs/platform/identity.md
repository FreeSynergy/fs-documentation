# Identity wrapper

Signing in, and access to systems. We define how it behaves; Kanidm carries it out where it can.

**Status: planned, no code yet (2026-11-06).** Back to the [overall plan](../apps/roadmap.md). Name still open. Details:
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

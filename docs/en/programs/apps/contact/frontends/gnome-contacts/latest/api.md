# GNOME Contacts - API Documentation

## Overview

GNOME Contacts itself has **no API** — the programmatic level is the **Evolution Data Server (EDS)** with its D-Bus/libebook interface, plus the protocols of the attached sources (CardDAV, LDAP, Google Contacts API). vCard files are the neutral exchange route.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| libebook / EDS D-Bus (`EBookClient`) | Read/write contacts | official (C/Vala; GObject introspection for Python/JS) |
| CardDAV/LDAP/Google contacts of the sources | Synchronisation | standard protocols |
| `.vcf` files | Import/export | official |
| REST | — | ❌ Not present |

## Authentication

EDS locally without auth; sources in the GNOME online-accounts dialog (OAuth2 Google, Basic CardDAV, simple bind LDAP), keys in the GNOME Keyring.

## libebook example (C, abridged)

```c
EBookClient *client;
e_book_client_connect_by_source(registry, source, &client, NULL);

ECVCard vcv; e_vcard_from_file("andrea.vcf", &vcv, NULL);
e_book_client_create_contact(client, E_CONTACT(&vcv), &uid, NULL);
```

- Sources = `ESource` entries; each source is an address book
- `e_book_client_get_view()` with an RFC-2426 search filter (`"fn=Andrea"`)

## Python/JS via GObject introspection

```python
gi.require_version('EBookClient', '1.2')
from gi.repository import EBookClient
```

## Exchange route for scripts

`⋮ → Export…` produces a `.vcf` batch → process further as you like; re-import via `⋮ → Import…`.

## Rate limits

Only those of the source servers (Google quotas, Nextcloud throttling).

## Skin note

A GNOME Contacts skin mirrors the card/fields mask; data-model bridge via EDS or `.vcf` → [Contact model](../../../../../../data/models.md).

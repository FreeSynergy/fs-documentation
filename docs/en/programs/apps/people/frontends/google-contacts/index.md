# Google Contacts

> Category: [people](../../index.md) · Type: contact manager (web, Android) · Vendor: Google · Licence: proprietary

## What it is

Google Contacts is the address book tied to a Google Account. It is used in a browser and is built into Android; the contacts sync to all devices signed in to the account. Contacts that are not saved yet are kept in a separate "Other contacts" group.

## Notable ideas

Why this program is documented here (ADR 0013):

- **Merge suggestions** ("Merge & fix"): the program finds duplicate entries of one person itself and offers to combine them one by one or all at once; merged contacts can be separated again. Relevant for us because duplicates are the main decay of any address book that imports from several sources.
- **Other contacts**: people you only wrote to are kept apart from the real address book until you promote them. This is a model for "known" versus "seen once".
- **Change history** per contact, so an edit can be undone.

## Documented versions

| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ from help pages only; the live interface was not inspected |

## Protocols and standards used

Contact data standards are described under [data/people](../../../../../data/people/index.md). Which protocols Google Contacts offers for third parties is listed in [api.md](latest/api.md) (Open).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources

| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.google.com/contacts/answer/7078226 ✅ | official help page (merge duplicates) | 2026-11-10 |
| https://support.google.com/contacts/answer/1069522 ✅ | official help page (adding contacts, sync, Other contacts, history) | 2026-11-10 |

# Apple Mail iOS 26 — Description

Documented on 2026-11-05 from screenshots (internal, not published, ADR 0038): iOS 26 on an
iPhone 17 Pro, plus current macOS Mail (same 2026 generation) for comparison, one image labelled
iOS 27, a few older iOS screenshots and macOS 10.12 images from 2016 (outdated, mentioned briefly).

✅ = seen in a screenshot · ⚠️ = inferred or known otherwise

## Overview
Apple Mail on iOS 26 uses Apple's translucent "glass" look: floating round buttons, a floating
search capsule at the bottom, large titles and card-shaped sheets ✅. The inbox is sorted into
categories with chips at the top ✅. Actions live in swipe gestures, long-press menus and bottom
sheets rather than in toolbars ✅.

## What it does
- Reads and writes mail for several accounts (iCloud and others) ✅.
- Sorts the inbox automatically into Primary, Transactions, Updates, Promotions ✅.
- Offers smart mailboxes (VIP, Flagged, Unread, To/Cc, Attachments, Remind Me, Follow Up, Send Later,
  Muted, thread notifications) next to real folders ✅.
- Protects against tracking (Protect Mail Activity) and against mis-addressing (Mark Addresses) ✅.
- Summarises a mail on request ("Summarize", Apple Intelligence) ✅.

## Who it suits
People who mostly read and triage on the phone; people who want the defaults to be private.

## Differentiation
### Apple Mail vs. Outlook
Fewer visible commands, more gestures; automatic categories instead of Focused/Other; privacy
protection by default; no ribbon, no right-pane reading on the phone ✅. Outlook has richer
organisation (categories with colours, rules, recall, offline control) ✅ (see
[Outlook](../../outlook/m365-2026-11/description.md)).

### iOS vs. macOS (current) ✅
The Mac version shows the same ideas in three columns: sidebar (Favourites with All Inboxes, VIPs,
Flagged, Remind Me, All Drafts, All Sent; Smart Mailboxes; account folders), list with category
tabs, reading pane with Summarize; a toolbar with reply, archive, delete, junk, move, flag, search;
a composer with a floating toolbar ✅. It may get its own version folder later (`macos-26`).

### Older states
- Older iOS (pre-2020 look): the same editable smart mailbox list existed (Inbox, VIP, Flagged,
  Unread, To/Cc, Attachments, Notifications, Today) ✅ — the idea is long-lived.
- macOS 10.12 (2016): settings with tabbed preferences (accounts, junk, fonts and colours, viewing,
  composing, signatures, rules), aliases per account and a From selector ✅ — outdated.
- The image labelled **iOS 27** shows five phone screens with a bottom tab bar (Inbox, Today,
  Attachments, Flagged, Search), a "Priority" card and a Today view mixing schedule and tasks ✅ seen,
  but it looks like a **concept**, not a confirmed Apple release ⚠️.

## Technical details
- Platforms: iOS, iPadOS, macOS, visionOS ⚠️; no web or Windows version ⚠️.
- Storage/sync: local copy of the IMAP mailboxes; settings sync through iCloud ⚠️.
- Encryption: S/MIME supported ⚠️; no OpenPGP built in ⚠️.
- Self-hosting: the client works with any IMAP server ✅ (account dialog accepts any address; older
  screenshots show a non-Apple provider) ✅.

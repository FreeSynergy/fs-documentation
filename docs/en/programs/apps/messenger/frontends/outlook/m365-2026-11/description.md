# Outlook m365-2026-11 — Description

Documented on 2026-11-05 from screenshots collected by the project owner (internal, not published,
ADR 0038). Microsoft shows no version number in the new Outlook; this folder describes the
**current Microsoft 365 release as of November 2026** ("new Outlook" for Windows and web, plus the
mobile app). Some screenshots show **classic Outlook** (the Win32 desktop program) or older web
states; those are marked as such.

✅ = seen in a screenshot · ⚠️ = inferred or known from elsewhere, not seen

## Overview
Outlook is Microsoft's mail and calendar client inside Microsoft 365. The current generation
("new Outlook") is the same web application on Windows and in the browser ✅; the mobile app
follows the same ideas in a phone layout ✅. Classic Outlook still exists next to it and differs in
menus (full ribbon, File backstage, Send/Receive tab) ✅.

## What it does
- Several mail accounts of different providers in one window — Microsoft 365, Outlook.com, Gmail,
  Yahoo, iCloud, IMAP ✅.
- Conversation list split into a "Focused" and an "Other" stream, with pinned mails on top and
  date groups (today, yesterday, this week) ✅.
- Time-based mail handling: schedule send, undo send, snooze ("remind again"), follow-up flags with
  reminders, recall a sent message ✅.
- Inline calendar handling: invitations answered in the reading pane, an "upcoming event" chip in the
  title bar, a full calendar module ✅.
- Offline mode with a chosen set of folders and days ✅ (new Outlook setting; classic Outlook has a
  "work offline" switch) ✅.
- AI assistant (Copilot) for summaries, writing help and generated themes ✅ — out of scope for us
  except as an idea list (see [features](features.md)).

## Who it suits
Office workers in organisations using Microsoft 365; people who live in mail and calendar together.
Many people have *learned* mail handling here — this is the "what everyone knows" reference frontend
of ADR 0038 ⚠️ (judgement).

## Differentiation
### Outlook vs. Apple Mail
Outlook is dense, toolbar-driven and desktop-first (ribbon, three panes, right-click menus); Apple Mail
is sparse, gesture-driven and phone-first (swipe actions, sheets, large titles). Both now sort the
inbox automatically (Focused/Other vs. categories) ✅.

### New Outlook vs. classic Outlook
New Outlook: simplified single-line ribbon, settings in one three-column dialog, web technology ✅.
Classic: full ribbon with many tabs, File backstage for account and profile settings, Send/Receive
groups, status bar with configurable counters, COM add-ins (third-party ribbons seen) ✅.

## Technical details
- Platforms: Windows app and browser (same UI) ✅, Android/iOS app ✅, classic Windows desktop ✅.
- Storage/sync: server-side mailbox (Exchange Online) with optional local offline copy ✅ (setting);
  sync protocol not visible ⚠️ (see [api](api.md)).
- Encryption: a sensitivity/protection control (shield icon) in the composer ✅; S/MIME and Microsoft
  Purview message encryption are known ⚠️.
- Self-hosting: no — Microsoft cloud only (Exchange Server on-premises exists ⚠️).

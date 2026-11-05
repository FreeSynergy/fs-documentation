# Outlook m365-2026-11 — Features

Describes the **foreign program**. Our implementation status lives only in
[requirements](../../../requirements.md) (ADR 0012). ✅ = seen in a screenshot · ⚠️ = not seen.
"classic" = seen only in classic Outlook.

## Main features

### Accounts
- Several accounts of different providers in one folder tree — Microsoft 365, Outlook.com, Gmail, Yahoo, iCloud, IMAP ✅
- "Add account" dialog that suggests accounts already known on the device, plus an advanced setup ✅
- Account settings in a backstage page: account settings, name and sync settings, delegate access, download the global address book, change/manage profiles, manage add-ins (classic) ✅
- Automatic replies (out of office), signatures, mobile devices, storage per account ✅ (settings list)
- Distribution groups managed from settings ✅ (settings list)

### Inbox and list
- Focused / Other split of the inbox ✅ (also on mobile ✅)
- Pin a mail to the top of the list (pinned group) ✅
- Date groups in the list (pinned, today, yesterday, this week, last month) ✅
- Conversation view with expand chevron per row ✅
- Unread shown by bold sender, blue subject and a blue bar on the left edge ✅
- Inline meeting chip with date and an RSVP button directly in the list row ✅
- Inline picture thumbnails in the list row (older web state) ✅
- Category tag shown in the row ✅; mention marker (@) in the row ✅
- Reaction counts in the row on mobile ✅
- "Internal"/"External" sender markers on mobile ✅
- Filter and sort buttons above the list ✅; selection mode toggle ✅
- Classic: All / Unread / Mentions quick filters ✅

### Reading
- Reading pane with sender, recipients, time, reply / reply all / forward icons ✅
- Contact presence dot on avatars ✅
- Reactions on received mails (emoji with count) ✅
- AI summary card on top of a long conversation, with feedback buttons ✅
- Calendar invitation answered in place: time, online meeting link, conflict check, "notify organiser" option, optional message, accept / tentative / decline / propose a new time ✅
- Read receipt tracking (seen as a disabled menu entry) ✅
- Celebration animations when a mail contains words like "congratulations" (can be turned off) ✅

### Writing
- Inline reply in the reading pane or a separate compose window ✅
- Send split button: send now or **schedule send** with two presets and a custom date/time picker ✅
- **Undo send**: delay of 0–10 seconds (slider), a bar at the bottom with "undo" while sending ✅
- Draft autosave with "draft saved at <time>" ✅
- Recipient chips with presence/validity mark; Cc/Bcc on demand ✅
- From selector per account ✅
- Formatting bar: font, size, bold, italic, underline, strikethrough, highlight, text colour, styles, paragraph spacing ✅
- Attach file, insert link, signature, high/low importance ✅
- Sensitivity / protection control (shield) ✅
- Grammar and style suggestions in a small popover (Editor) ✅
- Slash command in the body ("type / to insert files and more") ✅
- Dictation button, Loop components, apps/add-ins in the ribbon ✅ (seen as ribbon buttons)
- Address book lookup, check names (classic) ✅

### Organising
- Move to / copy to folder; archive; delete; sweep (clean up mails from a sender) ✅
- Categories with name and colour; create, edit, delete ✅
- **Categorised search folder**: starring a category puts a folder for it into Favourites ✅
- Favourites section on top of the folder tree ✅
- **Snooze** ("remind again"): later today, tomorrow, this weekend, next week, or a chosen date; snoozed mails collected in their own folder ✅
- **Follow-up flags**: today, tomorrow, this week, next week, no date, custom (start date, due date, reminder with time and sound), mark complete, clear flag (classic) ✅
- Quick Steps (one-click multi-step actions) ✅; Quick Actions on hover ✅ (menu entry "set quick actions", classic)
- Rules ✅; ignore conversation ✅; report / junk / block sender ✅
- Find related (same sender / conversation) ✅
- Recall a sent message (removes it from recipients' mailboxes inside the organisation, with a recall report mail) ✅
- Assign a retention policy; create a task from a mail ✅
- Send to OneNote, quick print (classic) ✅

### Offline and sync
- Offline setting: on/off, which folders (default + favourites), how many days (e.g. 30), include attachments ✅
- Classic: send/receive all folders, update folder, send all, send/receive groups, show progress, cancel all, download headers only, mark/unmark for download, work offline toggle, "offline mode" in the status bar ✅

### Notifications
- Per type on/off: mail (new mails, reactions, mentions), calendar (event reminders), documents (comments, edits, mentions) ✅
- Bell icon with a panel in the title bar ✅

### Appearance
- Mode light / dark / system ✅; picture themes and AI-generated themes ✅ (desktop and mobile)
- Density setting on mobile ✅; view settings: conversations, message preview, zoom, ribbon, folder pane, reading pane, density, immersive reader ✅

### Calendar (borrowed module, shown for context)
- Day / work week / week / month / split view, share, print ✅
- Weather and work location (office/home) per day ✅; join button on online meetings ✅
- Several calendars with colours (birthdays, holidays, personal) ✅

## What Outlook does NOT do
- No end-to-end encryption by default; no chat-style conversation view ⚠️
- Swipe actions on mobile are known but **not seen** ⚠️
- No self-hosting of the new Outlook ⚠️
- Recall only works inside the same organisation ⚠️

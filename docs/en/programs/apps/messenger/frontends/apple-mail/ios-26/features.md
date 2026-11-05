# Apple Mail iOS 26 — Features

Describes the **foreign program**. Our implementation status lives only in
[requirements](../../../requirements.md) (ADR 0012). ✅ = seen · ⚠️ = not seen.
(mac) = seen only in the current macOS version.

## Main features

### Inbox
- Automatic categories Primary, Transactions, Updates, Promotions as chips; the active chip shows its name ✅
- "About categories" sheet: what each category holds and how many mails were sorted last week ✅
- Show/hide categories, show contact photos (mac View menu) ✅
- Row: avatar or Memoji, sender, time, chevron, subject with emoji, two-line preview ✅; VIP star left of the row ✅; unread dot ⚠️ (not visible in the iOS 26 images)
- Subtitle under the title: account and "updated just now" ✅
- Mailing-list banner with unsubscribe ✅; "found in <mailbox>" label ✅

### Mailboxes
- Editable list of smart mailboxes with tick boxes and drag handles: Inbox, VIP, Flagged, Unread,
  To/Cc, Attachments, Thread notifications, Remind Me, Follow Up, Send Later, Muted threads ✅
- New mailbox (real folder) ✅; Smart Mailboxes defined by rules, e.g. "Today", "Family Pictures" (mac) ✅
- All Inboxes / All Drafts / All Sent across accounts (mac) ✅

### Reading
- Up/down arrows to the previous/next mail; back button with unread count ✅
- Summarize button on top of the mail ✅
- Header with avatar, sender, recipients (expandable), time and flag ✅
- Rich links in mails (map location card, guide card with "open in Maps") (mac) ✅

### Triage
- Swipe actions: More, Flag, Delete ✅ (left swipe)
- Action sheet: Reply, Reply All, Forward, Delete (large tiles); Remind Me; Unflag; flag colour row ✅
- Long-press preview with menu: reply, reply all, forward, Mark ›, Notify Me, Mute ✅
- Select mode → move to mailbox via a sheet with a stacked preview of the selection ✅
- Archive, junk, move, flag from the toolbar (mac) ✅

### Writing
- Composer with To, Cc, Subject, From, Signature, Image size, Message size (mac) ✅
- Floating toolbar: reply-mode, text format (Aa), emoji, writing tools ⚠️ (icon), header fields, attach ›, send later ⚠️ (clock-arrow icon) (mac) ✅
- Attach menu: files, include attachments, photos, take photo / scan documents / add sketch from a nearby iPad (mac) ✅
- Quoted reply marked with a coloured bar (mac) ✅
- Aliases per account and From selector (macOS 10.12) ✅
- Send Later and Remind Me (as mailboxes and sort keys) ✅

### Search
- Search capsule at the bottom with dictation ✅
- Scope: all mailboxes / current mailbox ✅
- Top results, then more/all results; matched words highlighted ✅
- Suggestions while typing ("subject contains …", completed phrases) (mac) ✅

### Contacts
- Contact card from a sender: Add to VIP, search mails of this contact, send message, share contact,
  add to favourites, add to list ✅; block contact ⚠️ (partly hidden)

### Privacy and safety
- Protect Mail Activity switch ✅
- Mark Addresses: highlight addresses outside given domains ✅

### Sort and view (mac View menu) ✅
- Sort by attachments, date, Remind Me, Send Later, flags, from, size, subject, to, unread; ascending/descending; inbox only / all mailboxes
- Filter; column layout; preview below; show date/time, To/Cc, size, contact photo, categories
- Highlight conversations; organise by conversation; expand / collapse all conversations

### Accounts
- Add account by e-mail address, or choose a provider from a list ✅

## What Apple Mail does NOT do
- No rules on iOS (rules exist on the Mac ⚠️ — seen as a preferences tab in macOS 10.12 ✅)
- No colour categories/labels beyond flag colours ✅ (only flags seen)
- No recall, no read receipts ⚠️
- No OpenPGP ⚠️; no web version ⚠️

# Outlook m365-2026-11 — UI states

✅ = seen in a screenshot · ⚠️ = inferred.

| State | Trigger | Next states |
|-------|---------|-------------|
| Online (normal) | default | offline, sending |
| Offline (new Outlook) | setting "offline" on; network lost ⚠️ | online — mails/calendar/people of the chosen folders and days stay readable ✅ |
| Work offline (classic) | ribbon button "work offline" ✅ | online; status bar shows "offline mode" ✅ |
| Send/receive in progress (classic) | "send/receive all folders" ✅ | done; cancelled ("cancel all") ✅; progress window ("show progress") ✅ |
| Draft saved | autosave while writing ✅ | sending; discarded |
| Sending, undo window | "Send" with undo delay > 0 ✅ | sent (after 0–10 s, user-set) ✅; back to draft ("undo") ✅ |
| Scheduled | "schedule send" with a time ✅ | sent at that time ⚠️; edited/cancelled ⚠️ |
| Sent | delay over | recall requested ✅ |
| Recall requested | "recall message" + confirm dialog ✅ | recall report mail arrives in the inbox ✅ |
| Snoozed | snooze with a time ✅ | back in the inbox at that time ⚠️; listed in a "snoozed" folder meanwhile ✅ |
| Flagged / follow-up | flag with due date and reminder ✅ | reminder fires ⚠️; completed ✅; cleared ✅ |
| Pinned | "pin" ✅ | unpinned ⚠️ |
| Unread / read | open, or "mark as unread" ✅ | — |
| Focused / Other | automatic sorting ✅; move between them ⚠️ | — |
| Invitation unanswered | meeting mail ✅ | accepted / tentative / declined / new time proposed ✅ |
| Notifications on/off per type | settings ✅ | — |
| Empty list / nothing selected | no selection | — (empty reading pane not seen ⚠️) |
| Settings dirty | change in settings dialog ✅ | saved / discarded ✅ |

Transitions are announced through a bottom bar with an action ("sending… undo") ✅ and through mails
(recall report) ✅.

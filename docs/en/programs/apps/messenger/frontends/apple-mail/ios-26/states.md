# Apple Mail iOS 26 — UI states

✅ = seen · ⚠️ = inferred.

| State | Trigger | Next states |
|-------|---------|-------------|
| Updated just now / updated n minutes ago | background or manual fetch ✅ | updating ⚠️ |
| Category filter active | tap a chip ✅ | other category; all ⚠️ |
| Row swiped open | swipe left ✅ | action done; closed |
| Selection mode | "Select" ✅ | move sheet ✅; cancel |
| Mailbox edit mode | "Edit" ✅ | Done ✅ |
| Message flagged (colour) | action sheet ✅ | unflagged ✅ |
| Remind Me set | action sheet ✅ | mail returns at the chosen time ⚠️; listed in "Remind Me" mailbox ✅ |
| Send Later queued | compose with a later time ⚠️ | sent; listed in "Send Later" mailbox ✅ |
| Follow up suggested | sent mail without answer ⚠️ | listed in "Follow Up" mailbox ✅ |
| Notify Me on a thread | long-press menu ✅ | notifications for replies ⚠️; off |
| Muted thread | long-press menu ✅ | unmuted ⚠️; listed in "Muted threads" ✅ |
| VIP sender | contact card ✅ | star shown in list ✅; VIP mailbox ✅ |
| Searching | type in search capsule ✅ | results (top / more) ✅; scope switched ✅ |
| No message selected (mac) | empty selection ✅ | — (large grey placeholder text) ✅ |
| Add account | dialog with address field, "continue" disabled until input ✅ | provider sign-in ⚠️ |
| Protect Mail Activity on/off | settings ✅ | — |

Undo: shake to undo / undo after delete ⚠️ (not seen). Undo send exists ⚠️ (known since iOS 16, not seen).

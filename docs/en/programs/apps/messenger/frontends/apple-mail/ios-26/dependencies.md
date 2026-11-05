# Apple Mail iOS 26 — Dependencies

Which of **our** components a frontend in this style needs. Names from `temp/messenger-components.md`;
**NEW** = not among our 84 components.

| Region / feature | Component | Level |
|------------------|-----------|-------|
| Large title + subtitle ✅ | `primitives/basics/heading` ⚠️ + `label` | primitive |
| Floating round buttons on glass ✅ | `primitives/actions/button` (round, translucent variant — change) | primitive |
| Category chips ✅ | `widgets/navigation/tabs` (chip variant) or `primitives/actions/button-group` | widget |
| Category explanation sheet ✅ | `widgets/overlays/drawer` + `widgets/containers/card` | widget |
| Message list rows ✅ | `widgets/data/list-view` + `widgets/data/avatar` | widget |
| VIP star in the margin ✅ | `primitives/feedback/badge` (icon variant) | primitive |
| Swipe actions (More / Flag / Delete) ✅ | `widgets/data/list-view` + `interactions/gestures/swipe/swipe` | widget + gesture |
| Long-press preview + menu ✅ | **NEW `peek-menu`** ⚠️ (preview card + `context-menu`) — or `context-menu` with a preview slot (change) | widget |
| Bottom bar: filter, search, compose ✅ | `primitives/fields/search-field` + `button` | primitive |
| Message view with next/previous ✅ | NEW `mail-view` + `button` | widget |
| Summary button ✅ | `button` (only if we offer summaries — open) | primitive |
| Action sheet (tiles + list + colours) ✅ | `widgets/overlays/drawer` + **NEW `action-tiles`** ⚠️ + **NEW `color-swatch-row`** ⚠️ | widget |
| Flag colours ✅ | `message.flag` with colour → `badge` colour variant | primitive |
| Move sheet with stacked preview ✅ | `widgets/overlays/drawer` + `widgets/data/tree-view` + **NEW `selection-stack`** ⚠️ | widget |
| Smart mailbox list, editable ✅ | `widgets/data/list-view` (check + drag-reorder — change) | widget |
| Contact card sheet ✅ | contacts program widget (borrowed, ADR 0020) | widget |
| Mailing-list banner with unsubscribe ✅ | `primitives/feedback/alert` + `button` | primitive |
| Search scope toggle ✅ | `primitives/actions/button-group` | primitive |
| Search results (top / more) ✅ | `widgets/data/list-view` with groups | widget |
| Dictation in search ✅ | platform input (shell), not a component ⚠️ | — |
| Settings switches (Protect Mail Activity, Mark Addresses) ✅ | app settings (`switch`, `tags-input`) | app |
| Add account sheet ✅ | `widgets/containers/wizard` | widget |
| Composer (mac) ✅ | NEW `composer` + `rich-text-editor` + `tags-input` (recipients) | widget |

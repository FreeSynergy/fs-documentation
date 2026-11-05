# Outlook m365-2026-11 — Dependencies

Which of **our** components a frontend in this style needs. Names from `temp/messenger-components.md`;
**NEW** = not among our 84 components. ✅/⚠️ refer to the Outlook feature being seen.

| Region / feature | Component | Level |
|------------------|-----------|-------|
| Window with 3–4 resizable panes ✅ | `widgets/containers/split-view` + app shell | widget / app |
| App rail (suite switcher) ✅ | `widgets/navigation/sidebar` (collapsed) — shell, not messenger | widget |
| Title bar search ✅ | `primitives/fields/search-field` | primitive |
| Upcoming-event chip in title bar ✅ | **NEW `next-event-chip`** (borrowed calendar widget, compact) | widget |
| Ribbon with tabs, split buttons ✅ | `widgets/navigation/toolbar` (ribbon variant) + `widgets/navigation/tabs` + **NEW `split-button`** ⚠️ (or `button-group` variant) | widget |
| Folder tree with favourites, counters ✅ | `widgets/data/tree-view` + `primitives/feedback/badge` | widget |
| Focused / Other ✅ | `widgets/navigation/tabs` | widget |
| Message list, date groups, pinned group ✅ | `widgets/data/list-view` (grouping with collapsible headers — change) | widget |
| Row with chips (RSVP, category, @) ✅ | `widgets/data/list-view` row + `primitives/feedback/badge` + borrowed calendar invite chip | widget |
| Reading pane ✅ | NEW `mail-view` | widget |
| HTML body | NEW `html-view` ⚠️ / `workbenches/special/embed` | workbench |
| AI summary card ✅ | `widgets/containers/card` (only if we offer summaries — open) | widget |
| Reactions on mails ✅ | NEW `reaction-bar` | widget |
| Presence dot ✅ | `widgets/data/avatar` | widget |
| Contact hover card ✅ | `widgets/overlays/hover-card` + contacts card widget | widget |
| Invitation response block ✅ | calendar program widget (borrowed) | widget |
| Composer inline / pop-out ✅ | NEW `composer` + `workbenches/fields/rich-text-editor` | widget/workbench |
| Recipients with chips ✅ | `primitives/fields/tags-input` (variant `recipients`) + `combobox` | primitive |
| Grammar popover ✅ | `widgets/overlays/popover` ⚠️ (only with a local checker) | widget |
| Schedule send / snooze / follow-up time ✅ | `widgets/fields/date-picker` + `widgets/fields/time-picker` + **NEW `time-preset-menu`** (later today / tomorrow / weekend / next week + custom) | widget |
| Undo-send bar ✅ | `primitives/feedback/toast` with action + countdown (change) | primitive |
| Undo delay slider ✅ | `primitives/fields/slider` ⚠️ | primitive |
| Context menus with submenus ✅ | `widgets/overlays/context-menu` | widget |
| Categories with colour ✅ | **NEW `category-chip`** ⚠️ (or `badge` colour variant) + settings list | primitive |
| Category / smart search folders ✅ | `tree-view` entry bound to a saved query (change) | widget |
| Rules ✅ | NEW `rule-editor` | widget |
| Offline settings ✅ | settings page (`switch`, `select`) | app |
| Offline / sync indicator ✅ (classic status bar) | **NEW `sync-state`** ⚠️ (or `badge`) | primitive |
| Settings dialog 3 columns ✅ | `widgets/overlays/modal` + `sidebar` + `field` | app |
| Add account dialog ✅ | `widgets/containers/wizard` | widget |
| Mobile bottom nav, floating new-mail button ✅ | `widgets/navigation/bottom-navigation` + **NEW `floating-action-button`** ⚠️ (or `button` variant) | widget |
| Mobile swipe actions ⚠️ | `list-view` + `interactions/gestures/swipe` | gesture |
| Theme picker with previews ✅ | settings page + `primitives/media/image` | app |

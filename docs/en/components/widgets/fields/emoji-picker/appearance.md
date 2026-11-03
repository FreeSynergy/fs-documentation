# Emoji Picker - Appearance

## Base layout
An emoji picker is an emoji selection for chat/comments.

```
┌─────────────────────────────────────────┐
│ [Smileys] [Faces] [Hands] ...           │  ← tabs
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
│  😊  😇  🙃  😁  😋  😛  😜  😝          │
│  🤪  😘  🤗  🤭  🫦  😙  🤤  😚          │
│  🥰  😗  😖  😞  😟  😬  😣  😪           │
│  🥱  😴  😷  🤒  🤕  🤢  🤮  🤧           │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **inline** | fixed below the input field, height limited, the list scrolls |
| **overlay** | flap with a shadow over the text, tabs on top |
| **reaktion** | one-row bar with 6–8 emojis and a "more…" button |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Default** | light | standard |
| **Active** | primary colour | active tab |
| **Hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | the shadow becomes stronger |

## Responsive

- The emoji grids scale with: 8 columns from 300 px, 6 columns on narrow devices.
- Category changes by `swipe`; the list keeps its scroll position per category.
- Below `small` screen width the picker becomes a bottom-anchored full surface with
  a fixed tab bar on top; the tiles stay at least 40 px large.

## Tabs

| Tab | Emojis |
|-----|--------|
| **Smileys** | 😀  😃  😄  ... |
| **Faces** | 🤪  😘  🤗  ... |
| **Hands** | ✌️  🤘  🙌  ... |
| **Animals** | 🐱  🐶  🐼  ... |
| **Food** | 🍔  🍕  🍫  ... |
| **Sports** | ⚽  🏀  🏈  ... |
| **Travel** | 🚗  🚀  ✈️  ... |

## Search

```
┌─────────────────────────────────────────┐
│ 🔍 Search...                            │
├─────────────────────────────────────────┤
│  😀  😃  😄  😁  😆  😅  🤣  😂          │
└─────────────────────────────────────────┘
```

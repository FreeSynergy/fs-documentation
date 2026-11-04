# Context Menu - Appearance

## Base layout
A context menu is opened by right-click or a long touch action.

```
┌─────────────────────────────────────────┐
│ 📋 Edit                                 │
│ 📄 Copy                                 │
│ 🗑️ Delete                               │
│ ─────────────────────                   │
│ 🔄 Refresh                              │
│ ℹ️ Properties                            │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Trigger | Appearance |
|---------|---------|------------|
| **Standard** | right-click (desktop) | menu at the pointer |
| **Long Press** | long touch action | menu above the object, full width on a narrow surface |
| **Overflow Menu** | click on three dots | menu below the button |

## Sizes

| Size | Width | Font size | Use |
|------|-------|-----------|-----|
| Small | 150px | 12px | few options |
| Medium | 200px | 14px | standard |
| Large | 250px | 16px | many options |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Active** | primary colour | active menu item |
| **Hover** | lighter | hover state |
| **Disabled** | grey | disabled options |
| **Danger** | red | dangerous actions |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `color` | the colour changes |
| `border-radius` | corners are rounded |

## Responsive

The menu unfolds away from the trigger point and switches sides when there is too little
space to the screen edge (`pop-in` from the respective corner). If it is taller than the
free space, it scrolls itself; the trigger point stays visible.

```css
.context-menu { position: fixed; min-width: 150px; max-height: 70vh; overflow: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2); animation: pop-in 120ms; }
.context-menu--flip-x { transform-origin: right top; }  /* no space on the right */
.context-menu--flip-y { transform-origin: left bottom; } /* no space below */
```

## Icons

| Icon | Meaning |
|------|---------|
| 📋 | edit |
| 📄 | copy |
| 🗑️ | delete |
| 🔄 | refresh |
| ℹ️ | information |

## Separator

```
┌─────────────────────────────────────────┐
│ Actions                                 │
│ ─────────────────────                   │
│ More actions                            │
└─────────────────────────────────────────┘
```

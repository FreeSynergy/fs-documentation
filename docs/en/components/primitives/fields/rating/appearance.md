# Rating - Appearance

## Base layout

A rating is a star or point evaluation.

## Variants

### Star rating

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆                                   │
└─────────────────────────────────────────┘
```

### Heart rating

```
┌─────────────────────────────────────────┐
│ ❤️❤️❤️❤️                                 │
└─────────────────────────────────────────┘
```

### Number rating

```
┌─────────────────────────────────────────┐
│ 4/5                                     │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 80px | inline |
| medium | 120px | standard |
| large | 160px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **filled** | gold | filled symbols |
| **empty** | grey | empty symbols |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `transform` | lifting |

## Responsive

- The symbols stay at least 24 px large; on touch devices the hit area per step grows
  to 44 px without the strip becoming wider.
- In narrow space the rating number slips below the strip instead of beside it.
- One tap is enough; `drag` across the strip allows fine adjustment, releasing confirms.

## With count

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (4.5)                            │
└─────────────────────────────────────────┘
```

## Read-only

```
┌─────────────────────────────────────────┐
│ ⭐⭐⭐⭐☆ (123 ratings)                    │
└─────────────────────────────────────────┘
```

# Pol.is - Structure and UI/UX

## Conversation layout

```
┌─────────────────────────────────────────────────────────────────┐
│ „What does our square need?“   [Your comment………]  [Send]       │
├───────────────┬─────────────────────────────────────────────────┤
│ Card stack    │  Opinion map (scatter, groups A/B/C)            │
│ „Free parking │   ●A  ●●B        ⌒ Consensus zone               │
│  fees“        │  ●C ●     ●A                                    │
│  [👍][👎][pass]│  Group chips: A=28% B=35% C=19%                 │
└───────────────┴─────────────────────────────────────────────────┘
```

## UI/UX

- Card-stack mechanic (like a dating app) lowers the barrier to participation considerably
- Group colours are consistent throughout; "important" flag for key cards

## Interactions

- Rate by click or keyboard buttons; comment editor with a character limit
- Live updates without reload (group counts shift)

## Responsive design

- Fully mobile-friendly (core goal: participation by phone)

## Accessibility

- Basic web; ratings also operable by keyboard (buttons are focusable)

## Performance

- Cluster computation takes seconds; very large conversations use card paging

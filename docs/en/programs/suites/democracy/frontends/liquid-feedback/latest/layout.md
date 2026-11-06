# LiquidFeedback - Structure and UI/UX

## Initiative: three-part layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Initiative LI-34 „Statute amendment §5“   Room: Programme        │
│ Phase: [Discussion] → Quorum 12/20 → Vote (until 12.11)          │
├────────────────┬─────────────────────┬───────────────────────────┤
│ Proposal (text)│ Arguments for/against│ Vote                     │
│ + amendment…   │  ▸ For 14 (traffic) │ ✓ Approval 22             │
│                │  ▸ Against 8        │ ○ Neutral 4               │
│                │                     │ ✗ Rejection 3             │
│                │                     │ Delegation graph ▽        │
└────────────────┴─────────────────────┴───────────────────────────┘
```

## UI/UX

- Text-heavy and tabular; status bars show phase and quorum progress
- Delegation management as a list (who votes for me, whom I give my vote to)

## Interactions

- Vote via radio button; delegation by clicking a person
- Argument rating (for/against/traffic light) instead of likes

## Responsive design

- Desktop-focused; readable on mobile but not built for meetings

## Accessibility

- Standard HTML tables; no special provisions documented

## Performance

- Organisation size (hundreds of active members) is not a problem

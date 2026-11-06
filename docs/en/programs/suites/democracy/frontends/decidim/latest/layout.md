# Decidim - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Organisation   Processes …            Log in | Register           │
├──────────────────────────────────────────────────────────────────┤
│ Process „Budget 2027“ — Phase: Prioritisation (until 15.11)      │
│ Tabs: Proposals | Meetings | Budgets | Results                    │
│ Proposal list: Title · Topic · Supports ✓128 · Comments 24       │
│ Detail: text, map, Support button, comment thread                │
└──────────────────────────────────────────────────────────────────┘
```

- Phase as a status banner; components as tabs; supports with a counter

## UI/UX

- Calm, institutional design (Tailwind system in newer versions), clear typography
- Moderation tools (report button) visible to participants

## Interactions

- Support with one click (verification required); comments with reply trees
- Admin forms in multiple steps (process wizard)

## Responsive design

- Fully responsive (mobile participation is a goal)

## Accessibility

- WCAG efforts documented (contrast, keyboard-operable forms)

## Performance

- Large processes (thousands of proposals) with topic filter; admin areas cache little

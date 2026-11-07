# Zapier - Structure and UI/UX

## Zap structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Zap "New tickets → CRM"         [Test] [Publish]  ⋮              │
├──────────────────────────────────────────────────────────────────┤
│ Step 1 Trigger   Zammad · New Ticket          [Test step]        │
│ Step 2 Action    Filter (only Priority ≥ high) [Test step]       │
│ ├─ Path A: condition "Customer exists"                           │
│ │   Step 3a Update Company                                       │
│ └─ Path B: otherwise                                             │
│     Step 3b Create Company                                       │
│ Step 4 Action    Slack notify                                    │
├──────────────────────────────────────────────────────────────────┤
│ Run history (234 runs) · Failed replay · Version v3              │
└──────────────────────────────────────────────────────────────────┘
```

- Vertical step chain with paths; each step has a field mapper on the left (sample record from the trigger)

## UI/UX

- Guided, form-fixed — little freeform (by design); sample data picker "Try again" for test data

## Interactions

- Click chains (step → app → event → map), no canvas dragging (paths as blocks)
- Replay of failed runs; version comparison

## Responsive design

- Web responsive; mobile app for zap management/approvals

## Accessibility

- Standard web forms; no canvas

## Performance

- Trigger latency = polling interval (typically 5–15 min, instant triggers where available); tasks are counted per action

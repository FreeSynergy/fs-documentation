# Helodesk - Structure and UI/UX

## Page structure

```
┌────────────────────────────────────────────────────────────────┐
│ Helodesk   [Contact Center][Cases][Contacts][Reports][⚙]       │
│ ┌ Softphone ──────────┐                                        │
│ │ 01 23 45 67 89  ☎   │  Case #4821 "Complaint"                │
│ │ Queues: Support (3) │  Channel: call · queue: support        │
│ └─────────────────────┘  [Status ▾][Owner ▾][Tags]             │
│                          ┌ Communication ───────────────────┐  │
│                          │ ☎ 09:12 call 2:31 (Anna)          │ │
│                          │ ✉ 09:40 reply to customer         │ │
│                          │ [New message / callback]          │ │
│                          └───────────────────────────────────┘ │
│                          Right: contact + history + KB         │
└────────────────────────────────────────────────────────────────┘
```

- The softphone panel is always present (top left), the case mask in the middle, the contact on the right

## UI/UX

- Modern SaaS design (violet accent), tight interlocking of call/case
- The screen pop automatically opens the context for dialled/incoming contacts

## Interactions

- **Click-to-dial** from any number (contact/case/phone book)
- **Transfer** by dragging the active call onto the agent list
- Chat/callback widgets embedded on customer websites (your own frontends there)

## Responsive design

- The web app is desktop-optimised; the agent app (iOS/Android) with softphone function; admin fully in the web

## Accessibility

- Form landscape of normal SaaS quality; call control additionally via keyboard in the softphone panel (numeric block)
- Screenreader: case details readable accessibly; live telephony status as text

## Performance

- The WebRTC softphone needs a stable network; QoS notes in the admin area

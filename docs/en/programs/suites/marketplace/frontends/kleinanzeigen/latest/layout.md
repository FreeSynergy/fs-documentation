# Kleinanzeigen - Structure and UI/UX

## App/web layout

```
┌──────────────────────────────────────────────────────────────┐
│ 🔍 Search…           [+ Ad]                 [Chat][Mine]     │
├──────────────────────────────────────────────────────────────┘
│ Category tiles · radius slider (radius map)                  │
│ Ad list: image · title · price · location+distance · date    │
│ Detail: gallery, description, "Write message",               │
│         location cluster on map, provider profile, safety    │
│ Chat: bubbles with system notices (safe payment / fraud)     │
└──────────────────────────────────────────────────────────────┘
```

## UI/UX

- app character (mobile-first), large buttons for ads/chat
- safety banner in chat (protection campaigns against grandparent scams)

## Interactions

- Ad creation as a multi-step assistant (category → photo → text → price/location)
- Search alerts as a permission dialog (push)

## Responsive design

- Web is responsive; the app is the main access route

## Accessibility

- standard app components; alt text for photos optional (recommended)

## Performance

- lists virtualized; map tiles cluster

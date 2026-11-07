# Node-RED - Structure and UI/UX

## Editor structure

```
┌──────────────────────────────────────────────────────────────────┐
│ ☰  Flow 1 ▾                    [Deploy]        🔍 Zoom/Grid ⌗   │
├───────────┬────────────────────────────────────┬─────────────────┤
│ Palette   │  Canvas (nodes + wires)            │ Info | Debug    │
│ inject    │   [inject]──→[function]──→[debug]  │ msg.payload=…   │
│ function  │      ↘ [http in]→[template]        │ Node docs       │
│ switch …  │                                    │ Config          │
│ (search)  │   [MQTT in]→[dashboard chart]      │ Dashboard       │
└───────────┴────────────────────────────────────┴─────────────────┘
```

- Palette on the left (click = node onto the canvas), canvas with grid, sidebar on the right (Info/Debug/Config/Dashboard)
- "Deploy" = live publishing of the flows (green nodes = deployed)

## UI/UX

- Plain, functional editor; node category colors; wires with arrows/"link" nodes for overviews
- Dark mode can be enabled

## Interactions

- **Drag/drop** nodes; click and drag = wiring; select nodes with `Shift`+click
- "Trigger node" for testing, debug side column as a stream
- Multi-user editing only via external synchronization (not built in)

## Responsive design

- Desktop tool; canvas impractical on mobile (viewing is fine)

## Accessibility

- Form/tab-oriented panels; canvas primarily mouse-based
- Keyboard: Ctrl+C/V/Z/S etc. (see [shortcuts.md](shortcuts.md))

## Performance

- Flows run in-process; split large messages (Base64 streams); keep `flows.json` under version control
